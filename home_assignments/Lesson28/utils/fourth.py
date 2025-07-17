# Task 4: Utility module with a factorial function

def faktorialas(n):
    if n <= 1:
        return 1
    return n * faktorialas(n - 1)
