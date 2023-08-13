# Livrarias centrais
import colorama
from colorama import Fore
import random
import time
import os
import sys
from random import randint
from time import sleep


# Creditos da equipe
print('''Esse é um trabalho coletivo feito por:

Leandro
Ana Lívia
Benete
Kelwin
Vitor
''')
time.sleep(3)

# O tanto de dinheiro que você têm
money = 0
devil_money = 0
loan = 0
loan_shark = 0

coin = ''
yakuza = ''
# Nome da pessoa
name = input('Em primeiro lugar, qual o seu nome?: ')

# O começo do jogo
print("Você acorda um dia e decide que vai apostar tudo num cassino perto de casa")
print()
money = random.randint(1000,3000)
print('Você tem R$', money, 'para apostar')
print()

# Seleção de jogo
while True:

  if money < 0:
    break

  if 3000 < money < 5000:
    life = input('Deseja parar de jogar (y/n)?: ')
    if life == 'y':
      print('Você vai para casa com todo o seu dinheiro e decide apostar mais no dia seguinte')
      break
    if life == 'n':
      continue

  if money > 10000:
    print('Você fica com todo o dinheiro que você ganhou e decide melhorar a sua vida')
    break

  if coin == 'n':
    break
  
  print("""Esses são os jogos os jogos do primeiro andar

[1] Jogo do 21
[2] Caça-níquel
[3] Jogo do Bicho
[4] RPG do Kelwin
""")
  print('Para jogar um rpg, digite: rpg')
  print()
  selec = input("Que jogo você deseja jogar? ")
  
# Jogo do 21
  if (selec == "1"):
    # Regras do jogo
    print('O objetivo do jogo é chegar mais perto do número 21, sem ultrapassar ele, para isso: o dealer dá 2 cartas para o jogador, enquanto o mesmo deixa uma carta virada para baixo, você tem que ter o número mais próximo de 21')
    time.sleep(5)
    os.system('clear')
    # Trabalhar o negócio do dealer e do jogador
    while True:
      print ()
      print("Vamos jogar um jogo de 21")
      print()
      # As variáveis centrais
      bet = 0
      qtd1s = 0
      qtd2s = 0
      vitorias = 0
      print('Você tem R$', money)
      i = random.randint(0,2000)
      # A aposta do jogador
      while True:
          print('Esse é o valor do bolâo: R$', i)
          bet = int(input('Quanto você deseja apostar?: '))
          if money < 0:
            i = i + bet
            money = money - bet
            print('Agora você tem uma dívida de R$', money)
            print()
            break
          if (bet >= money) or (bet <= money):
            i = i + bet
            money = money - bet
            print('Agora você tem R$', money)
            print()
            break
          else:
            print('Esse valor não existe, tente novamente')
            print()
            continue
      # O nome do jogador
      print("Sua vez", name)
      print()
      # As cartas do dealer
      print('O dealer vai dar as cartas')
      for x in range (0,2):
        D = random.randint(1,10)
        print('Suas cartas são:', D)
        if D >= 1:
           qtd1s = qtd1s + D
      print()
      print('O número total das cartas que você recebeu:', qtd1s)
      print()
        # O funcionamento central do J1
      while True:
        qtd = int(input("Quantas cartas você gostaria de pegar?: "))
        print()
        for x in range (0,qtd):
          N = random.randint(1,10)
          print('Suas cartas são:', N)
          if (N>=1):
            qtd1s = qtd1s + N
        print()
        print('O total de cartas que você têm:', qtd1s)
        print()
        print('...')
        time.sleep(2)
      # O resultado final, do total das cartas
        if (qtd1s>21):
          print ('Seu número de cartas ultrapassou 21')
          print()
          print("Sua vez passou")
          print ('/' * 40)
          break
        if (qtd1s==21):
          print('Você ganhou essa partida')
        if (qtd1s<21):
          print('Você deseja puxar mais outra carta?')
          x = input('y/n: ')
          print ()
     # O Jogador 1 irá puxar mais cartas
        if (x == 'y'):
          continue
        else:
          print ("Sua vez passou")
          print('/' * 40)
          break
        time.sleep(2)
          
      # O funcionamento do dealer
      while True:
        for x in range (0,2):
          M = random.randint(1,10)
          print('Suas cartas são:', M)
          if (M>=1):
            qtd2s = qtd2s + M
        print()
        print('O total de cartas que você têm:', qtd2s)
        print()
        print('...')
        time.sleep(2)
        # O resultado final, do total das cartas
        if (qtd2s>21):
          print('O número de cartas do dealer ultrapassou 21')
          print("O jogo acabou")
          print('!' * 40)
          print()
          print('Agora iremos ver os resultados...')
          time.sleep(3)
          break
        if (qtd2s==21):
          print('O dealer ganhou essa partida')
          break
        else:
          print ('O dealer e o jogador decidiram as suas mãos')
          print("O jogo acabou")
          print('!' * 40)
          print()
          print('Agora iremos ver os resultados...')
          time.sleep(3)
          break
      # O resultado final
      if (qtd1s < 21) and (qtd2s > 21):
        print (name, 'ganhou o jogo')
        vitorias = vitorias + 1
        money = money + i
      if (qtd1s > 21) and (qtd2s < 21):
        print('Você perdeu')
      if (qtd1s > qtd2s) and (qtd1s < 21) and (qtd2s < 21):
        print(name, 'ganhou o jogo')
        vitorias = vitorias + 1
        money = money + i
      if (qtd2s > qtd1s) and (qtd1s < 21) and (qtd2s < 21):
        print ('Você perdeu')
      if (qtd1s == 21) and (qtd2s < qtd1s):
        print(name, 'ganhou o jogo')
        vitorias = vitorias + 1
        money = money + i
      if (qtd2s == 21) and (qtd1s < qtd2s):
        print('Você perdeu')
      if (qtd1s == qtd2s):
        print ('O jogo empatou')
        
      print('Agora você tem', money)
    
      # Retry
      print('Você deseja jogar de novo?')
      chance = input('y/n?: ')
      print('/' * 30)
      print()
      if (chance == "y"):
        os.system('clear')
        continue
      if (chance == 'n'):
        # Suas vitórias
        if (vitorias >= 1):
          print('O tanto de vezes que você ganhou:',vitorias)
        print()
        # Fim do jogo
        print("Você deseja outro jogo?")
        coin = input("y/n? ")
        print('/' * 30)
        if (coin == "y"):
          os.system('clear')
          break
        if coin == 'n':
          break
        else:
          print('Não é essa tecla')

