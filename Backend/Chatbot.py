import os

class Chatbot:
    """
    Handles general conversational AI functionality for Frosty.
    Supports OpenAI, Cohere, and local LLMs.
    """

    def __init__(self, provider: str = "openai"):
        self.provider = provider
        self.openai_api_key = os.getenv("OPENAI_API_KEY")

    def get_response_stream(self, prompt: str):
        """
        Yields response chunks as they're generated from OpenAI.
        """
        if self.provider == "openai":
            yield from self._openai_response_stream(prompt)
        else:
            yield "Streaming not supported for this provider."

    def _openai_response_stream(self, prompt: str):
        try:
            from openai import OpenAI
            client = OpenAI(api_key=self.openai_api_key)

            stream = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are Frosty, a helpful AI assistant."},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=128,
                temperature=0.3,
                stream=True
            )

            for chunk in stream:
                if chunk.choices[0].delta.content is not None:
                    yield chunk.choices[0].delta.content
        except Exception as e:
            yield f"OpenAI API streaming error: {str(e)}"