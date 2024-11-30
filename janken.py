print('じゃんけんスタート')
print('自分の手を入力してください')

my_hand = 0
enemy_hand = 2

if my_hand == 0:
  if enemy_hand == 0:
    print('あいこ')
  elif enemy_hand == 1:
    print('勝ち')
  elif enemy_hand == 2:
    print('負け')
