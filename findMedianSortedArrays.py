def findMedianSortedArrays(A,B):
    n,m = len(A),len(B)
    if n>m:
        findMedianSortedArrays(B,A)
    
    k = (n+m+1)//2 # left partition size of merged array AB
    
    left,right = 0,len(A)-1 # A's index solution space is left <= X <= right
    while left < right:
        cutRightA = (left+right)//2 + 1 # left index of A's right partition
        cutRightB = k - cutRightA
        cutLeftA = cutRightA - 1
        cutLeftB = cutRightB - 1
        
        print([cutLeftA,cutLeftB])

        if cutRightA >= n:
            right = cutLeftA-1
        elif cutRightB >= m:
            left = cutRightA
        elif A[cutLeftA] > B[cutRightB]:
            right = cutLeftA-1
        elif B[cutLeftB] > A[cutRightA]:
            left = cutRightA
        else:
            left = cutLeftA
            right = cutRightA
    
    cutRightA = (left+right)//2 + 1 # left index of A's right partition
    cutRightB = k - cutRightA
    cutLeftA = cutRightA - 1
    cutLeftB = cutRightB - 1

    c1 = max(A[cutLeftA] if cutLeftA >= 0 else -float('inf'),
            B[cutLeftB] if cutLeftB >= 0 else - float('inf'))
    c2 = min(A[cutRightA] if cutRightA < n else float('inf'),
                B[cutRightB] if cutRightB < m else float('inf'))
    
    return c1 if (n+m)%2 == 1 else c1/2 + c2/2

print(findMedianSortedArrays([1,3],[1,2,3,4]))
