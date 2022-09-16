import tkinter as tk


def mod12(note):
    note = int(note)
    while note < 0:
        note += 12
    while note >= 12:
        note -= 12
    return note


class Window(tk.Tk):
    def __init__(self):
        super(Window, self).__init__()
        self.note_index = tk.IntVar()
        self.geometry("380x150")
        self.resizable(False, False)
        self.title("Transposition")
        self.table = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]

        # NOTE INPUT LABEL
        self.top_label_text = tk.StringVar()
        self.top_label_text.set("Enter base note (use # for sharps, eg. A#): ")
        self.label = tk.Label(self, textvar=self.top_label_text, font=("Arial", 10))
        self.label.grid(row=0, column=0, padx=5, pady=5, sticky="E")

        # NOTE INPUT
        self.note_text = tk.StringVar()
        self.note_entry = tk.Entry(self, textvariable=self.note_text, width=5)
        self.note_entry.grid(row=0, column=1, ipadx=35)

        # INTERVAL INPUT LABEL
        self.interval_label_text = tk.StringVar()
        self.interval_label_text.set("Enter interval in semitones: ")
        self.interval_label = tk.Label(self, textvar=self.interval_label_text, font=("Arial", 10))
        self.interval_label.grid(row=1, column=0, padx=5, pady=5, sticky="E")

        # INTERVAL INPUT
        self.interval_text = tk.StringVar()
        self.interval_entry = tk.Entry(self, textvariable=self.interval_text, width=5)
        self.interval_entry.grid(row=1, column=1, ipadx=35)

        # ---------------------Calculate Button ---------------------
        self.transpose_button = tk.Button(self, text="Calculate", command=self.transpose, font=("Arial", 11, "bold"))
        self.transpose_button.grid(row=2, columnspan=2, padx=10, pady=10, sticky="N")

        # ---------------------Show Pitch Label ---------------------
        self.show_label_text = tk.StringVar()
        self.show_label_text.set("Transposed note is : ")
        self.show_label = tk.Label(self, textvar=self.show_label_text, font=("Arial", 10))
        self.show_label.grid(row=3, column=0, padx=5, pady=5)

        self.show_label_value = tk.StringVar()
        self.show_label = tk.Label(self, textvar=self.show_label_value, font=("Arial", 10, "bold"))
        self.show_label.grid(row=3, column=1, pady=5)

    def transpose(self):
        if self.note_entry.get().upper() not in self.table or not self.interval_entry.get().isdigit():
            self.show_label_value.set("Could not find!")
        else:
            note_index = mod12(self.interval_entry.get())
            for note in self.table:
                if self.note_entry.get().upper() == note:
                    for idx, ele in enumerate(self.table):
                        if note == ele:
                            note_index += idx
                            if note_index > 11:
                                note_index -= 12
                            self.show_label_value.set(self.table[note_index])


if __name__ == "__main__":
    window = Window()
    window.mainloop()
