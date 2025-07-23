
# Topic 4: Text Cleaning Pipeline
“Before you model text, you must clean it. Garbage in, garbage out.”

Goal of the Text Cleaning Pipeline:
- Remove irrelevant parts (noise)

- Normalize structure (lowercase, remove punctuations, etc.)

 - Prepare for vectorization (BoW, TF-IDF, embeddings)

- Modularize code for reuse

| Step | Action                             | Purpose                           |
| ---- | ---------------------------------- | --------------------------------- |
| 1️  | Lowercasing                        | Standardize words ("The" = "the") |
| 2️  | Remove punctuation                 | Remove noise                      |
| 3️  | Remove digits                      | If numbers are not important      |
| 4️  | Remove stopwords                   | Remove common words               |
| 5️  | Lemmatization                      | Reduce words to base form         |
| 6️  | (Optional) POS/NER-based filtering | Keep nouns, remove pronouns etc.  |
