'''
割り勘アプリ
「合計金額を教えてね(円):」入力を受け取る
「人数を教えてね(人):」入力を受け取る
1人あたり金額を返す
端数を返す

'''


amount = int(input('合計金額を教えてね(円):'))
number_of_person = int(input('人数を教えてね(人):'))

print(f'一人あたり:{amount // number_of_person}, 端数:{amount % number_of_person}')