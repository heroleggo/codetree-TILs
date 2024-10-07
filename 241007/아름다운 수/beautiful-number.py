cnt = 0

def func(n):
    data = ['1', '22', '333', '4444']
    
    def select(selected):
        global cnt
        curr_length = len(''.join(selected))
        if curr_length == n:
            cnt += 1
            return
        for i in data:
            if curr_length + len(i) <= n:
                selected.append(i)
                select(selected)
                selected.pop()
    select([])
    return cnt

n = int(input())

print(func(n))