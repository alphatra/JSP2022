import time

def fibonacci(x) -> int:
    return 1/(1-x-x^2)
start = time.time()
print("hello")
end = time.time()
print(end - start)