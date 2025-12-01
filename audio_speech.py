import base64
import os

class AudioSpeech:
    def __init__(self, client, folder=r"D:\Study\Code\OpenAI\open_ai\audio"):
        self.client = client
        self.folder = folder

        if not os.path.exists(folder):
            os.makedirs(folder)

    def audio_output(self, prompt, filename):
        completion = self.client.client.chat.completions.create(
            model="gpt-4o-audio-preview",
            modalities=["text", "audio"],
            audio={"voice": "alloy", "format": "wav"},
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        print(completion.choices[0])

        wav_bytes = base64.b64decode(
            completion.choices[0].message.audio.data
        )

        save_path = os.path.join(self.folder, filename)

        with open(save_path, "wb") as f:
            f.write(wav_bytes)

        print(f"Saved audio to: {save_path}")