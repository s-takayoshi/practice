'''
例→
$ python bmi.py
Height(m)? > 170
Weight(kg)? > 60
Your BMI is 20.76
'''

height = int(input('あなたの身長は?(cm)＞')) / 100
weight = int(input('あなたの体重は?(kg)＞'))

bmi = weight / (height ** 2)
print(f'{bmi:.2f}')