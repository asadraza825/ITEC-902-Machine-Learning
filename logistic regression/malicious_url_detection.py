# import warnings filter
from warnings import simplefilter
# ignore all future warnings
simplefilter(action='ignore', category=FutureWarning)
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

def preprocessing(url_list):
    all_features = []
    for url in url_list:
        url = url.lower()
        features = url.split("/")
        for features1 in features:
            features2 = features1.split("-")
            for features3 in features2:
                features_lst = []
                features4 = features3.split(".")
                features_lst = features_lst+ features4
        all_features = all_features+features_lst
    all_features = list(set(all_features))
    if "com" in all_features:
        all_features.remove("com")
    return all_features

data_file = open("data_malicious_url.csv","r")
url_list = ["testing"]
class_label_list = []
data_row = []
try:
    for row in data_file:
        url = str(row.split(",")[0])
        url_list.append(url)
        class_label = str(row.split(",")[1])
        class_label_list.append(class_label)
        data_row.append([url,class_label])
except:
    print()
class_label_list.append("good")
vectorizer = TfidfVectorizer(tokenizer=preprocessing)  # term-frequency and inverse-document-frequency
x = vectorizer.fit_transform(url_list)
x_train, x_test, y_train, y_test = train_test_split(x, class_label_list, test_size=0.2, random_state=42) # to split data into training and testing sets.
logit = LogisticRegression()
logit.fit(x_train,y_train)
score = logit.score(x_test,y_test)
print("Score: {}".format(100*score))
x_predict = ['www.evilass.com','google.com/search=VAD3R','yahoo.com']
x_predict = vectorizer.transform(x_predict)
y_predict = logit.predict(x_predict)
print (y_predict)