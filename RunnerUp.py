def main(n, arr):
    arr.sort()
    mx = max(arr[0], arr[1])
    secondmax = min(arr[0], arr[1])
    n = len(arr)
    for i in range(2, n):
        if arr[i] > mx:
            secondmax = mx
            mx = arr[i]
        elif arr[i] > secondmax and mx != arr[i]:
            secondmax = arr[i]
    print(secondmax)

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    main(n, arr)