# import sys
from typing import Generator

# sys.set_int_max_str_digits(100_000)


def fib() -> Generator[int, None, None]:
    f2: int = 0
    yield f2
    f1: int = 1
    yield f1
    while True:
        fn: int = f2 + f1
        yield fn
        f2, f1 = f1, fn


def fibn(n: int) -> int:
    for m, result in enumerate(fib()):
        if m >= n:
            break
    return result


def main() -> None:
    n: int = 1000
    result: int = fibn(n)
    # print(result)
    print(f"{n:,d} = {result:d}")
    print(f"Number of digits: {len(str(result))}")


if __name__ == "__main__":
    main()
