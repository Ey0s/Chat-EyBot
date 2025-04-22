import os
import random
import datetime
import json
import customtkinter as ctk


class ChatBot:
    def __init__(self, json_file, creator_name="Eyosyas"):
        self.creator = creator_name
        self.responses = self.load_responses(json_file)

    def load_responses(self, json_file):
        if os.path.exists(json_file):
            with open(json_file, 'r') as file:
                return json.load(file)
        else:
            print(f"Error: {json_file} does not exist.")
            return {}

    def get_time(self):
        return "Current time is " + datetime.datetime.now().strftime("%H:%M:%S")

    def get_date(self):
        return "Today's date is " + datetime.datetime.now().strftime("%Y-%m-%d")

    def get_response(self, message):
        message = message.lower()
        for dynamic_key, dynamic_data in self.responses.get("dynamic_responses", {}).items():
            if any(keyword in message for keyword in dynamic_data["keywords"]):
                function_name = dynamic_data["function"]
                if hasattr(self, function_name): 
                    return getattr(self, function_name)()

        for category, category_data in self.responses.get("static_responses", {}).items():
            for pattern in category_data["patterns"]:
                if pattern in message:
                    return random.choice(category_data["responses"])

        return random.choice(self.responses.get("static_responses", {}).get("default", {}).get("responses", ["Sorry, I didn't understand that."]))


class ChatApp:
    def __init__(self, root, chatbot):
        self.chatbot = chatbot
        self.history = self.load_history()

        self.root = root
        self.root.title(f"Chat-Ey Bot by {self.chatbot.creator}")
        self.root.geometry("600x600")
        self.root.resizable(False, False)

        ctk.set_appearance_mode("System")
        ctk.set_default_color_theme("blue")

        main_frame = ctk.CTkFrame(self.root)
        main_frame.pack(padx=10, pady=10, fill="both", expand=True)

        self.chat_display = ctk.CTkTextbox(main_frame, wrap="word", state="disabled", font=("Arial", 14))
        self.chat_display.pack(pady=(0, 10), fill="both", expand=True)

        self.chat_display.tag_config("user", foreground="#2b7de9")
        self.chat_display.tag_config("bot", foreground="#4CAF50")
        self.chat_display.tag_config("system", foreground="#FF5722")

        input_frame = ctk.CTkFrame(main_frame)
        input_frame.pack(fill="x")

        self.user_input = ctk.CTkEntry(input_frame, placeholder_text="Type your message...", font=("Arial", 14), height=40)
        self.user_input.pack(side="left", fill="x", expand=True, padx=(0, 5))
        self.user_input.bind("<Return>", lambda event: self.send_message())

        send_button = ctk.CTkButton(input_frame, text="Send", width=80, command=self.send_message)
        send_button.pack(side="right")

        btn_frame = ctk.CTkFrame(main_frame)
        btn_frame.pack(pady=5, fill="x")

        for (text, command) in [
            ("Show History", self.show_history),
            ("Clear Chat", self.clear_chat),
            ("Clear History", self.clear_history),
            ("Exit", self.exit_app)
        ]:
            ctk.CTkButton(btn_frame, text=text, command=command).pack(side="left", padx=5, fill="x", expand=True)

        self.add_to_chat("Bot", f"Hello! I'm Chat-Ey, created by {self.chatbot.creator}. How can I help you today?")
        self.user_input.focus_set()

    def send_message(self):
        user_message = self.user_input.get().strip()
        if user_message:
            self.add_to_chat("user", f"You: {user_message}")
            self.user_input.delete(0, "end")

            bot_response = self.chatbot.get_response(user_message)
            self.add_to_chat("bot", f"Bot: {bot_response}")
            self.history.append(f"You: {user_message}")
            self.history.append(f"Bot: {bot_response}")
            self.save_history()

    def add_to_chat(self, sender, message):
        self.chat_display.configure(state="normal")
        if sender == "user":
            self.chat_display.insert("end", message + "\n", "user")
        elif sender == "bot":
            self.chat_display.insert("end", message + "\n", "bot")
        else:
            self.chat_display.insert("end", message + "\n", "system")
        self.chat_display.configure(state="disabled")
        self.chat_display.yview("end")

    def show_history(self):
        history_text = "\n".join(self.history)
        self.add_to_chat("system", f"Chat History:\n{history_text}")

    def clear_chat(self):
        self.chat_display.configure(state="normal")
        self.chat_display.delete(1.0, "end")
        self.chat_display.configure(state="disabled")

    def clear_history(self):
        self.history.clear()
        self.add_to_chat("system", "Chat history cleared.")
        self.save_history()

    def exit_app(self):
        self.root.quit()

    def load_history(self):
        if os.path.exists('history.json'):
            with open('history.json', 'r') as file:
                return json.load(file)
        return []

    def save_history(self):
        with open('history.json', 'w') as file:
            json.dump(self.history, file, indent=4)


def main():
    chatbot = ChatBot('responses.json', creator_name="Eyosyas")

    root = ctk.CTk()
    app = ChatApp(root, chatbot)
    root.mainloop()

if __name__ == "__main__":
    main()
