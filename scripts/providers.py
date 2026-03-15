"""
Model provider abstraction for AutoDraft
Supports OpenAI, Anthropic, and Hyperbolic
"""

import os


class ModelProvider:
    """Simple abstraction for model providers"""

    def __init__(self, provider_name: str):
        self.provider_name = provider_name.lower()

        if self.provider_name == "openai":
            import openai
            self.client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
            self.model = os.getenv("OPENAI_MODEL", "gpt-4-turbo-preview")

        elif self.provider_name == "hyperbolic":
            import openai
            self.client = openai.OpenAI(
                api_key=os.getenv("HYPERBOLIC_API_KEY"),
                base_url=os.getenv("HYPERBOLIC_BASE_URL", "https://api.hyperbolic.xyz/v1")
            )
            self.model = os.getenv("HYPERBOLIC_MODEL", "meta-llama/Meta-Llama-3.1-70B-Instruct")

        elif self.provider_name == "anthropic":
            import anthropic
            self.client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))
            self.model = os.getenv("ANTHROPIC_MODEL", "claude-sonnet-4-5-20250929")

        else:
            raise ValueError(f"Unsupported provider: {provider_name}")

    def generate(self, prompt: str, system: str = None) -> str:
        """Generate text using the configured provider"""

        if self.provider_name in ["openai", "hyperbolic"]:
            messages = []
            if system:
                messages.append({"role": "system", "content": system})
            messages.append({"role": "user", "content": prompt})

            response = self.client.chat.completions.create(
                model=self.model,
                messages=messages,
                temperature=0.7,
                max_tokens=4000
            )
            return response.choices[0].message.content

        elif self.provider_name == "anthropic":
            kwargs = {
                "model": self.model,
                "max_tokens": 4000,
                "temperature": 0.7,
                "messages": [{"role": "user", "content": prompt}]
            }
            if system:
                kwargs["system"] = system

            response = self.client.messages.create(**kwargs)
            return response.content[0].text


def validate_provider_config(provider_name: str) -> bool:
    """Validate that provider configuration is complete"""
    provider_name = provider_name.lower()

    if provider_name == "openai":
        return bool(os.getenv("OPENAI_API_KEY"))
    elif provider_name == "hyperbolic":
        return bool(os.getenv("HYPERBOLIC_API_KEY"))
    elif provider_name == "anthropic":
        return bool(os.getenv("ANTHROPIC_API_KEY"))
    else:
        return False
