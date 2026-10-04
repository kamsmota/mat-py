print("Digite o número de linhas da matriz: ")
linhas = int(input())

print("Digite o número de colunas da matriz: ")
colunas = int(input())

matriz = []

for i in range(linhas):
    ordem = True
    while ordem:
        print(f"Digite os valores da linha {i + 1} separados por espaço: ")
        entrada = input()
        valores = entrada.split()
        if len(valores) == colunas:
            linha = []
            for j in valores:
                linha.append(int(j))
    
            matriz.append(linha)
            ordem = False
        else:
            ordem = True
        print(ordem)
        
print("Matriz final: ")
for linha in matriz:
    print(linha)