import sys
def add_sale(cash):
    with open('bakery.csv', 'a', encoding='utf-8') as f:
        cash = str(cash + '\n')
        f.write(cash)

cash = str(sys.argv)

add_sale(cash)