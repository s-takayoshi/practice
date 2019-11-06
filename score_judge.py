'''
下記のようなCLIアプリケーションを作ってください
入力された試験の点数に基づき、成績の判定するアプリケーションです
成績の判定条件
80点以上 => A
60点以上 => B
40点以上 => C
40点未満 => F
'''


score = int(input('点数は？＞'))

if 80 <=  score < 100:
    print('判定: A')

elif 60 <= score < 80:
    print('判定: B')

elif 40 <= score < 60:
    print('判定: C')

elif 0 <= score < 40:
    print('判定: F')

else:
    print('警告!「0 〜 100」の数値を入力してください')