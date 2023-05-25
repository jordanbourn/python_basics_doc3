shopping_cart = True
cart = ['eggs', 'peanut butter', 'apples', 'bread']

while shopping_cart:
    user_input = input('Would you like to SHOW, ADD, DELETE, or QUIT?\n')
    if user_input == 'SHOW':
        print(cart)
    if user_input == 'ADD':
        add_input = input('What would you like to add to your shopping cart?\n')
        cart.append(add_input)
    if user_input == 'DELETE':
        delete_input = input('What would you like to delete from your shopping cart?\n')
        cart.remove(delete_input)
    if user_input == 'QUIT':
        shopping_cart = False
        if shopping_cart == False:
            print(cart)