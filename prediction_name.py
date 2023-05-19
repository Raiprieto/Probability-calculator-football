import tkinter as tk
from tkinter import ttk
from calculations import *
from scraping_stats import *

global df

df = pd.read_csv('fixture.csv')

class PredictGameApp(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("Predict Game App")
        self.pack()
        self.create_widgets()
    def create_widgets(self):
    # Set the font and size for the entire application
        self.master.option_add('*Font', 'Helvetica 12')

        # Create a style sheet for the buttons
        self.style = ttk.Style()
        self.style.configure('GameButton.TButton', padding=10, font=('Helvetica', 16), background='#4CAF50', foreground='#598687')
        self.style.map('GameButton.TButton', background=[('active', '#466170')])

        # Create labels and entry boxes for each input parameter
        tk.Label(self, text="Home Team", font=('Inter', 20)).grid(row=0, column=0, padx=20, pady=20, sticky='w')
        self.home_team_entry = tk.Entry(self, font=('Inter', 20))
        self.home_team_entry.grid(row=0, column=1, padx=20, pady=20)

        tk.Label(self, text="Away Team", font=('Helvetica', 20)).grid(row=2, column=0, padx=20, pady=20, sticky='w')
        self.away_team_entry = tk.Entry(self, font=('Helvetica', 20))
        self.away_team_entry.grid(row=2, column=1, padx=20, pady=20)


        # Create a button to call the predict_game function
        self.predict_button = ttk.Button(self, text="Predict outcome", style='GameButton.TButton', command=self.match)
        self.predict_button.grid(row=4, column=0, columnspan=2, padx=20, pady=20)

        # Create a label to display the predicted probabilities
        tk.Label(self, text="Home Odds", font=('Helvetica', 20)).grid(row=5, column=0, padx=20, pady=20)
        self.result_label1 = tk.Button(self, text="", font=('Helvetica', 24), fg='#598687')
        self.result_label1.grid(row=5, column=1, padx=20, pady=20)

        tk.Label(self, text="Draw", font=('Helvetica', 20)).grid(row=6, column=0, padx=20, pady=20)
        self.result_label2 = tk.Button(self, text="", font=('Helvetica', 24), fg='#598687')
        self.result_label2.grid(row=6, column=1, padx=20, pady=20)

        tk.Label(self, text="Away Odds", font=('Helvetica', 20)).grid(row=7, column=0, padx=20, pady=20)
        self.result_label3 = tk.Button(self, text="", font=('Helvetica', 24), fg='#598687')
        self.result_label3.grid(row=7, column=1, padx=20, pady=20)

        self.result_label4 = tk.Label(self, text="", font=('Helvetica', 24), fg='#598687')
        self.result_label4.grid(row=8, column=0, columnspan=3, padx=20, pady=20, sticky="nsew")


    def match(self):

        home_team = self.home_team_entry.get()
        away_team = self.away_team_entry.get()

        home_win_odds, draw_odds, away_win_odds = find_match(home_team, away_team, df)

        result_text1 = "{:.2f}".format(home_win_odds)
        result_text2 = " {:.2f}".format(draw_odds)
        result_text3 = " {:.2f}".format(away_win_odds)
        result_text4 = "If the bookies offer more, bet"
        self.result_label1.configure(text=result_text1)
        self.result_label2.configure(text=result_text2)
        self.result_label3.configure(text=result_text3)
        self.result_label4.configure(text=result_text4)



