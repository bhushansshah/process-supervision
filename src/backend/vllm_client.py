"""Async client wrapping vLLM's OpenAI-compatible API."""

from __future__ import annotations

import logging
from typing import AsyncIterator, Optional

import httpx

from src.config import GenerationConfig, ModelConfig

logger = logging.getLogger(__name__)


class VLLMClient:
    """Lightweight async wrapper around vLLM's /v1/chat/completions endpoint."""

    def __init__(self, model_config: ModelConfig, timeout: float = 120.0) -> None:
        self.model_config = model_config
        self._client = httpx.AsyncClient(
            base_url=model_config.api_base,
            headers={"Authorization": f"Bearer {model_config.api_key}"},
            timeout=httpx.Timeout(timeout),
        )

    async def generate(
        self,
        messages: list[dict],
        generation_config: GenerationConfig,
        extra_stop: Optional[list[str]] = None,
    ) -> str:
        """Send a chat completion request and return the full response text.

        Args:
            messages: OpenAI-format message list.
            generation_config: Sampling parameters.
            extra_stop: Additional stop sequences beyond those in the config.

        Returns:
            The assistant's response text.
        """
        stop = list(generation_config.stop_sequences)
        if extra_stop:
            stop.extend(extra_stop)

        payload = {
            "model": self.model_config.effective_name,
            "messages": messages,
            "temperature": generation_config.temperature,
            "top_p": generation_config.top_p,
            "max_tokens": generation_config.max_tokens,
            "stop": stop if stop else None,
        }

        logger.debug("Request payload (model=%s): %d messages", self.model_config.effective_name, len(messages))

        resp = await self._client.post("/chat/completions", json=payload)
        resp.raise_for_status()
        data = resp.json()

        choice = data["choices"][0]
        text: str = choice["message"]["content"]
        finish_reason: str = choice.get("finish_reason", "unknown")

        logger.debug("Response finish_reason=%s, length=%d chars", finish_reason, len(text))
        return text

    async def generate_stream(
        self,
        messages: list[dict],
        generation_config: GenerationConfig,
        extra_stop: Optional[list[str]] = None,
    ) -> AsyncIterator[str]:
        """Stream tokens from the model (SSE). Yields text chunks."""
        stop = list(generation_config.stop_sequences)
        if extra_stop:
            stop.extend(extra_stop)

        payload = {
            "model": self.model_config.effective_name,
            "messages": messages,
            "temperature": generation_config.temperature,
            "top_p": generation_config.top_p,
            "max_tokens": generation_config.max_tokens,
            "stop": stop if stop else None,
            "stream": True,
        }

        import json as _json

        async with self._client.stream("POST", "/chat/completions", json=payload) as resp:
            resp.raise_for_status()
            async for line in resp.aiter_lines():
                if not line.startswith("data: "):
                    continue
                data_str = line[len("data: "):]
                if data_str.strip() == "[DONE]":
                    break
                chunk = _json.loads(data_str)
                delta = chunk["choices"][0].get("delta", {})
                if "content" in delta:
                    yield delta["content"]

    async def close(self) -> None:
        await self._client.aclose()

    async def __aenter__(self) -> "VLLMClient":
        return self

    async def __aexit__(self, *exc) -> None:
        await self.close()
