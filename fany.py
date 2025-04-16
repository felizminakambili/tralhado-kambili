
registro_estudantes={}
#perguntar o numero de estudantes
num_estudantes=int(input("quantos estudantes deseja registrar "))

for i in range(1,num_estudantes+1):
    nome=(input(" digite o nome do estudante: "))
    disciplina_estu=int(input(f"quantas disciplinas tem o {nome}?"))
    notas_estu=[]
    #bloco de repitiçao para acumular as notas
    for j in range(1, disciplina_estu+1):
        nota=int(input(f"nota {j}: "))
        notas_estu.append(nota)
registro_estudantes[nome]=notas_estu
#aqui temos o registro final
for nome,notas in registro_estudantes.items():
        print(f"{nome}: {notas}")




