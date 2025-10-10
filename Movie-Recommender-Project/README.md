### Movie Recommendation System
#### 1. Project Objective
To build a content-based recommendation engine that suggests movies to users based on similarity to a movie they have already watched. This project demonstrates a foundational understanding of recommendation systems and text feature extraction.

#### 2. Methodology
* **Feature Extraction:** Key textual features like overview, genre, keywords, cast, and crew were selected and combined into a single "tags" column for each movie.

* **Text Vectorization:** Scikit-learn's CountVectorizer was used to convert these textual tags into a high-dimensional vector space, representing the content of each movie mathematically.

* **Similarity Calculation:** Cosine Similarity was computed between all pairs of movie vectors. This metric measures the similarity of content, regardless of the magnitude of the vectors.

* **Recommendation Function:** A function was built that takes a movie title as input, finds its corresponding vector, and returns the top 5 most similar movies based on the pre-computed cosine similarity scores.

#### 3. Impact
This project successfully implements a core feature found in modern content platforms. It showcases the ability to apply NLP techniques to build a system that can enhance user engagement by providing personalized content recommendations.
