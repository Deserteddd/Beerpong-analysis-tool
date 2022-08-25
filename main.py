import matplotlib.pyplot as plt
from tkinter import *

class Team:
    def __init__(self, name:str, cups:int, total_throws:int, accuracy:float, hits:int):
        self.name = name
        self.cups = cups
        self.total_throws = total_throws
        self.accuracy = accuracy
        self.hits = hits
        self.throw_history = []

    def throw(self, hit:bool):
        self.throw_history.append((self.total_throws, hit))
        self.total_throws += 1
        if hit:
            self.hits += 1
        self.accuracy = self.hits/self.total_throws

class Main:
    def __init__(self):
        #main window
        self.root = Tk()
        self.root.title("Beerpong analysis tool - ver: 1.0")
        self.root.resizable(False, False)
        #hit/miss buttons
        self.team1_hit = Button(self.root, width=30, height=5, text="Osuma", command=lambda: self.gameEvent(team1, True))
        self.team1_hit.configure(background="Blue", foreground="White", font=("Arial", 20))
        self.team1_hit.grid(row=1, column=0)
        self.team1_miss = Button(self.root, width=30, height=5, text="Huti", command=lambda: self.gameEvent(team1, False))
        self.team1_miss.configure(background="Blue", foreground="White", font=("Arial", 20))
        self.team1_miss.grid(row=2, column=0)
        self.team2_hit = Button(self.root, width=30, height=5, text="Osuma" , command=lambda: self.gameEvent(team2, True))
        self.team2_hit.configure(background="Red", foreground="White", font=("Arial", 20))  
        self.team2_hit.grid(row=1, column=1)
        self.team2_miss = Button(self.root, width=30, height=5, text="Huti", command=lambda: self.gameEvent(team2, False))
        self.team2_miss.configure(background="Red", foreground="White", font=("Arial", 20))
        self.team2_miss.grid(row=2, column=1)
        #total throws
        self.t1_throws = StringVar()
        self.t1_throws.set(f'Heitot: {team1.total_throws}')
        self.t1_throws_label = Label(self.root, font=("Arial", 16), textvariable=self.t1_throws)
        self.t1_throws_label.grid(row=3, column=0, sticky=W)
        self.t2_throws = StringVar()
        self.t2_throws.set(f'Heitot: {team1.total_throws}')
        self.t2_throws_label = Label(self.root, font=("Arial", 16), textvariable=self.t2_throws)
        self.t2_throws_label.grid(row=3, column=1, sticky=W)
        #remaining cups
        self.t1_cups = StringVar()
        self.t1_cups.set(f'Kuppeja: {team1.cups}')
        self.team1_cups_label = Label(self.root, font=("Arial", 16), textvariable=self.t1_cups)
        self.team1_cups_label.grid(row=4, column=0, sticky=W)
        self.t2_cups = StringVar()
        self.t2_cups.set(f'Kuppeja: {team2.cups}')
        self.team2_cups_label = Label(self.root, font=("Arial", 16), textvariable=self.t2_cups)
        self.team2_cups_label.grid(row=4, column=1, sticky=W)
        #accuracy indicator
        self.t1_accuracy = StringVar()
        self.t1_accuracy.set(f"Tarkkuus: {team1.accuracy}%")
        self.team1_accuracy = Label(self.root, font=("Arial", 16), textvariable=self.t1_accuracy)
        self.team1_accuracy.grid(row=5, column=0, sticky=W)
        self.t2_accuracy = StringVar()
        self.t2_accuracy.set(f"Tarkkuus: {team2.accuracy}%")
        self.team2_accuracy = Label(self.root, font=("Arial", 16), textvariable=self.t2_accuracy)
        self.team2_accuracy.grid(row=5, column=1, sticky=W)

        #mainloop
        self.root.mainloop()

    def updateText(self):  
                self.t1_cups.set(f'Kuppeja: {team1.cups}')
                self.t2_cups.set(f'Kuppeja: {team2.cups}')
                self.t1_accuracy.set(f"Tarkkuus: {round(team1.accuracy*100, 1)}%")
                self.t2_accuracy.set(f"Tarkkuus: {round(team2.accuracy*100, 1)}%")
                self.t1_throws.set(f'Heitot: {team1.total_throws}')
                self.t2_throws.set(f'Heitot: {team2.total_throws}')

    def gameEvent(self, team: Team, hit: bool):
        if team == team1:
            opponent = team2
        else:
            opponent = team1
        if hit:
            team.throw(True)
            opponent.cups -= 1
            self.updateText()
        else:
            team.throw(False)
            self.updateText()
        if opponent.cups == 0:
            self.root.destroy()
            self.plotEverything()     

    def plotEverything(self):    
        plt.plot(self.shotListInterpeter(team1), "b")
        plt.plot(self.shotListInterpeter(team2), "r")
        plt.xlabel("Heitot")
        plt.ylabel("Osumat")
        plt.show()

    def shotListInterpeter(self,team: Team):
        return_list = []
        counter = 0
        for i in team.throw_history:
            if i[1] == True:
                counter += 1
                return_list.append(counter)
            else:
                return_list.append(counter)
        return return_list

team1 = Team("Blue", cups=10, total_throws=0, accuracy=0, hits=0)
team2 = Team("Red", cups=10, total_throws=0, accuracy=0, hits=0)

if __name__ == "__main__":
    Main()
