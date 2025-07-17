from planner import simple_planner
from tools import run_tool

class Agent:
    def __init__(self, name="Tinga"):
        self.name = name
        self.memory = []

    def run(self, prompt):
        self.memory.append({"user": prompt})
        tool, args = simple_planner(prompt)
        result = run_tool(tool, args)
        self.memory.append({"agent": result})
        return result