# Caça-níquel
  if (selec == "2"):
    print(''' 
  ▄████▄   ▄▄▄       ▄████▄   ▄▄▄          ███▄    █  ██▓  █████   █    ██ ▓█████  ██▓    
  ▒██▀ ▀█  ▒████▄    ▒██▀ ▀█  ▒████▄        ██ ▀█   █ ▓██▒▒██▓  ██▒ ██  ▓██▒▓█   ▀ ▓██▒    
  ▒▓█    ▄ ▒██  ▀█▄  ▒▓█    ▄ ▒██  ▀█▄     ▓██  ▀█ ██▒▒██▒▒██▒  ██░▓██  ▒██░▒███   ▒██░    
  ▒▓▓▄ ▄██▒░██▄▄▄▄██ ▒▓▓▄ ▄██▒░██▄▄▄▄██    ▓██▒  ▐▌██▒░██░░██  █▀ ░▓▓█  ░██░▒▓█  ▄ ▒██░    
  ▒ ▓███▀ ░ ▓█   ▓██▒▒ ▓███▀ ░ ▓█   ▓██▒   ▒██░   ▓██░░██░░▒███▒█▄ ▒▒█████▓ ░▒████▒░██████▒
  ░ ░▒ ▒  ░ ▒▒   ▓▒█░░ ░▒ ▒  ░ ▒▒   ▓▒█░   ░ ▒░   ▒ ▒ ░▓  ░░ ▒▒░ ▒ ░▒▓▒ ▒ ▒ ░░ ▒░ ░░ ▒░▓  ░
    ░  ▒     ▒   ▒▒ ░  ░  ▒     ▒   ▒▒ ░   ░ ░░   ░ ▒░ ▒ ░ ░ ▒░  ░ ░░▒░ ░ ░  ░ ░  ░░ ░ ▒  ░
  ░          ░   ▒   ░          ░   ▒         ░   ░ ░  ▒ ░   ░   ░  ░░░ ░ ░    ░     ░ ░   
  ░ ░            ░  ░░ ░            ░  ░            ░  ░      ░       ░        ░  ░    ░  ░
  ░                  ░                                                                     ''')
    print()
    time.sleep(2)
    print()
    while True:
      print('Uma ficha custa 10 reais')
      token = int(input('Quantas fichas você vai comprar?: '))
      money = money - token * 10
      print('Você tem R$', money)
      if money < 10:
        print('Você não tem dinheiro suficiente')
      for x in range(0, token):
        a = random.randint(1,7)
        b = random.randint(1,7)
        c = random.randint(1,7)
        print(a, b, c)
        time.sleep(2)
        if (a == b or b == c or a == c):
          print('Parabéns, você conseguiu R$ 100')
          print()
          money = money + 100
          continue
        if (a == 7 and b == 7 and c == 7):
          print ("GRANDE PRÊMIO")
          time.sleep(2)
          print('Você ganhou R$ 5000')
          money = money + 5000
          continue
      print('Você tem R$', money)
        
    # Retry
      print('Você deseja jogar de novo?')
      chance = input('y/n?: ')
      print('/' * 30)
      print()
      if (chance == "y"):
        os.system('clear')
        continue
      if (chance == 'n'):
        print()
        # Fim do jogo
        print("Você deseja outro jogo?")
        coin = input("y/n? ")
        print('/' * 30)
        if (coin == "y"):
          os.system('clear')
          break
        if coin == 'n':
          break
        else:
          print('Não é essa tecla')

# Jogo do Bicho
  if selec == '3':
    print('O jogo envolve em você escolher um número que se relacione a um grupo/animal, se você acertar o número na categoria, você ganha 18 vezes o valor que apostou')
    while True:
      bet = int(input('Quando você aposta?: '))
      if bet > money:
        money = money - bet
        print('Agora você tem uma dívida de R$', money)
        print()
        break
      if bet <= money:
        money = money - bet
        print('Agora você tem R$', money)
        print()
        break
      else:
        print('Esse valor não existe, tente novamente')
        continue
    print()
    time.sleep(2)
    print('''Esses são os grupos para escolher:
Grupo 1: Avestruz
Números: 01 - 02 - 03 - 04

Grupo 2: Águia
Números: 05 - 06 - 07 - 08

Grupo 3: Burro
Números: 09 - 10 - 11 - 12

Grupo 4: Borboleta
Números: 13 - 14 - 15 - 16

Grupo 5: Cachorro
Números: 17 - 18 - 19 - 20

Grupo 6: Cabra
Números: 21 - 22 - 23 - 24

Grupo 7: Carneiro
Números: 25 - 26 - 27 - 28

Grupo 8: Camelo
Números: 29 - 30 - 31 - 32

Grupo 9: Cobra
Números: 33 - 34 - 35 - 36

Grupo 10: Coelho
Números: 37 - 38 - 39 - 40

Grupo 11: Cavalo
Números: 41 - 42 - 43 - 44

Grupo 12: Elefante
Números: 45 - 46 - 47 - 48

Grupo 13: Galo
Números: 49 - 50 - 51 - 52

Grupo 14: Gato
Números: 53 - 54 - 55 - 56

Grupo 15: Jacaré
Números: 57 - 58 - 59 - 60

Grupo 16: Leão
Números: 61 - 62 - 63 - 64

Grupo 17: Macaco
Números: 65 - 66 - 67 - 68

Grupo 18: Porco
Números: 69 - 70 - 71 - 72

Grupo 19: Pavão
Números: 73 - 74 - 75 - 76

Grupo 20: Peru
Números: 77 - 78 - 79 - 80

Grupo 21: Touro
Números: 81 - 82 - 83 - 84

Grupo 22: Tigre
Números: 85 - 86 - 87 - 88

Grupo 23: Urso
Números: 89 - 90 - 91 - 92

Grupo 24: Veado
Números: 93 - 94 - 95 - 96

Grupo 25: Vaca
Números: 97 - 98 - 99 - 00
''')
    choice = int(input('Selecione 4 números (sem virgula): '))
    numbers = []
    for x in range(1,6):
      y = random.randint(1000,9999)
      print(x, 'Categoria:', y)
      z = divmod(y,100)
      a = list(z)
      numbers.append(a)
    mylist = [x for xs in numbers for x in xs]
    b = divmod(choice,100)
    mylist2 = list(b)
    check = any(item in mylist for item in mylist2)
    if check is True:
      print('Parabéns, você acertou uma das categorias')
      money = bet * 18
      print('Você tem R$', money)
    else:
      print('Que pena')

    print('Você deseja jogar de novo?')
    chance = input('y/n?: ')
    print('/' * 30)
    print()
    if (chance == "y"):
      os.system('clear')
      continue
    if (chance == 'n'):
      print()
      # Fim do jogo
      print("Você deseja outro jogo?")
      coin = input("y/n? ")
      print('/' * 30)
      if (coin == "y"):
        os.system('clear')
        break
      if coin == 'n':
        break
      else:
        print('Não é essa tecla')

