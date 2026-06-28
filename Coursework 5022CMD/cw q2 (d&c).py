import time
class Transaction:    #entity class
    def __init__(self, transactionID, customerName, productName, amount, transactionDate):
        self.transactionID = transactionID
        self.customerName = customerName
        self.productName = productName
        self.amount = amount
        self.transactionDate = transactionDate

    def __str__(self):
        return (f"ID:{self.transactionID} - {self.customerName} - {self.productName} - RM{self.amount:.2f} - {self.transactionDate}")


def merge_sort(arr):  #merge sort
    if len(arr) <= 1:   #base case if 0 or 1 item -> already sorted -> return immediately
        return arr

    middle = len(arr) // 2   #divide
    left = arr[:middle]  #everything :before the middle
    right = arr[middle:]  #everything after: the middle

    left = merge_sort(left)  #conquer
    right = merge_sort(right)

    return merge(left, right)  #call the merge func from below to merge back


def merge(left, right):  #merge sort (merge back)
    result = []   # collects the final merged, sorted order
    i = j = 0    # i will check the left side and j will check the right side.

    while i < len(left) and j < len(right):   # keep going while BOTH lists still have items
        if left[i].transactionID < right[j].transactionID:
            result.append(left[i])
            i += 1           # left's item is smaller, take it, move forward
        else:
            result.append(right[j])
            j += 1       # right's item is smaller/equal, take it, move forward

    result.extend(left[i:])
    result.extend(right[j:])
    return result


def binary_search(arr, target, low, high):  #binary search
    if low > high:
        return -1     #base case, range is empty, target not found

    middle = (low + high) // 2   #find the middle of the current range.

    if arr[middle].transactionID == target:
        return middle

    return (binary_search(arr, target, low, middle - 1) if target < arr[middle].transactionID
            else binary_search(arr, target, middle + 1, high))
    # if target is smaller, search the LEFT half; otherwise search the RIGHT half


def linear_search(arr, target): #linear search
    for i in range(len(arr)):
        if arr[i].transactionID == target:   #match found, return its index immediatly
            return i
    return -1   #checked evreything, never found a match


def display_transactions(arr): #display transaction
    for transaction in arr:
        print(transaction)   # print() automatically calls __str__ on each Transaction


def compare_performance(arr):
    existing_ids = [1001, 1005, 1010]      # IDs known to exist in the dataset
    non_existing_ids = [9999, 8888]         # IDs known to NOT exist

    start = time.perf_counter()
    for _ in range(1000):
        sorted_arr = merge_sort(arr.copy())    # sort a fresh copy each time, repeated for measurable timing
    end = time.perf_counter()
    merge_time = end - start

    print("\nPerformance Comparison")
    print("-----------------------")
    print(f"Merge Sort Time (1000 runs): {merge_time:.6f} seconds")
    print("\n--- Binary Search vs Linear Search ---")

    for target in existing_ids + non_existing_ids:     # loop through BOTH groups together
        label = "existing" if target in existing_ids else "non-existing"

        start = time.perf_counter()
        for _ in range(10000):
            binary_search(sorted_arr, target, 0, len(sorted_arr) - 1)
        binary_time = time.perf_counter() - start

        start = time.perf_counter()
        for _ in range(10000):
            linear_search(sorted_arr, target)
        linear_time = time.perf_counter() - start

        print(f"\nSearching ID {target} ({label}):")
        print(f"  Binary Search Time : {binary_time:.6f} seconds")
        print(f"  Linear Search Time : {linear_time:.6f} seconds")


def menu():   ####### MAIN PROGRAM "MENU" #########
    transactions = [         #predefined dataset  ***UNSORTED**
        Transaction(1008, "Ali", "Laptop", 2500, "2026-06-01"),
        Transaction(1003, "John", "Mouse", 50, "2026-06-02"),
        Transaction(1010, "Sarah", "Keyboard", 120, "2026-06-03"),
        Transaction(1001, "Adam", "Monitor", 800, "2026-06-04"),
        Transaction(1005, "Lisa", "Printer", 450, "2026-06-05"),
        Transaction(1002, "David", "USB", 35, "2026-06-06"),
        Transaction(1009, "Aina", "Tablet", 1200, "2026-06-07"),
        Transaction(1006, "Ming", "Phone", 1800, "2026-06-08"),
        Transaction(1004, "Kumar", "SSD", 300, "2026-06-09"),
        Transaction(1007, "Siti", "Camera", 1500, "2026-06-10")
    ]
    sorted_transactions = transactions

    while True:
        print("\n===== Transaction System =====")
        print("1. Display Transactions")
        print("2. Sort using Merge Sort")
        print("3. Search using Binary Search")
        print("4. Search using Linear Search")
        print("5. Compare Performance")
        print("6. Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            display_transactions(sorted_transactions)

        elif choice == "2":
            print("\nBefore Sorting")
            display_transactions(transactions)
            sorted_transactions = merge_sort(transactions)
            print("\nAfter Sorting")
            display_transactions(sorted_transactions)

        elif choice == "3":
            target = int(input("Enter Transaction ID: "))
            result = binary_search(sorted_transactions, target, 0, len(sorted_transactions) - 1)
            print(sorted_transactions[result] if result != -1 else "Transaction not found")

        elif choice == "4":
            target = int(input("Enter Transaction ID: "))
            result = linear_search(sorted_transactions, target)
            print(sorted_transactions[result] if result != -1 else "Transaction not found")

        elif choice == "5":
            compare_performance(sorted_transactions)

        elif choice == "6":
            print("Goodbye")
            break

        else:
            print("Invalid choice")
menu()