doubleArray = [3, 6, 9, 12]
doubleArray2 = [27, 30, 33, 36]
#the list are all mulltiple of threes
def double(sequence):
    sum = 0
    for number in sequence:
        sum += number*2
#the sum will add to the arguement that is being multiplied by 2
    return sum
double([15, 18, 21, 24])
double(doubleArray)
x = double(doubleArray2)
print(x)
#This will get me a result of 72
