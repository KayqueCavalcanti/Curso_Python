from sys import path

# Forma 1: Importando o caminho completo do módulo
import aula39_package.modulo
# Forma 2: Importando o módulo direto de dentro do pacote
from aula39_package import modulo
# Forma 3: Importando tudo o que está dentro do módulo (má prática comentada na aula)
from aula39_package.modulo import variavel, nova_variavel
#from aula39_package.modulo import *

# Linhas de teste comentadas na imagem do curso:
# from aula39_package.modulo import soma_do_modulo
# print(*path, sep='\n')
# print(soma_do_modulo(1, 2))

# Execução das linhas ativas da imagem:
print(aula39_package.modulo.soma_do_modulo(1, 2))  # Testa a Forma 1
print(modulo.soma_do_modulo(1, 2))                 # Testa a Forma 2
print(variavel)                                     # Testa os dados vindos da Forma 3
print(nova_variavel)                                # Testa os dados vindos da Forma 3