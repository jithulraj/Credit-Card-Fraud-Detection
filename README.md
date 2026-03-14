

### **End-to-End Credit Card Fraud Detection Model** 🛡️💳

#### **Table of Contents**

1. **Project Overview**
2. **Dataset & Domain Understanding**
3. **Key Challenges: The 0.17% Majority Class**
4. **Technical Architecture & Methodology**
5. **SQL: Big Data & Bulk Loading**
6. **Python: Machine Learning & Addressing Imbalance**
7. **Version Control & Deployment Challenges**
8. **Final Results & Application Logic**
9. **How to Run the Project Locally**
10. **Live Application**
11. **Series Context**
12. **License**

---

### **1. Project Overview**

This project focuses on building a robust, real-time predictive system to identify fraudulent credit card transactions [cite: 2026-02-27]. Adopting a **Learning by Doing** approach, the entire pipeline—from data ingestion and analysis to machine learning and cloud deployment—was constructed from scratch.

The primary goal is to move beyond simple accuracy and focus on building a **sensitive model** capable of detecting rare fraud cases (the 0.17% minority class) with high recall [cite: 2026-03-01].

### **2. Dataset & Domain Understanding**

The dataset was sourced from Kaggle and contains transactions made by European cardholders over a specific period [cite: 2026-02-28].

* **Total Transactions**: 284,807
* **Fraud Cases**: 492 
* **Class 1 (Fraud)**: 0.17% 
* **Class 0 (Legitimate)**: 99.83% 

All features in the dataset (V1–V28) are PCA-transformed (Principal Component Analysis) to ensure user privacy [cite: 2026-02-27]. This domain-specific transformation means the model relies entirely on statistical patterns and variance within these abstract features rather than personal details [cite: 2026-02-27, 2026-03-05].

### **3. Key Challenges: The 0.17% Majority Class**

The defining characteristic of this project is extreme **Class Imbalance** [cite: 2026-03-01]. The fraud cases are a vanishingly small fraction of the data [cite: 2026-03-01]. If left unaddressed, a machine learning model could achieve over 99.8% accuracy by simply predicting "Legitimate" for every transaction, while failing to detect any fraud [cite: 2026-03-01]. The challenge was to make the model prioritize the rare class [cite: 2026-03-01].

### **4. Technical Architecture & Methodology**

The project was built as a complete data pipeline using industry-standard tools and methodologies:

* **Storage**: MySQL (for data hosting and SQL exploration).
* **Analysis**: Exploratory Data Analysis (EDA) in SQL and Python .
* **Machine Learning**: Random Forest Classifier.
* **Deployment**: Streamlit Cloud (for hosting the live app).

### **5. SQL: Big Data & Bulk Loading**

Before analysis, the massive dataset needed to be moved from CSV to a database environment [cite: 2026-02-27].

* **The Blocker**: Standard table import wizards struggled and hung due to the high row count (2.84 lakh) [cite: 2026-02-27].
* **The Solution**: High-performance SQL bulk loading [cite: 2026-02-27].
* **Key Learning**: Using the **`LOAD DATA INFILE`** command reduced the loading time from hours (with the wizard) to just **2-3 seconds**.

### **6. Python: Machine Learning & Addressing Imbalance**

Python and its vast library ecosystem were used to train the final model.

* **Libraries**: `Pandas` (data handling), `Scikit-learn` (machine learning), `Imblearn` (handling imbalance), `Joblib` (model saving).
* **Handling Imbalance**: I implemented **SMOTE** (Synthetic Minority Over-sampling Technique) to artificially generate more minority (fraud) samples, allowing the model to learn hidden patterns in the fraud cases more effectively.
* **The Model**: **Random Forest Classifier**, which proved to be highly robust and accurate for this classification task.

### **7. Version Control & Deployment Challenges**

Hosting the application on the cloud presented version control and Git challenges.

* **Version Control**: Git & GitHub.
* **Deployment**: Streamlit Cloud.
* **The Blocker**: During deployment, I encountered merge conflicts between my local repository and the remote GitHub branch. This hindered the Streamlit Cloud deployment.
* **The Solution**: I used Git commands like `git pull` to sync the local and remote versions and `git push --force` to resolve mismatches, ensuring a clean deployment.

### **8. Final Results & Application Logic**

The final application is live and interactive.

* **Results**: By analyzing feature importance, I confirmed that specific extreme negative values in V10 and V14 were critical fraudulent patterns [cite: 2026-03-01].
* **Application Logic**: To enhance real-world reliability, a combined logic was implemented [cite: 2026-03-05]. The application triggers a fraud alert if the model predicts fraud **OR** if extreme V10/V14 thresholds are met [cite: 2026-03-05].

#### **Testing the Live App for Fraud**

You can test the sensitivity of the live application by entering these "Extreme" values, which the model has learned to identify as potentially fraudulent [cite: 2026-03-05]:

* **Feature V10**: `-20.0` or lower
* **Feature V14**: `-25.0` or lower
* **Feature V4**: `10.0` or higher
* **Amount**: `1500` or higher

### **9. How to Run the Project Locally**

To run this project on your local machine:

1. Clone the repository:
```bash
git clone  https://github.com/jithulraj/Credit-Card-Fraud-Detection.git

```


2. Navigate to the project directory.
3. Install the required libraries (Pandas, Numpy, Scikit-learn, Imblearn, Joblib, Streamlit).
4. Run the application using Streamlit:
```bash
streamlit run app.py

```



### **10. Live Application**

Access the deployed version of the application here:

* **Live App Link**: `https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud/data`
* **Kaggle Dataset**: `[Insert Kaggle Dataset URL]`

### **11. Series Context**

* **Series**: **Learning by Doing: Data Skills**
* **Project**: **1/50: Credit Card Fraud Detection**

This is the first of fifty professional portfolio projects where I am mastering new data skills—from SQL ingestion and imbalance handling to model deployment—entirely through practical, hands-on application [cite: 2026-03-05]. The full lifecycle approach demonstrated in this project shows a readiness for production environments.