# RPG do Kelwin
  if selec == "4":
    print("\n" * 55)
    dx1 = "bem vindo a esse pequeno jogo de combate!!"
    for letter in dx1:
        print(letter, end='', flush=True)
        sleep(0.001)
    time.sleep(2)
    print("")
    dx2 = "aqui veremos o quanto você é bom com estratégias"
    for letter in dx2:
        print(letter, end='', flush=True)
        sleep(0.001)
    time.sleep(2)
    print("")
    dx3 = "isso"
    for letter in dx3:
        print(letter, end='', flush=True)
        sleep(0.001)
    time.sleep(2)
    print("")
    dx4 = "se você escolher jogar no difícil"
    for letter in dx4:
        print(letter, end='', flush=True)
        sleep(0.001)
    time.sleep(2)
    print("")
    dx5 = "se estiver pronto para começar..."
    for letter in dx5:
        print(letter, end='', flush=True)
        sleep(0.001)
    time.sleep(2)
    print("")
    input("pressione enter")
    print("")
#escolha de dificuldade
    while True:
      print("escolha sua dificuldade:")
      print("1 - Facil\n2 - Médio\n3 - dificil")
      d = input(">")
  
      if d == "1":
       r1 = 1
       r2 = 15
       r5 = 5
       r6 = 10
       rlifeplayer = 80
       rlifeenemy = 50
       break
    
      if d == "2":
       r1 = 1
       r2 = 13
       r5 = 5
       r6 = 13
       rlifeplayer = 100
       rlifeenemy = 100
       break
    
      if d == "3":
       r1 = 1
       r2 = 13
       r5 = 8
       r6 = 18
       rlifeplayer = 150
       rlifeenemy = 200
       break 
      else:
            print("Escolha inválida. Tente novamente.")
        
    if d == "3":
      print("")
      dx6 = "Vai mesmo jogar jogo difícil?"
      for letter in dx6:
        print(letter, end='', flush=True)
        sleep(0.001)
      time.sleep(2)
      print("")
      dx7 = "[1] Claro"
      for letter in dx7:
        print(letter, end='', flush=True)
        sleep(0.001)
      print("")
      dx8 = "[2] Estou querendo desistir, não sei se consigo"
      for letter in dx8:
        print(letter, end='', flush=True)
        sleep(0.001)
      time.sleep(1)
      print("")
      dd = input(">")
      print("")
      while True:
         if dd == "2":
           dx9 = "pensei que pra você"
           for letter in dx9:
             print(letter, end='', flush=True)
             sleep(0.001)
           time.sleep(2)
           print("")
           dx10 = "palavras fossem apenas palavras..."
           for letter in dx10:
             print(letter, end='', flush=True)
             sleep(0.001)
           time.sleep(2)
           print("")
           break
         elif dd == "1":
           print("")
           dx11 = "Então vamos lá..."
           for letter in dx11:
             print(letter, end='', flush=True)
             sleep(0.001)
           time.sleep(2)
           print("")
           break
         else:
           print("Escolha inválida. Tente novamente.")
    if dd == "2":
      break
    
