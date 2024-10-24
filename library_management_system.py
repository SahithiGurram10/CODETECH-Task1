# -*- coding: utf-8 -*-
"""Library Management System.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1x2X-8W92KYL8tnwb5RcHFTb0PGyIs3-l

# Libray Management System

**Step 1: Create or Load a Dataset**
"""

import pandas as pd

# Create a sample dataset for books
data = {
    'Title': ['Book A', 'Book B', 'Book C', 'Book D', 'Book E',
              'Book F', 'Book G', 'Book H', 'Book I', 'Book J'],
    'Pages': [200, 300, 150, 500, 450, 600, 350, 250, 400, 300],
    'Rating': [4.5, 4.0, 3.5, 4.7, 4.8, 3.9, 4.3, 3.8, 4.6, 4.2],
    'Price': [10.99, 15.99, 8.99, 20.99, 18.99, 22.99, 12.99, 14.99, 19.99, 17.99]
}

df = pd.DataFrame(data)

# Save the DataFrame to a CSV file
df.to_csv('library_books.csv', index=False)

# Display the DataFrame
print(df)

"""**Step 2:Load the Datset**

Next,load the dataset and prepare it for clustering.
"""

# Load the dataset
data = pd.read_csv('library_books.csv')

# Display the first few rows of the dataset
print(data.head())

"""**Step 3: Data Preprocessing**

# We wil sacle the numerical features to ensure all features contribute equally to distance calculations in clustering.
"""

from sklearn.preprocessing import StandardScaler

# Select numerical features for clustering
features = data[['Pages', 'Rating', 'Price']]

# Scale the features
scaler = StandardScaler()
scaled_features = scaler.fit_transform(features)

"""**Step 4: K-Means Clustering**

1.Apply K-means and evaluate the clustering results.
"""

from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score, davies_bouldin_score
import matplotlib.pyplot as plt

# Fit K-Means
kmeans = KMeans(n_clusters=3, random_state=42)
kmeans_labels = kmeans.fit_predict(scaled_features)

# Evaluate K-Means clustering
silhouette_kmeans = silhouette_score(scaled_features, kmeans_labels)
davies_bouldin_kmeans = davies_bouldin_score(scaled_features, kmeans_labels)
print(f'K-Means Silhouette Score: {silhouette_kmeans}')
print(f'K-Means Davies-Bouldin Index: {davies_bouldin_kmeans}')

"""**Step 5: Hierarchical Clustering**

1.Apply Hierarchical Clustering and visualize the dendrogram.
"""

from sklearn.cluster import AgglomerativeClustering
from scipy.cluster.hierarchy import dendrogram, linkage

# Hierarchical clustering
hier_clust = AgglomerativeClustering(n_clusters=3)
hier_labels = hier_clust.fit_predict(scaled_features)

# Evaluate Hierarchical clustering
silhouette_hier = silhouette_score(scaled_features, hier_labels)
davies_bouldin_hier = davies_bouldin_score(scaled_features, hier_labels)
print(f'Hierarchical Clustering Silhouette Score: {silhouette_hier}')
print(f'Hierarchical Clustering Davies-Bouldin Index: {davies_bouldin_hier}')

# Plot Dendrogram
linked = linkage(scaled_features, method='ward')
plt.figure(figsize=(10, 7))
dendrogram(linked, labels=data['Title'].values)
plt.title('Dendrogram')
plt.xlabel('Books')
plt.ylabel('Distance')
plt.show()

"""Step 6: DBSCAN Clustering

1.Apply DBSCAN and evaluate the results.
"""

from sklearn.cluster import DBSCAN

# DBSCAN clustering
dbscan = DBSCAN(eps=0.5, min_samples=2)
dbscan_labels = dbscan.fit_predict(scaled_features)

# Evaluate DBSCAN clustering
if len(set(dbscan_labels)) > 1:  # Check if there is more than one cluster
    silhouette_dbscan = silhouette_score(scaled_features, dbscan_labels)
    davies_bouldin_dbscan = davies_bouldin_score(scaled_features, dbscan_labels)
    print(f'DBSCAN Silhouette Score: {silhouette_dbscan}')
    print(f'DBSCAN Davies-Bouldin Index: {davies_bouldin_dbscan}')
else:
    print("DBSCAN did not find any clusters.")

"""**Step 7: Visualize the Clustering Results**

Visualize the clusters for k_means and DBSCAN.
"""

# Visualizing K-Means clusters
plt.figure(figsize=(10, 7))
plt.scatter(scaled_features[:, 0], scaled_features[:, 1], c=kmeans_labels, cmap='viridis', marker='o')
plt.title('K-Means Clustering')
plt.xlabel('Pages (scaled)')
plt.ylabel('Rating (scaled)')
plt.show()

# Visualizing DBSCAN clusters
plt.figure(figsize=(10, 7))
plt.scatter(scaled_features[:, 0], scaled_features[:, 1], c=dbscan_labels, cmap='plasma', marker='o')
plt.title('DBSCAN Clustering')
plt.xlabel('Pages (scaled)')
plt.ylabel('Rating (scaled)')
plt.show()

"""**Conclusion**

In this project, we explored unsupervised learning techniques through clustering analysis of a library dataset containing information about books. The dataset included features such as Pages, Rating, and Price. The main goals were to identify natural groupings of books based on these features and evaluate the effectiveness of different clustering algorithms.
"""