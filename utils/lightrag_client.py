# treating LightRAG as a retriever.


from __future__ import annotations

import os
from typing import Any, Dict, List

import requests
###############################################################################################
LIGHTRAG_BASE_URL = os.getenv("LIGHTRAG_URL", "http://localhost:9621")
###############################################################################################

class LightRAGError(Exception):


def _build_query_payload(
    query: str,
    mode: str = "mix",
    top_k: int | None = None,
) -> Dict[str, Any]:
    payload: Dict[str, Any] = {
        "query": query,
        "mode": "mix",  # naive, local, global, mix
        "include_references": True,
        "include_chunk_content": True,
    }
    if top_k is not None:
        payload["top_k"] = top_k
    return payload


def query_raw_chunks(
    query: str,
    mode: str = "mix",
    top_k: int | None = None,
    timeout: float = 60.0,
) -> Dict[str, Any]:

    url = f"{LIGHTRAG_BASE_URL}/query"
    payload = _build_query_payload(query=query, mode=mode, top_k=top_k)

    try:
        resp = requests.post(url, json=payload, timeout=timeout)
    except Exception as e:
        raise LightRAGError(f"Failed to connect to LightRAG server at {url}: {e}")

    if resp.status_code != 200:
        raise LightRAGError(
            f"LightRAG returned {resp.status_code}: {resp.text[:500]}"
        )

    try:
        data = resp.json()
    except Exception as e:
        raise LightRAGError(f"Failed to parse LightRAG JSON response: {e}; body={resp.text[:500]}")

    references = data.get("references", []) or []

    snippets: List[Dict[str, Any]] = []
    for ref in references:
        file_path = ref.get("file_path")
        ref_id = ref.get("reference_id")
        chunks = ref.get("content") or []
        for chunk in chunks:
            if not isinstance(chunk, str):
                continue
            snippets.append(
                {
                    "file_path": file_path,
                    "reference_id": ref_id,
                    "text": chunk,
                }
            )

    return {
        "snippets": snippets,
        "raw_response": data.get("response"),
        "raw_references": references,
    }
