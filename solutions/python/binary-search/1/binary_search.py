def find(search_list, value):
    # sort search_list
    search_list.sort()
    value_index = 0
    while True:
        if search_list == []:
            raise ValueError("value not in array")
        else:
            # get the middle element
            index = len(search_list)//2
        
        if value > search_list[index]:
            search_list = search_list[(index+1):]
            value_index += (index + 1)
        elif value < search_list[index]:
            search_list = search_list[:index]
        else: # must be equality condition
            value_index += index 
            return value_index
