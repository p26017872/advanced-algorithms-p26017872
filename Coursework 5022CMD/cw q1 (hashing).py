import time

# Entity Class
class Medicine:
    def __init__(self, product_id, name, category, price, quantity):
        self.product_id = product_id
        self.name = name
        self.category = category
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f"[ID:{self.product_id}] {self.name} | {self.category} | RM{self.price:.2f} | Qty: {self.quantity}"


# Hash Table with Linear Probing
class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [None] * size

    def hash_function(self, product_id):
        return product_id % self.size

    def insert(self, medicine):
        index = self.hash_function(medicine.product_id)
        start_index = index

        while self.table[index] is not None:
            if self.table[index].product_id == medicine.product_id:
                print(f"Duplicate ID {medicine.product_id}! Cannot insert.")
                return
            index = (index + 1) % self.size
            if index == start_index:
                print("Hash table is full!")
                return

        self.table[index] = medicine

    def search(self, product_id):
        index = self.hash_function(product_id)
        start_index = index

        while self.table[index] is not None:
            if self.table[index].product_id == product_id:
                return self.table[index]
            index = (index + 1) % self.size
            if index == start_index:
                break

        return None

    def display(self):
        print("\n--- Hash Table Contents ---")
        for i in range(self.size):

            if self.table[i] is None:
                print("Slot", i, ": Empty")
            else:
                print("Slot", i, ":", self.table[i])


# Plain Array Search (for comparison)
def array_search(arr, product_id):
    for item in arr:
        if item.product_id == product_id:
            return item
    return None

# Performance Comparison
def compare_performance(ht, arr, search_id, label):
    start = time.perf_counter()
    for _ in range(10000):
        ht.search(search_id)
    end = time.perf_counter()
    ht_time = end - start

    start = time.perf_counter()
    for _ in range(10000):
        array_search(arr, search_id)
    end = time.perf_counter()
    arr_time = end - start

    print(f"\n--- Searching for {label} (ID: {search_id}) ---")
    print(f"Hash Table time : {ht_time:.6f} seconds")
    print(f"Array time       : {arr_time:.6f} seconds")


def menu():
    ht = HashTable(10)  #create a hash table object with 10 slots

    m1 = Medicine(101, "Paracetamol", "Tablet", 5.50, 100)   #create object for predefined
    m2 = Medicine(102, "Cough Syrup", "Syrup", 12.00, 40)
    m3 = Medicine(103, "Vitamin C", "Supplement", 8.90, 60)
    m4 = Medicine(104, "Antacid", "Tablet", 6.20, 75)
    m5 = Medicine(105, "Fish Oil", "Supplement", 25.00, 30)

    ht.insert(m1) #insert the predefined data using into the hash table
    ht.insert(m2)
    ht.insert(m3)
    ht.insert(m4)
    ht.insert(m5)

    sample_medicines = [m1, m2, m3, m4, m5]  #for comparing

    while True:
        print("\n===== Pharmacy Inventory System =====")
        print("1. Display all medicines")
        print("2. Insert new medicine")
        print("3. Search medicine by ID")
        print("4. Compare Hash Table vs Array performance")
        print("5. Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            ht.display()

        elif choice == "2":  #insert
            pid = int(input("Enter Product ID: "))
            name = input("Enter Name: ")
            category = input("Enter Category: ")
            price = float(input("Enter Price: "))
            qty = int(input("Enter Quantity: "))

            medicine = Medicine(pid, name, category, price, qty)  #create medicine object

            ht.insert(medicine)
            print("Medicine inserted!")

        elif choice == "3":  #search
            pid = int(input("Enter Product ID to search: "))
            result = ht.search(pid)
            print(result if result else "Medicine not found.")

        elif choice == "4":
            existing_ids = [101, 103, 104, 105]
            non_existing_ids = [777, 888, 999]
            print("\n========== EXISTING KEYS ==========")
            for pid in existing_ids:
                compare_performance(ht, sample_medicines, pid, "existing key")

            print("\n========== NON-EXISTING KEYS ==========")
            for pid in non_existing_ids:
                compare_performance(ht, sample_medicines, pid, "non-existing key")

        elif choice == "5":
            print("Exiting program. Goodbye!")
            break

        else:
            print("Invalid choice, try again.")


if __name__ == "__main__":
    menu()

