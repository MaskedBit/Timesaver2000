import tkinter as tk
from datetime import datetime
import time

class Timesaver(tk.Tk):
    def __init__(self):
        super().__init__()
        self.running = False
        self.startTime = 0
        self.endTime = 0
        self.penalties = 0
        self.title("Timesaver 2000")
        self.geometry('600x400')
        tk.Label(self, text="Timesaver 2000").grid(row=0, column=0, columnspan=2)
        self.timeDisplay = tk.StringVar(self, "00:00:00")
        self.timeLabel = tk.Label(self, textvariable=self.timeDisplay).grid(row=1, column=0, columnspan=2)
        self.startButton = tk.Button(self, text="Start", command=self.start)
        self.startButton.grid(row=3, column=0)
        self.finishButton = tk.Button(self, text="Finish", command=self.stop)
        tk.Button(self, text="Penalty", command=self.penalty).grid(row=3, column=1)

    def start(self):
        if not self.running:
            self.running = True
            self.startTime = int(time.time())
            self.endTime = self.startTime
            self.startButton.grid_forget()
            self.finishButton.grid(row=3, column=0)
            self.update()

    def stop(self):
        if self.running:
            self.after_cancel(self.after_loop)
            self.running = False
            self.endTime = int(time.time())
            self.finishButton.grid_forget()
            self.startButton.grid(row=3, column=0)
            self.update()

    def penalty(self):
        print("PENALTY!!")
        if self.running:
            self.penalties = self.penalties + 60

    def update(self):
        if self.running:
            self.endTime = int(time.time())
            elapsed = self.penalties + self.endTime - self.startTime
            hours = int(elapsed / 3600)
            minutes = int((elapsed / 60) - (hours * 60))
            seconds = int(elapsed - (hours * 3600) - (minutes * 60))
            self.timeDisplay.set(f"{hours:02d}:{minutes:02d}:{seconds:02d}")
            self.after_loop = self.after(300, self.update)

if __name__ == "__main__":
    app = Timesaver()
    app.mainloop()
