if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arr1 = list(arr)
n_arr = [
    number for number in arr1
    if  number < max(arr1)
]
print(max(n_arr))