#escolha de pack de magias
    while True:
      print("escolha seu pack de magias")
      print("1 - bola de fogo, raio roxo, trovoadas")
      print("2 - Trovoadas, Raio roxo, chuva ácida")
      print("3 - bola de fogo, chuva ácida, raio roxo")
      magic = input(">")
      if magic == "1":
        print("ótimo, você escolheu seu pack de magias")
        break
      if magic == "2":
        print("ótimo, você escolheu seu pack de magias")
        break
      if magic == "3":
        print("ótimo, você escolheu seu pack de magias")
        break
      else:
         print("Escolha inválida. Tente novamente.")

    class Jogador:
      def __init__(self, nome, hp_maximo):
        self.nome = nome
        self.hp_maximo = hp_maximo
        self.hp_atual = hp_maximo
      def atacar(self, inimigo):
        dano = random.randint(r1, r2)
        inimigo.hp_atual -= dano
        print(f"{self.nome} ataca {inimigo.nome} e causa {dano} de dano!")
        if inimigo.hp_atual <= 0:
            EndOfGame.deathofenemy()
        else:
          inimigo.atacar(jogador)
    class Inimigo:
      def __init__(self, nome, hp_maximo):
        self.nome = nome
        self.hp_maximo = hp_maximo
        self.hp_atual = hp_maximo
      def atacar(self, jogador):
        dano = random.randint(r5, r6)
        jogador.hp_atual -= dano
        print(f"{self.nome} ataca {jogador.nome} e causa {dano} de dano!")
        if jogador.hp_atual <= 0:
            EndOfGame.death()
    class Flowers:
      def __init__(self, flower_max):
        self.flower_max = flower_max
        self.flower_atual = flower_max
    class Curas:
      def cogumelo(jogador):
        cura = random.randint(1,30)
        while True:
         if flower.flower_atual == 0 or flower.flower_atual <3:
           print("Flores insuficientes")
           break
         else:
           flower.flower_atual -= 3
           jogador.hp_atual += cura
           if jogador.hp_atual > jogador.hp_maximo:
             jogador.hp_atual = jogador.hp_maximo
           print(f"{jogador.nome} consome um cogumelo que carregava consigo e recupera {cura} de HP !! \nA batalha está ficando intensa")
           inimigo.atacar(jogador)
           break
      def erva(jogador):
       cura = random.randint(1,45)
       while True:
         if flower.flower_atual == 0 or flower.flower_atual <5:
           print("Flores insuficientes")
           break
         else:
           flower.flower_atual -= 5
           jogador.hp_atual += cura
           if jogador.hp_atual > jogador.hp_maximo:
             jogador.hp_atual = jogador.hp_maximo
           print(f"{jogador.nome} consome uma ervinha verde de cura que carregava consigo e recupera {cura} de HP !! \nA batalha está ficando intensa")
           inimigo.atacar(jogador)
           break
    class Magia:
      def boladefogo(inimigo):
        dano = random.randint(1,20)
        while True:
         if flower.flower_atual == 0 or flower.flower_atual < 4:
           print("Flores insuficientes")
           break
         else:
           flower.flower_atual -= 4
           inimigo.hp_atual -= dano
           print(f"{jogador.nome} usa a magia bola de fogo em {inimigo.nome} e causa {dano} de dano !!")
           if inimigo.hp_atual <= 0:
               EndOfGame.deathofenemy()
           else:
             inimigo.atacar(jogador)
             if jogador.hp_atual <= 0:
                 EndOfGame.death()
           break
      def trovoadas(inimigo):
        dano = random.randint(1,10)
        while True:
         if flower.flower_atual ==0 or flower.flower_atual <3:
           print("Flores insuficientes")
           break
         else:
           flower.flower_atual -= 3
           inimigo.hp_atual -= dano
           print(f"{jogador.nome} usa a magia de trovões em {inimigo.nome} e causa {dano} de dano !!")
           if inimigo.hp_atual <= 0:
               EndOfGame.deathofenemy()
           else:
             inimigo.atacar(jogador)
             if jogador.hp_atual <= 0:
               EndOfGame.death()
           break
      def raioroxo(inimigo):
        dano = random.randint(1,12) 
        while True:
         if flower.flower_atual ==0 or flower.flower_atual <3:
           print("Flores insuficientes")
           break
         else:
           flower.flower_atual -= 3
           inimigo.hp_atual -= dano
           print(f"{jogador.nome} chama dos céus a magia de raios roxos e usa em {inimigo.nome} e causa {dano} de dano !!")
           if inimigo.hp_atual <= 0:
               EndOfGame.deathofenemy()
           else:
             inimigo.atacar(jogador)
             if jogador.hp_atual <= 0:
                EndOfGame.death()
           break
      def chuvaacida(inimigo):
        dano = random.randint(1,35)
        while True:
         if flower.flower_atual ==0 or flower.flower_atual <5:
           print("Flores insuficientes")
           break
         else:
           flower.flower_atual -= 5
           inimigo.hp_atual -= dano 
           print(f"{jogador.nome} usa uma magia bem perigosa, podendo atingir a si mesmo, a chamada chuva de ácido. Usa em {inimigo.nome} e causa {dano} de dano !!")
           if inimigo.hp_atual <= 0:
               EndOfGame.deathofenemy()
           else:
             inimigo.atacar(jogador)
             if jogador.hp_atual <= 0:
                EndOfGame.death()
           break
    class Combate:
     def __init__():
      while jogador.hp_atual > 0 and inimigo.hp_atual > 0:
        print("")
        print(f"{jogador.nome}: HP = {jogador.hp_atual}/{jogador.hp_maximo}")
        print(f"{inimigo.nome}: HP = {inimigo.hp_atual}/{inimigo.hp_maximo}")
        print(f"flores: {flower.flower_atual}/{flower.flower_max}")
        print("O que você quer fazer?")
        print("1. Atacar")
        print("2. Usar Magias")
        print("3. curar-se")
        escolha = input("> ")
        print("")
       #menu de ataque
        if escolha == "1":
          print("\n" * 55)
          jogador.atacar(inimigo)
       #magias      
        elif escolha == "2":
         while True:
          print("\n" * 55)
          print("")
          print(f"{jogador.nome}: HP = {jogador.hp_atual}/{jogador.hp_maximo}")
          print(f"{inimigo.nome}: HP = {inimigo.hp_atual}/{inimigo.hp_maximo}")
          print(f"flores: {flower.flower_atual}/{flower.flower_max}")
          print("escolha sua magia")
          if magic == "1":
            print("")
            print("1 - bola de fogo (custo: 4 flores)\n2 - raio roxo (custo: 3 flores)\n3 - trovoadas (custo: 3 flores) \n4 - voltar")
            escolha3x1 = input(">")
            print("")
            if escolha3x1 == "1":
               print("\n" * 55)
               Magia.boladefogo(inimigo)
               break
            elif escolha3x1 == "2":
               print("\n" * 55)
               Magia.raioroxo(inimigo)
               break
            elif escolha3x1 == "3":
               print("\n" * 55)
               Magia.trovoadas(inimigo)
               break
            elif escolha3x1 == "4":
               print("\n" * 55)
               break
            else:
             print("\n" * 55)
             print("Escolha inválida. Tente novamente.")
          elif magic == "2":
            print("")
            print("1 - trovoadas (custo: 3 flores)\n2 - raio roxo (custo: 3 flores)\n3 - chuva ácida (custo: 5 flores)\n4 - voltar")
            escolha3x2 = input(">")
            print("")
            if escolha3x2 == "1":
               print("\n" * 55)
               Magia.trovoadas(inimigo)
               break
            elif escolha3x2 == "2":
               print("\n" * 55)
               Magia.raioroxo(inimigo)
               break
            elif escolha3x2 == "3":
               print("\n" * 55)
               Magia.chuvaacida(inimigo)
               break
            elif escolha3x2 == "4":
               print("\n" * 55)
               break
            else:
              print("\n" * 55)
              print("Escolha inválida. Tente novamente.")
          elif magic == "3":
            print("")
            print("1 - bola de fogo (custo: 4 flores) \n2 - chuva ácida  (custo: 5 flores)\n3 - raio roxo (custo: 3 flores)\n4 - voltar")
            escolha3x3 = input(">")
            print("")
            if escolha3x3 == "1":
              print("\n" * 55)
              Magia.boladefogo(inimigo)
              break
            elif escolha3x3 == "2":
              print("\n" * 55)
              Magia.chuvaacida(inimigo)
              break
            elif escolha3x3 == "3":
              print("\n" * 55)
              Magia.raioroxo(inimigo)
              break
            elif escolha3x3 == "4":
              print("\n" * 55)
              break
            else:
              print("\n" * 55)
              print("Escolha inválida. Tente novamente.")
      #curas
        elif escolha == "3":
          while True:
            print("\n" * 55)
            print("")
            print(f"{jogador.nome}: HP = {jogador.hp_atual}/{jogador.hp_maximo}")
            print(f"{inimigo.nome}: HP = {inimigo.hp_atual}/{inimigo.hp_maximo}")
            print(f"flores: {flower.flower_atual}/{flower.flower_max}")
            print("escolha a cura que deseja utilizar")
            print("1 - cogumelo (custo: 3 flores)\n2 - erva (custo: 5 flores)\n3 - voltar")
            escolha4 = input(">")
            print("")
            if escolha4 == "1":
              print("\n" * 55)
              Curas.cogumelo(jogador)
              break
            elif escolha4 == "2":
              print("\n" * 55)
              Curas.erva(jogador)
              break
            elif escolha4 == "3":
              print("\n" * 55)
              break
            else:
               print("\n" * 55)
               print("Escolha inválida. Tente novamente.")
        else:
         print("\n" * 55)
         print("Escolha inválida. Tente novamente.")
    class EndOfGame:
     def death():
      d1 = "você morreu...\nobrigado por jogar!!\n\n"
      print("")
      for letter in d1:
        print(letter, end='', flush=True)
        sleep(0.001)
      print("")
      sleep(3)
     def deathofenemy():
      d2 = f"O {inimigo.nome} foi derrotado\nobrigado por jogar!!\n"
      for letter in d2:
        print(letter, end='', flush=True)
        sleep(0.001)
      sleep(3)
      print("")

    print("\nescolha o nome de seu inimigo:")
    print("")
    print("[1] Eu mesmo digito")
    print("[2] Lucas")
    print("[3] Gabriel")
    print("[4] Pedro")
    print("[5] Enzo")
    print("[6] Gêvane")
    print("[7] Stálio")
    print ("")
    escolhanome = input(">")
    if escolhanome == "1":
      escolhanome2 = input("então digite o nome: \n")
    elif escolhanome == "2":
      escolhanome2 = "Lucas"
    elif escolhanome == "3":
      escolhanome2 = "Gabriel"
    elif escolhanome == "4":
      escolhanome2 = "Pedro"
    elif escolhanome == "5":
      escolhanome2 = "Enzo"
    elif escolhanome == "6":
      escolhanome2 = "Gêvane"
    elif escolhanome == "7":
      escolhanome2 = "Stálio"
    else:
      print("Escolha inválida. Tente novamente.")
    
    if d == "1":
      flower = Flowers(25)
    if d == "2":
      flower = Flowers(35)
    if d == "3":
      flower = Flowers(65)
    jogador = Jogador(name, rlifeplayer)
    inimigo = Inimigo(escolhanome2, rlifeenemy)

    print(f"\nO {inimigo.nome} apareceu!")
    sleep(1)
    print("Use sua melhor estratégia para vencer...")
    sleep(3)
    Combate.__init__()

