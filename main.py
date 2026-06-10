from tools import execute_tool
from router import decide_tool
from llm import ask_llm
from tools import(
    open_chrome
)

print("Siri is listening...")
print("Type exit to quit.\n")

while True:

    query = input("You: ").strip().lower()

    if query in ["exit", "quit", "bye"]:
        print("Siri: Goodbye!")
        break
    
    tool = decide_tool(query)
    if tool != "NONE":
        result = execute_tool(tool)
        print(f"Siri: {result}\n")
        continue

    response = ask_llm(query)

    print(f"{response}\n")
