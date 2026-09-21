import tkinter as tk

class Timesaver(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Timesaver 2000")
        self.geometry('600x400')
        tk.Label(self, text="Timesaver 2000").grid(row=0, column=0, columnspan=2)
        self.timeDisplay = tk.StringVar(self, "00:00:00")
        self.timeLabel = tk.Label(self, textvariable=self.timeDisplay).grid(row=1, column=0, columnspan=2)
        self.buttonLabel = tk.StringVar(self, "Start")
        tk.Button(self, textvariable=self.buttonLabel, command=self.start).grid(row=3, column=0)
        tk.Button(self, text="Penalty", command=self.penalty).grid(row=3, column=1)

    def start(self):
        print("Start clicked")

    def stop(self):
        print("Stop clicked")

    def penalty(self):
        print("PENALTY!!")

if __name__ == "__main__":
    app = Timesaver()
    app.mainloop()
