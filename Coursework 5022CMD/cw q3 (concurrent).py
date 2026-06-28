import time              # needed for measuring execution time
import threading          # needed for creating and managing threads


######## Factorial Function ######
def factorial(n):
    result = 1                      # starting value for the running product
    for i in range(1, n + 1):         # loop from 1 up to and including n
        result *= i                     # multiply result by the current number
    return result                     # send back the final factorial value


########## Multithreaded Version ############
def factorial_thread(n, results, index):
    results[index] = factorial(n)      # calculate factorial(n) and store it at "index" in the shared list


def run_multithreaded():
    numbers = [50, 100, 200]           # the three numbers we need factorials for
    results = [None, None, None]        # shared storage, one slot per thread's result
    threads = []                          # will hold the 3 Thread objects

    start_time = time.perf_counter_ns()   # record t1, BEFORE any thread starts

    for i, n in enumerate(numbers):                                  # i = 0,1,2 ; n = 50,100,200
        t = threading.Thread(target=factorial_thread, args=(n, results, i))
        # creates a thread that will run factorial_thread(n, results, i) when started
        threads.append(t)        # keep track of this thread so we can wait for it later
        t.start()                   # actually begin running the thread now

    for t in threads:               # loop through all 3 threads
        t.join()                       # wait here until this particular thread finishes

    end_time = time.perf_counter_ns()   # record t2, AFTER all threads have completed
    return end_time - start_time          # T = t2 - t1, the total elapsed time in nanoseconds


################# Sequential Version (no threading) ##############
def run_sequential():
    numbers = [50, 100, 200]            # same three numbers as before

    start_time = time.perf_counter_ns()   # record t1

    for n in numbers:                       # process each number ONE AT A TIME
        factorial(n)                           # calculate it, but don't bother storing the result here

    end_time = time.perf_counter_ns()       # record t2
    return end_time - start_time              # T = t2 - t1


###################### Run 10 Rounds and Average (Multithreaded) ######################
def test_multithreaded_10_rounds():
    print("\n===== MULTITHREADED TEST (10 rounds) =====")
    times = []                                # will collect all 10 T values
    for round_num in range(1, 11):              # round_num = 1,2,...,10
        elapsed = run_multithreaded()              # run once, get T for this round
        times.append(elapsed)                        # save it
        print(f"Round {round_num}: T = {elapsed} ns")  # show this round's result
    total = sum(times)                          # add up all 10 T values
    average = total / len(times)                  # divide by 10 to get the average T
    print(f"\nTotal time: {total} ns")
    print(f"Average time (T): {average:.2f} ns")
    return times, total, average                  # send back all the data, in case it's needed elsewhere


#################### Run 10 Rounds and Average (Sequential) ########
def test_sequential_10_rounds():
    print("\n===== SEQUENTIAL TEST (10 rounds) =====")
    times = []
    for round_num in range(1, 11):
        elapsed = run_sequential()
        times.append(elapsed)
        print(f"Round {round_num}: T = {elapsed} ns")
    total = sum(times)
    average = total / len(times)
    print(f"\nTotal time: {total} ns")
    print(f"Average time (T): {average:.2f} ns")
    return times, total, average


############### Main Program (Menu) #############
def menu():
    while True:
        print("\n===== Factorial Concurrency Experiment =====")
        print("1. Run Multithreaded Test (10 rounds)")
        print("2. Run Sequential Test (10 rounds)")
        print("3. Run BOTH and compare")
        print("4. Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            test_multithreaded_10_rounds()           # just run the multithreaded test alone

        elif choice == "2":
            test_sequential_10_rounds()                 # just run the sequential test alone

        elif choice == "3":
            mt_times, mt_total, mt_avg = test_multithreaded_10_rounds()    # run both tests
            seq_times, seq_total, seq_avg = test_sequential_10_rounds()

            print("\n===== COMPARISON SUMMARY =====")
            print(f"Multithreaded - Total: {mt_total} ns | Average: {mt_avg:.2f} ns")
            print(f"Sequential    - Total: {seq_total} ns | Average: {seq_avg:.2f} ns")

            if mt_avg < seq_avg:                          # compare the two averages
                print("\nResult: Multithreading was faster on average.")
            else:
                print("\nResult: Sequential was faster (or equal) on average.")

        elif choice == "4":
            print("Exiting program. Goodbye!")
            break                                            # exits the while loop, ends the program

        else:
            print("Invalid choice, try again.")


if __name__ == "__main__":     # only run menu() if this file is run directly
    menu()