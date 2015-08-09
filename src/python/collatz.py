def collatz(n):
    """
    Generate the collatz sequence starting at n. Terminates at 1 instead of
    iterating through the trivial cycle.
    """
    seq = [n]
    while True:
        if not (n % 2):
            seq.append(n / 2)
        else:
            seq.append(n*3 + 1)
        n = seq[-1]
        if n == 1:
            break
    return seq


def collatz_repeat(n):
    """
    For each number that serves as the start of a Collatz sequence, return two
    tuples (as a dictionary):
        (number first seen in previous sequence, nth iteration of this sequence
                                                 at which we see it.)
        (number starting sequence where first seen, nth iteration of that seq.
                                                    where we first saw it.)
    """
    reverse_at = {}
    result = {}
    for i in range(1, n+1):
        result[i] = [0, 0]
        for i_j, j in enumerate(collatz(i), start=1):
            if j not in reverse_at:
                reverse_at[j] = (i, i_j)
            else:
                result[i] = (j, i_j,
                             reverse_at[j][0],
                             reverse_at[j][1])
                break
    return result


def collatz_reverse(n):
    """
    For each numbers reached by a collatz sequence up to n, track all seeds
    that reach it and at which term they reach it.
    """
    reverse_at = {}
    for i in range(1, n+1):
        for i_j, j in enumerate(collatz(i), start=1):
            if j not in reverse_at:
                reverse_at[j] = [i_j, i]
            else:
                reverse_at[j].extend([i_j, i])
    return reverse_at

def annotate_collatz_repeat(d):
    """
    Annotate collatz_repeat returns so we can easily tell meaning of numbers.
    """
    return {k: ("first_saw", v[0],
                "at_nth", v[1],
                "first_saw_in", v[2],
                "first_nth", v[3]) for k, v in d.items()}

def print_collatz_repeat(d):
    """
    Print to CSV format with colums:
        starting_n, first_saw, saw_at_nth, first_saw_in, first_saw_nth
    """
    for k, v in sorted(d.items()):
        print(str(k) + "," + ",".join((str(x) for x in v)))


if __name__ == "__main__":
    print_collatz_repeat(collatz_reverse(1300))
    # print(annotate_collatz_repeat(collatz_repeat(20)))
