# sequential search

def seq_search(item_list, item):
    found = False
    for val in item_list:
        if val == item:
            found = True
            break
        else:
            found = False
    return found

print(seq_search([1,4,2,5,6,5,9], 2))