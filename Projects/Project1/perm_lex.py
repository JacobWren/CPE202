import math


def perm_gen_lex_list(a):
    """Generates all the permutations of the characters in a string in lexicographic order."""
    lg = len(a)
    # 2 bases cases
    if a == "":
        return []
    if lg == 1:
        return a[0]
    # initialize empty lists
    p = []
    m = []
    b = a[:]
    for j in range(len(a)):
        a = b
        a = list(a)
        x = a.pop(j) # takes last character of 'a'
        Output = perm_gen_lex_list(a)
        m.append([x] + [Output]) # Concatenate the last character only ONCE to permutation of the remaining characters!
        # We build up to generating the final permutated list. The final permutated list is
        # complete when perm_gen_lex(a) has length equal to the input string minus one.
        if type(Output) == list and len(Output) == math.factorial(lg - 1):
            # Remember in line 20 we only concatenate the last character once. But since there are potentially many
            # permutations this needs to be done 'len(Output)' times
            for i in range(len(Output)):
                p.append([x] + Output[i])
    # This is similar to the if statements in line 24
    if len(p) == math.factorial(lg):
        m = p
    return m

#x = perm_gen_lex_list('a')
#print(x)


# This function is needed because we worked with lists not strings above.
def perm_gen_lex(x):
    x = perm_gen_lex_list(x)
    """This second function simply takes a 2D list from 'perm_gen_lex_list' into a 1D list. 
    It also makes each sublist into a single string."""
    e = ""
    n = []
    for i in x:
        for j in i:
            e = e + j
        n.append(e)
        e = ""
    return n

#print(perm_gen_lex('abc'))
