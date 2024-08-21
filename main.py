import os
import openai
import readline
from rich.console import Console
from rich.markdown import Markdown

console = Console()

# Ensure your OpenAI API key is set
openai.api_key = os.getenv("OPENAI_API_KEY")

# ANSI escape codes for colors
RED = "\033[91m"
WHITE = "\033[97m"
RESET = "\033[0m"

# Define the conversation history with custom instructions
conversation_history = [
    {"role": "system", "content": "You are a helpful assistant. You are a Linux expert. You are a coding expert."}
]

def chat_with_gpt():
    while True:
        try:
            user_input = input(f"{WHITE}You: {RESET}")

            if user_input.lower() in ["exit", "quit", "q"]:
                print("Exiting chat...")
                break

            # Add the user's input to the history so it can be accessed with the up arrow key
            readline.add_history(user_input)
            conversation_history.append({"role": "user", "content": user_input})

            response = openai.chat.completions.create(
                model="gpt-4o-mini",
                messages=conversation_history,
                max_tokens=5000,
                temperature=0.7,
            )

            bot_response = response.choices[0].message.content.strip()
            console.print(f"GPT-4o-mini:", style= "white")
            console.print(Markdown(bot_response))

            # Append GPT-4's response to the conversation history
            conversation_history.append({"role": "assistant", "content": bot_response})

        except KeyboardInterrupt:
            print("\nExiting chat...")
            break
        except Exception as e:
            print(f"An error occurred: {e}")

def save_conversation_to_log(conversation_history, log_filename="conversation.log"):
    with open(log_filename, "a") as log_file:
        log_file.write("\n--- New Conversation ---\n")
        for message in conversation_history:
            role = message['role'].capitalize()
            content = message['content']
            log_file.write(f"{role}: {content}\n")
        log_file.write("\n--- End of Conversation ---\n\n")
    
if __name__ == "__main__":
    chat_with_gpt()
    save_conversation_to_log(conversation_history)
    print("Conversation history saved to conversation.log.")