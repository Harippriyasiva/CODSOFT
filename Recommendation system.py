import numpy as np

# Each row corresponds to a user's ratings for different movies
user_movie_ratings = np.array([
    [5, 4, 0, 0, 1],
    [0, 5, 4, 0, 2],
    [1, 0, 0, 5, 0],
    [4, 0, 5, 0, 0],
    [0, 2, 0, 4, 5]
])

def calculate_similarity(user1, user2):
    common_ratings = np.logical_and(user1 != 0, user2 != 0)
    if np.sum(common_ratings) == 0:
        return 0
    mean_user1 = np.mean(user1[common_ratings])
    mean_user2 = np.mean(user2[common_ratings])
    num = np.sum((user1[common_ratings] - mean_user1) * (user2[common_ratings] - mean_user2))
    denom1 = np.sum((user1[common_ratings] - mean_user1)**2)
    denom2 = np.sum((user2[common_ratings] - mean_user2)**2)
    similarity = num / np.sqrt(denom1 * denom2)
    return similarity

def get_top_movie_recommendations(user_id, user_movie_ratings, N):
    user_ratings = user_movie_ratings[user_id]
    similarities = [calculate_similarity(user_ratings, other_user) for other_user in user_movie_ratings]
    sorted_users = np.argsort(similarities)[::-1][1:]  # Sort in descending order and remove the user itself
    recommendations = []
    for other_user_id in sorted_users:
        unrated_movies = np.where(user_movie_ratings[other_user_id] == 0)[0]
        recommendations.extend(unrated_movies)
        if len(recommendations) >= N:
            break
    return recommendations[:N]

# Get top 3 movie recommendations for user 0
user_id = 0
top_recommendations = get_top_movie_recommendations(user_id, user_movie_ratings, N=3)

print(f"Top 3 movie recommendations for user {user_id}: {top_recommendations}")
