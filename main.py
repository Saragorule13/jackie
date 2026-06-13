import os
import sys

class C:
    """ANSI escape codes for terminal colors."""
    RESET   = "\033[0m"
    BOLD    = "\033[1m"
    DIM     = "\033[2m"
    CYAN    = "\033[96m"
    GREEN   = "\033[92m"
    YELLOW  = "\033[93m"
    RED     = "\033[91m"
    MAGENTA = "\033[95m"
    BLUE    = "\033[94m"

# Enable ANSI colors on Windows
os.system("")

# ── Imports ────────────────────────────────────────────────────────────
from tools import open_app, open_website
from router import decide_tool
from llm import ask_llm
from voice.stt import record_audio, transcribe_audio
from voice.tts import speak

# ── Helpers ────────────────────────────────────────────────────────────
ASSISTANT_NAME = "jackie"
EXIT_COMMANDS = {"exit", "quit", "bye", "stop", "goodbye"}


def print_banner():
    """Display a styled startup banner."""
    banner = f"""
{C.CYAN}{C.BOLD}╔══════════════════════════════════════════╗
║          🎤  JACKIE  —  Voice AI         ║
╚══════════════════════════════════════════╝{C.RESET}
{C.DIM}  Say "exit" or "bye" to quit.{C.RESET}
"""
    print(banner)


def user_prompt():
    """Show the input prompt and wait for ENTER."""
    print(f"{C.DIM}{'─' * 44}{C.RESET}")
    input(f"  {C.YELLOW}⏎  Press ENTER and speak...{C.RESET}")


def show_user(text):
    """Print what the user said."""
    print(f"  {C.GREEN}You ▸{C.RESET}  {text}")


def show_jackie(text):
    """Print Jackie's response."""
    print(f"  {C.CYAN}{ASSISTANT_NAME} ▸{C.RESET}  {text}")


def show_action(icon, text):
    """Print an action being performed."""
    print(f"  {C.MAGENTA}{icon}{C.RESET}  {text}")


def show_error(text):
    """Print an error message."""
    print(f"  {C.RED}✗  {text}{C.RESET}")


# ── Tool handlers ─────────────────────────────────────────────────────
def handle_open_app(decision):
    target = decision["target"]
    show_action("🚀", f"Launching {C.BOLD}{target}{C.RESET}...")
    speak(f"Opening {target}")
    result = open_app(target)
    show_jackie(result)


def handle_open_website(decision):
    target = decision["target"]
    show_action("🌐", f"Opening {C.BOLD}{target}{C.RESET}...")
    speak(f"Opening {target}")
    result = open_website(target)
    show_jackie(result)


def handle_chat(query):
    show_action("💬", "Thinking...")
    response = ask_llm(query)
    show_jackie(response)
    speak(response)


HANDLERS = {
    "open_application": handle_open_app,
    "open_website":     handle_open_website,
}


# ── Main loop ─────────────────────────────────────────────────────────
def main():
    print_banner()

    while True:
        try:
            user_prompt()

            audio_file = record_audio()
            query = transcribe_audio(audio_file).strip().lower()

            if not query:
                show_jackie("I didn't catch that. Try again?")
                continue

            show_user(query)

            if query in EXIT_COMMANDS:
                show_jackie("Goodbye! 👋")
                speak("Goodbye!")
                break

            # Route the query
            decision = decide_tool(query)
            tool = decision.get("tool", "NONE")

            handler = HANDLERS.get(tool)
            if handler:
                handler(decision)
            else:
                handle_chat(query)

        except KeyboardInterrupt:
            print(f"\n\n  {C.DIM}Interrupted.{C.RESET}")
            show_jackie("Goodbye! 👋")
            break
        except Exception as e:
            show_error(f"Something went wrong: {e}")
            continue


if __name__ == "__main__":
    main()