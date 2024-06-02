import pandas as pd
from sklearn.model_selection import train_test_split
from main import analyze_email
from decouple import config
from groq import Groq

pd.set_option("future.no_silent_downcasting", True)

data = pd.read_excel('spam.xlsx')
emails = data.drop('Category',axis=1)
#emails = data['Message']
#print(emails.head())

# hna maghadich n7taj train wela test, objectif how ntester model li deja 3ndi
# train w dkchi d RAG ankhlih later, had dataset kamla antester biha

"""
Encodage: ham : 0,
        spam : 1
"""

Category_encoding = {
    'ham':0,
    'spam':1
}
data['Category'] = data['Category'].replace(Category_encoding)
true_labels= data['Category']

def test_analyze_email(client,test_emails,true_labels):
    predicted_scores = []
    explanations = []

    for email in test_emails:
        result = analyze_email(client,email,additional_context=None)
        print(type(email))
        print()
        print(f"Result: {result}")
        try:
            score_line = next(line for line in result.split('\n') if 'Phishing Risk Score' in line)
        # score line will be smth like this: Phishing Risk Score : 75
       # score = score_line.split(': ')
        # score line atwli list bhal haka ['Phishing Risk Score','75']
        #score = int(score[1].strip())
            score = int(score_line.split(': ')[1].strip())
        except (ValueError, StopIteration) as e:
            print(f"Error: {e}")
        predicted_scores.append(score)
        explanations.append(result)

    return predicted_scores, explanations

"""
reminder about phishing risk score:
0 indicates a completely safe email and 100 indicates a definite phishing attempt
"""

def binary_classification_forScores(scores,threshold=50):
    """
    had function atb9a tchuf scores li khdinahom mn function test_analyze_email,
    w nrdohom ima 0 wla 1 values, bach n9dro ncomparew m3a real values
    """
    binary_labels = []
    for score in scores:
        if score >= threshold:
            binary_labels.append(1)             #1 phishing
        else:
            binary_labels.append(0) #safe
    return binary_labels

client = Groq(api_key=config("GROQ_API_KEY"))
predicted_scores, explanations=test_analyze_email(client,emails,true_labels)
predicted_labels = binary_classification_forScores(predicted_scores)
print(predicted_labels)
