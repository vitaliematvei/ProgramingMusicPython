import tkinter as tk

from translate_from_note_to_pitch_class import translate_from_note_to_pitch_class


class Window(tk.Tk):
    def __init__(self):
        super(Window, self).__init__()
        self.title("Notes Intevral")
        self.geometry("300x200+300+250")

        self.top_label_txt = tk.StringVar()

        self.first_note_label = tk.StringVar()
        self.first_note_txt = tk.StringVar()

        self.second_note_label = tk.StringVar()
        self.second_note_txt = tk.StringVar()

        self.show_interval_txt = tk.StringVar()

        # ---------------------TOP Label ---------------------
        self.top_label_txt.set("Introduce two notes, Ex.: C and F:")
        self.top_label = tk.Label(self, textvar=self.top_label_txt, font="Arial", fg="#E46457", bg="#f0f0f0")
        self.top_label.pack(padx=10, pady=10)

        # ---------------------First Note Input ---------------------
        # Label
        self.first_note_label.set("Introduce the first note, please: ")
        self.label = tk.Label(self, textvar=self.first_note_label, font="Arial 10", fg="#000000", bg="#f0f0f0")
        self.label.place(x=30, y=50)
        # Input Text
        self.first_note_entry = tk.Entry(self, textvar=self.first_note_txt)
        self.first_note_entry.place(x=240, y=50, width=15)

        # ---------------------Second Note Input ---------------------
        # Label
        self.second_note_label.set("Introduce the second note, please: ")
        self.label = tk.Label(self, textvar=self.second_note_label, font="Arial 10", fg="#000000", bg="#f0f0f0")
        self.label.place(x=30, y=80)
        # Text
        self.second_note_entry = tk.Entry(self, textvar=self.second_note_txt)
        self.second_note_entry.place(x=240, y=80, width=15)

        # ---------------------Calculate Button ---------------------
        self.calculate_button = tk.Button(self, text="Calculate", command=self.show_interval)
        self.calculate_button.place(x=100, y=120, width=100)

        # ---------------------Show Interval Label ---------------------
        self.show_interval_label = tk.Label(self, textvar=self.show_interval_txt, font="Arial 10", fg="#000000",
                                        bg="#f0f0f0")
        self.show_interval_label.place(x=30, y=150)

    def show_interval(self):
        show = translate_from_note_to_pitch_class(
            self.first_note_entry.get().lower(),
            self.second_note_entry.get().lower())
        self.show_interval_txt.set(show)


if __name__ == "__main__":
    window = Window()
    window.mainloop()


