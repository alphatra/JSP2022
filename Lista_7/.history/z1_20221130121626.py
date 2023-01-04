import time

def fibonacci(x) -> int:
    return 1/(1-x-x^2)
start = time.time()
print(f"x -> 10 fibonacci(x=10):{fibonacci(10)}")
end = time.time()
print(end - start)