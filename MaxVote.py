def getMaxVoting(results):

    #list to store the extracted output results
    newresults = []

    #loop through the prediction result list
    for result in results:
        #call getOutPut function to get the name of prediction of each result
        #and store them in the list
        newresults.append(getOutput(result))

    #get the count of each prediction
    c1 = newresults.count('Setosa')
    c2 = newresults.count('Versicolor')
    c3 = newresults.count('Verginica')

    #store the number of each varient
    dataMap = {'Setosa': c1, 'Versicolor': c2, 'Verginica': c3}

    #find the most predicted varient
    maxVote = max(dataMap, key=dataMap.get)

    print(dataMap)

    #consider the max voted varient as most accurate answer and returen it
    return maxVote


def getOutput(result):
    output = ''

    #assign the name according to the result number
    if result == 0:
        output = 'Setosa'

    elif result == 1:
        output = 'Versicolor'

    else:
        output = 'Verginica'
    return output
