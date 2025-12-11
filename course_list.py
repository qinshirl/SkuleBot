from typing import Dict, Any, List

from graph.state import State
from utils.kg_client import run_query


def course_list_node(state: State) -> dict:
    courses = state.get("suggested_courses") or []
    if not courses:
        print("[course_list] No suggested_courses in state.")
        return {}

    codes = [c.get("code") for c in courses if c.get("code")]
    if not codes:
        print("[course_list] No valid course codes in suggested_courses.")
        return {}

    query = """
    MATCH (c:Course)-[:HAS_EXAM]->(e:Exam)
    WHERE c.code IN $codes
    RETURN c.code AS code, count(e) AS exam_count
    """
    records = run_query(query, {"codes": codes})

    exam_map: Dict[str, int] = {rec["code"]: rec["exam_count"] for rec in records}

    # Attach exam_count to each course dict (default 0)
    enriched: List[Dict[str, Any]] = []
    for c in courses:
        code = c.get("code")
        enriched.append(
            {
                **c,
                "exam_count": exam_map.get(code, 0),
            }
        )

    print("[course_list] Enriched suggested_courses with exam_count:", exam_map)

    return {"suggested_courses": enriched}
