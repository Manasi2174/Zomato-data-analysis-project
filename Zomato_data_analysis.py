# Importing the necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Creating the dataframe and reading the csv file
data_frame = pd.read_csv("Zomato-data-.csv")
print(data_frame.head())  

# Data cleaning and preparation
# convert the rate column to float by removing the denominator characaters
print("<------------------------------------------------->")
def handle_rate(value):
    value = str(value).split('/')
    value=value[0]
    return float(value)

data_frame['rate'] = data_frame['rate'].apply(handle_rate)
print(data_frame['rate'])           # we will get all float values only
print(data_frame.info())            # Gives summary of dataset
print(data_frame.isnull().sum())    # Checking for missing or null values

# Exploring the restaurant types 
# performing the visualizations on listed_in(type) column to identify the popular restaurant

print("<--------------------------------------->")
sns.countplot(x=data_frame['listed_in(type)'],palette="coolwarm")
plt.xlabel("Type of restaurant")
plt.ylabel("Count")
plt.show()
# Conclusion: The majority of the restaurants fall into the dining category.


# Counting the votes by restaurant type for each category
grouped_data = data_frame.groupby('listed_in(type)')['votes'].sum()
result = pd.DataFrame({'votes':grouped_data})
plt.plot(result,c='Purple',marker='o')
plt.xlabel('Type of restaurant')
plt.ylabel('Votes')
plt.show()
# Conclusion: Dining restaurants are preferred by a larger number of individuals.


# Identifying the most voted restaurant
# finding the restaurant with the highest number of votes

max_votes = data_frame['votes'].max()
res_with_max_votes = data_frame.loc[data_frame['votes'] == max_votes, 'name']

print("<-----Restaurant's with the maximum votes : ------->")
print(res_with_max_votes)


# Online order avalibility 
# Exploring the online_order column to see hoe many restaurant accepts online orders

sns.countplot(x=data_frame['online_order'],palette="pastel")
plt.xlabel('Online_Order')
plt.ylabel('Count of restaurant')
plt.show()
#Conclusion: This suggests that a majority of the restaurants do not accept online orders.


# Analyze the ratings
# Checking the distributions of rating from rate cloumn

plt.hist(data_frame['rate'],bins=5,color='orange')
plt.title('Rating Distribution')
plt.show()
# Conclusion: The majority of restaurants received ratings ranging from 3.5 to 4.

# Approximate cost for couples
# Analyze the approximate cost for two peoples column to find the preferred price range

couple_data = data_frame['approx_cost(for two people)']
sns.countplot(x=couple_data,palette="husl")
plt.xlabel('Approximate cost for two peoples')
plt.ylabel('Count')
plt.show()
# Conclusion: The majority of couples prefer restaurants with an approximate cost of 300 rupees.


# Ratings Comparision (online vs offline)
# Compare the ratings between the restaurant that accepts the online orders and those that don't
plt.figure(figsize=(6,6))
sns.boxplot(x='online_order', y='rate' , data=data_frame,palette="husl")
plt.show()
#Conclusion: Offline orders received lower ratings in comparison to online orders which obtained excellent ratings


# Order Mode prefrences by restaurant type
# Finding te relationship between order mode(online order) and restaurant type
pivot_table = data_frame.pivot_table(index='listed_in(type)',columns='online_order',aggfunc='size',fill_value=0)
sns.heatmap(pivot_table,annot=True,cmap='YlGnBu',fmt='d')
plt.title('Heatmap')
plt.xlabel('Online Order')
plt.ylabel('Listed In (Type)')
plt.show()
# With this we can say that dining restaurants primarily accept offline orders whereas cafes primarily receive online orders. 
# This suggests that clients prefer to place orders in person at restaurants but prefer online ordering at cafes.

