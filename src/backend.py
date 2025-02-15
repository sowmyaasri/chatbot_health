import json
import os
from groq import Groq

class AI:
    def __init__(self):
        self.client = Groq(
            api_key="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",
        )
        self.system_prompt = "You are a mental health expert and a psychiatrist who will respond to the user in a kind and polite manner"
        self.history_file = "chat_history.json"

    def _load_history(self):
        if os.path.exists(self.history_file):
            with open(self.history_file, "r") as f:
                return json.load(f)
        return []

    def _save_history(self, messages):
        with open(self.history_file, "w") as f:
            json.dump(messages, f)

    def chat(self, message: str, model_name="llama-3.3-70b-versatile") -> str:
        messages = self._load_history()
       
        messages.append({"role": "user", "content": message})

        # Get the assistant's response
        chat_completion = self.client.chat.completions.create(
            messages=messages + [
                {"role": "system", "content": self.system_prompt},
                {"role": "user", "content": message}
            ],
            model=model_name,
        )

        assistant_response = chat_completion.choices[0].message.content
        
        # Add the assistant's response to the history
        messages.append({"role": "assistant", "content": assistant_response})
        
        # Save the updated history
        self._save_history(messages)
        
        return assistant_response
