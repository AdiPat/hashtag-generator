import traceback
from typing import List
from openai import OpenAI
import os
import json


class HashtagUtils:
    def __init__(self):
        self.client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    def get_hashtags(self, content: str, temperature=0.5, num_tags=5) -> List[str]:
        try:
            completion = self.client.chat.completions.create(
                model="gpt-4o",
                messages=[
                    {
                        "role": "system",
                        "content": f"You are an AI agent that generates hashtags for a given piece of content.\
                                            The content will be supplied to your in the form of a prompt.\
                                            Return the result as a JSON-array of the hashtags. \
                                            Generate {num_tags} hashtags for the following content.",
                    },
                    {"role": "user", "content": f"Content: {content}"},
                ],
                temperature=temperature,
                response_format={"type": "json_object"},
            )

            hashtags_json = completion.choices[0].message.content
            hashtags = json.loads(hashtags_json)

            return hashtags
        except Exception as e:
            traceback.print_exc()
            return None
        
    def get_similar_hashtags(self, tags: List[str], temperature=0.5, num_tags=5) -> List[str]:
        try:
            completion = self.client.chat.completions.create(
                model="gpt-4o",
                messages=[
                    {
                        "role": "system",
                        "content": f"You are an AI agent that analyses hashtags and generates similar hashtags.\
                                            The hashtags will be supplied to your in the form of a prompt.\
                                            Return the result as a JSON-array of the similar hashtags. \
                                            Generate {num_tags} hashtags for the following hashtags.",
                    },
                    {"role": "user", "content": f"Hashtags: {",".join(tags)}"},
                ],
                temperature=temperature,
                response_format={"type": "json_object"},
            )

            hashtags_json = completion.choices[0].message.content
            hashtags = json.loads(hashtags_json)

            return hashtags
        except Exception as e:
            traceback.print_exc()
            return None
