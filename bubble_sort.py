array = [1,8,9,7,-5]

def bubble_sort(a):
    array = a 
    for i in range(len(array)-1):
        for j in range(len(array)-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]

    print(array)

def insertion_sort(array):
    for i in range(1, len(array)):
        location = i
        current = array[i]
        while location > 0 and array[location-1] > current:
            array[location] = array[location-1]
            location-=1
        array[location]=current

    print(array)

def selection_sort(array):
    for i in range(len(array)):
        min = i
        for j in range(i+1,len(array)):
            if array[j] >  array[min]:
                min = j
            array[min], array[j] = array[j], array[min]
    print(array)

selection_sort(array)











