def func(k, n):
    # 초기화
    data = [i for i in range(1, k + 1)]

    def select(selected):
        d = selected
        # 종료조건 작성
        if len(selected) == n:
            print_data(selected)
            return
        # 재귀 작성
        for i in data:
            d.append(i)
            select(d)
            d.pop()
    select([])


def print_data(arr):
    print(' '.join([str(x) for x in arr]))


[k, n] = list(map(int, input().split()))

func(k, n)