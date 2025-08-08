# Word2Vec - CBOW vs Skip-Gram
***Mindset: "From one-hot -> to dense, meaningful word vectors"***

**Why We Need Word2Vec (The Problem)**

Before Word2Vec:
We used one-hot vectors: very sparse and meaningless

"cat" = [0, 0, 1, 0, 0, 0, …]

No notion of similarity: "cat", "dog", and "tiger" had nothing in common numerically

## Goal of Word2Vec: 

Learn dense vector representations of words where:
- Similar words have similar vectors
- Word meanings are captured by contexts in which they appear

Core Idea of Word2Vec
| Model         | Goal                                       | Analogy                        |
| ------------- | ------------------------------------------ | ------------------------------ |
| **CBOW**      | Predict target word from surrounding words | "Fill in the blank"            |
| **Skip-Gram** | Predict context words from target word     | "What words come around this?" |


## When to use what?
| Scenario                          | Choose        |
| --------------------------------- | ------------- |
| You have lots of text             | **CBOW**      |
| You care about rare/unusual words | **Skip-Gram** |
_____________________________________________________________________________________________________________________________________________________

# CBOW (Continuous Bag of Words) – Core Intuition
Analogy First: “Guess the Word in a Sentence”
Imagine this sentence: "I ___ eating spicy noodles", You're trying to guess the missing word. Your brain looks at the surrounding words: I, eating, spicy, noodles

Then it predicts the missing one: maybe "love", "like", or "enjoy"? That’s CBOW: Use the context (surrounding words) to predict the center word.

CBOW in Word2Vec:
- You take a window of words around a center word.
- Input = context words
- Output = center word

## What Does the CBOW Model Learn?
It trains a small neural net that maps one-hot input vectors to a dense representation (word embeddings).

- These embeddings are stored in the hidden layer weights.

- Once trained, you can use them to find:

- Word similarities ->  Analogies and Clusters of related words

_____________________________________________________________________________________________________________________________________________________

# Skip-Gram – Core Intuition
**Analogy First: “Teach the Context from One Word”**

Imagine you're playing a new word game: You're given one word — say “eating” — and asked to guess all the surrounding words in the sentence.

Sentence: "I love eating spicy food"

From “eating”, you'd guess:
"love"
"spicy"
Maybe "I"
Maybe "food"

That’s Skip-Gram: Use the center word to predict surrounding context words.

## Skip-Gram in Word2Vec:
- Input: Center word
- Output: Context words
- Trains a model to predict nearby words for a given word.


