import base64
import os.path


class ImageVision:
    def __init__(self, client, folder=r"D:\Study\Code\OpenAI\open_ai\image"):
        self.client = client
        self.folder = folder

        if not os.path.exists(folder):
            os.makedirs(folder)

    def image_gen(self, prompt, title):
        response = self.client.client.responses.create(
            model="gpt-4.1-mini",
            input=prompt,
            tools=[{"type": "image_generation"}]
        )

        image_data = next(
            (o for o in response.output if o.type == "image_generation_call"),
            None
        )

        if image_data:
            image_base64 = image_data.image[0].b64_json
            save_path = os.path.join(self.folder, title)

            with open(save_path, "wb") as f:
                f.write(base64.b64decode(image_base64))