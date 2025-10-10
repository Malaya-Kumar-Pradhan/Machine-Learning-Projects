import streamlit as st
import pickle

movies_list=pickle.load(open("movies.pkl","rb"))
movies1_list=movies_list["original_title"].values
similarity=pickle.load(open("similarity.pkl","rb"))

def recommend(movie):
    movie_index = movies_list[movies_list["original_title"] == movie].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    recommend_movies = []
    for i in movie_list:
        recommend_movies.append(movies_list["original_title"][i[0]])
    return recommend_movies

st.title("Movie Recommender System")
selected_movie_name = st.selectbox(
    "Which movie do you like?",
    movies1_list,
    placeholder="Select a movie...",
)
if st.button("Recommend"):
    recommendation=recommend(selected_movie_name)
    for i in recommendation:
        st.write(i)





