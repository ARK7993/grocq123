def simple_planner(prompt: str):
    if "calculate" in prompt.lower() or any(char.isdigit() for char in prompt):
        return "math", {"expression": prompt}
    elif "search" in prompt.lower() or "what is" in prompt.lower():
        return "search", {"query": prompt}
    else:
        return "echo", {"text": prompt}
