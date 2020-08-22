##ERRORO

def FindAprxmedian(array):
    print("ARRAY")
    print(array)
    A = []
    for i in range(0,len(array)+1,5):
        print("I")
        print(i)
        if(len(array)-i>=5):
            test = A[i:i+5]
        else:
            test = A[i:]
        test = test.sort()
        print("TEST")
        print(test)
        A.append(test[len(test)//2])
    A.sort()
    print(A)
    return A[(len(A)//2)]

def FindMedian(posi,array):
    pass

array = [1,2,3,4,5,6,7]
approx_median = FindAprxmedian(array)
print(approx_median)

#median = FindMedian(approx_median,array)

#print(median)