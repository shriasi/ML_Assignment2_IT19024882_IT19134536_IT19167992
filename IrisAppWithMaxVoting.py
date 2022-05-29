import pickle
import streamlit as st
from sklearn.tree import DecisionTreeClassifier
from MaxVote import getMaxVoting

with open('iris_classifier.pickle', 'rb') as f:
    clf = pickle.load(f)

with open('iris_classifier_2.pickle', 'rb') as f2:
    clf2 = pickle.load(f2)

with open('iris_classifier_3.pickle', 'rb') as f3:
    clf3 = pickle.load(f3)


def main():
    st.title('Iris-Species-Classifier')
    sl = st.number_input('SepalLength')
    sw = st.number_input('SepalWidth')
    pl = st.number_input('PetalLength')
    pw = st.number_input('PetalWidth')

    if st.button('Predict'):
        result = clf.predict([[sl, sw, pl, pw]])
        result2 = clf2.predict([[sl, sw, pl, pw]])
        result3 = clf3.predict([[sl, sw, pl, pw]])

        output = getMaxVoting([result, result2, result3])

        st.success(output)


if __name__ == '__main__':
    main()