from collections import deque

bank = deque(["korim","rafin","hamim"])
#print(bank)
#bank.popleft() --> popleft()  use for  delete left item  in queue!!
bank.append("badsha")
bank.append("durjoy")
print(bank)
