from openai_api import OpenAIAPI
from text_gen import TextGenerator
from image_vision import ImageVision

client = OpenAIAPI()
text_gen = TextGenerator(client)
image_vision = ImageVision(client)

while True:
    print("\n--- AI Assistant ---")
    print("1. Generate Text")
    print("2. Generate Image")
    print("0. Exit")

    choice = input("Enter your choice: ")   

    if choice == '1':
        user_query = input("Enter your prompt: ")

        while user_query.lower() != "exit" :
            try:
                response = text_gen.generate_text(user_query)
                print("\nGenerated Text:\n", response.output_text)
            except Exception as e:
                print("Error during text generation:", e)

            user_query = input("Enter your prompt (or type 'exit' to quit): ")

    elif choice == '2':
        image_prompt = input("Enter image description: ")
        image_title = input("Enter image file name (with .png or .jpg): ")

        try:
            image_vision.image_gen(image_prompt, image_title)
            print(f"Image generated and saved as {image_title}")
        except Exception as e:
            print("Error during image generation:", e)

    elif choice == '0':
        print("Exiting the program.")
        break

    else:
        print("Invalid choice. Please try again.")
