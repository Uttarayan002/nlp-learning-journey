
# Introduction: “How Machines Read Text”
Text is unstructured data. For a machine to work with it (whether for classification, recommendation, or summarization), it must convert text into numbers — vectors that models can understand.

This process begins with:
**Tokenization** -> **Stopword Removal** -> **Lemmatization**
Think of it as:
Splitting words -> Removing noise -> Reducing words to their base form

##  Step 1: Tokenization
What is it?
Tokenization is the process of breaking down a sentence into individual units, usually words or subwords called tokens.
Why it's important?
Every NLP pipeline starts here. Without tokenizing, you can't clean, analyze, or model the text.

## Step 2: Stopwords Removal
What are Stopwords?

Stopwords are common words like “the”, “is”, “and” that don’t carry useful meaning for modeling.
Not always removed — depends on task. In text generation or summarization, stopwords may be needed.

## Step 3: Lemmatization
What is Lemmatization?

It’s the process of reducing words to their base form (lemma) using linguistic knowledge.




