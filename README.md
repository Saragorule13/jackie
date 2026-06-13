# Jackie - Local AI Desktop Assistant

Jackie is a local AI-powered desktop assistant that uses Large Language Models (LLMs) to understand natural language commands, perform desktop automation, and interact through voice. The assistant runs entirely on-device using Ollama and Faster-Whisper, providing a privacy-focused and offline-capable experience.

## Features

* Local LLM inference using Ollama
* AI-powered intent routing
* Voice command support using Faster-Whisper
* Voice responses using Text-to-Speech (TTS)
* Desktop application launching through natural language
* Website opening through natural language commands
* Dynamic application registry with alias support
* Privacy-first, fully local execution
* Offline-capable architecture
* Modular and extensible design

## Tech Stack

### AI

* Ollama
* Qwen
* Faster-Whisper

### Backend

* Python

### Automation

* subprocess
* webbrowser

### Audio

* sounddevice
* scipy
* pyttsx3

## Installation

### Clone Repository

```bash
git clone https://github.com/Saragorule13/jackie.git
cd jackie
```

### Create Virtual Environment

```bash
python -m venv .venv
```

### Activate Environment

**Windows**

```bash
.venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Install Ollama

Download and install Ollama.

Pull the model:

```bash
ollama pull qwen3:8b
```

### Run Jackie

```bash
python main.py
```

## Example Commands

### Application Launching

```text
Open Chrome
Open Spotify
Open VS Code
Open Discord
Open Steam
```

### Website Launching

```text
Open GitHub
Open YouTube
Open LeetCode
```

### General Questions

```text
What is binary search?
Explain operating systems.
How does merge sort work?
```

## Current Capabilities

* Understands voice commands
* Converts speech to text locally
* Uses an LLM for intent understanding
* Launches installed applications
* Opens websites
* Answers general questions
* Responds using synthesized speech
* Runs entirely on-device

## Roadmap

### Completed

* [x] Local LLM Integration
* [x] AI Routing
* [x] Voice Input (Speech-to-Text)
* [x] Voice Output (Text-to-Speech)
* [x] Application Launcher
* [x] Website Launcher
* [x] Dynamic App Registry
* [x] Alias-Based Application Resolution

### Planned

* [ ] Wake Word Detection ("Hey Jackie")
* [ ] Memory System
* [ ] Retrieval-Augmented Generation (RAG)
* [ ] File & Folder Operations
* [ ] Screen Understanding
* [ ] Browser Automation
* [ ] Plugin Architecture

## Why Jackie?

Most AI assistants rely heavily on cloud APIs and external services. Jackie is designed as a local-first assistant that prioritizes privacy, offline functionality, and extensibility while serving as a foundation for a fully capable AI desktop assistant.

## Future Vision

Jackie aims to evolve into a personal AI operating layer capable of:

* Voice-based interaction
* Long-term memory
* Knowledge retrieval from personal documents
* Browser automation
* Desktop automation
* Multimodal understanding

## Author

**Sara Gorule**

GitHub: https://github.com/Saragorule13
