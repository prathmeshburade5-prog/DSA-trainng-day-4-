def selectionSort(arr):

    for i in range(len(arr)):

        min=arr[i]
        loc=i

        for j in range(i+1,len(arr)):

            if min>arr[j]:

                min=arr[j]
                loc=j

        temp=arr[i]
        arr[i]=arr[loc]
        arr[loc]=temp


if __name__ == '__main__':

    arr=[6,23,2,4,1,8,56,3]

    selectionSort(arr)

    print(*arr)