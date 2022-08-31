import tkinter as tk


class Window(tk.Tk):
    def __init__(self):
        super(Window, self).__init__()
        self.geometry("450x150")
        self.resizable(False, False)
        self.title("Transposition")
        self.label_text = tk.StringVar()
        self.label_text.set("Enter base note (use # for sharps, eg. A#): ")
        self.name_text = tk.StringVar()
        self.label = tk.Label(self, textvar=self.label_text, font=("Arial", 11, "bold"))
        self.label.pack(anchor="w", padx=10, pady=5)


if __name__ == "__main__":
    window = Window()
    window.mainloop()

