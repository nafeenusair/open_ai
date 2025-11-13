from openai_api import OpenAIAPI
from text_gen import TextGenerator

client = OpenAIAPI()
text_gen = TextGenerator(client)

while True:
    print("\n--- AI Assistant ---")
    print("1. Generate Text")
    print("2. Exit")

    choice = input("Enter your choice: ")   

    if choice == '1':
        user_query = input("Enter your prompt: ")
        try:
            response = text_gen.generate_text(user_query)
            print("\nGenerated Text:\n", response.output_text)
        except Exception as e:
            print("Error during text generation:", e)
    elif choice == '2':
        print("Exiting the program.")
        break   
    else:
        print("Invalid choice. Please try again.")
