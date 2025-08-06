# Parte 03 comandos de repetição
# Laço de repetição for
# for i in range(1,101)
  #  print(i)

'''i = 1
while i <= 10:
      print(f'{i} X 5 = {i * 5}')
      i+=1'''

    segredo = '5'
    erros = 0
    while True:
        chute = input('Dê o seu palpite:')
        if chute == segredo:
            print('acertou')
            break
        else:
            erros += 1
        print(f'Você errou {erros}')