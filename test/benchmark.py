from timeit import timeit
import sys

# invoke w/either python or pypy

sys.path.append('src/python')

if __name__ == "__main__":
    imports = "from collatz import collatz, collatz_repeat, collatz_reverse"
    print(timeit("collatz(10000)", setup=imports))

# these don't finish at moment, Julia hits it in 0.83 and 1.1 seconds in what
# should be same general complexity (but typed arrays, etc.)
#    print(timeit("collatz_repeat(10000)", setup=imports))
    print(timeit("collatz_reverse(10000)", setup=imports, number=5))
