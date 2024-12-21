import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('billboard_top_100_with_genres.csv')

df_artists = df['Artist'].str.split(', ', expand=True).stack().reset_index(level=1, drop=True)
df_artists.name = 'Artist'

artist_counts = df_artists.value_counts().head(10)  

# Plot the data
plt.figure(figsize=(10, 6))
sns.barplot(x=artist_counts.values, y=artist_counts.index, palette='viridis')
plt.title('Top 10 Artists with the Most Songs on the Billboard Top 100', fontsize=14)
plt.xlabel('Number of Songs', fontsize=12)
plt.ylabel('Artist', fontsize=12)
plt.tight_layout()
plt.show()
