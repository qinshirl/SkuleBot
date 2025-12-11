from neo4j import GraphDatabase
import os

NEO4J_URI = os.getenv("NEO4J_URI", "bolt://localhost:7687")
NEO4J_USER = os.getenv("NEO4J_USER", "neo4j")
NEO4J_PASSWORD = os.getenv("NEO4J_PASSWORD", "password")

driver = GraphDatabase.driver(NEO4J_URI, auth=(NEO4J_USER, NEO4J_PASSWORD))


def run_query(query: str, params: dict = None):
    params = params or {}
    with driver.session() as session:
        result = session.run(query, **params)
        return [record.data() for record in result]
