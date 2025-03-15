# Customer Segmentation Behaviour Analysis

This project applies machine learning techniques to segment customers based on their purchasing behaviors. By clustering customers, this project identifies different customer groups, which can inform targeted marketing strategies and improve business decision-making. The clustering is performed using the KMeans algorithm, and various cluster performance metrics are assessed for a deeper understanding of the customer base.

# Project Overview

In this project, I use customer data to perform segmentation based on behavioral metrics using RFM Analysis such as frequency of purchases, total monetary expenditure, and recency of purchase. These segments can help businesses tailor their marketing efforts, retention strategies, and overall customer experience.

# Key Features

**Customer Segmentation** using KMeans clustering to identify distinct groups.

**Silhouette Score, Davies-Bouldin Score, and Calinski-Harabasz Score** for evaluating the clustering quality.

**Radar Chart Visualization** for understanding the characteristics of each cluster.

**Cluster Insights** including customer behavior, spending patterns, and business recommendations for each group.

**Table of Contents**

1. Data Loading
2. Data Preprocessing
3. Clustering and Segmentation
4. Model Evaluation
5. Visualization
6. Business Insights
7. How to Use
8. License

**Project Setup**

**Requirements**
  * Python 3.x
  * Libraries:
  * pandas
  * numpy
  * scikit-learn
  * matplotlib
  * seaborn
  * tabulate
  * scipy
    
To install the dependencies, you can use the following pip command:

  * pip install -r requirements.txt

**Data Preprocessing**

**Load Data:** The data is loaded from a CSV file containing customer transactional data.

**Standardization:** The features are scaled using standardization techniques to ensure they are on the same scale for clustering.

**Feature Selection:** Key features such as **Recency, Frequency, Monetary, Total_Products and Avg_Monetary_Value** are selected for clustering.

**Missing Data Handling:** Any missing values in the dataset are handled appropriately using removal methods.

**Clustering and Segmentation**

**KMeans Clustering** is used to segment the customers into 3 clusters based on their transactional behavior.

The number of clusters was chosen based on prior analysis, which suggests 3 distinct customer segments.

**Model Parameters:**
  * n_clusters=3 (3 customer segments)
  * random_state=42 (for reproducibility)

**Model Evaluation**

To assess the clustering performance, the following evaluation metrics are used:

1. **Silhouette Score:** Measures how similar an object is to its own cluster compared to other clusters. Higher scores indicate better-defined clusters.
   
2. **Calinski-Harabasz Score:** Measures the ratio of the sum of between-cluster dispersion to within-cluster dispersion. Higher values indicate better-defined clusters.
   
3. **Davies-Bouldin Score:** Measures the average similarity ratio of each cluster with its most similar cluster. Lower scores indicate better separation of clusters.

**Results:KMeans**

**Silhouette Score:** 0.61 (indicating average separation between clusters)

**Calinski-Harabasz Score:** 5605 (indicating good clustering quality)

**Davies-Bouldin Score:** 0.51 (indicating moderate separation)

**Visualization**

**Radar Chart**

Radar charts are generated for each cluster to visualize the average behavior of customers in that segment across various features.

Each cluster is represented by a different color, and the features are plotted on a circular axis to easily compare the behaviors.

**Cluster Distribution**

A bar plot shows the percentage distribution of customers across the 3 clusters, providing insights into the balance of customer segments.

**Business Insights**

1. **Cluster 0:** contains inactive or Churned Customers that haven’t purchased in a long time. 

   **Key strategies to implement: Win-Back Plan for Churned Customers** – Personalized offers, reminders, and surveys

2. **Cluster 1: Average or Regular Customers:** shows customers that  have purchased relatively recently, these customers  purchase at an average rate, spend a typical amount, and buy a standard number of products.

   **Key strategies to implement: Retention Plan for Regular Buyers** – Product recommendations, exclusive deals, and loyalty rewards.

3. **Cluster 2: High-Value, Loyal Customers:**  shows that these customers buy frequently and recently, these customers  purchase very often, spend significantly more, and buy a lot of products.

   **Key strategies to implement: VIP Customer Strategy** – Premium services, early access to deals, and personalized engagement.
    
**How to Use**

1. Clone the repository:

  * git clone https://github.com/yourusername/customer-segmentation-analysis.git

2. Install the required dependencies:

  * pip install -r requirements.txt

3. Run the analysis:
 
Open the **customer_segment.ipynb** script to run the KMeans clustering and generate visualizations.

Modify the dataset path or customize the number of clusters as needed.

**License**
This project is licensed under the MIT License - see the LICENSE file for details.

**Acknowledgements**

**Customer Data:** The dataset used in this project was provided by [amdari].

**KMeans Algorithm:** Clustering performed using the scikit-learn library.

This README.md provides an in-depth guide on setting up, running, and interpreting the results of your customer segmentation project.










