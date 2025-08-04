import os

class TextToSpeech:
    """
    Handles text-to-speech (TTS) for Frosty using ElevenLabs API.
    """

    def __init__(self, provider: str = "elevenlabs"):
        self.provider = provider
        self.api_key = os.getenv("ELEVENLABS_API_KEY")

    def speak(self, text: str, voice: str = "Jessica") -> None:
        if self.provider == "elevenlabs":
            try:
                from elevenlabs.client import ElevenLabs
                from elevenlabs import play
                client = ElevenLabs(api_key=self.api_key)
                voices_obj = client.voices.get_all()
                voices = voices_obj.voices

                # Find voice ID by name (case-insensitive)
                voice_id = None
                for v in voices:
                    if hasattr(v, "name") and v.name.lower() == voice.lower():
                        voice_id = v.voice_id
                        break
                if not voice_id:
                    # Fallback to first available voice
                    voice_id = voices[0].voice_id

                audio_gen = client.text_to_speech.convert(
                    voice_id=voice_id,
                    model_id="eleven_multilingual_v2",
                    text=text
                )
                audio_bytes = b"".join(audio_gen)  # <--- Join chunks before playing!
                play(audio_bytes)
            except Exception as e:
                print(f"[TTS] ElevenLabs error: {e}")
        else:
            print("[TTS] Only ElevenLabs provider is implemented here.")
