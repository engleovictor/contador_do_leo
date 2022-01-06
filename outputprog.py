import objandfuncs as lib

produtos = lib.carregar_dados()[0]

for x in produtos:
    print(f'REFERÊNCIA: {x.ref}')
    print('COR - TAMANHOS:    1     2     3     4     5     6')
    for y in x.dat:
        print(f"{y['cor']}            {y['1']:0>4}  {y['2']:0>4}  {y['3']:0>4}  {y['4']:0>4}  {y['5']:0>4}  {y['6']:0>4}")
    print()

input()