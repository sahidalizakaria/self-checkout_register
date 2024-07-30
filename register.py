catalogue = {
"Notebook": 70,
"Pen": 50,
"Pencil": 30,
"Eraser": 20
}

def length(dictionary):
	measure = max(len((x)) for x in dictionary)
	return measure
padding = 2

numbered_catalogue = {}
for n, (k, v) in enumerate(catalogue.items()):
    numbered_catalogue.update({str(n+1):[k,v]})

space0 = []
space_0 = length(numbered_catalogue) + padding
space0.append(space_0)

number_header_len = len('No.')
if space0[0] <= number_header_len:
	space0[0] = number_header_len + 1

space1 = []
space_1 = length(catalogue) + padding
space1.append(space_1)

product_header_len = len('Product')
if space1[0] <= product_header_len:
	space1[0] = product_header_len + 1

print(f"{'No.':{space0[0]}}{'Product':{space1[0]}}Price")
for key, value in numbered_catalogue.items():
	number = "{0:{space}}".format(key, space=space0[0])
	product = "{0:{space}}".format(value[0], space=space1[0])
	price = "{0:0}".format(value[1])
	print(number + product + price)


catalogue_list = list(catalogue.keys())

bought = {}
bought2 = {}
def buy_product(pro, count):
	pro1 = catalogue_list[pro-1]
	pro2 = catalogue[pro1]
	multiply = pro2*count
	buy_result = f"{pro1} x{count} = {multiply}"
	print(buy_result)
	bought_update = {f"{pro1}":[count, multiply]}
	if pro1 in bought:
		bought2.update(bought_update)
	else:
		bought.update(bought_update)
	return multiply

def count_input():
	while True:
		try:
			b = int(input("The product count: "))
			return b
			break
		except ValueError:
			print('Enter numerical value.')

def buy_product2():
	while True:
		try:
			print('\n')
			a = int(input("Product number: "))
			catalogue_list[a-1]
		except ValueError:
			print('Enter numerical value.')
		except IndexError:
			print('No products with such number')
		else:
			b = count_input()
			buy_product(a, b)
			while True:
				done = (lambda one: one.lower()) (input("Are you done (y/n)? "))
				if done == "y":
					break
				elif done == "n":
					buy_product2()
					break
				else:
					print('Enter "y" or "n".')
			break				
							
while True:
	buy_product2()
	break

for key, value in bought2.items():
	if key in bought:
		bv = bought[key]
		cc = value[0] + bv[0]
		pp = value[1] + bv[1]
		bought.update({f"{key}":[cc, pp]})

space2 =[]
space_2 = length(bought) + padding
space2.append(space_2)

if space2[0] <= product_header_len:
	space2[0] = product_header_len + 1


bought_cp_list = list(bought.values())
bought_count_list = [str(x[0]) for x in bought_cp_list]

space3 = length(bought_count_list) + padding

count_header_len = len('Count')
if space3 <= count_header_len:
	space3 = count_header_len + 1

print(f"\n{'Product':{space2[0]}}{'Count':{space3}}{'Price':0}")
for key, value in bought.items():
	product = "{0:{space}}".format(key, space=space2[0])
	count2 = "{0:{space}}".format(str(value[0]), space=space3)
	price = "{0:0}".format(value[1])
	print(product + count2 + price)

def total(prices):
	totalling = sum(prices)
	return totalling

bought_price_list = [x[1] for x in bought_cp_list]

total = total(bought_price_list)

bought_price_list_str = [str(x[1]) for x in bought_cp_list]

space_total = space2[0] + space3

space_bpl = length(bought_price_list_str)

space_underscore = space_total + space_bpl

for i in range(space_underscore):
	print("-", end="")
print("+")
print(f"{'Total:':{space_total}}{total}\n")


#calculate the discount
def discount(percent):
	result = total - (total * percent)
	return result

discount_notice = "Do you want to find out if you're eligible for a discount? To determine your eligibility, we will ask you about your age & student status. By entering 'y', you agree to our Privacy Policy. (y/n): "
print('\n')

discount_opt = (input(discount_notice)).lower()

while discount_opt != "y" and discount_opt != "n":
	print('Enter "y" or "n".')
	discount_opt = (input(discount_notice)).lower()
		
if discount_opt == "y":
	#require integer as input for age
	while True:
		try:
			age = int(input("Age: "))
			break
		except ValueError:
			print('Enter whole number/s.')

	#ask student status
	is_student = (input("Are you a student? (y/n): ")).lower()
	
#require "yes" or "no" as input for the student status
	while is_student != "y" and is_student != "n":
		print('Enter "y" or "n".')
		is_student = (input("Are you a student? (y/n): ")).lower()
	if age < 18:
		if is_student == "y":
			discount_info = "20%"
			discounted = discount(0.2)
		else:
			discount_info = "10%"
			discounted = discount(0.1)
	elif age >= 75:
		discount_info = "5%"
		discounted = discount(0.05)
	else:
		discount_info = "-"
		discounted = total
else:
	discount_info = "-"
	discounted = total

print(f"{'Discount:':{space_total}}{discount_info}")

print(f"{'Pay:':{space_total}}{discounted}")

#continue the transaction
print("\n" + "Proceed to payment")

while True:
	try:
		money = int(input(f"{'Your money:':{space_total}}"))
		break
	except ValueError:
		print('Enter whole number/s.')

print(f"{'Change:':{space_total}}{money - discounted}")

print("\n" + "Thank you for your purchase!")