rows, cols = 5, 10
arr = [[0]*cols]*rows # all rows refernce to the same list!
print(arr, "before")

arr[0][0] = 1
arr[rows - 1][cols - 1] = 5
print(arr, "after")

arr = [[0] * cols for _ in range(rows)]
arr[0][0] = 1
arr[rows - 1][cols - 1] = 5
print(arr, "after good initialization")

arr = [[0 for i in range(cols)] for j in range(rows)]
arr[0][0] = 1
arr[rows - 1][cols - 1] = 5
print(arr, "another good initialization")