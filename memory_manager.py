class MemoryManager:
    def __init__(self, block_sizes):
        """
        Initializes the memory blocks and sets the Next Fit pointer.
        
        Args:
            block_sizes (list): List of block sizes (in KB).
        """
        # Initialize memory blocks with their size and status (Free).
        self.memory = [{"size": size, "status": "Free"} for size in block_sizes]
        # The pointer that tracks where the Next Fit search starts.
        self.next_fit_pointer = 0

    def allocate_memory(self, process_size):
        """
        Allocates memory for a process using the Next Fit algorithm.
        The algorithm starts searching from the current next_fit_pointer and searches circularly through the memory blocks.
        
        Args:
            process_size (int): Size of the process to allocate.
        
        Returns:
            str: Allocation result message, indicating success or failure.
        """
        num_blocks = len(self.memory)
        
        if process_size <= 0:
            return "Process size must be greater than 0."

        # Loop through all memory blocks starting from the current next_fit_pointer
        for i in range(num_blocks):
            # Calculate the current index to check (circular behavior)
            index = (self.next_fit_pointer + i) % num_blocks
            block = self.memory[index]

            # Check if the current block is free and has enough space for the process
            if block["status"] == "Free" and block["size"] >= process_size:
                allocated_size = process_size
                remaining_size = block["size"] - process_size

                # Allocate memory in the current block
                block["status"] = "Allocated"
                block["size"] = allocated_size  # Update the size to the allocated amount

                # If there is remaining space in the block, create a new Free block
                if remaining_size > 0:
                    self.memory.insert(index + 1, {"size": remaining_size, "status": "Free"})

                # Update the next_fit_pointer to the next block
                self.next_fit_pointer = (index + 1) % len(self.memory)
                return f"Process of size {process_size} KB allocated at block {index}."

        # If no suitable block is found after a complete circular scan, return failure message
        return "No suitable block found for allocation."

    def free_memory(self, block_index):
        """
        Frees a memory block.

        Args:
            block_index (int): Index of the block to free.
        
        Returns:
            str: Deallocation result message.
        """
        if 0 <= block_index < len(self.memory):
            block = self.memory[block_index]
            if block["status"] == "Allocated":
                block["status"] = "Free"
                self.merge_free_blocks()
                return f"Block {block_index} is now free."
            else:
                return f"Block {block_index} is already free."
        return "Invalid block index."

    def merge_free_blocks(self):
        """
        Merges adjacent free memory blocks.
        """
        i = 0
        while i < len(self.memory) - 1:
            current = self.memory[i]
            next_block = self.memory[i + 1]
            if current["status"] == "Free" and next_block["status"] == "Free":
                current["size"] += next_block["size"]
                self.memory.pop(i + 1)
            else:
                i += 1

    def display_memory(self):
        """
        Displays the current state of memory blocks.
        """
        print("Current Memory State:")
        print("-" * 40)
        for i, block in enumerate(self.memory):
            print(f"Block {i}: Size {block['size']} KB, Status {block['status']}")
        print("-" * 40)
