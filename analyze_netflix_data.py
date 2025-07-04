
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import seaborn as sns

# Carregar o dataset
df = pd.read_csv("netflix_titles.csv")

# Preencher valores nulos nas colunas relevantes para evitar erros
df["description"] = df["description"].fillna("")
df["listed_in"] = df["listed_in"].fillna("")

# Combinar descrição e gêneros para uma representação mais rica
df["combined_features"] = df["description"] + " " + df["listed_in"]

# Vetorizar o texto usando TF-IDF
tfidf_vectorizer = TfidfVectorizer(stop_words="english", max_features=5000)
tfidf_matrix = tfidf_vectorizer.fit_transform(df["combined_features"])

# Aplicar K-Means Clustering
# Vamos tentar 5 clusters como um ponto de partida
num_clusters = 5
kmeans_model = KMeans(n_clusters=num_clusters, init='k-means++', max_iter=300, n_init=10, random_state=42)
df["cluster"] = kmeans_model.fit_predict(tfidf_matrix)

# Visualização dos resultados
plt.figure(figsize=(12, 6))
sns.countplot(data=df, x='cluster', palette='viridis')
plt.title('Distribuição de Conteúdo por Cluster')
plt.xlabel('Cluster')
plt.ylabel('Número de Títulos')
plt.savefig('cluster_distribution.png')

# Exibir os 5 principais termos para cada cluster
print('\nPrincipais termos por cluster:')
order_centroids = kmeans_model.cluster_centers_.argsort()[:, ::-1]
terms = tfidf_vectorizer.get_feature_names_out()
for i in range(num_clusters):
    print(f'Cluster {i}:')
    for ind in order_centroids[i, :5]:
        print(f' {terms[ind]}')

# Exibir alguns títulos de exemplo para cada cluster
print('\nExemplos de títulos por cluster:')
for i in range(num_clusters):
    print(f'Cluster {i}:')
    print(df[df['cluster'] == i]['title'].sample(min(5, len(df[df['cluster'] == i]))).tolist())

# Análise de tipos de conteúdo por cluster
plt.figure(figsize=(12, 6))
sns.countplot(data=df, x='cluster', hue='type', palette='magma')
plt.title('Distribuição de Tipos de Conteúdo por Cluster')
plt.xlabel('Cluster')
plt.ylabel('Número de Títulos')
plt.savefig('type_distribution_by_cluster.png')

# Análise de países por cluster (top 5 países por cluster)
plt.figure(figsize=(15, 8))
country_cluster = df.groupby('cluster')['country'].value_counts().groupby(level=0).head(5).reset_index(name='count')
sns.barplot(data=country_cluster, x='cluster', y='count', hue='country', palette='plasma')
plt.title('Top 5 Países por Cluster')
plt.xlabel('Cluster')
plt.ylabel('Número de Títulos')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig('country_distribution_by_cluster.png')

print('Análise de clustering concluída e gráficos salvos.')


