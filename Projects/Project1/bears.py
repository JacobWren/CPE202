def bears(n):
    """A True return value means that it is possible to win
          the bear game by starting with n bears. A False return value means
          that it is not possible to win the bear game by starting with n
          bears."""
    # 2 base cases
    if n == 42:
        return True
    if n < 42:
        return False
    if n % 2 == 0 and bears(n // 2):
        return True
    if (n % 3 == 0 or n % 4 == 0) and ((int(str(n)[-2:][0]) * int(str(n)[-2:][1]))) != 0 and \
            bears(int(n - (int(str(n)[-2:][0]) * int(str(n)[-2:][1])))):
        return True
    if n % 5 == 0 and bears(int(n - 42)):
        return True
    # This is a quasi base case. It is equivalent to negating all of the previously defined rules.
    # If this is run, then the path we took was a bad path so we will re-trace ALL of our steps until we could have
    # taken a different path.
    return False

#print(bears(500))
