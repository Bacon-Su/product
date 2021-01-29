product = []

print('輸入q退出')
while True:
	name = input('請輸入商品名稱:')
	if name == 'q':
		break
	price = input('請輸入商品價格:')
	product.append([name, price])#product[p[name]p[price]]product中裝有兩個p[]
print(product)

print(product[0][0])#product[(大清單的0)p[(小清單的0)0]p[1], p[0]p[1]]
#印出第一個商品的名字

for p in product:
	print(p)
