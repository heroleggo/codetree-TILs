def helloWorld(n):
    if n == 0:
        return
    else:
        print("HelloWorld")
        helloWorld(n - 1)

n = int(input())

helloWorld(n)