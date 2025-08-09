# GloVe

**GloVe** = **G**lobal **Ve**ctors for Word Representation (Stanford, 2014).
It’s another way to create **static word embeddings**, but instead of training a prediction task like Word2Vec, it uses **matrix factorization** on **word co-occurrence statistics** from a large corpus.

## The Core Idea

**Co-occurrence** means:
How often two words appear together in a certain context window in a text corpus.
A **co-occurrence matrix** is a big table:
* **Rows** = target words
* **Columns** = context words
* **Values** = number of times the context word appears near the target word

### For instance, 
Corpus: "I like deep learning. I like NLP."
Window size = 1 (look 1 word before and after)

| Target\Context | I | like | deep | learning | NLP |
| -------------- | - | ---- | ---- | -------- | --- |
| I              | 0 | 2    | 0    | 0        | 0   |
| like           | 2 | 0    | 1    | 0        | 1   |
| deep           | 0 | 1    | 0    | 1        | 0   |
| learning       | 0 | 0    | 1    | 0        | 0   |
| NLP            | 0 | 1    | 0    | 0        | 0   |

which tells us:
* "I" appears next to "like" **2 times**.
* "like" appears next to "deep" **1 time**, and next to "NLP" **1 time**.


##  How GloVe Uses It

1. Build the **global co-occurrence matrix** from the corpus.
2. Convert raw counts into **probabilities** (so frequent words don’t dominate).
3. Factorize the matrix into **two smaller matrices** → these become your **word embeddings**.

**Analogy:**

* **Word2Vec** = learning meaning from conversations **one snippet at a time**
* **GloVe** = learning meaning from analyzing the **entire library's statistics**

If you want, I can **draw a diagram** showing how a co-occurrence matrix turns into GloVe embeddings — it makes the process much easier to see.

