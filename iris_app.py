import pickle
import streamlit as st
from sklearn.tree import DecisionTreeClassifier
with open('iris_classifier.pickle','rb') as f:
    clf = pickle.load(f)
    
with open('iris_classifier_2.pickle','rb') as f2:
    clf2 = pickle.load(f2)    

def main():
    st.title('Iris-Species-Classifier')
    sl = st.number_input('SepalLength')
    sw = st.number_input('SepalWidth')
    pl = st.number_input('PetalLength')
    pw = st.number_input('PetalWidth')

     if st.button('Predict'):
        result = clf.predict([[sl,sw,pl,pw]])
        result2 = clf2.predict([[sl,sw,pl,pw]])

        resultList = []

        resultList.add(getOutput(result))
        resultList.add(getOutput(result2))

        c1 = resultList.count('Setosa')
        c2 = resultList.count('Versicolor')
        c3 = resultList.count('Verginica')

        dataMap = {'Setosa':c1, 'Versicolor':c2, 'Verginica':c3}

        maxVote = max(dataMap, key=dataMap.get)

        st.sucess(maxVote)




def getOutput(result):
    output = ''
    if result==0:
            output = 'Setosa'

        elif result == 1:
            output = 'Versicolor'

        else:
            output = 'Verginica'
    return output       


if __name__=='__main__':
    main()
