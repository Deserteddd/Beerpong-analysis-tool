# import matplotlib.pyplot as plt
from tkinter import *
from ctypes import windll
windll.shcore.SetProcessDpiAwareness(1)


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
    def __init__(self, team1: Team, team2: Team):
        self.team1 = team1
        self.team2 = team2
        #main window
        self.root = Tk()
        self.root.title("Beerpong analysis tool - ver: 1.0")
        self.root.resizable(False, False)
        #team names
        self.t1_name_label = Label(self.root, font=("Arial", 16), text=team1.name)
        self.t1_name_label.grid(row=0, column=0, sticky=W)
        self.t2_name_label = Label(self.root, font=("Arial", 16), text=team2.name)
        self.t2_name_label.grid(row=0, column=1, sticky=W)
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
                self.t1_cups.set(f'Kuppeja: {self.team1.cups}')
                self.t2_cups.set(f'Kuppeja: {self.team2.cups}')
                self.t1_accuracy.set(f"Tarkkuus: {round(self.team1.accuracy*100, 1)}%")
                self.t2_accuracy.set(f"Tarkkuus: {round(self.team2.accuracy*100, 1)}%")
                self.t1_throws.set(f'Heitot: {self.team1.total_throws}')
                self.t2_throws.set(f'Heitot: {self.team2.total_throws}')

    def gameEvent(self, team: Team, hit: bool):
        if team == self.team1:
            opponent = self.team2
        else:
            opponent = self.team1
        if hit:
            team.throw(True)
            opponent.cups -= 1
            self.updateText()
        else:
            team.throw(False)
            self.updateText()
        if opponent.cups == 0:
            self.root.destroy()
            # self.plotEverything()     

    # def plotEverything(self):    
    #     plt.plot(self.shotListInterpeter(self.team1), "b")
    #     plt.plot(self.shotListInterpeter(self.team2), "r")
    #     plt.xlabel("Heitot")
    #     plt.ylabel("Osumat")
    #     plt.show()
    #     pass

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

class Start:
    # Set team
    def __init__(self):
        self.root = Tk()
        self.root.title("Beerpong analysis tool - ver: 1.0")
        # Team name entries
        self.t1_name_var = StringVar(value='Sininen joukkue')
        self.t2_name_var = StringVar(value='Punainen joukkue')
        self.t1_name = Entry(self.root, textvariable=self.t1_name_var, width=25, font=('Arial', 14)).grid(row=1, column=2, sticky=W)
        self.t2_name = Entry(self.root, textvariable=self.t2_name_var, width=25, font=('Arial', 14)).grid(row=1, column=3, sticky=W)
        #Labels
        self.t1_name_label = Label(self.root, text='Joukkue 1').grid(row=0, column=2, sticky=W)
        self.t2_name_label = Label(self.root, text='Joukkue 2').grid(row=0, column=3, sticky=W)
        self.cups_label = Label(self.root, text='Kupit').grid(row=3, column=1, sticky=W)
        self.name_label = Label(self.root, text='Nimi').grid(row=1, column=1, sticky=W)
        # Cups
        self.t1_cups_var = IntVar(value=10)
        self.t2_cups_var = IntVar(value=10)
        self.t1_cups = Entry(self.root, textvariable=self.t2_cups_var, width=5, font=('Arial', 14)).grid(row=3, column=2, sticky=W)
        self.t2_cups = Entry(self.root, textvariable=self.t2_cups_var, width=5, font=('Arial', 14)).grid(row=3, column=3, sticky=W)

        # Buttons
        start_button = Button(self.root, text='Aloita', font=('Arial', 14), command=lambda: self.start_main())
        start_button.grid(row=5, column=3, sticky=E)

        self.root.mainloop()
    
    def start_main(self):
        t1_cups = self.t1_cups_var.get()
        t2_cups = self.t2_cups_var.get()        
        team1 = Team(self.t1_name_var.get(), t1_cups, total_throws=0, accuracy=0, hits=0)
        team2 = Team(self.t2_name_var.get(), t2_cups, total_throws=0, accuracy=0, hits=0)
        self.root.destroy()
        Main(team1, team2)


if __name__ == "__main__":
    Start()
