import random
from datetime import date

def start_message():
  print(date.today())
  print('じゃんけんスタート')

def get_my_hand():
  print('自分の手を入力してください')
  return int(input('0:グー, 1:チョキ, 2:パー'))

def get_you_hand():
  return random.randint(0, 2)

def view_result(my_hand, enemy_hand):
  result = my_hand - enemy_hand
  if result == 0:
    print('あいこ')
  elif result == -1 or result == 2:
    print('勝ち')
  else:
    print('負け')

start_message()

my_hand = get_my_hand()
enemy_hand = get_you_hand()

view_result(my_hand, enemy_hand)
