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
1. **Optimal Clusters Analysis:** To ascertain the optimal number of clusters (k) for segmenting customers, two renowned methods were used - Elbow Method and  Silhouette Method and both method suggest that optimal k = 4.

<img width="561" alt="image" src="https://github.com/user-attachments/assets/59b2b544-0f0d-41e5-987f-1feec1f51375" />

2. **Models Selection:** To select the best model to use, hyperparameter tunning were performed on Four(4) models to dentify the optimal number of clusters for customer segmentation:
   
   - **KMeans** : Clusters data by minimizing the variance within each cluster using centroid-based     
                  partitioning.
   - **Agglomerative Clustering**: A hierarchical clustering method that iteratively merges the closest 
                  pairs of clusters.
   - **Hierarchical Clustering:** Builds a tree-like structure (dendrogram) to show nested clusters formed 
                  through either merging (agglomerative) or splitting (divisive).
   - **DBSCAN (Density-Based Spatial Clustering of Applications with Noise):** Groups data points based on 
                   density, identifying clusters of arbitrary shapes and noise points. 

## Model Evaluation:

To assess the clustering performance, the following evaluation metrics were used:
1. **Silhouette Score:** Measures how similar an object is to its own cluster compared to other clusters. Higher scores indicate better-defined clusters.
2. **Calinski-Harabasz Score:** Measures the ratio of the sum of between-cluster dispersion to within-cluster dispersion. Higher values indicate better-defined clusters.  
3. **Davies-Bouldin Score:** Measures the average similarity ratio of each cluster with its most similar cluster. Lower scores indicate better separation of clusters
   
  <img width="322" alt="image" src="https://github.com/user-attachments/assets/da6e52c9-3725-430a-9498-c9ad7b6f2e15" />


KMeans is the best overall model because it has the highest Calinski-Harabasz Score- meaning its clusters are compact and well-separated, has the lowest Davies-Bouldin Score-meaning its clusters are well-distinguished and its Silhouette Score (0.6061) is good, although DBSCAN is higher, but DBSCAN struggles with compactness.

 ## Visualization - KMeans Clustering
1. **Cluster Distribution**
   
<img width="632" alt="image" src="https://github.com/user-attachments/assets/eed2f068-640b-4e6d-bc1f-6d33ae1da714" />

The bar plot shows the percentage distribution of customers across the four(4) clusters, providing insights into the balance of customer segments

2. **Radar Chart**

