# Customer Segmentation Behaviour Analysis


<img width="960" alt="image" src="https://github.com/user-attachments/assets/28e6153e-9fe4-4879-9dc3-0ba560604810" />

This project applies machine learning techniques to segment customers based on their purchasing behaviors. By clustering customers, this project identifies different customer groups, which can inform targeted marketing strategies and improve business decision-making. The clustering is performed using the KMeans algorithm, and various cluster performance metrics are assessed for a deeper understanding of the customer base.

## Project Overview

In this project, customer data was used to perform segmentation based on behavioral metrics using RFM Analysis such as frequency of purchases, total monetary expenditure, and recency of purchase. These segments can help businesses tailor their marketing efforts, retention strategies, and overall customer experience.

## Business Introduction

The focal company is a leading online retailer offering a wide range of products, including electronics, apparel, and home goods. With millions of customers globally, the business prides itself on its fast delivery, customer-centric policies, and personalized shopping experience. Some major achievements highlighted by the company include:
* Growth in user base by 30% annually over the last five years.
* Implementation of a personalized recommendation system, improving customer satisfaction.
* Achieved 80% retention rate among VIP customers in the first two years of loyalty program implementation.
  
Despite its numerous successes, the company has encountered a formidable challenge that has left its leadership team determined to find a solution: an alarmingly high shopping cart abandonment rate.

## Business Problem

The company is facing a significant challenge in retaining customers over time. While the company experiences high customer acquisition rates, they are seeing a drop-off in returning customers after the first purchase. Specific challenges include:

* Declining repeat purchase rate: New customers are not returning after their initial purchase.
* Customer churn: A noticeable percentage of customers leave after a brief period of activity, increasing marketing and acquisition costs.
* Low engagement: Customers show decreased interaction with the platform after their first few visits, indicating a failure to maintain long-term interest.
  
Resolving these issues is critical for improving customer lifetime value (CLV) and overall business growth.

## Project Objectives
* Retention Rate Analysis: Measure and evaluate customer retention rates across different cohorts over time.
* Customer Segmentation: Group customers into distinct clusters based on shared characteristics or behaviors, utilizing methods like RFM analysis.
* Churn Analysis: To pinpoint the reasons and timing of customer churn within various cohorts and build a predictive model that can be used to predict churn behavior.
* Recommendation Strategies: Develop data-driven recommendations to enhance customer retention, leveraging insights from cohort analysis and segmentation.

## Data Description
1. InvoiceNo: Code representing each unique transaction.
2. StockCode: Code uniquely assigned to each distinct product.
3. Description: Description of each product.
4. Quantity: The number of units of a product in a transaction.
5. InvoiceDate: The date and time of the transaction.
6. UnitPrice: The unit price of the product in sterling.
7. CustomerID: Identifier uniquely assigned to each customer.
8. Country: The country of the customer.

## Data Preprocessing & Exploratory Data Analysis (EDA)
The Customer ID column(important feature) had 25% missing values and were dropped to prevent introduction of bias.

### 1. Monthly Sales Trend

<img width="545" alt="image" src="https://github.com/user-attachments/assets/ccff51b8-b2b5-493c-99a0-e933f3fe8875" />

The sales trend analysis reveals clear seasonal patterns of significant surge in sales occurs in the second half of the year, particularly from September to November 2011, likely driven by holiday shopping or promotional activities and a sharp decline follows from December 2011 to February 2011, possibly due to reduced activity after the holiday peak.

### 2. Cutomer Retention Cohort Analysis

<img width="527" alt="image" src="https://github.com/user-attachments/assets/6b72556a-8ab8-470c-897d-e8119c3f232d" />

   * Customer Percentage Retention Analysis: Analyzing the heatmap, the average benchmark retention rate ranges between 30% and 40%. Notably, only December 2010 managed to sustain this 
     benchmark, even achieving a 50% retention rate by the 12th month. This is followed by January 2011, which also performed relatively well. In contrast, other months have maintained 
     lower retention rates, ranging between 20% and 29%.
   

## Feature Engineering, Selection, and Dimensionality Reduction

### Feature Engineering:
The features are scaled using standardization techniques to ensure they are on the same scale for clustering and new features were createds based on RFM Analysis:

1. Recency (R) Recency measures how recently a customer has made a purchase, providing insights into their engagement with the business.
2. Frequency (F): measures total number of unique transactions made by a customer
3. Monetary: measures the total amount spent by each customer.

### Feature Scaling and PCA: 
1. Scaling: Here, it's crucial to scale the features, as  this is vital for distance-based methods 
            like K-means and PCA and features with larger ranges can dominate, leading to biased      
            clustering.
2. PCA:     Reveals that three features can account for 81% can explained the variance to perform                       the clustering.

