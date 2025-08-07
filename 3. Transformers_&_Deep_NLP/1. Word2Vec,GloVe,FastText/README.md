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



