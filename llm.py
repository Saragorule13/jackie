# user query -> ollama -> response is wat we doim here

from ollama import chat
from ollama import ChatResponse

def ask_llm(prompt):
    response: ChatResponse = chat(model='qwen3:8b', messages=[
        {
            "role": "user",
            "content": prompt,
        },
    ])

    return response.message.content