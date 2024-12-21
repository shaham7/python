import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('billboard_top_100_with_genres.csv')

df_genres = df['Genres'].str.split(', ', expand=True).stack().reset_index(level=1, drop=True)
df_genres.name = 'Genre'

df_expanded = df[['Popularity']].join(df_genres)

genre_popularity = df_expanded.groupby('Genre')['Popularity'].mean().sort_values(ascending=False).head(10)

# Plot the data
plt.figure(figsize=(12, 6))
sns.barplot(x=genre_popularity.values, y=genre_popularity.index, palette='coolwarm')
plt.title('Top 10 Genres by Average Popularity', fontsize=14)
plt.xlabel('Average Popularity', fontsize=12)
plt.ylabel('Genre', fontsize=12)
plt.tight_layout()
plt.show()
