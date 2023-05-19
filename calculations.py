from scipy.stats import poisson
from itertools import product
import pandas as pd

def predict_game(home_goals_avg, home_against, away_goals_avg, away_against):
   

   
    m_home = []
    m_draw = []
    m_away = []


    for i in range(6):
        for k in range(6):
            prob = poisson.pmf(i,(home_goals_avg+away_against)/2) * poisson.pmf(k, (away_goals_avg + home_against)/2)
            if i>k:
                m_home.append(prob)

            if i<k:
                m_away.append(prob)

            if i==k:
                m_draw.append(prob)





    return 1/sum(m_home), 1/sum(m_draw) , 1/sum(m_away)


def createfixture(df1):
    # extract team names from first column
    team_names = df1.iloc[:, 0].values

    # generate all possible combinations of matches
    matches = [(home, away) for home, away in product(team_names, repeat=2) if home != away]

    # create an empty dataframe with the desired columns
    df2 = pd.DataFrame(columns=['Home_team', 'Away_team', 'Home_win', 'Draw', 'Away_win'])

    # iterate over all possible matches and apply predict_game() function
    for match in matches:
        home_team = match[0]
        away_team = match[1]
        PJh, xGh, xGAh  = df1.loc[df1.iloc[:, 0] == home_team, ['PJh','xGh','xGAh']].values[0]
        PJv, xGv, xGAv =  df1.loc[df1.iloc[:, 0] == away_team, ['PJv', 'xGv', 'xGAv']].values[0]
        
        home_win, draw, away_win = predict_game(float(xGh)/float(PJh), float(xGAh)/float(PJh), float(xGv)/float(PJv), float(xGAv)/float(PJv))
        df2 = df2.append({'Home_team': home_team,
                          'Away_team': away_team,
                          'Home_win': home_win,
                          'Draw': draw,
                          'Away_win': away_win}, ignore_index=True)

    return df2


def find_match(home, away, df):
    for i, row in df.iterrows():
        if home in row['Home_team'] and away in row['Away_team']:
            x = df['Home_win'][i]
            y = df['Draw'][i]
            z = df['Away_win'][i]
            return x, y, z