import pandas as pd

df = pd.read_csv("C:/Users/Hp Laptop/Desktop/New Staff/Project Quiz/.spyproject/movie_dataset.csv")


#print(df.head())

df_cleaned = df.dropna()
df_cleaned.columns = df_cleaned.columns.str.replace(' ', '_')

summary_stats = df_cleaned.describe()
print(summary_stats)

highest_rated_movie = df[df['Rating'] == df['Rating'].max()]
print(highest_rated_movie[['Title', 'Rating']])

print(df.columns)

avg_revenue = df["Rating"].mean()
print("Average Revenue:", avg_revenue)

df['Year'] = pd.to_datetime(df['Year'], errors='coerce')



# Converting the 'Year' column to datetime type
df['Year'] = pd.to_datetime(df['Year'], errors='coerce')

# Filtering movies released in the year 2016
movies_2016 = df[df['Year'].dt.year == 2016]

# Printing the number of movies released in 2016
print("Number of movies released in 2016:", len(movies_2016))


# Filtering movies directed by Christopher Nolan
nolan_movies = df[df['Director'] == 'Christopher Nolan']

# Printing the number of movies directed by Christopher Nolan
print("Number of movies directed by Christopher Nolan:", len(nolan_movies))



# Filtering movies with a rating of at least 8.0
high_rated_movies = df[df['Rating'] >= 8.0]

# Printing the number of movies with a rating of at least 8.0
print("Number of movies with a rating of at least 8.0:", len(high_rated_movies))


# Filtering movies directed by Christopher Nolan
nolan_movies = df[df['Director'] == 'Christopher Nolan']

# Calculating the median rating of Nolan's movies
median_rating_nolan = nolan_movies['Rating'].median()

# Printing the result
print("Median rating of movies directed by Christopher Nolan:", median_rating_nolan)



# Converting the 'Year' column to datetime type
df['Year'] = pd.to_datetime(df['Year'], errors='coerce')

# Calculating the average rating for each year
average_rating_by_year = df.groupby(df['Year'].dt.year)['Rating'].mean()

year_highest_rating = average_rating_by_year.idxmax()

# Printing the result
print("Year with the highest average rating:", year_highest_rating)


######################################################################


numeric_columns = df.select_dtypes(include=['number'])

# Displaying the correlation matrix
correlation_matrix = numeric_columns.corr()
print("Correlation Matrix:")
print(correlation_matrix)


correlation_matrix.to_csv("correlation_matrix.csv", index=False)