# testing endings
  if (selec == '5'):
    print()
    print('this is just a test')
    money = money - 5000
    
    # Após o fim do jogo
    print("Você deseja outro jogo?")
    coin = input("y/n? ")
    print('/' * 30)
    print()
    if (coin == "y"):
      continue
    if coin == 'n':
      break
    else:
      print('Não é essa tecla')

# RPG da Livia 
  if (selec == 'rpg'):
    #BOAS VINDAS
    print('=' * 40)
    print()
    time.sleep(1)
    print(
      Fore.BLUE, '''
     ██▓███   ██▀███   ██▓███    ▄████ 
    ▓██░  ██▒▓██ ▒ ██▒▓██░  ██▒ ██▒ ▀█▒
    ▓██░ ██▓▒▓██ ░▄█ ▒▓██░ ██▓▒▒██░▄▄▄░
    ▒██▄█▓▒ ▒▒██▀▀█▄  ▒██▄█▓▒ ▒░▓█  ██▓
    ▒██▒ ░  ░░██▓ ▒██▒▒██▒ ░  ░░▒▓███▀▒
    ▒▓▒░ ░  ░░ ▒▓ ░▒▓░▒▓▒░ ░  ░ ░▒   ▒ 
    ░▒ ░       ░▒ ░ ▒░░▒ ░       ░   ░ 
    ░░         ░░   ░ ░░       ░ ░   ░ 
                ░                    ░ 
                                       
    ▄▄ ▄▄ ▄▄ ▄▄ ░░▄▀ ░░▄▀ ▄▄ ▄▄ ▄▄ ▄▄
    ░░ ░░ ░░ ░░ ▄▀░░ ▄▀░░ ░░ ░░ ░░ ░░
    ''')
    time.sleep(1)
    print('Bem vindo à versão 0.0.12 ALPHA de PRGP!')
    time.sleep(2)
    print(Fore.WHITE)
    print('Seja bem vindo,', name, '!')
    
    # JANELA DE STATUS DO name --------------------------------------
    lvl = 1
    exp = 0
    mexp = 10
    life = 10
    mlife = 10
    atk = 1
    crit = 3
    spd = 10
    deff = 1
    luck = 10
    gold = 0
    
    inv = ['potion', 'potion']
    head = []
  
    # ITENS -----------------------------------------------------------
    
    potion = 3
    
    vbastão = 3
    bastão = atk + 3
    
    v_armadura_de_couro = 2
    armadura_de_couro = deff + 2
    
    # INTRODUÇÃO (cena 1) -------------------------------------------------------
    
    print('Olá,', name,'! Seja muito bem-vindo ao PRPG- um jogo sem nome e sem sentido!')
    #print('Você irá aprender o básico do jogo a medida que for jogando, não é como se fosse difícil de qualquer forma ')
    print()
    input('pressione ENTER para continuar: ')
    print()
    print('='*100)
    
    print('É mais um dia na vida de', name, ''', um desempregado vagabundo.
    
    A vida era difícil na vila Pisca, você não trabalhava, ams ainda assim ela era pequena demais para suas grandes ambições.
    
    Um dia, você decide que vai sair da cidade para procurar um emprego digno de um grande corno que nem você. Daí começa a sua aventura.
    ''')
    input('pressione ENTER para continuar: ')
    print()
    
    
    
    print(Fore.LIGHTBLUE_EX)
    print('STATUS de: ', name)
    print('-'*16)
    print('- race = caramelo dogo')
    print('- lvl = ', lvl)
    print('- exp = ', exp, '/', mexp)
    print('- life = ', life, '/', mlife)
    print('- atk = ', atk)
    print('- def = ', deff)
    print('- crit = ', crit)
    print('- spd = ', spd)
    print('- luck = ', luck)
    print('')
    print('INVENTÁRIO:')
    print('-'*7)
    print('gold =', gold)
    print(*inv, sep="\n")
    print(Fore.WHITE)
    
    print()
    print('='*40)
    print()
    time.sleep(2)
    
    # CENA 2 --------------------------------------------------
    
    print(
      '''É um belo dia lá fora. Pássaros cantando e flores desabroxando. Em um dia como esse você encontra DOGUINHO, ele está interrompendo a passagem na ponte. Você tenta passar, mas ele bloqueia sua passagem.
    
    Ele insiste que você deve pagar o pedágio de 10 gold para passar.
    
    Você tem as seguintes opções:
    
        [1] = Pagar o pedágio
        [2] = Lutar
        [3] = Ir embora
    ''')
    time.sleep(2)
    
    while True:
      r = int(input('O que você vai fazer?: '))
      print(Fore.LIGHTYELLOW_EX)
      time.sleep(2)
      if (r != 1) and (r != 2) and (r != 3):
        print('Resposta inválida!')
      if r == 1:
        break
      if r == 2:
        break
      if r == 2:
        break
    print(Fore.WHITE)
    
    if (r == 1):
      print('Você procura por dinheiro em seus bolsos')
      print()
      time.sleep(2)
      if gold < 10:
        print(
          'Você lembra que não tem nenhum dinheiro. DOGUINHO se irrita e te arrasta para a batalha.'
        )
        r = 2
        print()
      if (gold >= 10):
        gold = gold - 10
        print(
          'Você pagou o pedágio. Doguinho te deixa passar a ponte tranquilamente')
        time.sleep(2)
        print()
        print('Você tem', gold, 'de gold restantes')
        time.sleep(2)
    
    if r == 3:
      print('''Você simplesmente vai embora.
      
      Você ouve risadas ao fundo.''')
    
    if r == 2:
      print('Você não vai se acovardar por um mero cachorro, você decide lutar!')
      time.sleep(2)
      print()
      print('=' * 40)
      print()
    
      #STATUS DE DOGUINHO------------------------------------------------
    
      named = 'DOGUINHO'
      lvld = 10
      lifed = 15
      atkd = 2
      critd = 5
      spdd = 7
      luckd = 15
      goldd = 10
    
      print('STATUS de: ', named)
      print('-' * 16)
      print('- lvl = ', lvld)
      print('- life = ', lifed)
      #print('- atk = ', atkd)
      #print('- crit = ', critd)
      #print('- spd = ', spdd)
      #print('- luck = ', luckd)
      print('=' * 16)
      print('')
    
      while lifed > 0:
        print('''Você tem as seguintes opções:
        
        [1] Habilidades
        [2] Checar STATUS
        [3] Analisar DOGUINHO
        [4] Fugir''')
    
        print('')
        r = int(input('O que você vai fazer?: '))
        time.sleep(1)
        print()
        print('=' * 16)
        print()
        if spdd > spd:
          print(Fore.RED)
          danod = randint(0, luckd)
          if danod == luckd:
            catkd = atkd + critd
            print(Fore.RED, named, ' te acertou um dano crítico! Você sofreu, ',
                  catkd, 'de dano')
            life = life - catkd
            print('Você agora tem ', life, 'de vida')
    
          if danod == 0:
            print(named, ' errou o ataque!')
    
          if (danod != luckd) and (danod != 0):
            life = life - atkd
            print(Fore.RED, named, ' te atacou! Você sofreu ', atkd, 'de dano!')
            print()
            print('Você agora tem', life, 'de vida')
    
            print(Fore.WHITE, '=' * 16)
            print('')
            time.sleep(1)
    
        #cCHECAR STATUS------------------------------------------------------
        if r == 2:
          print('STATUS de: ', name)
          print('-' * 16)
          print('race = doguinho (caramelo)')
          print('- lvl =', lvl)
          print('- exp = ', exp, '/', mexp)
          print('- life = ', life, '/', mlife)
          print('- atk =', atk)
          print('- crit =', crit)
          print('- ' * 7)
          print('gold =', gold)
    
          print('')
          print('==' * 40)
          print('')
          time.sleep(2)
    
        #ANALISAR STATS DE DoGUINHO---------------------------------
        if r == 3:
          print('STATUS de: ', named)
          print('-' * 16)
          print('- lvl = ', lvld)
          print('- life = ', lifed)
          print('- atk = ', atkd)
          print('- crit = ', critd)
          print('- spd = ', spdd)
          print('- luck = ', luckd)
          print()
          print('=' * 16)
          print()
    
        #fugir---------------------------------------------------------------
    
        if r == 4:
          print('Você tem 1/10 chances de fugir. Tem certeza que deseja tentar?')
          s = input('y/n')
          if s == y:
            C = randint(0, 10)
            if C == 10:
              print('Você escapou com sucesso!')
              break
            else:
              print(
                'Você tentou escapar, mas DOGUINHO lhe pegou tentando fugir e vocês continuam a batalha'
              )
          else:
            print('batalha continua')
    
        #AÇÕES ----------------------------------------------------------------------
    
        if r == 1:
          print('''Habilidades:
        [1] Atacar
        [2] Defender
        [3] Inventário
        
          ''')
          r = int(input('''O que vai fazer?: '''))
          print()
    
          if r == 1:
            catk = randint(0, luck)
            if catk == luck:
              dano = atk + crit
              lifed = lifed - dano
              print('Dano crítico! Você infringiu ', dano, ' de dano!')
              
            if catk == 0:
              print('Você errou o ataque!')
              
            if (catk != luck) and (catk != 0):
              lifed = lifed - atk
              print('Você infringiu ', atk, 'de dano!')
      
            print()
            print('DOGUINHO tem agora ', lifed, 'de vida')
            print()
    
          if r == 2:
            deff = deff * 2
            print ('Você defendeu!')
        
          #SE GANHOU ----------------------
          if lifed <= 0:
            print('=' * 16)
            print()
            print('Você derrotou DOGUINHO')
            time.sleep(2)
    
            exp = exp + lvld
            if exp >= mexp:  
              lvl = lvl + 1
              exp = 0
              mexp = mexp * 2
              life = life + 3
              atk = atk + 2
              crit = crit + 2
              spd = spd + 2
              luck = luck + 1
              print()
              print('PARABENS! VOCÊ SUBIU DE NÍVEL!')
              print()
              print('Você agora é nível ', lvl, '!')
              time.sleep(2)
              print(Fore.LIGHTBLUE_EX)
              print('STATUS de: ', name)
              print('-' * 16)
              print('- lvl = ', lvl)
              print('- exp = ', exp, '/', mexp)
              print('- life = ', life, '/', mlife)
              print('- atk = ', atk)
              print('- crit = ', crit)
              print('- spd = ', spd)
              print('- luck = ', luck)
              print()
              print('INVENTÁRIO:')
              print('-' * 7)
              print('gold =', gold)
              print(*inv, sep="\n")
              print(Fore.WHITE)
              break
    
          #ATAQUE DO DOGUINHO-----------------------------------------------
          danod = randint(0, luckd)
          print(Fore.RED)
          if danod == luckd:
            catkd = (atkd + critd) - deff
            if catkd <= 0:
              catkd = 1
              life = life - catkd
            else:
              life = life - catkd
              
            print('DOGUINHO te acertou um dano crítico! Você sofreu, ', catkd, 'de dano')
            print()
            print('Você agora tem ', life, 'de vida')
    
          if danod == 0:
            print('DOGUINHO errou o ataque!')
    
          if (danod != luckd) and (danod != 0):
            atkd = atkd - deff
            if atkd <= 0:
              atkd = 1
            life = life - atkd
            
            print(named, ' te atacou! Você sofreu ', atkd, 'de dano!')
            print()
            print('Você agora tem', life, 'de vida')
    
          print()
          print(Fore.WHITE, '=' * 40)
          print()
    
        time.sleep(2)
    
        if life <= 0:
          print('Você foi derrotado!')
          time.sleep(2)
          print()
          print('Você é forçado a trabalhar para a Gangue dos Cachorros Capitalistas para todo o sempre! Ao menos agora você tem um emprego?...')
          exit('''
      ·▄▄▄▪  • ▌ ▄ ·.     ·▄▄▄▄  ▄▄▄ .     ▐▄▄▄       ▄▄ •       
      ▐▄▄·██ ·██ ▐███▪    ██▪ ██ ▀▄.▀·      ·██▪     ▐█ ▀ ▪▪     
      ██▪ ▐█·▐█ ▌▐▌▐█·    ▐█· ▐█▌▐▀▀▪▄    ▪▄ ██ ▄█▀▄ ▄█ ▀█▄ ▄█▀▄ 
      ██▌.▐█▌██ ██▌▐█▌    ██. ██ ▐█▄▄▌    ▐▌▐█▌▐█▌.▐▌▐█▄▪▐█▐█▌.▐▌
      ▀▀▀ ▀▀▀▀▀  █▪▀▀▀    ▀▀▀▀▀•  ▀▀▀      ▀▀▀• ▀█▄▀▪·▀▀▀▀  ▀█▄▀▪''')
          
