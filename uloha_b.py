pocet_jed = int(input())

jedla = list(input().split())

if not all(x is None for x in jedla) and len(jedla) >= pocet_jed and len(set(jedla)) > 1:
    if sorted(jedla, reverse=True) != jedla:
        print(' '.join(sorted(jedla, reverse=True)))
    else: print(' '.join(sorted(jedla)))
else:
    print("Janka bude frflat")