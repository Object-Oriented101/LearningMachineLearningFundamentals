import numpy as np
from collections import Counter


dists = np.array([[1., 0.1, 3., 2., 10., 1.5, 12.]])  # shape-(1, 7)
labels = np.array([2,    0,  2,  2,  3,    8,  5])    # shape-(7,)



def predict(dists, labels, k=1):

    # student code goes here
    doubleHolder = [];

    #First sort from lowest to highest value
    for x in range(dists.size):
        doubleHolder.append([dists[0][x],labels[x]])
        doubleHolder.sort(key=lambda pair: pair[0])    
    
    closestClass = []
    
    for i in range(0,k):
        closestClass.append(doubleHolder[i][1]);
    print(closestClass)
     
    data = Counter(closestClass)
    mode = data.most_common(1)
    mode = [list(row) for row in mode]
    print(mode)
    modeperClass = [x[1] for x in data.most_common()];
    counter = 0;
    for i in modeperClass:
        if(i == mode and counter != 2):
            counter = counter + 1;
        elif(counter == 2):
            return np.asarray([doubleHolder[0][1]])
    print([mode[0][0]])
    return np.asarray([mode[0][0]])


#Sort the labels aswell
#return the smallest label
    
dists = np.array([[0.1,0.1]]);
labels = np.array([2,0]);
print(predict(dists,labels,k=2));