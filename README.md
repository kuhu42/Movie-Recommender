# Movie-Recommender
Project to recommend movies based on a sample movie and rating dataset.
It uses the concept of ‘Collaborative Filtering’ which essentially implies using algorithms to filter data from user reviews to make personalized recommendations for users with similar preferences.
The developed code can:
a) Recommend a movie based on the preferences of other similar users, even plotting graphs for a more organised representation of data.
b) Recommend by analysing the parameters of a single or multiple movies the target user likes and suggesting movies with similar parameters.

Procedure
I) User-User Based Filtering
(parameters analysed using: ratings, count)
The code begins with inputting, by reading, both the .csv files. Modifying both these files by dropping columns which aren’t useful to us and merge both these files on their common and unique column ‘movieId’ gives a third, new dataframe.
Then extracting the mean ratings and count of votes for each movie, the two primary parameters, one can display the top 5 results to the user for easy choosing.
I also plotted three graphs depicting the mean rating, mean count and mean rating vs mean count in three graphs respectively.

II) Content-User Based Filtering (parameter analysed on: rating)
Beginning by creating a matrix of all the movie titles corresponding to the ratings given by each user, the code asks the user for their input on the movie similar to which they want recommendations. After this I find the coefficient of correlation of each movie to the input movie and display the most suitable results accordingly.
Next in this I take the input to be a set (dataframe) of movies and their ratings subsequently finding the movies which are most suitable.
