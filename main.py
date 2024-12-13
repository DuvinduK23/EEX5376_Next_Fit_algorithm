import MemoryManager from memory_manager

def run_simulation():
    """
    Runs the memory allocation simulation with an interactive menu.
    """
    block_sizes = [200, 300, 100, 500, 50]
    manager = MemoryManager(sum(block_sizes))  # Initialize with total memory size
    print(f"Simulation initialized with total memory size: {sum(block_sizes)} KB.\n")

    while True:
        print("\nMenu:")
        print("1. Display Memory")
        print("2. Allocate Memory")
        print("3. Free Memory")
        print("4. Exit")
        try:
            choice = int(input("Enter your choice: "))

            if choice == 1:
                manager.display_memory()
            elif choice == 2:
                try:
                    size = int(input("Enter process size (KB): "))
                    print(manager.allocate_memory(size))
                except ValueError:
                    print("Invalid input. Please enter a numeric value.")
            elif choice == 3:
                try:
                    address = int(input("Enter the start address of the block to free: "))
                    print(manager.free_memory(address))
                except ValueError:
                    print("Invalid input. Please enter a numeric value.")
            elif choice == 4:
                print("Exiting the simulation.")
                break
            else:
                print("Invalid choice. Please select a valid option.")
        except ValueError:
            print("Invalid input. Please enter a number corresponding to the menu options.")


if __name__ == "__main__":
    run_simulation()
