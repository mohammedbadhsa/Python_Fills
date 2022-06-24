
# useign recusion function for factrials !!
def factrials(n):
    if (n==1):
        return 1
    else:
        return n * factrials(n-1)

print(factrials(40))
print(factrials(4))