# This is a space for scrap work for Graphs week

listicle = [[8, 4], [90, -1, 3], [9, 62], [-7, -1, -56, -6], [201], [76, 18]]

def smallest_calculator(lists):
    total = 0
    for small_list in lists:
        smallest_item = small_list[0]
        for item in small_list:
            if item < smallest_item:
                smallest_item = item
        print(smallest_item)
        total += smallest_item 
    return f"Total:{total}"

print(smallest_calculator(listicle))