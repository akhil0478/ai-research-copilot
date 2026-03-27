# backend/orchestrator.py

def run_pipeline(user_input):
    state = {}

    # Temporary placeholders (until agents are built)
    state["query"] = user_input
    state["papers"] = []
    state["summaries"] = []
    state["gaps"] = []
    state["citations"] = []

    return state