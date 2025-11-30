class TextGenerator:
    def __init__(self, client):
        self.client = client

    def generate_text(self, prompt):
        response = self.client.client.responses.create(
        model="gpt-5-nano",
        reasoning= {"effort": "low"},
        input=[
            {
                "role": "developer",
                "content": "You are a helpful coding assistant."
            },
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

        return response