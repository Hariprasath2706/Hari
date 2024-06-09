array=[]
def store_and_display():
    n=int(input("Enter the number of element:"))
    print("Enter the element:")
    for _ in range(n):
        array.append(input())
    print("Elements in the array:")
    for element in array:
        print(element)

