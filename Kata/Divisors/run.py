def Tracie():

    arr = [1, 3, 4, 2, 6]

    n = len(arr)
    AnsArr = []
    max_integer = max(arr)
    times = [0 for i in range(max_integer+1)]
    for i in range(n):
        if arr[i] in times:
            times[arr[i]] += 1
        else:
            times[arr[i]] = 1
    response = [0 for i in range(max_integer+1)]
    for i in range(1, max_integer + 1, 1):
        for j in range(i, max_integer + 1, i):
            if (i == j):
                response[i] += (times[j] - 1)
            else:
                response[i] += times[j]
                response[j] += times[i]
    for i in range(n):
        print(response[arr[i]], end=" ")
        AnsArr.append(response[arr[i]])
    print("\n")
    print(""*5, "Answer appended in a list", ""*5, "\n", AnsArr)


Tracie()
