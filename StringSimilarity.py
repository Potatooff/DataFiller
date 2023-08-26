from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
from cachetools import cached, TTLCache


model = SentenceTransformer('sentence-transformers/all-mpnet-base-v2')
CACHE_SIZE = 99999999999999999999999  
CACHE_TIMEOUT = 7000000000000000000000000000
cache = TTLCache(maxsize=CACHE_SIZE, ttl=CACHE_TIMEOUT)

@cached(cache)
def similarity(source, produced):
    sentences = [source, produced]
    print(sentences)
    embeddings = model.encode(sentences)
    similarity_matrix = cosine_similarity(embeddings)
    similarity = similarity_matrix[0, 1]
    similarity = similarity * 100
    print(similarity)
    return similarity

# model from sentence transformers
