from memory_manager import MemoryManager

def main():
    """
    Runs the memory allocation simulation with an interactive menu.
    """
    # Example memory block sizes
    block_sizes = [200, 300, 100, 500, 50]
    mm = MemoryManager(block_sizes)

    while True:
        print("\nMenu:")
        print("1. Display Memory")
        print("2. Allocate Memory")
        print("3. Free Memory")
        print("4. Exit")
        
        try:
            choice = int(input("Enter your choice: "))

            if choice == 1:
                mm.display_memory()  # Show the current memory state
            elif choice == 2:
                try:
                    size = int(input("Enter process size (KB): "))  # Process size input
                    print(mm.allocate_memory(size))  # Try to allocate memory
                except ValueError:
                    print("Invalid input. Please enter a numeric value.")
            elif choice == 3:
                try:
                    index = int(input("Enter block index to free: "))  # Block index input
                    print(mm.free_memory(index))  # Free the memory at the given index
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
    main()
