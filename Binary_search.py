#a function that make list and target parameter
#multiple variables: middle, start, end, steps
#recursion or while loop
# increase the step seach time a split is done
# conditions to track target position.


mylist= [1,2,4,7,8,9,10]

def binary_search(list,target):
    middle=0
    start=0
    end=len(list)
    steps=0

    while (steps<=end):
        print("step", steps,":", str(list[start:end+1]))

        steps +=1
        middle =(start+end) // 2
        if target==list[middle]:
            return middle
        if target < list[middle]:
            end= middle -1
        else:
            start= middle + 1
    return -1

binary_search(mylist,4)