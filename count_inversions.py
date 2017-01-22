def merge(a, l, m, h):
    inversions = 0
    i = l
    j = m + 1
    k = l
    m_a = list(a)
    while(i <= m and j <= h):
        if (m_a[j] < m_a[i]):
            a[k] = m_a[j]
            j = j + 1
            inversions = inversions + (m - i + 1)
        else:
            a[k] = m_a[i]
            i = i + 1
        k = k + 1
    while(i <= m):
        a[k] = m_a[i]
        k = k + 1
        i = i + 1
    while(j <= h):
        a[k] = m_a[j]
        k = k + 1
        j = j + 1
    return inversions

def mergesort(a, l, h):
    m = (l+h)/2
    if (l < h):
        il = mergesort(a, l, m)
        ir = mergesort(a, m+1, h)
        im = merge(a, l, m, h)
        return il + ir + im
    else:
        return 0

def count_inversions(a):
    return mergesort(a, 0, len(a)-1)

t = int(raw_input().strip())
for a0 in xrange(t):
    n = int(raw_input().strip())
    arr = map(int, raw_input().strip().split(' '))
    print count_inversions(arr)
