import os

class Chatbot:
    """
    Handles general conversational AI functionality for Frosty.
    Supports OpenAI, Cohere, and local LLMs (HuggingFace).
    """

    def __init__(self, provider: str = "openai", local_model_name: str = "distilgpt2"):
        """
        provider: 'openai', 'cohere', or 'local'
        local_model_name: model for local LLM (HuggingFace)
        """
        self.provider = provider
        self.local_model_name = local_model_name
        self.openai_api_key = os.getenv("OPENAI_API_KEY")
        self.cohere_api_key = os.getenv("COHERE_API_KEY")
        self.local_pipe = None  # For caching HuggingFace pipeline

    def get_response(self, prompt: str) -> str:
        """
        Gets a full response from the selected provider.
        """
        if self.provider == "openai":
            return self._openai_response(prompt)
        elif self.provider == "cohere":
            return self._cohere_response(prompt)
        elif self.provider == "local":
            return self._local_response(prompt, self.local_model_name)
        else:
            return "Unknown provider."

    def get_response_stream(self, prompt: str):
        """
        Streams chunks of the response (only supported for OpenAI for now).
        """
        if self.provider == "openai":
            yield from self._openai_response_stream(prompt)
        else:
            yield "Streaming not supported for this provider."

    def _openai_response(self, prompt: str) -> str:
        try:
            from openai import OpenAI
            client = OpenAI(api_key=self.openai_api_key)
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are Frosty, a helpful AI assistant."},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=128,
                temperature=0.3,
            )
            reply = response.choices[0].message.content
            return reply
        except Exception as e:
            return f"OpenAI API error: {str(e)}"

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

    def _cohere_response(self, prompt: str) -> str:
        try:
            import cohere
            co = cohere.Client(self.cohere_api_key)
            response = co.chat(
                message=prompt,
                model='command-r-plus',  # or 'command' depending on your plan
                temperature=0.3,
                max_tokens=128
            )
            return response.text
        except Exception as e:
            return f"Cohere API error: {str(e)}"

    def _local_response(self, prompt: str, model_name: str = "distilgpt2") -> str:
        try:
            from transformers import pipeline
            if (self.local_pipe is None or
                self.local_pipe.model.config._name_or_path != model_name):
                self.local_pipe = pipeline(
                    "text-generation",
                    model=model_name,
                    max_new_tokens=128
                )
            result = self.local_pipe(prompt)
            return result[0]['generated_text']
        except Exception as e:
            return f"[Local LLM error] {str(e)}"