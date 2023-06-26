import tkinter as tk
from tkinter import messagebox

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz App")
        self.root.geometry("500x300")

        self.questions = [
            {
                "question": "What is the capital of France?",
                "options": ["Paris", "Rome", "Madrid", "Berlin"],
                "answer": "Paris"
            },
            {
                "question": "Which planet is known as the Red Planet?",
                "options": ["Venus", "Mars", "Jupiter", "Mercury"],
                "answer": "Mars"
            },
            {
                "question": "Who painted the Mona Lisa?",
                "options": ["Pablo Picasso", "Leonardo da Vinci", "Vincent van Gogh", "Michelangelo"],
                "answer": "Leonardo da Vinci"
            },
            {
                "question": "What is the largest ocean in the world?",
                "options": ["Atlantic Ocean", "Arctic Ocean", "Indian Ocean", "Pacific Ocean"],
                "answer": "Pacific Ocean"
            },
            {
                "question": "Which country is known as the 'Land of the Rising Sun'?",
                "options": ["China", "Japan", "India", "South Korea"],
                "answer": "Japan"
            }
        ]

        self.question_index = 0
        self.score = 0

        self.question_label = tk.Label(self.root, text="", font=("Arial", 16))
        self.question_label.pack(pady=20)

        self.option_var = tk.StringVar()
        self.option_var.set(-1) # type: ignore

        self.option_buttons = []
        for i in range(4):
            button = tk.Radiobutton(self.root, text="", variable=self.option_var, value=i, font=("Arial", 12))
            button.pack(pady=5)
            self.option_buttons.append(button)

        self.next_button = tk.Button(self.root, text="Next", command=self.next_question, font=("Arial", 14))
        self.next_button.pack(pady=10)
        self.next_button["state"] = "disabled"

        self.show_question()

    def show_question(self):
        if self.question_index < len(self.questions):
            question_data = self.questions[self.question_index]
            self.question_label["text"] = question_data["question"]
            options = question_data["options"]
            for i in range(4):
                self.option_buttons[i]["text"] = options[i]
            self.next_button["state"] = "active"
        else:
            self.show_result()

    def next_question(self):
        selected_option = self.option_var.get()
        if selected_option != -1:
            question_data = self.questions[self.question_index]
            if question_data["options"][int(selected_option)] == question_data["answer"]:
                self.score += 1
            self.question_index += 1
            self.option_var.set(-1) # type: ignore
            self.show_question()

    def show_result(self):
        messagebox.showinfo("Quiz Result", f"You scored {self.score} out of {len(self.questions)}")
        self.root.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()
