"""Python interpreter tool — execute code in a subprocess with timeout."""

from __future__ import annotations

import logging
import subprocess
import sys
import textwrap
from typing import Optional

logger = logging.getLogger(__name__)

# Preamble injected before every code execution to pre-import useful modules.
_PREAMBLE = textwrap.dedent("""\
    import math
    import sympy
    from sympy import *
    import numpy as np
    from fractions import Fraction
    import itertools
    import functools
    import collections
""")


class PythonInterpreter:
    """Execute Python code in an isolated subprocess and capture output.

    Features:
    - Configurable timeout (default 30 s)
    - Pre-imports sympy, math, numpy, fractions, itertools
    - Returns (stdout, error) tuple — error is None on success
    - Gracefully handles timeouts and syntax errors
    """

    def __init__(
        self,
        timeout: int = 30,
        allowed_modules: Optional[list[str]] = None,
    ) -> None:
        self.timeout = timeout
        self.allowed_modules = allowed_modules  # reserved for future sandboxing

    def execute(self, code: str) -> tuple[str, Optional[str]]:
        """Run *code* in a subprocess and return (stdout, error).

        Args:
            code: Python source code to execute.

        Returns:
            A tuple of (stdout_text, error_text). *error_text* is ``None``
            when execution succeeds.
        """
        full_code = _PREAMBLE + "\n" + code

        logger.debug("Executing code (%d chars, timeout=%ds)", len(code), self.timeout)

        try:
            result = subprocess.run(
                [sys.executable, "-c", full_code],
                capture_output=True,
                text=True,
                timeout=self.timeout,
            )
        except subprocess.TimeoutExpired:
            logger.warning("Code execution timed out after %ds", self.timeout)
            return "", f"Execution timed out after {self.timeout} seconds."
        except Exception as exc:
            logger.exception("Unexpected error running subprocess")
            return "", f"Subprocess error: {exc}"

        stdout = result.stdout.strip()
        stderr = result.stderr.strip()

        if result.returncode != 0:
            # Return the traceback so the model can see and fix the error
            error_msg = stderr if stderr else f"Process exited with code {result.returncode}"
            logger.debug("Code execution failed: %s", error_msg)
            return stdout, error_msg

        logger.debug("Code execution succeeded, stdout=%d chars", len(stdout))
        return stdout, None
