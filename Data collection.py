products = []
while True:
    selection = int(input("1.Add New Product\n2.Print Product Details"
                          "\n3.Buy Product"
                          "\n4.Delete Product"
                          "\n5.Exit"))
    if selection == 1:
        product_number = input("Enter Product Number :")
        product_name = input("Enter Product Name :")
        product_price = input("Enter Product Price :")
        product_qty =  int(input("Enter Product Quantity :"))
        product = {
            "id" : product_number,
            "name" : product_name,
            "price" : product_price,
            "qty" : product_qty
        }
        products.append(product)
        print("Product Added Successfully")
    elif selection == 2:
        product_number = input("Enter product number :")
        for i in products:
            if i['id'] == product_number:
                print(i)
                break
    elif selection == 3:
        product_number = input("Enter product number :")
        product_quantity = int(input("Inter Product Quantity: "))
        for i in products:
            if i['id'] == product_number:

                i['id']
                break
        final_price = product_price * product_quantity
        new_quantity = product_qty - product_quantity

    elif selection == 4:
        product_number = input("Enter product number :")
        for i in products:
            if i.get("id") == product_number:
                products.remove(i)
                break

    elif selection == 5:
        exit()
    else:
        print("Invalid Input")
