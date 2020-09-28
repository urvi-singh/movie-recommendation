import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
def get_title_from_index(index):
	return df[df.index==index]
	["name"].values[0]
def get_index_from_name(name):
	return df[df.name==name]
	["index"].values[0]
df=pd.read_csv("movies.csv")
print (df.head())
features=['rating', 'writer', 'director', 'genre']
for feature in features:
	df[feature] = df[feature].fillna(' ')
def combine_feats(row):
	return (row['rating'] + " " + row['writer'] + " " +  
	row['director'] + " " + row['genre'])
df["comb_feat"] = df.apply(combine_feats, axis=1)
print (df["comb_feat"].head())
cv=CountVectorizer( )
count_matrix = cv.fit_transform(df["comb_feat"])
cosine_sim = cosine_similarity(count_matrix)
movie_user_likes = "Crocodile"
movie_index = get_index_from_name(movie_user_likes)
similar_movies = list(enumerate(cosine_sim[movie_index]))
sorted_similar_movies = sorted(similar_movies, key=lambda x:x[1], reverse= True)
i=0
for movie in sorted_similar_movies:
	print (get_title_from_index(movie[0]))
	i=i+1
    if i>50:
        break