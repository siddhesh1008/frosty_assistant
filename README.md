# FROSTY – Personal AI Assistant

**FROSTY** is an open, modular AI assistant inspired by JARVIS, designed for Linux home servers with a modern web interface. It leverages the power of Cohere, OpenAI, and Local LLMs for chat, classification, and automation—ready for future expansion (voice, vision, coding, smart home, and more).

---

## 🚀 Architecture Overview

┌──────────────────────────────────────────────┐
│ Frontend (React) │
│ - Chat UI, voice button, task panel │
│ - Webcam panel (future) │
└───────────────┬──────────────────────────────┘
│ WebSocket/REST API
┌───────────────▼──────────────────────────────┐
│ Backend API (FastAPI) │
│ - Session, user prefs, routing │
│ - Receives: text, audio, tasks │
└───────────────┬──────────────────────────────┘
│
┌──────────▼──────────┐
│ Wake Word/Audio │
│ (LiveKit+STT+TTS) │
└──────────┬──────────┘
│
┌───────▼───────────┐
│ Brain Router │
│ - Classifies query│
│ - Chooses Handler │
│ - Selects AI │
└───────┬───────────┘
│
┌───────────▼─────────────┐
│ Decision Making Model │
│ (Rule/AI based, Cohere)│
└────┬─────┬─────┬────────┘
│ │ │
┌───────▼┐ ┌──▼───┐ ┌▼────────┐
│General │ │Realtime││Automation│
│Handler │ │Handler ││Handler │
└──┬─────┘ └────┬──┘ └────┬────┘
│ │ │
┌──▼────────────▼─────────▼───┐
│ AI Provider Layer │
│ (pluggable, auto-fallback) │
│ ┌───────────────┐ │
│ │ OpenAI API │ │
│ ├───────────────┤ │
│ │ Cohere API │ │
│ ├───────────────┤ │
│ │ Local LLM │ │
│ └───────────────┘ │
└────────────┬────────────────┘
│
┌────────▼────────┐
│ Integrations │
│ (Home, APIs, │
│ Reminders, etc)│
└────────────────┘


---

## 🧩 Main Components

- **Frontend (React):**  
  - Tech-inspired, modern UI (chat, mic, tasks, webcam, settings)
- **Backend (FastAPI, Python):**  
  - API server, manages sessions, logic, and integrations
- **Wake Word/Audio Layer:**  
  - Always-listening, wake word (e.g., Porcupine), speech-to-text (STT), text-to-speech (TTS), LiveKit for real-time audio
- **Brain Router & Decision Model:**  
  - Routes each user query to the correct handler using rule-based or AI-based classification (Cohere, LLM)
- **Handlers:**  
  - **General:** Small talk, facts, info  
  - **Realtime:** Web queries, news, dynamic info  
  - **Automation:** Smart home, reminders, plugins, coding, etc.
- **AI Provider Layer:**  
  - Unified access to OpenAI, Cohere, and local LLMs (configurable, auto-fallback)
- **Integrations:**  
  - Easy plugin system for external services (Home Assistant, calendar, coding, etc.)

---

## ⚡️ Design Principles

- **Modular:** Swap/extend any part (AI, UI, tasks, voices)
- **Future-proof:** Ready for vision, AR, coding, multi-modal extensions
- **Open:** Supports local, open-source, and cloud AI providers
- **Accessible:** Web-based, works from any device (PC, tablet, phone)

---

## 🛠️ Getting Started

> **Work in progress!**  
> Folder structure, setup scripts, and detailed docs will follow as modules are implemented.

---

## 🤖 Features Roadmap

- [x] Modular web frontend (React)
- [x] Flexible backend with multi-AI support
- [ ] Voice interaction with wake word & live audio (LiveKit)
- [ ] Task & smart home integrations
- [ ] Webcam/AR/vision support
- [ ] Plugin marketplace

---

## 📁 Example Folder Structure

frosty/
│
├── frontend/ # React web app (UI)
├── backend/ # FastAPI server
│ ├── brain/ # Router, handlers, decision model
│ ├── ai_providers/ # OpenAI, Cohere, Local LLM adapters
│ ├── integrations/ # Plugins: smart home, web, tasks
│ ├── audio/ # Wake word, STT, TTS, LiveKit
│ └── utils/
├── data/ # Storage (history, settings)
├── docs/ # Documentation, diagrams
└── README.md


---

## 📚 Credits & Inspirations

- [LiveKit.io](https://livekit.io)
- [Cohere AI](https://cohere.com)
- [OpenAI](https://openai.com)
- [Open-source LLMs (Ollama, LM Studio, etc.)](https://ollama.com)

---

**FROSTY is your open, extensible, private AI assistant. Ready for next-gen interaction.**

