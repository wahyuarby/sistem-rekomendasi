import pickle

with open('laptop_recommender.pkl', 'rb') as f:
    recommender = pickle.load(f)

print(recommender) # Untuk melihat isi model