# Colocar um jogo do bicho
if (money <= -1000):
  print('Agora você está devendo muito para o cassino, assim eles tem total propriedade sobre você')
  time.sleep(1)
  print('Eles te convidam para uma sala especial para pessoas como você')
  time.sleep(1)
  print('O benfício desses jogos é que você estará livre de dívidas')
  yakuza = input('Aceitas (y/n)?: ')
  if yakuza == 'y':
    print('...')
    time.sleep(3)
    print('Você entra no subsolo do cassino e vê várias pessoas desesperadas apostando com o dinheiro que elas não tem')
    time.sleep(1)
    print()
    print('O jogo escolhido para você é uma espécie de roleta russa')
    time.sleep(2)
    print()
    death = '1'
    if death == '1':
      print('Nesse jogo você joga contra alguém, e o dealer é quem revela as cartas, aquele que tem as cartas iguais ao dealer tem o direito a dar um tiro no outro e se livrar de sua dívida')
      time.sleep(3)
      print()
      lists = ["O", "+", "~~~", "[]", "*"]
      cards = ["O", "+", "~~~", "[]", "*"]
      a = ("O")
      b = ("+")
      c = ("~~~")
      d = ("[]")
      e = ("*")
      
      print('Primeiro, vocês pegam um revolver e recarrega ele')
      time.sleep(2)
      bullets = int(input('Quantas balas você deseja colocar no revolver: '))
      match = random.randint(1,6)
      print()
      print('Depois, vocês deixam todo o resto para a sorte')
      
      while True:
        print('''Essas são as suas cartas de 
      
a, b, c, d, e''')
        print (a, b, c, d, e)
        print()
        # lista do jogador
        my_list = []
        while True:
          x = input('Qual a sua primeira carta?: ')
          if x == '':
            print('Você não pode escolher nada')
            continue
          if x == 'a':
            my_list.append(a)
          elif x == 'b':
            my_list.append(b)
          elif x == 'c':
            my_list.append(c)
          elif x == 'd':
            my_list.append(d)
          elif x == 'e':
            my_list.append(e)
          break
        
        print()
        while True:
          y = input('Qual a sua segunda carta?: ')
          if x in y:
              print('Esse input já foi usado')
              continue
          if x != y:
            if y == 'a':
              my_list.append(a)
            elif y == 'b':
              my_list.append(b)
            elif y == 'c':
              my_list.append(c)
            elif y == 'd':
              my_list.append(d)
            elif y == 'e':
              my_list.append(e)
            break
            
        print()
        while True:    
          z = input('Qual a sua terceira carta?: ')
          if (y in z) or (x in z):
              print('Esse input já foi usado') 
              continue
          if z != y:
            if z == 'a':
              my_list.append(a)
            elif z == 'b':
              my_list.append(b)
            elif z == 'c':
              my_list.append(c)
            elif z == 'd':
              my_list.append(d)
            elif z == 'e':
              my_list.append(e)
            break
            
        print()
        while True:    
          q = input('Qual a sua quarta carta?: ')
          if (z in q) or (y in q) or (x in q):
              print('Esse input já foi usado')
              continue
          if q != z:
            if q == 'a':
              my_list.append(a)
            elif q == 'b':
              my_list.append(b)
            elif q == 'c':
              my_list.append(c)
            elif q == 'd':
              my_list.append(d)
            elif q == 'e':
              my_list.append(e)
            break
            
        print()
        while True:
          w = input('Qual a sua última carta?: ')
          if (q in w) or (z in w) or (y in w) or (x in w):
              print('Esse input já foi usado')
              continue
          if w != q:
            if w == 'a':
              my_list.append(a)
            elif w == 'b':
              my_list.append(b)
            elif w == 'c':
              my_list.append(c)
            elif w == 'd':
              my_list.append(d)
            elif w == 'e':
              my_list.append(e)
            break
            
        print()
        
        # Lista do Jogador
        print('Essas são as cartas que você escolheu')
        print(my_list)
        print()
        
        # Lista do dealer
        print('Essa são as cartas do dealer')
        random.shuffle(lists)
        print(lists)
        print()
        
        # As cartas iguais do dealer e do jogador, já que é o que importa
        print('As cartas iguais entre você e o dealer são:')
        print([x for x, y in zip(my_list, lists) if x==y])
        print()
        
        # Lista do oponente
        print('Essa são as cartas do seu oponente')
        random.shuffle(cards)
        print(cards)
        print()
        print()
        
        # As cartas iguais do dealer e do oponente, já que é o que importa
        print('As cartas iguais entre o seu oponente e o dealer são:')
        print([x for x, y in zip(cards, lists) if x==y])
        print()
        
        # Suas cartas sejam iguais com as do dealer
        k = list(zip(my_list, lists))
        # As cartas do oponente sejam iguais com as do dealer
        l = list(zip(cards, lists))
      
        time.sleep(2)
      
        
        # Caso suas cartas sejam iguais com as do dealer
        if k > l:
          if (bullets == range(1,6)) or (bullets == 6):
            print('Você atira nele')
            time.sleep(2)
            print('Ele morre')
            time.sleep(3)
            print()
            print('Parabéns, agora você está livre de qualquer dívida com o cassino')
            money = money * 0
            break
          else:
            print('O revolver não dispara')
            time.sleep(2)
            print('Ninguém morre')
            continue
        # Caso vocês dois tenham o mesmo número de cartas
        elif k == l:
          if ((bullets == range(1,5)) or (bullets == 6)) and (match == range(1,6)):
            print('Vocês dois se atiram ao mesmo tempo')
            time.sleep(1)
            print('Vocês morrem')
            break
          elif x == 1 and y == 1:
            print('Os revolveres não disparam')
            time.sleep(2)
            print('Ninguém morre')
            continue
          elif (bullets == range(1,5)) or (bullets == 6):
            print('Você atira nele')
            time.sleep(2)
            print('Ele morre')
            time.sleep(3)
            print()
            print('Parabens, agora você está livre de qualquer dívida com o cassino')
            money = money * 0
            break
          elif (match == range(1,5)) or (match == 6):
            print('Ele atira em você')
            time.sleep(1)
            print('Você morre')
            break
        # Caso ele tenham o número maior de cartas iguais com a do dealer
        elif k < l:
          if (match == range(1,5)) or (match == 6):
            print('Ele atira em você')
            time.sleep(1)
            print('Você morre')
            break
          else:
            print('O revolver não dispara')
            time.sleep(2)
            print('Ninguém morre')
            continue
        print()
        time.sleep(5)
          
  if yakuza == 'n':
    print('Você saí do cassino, mas você ainda continua com essas dívidas')
    
