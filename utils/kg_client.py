# graph/nodes/topic_lookup/kg_client.py
import os
from neo4j import GraphDatabase

NEO4J_URI = os.getenv("NEO4J_URI", "neo4j://127.0.0.1:7687")
NEO4J_USER = os.getenv("NEO4J_USER", "neo4j")
NEO4J_PASSWORD = os.getenv("NEO4J_PASSWORD", "password")

driver = GraphDatabase.driver(NEO4J_URI, auth=(NEO4J_USER, NEO4J_PASSWORD))


def run_query(query: str, params: dict or None = None):
    params = params or {}
    with driver.session(database=os.getenv("NEO4J_DB", "test0ece110")) as session:
        result = session.run(query, **params)
        return [record.data() for record in result]
