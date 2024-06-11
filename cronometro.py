import tkinter as tk

class Stopwatch:
    def __init__(self, root):
        self.root = root
        self.root.title("Cronômetro")
        
        self.hours = 0
        self.minutes = 0
        self.seconds = 0
        self.running = False

        self.time_label = tk.Label(root, text="00:00:00", font=("Arial", 24))
        self.time_label.pack()

        self.start_button = tk.Button(root, text="Iniciar", command=self.start_stopwatch)
        self.start_button.pack(side="left", padx=5)

        self.stop_button = tk.Button(root, text="Parar", command=self.stop_stopwatch)
        self.stop_button.pack(side="left", padx=5)

        self.reset_button = tk.Button(root, text="Resetar", command=self.reset_stopwatch)
        self.reset_button.pack(side="left", padx=5)

    def update_time(self):
        if self.running:
            self.seconds += 1
            if self.seconds >= 60:
                self.seconds = 0
                self.minutes += 1
                if self.minutes >= 60:
                    self.minutes = 0
                    self.hours += 1
            current_time = "{:02d}:{:02d}:{:02d}".format(self.hours, self.minutes, self.seconds)
            self.time_label.config(text=current_time)
            self.root.after(1000, self.update_time)

    def start_stopwatch(self):
        if not self.running:
            self.running = True
            self.update_time()

    def stop_stopwatch(self):
        self.running = False

    def reset_stopwatch(self):
        if not self.running:
            self.hours, self.minutes, self.seconds = 0, 0, 0
            self.time_label.config(text="00:00:00")

def main():
    root = tk.Tk()
    stopwatch = Stopwatch(root)
    root.mainloop()

if __name__ == "__main__":
    main()
