from gensim.models import Word2Vec
from nltk.tokenize import word_tokenize
import nltk
nltk.download('punkt')


# Our toy corpus
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

# sg=1 means Skip-Gram
skipgram_model = Word2Vec(
    sentences=tokenized_corpus,
    vector_size=100,    # Dimension of embedding
    window=2,           # Context window size
    min_count=1,        # Minimum frequency of words to be included
    sg=1                # Skip-Gram model
)


# View vector of a word
print("Vector for 'food':\n", skipgram_model.wv['food'])

# Find similar words
print("\nWords similar to 'food':")
print(skipgram_model.wv.most_similar('food'))

# Word similarity
similarity = skipgram_model.wv.similarity('eating', 'noodles')
print(f"\nSimilarity between 'eating' and 'noodles': {similarity:.4f}")
