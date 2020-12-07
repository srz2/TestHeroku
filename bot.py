import time
import math

def main():
    print("Starting up")
    count = 0
    while True:
        count += 1
        print(f'[{math.trunc(time.time())}]: Working', count)
        time.sleep(5)

if __name__ == "__main__":
    main()