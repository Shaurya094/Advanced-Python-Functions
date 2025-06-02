a = [1, 2, 3]
b = [4, 5, 6]
add = map(lambda x, y: x + y, a, b)
print ("List 1: ", a)
print ("List 2: ", b)
print("Addition of 2 lists: ", (list(add)))

n = [1, 2, 3, 4, 5]
def sq(n):
    return n*n
sqr = list(map(sq, n))
print ("Square numbers: ", sqr)
