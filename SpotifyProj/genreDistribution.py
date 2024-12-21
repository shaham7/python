import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('billboard_top_100_with_genres.csv')

df_genres = df['Genres'].str.split(', ', expand=True).stack().reset_index(level=1, drop=True)
df_genres.name = 'Genre'

genre_counts = df_genres.value_counts().head(10) 

# pie chart for genre distribution
plt.figure(figsize=(8, 8))
genre_counts.plot.pie(autopct='%1.1f%%', startangle=140, cmap='tab20')
plt.title('Genre Distribution on the Billboard Top 100', fontsize=14)
plt.ylabel('')  # Removing y-axis label because its pointless
plt.tight_layout()
plt.show()
