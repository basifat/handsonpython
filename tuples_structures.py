tp = 12345, 54321, 'hello!'
#print(tp)


def test(a):
    return [a,10,15,16]

x,y,z,b =test(5)
#print(x)
# print(y)
# print(z)

student = ("Tunde", 70)
student2 = ("Abel", 70)

# Dictionaries
dico = dict([
    student,
    student2
])


#print(dico)

banana = ("banana", 4)
apple = ("apple", 2)
orange = ("orange", 3)
pear = ("pear", 1)

stock= dict([
    banana,
    apple,
    orange,
    pear
])

prices = {"banana":6,"apple": 12, "orange":9,"pear": 15}
#print(stock)

total_quantity=0

# for fruit, qty in stock.items():
#     total_quantity = total_quantity + qty
# print(total_quantity)

#find total price of items when the stock quantity is greater than 2
#When stock quantity is greater than 2, subtract 1 from the stock quantity
#1. iterate through the stock dictionary
#2. find items with stock greater than 2
#3. get the prices for the items greater than 2
#4. sum the total price of all the items 

# stock_item = stock["banana"]
# stock_item -= 1
# stock["banana"] = stock_item


# banana = ("banana", 4)
# apple = ("apple", 2)
# orange = ("orange", 3)
# pear = ("pear", 1)

# print(stock)
# stock["mango"] = 90
# print(stock)
# furit_dico = {"mango": 90, "orange": 90}
# furit_dico["another_fruit"] = 1000
# furit_dico

#Big 0(n) = 
fruit_arr = [12, 14, 15, 18, 19, 90, 18]

fruit_dico = {"mango": 12, "apple": 14, "pear": 18}

print(fruit_dico["pear"])
# print(fruit_dico["berries"])

for number in fruit_arr:
    if number == 18:
        pass
        #do something



def get_items_total_price():
    total_price = 0
    for fruit, quantity in stock.items():
        if quantity > 2:
            stock[fruit] = stock[fruit]-1
            price=prices[fruit] 
            total_price = total_price + price
    return total_price, stock

item_total, updated_stock = get_items_total_price()
print(item_total, updated_stock)




university = [("abel",1), ("abel",1), ("abel",0), ("abel",1), ("abel",1), 
("tunde",1), ("tunde",1), ("tunde",1), ("tunde",1), ("tunde",1)]
# Find total attendance days for each student in our university
# output = [("abel", 4), ("tunde",5)]
#iterate though the university list of tuples

#university = ["tunde", "abel"", 1, 5, "tunde"]
student1_dico = {"tunde": 0, "abel": 0}
for student,record in university:
    print(student)
    print(record)
    student1_dico[student] = student1_dico[student] + record
print(student1_dico)

    


