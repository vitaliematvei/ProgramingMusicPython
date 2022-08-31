import tkinter as tk


class Window(tk.Tk):
    def __init__(self):
        super(Window, self).__init__()
        self.geometry("450x150")
        self.resizable(False, False)
        self.title("Transposition")
        self.grid_columnconfigure((0, 1), weight=1)

        # TOP LABEL
        self.label_text = tk.StringVar()
        self.label_text.set("Enter base note (use # for sharps, eg. A#): ")
        self.name_text = tk.StringVar()
        self.label = tk.Label(self, textvar=self.label_text, font=("Arial", 11, "bold"))
        self.label.grid(row=1, column=0, padx=10, pady=5)

        # TOP INPUT
        self.note_text = tk.StringVar()
        self.note_entry = tk.Entry(self, textvariable=self.note_text)
        self.note_entry.grid(row=1, column=1, padx=5, pady=5)

        # SHOW RESULT
        self.label_result = tk.StringVar()
        self.label_result = self.note_entry
        self.label_result_entry = tk.Label(self, textvariable=self.label_result, font=("Arial", 11, "bold"))
        self.label_result_entry.grid(row=3, column=1, padx=5, pady=5)


if __name__ == "__main__":
    window = Window()
    window.mainloop()

