# Get list as an input
def getListInput(list_name):
    # creating an empty list
    input_list = []
    
    # number of elements as input
    list_count = int(input("\nEnter " + list_name + " list item count: "))
  
    for i in range(list_count):
        while True:
            try:
                item = int(input("Enter item: "))
                input_list.append(item)
                break;
            except ValueError:
                print("Only number allowed.")
      
    return input_list

# Get common items in two lists
def getCommonItemList(first_list, second_list):
    print("\nFirst List: ", first_list)
    print("Second List: ", second_list)
    common_list = []

    for item in first_list:
        if (item in second_list and item not in common_list):
            common_list.append(item)

    return common_list

print("\n********************* Two List Common Elements *********************")
first_list = getListInput('First')
second_list = getListInput('Second')
print("Common List: ", getCommonItemList(first_list, second_list))
