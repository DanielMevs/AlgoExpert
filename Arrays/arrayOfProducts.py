
#O(n^2) time implementation
def productArray(array):
    products = []
    runningProduct = 1
    for i in range(0,len(array)):
        j = i+1;
        while j < len(array) + i:
            runningProduct *= array[j%len(array)]
            j+=1
        products.append(runningProduct)
        runningProduct = 1
    return products


#print(productArray([3,2,1,4]))    


#O(n) time implementation where n = size of input array
def productArrayEfficient(array):
    products = [1]*len(array)
    runningProduct = 1
    for i in range(0,len(array)):
        products[i] = runningProduct
        runningProduct *= array[i]
    runningProduct = 1
    for i in reversed(range(len(array))):
        products[i] *= runningProduct
        runningProduct *= array[i]
        
    return products


print(productArrayEfficient([3,2,1,4]))    