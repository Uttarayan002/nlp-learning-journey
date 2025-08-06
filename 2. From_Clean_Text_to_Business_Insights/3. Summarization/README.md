# Text summarization 
In Natural Language Processing (NLP) is the process of shortening long pieces of text into shorter versions, while retaining the most important information and overall meaning of the original content. The goal is to create a concise and coherent summary that allows readers to understand the main points quickly. There are two main approaches to text summarization:

1. **Extractive Summarization**: This method involves selecting a subset of words, phrases, or sentences directly from the original text and combining them to form a summary. The system identifies key sentences based on various features such as word frequency, sentence position, and thematic significance.

2. **Abstractive Summarization**: This approach generates new sentences that capture the essence of the original text. Unlike extractive summarization, abstractive summarization can produce summaries that include paraphrased content or new expressions that are not explicitly present in the original text. This method often uses advanced NLP techniques, including deep learning models like transformers.

Text summarization is used in various applications, such as news aggregation, document processing, and creating digestible content for quick consumption. It helps in efficiently managing and understanding large volumes of textual data.
_______________________________________________________________________________________________________________________________________________________________________________________________________________________________________________

# What is Extractive Summarization?
It selects the most important sentences from the original text to form a summary — like highlighting only the best lines in a news article.

## Algorithm: TextRank (Like PageRank for Sentences)
- Each sentence is a node.
- Edges = similarity (semantic or TF-IDF)
- Run a graph algorithm to rank sentences
- Pick top n scored sentences as summary

Code: [Extractive Summarization](https://github.com/Uttarayan002/nlp-learning-journey/blob/main/2.%20From_Clean_Text_to_Business_Insights/3.%20Summarization/1_extractive_text_summarization.py)

## What is Extractive Summarization with TF-IDF?
An extractive summarizer using TF-IDF (Term Frequency-Inverse Document Frequency) is a type of summarization technique that selects and extracts important sentences from a document based on the significance of the words they contain. Here's a brief overview of how it works:

1. **Term Frequency (TF)**: This measures how frequently a term (word) appears in a document. The idea is that the more a word appears in a document, the more relevant it is to that document.

2. **Inverse Document Frequency (IDF)**: This measures how important a term is across a collection of documents (corpus). Words that appear frequently in many documents are considered less important. IDF is calculated as the logarithm of the total number of documents divided by the number of documents containing the term.

3. **TF-IDF Score**: This is the product of TF and IDF. It gives a weight to each word in a document, indicating its importance. Words with high TF-IDF scores are considered more important.

4. **Sentence Scoring**: In an extractive summarizer, sentences are scored based on the sum of the TF-IDF scores of the words they contain. Sentences with higher scores are deemed more important.

5. **Summary Generation**: The summarizer selects the top-scoring sentences and combines them to form a summary. The goal is to ensure that the summary captures the main points of the original document.

This approach is relatively simple and efficient, making it a popular choice for many text summarization tasks. However, it relies on the assumption that the most important sentences are those that contain the most important words, which may not always be the case.