# Pedindo mais dinheiro
if (money <= -100) or (yakuza == 'n'):
  print("Você está sem dinheiro")
  print()
  print("Deseja chamar alguém para pedir dinheiro?")
  help = input("y/n: ")
  print()
  
  # - Sem nenhuma ajuda
  # - Você engole o choro e faz o L
  if (help == "n"):
    print("Você volta para casa refletindo o que fez, e decide comer o miojo guardado na geladeira")
    
  if (help == "y"):
    print("""Suas opções são:

[1] O banco
[2] O agiota
[3] A família""")
    print()
    venom = input("Qual a sua escolha?: ")
    # O empréstimo do banco
    if (venom == "1"):
      print("Você decide ligar para o banco")
      print()
      credit = random.randint(0,1000)
      print('Você tem', credit, 'de score no Serasa')
      time.sleep(3)
      print()
      if (credit < 501):
        print('O banco nem olha para sua proposta, por causa do seu crédito quase inexistente')
        print()
        while True:
          print('Deseja ligar para o agiota')
          option = input('y/n: ')
          if (option == "y"):
            break
          if (option == 'n'):
            break
          else:
            print('Não é essa tecla')
        print()
      if (701 > credit > 501):
        print('O banco lhe propõe um empréstimo de 1000 reais')
        print()
        print("Você aceita?")
        x = input("y/n: ")
        print()
        if (x == 'y'):
          loan = 1000
          print('Você só tem R$', loan)
          option = 'n'
        if x == 'n':
          print('Você continua pobre')
          time.sleep(2)
          print()
          print('Deseja ligar para o agiota')
          option = input('y/n: ')
        else:
          print('Não é essa tecla')
      if (credit >= 701):
        print('Você negocia um empréstimo de 3000 reais')
        loan = 3000
        print()
        print('Deseja voltar a jogar?')
        y = input('y/n: ')
        # I need to find a solution to replay all games
        if (y == 'n'):
          option = 'n'
      if (credit == 1000):
        print('Você consegue convencer eles a darem um empréstimo de 20000 reais, com a desculpa que é para a entrada de uma casa')
        loan = 20000
      print()
      
      # - Por causa no Banco
      # 1 - Com a sua sorte interminável, você pega todo o seu dinheiro e vai morar numa ilha privada com tudo do bom e do melhor
      if (money >= 5000) and (credit >= 701):
        print('Você decide pegar todo esse dinheiro e gastar com coisas caras, assim ficando pobre novamente e querendo apostar de novo')
      # 2 - Você pega o dinheiro do empréstimo e vai continuar a sua vida em paz
      elif (loan >= 100) and (option == 'n'):
        print('Você decide pegar o dinheiro do empréstimo do banco e continuar com a sua vida')
    
    # O empréstimo do agiota
    if (venom == "2" or option == 'y'):
      print("Você decide ligar para ele")
      print()
      time.sleep(3)
      luck = random.randint(0,1)
      if (luck == 0):
        print("Você liga para ele, mas você tem o asar de ele estar sendo procurado pela polícia e você ser redirecionado para um informante da polícia que estava procurando ele faz 3 semanas")
        time.sleep(1)
        print()
        loan_shark = 0
        print('Você sai sem dinheiro, além disso você agora é procurado pela polícia')
        time.sleep(2)
        print()
      if (luck == 1):
        print("Você liga para ele, mas ele te dá um empréstimo de R$ 1000 com um prazo para entregar amanhâ, com 300% de juros a hora")
        loan_shark = 1000
      if (luck == 2):
        print('Você liga para ele, ele te dá um empréstimo com 50% de juros ao mês')
        print()
        loan_shark = random.randint(1000, 3000)
        print('Ele te empresta R$', loan_shark)
      if (luck == 3):
        print("Você liga para ele, e hoje ele tá de bom humor, assim ele te dá um empréstimo de R$ 5000, cobrando 10x com juros")
        loan_shark = 5000
      print()
      # - Por causa do agiota
      # 1 - Você vai preso pela polícia por um crime que você não cometeu e você perde tudo
      if (luck == 0):
        print('Você vai preso pela polícia, mas como o sistema judiciário desse país é falho, você fica preso por 10 anos por um crime que você nem cometeu')
    # 2 - Você fica com o dinheiro do empréstimo e decide fugir
      elif (luck == 1 or 2 or 3 ) and (loan_shark >= 1000):
        print("Como você não tem dinheiro para pagar o agiota, você pega todo o seu dinheiro e foge do estado onde você mora")

    if (venom == "3"):
      print("Você decide ligar para  eles")
      relation = random.randint(0,1)
      if (relation == 0):
        print ("Você liga para a sua família")
        print("...")
        time.sleep(3)
        print()
        print("Mas ninguém responde")
      if relation == 1:
        print ("Você liga para a sua família")
        print("...")
        time.sleep(3)
        print()
        print('Alguém responde')
        print()
        print('Alô?')
        time.sleep(1)
        print('Quem fala?')
        print('...')
        time.sleep(1)
        print('É a sua mãe')
        print()
        decision = input('Você deseja colocar esse peso nas costas da sua dela (y/n)?: ')
        if decision == 'y':
          print('Oi mãe')
          time.sleep(1)
          print('Eu queria perguntar se a senhora poderia me dar um pouco de dinheiro para pagar as contas daqui de casa')
          print()
          print('De novo?')
          time.sleep(2)
          print('Tudo bem, se o meu filho estiver realmente precisando então eu darei esse dinheiro para você')
          time.sleep(1)
          print('Pois eu sei que você vai fazer a coisa certa')
          donation = 500
          print()
          print('Você respeita a confiança da sua mãe e decide pagar todas as suas contas e comprar algo legal para a sua mãe')
        if decision == 'n':
          print('Oi mãe')
          time.sleep(1)
          print('Eu só queria saber como a senhora está, afinal faz tanto tempo que a gente não conversa')
          print()
          time.sleep(1)
          print('Eu estou bem', name, ',eu também queria saber como você estava')
          print()
          print('Eu estou bem mãe')
          time.sleep(2)
          print('Eu tenho que ir mãe, amanhã eu irei visitar a senhora')
          print()
          time.sleep(1)
          print('Tudo bem, a mãe te ama muito')
          print()
          time.sleep(1)
          print('Eu também te amo mãe')
          print()
          time.sleep(1)
          print('Chamada acabada')
          print()
          print('Você sente que foi a coisa certa a se fazer, agora você decide resolver a sua vida, então você larga essa vida de apostas e decide trabalhar num supermercado como operador de caixa')         

fimx1 = "Fim do nosso jogo..."
for letter in fimx1:
        print(letter, end='', flush=True)
        sleep(0.001)
print("")
sleep(2)
fimx2 = "Obrigado pela atenção e por chegar até aqui."
for letter in fimx2:
        print(letter, end='', flush=True)
        sleep(0.001)
print("")
sleep(2)