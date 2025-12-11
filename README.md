# SkuleBot

A multi-agent course information assistant for UofT Engineering, powered by **LangGraph**, **LightRAG**, and **Neo4j**, with optional **Discord bot integration**.

SkuleBot provides grounded, interpretable retrieval over course syllabi, past exams, and curated topic maps. It exposes a FastAPI/ASGI backend for programmatic access and a Discord bot interface for student-facing deployment.

---

## 1. Features

### Backend (LangGraph + LightRAG)

* Multi-agent pipeline built using **LangGraph** (`router`, `classifier`, `topic_lookup`, `human fallback`).
* Graph-enhanced retrieval with **LightRAG** (entity extraction, relation extraction, dual-level retrieval).
* Neo4j integration for structured course and topic graph queries.
* Extensible state machine (`graph/state.py`).
* Custom nodes under `graph/nodes/*`.
* FastAPI endpoints for chat completion via `api.py`.
* Unified service wrapper in `service.py`.

### Discord Bot

* Lightweight wrapper around the backend via REST calls.
* Automatic routing of Discord queries → Intent detection → SkuleBot response.
* Runs in a dedicated virtual environment under `discord_bot/`.

---

## 2. Project Structure

```
SkuleBot/
├── api.py                # FastAPI endpoints
├── main.py               # ASGI entrypoint (backend)
├── service.py            # Low-level backend service wrappers
├── course_list.py        # Static utilities for course codes
├── graph/
│   ├── state.py
│   ├── router.py
│   ├── classifier.py
│   ├── nodes/
│       ├── human.py
│       ├── therapist.py
│       └── topic_lookup/
├── discord_bot/
│   ├── discord_bot.py
│   └── discord_env/
├── LightRAG/             # Vendor repo with local modifications
├── utils/
│   ├── lightrag_client.py
│   ├── kg_client.py
│   ├── scrape.py
│   └── topic_map.py
├── Dockerfile
└──  requirements.txt         
```

---

## 3. Installation

### 3.1 Clone the Repository

```bash
git clone https://github.com/qinshirl/SkuleBot.git
cd SkuleBot
```

### 3.2 Python Environment

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

---

## 4. Environment Configuration

Create a `.env` file in the project root:

```
OPENAI_API_KEY=...
NEO4J_URI=bolt://127.0.0.1:7687
NEO4J_USERNAME=...
NEO4J_PASSWORD=...
NEO4J_DB=...
LIGHTRAG_WORKSPACE=default
```

(Optional) If Neo4j is on Docker or remote, adjust the URI accordingly.

---

## 5. Running the Backend

### 5.1 Start the ASGI Server

```bash
uvicorn main:app --reload
```

You should see:

```
INFO:     Uvicorn running on http://127.0.0.1:8000
```

### 5.2 Test the /chat Endpoint

```bash
curl -X POST http://127.0.0.1:8000/chat \
  -H "Content-Type: application/json" \
  -d '{"message": "Tell me about ECE110"}'
```

Sample output:

```json
{
  "response": "ECE110 covers electrical fundamentals..."
}
```

---

## 6. Backend Architecture

### 6.1 Overall Architecture

![SkuleBot State Machine](images/state_machine.png)

### 6.2 LightRAG Integration

Located in: `utils/lightrag_client.py`.

Key features used:

* Entity-chunk extraction
* Relation detection
* Dual-retrieval (entity search + text search)
* Multi-hop graph walk → improves syllabus/exam lookup

**Example:**

```python
from utils.lightrag_client import rag

await rag.ainsert("ECE100 midterm solutions...")
result = await rag.aquery("Tell me topics in ECE100")
```

---

## 7. Inserting Local Markdown Files into LightRAG

### Automatic Folder Insert

If you extend your current helper (e.g., in `main_raw.py`):

```python
import os

async def insert_folder(rag, folder):
    for filename in os.listdir(folder):
        full = os.path.join(folder, filename)
        if os.path.isfile(full) and full.endswith((".md", ".txt")):
            with open(full, "r", encoding="utf8") as f:
                text = f.read()
            await rag.ainsert(text)
```

Usage:

```python
await insert_folder(rag, "./LightRAG/inputs")
```

---

## 8. Discord Bot Setup

### 8.1 Create a Bot on Discord Developer Portal

1. Visit [https://discord.com/developers/applications](https://discord.com/developers/applications)
2. Create a new Bot
3. Enable **MESSAGE CONTENT INTENT**
4. Copy the **Bot Token** into a `.env` under `discord_bot/`:

```
DISCORD_BOT_TOKEN=...
BACKEND_URL=http://127.0.0.1:8000/chat
```

### 8.2 Install Bot Dependencies

```bash
cd discord_bot
source discord_env/bin/activate
pip install discord.py python-dotenv requests
```

### 8.3 Running the Bot

```bash
python discord_bot.py
```

## 9. Docker Deployment

### 9.1 Build

```bash
docker build -t skulebot-backend .
```

### 9.2 Run

```bash
docker run -p 8000:8000 \
  --env-file .env \
  skulebot-backend
```

---

## 10. Adding New Nodes or Skills

All nodes live under:

```
graph/nodes/
```

To add a new node:

1. Create `graph/nodes/<name>.py`
2. Add handler logic (async, returns Dict)
3. Register in `router.py` based on routing intent
4. Update state machine in `main.py`

---

## 11. Neo4j Integration

Neo4j instance is automatically consumed through:

```python
from utils.kg_client import Neo4jClient
```

---
## 12. PDF to markdowm
use dolphin to convert
https://github.com/bytedance/Dolphin

Feng, H., Wei, S., Fei, X., Shi, W., Han, Y., Liao, L., … & others. (2025). *Dolphin: Document Image Parsing via Heterogeneous Anchor Prompting*. arXiv preprint [arXiv:2505.14059](https://arxiv.org/abs/2505.14059).

### Instructions
```text
git clone https://github.com/ByteDance/Dolphin.git
cd Dolphin
pip install -r requirements.txt   (use python 3.11)
pip install huggingface_hub
huggingface-cli download ByteDance/Dolphin-1.5 --local-dir ./hf_model
python demo_page.py --model_path ./hf_model --save_dir ./results \
    --input_path (our pdf file)
```
---


## 13. Troubleshooting

### LightRAG creates empty graph files

Delete the workspace:

```bash
rm -rf LightRAG/rag_storage/*
```

### Neo4j authentication errors

Verify `.env` credentials and Neo4j Browser connectivity.

### Discord bot not receiving messages

Ensure MESSAGE CONTENT INTENT is enabled in the Developer Portal.

---



---

## 14. License

This project uses the LightRAG license for all components under `LightRAG/` and a standard MIT license for SkuleBot’s original code.
