import numpy as np
from collections import Counter





def predict(dists, labels, k=1):
    
    # student code goes here
    finalHolder =  []
    for r in dists:
        doubleHolder = [];
        counter = 0;
        print("R")
        print(r)
        for x in r:
            doubleHolder.append([x,labels[counter]])
            counter = counter + 1;
        print("Original")
        print(doubleHolder)
        doubleHolder.sort(key=lambda pair: pair[0])
   
    
        print("DoubleHolder(sorted)")
        print(doubleHolder)
        closestClass = []
    
        for i in range(0,k):
            closestClass.append(doubleHolder[i][1]);
        print("Just Class(ClosestClass)")
        print(closestClass)
            
        data = Counter(closestClass)
        mode = data.most_common(1   )
        print("mode")
        print(mode)
        
        
        modeperClass = [x for x in data.most_common()];
        counter = 0; 
        print("Mode for each number")
        print(modeperClass);
        counter = 0;
        check = False;
        counterArray = 0;
        
        if k == 2:
            finalHolder.append(np.amin(closestClass))
            continue;
                   
        
        for i in modeperClass:
            print(mode[0][0], " ",i[0])
            if mode[0][1] == i[1] and mode[0][0] != i[0]:
                print("CIRCUIT BREAK")
                print([np.amin(closestClass)])
                finalHolder.append(np.amin(closestClass))
                check = True;
                break;
            counterArray = counterArray+ 1;
                    #return np.asarray([np.amin(labels)])
        if check == True:
            continue;
        print("NORMAL FLOW")
        print(mode[0][0])
        finalHolder.append(mode[0][0])
        print()
        #return np.asarray([mode[0][0]])
    print(finalHolder)
    return np.asarray(finalHolder);

#Sort the labels aswell
#return the smallest label
    

dists = np.array([[0.1, 0.1]])  # shape-(1, 7)
labels = np.array([2, 0])    # shape-(7,)

#answer is [8, 6, 8]

print(predict(dists,labels,k=2));

"""
def predict(dists, labels, k=1):
    
    # student code goes here
    finalHolder =  []
    for r in dists:
        doubleHolder = [];
        counter = 0;
        print("R")
        print(r)
        for x in r:
            doubleHolder.append([x,labels[counter]])
            counter = counter + 1;
        print("Original")
        print(doubleHolder)
        doubleHolder.sort(key=lambda pair: pair[0])
   
    
        print("DoubleHolder(sorted)")
        print(doubleHolder)
        closestClass = []
    
        for i in range(0,k):
            closestClass.append(doubleHolder[i][1]);
        print("Just Class(ClosestClass)")
        print(closestClass)
            
        data = Counter(closestClass)
        mode = data.most_common(1)
        print("mode")
        print(mode)
        
        
        modeperClass = [x[1] for x in data.most_common()];
        counter = 0; 
        print("Mode for each number")
        print(modeperClass);
        counter = 0;
        check = False;
        counterArray = 0;
        
        if k == 2:
            if modeperClass[0] == modeperClass[1]:
                finalHolder.append(np.amin(closestClass))
            else:
                   finalHolder.append(mode[0][0])
            continue;
                   
        
        for i in modeperClass:
            print(mode[0][0], " ", closestClass[counterArray])
            if mode[0][1] == i and mode[0][0] != closestClass[counterArray]:
                print("increment")
                counter = counter + 1;
            if counter == 2:
                    print("CIRCUIT BREAK")
                    print([np.amin(closestClass)])
                    finalHolder.append(np.amin(closestClass))
                    check = True;
                    break;
            counterArray = counterArray+ 1;
                    #return np.asarray([np.amin(labels)])
        if check == True:
            continue;
        print("NORMAL FLOW")
        print(mode[0][0])
        finalHolder.append(mode[0][0])
        print()
        #return np.asarray([mode[0][0]])
    print(finalHolder)
    return np.asarray(finalHolder);
    """