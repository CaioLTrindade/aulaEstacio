def calcular_media(notas):
    return sum(notas) / len(notas)

def avaliar_aluno(media):
    if media >= 7:
        print("Aprovado")
    elif media >= 5:
        print("Recuperação")
    else:
        print("Reprovado")

if __name__ == '__main__':
    alunos = []
    while True:
        nome = input("Digite seu nome: ")
        notas = []
        for i in range(3):
            nota = float(input("Digite sua nota: "))
            notas.append(nota)

        media = calcular_media(notas)
        situacao = avaliar_aluno(media)

        alunos.append({
            "nome": nome,
            "notas": notas,
            "media": media,
            "situacao": situacao
        })
continuar = input("Deseja cadastrar mais alunos? [S/N]")

if continuar != "S":
    break

for aluno in alunos:
        print(f"{aluno['nome']} - {aluno['notas']} - {aluno['media']: .1f} - {aluno['situacao']}")

        print("Fim")


