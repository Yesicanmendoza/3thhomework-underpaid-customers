def customer_payment(the_file):
    #Function that checks if  a customer overpaid or underpaid
    melon_cost = 1.0

    for line in the_file:
        line = line.rstrip()
        #Eliminate all the empty spaces at the right
        word = line.split('|')
        #Split every line by the "|" symbol

        cust_name = word[1]
        qty_melons = int(word[2])
        payment = float(word[3])

        customer_expected = qty_melons * melon_cost
        if customer_expected != payment:
            print(f"{cust_name} paid ${payment:.2f},",f"expected ${customer_expected:.2f}")


file = open("customer-orders.txt")

customer_payment(file)




