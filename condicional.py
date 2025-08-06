media = 75
frequencia = 1
media_aprovacao = 60
frequencia_minima = 0.75

#if media >= media_aprovacao:
    #print('Aluno aprovado por média')
#else:
   # print('Aluno reprovado por média')

#codigo limpo
'''
is_approved = media= media_aprovacao

if is_approved:
    print('Student is approved')
else:
    print('Student is not approved')
    

is_approved = media >= media_aprovacao and frequencia >= frequencia_minima
print(is_approved)'''

experiencia = 1
tem_mestrado = False

esta_apto = experiencia >=5 or tem_mestrado == True
print(esta_apto)

if esta_apto:
    print('Enviar E-mail')
else:
    print('Descartar curriculo')