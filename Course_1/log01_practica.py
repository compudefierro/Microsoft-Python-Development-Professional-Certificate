def binary_search(data, target):
    import logging

    logging.basicConfig(filename='log.txt', level=logging.INFO, filemode='w', format='%(asctime)s %(message)s')
    
    loops = 0
    low = 0
    high = len(data) - 1
  
    logging.info(f'Start binary_search: data={data}, target={target}')
  
    while low <= high:
        mid = (low + high) // 2
        loops += 1
        logging.info(f'Loop {loops}: low={low}, high={high}, mid={mid}, data[mid]={data[mid]}')
        if data[mid] == target:
            logging.info(f'Target found at index {mid} after {loops} loops')
            return mid, loops
        elif data[mid] < target:
            low = mid + 1
            logging.info(f'data[mid] < target, new low={low}')
        else:
            high = mid - 1
            logging.info(f'data[mid] > target, new high={high}')
    logging.info(f'Target not found after {loops} loops')
    return -1, loops

data = [1, 2, 33, 23, 32, 3, 4, 53, 6, 7, 8, 9,10,11,12]
data.sort()  # Binary search requires a sorted list
target = 33
result = binary_search(data, target)
print(result)  # Output: 2 (index of target in data)