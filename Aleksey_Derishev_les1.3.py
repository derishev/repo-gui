stroka = input('Введито колличество процентов (1-100): ')
percent = int(stroka)
if percent == 1:
    print(percent, ' процент')

elif (percent > 1 and percent < 5):
    print(percent, ' процента')
elif percent > 5 and percent < 21:
    print(percent, ' процентов')
elif stroka[1] == '1':
    print(percent, ' процент')
elif stroka[1] == '2' or stroka[1] == '3' or stroka[1] == '4':
    print(percent, ' процента')

else:
      print(percent, ' процентов')
