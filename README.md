# 🎵 Song Recommendation System using Clustering and PCA

This project builds an intelligent song recommendation system using unsupervised machine learning techniques such as KMeans clustering and PCA dimensionality reduction. The goal is to explore music data, identify clusters of similar songs, and provide song suggestions based on user input.

---

## Project Goals

- Perform **Exploratory Data Analysis (EDA)** on music features.
- Preprocess and **encode categorical features** like genre and explicit content.
- Apply **KMeans clustering** to group similar songs.
- Use **PCA (Principal Component Analysis)** to reduce dimensionality for visualization.
- Build an **interactive song recommender**.
- Deploy a user-friendly system via widgets.

---

## Dataset

The dataset contains 6,300 songs with attributes like:

- `name`, `artists`, `popularity`, `duration_ms`
- `genre`, `explicit`, and many audio features.

---

## Tools & Libraries

- Python, Jupyter Notebook
- Pandas, NumPy, Matplotlib, Seaborn
- Scikit-learn (StandardScaler, KMeans, PCA)
- IPyWidgets (for interaction)

---
## Steps Followed

### 1. **Exploratory Data Analysis**
- Analyzed genre distributions, popularity, outliers using boxplots and heatmaps.

### 2. **Preprocessing**
- Handled outliers.
- Encoded `genre` and `explicit` using one-hot encoding.
- Standardized all numerical features.

### 3. **Clustering with KMeans**
- Used the Elbow Method to choose the optimal number of clusters.
- Assigned each song to a cluster for recommendation logic.

### 4. **Dimensionality Reduction with PCA**
- Reduced feature space to 2D using PCA.
- Visualized clusters using a scatter plot.

### 5. **Recommendation System**
- Matched input song to a cluster.
- Recommended similar songs from the same cluster.
- Built interactive dropdown with widgets to select and get recommendations.

---

## How to Use

1. Clone this repository:
   ```bash
   git clone https://github.com/Lydi-0317/song-recommendation-system.git
   cd song-recommendation-system
