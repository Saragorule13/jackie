from llm import ask_llm

TOOL = [
    "open_chrome",
    "open_vscode",
    "open_calculator",
    "open_notepad"
]

def decide_tool(prompt):
    message = f""" 
    You are a tool router.

Available tools:
{TOOL}

Rules:
- Return ONLY the tool name.
- If no tool is needed, return NONE.
- Do not explain anything.

User request:
{prompt}
    """

    response = ask_llm(message)
    return response.strip()