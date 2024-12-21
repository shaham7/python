import pandas as pd
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('billboard_top_100_with_genres.csv')

artists = df['Artist'].str.split(', ', expand=True).stack().reset_index(level=1, drop=True)
artists.name = 'Artist'

df_genres = df['Genres'].str.split(', ', expand=True).stack().reset_index(level=1, drop=True)
df_genres.name = 'Genre'

df_expanded = df[['Name', 'Popularity']].join(artists).join(df_genres)

genre_counts = df_genres.value_counts().head(10)
artist_counts = artists.value_counts().head(10)  

artist_genre_counts = df_expanded.groupby(['Genre', 'Artist']).size().reset_index(name='Count')


artist_genre_popularity = (
    df_expanded.groupby(['Genre', 'Artist'])['Popularity']
    .mean()
    .reset_index()
    .sort_values(by=['Genre', 'Popularity'], ascending=[True, False])
)


top_artist_genre_popularity = artist_genre_popularity.loc[
    artist_genre_popularity.groupby('Genre')['Popularity'].idxmax()
]

# Genre Distribution dash
st.title('Billboard Top 100 Analysis Dashboard')
st.header('Genre Distribution')
fig, ax = plt.subplots(figsize=(10, 5))
sns.barplot(x=genre_counts.values, y=genre_counts.index, ax=ax, palette='mako')
ax.set_title('Top 10 Genres')
ax.set_xlabel('Number of Songs')
ax.set_ylabel('Genre')
st.pyplot(fig)

# Artist Contributions dash / should add a dorpdown
st.header('Artist Contributions to Genres')
selected_genre = st.selectbox('Select a Genre', artist_genre_counts['Genre'].unique())
genre_data = artist_genre_counts[artist_genre_counts['Genre'] == selected_genre]
fig, ax = plt.subplots(figsize=(10, 5))
sns.barplot(x='Count', y='Artist', data=genre_data, ax=ax, palette='tab10')
ax.set_title(f'Artist Contributions in {selected_genre}')
ax.set_xlabel('Number of Songs')
ax.set_ylabel('Artist')
st.pyplot(fig)

# Top Artists dash
st.header('Top 10 Artists with the Most Songs on the Billboard Top 100')
fig, ax = plt.subplots(figsize=(10, 5))
sns.barplot(x=artist_counts.values, y=artist_counts.index, ax=ax, palette='mako')
ax.set_title('Top 10 Artists with most songs')
ax.set_xlabel('Number of Songs')
ax.set_ylabel('Artist')
st.pyplot(fig)

# streamlit run dashboard.py
