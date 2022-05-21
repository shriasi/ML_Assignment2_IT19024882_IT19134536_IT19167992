import pickle
from sklearn.tree import DecisionTreeClassifier

with open('iris_classifier.pickle','rb') as f:
    clf = pickle.load(f)

def main():
    st.title('Iris-Species-Classifier')
    sl = st.number_input('SepalLength')
    sw = st.number_input('SepalWidth')
    pl = st.number_input('PetalLength')
    pw = st.number_input('PetalWidth')


if __name__=='__main__':
    main()
