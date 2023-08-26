import torch
from cachetools import cached, TTLCache
from transformers import PegasusForConditionalGeneration, PegasusTokenizer
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

model_name = 'tuner007/pegasus_paraphrase'
torch_device = 'cuda' if torch.cuda.is_available() else 'cpu'
tokenizer = PegasusTokenizer.from_pretrained(model_name)
CACHE_SIZE = 99999999999999999999999  
CACHE_TIMEOUT = 7000000000000000000000000000
cache = TTLCache(maxsize=CACHE_SIZE, ttl=CACHE_TIMEOUT)
model = PegasusForConditionalGeneration.from_pretrained(model_name).to(torch_device)
model1 = SentenceTransformer('sentence-transformers/all-mpnet-base-v2')

@cached(cache)
def get_response(input_text,num_return_sequences,num_beams):
  batch = tokenizer([input_text],truncation=True,padding='longest',max_length=200, return_tensors="pt").to(torch_device)
  translated = model.generate(**batch,max_length=150,num_beams=num_beams, num_return_sequences=num_return_sequences, temperature=1.5)
  tgt_text = tokenizer.batch_decode(translated, skip_special_tokens=True)
  return tgt_text
  #return tgt_text



@cached(cache)
def similarity(source, produced):
    sentences = [source, produced]
    print(sentences)
    embeddings = model1.encode(sentences)
    similarity_matrix = cosine_similarity(embeddings)
    similarity = similarity_matrix[0, 1]
    similarity = similarity * 100
    print(similarity)
    return similarity

# models from sentence transformers
