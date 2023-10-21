pro_price=int(input("Enter the price of product :"))
if pro_price > 3000:
    print("Your are getting 20% off on your product :")
    if pro_price == 5000:
        print("You geted a additional reward gao trip")
    print("After discount The price of product is {}".format(pro_price*0.2))
    
elif pro_price >= 2000 and pro_price <= 3000:
    print("Your are getting 30% off on your product :")
    print(f"After discount The price of product is {pro_price*0.7}")

else: 
     print("Your are getting 40% off on your product :")
     print(f"After discount The price of product is {pro_price*0.6}".format())

"""else:
    print("Your are getting 50% off on your product :")
    print("After discount the price of product is {} :".format(pro_price*0.5))"""
