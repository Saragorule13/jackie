import subprocess


def open_chrome():
    subprocess.Popen(
        r"C:\Program Files\Google\Chrome\Application\chrome.exe"
    )
    return "Opening Chrome..."


def open_vscode():
    subprocess.Popen("code")
    return "Opening VS Code..."


def open_calculator():
    subprocess.Popen("calc")
    return "Opening Calculator..."


def open_notepad():
    subprocess.Popen("notepad")
    return "Opening Notepad..."


def execute_tool(tool_name):
    
    tool_map = {
        "open_chrome": open_chrome,
        "open_vscode": open_vscode,
        "open_calculator": open_calculator,
        "open_notepad": open_notepad
    }

    if tool_name in tool_map:
        return tool_map[tool_name]()
    else:
        return "Tool not found."