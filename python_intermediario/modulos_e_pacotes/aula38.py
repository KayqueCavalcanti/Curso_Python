import importlib

import aula38_m

print(aula38_m.variavel)

for i in range(10):
    importlib.reload(aula38_m)
    print(i)

print('Fim')