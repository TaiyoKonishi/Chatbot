import json
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def load_faq_data(file_path='faq_data.json'):
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    questions = [item['question'] for item in data]
    answers = [item['answer'] for item in data]
    return questions, answers

def data_into_DataFrame(questions, answers):
    data = pd.DataFrame({
        "Question": questions,
        "Answer": answers
    })
    return data

def compute_tfidf(texts):
    tfidf = TfidfVectorizer()
    return tfidf.fit_transform(texts)

def get_most_similar_question(user_input, questions):
    # Combine FAQ + user input
    all_texts = questions + [user_input]
    
    # Compute tf-idf matrix
    tfidf_matrix = compute_tfidf(all_texts)
    
    # Compute cosine similarity: last row (user_input) vs all
    similarity = cosine_similarity(tfidf_matrix[-1], tfidf_matrix[:-1])
    
    # Get index of highest similarity
    best_match_index = similarity.argmax()
    return best_match_index

def respond_to_input(user_input, questions, answers, threshold=0.3):
    # Combine FAQ questions with user input
    all_texts = questions + [user_input]
    all_texts = [text for text in all_texts if text is not None]
    
    # TF-IDF vectorization
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(all_texts)
    
    # Compute cosine similarity: user input vs all questions
    similarity = cosine_similarity(tfidf_matrix[-1], tfidf_matrix[:-1])
    
    # Get best match
    best_index = similarity.argmax()
    best_score = similarity[0, best_index]
    
    # Check threshold
    if best_score < threshold:
        return "I'm sorry, I don't understand your question."
    
    return answers[best_index]

#questions, answers, data = load_faq_data()
#print(data)
#print(type(data))