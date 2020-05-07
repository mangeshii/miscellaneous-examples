def binarySearch(elements,search):


    first=0
    last=len(elements)-1

    while first <= last:
        mid = (first + last) // 2
        
        if elements[mid] == search:
            return mid

        else:
            if search < elements[mid]:
                last = mid-1
            elif search > elements[mid]:
                first = mid +1
    return -1

  
result=binarySearch([1, 3, 4, 5, 7, 8, 9],7)

if result != -1:
    print('the element is at position {}'.format(result))

else:

    print('the element does not exist')

    