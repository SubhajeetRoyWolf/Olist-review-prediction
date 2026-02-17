# Olist Review Score Prediction 🚀

## 📖 Project Overview

This project predicts whether a customer review will be a **low review score (≤2)** based on order-related features.

The goal is to help e-commerce businesses identify potentially dissatisfied customers early and take preventive actions.

---

## 🎯 Business Problem

Customer satisfaction directly impacts retention and revenue.  
By predicting low review scores, businesses can:

- Detect risky deliveries
- Improve logistics
- Reduce negative reviews
- Increase customer satisfaction

---

## 📊 Dataset

The dataset contains cleaned Olist e-commerce order data.

Features used for prediction:

- `price`
- `freight_value`
- `delivery_time`

Target variable:

- `low_review` (1 = Review score ≤ 2, 0 = Otherwise)

---

## 🤖 Model Used

- **Random Forest Classifier**
- 100 trees
- Max depth = 10
- Class balancing applied

### 📈 Model Performance

- ROC-AUC Score: **0.72**

A simplified model was selected to balance performance and deployment efficiency.

---

## 🛠 Tech Stack

- Python
- Pandas
- Scikit-learn
- Joblib
- Streamlit

---

## 🚀 Deployment

The model is deployed using Streamlit.

Run locally:

```bash
streamlit run app.py
