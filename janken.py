import random
from datetime import date

def check_input(hand):
    if hand < 0 or hand > 2:
        print('0から2の間で入力してください')
        exit()
    return True

def hand_name(hand):
    return ['グー', 'チョキ', 'パー'][hand]

def start_message():
  print(date.today())
  print('じゃんけんスタート')

def get_my_hand():
  print('自分の手を入力してください')
  hand = int(input('0:グー, 1:チョキ, 2:パー'))
  check_input(hand)
  print('あなたの手は{}です'.format(hand_name(hand)))

  return hand

def get_you_hand():
  hand = random.randint(0, 2)
  print('相手の手は{}です'.format(hand_name(hand)))
  return hand

def view_result(my_hand, enemy_hand):
  result = my_hand - enemy_hand
  if result == 0:
    print('あいこ')
    play()
  elif result == -1 or result == 2:
    print('勝ち')
  else:
    print('負け')

def play():
  my_hand = get_my_hand()
  enemy_hand = get_you_hand()
  view_result(my_hand, enemy_hand)

start_message()
play()
