import openai
import tkinter as tk

# Set the API key
openai.api_key = "YOUR_API_KEY_HERE"

class TextEditor:
    def __init__(self, master):
        self.master = master
        master.title("CODE DRIVE 0.X")
        master.geometry("400x300")

        # Create a text input for the user to enter a description of the desired code
        self.description_label = tk.Label(master, text="Enter code description:")
        self.description_label.pack()
        self.description_input = tk.Entry(master, width=30)
        self.description_input.pack()
        self.description_input.insert(0, "Enter code description")

        # Create a dropdown menu to select the programming language
        self.language_label = tk.Label(master, text="Select programming language:")
        self.language_label.pack()
        self.language_var = tk.StringVar(master)
        self.language_var.set("Python")  # default value
        self.language_dropdown = tk.OptionMenu(master, self.language_var, "Python", "HTML", "C#", "Rust", "Java", "C", "ASM")
        self.language_dropdown.pack()

        # Create a button to generate the code
        self.generate_button = tk.Button(master, text="Generate", command=self.generate_code)
        self.generate_button.pack()

        # Create a button to explain the code
        self.explain_button = tk.Button(master, text="Explain", command=self.explain_code)
        self.explain_button.pack()

        # Create a text area to display the generated code and code explanation
        self.code_display = tk.Text(master)
        self.code_display.pack()

    def generate_code(self):
        # Get the user's input description and selected programming language
        description = self.description_input.get()
        language = self.language_var.get()

        # Use the GPT-3 API to generate the code
        prompt = f"Write a {language} program that {description}"
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=prompt,
            temperature=0.7,
            max_tokens=1024,
            n = 1,
            stop=None,
            frequency_penalty=0,
            presence_penalty=0
        )
        code = response.choices[0].text

        # Display the generated code
        self.code_display.delete("1.0", tk.END)
        self.code_display.insert("1.0", "Generated code:\n\n")
        self.code_display.insert(tk.END, code)

    def explain_code(self):
        # Get the generated code
        code = self.code_display.get("2.0", tk.END)

        # Use the GPT-3 API to explain the code in English
        prompt = f"Explain the following code in English: {code}"
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=prompt,
            temperature=0.7,
            max_tokens=1024,
            n = 1,
            stop=None,
            frequency_penalty=0,
            presence_penalty=0
        )
        explanation = response.choices[0].text

        # Display the explanation
        self.code_display.delete("1.0", tk.END)
        self.code_display.insert("1.0", "Code explanation:\n\n")
        self.code_display.insert(tk.END, explanation)

root = tk.Tk()
text_editor = TextEditor(root)
root.mainloop()
