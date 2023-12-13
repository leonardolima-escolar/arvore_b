# numpy
# [[][[][]]] (()(()()))
from PrettyPrint import PrettyPrintTree


class No:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None

    def mostra_no(self):
        print(self.valor)


class ArvoreBinaria:
    def __init__(self):
        self.raiz = None

    def altura(self):
        def altura_recursivamente(no):
            if no is None:
                return 0

            altura_esquerda = altura_recursivamente(no.esquerda)
            altura_direita = altura_recursivamente(no.direita)

            return max(altura_esquerda, altura_direita) + 1

        return altura_recursivamente(self.raiz) - 1

    def numero_nos(self, no):
        if no is None:
            return 0

        nos_esquerda = self.numero_nos(no.esquerda)
        nos_direita = self.numero_nos(no.direita)

        return nos_esquerda + nos_direita + 1

    # 4 - Escrever um algoritmo que retorne quantos nós folhas existem na árvore
    def numero_folhas(self, no):
        if no is None:
            return 0

        if no.esquerda is None and no.direita is None:
            return 1

        folhas_esquerda = self.numero_folhas(no.esquerda)
        folhas_direita = self.numero_folhas(no.direita)

        return folhas_esquerda + folhas_direita

    def inserir(self, valor):
        novo_no = No(valor)

        if self.raiz is None:
            self.raiz = novo_no
        else:
            no_atual = self.raiz

            while True:
                if valor < no_atual.valor:
                    if no_atual.esquerda is None:
                        no_atual.esquerda = novo_no
                        return no_atual.esquerda
                    else:
                        no_atual = no_atual.esquerda

                elif valor > no_atual.valor:
                    if no_atual.direita is None:
                        no_atual.direita = novo_no
                        return no_atual.direita
                    else:
                        no_atual = no_atual.direita

                else:
                    print(
                        f"Valor {valor} já existe na árvore.")
                    return None

    def deletar(self, valor):
        self.raiz = self._deletar_recursivamente(self.raiz, valor)

    def _deletar_recursivamente(self, no_atual, valor):
        if no_atual is None:
            return no_atual

        if valor < no_atual.valor:
            no_atual.esquerda = self._deletar_recursivamente(
                no_atual.esquerda, valor)

        elif valor > no_atual.valor:
            no_atual.direita = self._deletar_recursivamente(
                no_atual.direita, valor)

        else:
            if no_atual.esquerda is None:
                return no_atual.direita
            elif no_atual.direita is None:
                return no_atual.esquerda

            sucessor = self._encontrar_sucessor(no_atual.direita)
            no_atual.valor = sucessor.valor
            no_atual.direita = self._deletar_recursivamente(
                no_atual.direita, sucessor.valor)

        return no_atual

    def _encontrar_sucessor(self, no):
        while no.esquerda is not None:
            no = no.esquerda
        return no

    # 3 - Escreva um algoritmo para encontrar um número em uma árvore binária
    def buscar(self, valor):
        return self._buscar_recursivamente(self.raiz, valor)

    def _buscar_recursivamente(self, no, valor):
        if no is None:
            return False

        if valor == no.valor:
            return True
        elif valor < no.valor:
            return self._buscar_recursivamente(no.esquerda, valor)
        else:
            return self._buscar_recursivamente(no.direita, valor)

    # imprimir depois em formato de árvore
    def imprimir(self):
        def imprimir_recursivamente(no_atual):
            if no_atual is None:
                return ""

            resultado = ""
            resultado += f"({imprimir_recursivamente(no_atual.esquerda)})"
            resultado += f"{no_atual.valor}"
            resultado += f"({imprimir_recursivamente(no_atual.direita)})"

            return resultado

        arvore_com_parenteses = imprimir_recursivamente(self.raiz)
        print(arvore_com_parenteses)

    # 2 - Escreva um algoritmo para encontrar o maior e o menor número de uma árvore binária
    def maior_numero(self):
        if self.raiz is None:
            return None

        no_atual = self.raiz
        maior = self.raiz

        while (no_atual):
            maior = no_atual
            no_atual = no_atual.direita

        return maior.valor

    def menor_numero(self):
        if self.raiz is None:
            return None
        no_atual = self.raiz
        menor_no = self.raiz

        while (no_atual):
            menor_no = no_atual
            no_atual = no_atual.esquerda

        return menor_no.valor


arvore = ArvoreBinaria()
arvore.inserir(10)
arvore.inserir(10)
arvore.inserir(5)
arvore.inserir(15)
arvore.inserir(3)
# arvore.inserir(7)
# arvore.inserir(12)
# arvore.inserir(20)
# arvore.deletar(10)
# arvore.deletar(15)
# arvore.inserir(-1)
# arvore.inserir(-2)
# arvore.deletar(5)
print(arvore.altura())
print(arvore.numero_nos(arvore.raiz))
print(f"Na árvore existem {arvore.numero_folhas(arvore.raiz)} nós folhas")
print(f"Número 10 existe na arvore? {arvore.buscar(10)}")
print(f"Número 111 existe na arvore? {arvore.buscar(111)}")
print(f"Maior número: {arvore.maior_numero()}")
print(f"Menor número: {arvore.menor_numero()}")

arvore.imprimir()

# 1 - Faça um algoritmo para preencher as seguintes sequências:  [1 2 3 4 5 6 7 8 9] e [3 2 6 5 4 1 7 8 9], respectivamente
arvore_o = ArvoreBinaria()
arvore_no = ArvoreBinaria()

for numero in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
    arvore_o.inserir(numero)
for numero in [3, 2, 6, 5, 4, 1, 7, 8, 9]:
    arvore_no.inserir(numero)

arvore_o.imprimir()
arvore_no.imprimir()

print("Árvore Original:")
ppt = PrettyPrintTree(
    lambda x: [x.esquerda, x.direita] if x else [],
    lambda x: str(x.valor) if x else ""
)
ppt(arvore_o.raiz)

print("Árvore Não-Ordenada:")
ppt(arvore_no.raiz)
