# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
movie_titles=pd.read_csv("C:\\Users\\Asus\\Downloads\\movies.csv")
print(movie_titles.head())
movie_ratings=pd.read_csv("C:\\Users\\Asus\\Downloads\\ratings.csv")
print(movie_ratings.head())
print(movie_ratings.shape)
#deleting unwanted columns
movie_ratings.drop(['timestamp'],inplace=True,axis=1)
print(movie_ratings.head())
movie_titles.drop(['genres'],inplace=True,axis=1)
print(movie_titles.head())
#merging on 'movieId' column to operate on a single dataframe
merged_movie_df=pd.merge(movie_ratings,movie_titles,on='movieId')
print(merged_movie_df.head())
#finding the mean ratings and count per movie
print(merged_movie_df.groupby('title')['rating'].mean().head())
print(merged_movie_df.groupby('title')['rating'].mean().sort_values(ascending=False).head())
print(merged_movie_df.groupby('title')['rating'].count().sort_values(ascending=False).head())
#highest rating and count df
rating_mean=pd.DataFrame(columns=['Rating Mean','Rating Count'])
#assigning values to each column
rating_mean['Rating Mean']=merged_movie_df.groupby('title')['rating'].mean()
rating_mean['Rating Count']=merged_movie_df.groupby('title')['rating'].count()
print(rating_mean.sort_values("Rating Mean",ascending=False).head())

#graphing
plt.figure(figsize=(10,8))
sns.set_style("darkgrid")
rating_mean['Rating Mean'].hist(bins=30,color='purple')
plt.figure(figsize=(10,8))
sns.set_style("darkgrid")
rating_mean['Rating Count'].hist(bins=33,color='green')
plt.figure(figsize=(10,8))
sns.set_style("darkgrid")
sns.regplot(x="Rating Mean",y="Rating Count",data=rating_mean,color='brown')

#ITEM BASED
#creating matrix where correlations are to be stored
user_rating_matrix=merged_movie_df.pivot_table(index='userId',columns='title',values='rating')
print(user_rating_matrix)
print(user_rating_matrix.shape)
#single movie
movie_titles=pd.read_csv("C:\\Users\\Asus\\Downloads\\movies.csv")
movie_titles.drop(['movieId'],inplace=True,axis=1)
print(movie_titles.head())
#giving user option to choose movie
movie_name=input("Enter Movie Name: ")
movie_rate=user_rating_matrix[movie_name]
#finding coefficient of correlation to print the most appropriate recommendations
movie_corr=pd.DataFrame(user_rating_matrix.corrwith(movie_rate),columns=["corr"])
movie_corr=movie_corr.join(rating_mean["Rating Count"])
#droping NaN values
print(movie_corr.dropna(inplace=True))
print(movie_corr.head())
#Printing Movies where rate count is greater than 50
corr_50=movie_corr[movie_corr["Rating Count"]>50]
print(corr_50.sort_values("corr",ascending=False).head())

#multiple movies
#creating matrix 
all_corr=user_rating_matrix.corr(method='pearson',min_periods=50)
print(all_corr.head())
movie_data=[['Forrest Gump (1994)',4.0],['Fight Club (1999)',3.5],['Interstellar (2014)',
4.0]]
test_movies= pd.DataFrame(movie_data, columns=['Movie Name','Movie Rating'])
print(test_movies.head())
recommended_movies= pd.Series()
for i in range(0,2):
    movie= all_corr[test_movies['Movie Name'][i]].dropna()
#iteration
movie= movie.map(lambda movie_corr: movie_corr*test_movies["Movie Rating"][i])
#append recommended movies
recommended_movies= recommended_movies.append(movie)
#print final result
recommended_movies.sort_values(inplace=True,ascending=False)
print(recommended_movies.head(10))