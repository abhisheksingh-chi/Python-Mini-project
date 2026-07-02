user_list = []
no_of_items =int(input("Enter the number of items you want to add: ")) 
print("Please enter an integer!")
    
for i in range(no_of_items):
    items = input(f"Enter element {i+1}: ")
    user_list.append(items)
print("-----------LIST------------")
for i in range(len(user_list)) :
    print(f"{i+1}. {user_list[i].capitalize()}. ")
    i += 1  
