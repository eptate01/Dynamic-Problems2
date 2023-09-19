
def knapsack(arr, index, values):
    if index == len(arr):
        return 0
    putIn1, putIn2, putInNone = 0,0,0
    if values[0] >= arr[index]:
        temp = [values[0] - arr[index], values[1]]
        putIn1 = arr[index] + knapsack(arr, index+1, temp)
    if values[1] >= arr[index]:
        temp = [values[0] , values[1]- arr[index]]
        putIn2 = arr[index] + knapsack(arr, index+1, temp)
    putInNone = knapsack(arr, index+1, [i for i in values])
    possibilities_array[index][values[0]][values[1]] = max(putInNone, max(putIn1, putIn2))
    return possibilities_array[index][values[0]][values[1]]

def coinChange(arr, k):
    INF = 100000
    dp=[INF] * (k+1)
    dp[0]=0
    
    for coin in arr:
        for i in range(coin, k+1):
            if i-coin>=0:
                dp[i]=min(dp[i], dp[i-coin]+1)
    
    return -1 if dp[-1]==INF else dp[-1]

def findPartition(arr):
    n = len(arr)
    arrSum = sum(arr)
    halfSum = arrSum // 2
    if arrSum % 2 != 0:
        return False
 
    part = [[True for i in range(0,n + 1)] for j in range(0, halfSum + 1)]
 
    for i in range(1, arrSum // 2 + 1):
        part[i][0] = False
 
    for i in range(1, arrSum // 2 + 1):
 
        for j in range(1, n + 1):
            part[i][j] = part[i][j - 1]
 
            if i >= arr[j - 1]:
                part[i][j] = (part[i][j] or part[i - arr[j - 1]][j - 1])
 
    return part[halfSum][n]

def chainMultiplication(arr):
    N = len(arr) - 1
    C = [[0 for _ in range(N+1)] for _ in range(N+1)]
    # Base case
    for i in range ( 1, N + 1 ):
        C[i][i] = 0
    for length in range ( 2, N + 1 ): #chain length
        for i in range ( 1, N - length + 2 ): #rows
            j = i + length - 1
            C[i][j] = 0
            for k in range ( i, j ) :
                q = C[i][k] + C[k+1][j] + arr[i-1] * arr[k] * arr[j]
                if C[i][j] < q:
                    C[i][j] = q
    return C[1][N] 

arr = [8, 2, 6,7,4,3]
maxN, maxW = 26, 26
possibilities_array = [[[-1] * maxW] * maxW] * maxN
# Capacity of knapsacks
weights = [11,4]
# Function to be called
print(knapsack(arr, 0, weights))


print(findPartition([1,2,3,4]))

print(coinChange([5,1],11)) #to make 5. Number of denominations = 3

print(chainMultiplication([50,20,1,10,100]))