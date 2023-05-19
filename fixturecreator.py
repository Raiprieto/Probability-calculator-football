from scipy.stats import poisson
from scraping_stats import *
from calculations import *


df = la_liga_stats()
df = createfixture(df)

df2 = premier_stats()
df2 = createfixture(df2)

df3 = ligue1_stats()
df3 = createfixture(df3)

df4 = bundes_stats()
df4 = createfixture(df4)

df5 = eredivisie_stats()
df5 = createfixture(df5)

df6 = serieA_stats()
df6 = createfixture(df6)

df_combined = pd.concat([df, df2, df3, df4, df5, df6])

df_combined.to_csv('fixture.csv', index=False)