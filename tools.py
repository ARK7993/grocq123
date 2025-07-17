def math_tool(expression):
    try:
        return str(eval(expression))
    except:
        return "Error in calculation."

def search_tool(query):
    return f"Search result for '{query}' [simulated]"

def echo_tool(text):
    return f"You said: {text}"

def run_tool(tool_name, args):
    if tool_name == "math":
        return math_tool(args["expression"])
    elif tool_name == "search":
        return search_tool(args["query"])
    elif tool_name == "echo":
        return echo_tool(args["text"])
    else:
        return "Tool not found."
