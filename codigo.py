print("----------Avaliação para Aluguel----------")
print("Prezado(a), seja bem vindo(a) à Central de aluguel da Cars.")
print("Antes de começarmos, leia com atenção as exigências para ser aprovado(a):")
print("Deve cumprir todas as exigências:")
print("1° Possuir fiador ")
print("2° Renda 3x maior que o valor o aluguel ")
print("3° Possuir seguro ")
print(45*"-")
nome = input("Para iniciarmos, digite seu nome: ")
renda = int(input(f"Sr(a) {nome}, qual é o valor da sua renda mensal atualmente? R$"))
aluguel = int(input("Qual é o valor do aluguel? R$"))
fiador = input("O(a) Sr(a) possui fiador?" )
seguro = input("E seguro, o(a) Sr(a) possui seguro?" )
print("----------PROCESSANDO----------")

if fiador == "sim":
    print("Primeiro passo está dentro de nossas exigencias, o(a) Sr(a) possui fiador!")
else:
    print(f"Sr(a){nome}, infelizmente o(a) Sr(a) não cumpriu o 1° de nossas exigências, sem fiador não será possível.")
if renda >= 3 * aluguel:
    print(f'Calculando a sua renda, que está no valor de: R${renda} e o aluguel R${aluguel}, a renda está aprovado(a)!')
else:
    print(f"Sr(a) {nome}, infelizmente o(a) senhora não cumpriu a 2° de nossas exigências, sua renda não está aprovada!")
if seguro == "sim":
    print("Nossa 3° exigência está cumprida, o(a) Sr(a) possui seguro!")
else:
    print("Infelizmente sem o seguro também não será possível")
