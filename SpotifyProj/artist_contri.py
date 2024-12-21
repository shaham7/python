import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('billboard_top_100_with_genres.csv')

df_artists = df['Artist'].str.split(', ', expand=True).stack().reset_index(level=1, drop=True)
df_artists.name = 'Artist'

df_genres = df['Genres'].str.split(', ', expand=True).stack().reset_index(level=1, drop=True)
df_genres.name = 'Genre'

df_expanded = df[['Name', 'Popularity']].join(df_artists).join(df_genres)

artist_genre_popularity = (
    df_expanded.groupby(['Genre', 'Artist'])['Popularity']
    .mean()
    .reset_index()
    .sort_values(by=['Genre', 'Popularity'], ascending=[True, False])
)

top_artist_genre_popularity = artist_genre_popularity.loc[
    artist_genre_popularity.groupby('Genre')['Popularity'].idxmax()
]

# top artist popularity for each genre
plt.figure(figsize=(14, 40))
sns.barplot(
    x='Popularity', y='Genre', hue='Artist', data=top_artist_genre_popularity, dodge=False, palette='tab10'
)
plt.title('Top Artists by Average Popularity for Each Genre', fontsize=16)
plt.xlabel('Average Popularity', fontsize=14)
plt.ylabel('Genre', fontsize=14)
plt.legend(title='Artist', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show()

# this doesn't work properly because too many data points and I cant currently think of hwo to fix this 