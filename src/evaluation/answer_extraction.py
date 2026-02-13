"""Extract, normalize, and compare \\boxed{} answers."""

from __future__ import annotations

import logging
import re
from typing import Optional

logger = logging.getLogger(__name__)


# ---------------------------------------------------------------------------
# Extraction
# ---------------------------------------------------------------------------

_BOXED_RE = re.compile(r"\\boxed\{")


def extract_boxed_answer(text: str) -> Optional[str]:
    """Extract the content of the *last* ``\\boxed{...}`` in *text*.

    Handles nested braces correctly.  Returns ``None`` if no boxed answer
    is found.
    """
    # Find the *last* occurrence so we get the final answer
    matches = list(_BOXED_RE.finditer(text))
    if not matches:
        return None

    m = matches[-1]
    start = m.end()  # right after the opening '{'
    depth = 1
    i = start
    while i < len(text) and depth > 0:
        if text[i] == "{":
            depth += 1
        elif text[i] == "}":
            depth -= 1
        i += 1
    if depth != 0:
        return text[start:i].strip()
    return text[start: i - 1].strip()


# ---------------------------------------------------------------------------
# Normalization
# ---------------------------------------------------------------------------

def normalize_answer(answer: str) -> str:
    """Normalize an answer string for comparison.

    Steps:
    1. Strip whitespace
    2. Remove trailing period
    3. Remove enclosing $ signs
    4. Normalize common LaTeX patterns
    5. Lower-case for string comparison
    """
    s = answer.strip()
    # Remove enclosing $ ... $
    if s.startswith("$") and s.endswith("$"):
        s = s[1:-1].strip()
    # Remove trailing period
    s = s.rstrip(".")
    # Normalize some LaTeX
    s = s.replace("\\,", "")        # thin space
    s = s.replace("\\;", "")        # medium space
    s = s.replace("\\!", "")        # negative thin space
    s = s.replace("\\quad", " ")
    s = s.replace("\\qquad", " ")
    s = s.replace("\\text{", "").replace("\\mathrm{", "").replace("\\mathbf{", "")
    # Remove \left and \right
    s = s.replace("\\left", "").replace("\\right", "")
    # Collapse whitespace
    s = re.sub(r"\s+", " ", s).strip()
    return s


# ---------------------------------------------------------------------------
# Comparison
# ---------------------------------------------------------------------------

def compare_answers(predicted: str, ground_truth: str) -> bool:
    """Compare two answers, trying symbolic equivalence first then string match.

    Returns True if the answers are considered equivalent.
    """
    pred_norm = normalize_answer(predicted)
    gt_norm = normalize_answer(ground_truth)

    # 1. Exact string match (after normalization)
    if pred_norm.lower() == gt_norm.lower():
        return True

    # 2. Try numeric comparison
    try:
        pred_val = _to_float(pred_norm)
        gt_val = _to_float(gt_norm)
        if pred_val is not None and gt_val is not None:
            return abs(pred_val - gt_val) < 1e-6
    except Exception:
        pass

    # 3. Try sympy symbolic equivalence
    try:
        return _sympy_equal(pred_norm, gt_norm)
    except Exception:
        pass

    return False


def _to_float(s: str) -> Optional[float]:
    """Try to parse a string as a float. Handles fractions like 3/7."""
    s = s.strip()
    try:
        return float(s)
    except ValueError:
        pass
    # Try fraction
    if "/" in s:
        parts = s.split("/")
        if len(parts) == 2:
            try:
                return float(parts[0].strip()) / float(parts[1].strip())
            except (ValueError, ZeroDivisionError):
                pass
    return None


def _sympy_equal(a: str, b: str) -> bool:
    """Use sympy to check symbolic equivalence."""
    import sympy
    from sympy.parsing.latex import parse_latex

    try:
        expr_a = parse_latex(a)
        expr_b = parse_latex(b)
    except Exception:
        # If LaTeX parsing fails, try sympify
        try:
            expr_a = sympy.sympify(a)
            expr_b = sympy.sympify(b)
        except Exception:
            return False

    try:
        diff = sympy.simplify(expr_a - expr_b)
        return diff == 0
    except Exception:
        return False
