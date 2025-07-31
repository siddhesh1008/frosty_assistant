┌──────────────────────────────────────────────┐
│                Frontend (React)              │
│   - Chat UI, voice button, task panel        │
│   - Webcam panel (future)                    │
└───────────────┬──────────────────────────────┘
                │  WebSocket/REST API
┌───────────────▼──────────────────────────────┐
│                Backend API (FastAPI)         │
│   - Session, user prefs, routing             │
│   - Receives: text, audio, tasks             │
└───────────────┬──────────────────────────────┘
                │
     ┌──────────▼──────────┐
     │  Wake Word/Audio    │
     │  (LiveKit+STT+TTS)  │
     └──────────┬──────────┘
                │
        ┌───────▼───────────┐
        │   Brain Router    │
        │ - Classifies query│
        │ - Chooses Handler │
        │ - Selects AI      │
        └───────┬───────────┘
                │
    ┌───────────▼─────────────┐
    │  Decision Making Model  │
    │  (Rule/AI based, Cohere)│
    └────┬─────┬─────┬────────┘
         │     │     │
 ┌───────▼┐ ┌──▼───┐ ┌▼────────┐
 │General │ │Realtime││Automation│
 │Handler │ │Handler ││Handler   │
 └──┬─────┘ └────┬──┘ └────┬────┘
    │            │         │
 ┌──▼────────────▼─────────▼───┐
 │      AI Provider Layer      │
 │  (pluggable, auto-fallback) │
 │  ┌───────────────┐          │
 │  │ OpenAI API    │          │
 │  ├───────────────┤          │
 │  │ Cohere API    │          │
 │  ├───────────────┤          │
 │  │ Local LLM     │          │
 │  └───────────────┘          │
 └────────────┬────────────────┘
              │
     ┌────────▼────────┐
     │ Integrations    │
     │ (Home, APIs,   │
     │  Reminders, etc)│
     └────────────────┘
