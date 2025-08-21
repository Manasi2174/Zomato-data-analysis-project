# 🍴 Zomato Data Analysis

## 📌 Overview
This project analyzes the **Zomato restaurant dataset** using Python to uncover insights about customer preferences, cuisine popularity, pricing distribution, and ratings.
The goal is to demonstrate **data cleaning, exploratory data analysis (EDA), and visualization** skills using Python libraries like Pandas, Matplotlib and Seaborn

## 🛠️ Tech Stack & Tools
- **Python**  
- **Libraries:** Pandas, NumPy, Matplotlib, Seaborn  
- **IDE/Environment:** VS Code  
- **Dataset:** Zomato Restaurants Dataset (publicly available)

## 🔍 Key Steps

1. **Data Cleaning**
   - Removed missing and duplicate values
   - Cleaned restaurant ratings using a custom function:
    def handleRate(value):
         return float(str(value).split('/')[0])
     dataframe['rate'] = dataframe['rate'].apply(handleRate)

2. **Exploratory Data Analysis (EDA)**
   - Exploring Restaurant types 
   - Ratings distribution  
   - Online Order Availability
   - Analyze Ratings
   - Approximate Cost for Couples
   - Order Mode Preferences by Restaurant Type

## 📊 Outputs

### Exploring Restaurant Types
<img width="640" height="480" alt="restaurant types" src="https://github.com/user-attachments/assets/ff2ab9f8-9fe5-4db8-8366-04fd567c2a74" />

### Ratings Distribution
<img width="640" height="480" alt="rating distribution" src="https://github.com/user-attachments/assets/7f027186-7d34-4753-886e-5f73fc6deaea" />

### Online Order Availability
<img width="640" height="480" alt="online orders" src="https://github.com/user-attachments/assets/94fc55e8-c971-4317-9e40-962d4ea496e0" />

### Analyze Ratings as per restaurant type
<img width="640" height="480" alt="votes" src="https://github.com/user-attachments/assets/b69c77cd-03aa-47d0-a6f9-6ae3b915a31c" />

### Approximate Cost for Couples
<img width="1536" height="754" alt="appx_cost" src="https://github.com/user-attachments/assets/81219856-d2a3-4f27-9776-4cd2ee8c4fd4" />

### Ratings Comparison - Online vs Offline Orders
<img width="1536" height="754" alt="order_analyze" src="https://github.com/user-attachments/assets/70ce38b6-7d24-4c2d-94e7-7fd3543cd4e0" />

### Order Mode Preferences by Restaurant Type
<img width="1536" height="754" alt="order_mode_pref" src="https://github.com/user-attachments/assets/85a45e2e-21fa-414b-b374-80153bbab6f0" />





