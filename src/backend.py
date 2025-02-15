import json
import os
from groq import Groq

class AI:
    def __init__(self):
        self.client = Groq(
            api_key="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",
        )
        self.system_prompt = "You are a kind and professional mental health expert. Respond with empathy and support."
        self.history_file = "chat_history.json"
        self.model_name = "llama-3.3-8b"  # ✅ Use a smaller model to avoid hitting token limits

    def _load_history(self):
        """Load chat history, but keep only the last 5 messages to avoid exceeding API limits."""
        if os.path.exists(self.history_file):
            with open(self.history_file, "r") as f:
                messages = json.load(f)
                return messages[-5:]  # ✅ Keep only the last 5 messages
        return []

    def _save_history(self, messages):
        """Save chat history to a file."""
        with open(self.history_file, "w") as f:
            json.dump(messages, f)

    def chat(self, message: str) -> str:
        """Send a message to the AI and return the response."""
        messages = self._load_history()
        
        # ✅ Trim long user messages to prevent exceeding token limit
        if len(message) > 1000:
            message = message[:1000] + "..."

        messages.append({"role": "user", "content": message})

        # ✅ Add system prompt ONLY once at the start
        if len(messages) == 1:
            messages.insert(0, {"role": "system", "content": self.system_prompt})

        try:
            chat_completion = self.client.chat.completions.create(
                messages=messages,
                model=self.model_name,
            )
            assistant_response = chat_completion.choices[0].message.content
        except Exception as e:
            assistant_response = "Sorry, I'm having trouble responding right now. Please try again later."

        messages.append({"role": "assistant", "content": assistant_response})
        self._save_history(messages)

        return assistant_response
