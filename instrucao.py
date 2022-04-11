'''

Verificar velocidade em uma determinada rua

valocidade permitida é 80km/h, receber velocidade de um carro e informa-lo se recebeu um multa leve, grave ou gravíssima, caso não ultrapassou a velocidade vai informa-la que nao recebeu multa alguma.
Levando em consideracao as leis abaixo.
Acima 10km leve
Acima 11km a 20km grave
Acima 21km gravíssima

Analise 
Como descubro km/h?
Como saber valor digitado está correto?

1 - velocidade carro
2 - comparar as velocidades, verificar qual tipo da multa a ser aplicada
3 - velocidade max deve ser em km por horas
4 - mensagem da multa a ser aplicada com base na velocidade
5 - passos

input velocidade_usuario
seta variável velocidade_maxima

if velocidade_usuario > velocidade_maxima
  print(Nao recebeu multa)

if velocidade_usuario < velocidade_maxima
  if velocidade_usuario <= velocidade_maxima + 10
    print(multa leve)

  if velocidade_usuario > velocidade_maxima + 11 && velocidade_usuario > velocidade_maxima + 20
    print(multa grave)

  if velocidade_usuario > velocidade_maxima + 21
    print(multa gravíssima)

'''
