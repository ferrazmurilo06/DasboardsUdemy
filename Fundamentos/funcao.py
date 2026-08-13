# def welcome():
#     print("Bem-vindo(a) ao sistema de filmes!")

# for i in range(3):
#     welcome()

def media():
    num_ratings = int(input("Digite o número de avaliações: "))
    total = 0
    for i in range(num_ratings):
        note = float(input(f"Digite a nota para o filme: "))
        total += note
    if num_ratings > 0:
        average = total / num_ratings
    else:
        average = 0
    return average

print(media())