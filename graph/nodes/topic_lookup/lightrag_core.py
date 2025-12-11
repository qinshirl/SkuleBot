import os
import glob
from dotenv import load_dotenv

from lightrag import LightRAG, QueryParam
from lightrag.llm.openai import gpt_4o_mini_complete, openai_embed
from lightrag.utils import setup_logger
from lightrag.kg import shared_storage
from lightrag.kg.shared_storage import initialize_pipeline_status


load_dotenv()

setup_logger("lightrag", level="INFO")

WORKING_DIR = os.getenv("WORKING_DIR")
WORKSPACE = os.getenv("LIGHTRAG_WORKSPACE", "default")
shared_storage._default_workspace = WORKSPACE

import lightrag
print("[DEBUG] lightrag from:", lightrag.__file__, "workspace:", WORKSPACE)


_has_inserted_test_files = False


async def dummy_llm(prompt: str):
    return {"text": ""}


async def get_rag() -> LightRAG:
    rag = LightRAG(
        working_dir=WORKING_DIR,
        embedding_func=openai_embed,
        llm_model_func=gpt_4o_mini_complete,
        ####################################################################
        graph_storage="Neo4JStorage",
        ####################################################################
    )

    print("[LightRAG] Initializing storages...")
    await rag.initialize_storages()
    await initialize_pipeline_status()
    print("[LightRAG] Storages initialized.")

    return rag

# test insert single files
# async def insert_test_files(rag: LightRAG):
#     global _has_inserted_test_files
#     if _has_inserted_test_files:
#         return
#
#     FILES = [
#         "/Users/qinshirl/PycharmProjects/SkuleBot/LightRAG/inputs/ece100s_2001_exam.md",
#         "/Users/qinshirl/PycharmProjects/SkuleBot/LightRAG/inputs/ECE110H1_2024_TT2.md"
#     ]
#
#     for path in FILES:
#         if os.path.exists(path):
#             print(f"[LightRAG] Inserting test file: {path}")
#             with open(path, "r", encoding="utf8") as f:
#                 text = f.read()
#                 await rag.ainsert(text)
#         else:
#             print(f"[LightRAG] File missing, skipping: {path}")
#
#     _has_inserted_test_files = True
#     print("[LightRAG] Finished inserting test files.")





async def insert_test_files(rag: LightRAG, folder_path: str):
    global _has_inserted_test_files
    if _has_inserted_test_files:
        return

    patterns = [
        "*.md",
        "*.txt",
        "*.pdf",
    ]

    files = []
    for pattern in patterns:
        files.extend(glob.glob(os.path.join(folder_path, pattern)))

    if not files:
        print(f"[LightRAG] No files found in folder: {folder_path}")
    else:
        print(f"[LightRAG] Found {len(files)} files to insert from {folder_path}")

    for path in files:
        print(f"[LightRAG] Inserting: {path}")

        try:
            if path.lower().endswith(".pdf"):
                print(f"[LightRAG] WARNING: skipping PDF (no text extraction): {path}")
                continue

            with open(path, "r", encoding="utf8") as f:
                text = f.read()

            await rag.ainsert(text)

        except Exception as e:
            print(f"[LightRAG] ERROR reading {path}: {e}")

    _has_inserted_test_files = True
    print("[LightRAG] Finished inserting folder files.")


async def lightrag_retrieve(query: str):


    rag = await get_rag()
    # await insert_test_files(rag)
    await insert_test_files(
        rag,
        "/Users/qinshirl/PycharmProjects/SkuleBot/LightRAG/inputs/"
    )

    result = await rag.aquery(
        query,
        param=QueryParam(
            mode="hybrid",
            only_need_context=True,
        ),
    )

    return {
        "raw": result,
    }
