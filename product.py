import os #作業系統

products = []

def read_file(filename):
	if os.path.isfile(filename):#檢查是否有檔案(怕沒檔案不能讀取)
		print('找到檔案了')
		#讀取檔案
		with open(filename, 'r') as f:
			for line in f:
				if '商品,價格' in line:
					continue#不執行9跟10,不會印出商品價格,continue(跳到下一回),break(中斷迴圈)
				name, price = line.strip().split(',')#去除換行split逗點當切割標準
				products.append([name, price])
	else:
		print('找不到檔案')
	return products

def user_input(products):
	#讓使用者輸入
	print('輸入q退出')
	while True:
		name = input('請輸入商品名稱:')
		if name == 'q':
			break
		price = input('請輸入商品價格:')
		products.append([name, price])#product[p[name]p[price]]product中裝有兩個p[]
	return products
#print(products)

#print(products[0][0])#product[(大清單的0)p[(小清單的0)0]p[1], p[0]p[1]]
#印出第一個商品的名字

def print_products(products):
	#印出商品跟價格
	for p in products:
		print(p[0], '的價格是', p[1])

#'abc' + '123' = 'abc123'
#'abc' * 3 = 'abcabcabc'

def write_file(filename, products):
	#寫入檔案
	with open(filename, 'w') as f:#寫入時可以不用有檔案,有的話會覆蓋掉
		f.write('商品,價格\n')
		for p in products:
			f.write(p[0] + ',' + p[1] + '\n')

print(read_file('products.csv'))
products = user_input(products)
print_products(products)
write_file('products.csv', products)
#設計函數時不要讓函數拿到不知道的東西