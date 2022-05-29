import pandas as pd

def processData(data):
    if not data is None:

        #check the null values in our dataset
        data.isnull().sum()

        #check the number of counts of different sepecies in our dataset
        data['Species'].value_counts()

        data['Species'] = data['Species'].map({'Iris-setosa':0, 'Iris-versicolor':1, 'Iris-virginica':2})

        #delete id from dataset
        data.drop('Id',axis=1,inplace=True)

        #Seperate dependent and independent feature
        x = data.drop('Species',axis=1)
        y = data['Species']

        return x,y
