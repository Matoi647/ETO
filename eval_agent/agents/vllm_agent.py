# import openai
import logging
import backoff
from openai import OpenAI
from .base import LMAgent

# Modify OpenAI's API key and API base to use vLLM's API server.
openai_api_key = "EMPTY"
openai_api_base = "http://localhost:8000/v1"
client = OpenAI(
    # defaults to os.environ.get("OPENAI_API_KEY")
    api_key=openai_api_key,
    base_url=openai_api_base,
)
models = client.models.list()
model = models.data[0].id
print("<model>")
print(model)
print("</model>")

logger = logging.getLogger("agent_frame")


class VllmAgent(LMAgent):
    def __init__(self, config):
        super().__init__(config)

    def __call__(self, messages) -> str:
        # Prepend the prompt with the system message
        # from pprint import pprint
        # print("<messages>")
        # pprint(messages)
        # print("</messages>")

        response = client.chat.completions.create(
            model=model,
            messages=messages,
            max_tokens=self.config.get("max_tokens", 512),
            temperature=self.config.get("temperature", 0),
            # stop=self.stop_words,
            stop=['<|eot_id|>'],
        )
        from pprint import pprint
        # print("<response>")
        # pprint(response.choices[0].message.content)
        # print("</response>")

        return response.choices[0].message.content