![image](https://github.com/user-attachments/assets/cca7db30-d424-4c67-9a2f-2344aa74d48c)

The radar charts are generated for each cluster to visualize the average behavior of customers in that segment across various features.
Each cluster is represented by a different color, and the features are plotted on a circular axis to easily compare the behaviors

# Customers Clustering Analysis:

1. **Cluster 0(Low Recency, Moderate Frequency & Monetary Value): Average Customers** 

   Customers in this cluster recently made purchases and they forms the majority (68.98%), but their buying frequency and monetary contributions are average or slightly below average.

   Recommendation Strategies:

      - Loyalty Programs: Introduce rewards for consistent purchases to increase frequency.
      - Personalized Offers: Use targeted discounts to incentivize slightly increased spending.
      - Customer Engagement: Send thank-you messages or product recommendations to maintain engagement.


2. **Cluster 1(High Frequency & High Monetary Value): Top Spenders/High-Value Loyal Customers** 

   This is the most valuable customer segment(makes up only 0.09% but critical for revenue,) with high purchase frequency, high spending, and recent transactions.

   Recommendation Strategies:

      - VIP Programs: Offer exclusive benefits, early access to products, or premium support.
      - Cross-Selling and Upselling: Introduce high-end products or bundles since they are willing to spend.
      - Retention Focus: Send personalized thank-you notes and loyalty points to reinforce their value to the business.

3. **Cluster 2(High Recency, Low Frequency & Low Monetary Value)   :At-Risk (Churned) Customers**  
   Customers in this cluster are at risk of churn (represents 26.05%) as they haven’t purchased recently, and their spending is below average.

   Recommendation Strategies:

      - Win-Back Campaigns: Offer discounts or incentives to re-engage them.
      - Survey and Feedback: Understand reasons for disengagement and improve accordingly.
      - Reminder Emails: Send gentle nudges with product updates or special deals.
      - Reactivation Offers: Provide time-sensitive discounts to encourage purchase.

4. **Cluster 3(Moderate Recency, Moderate Frequency & Monetary Value): Potential Loyalists**  

      These customers(making up of 4.87%) are moderately active and have slightly higher-than-average spending, indicating potential for loyalty.

      Recommendation Strategies:

      - Retention Campaigns: Offer discounts on frequently purchased products to maintain engagement.
      - Personalization: Tailor offers based on their previous purchase patterns.
      - Build Brand Loyalty: Introduce membership perks or early access to sales.
      - Social Proof: Encourage reviews and referrals as they are moderately engaged.


**General Recommendations:**

1. **Customer Segmentation Marketing:** Use these insights to build targeted marketing strategies for each cluster.

2. **Retention Strategy:** 
      - Invest more in Cluster 1 (top spenders) to maintain loyalty.
      - Focus on Cluster 2 to win back customers before they churn.

3. **Personalized Communication:** Automate segmented email campaigns targeting each cluster with appropriate content.

4. **Product Strategy:**
      - For Cluster 3, highlight new product lines or complementary items to increase frequency.
      - For Cluster 0, showcase popular or related products to boost their spending slightly.

5. **Identify Key Drivers of High Retention:**
      Analyze the factors that led to the high retention rate observed in the Customer Retention Cohort Analysis for December 2010. Determine whether successful elements such as marketing campaigns, product enhancements, or customer engagement initiatives played a role. Replicate these effective strategies across other cohorts to boost retention.

6. **Investigate the Retention Drop in December 2011:**
      Examine why retention rates declined across all cohorts in December 2011. Potential areas of investigation include customer feedback, product quality, customer service issues, or any operational changes during that period. Identifying and addressing these root causes will help improve future retention outcomes.

7. **Set Realistic and Business-Specific Retention Targets:**
      While the typical e-commerce retention rate ranges from 20% to 40%, it's essential to establish goals tailored to your specific business context. Use historical data and industry benchmarks to set achievable targets, aiming for gradual improvements over time.

8. **Monitor and Adapt Continuously:**
      Retention dynamics can shift due to various factors, so it’s important to regularly track retention metrics and customer behavior. Continuously analyze cohort data and make data-driven adjustments to your retention strategies to maintain high customer loyalty.


Now that the company understands its customer segments and their behavior, use this information to craft targeted marketing strategies. Focus on areas with high product sales rather than just high customer acquisition, ensuring a more strategic approach to increasing sales and ROI.


# Future Work
To further enhance customer segmentation and retention strategies, several areas of improvement and exploration are proposed:

1. **Advanced Clustering Techniques:** Explore more sophisticated algorithms such as Gaussian Mixture Models (GMM) or Spectral Clustering to capture complex patterns and overlapping clusters.

2. **Deep Learning Approaches:** Incorporate Autoencoders or Neural Network-based clustering to identify non-linear relationships and improve segmentation accuracy.

3. **Personalization through Predictive Modeling:** Develop predictive models to forecast customer churn and loyalty, allowing proactive engagement and retention initiatives.

4. **Incorporation of Real-Time Data:** Integrate real-time customer interaction data to create dynamic clusters that adapt to changing customer behavior.

5. **Sentiment and Behavioral Analysis:** Use NLP techniques to analyze customer feedback and correlate it with cluster behaviors for better customer satisfaction insights.

6. **A/B Testing of Strategies:** Implement targeted marketing campaigns based on cluster characteristics and conduct A/B testing to evaluate the effectiveness of tailored strategies.

-----

## Project Setup:

* **Tech Stack**

  * Python 3.x
  * Libraries:
  * pandas
  * numpy
  * scikit-learn
  * matplotlib
  * seaborn
  * tabulate
  * scipy
     
* **How to Use**

  1. Clone the repository:

    * git clone 'the folder'

  2. Install the required dependencies:

    * pip install -r requirements.txt

  3. Run the analysis:
 
    * Open the **customer_segment.ipynb** script to run the KMeans clustering and generate visualizations.

  
**Acknowledgements**

**Customer Data:** The dataset used in this project was provided by @amdari.io
