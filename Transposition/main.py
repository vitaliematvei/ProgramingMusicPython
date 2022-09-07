import tkinter as tk


class Window(tk.Tk):
    def __init__(self):
        super(Window, self).__init__()
        self.geometry("450x150")
        self.resizable(False, False)
        self.title("Transposition")
        self.grid_columnconfigure((0, 1), weight=1)

        # NOTE INPUT LABEL
        self.top_label_text = tk.StringVar()
        self.top_label_text.set("Enter base note (use # for sharps, eg. A#): ")
        self.label = tk.Label(self, textvar=self.top_label_text, font=("Arial", 11, "bold"))
        self.label.grid(row=1, column=0, padx=10, pady=5)

        # NOTE INPUT
        self.note_text = tk.StringVar()
        self.note_entry = tk.Entry(self, textvariable=self.note_text)
        self.note_entry.grid(row=1, column=1, padx=5, pady=5)

        # INTERVAL INPUT LABEL
        self.interval_label_text = tk.StringVar()
        self.interval_label_text.set("Enter interval in semitones: ")
        self.interval_label = tk.Label(self, textvar=self.interval_label_text, font=("Arial", 11, "bold"))
        self.interval_label.grid(row=2, column=0, pady=5)

        # INTERVAL INPUT
        self.interval_text = tk.StringVar()
        self.interval_entry = tk.Entry(self, textvariable=self.interval_text)
        self.interval_entry.grid(row=2, column=1, padx=5, pady=5)

        # ---------------------Calculate Button ---------------------
        self.transpose_button = tk.Button(self, text="Calculate", command=self.transpose)
        self.transpose_button.grid(row=3, column=1, padx=5, pady=5)

        # ---------------------Calculate Interval Label ---------------------
        self.show_label_text = tk.StringVar()
        self.show_label_text.set("Transposed by x is : ")
        self.show_label_value = tk.StringVar()
        self.show_label = tk.Label(self, textvar=self.show_label_value, font=("Arial", 11, "bold"))
        self.show_label.grid(row=4, column=0, padx=10, pady=5)


    def transpose(self):
        #show = translate_from_note_to_pitch_class(
         #   self.note_entry.get().lower(),
          #  self.interval_entry.get().lower())
        show = self.note_entry.get().lower() + self.interval_entry.get().lower()
        self.show_label_value.set(show)


if __name__ == "__main__":
    window = Window()
    window.mainloop()
