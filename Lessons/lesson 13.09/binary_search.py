

def search(l, target, start, end):
    if end > start:
        mid = (start + end) // 2
        if l[mid] == target:
            return mid
        elif l[mid] > target:
            return search(l, target, start, mid-1)
        else:
            return search(l, target, mid+1, end)
    else:
        return -1

l = [1,2,3,4,5,6,7,8,9,10]

print(search(l, 99, 0, len(l)-1))