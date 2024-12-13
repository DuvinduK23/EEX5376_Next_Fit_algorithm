class NextFitMemoryManager:
    def __init__(self, memory_blocks):
        """
        Initializes the memory manager with a list of memory blocks.
        Each block is represented by a dictionary with its size and status.
        """
        self.memory = [{"size": size, "status": "Free"} for size in memory_blocks]
        self.last_allocated_block = -1  # Keep track of the last allocated block

    def allocate_memory(self, process_size):
        """
        Allocates memory to a process using the Next Fit algorithm.
        Starts searching from the last allocated block and wraps around if necessary.
        """
        num_blocks = len(self.memory)
        
        # First, check the last allocated block if it has enough free space
        if self.last_allocated_block != -1 and self.memory[self.last_allocated_block]["status"] == "Free" and self.memory[self.last_allocated_block]["size"] >= process_size:
            self.memory[self.last_allocated_block]["size"] -= process_size
            if self.memory[self.last_allocated_block]["size"] == 0:
                self.memory[self.last_allocated_block]["status"] = "Allocated"  # Mark as fully allocated
            return f"Process of size {process_size} KB allocated at block {self.last_allocated_block}."

        # If not, start searching from the next block
        for i in range(self.last_allocated_block + 1, num_blocks):
            if self.memory[i]["status"] == "Free" and self.memory[i]["size"] >= process_size:
                # Allocate memory by updating block status
                self.memory[i]["size"] -= process_size
                if self.memory[i]["size"] == 0:
                    self.memory[i]["status"] = "Allocated"  # Mark as fully allocated
                self.last_allocated_block = i  # Update the pointer to the last allocated block
                return f"Process of size {process_size} KB allocated at block {i}."

        # If no block found, wrap around to the beginning of the memory and continue searching
        for i in range(0, self.last_allocated_block + 1):
            if self.memory[i]["status"] == "Free" and self.memory[i]["size"] >= process_size:
                # Allocate memory by updating block status
                self.memory[i]["size"] -= process_size
                if self.memory[i]["size"] == 0:
                    self.memory[i]["status"] = "Allocated"  # Mark as fully allocated
                self.last_allocated_block = i  # Update the pointer to the last allocated block
                return f"Process of size {process_size} KB allocated at block {i}."

        # If no suitable block is found, return allocation failure message
        return "No suitable block found for allocation."

    def display_memory(self):
        """
        Displays the current state of the memory blocks.
        """
        print("\nCurrent Memory State:")
        for i, block in enumerate(self.memory):
            status = block['status']
            # Add an indication of how much free space remains if the block is allocated
            if status == "Allocated":
                print(f"Block {i}: Size {block['size']} KB, Status {status} (Remaining Space: {block['size']} KB)")
            else:
                print(f"Block {i}: Size {block['size']} KB, Status {status}")

# Example usage with user input for allocations
def user_input_allocation():
    memory_blocks = [200, 300, 100, 500, 50]  # Example memory blocks in KB
    manager = NextFitMemoryManager(memory_blocks)

    while True:
        manager.display_memory()

        # Ask the user for a process size to allocate
        try:
            process_size = int(input("\nEnter process size (KB) to allocate (0 to exit): "))
            if process_size == 0:
                print("Exiting...")
                break
        except ValueError:
            print("Please enter a valid integer for process size.")
            continue

        # Allocate memory for the process
        allocation_result = manager.allocate_memory(process_size)
        print(allocation_result)

# Run the program to allow user to input allocations
user_input_allocation()
