# Chat-Ey Bot: A Chatbot Application by Eyosyas

**Chat-Ey Bot** is a Python-based chatbot application built with `CustomTkinter` for a rich graphical user interface (GUI). This bot offers dynamic and static responses, allows users to chat interactively, and features functionalities such as viewing chat history, clearing chat, and clearing history. The bot can provide real-time information like the current date and time, and is easily extensible with additional responses.

## Features
- **Dynamic Responses**: The bot can reply with real-time data like the current time or today's date.
- **Static Responses**: The bot has predefined responses for certain keywords and patterns.
- **Chat History**: Keeps track of the entire conversation history.
- **Clear Chat**: Option to clear the current chat screen.
- **Clear History**: Clears the conversation history.
- **Exit Functionality**: Allows users to exit the application.

## Technologies Used
- **Python 3**: Core programming language.
- **CustomTkinter**: Used to build a modern, customizable GUI.
- **JSON**: For storing and loading the bot's responses.
- **OS**: File handling and path management.

## How It Works
1. **Loading Responses**: The chatbot loads its responses from a `responses.json` file, which contains both dynamic and static response categories.
2. **User Interaction**: The user inputs a message, and the bot generates a response based on the message. Dynamic responses, such as current time or date, are handled using dedicated functions.
3. **GUI**: The application is built using CustomTkinter, which offers a sleek interface with an easy-to-navigate input/output area, buttons for various controls (such as clearing history or chat), and display areas for messages.

## How to Run
1. Install dependencies:
   ```
   pip install customtkinter
   ```
2. Clone or download this repository.
3. Ensure that you have a `responses.json` file in the same directory, containing the bot's responses.
4. Run the script:
   ```
   python chatbot_app.py
   ```

## Example Usage

- **User Message**: "What's the time?"
- **Bot Response**: "Current time is 14:35:21."

- **User Message**: "Hi bot!"
- **Bot Response**: "Hello! I'm Chat-Ey, created by Eyosyas. How can I help you today?"

## Customizing the Bot
- You can add your own responses to the `responses.json` file. It allows for easy modification and extension of the bot's capabilities.
- Dynamic responses are triggered by keywords specified in the JSON file, and the corresponding function is called to provide real-time data.


## Created By
**Eyosyas** 

---
