product = {
    "supplier_age" : 4,
    "product_category_age" : 2,
    "units_sold" : 300,
    "current_discount": 15,
    "units_sold_after_discount" : 100,
    "remove_product" : False
}
def getDiscount(obj):
    discount = -1
    if(obj['supplier_age'] <=2):
        discount = 45
    elif(obj['product_category_age'] <=1):
        discount = 45
    elif(obj['units_sold'] > 500):
        discount = 0
    elif(obj['units_sold'] > 200):
        discount = 15
    elif(obj['current_discount'] != 35):
        discount = 35
    elif(obj['units_sold_after_discount'] < 200):
        obj['remove_product'] = True
        discount = 'NA'
    else:
        discount = 'NA'
    return discount

print(getDiscount(product))