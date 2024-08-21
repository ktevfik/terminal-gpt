# GPT-4o-mini Chat Assistant

This is a command-line based chat application that interacts with the GPT-4o-mini model using the OpenAI API. The assistant is customized with instructions to be a helpful Linux and coding expert. The application logs all conversations to a `conversation.log` file.

## Features

- Interactive Chat: Converse with a GPT-4o-mini assistant in real-time.
- Custom Instructions: The assistant is pre-configured as a helpful Linux and coding expert.
- Markdown Support: Responses are rendered in the terminal with Markdown formatting.
- Conversation Logging: All conversations are logged to a `conversation.log` file for future reference.

## Prerequisites

- Python 3.7+
- OpenAI API Key
- Installed Python packages:
  - `openai`
  - `rich`

## Installation

1. Clone the Repository:
   ```
   git clone https://github.com/ktevfik/terminal-gpt.git
   cd your-repo-name
   ```

2. Set Up a Virtual Environment (Optional but Recommended):
   ```
   python3 -m venv openavi-env
   source venv/bin/activate
   ```

3. Install Required Packages:
   ```
   pip install -r requirements.txt
   ```

4. Set Your OpenAI API Key:
   - Set your OpenAI API key as an environment variable:
     ```
     export OPENAI_API_KEY="your-api-key-here"
     ```

## Usage

Run the chat application with:

```
python main.py
```

### Interacting with the Assistant

- Start typing your questions or commands related to Linux or coding.
- The assistant will respond with expertise in Linux and coding topics.
- Type `exit`, `quit`, or `q` to end the conversation.

### Conversation Logging

- All conversations are automatically logged to a `conversation.log` file in the root directory.
- Each session is separated by `--- New Conversation ---` and `--- End of Conversation ---`.

## Example

```
You: How do I list files in a directory?
GPT-4o-mini: To list files in a directory, you can use the `ls` command in the terminal.
```

## Customization

You can modify the initial instructions to the assistant by editing the `conversation_history` in the script:

```
conversation_history = [
    {"role": "system", "content": "You are a helpful assistant. You are a Linux expert. You are a coding expert."}
]
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

