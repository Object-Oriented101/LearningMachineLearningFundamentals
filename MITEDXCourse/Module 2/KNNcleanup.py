import numpy as np

x = np.array([[1., -3., 8., 5.], [10., 3., 12., 0.]])
y = np.array([[1., -3., 8., 5.],[9.,  0., 5., 2.],[22., -1., -12., 0.]]);


finalArray = [];

for index in x:
    subtractionVector = index-y;
    subtractionVector = np.square(subtractionVector);
    sum = subtractionVector.sum(axis = 1);
    sum = np.sqrt(sum)
    finalArray.append(sum);







"""
for index in x:
    subtractionVector = index-y;
    print(subtractionVector);
    sumValue = [];
    
    for i in subtractionVector:
        sum = 0;
        for z in i:
            sum = sum + z ** 2;
        sum = np.sqrt(sum)
        sumValue.append(sum)
    print(sumValue)
    finalArray.append(sumValue);

"""
    
    
    
    
