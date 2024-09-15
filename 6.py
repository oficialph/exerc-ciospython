nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

media = (nota1 + nota2) / 2

if media >= 7:
    print(f"Média: {media:.2f}. O aluno está aprovado!")
else:
    print(f"Média: {media:.2f}. O aluno está em exame.")