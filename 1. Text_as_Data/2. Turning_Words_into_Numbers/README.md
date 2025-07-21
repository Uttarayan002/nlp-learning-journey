# BoW & TF-IDF – “Turning Words into Numbers”
Why Do We Need This?
After tokenization and cleaning, we have a list of words (tokens) — but ML models don’t understand words, only numbers. So we use vectorization methods like:

- Bag of Words (BoW) – counts word appearances

- TF-IDF – balances word frequency with importance across documents

## Bag-of-Words (BoW) – Count-Based Representation
Concept:
Each unique word in your dataset becomes a feature/column. Each sentence/document is represented as a row of word counts. This forms a sparse matrix where most values are zero.

**BoW Limitation**
Doesn’t care about word order
Can give too much importance to frequent but unimportant words (e.g., “love” appears everywhere)

That’s where TF-IDF comes in!

##  TF-IDF (Term Frequency – Inverse Document Frequency)
Concept:
- TF (Term Frequency) = how often a word appears in a document
- IDF (Inverse Document Frequency) = how rare the word is across all documents


Final Score = TF × IDF
This helps downweight common words and highlight rare, informative ones. You’ll see decimal values between 0 and 1 that represent importance rather than raw counts.



