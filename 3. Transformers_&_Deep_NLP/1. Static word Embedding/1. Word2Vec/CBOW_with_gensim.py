import gensim
from gensim.models import Word2Vec
from nltk.tokenize import word_tokenize
import nltk
# nltk.download('punkt')
# nltk.download('punkt_tab')

corpus = [
    "I love eating spicy food",
    "This restaurant has amazing noodles",
    "Food tastes great here",
    "I enjoy eating with friends",
    "The service was excellent"
]

# Tokenize each sentence
tokenized_corpus = [word_tokenize(sentence.lower()) for sentence in corpus]
print(tokenized_corpus)

# CBOW model using gensim (sg=0 means CBOW)
cbow_model = Word2Vec(
    sentences=tokenized_corpus,
    vector_size=100,        # Embedding size
    window=2,           # Context window size
    min_count=1,        # Ignore words with frequency < 1
    sg=0)                # CBOW (sg=1 would be Skip-Gram)


# Check vector of a word
print("Vector for 'eating':\n", cbow_model.wv['eating'])

# Find similar words
print("\nWords similar to 'eating':")
print(cbow_model.wv.most_similar('eating'))

# Word similarity
similarity = cbow_model.wv.similarity('eating', 'food')
print(f"\nSimilarity between 'eating' and 'food': {similarity:.4f}")
