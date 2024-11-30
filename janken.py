print('じゃんけんスタート')
print('自分の手を入力してください')

my_hand = 1
enemy_hand =0

if my_hand == 0:
  if enemy_hand == 0:
    print('あいこ')
  elif enemy_hand == 1:
    print('勝ち')
  elif enemy_hand == 2:
    print('負け')
elif my_hand == 1:
  if enemy_hand == 0:
    print('負け')