## Model Selection, Training and Evaluation
1. Optimal Clusters Analysis: To ascertain the optimal number of clusters (k) for segmenting customers, two renowned methods were used - Elbow Method and  Silhouette Method and both method suggest that optimal k = 4.

<img width="561" alt="image" src="https://github.com/user-attachments/assets/59b2b544-0f0d-41e5-987f-1feec1f51375" />

2. Models Selection: To select the best model to use, hyperparameter tunning were performed on Four(4) models to dentify the optimal number of clusters for customer segmentation:
   
   - **KMeans** : Clusters data by minimizing the variance within each cluster using centroid-based     
                  partitioning.
   - **Agglomerative Clustering**: A hierarchical clustering method that iteratively merges the closest 
                  pairs of clusters.
   - **Hierarchical Clustering:** Builds a tree-like structure (dendrogram) to show nested clusters formed 
                  through either merging (agglomerative) or splitting (divisive).
   - **DBSCAN (Density-Based Spatial Clustering of Applications with Noise):** Groups data points based on 
                   density, identifying clusters of arbitrary shapes and noise points. 

4. Evaluation Metrtics:

The results for each cluster size were then compared using Silhouette Score, Davies-Bouldin Score, and Calinski-Harabasz Score for evaluating the clustering quality;

  

  <img width="322" alt="image" src="https://github.com/user-attachments/assets/da6e52c9-3725-430a-9498-c9ad7b6f2e15" />



 



# Key Features

**Customer Segmentation** using KMeans clustering to identify distinct groups.

**Silhouette Score, Davies-Bouldin Score, and Calinski-Harabasz Score** for evaluating the clustering quality.

**Radar Chart Visualization** for understanding the characteristics of each cluster.

**Cluster Insights** including customer behavior, spending patterns, and business recommendations for each group.


## Results

**Clustering and Segmentation**

**KMeans Clustering** is used to segment the customers into 3 clusters based on their transactional behavior.

The number of clusters was chosen based on prior analysis, which suggests 3 distinct customer segments.

**Model Parameters:**
  * n_clusters=3 (3 customer segments)
  * random_state=42 (for reproducibility)

## Model Evaluation

To assess the clustering performance, the following evaluation metrics are used:

1. **Silhouette Score:** Measures how similar an object is to its own cluster compared to other clusters. Higher scores indicate better-defined clusters.
   
2. **Calinski-Harabasz Score:** Measures the ratio of the sum of between-cluster dispersion to within-cluster dispersion. Higher values indicate better-defined clusters.
   
3. **Davies-Bouldin Score:** Measures the average similarity ratio of each cluster with its most similar cluster. Lower scores indicate better separation of clusters.

### Results:KMeans

**Silhouette Score:** 0.61 (indicating average separation between clusters)

**Calinski-Harabasz Score:** 5605 (indicating good clustering quality)

**Davies-Bouldin Score:** 0.51 (indicating moderate separation)

**Visualization**

**Radar Chart**

Radar charts are generated for each cluster to visualize the average behavior of customers in that segment across various features.

Each cluster is represented by a different color, and the features are plotted on a circular axis to easily compare the behaviors.

**Cluster Distribution**

A bar plot shows the percentage distribution of customers across the 3 clusters, providing insights into the balance of customer segments.

# **Business Insights**

1. **Cluster 0:** contains inactive or Churned Customers that haven’t purchased in a long time. 

   **Key strategies to implement: Win-Back Plan for Churned Customers** – Personalized offers, reminders, and surveys

2. **Cluster 1: Average or Regular Customers:** shows customers that  have purchased relatively recently, these customers  purchase at an average rate, spend a typical amount, and buy a standard number of products.

   **Key strategies to implement: Retention Plan for Regular Buyers** – Product recommendations, exclusive deals, and loyalty rewards.

3. **Cluster 2: High-Value, Loyal Customers:**  shows that these customers buy frequently and recently, these customers  purchase very often, spend significantly more, and buy a lot of products.

   **Key strategies to implement: VIP Customer Strategy** – Premium services, early access to deals, and personalized engagement.


**Project Setup**
** Tech Stack**
  * Python 3.x
  * Libraries:
  * pandas
  * numpy
  * scikit-learn
  * matplotlib
  * seaborn
  * tabulate
  * scipy
     
**How to Use**

1. Clone the repository:

  * git clone 'the folder'

2. Install the required dependencies:

  * pip install -r requirements.txt

3. Run the analysis:
 
  * Open the **customer_segment.ipynb** script to run the KMeans clustering and generate visualizations.

  * Modify the dataset path or customize the number of clusters as needed.


**Acknowledgements**

**Customer Data:** The dataset used in this project was provided by [@amdari.io].











