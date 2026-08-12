nome = input("Digite o nome do filme: ")
ano = int(input("Digite o ano do filme: "))
nota_imdb = float(input("Digite a nota do filme no IMDB: "))

if nota_imdb > 8.0 or ano > 2015:
    print(f"O filme {nome} é considerado um sucesso de crítica!")
else:
    print(f"O filme {nome} não é considerado um sucesso de crítica.")