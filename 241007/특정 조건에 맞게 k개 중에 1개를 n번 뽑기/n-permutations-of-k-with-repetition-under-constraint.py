[k, n] = list(map(int, input().split()))

answer = []

def func():
    data = [i + 1 for i in range(k)]

    def choose():
        length = len(answer)
        if length == n:
            print(' '.join([str(x) for x in answer]))
            return
        if length < 2:
            for i in data:
                answer.append(i)
                choose()
                answer.pop()
        else:
            for i in data:
                if answer[length - 1] != i or answer[length - 2] != i:
                    answer.append(i)
                    choose()
                    answer.pop()
    
    choose()

func()