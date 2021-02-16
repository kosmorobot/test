
from itertools import zip_longest

employees=["Greg McGuiness", "Lola White", "Richard Bright", "Chloe Nelson", "Bradley Long", "Chiara Samos"]

print([
    n for n, (f, l) in zip_longest(employees, (e.split(' ') for e in employees))
    if f[0].lower() == f[-1].lower()
    or l[0].lower() == l[-1].lower()
])
