FROM ghcr.io/hkuds/lightrag:v1.4.9.8
COPY prompt.py /app/lightrag/prompt.py
COPY operate.py /app/lightrag/operate.py
COPY lightrag.py /app/lightrag/lightrag.py