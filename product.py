products = []

print('輸入q退出')
while True:
	name = input('請輸入商品名稱:')
	if name == 'q':
		break
	price = input('請輸入商品價格:')
	products.append([name, price])#product[p[name]p[price]]product中裝有兩個p[]
#print(products)

#print(products[0][0])#product[(大清單的0)p[(小清單的0)0]p[1], p[0]p[1]]
#印出第一個商品的名字

for p in products:
	print(p[0], '的價格是', p[1])

#'abc' + '123' = 'abc123'
#'abc' * 3 = 'abcabcabc'

with open('products.csv', 'w') as f:#寫入時可以不用有檔案,有的話會覆蓋掉
	f.write('商品,價格\n')
	for p in products:
		f.write(p[0] + ',' + p[1] + '\n')
