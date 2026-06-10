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
    
    if "open chrome" in query:
        print(f"Jackie: {open_chrome()}")
        continue
    

    response = ask_llm(query)

    print(f"{response}\n")
