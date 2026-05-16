def diagonalDifference(arr):

    left=0
    right=0

    n=len(arr)

    for i in range(n):

        left=left+arr[i][i]

        right=right+arr[i][n-1-i]

    return abs(left-right)


arr=[
    [1,2,3],
    [4,5,6],
    [9,8,9]
]

print(diagonalDifference(arr))