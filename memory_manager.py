class NextFitMemoryManager:
    def __init__(self, memory_blocks):
        self.memory = [{"size": size, "status": "Free"} for size in memory_blocks]
        self.last_allocated_block = -1

    def allocate_memory(self, process_size):
        num_blocks = len(self.memory)
        start_block = self.last_allocated_block

        if self.last_allocated_block != -1 and self.memory[self.last_allocated_block]["status"] == "Free" and self.memory[self.last_allocated_block]["size"] >= process_size:
            self.memory[self.last_allocated_block]["size"] -= process_size
            if self.memory[self.last_allocated_block]["size"] == 0:
                self.memory[self.last_allocated_block]["status"] = "Full"
            return f"Process of size {process_size} KB allocated at block {self.last_allocated_block}."

        for i in range(self.last_allocated_block + 1, num_blocks):
            if self.memory[i]["status"] == "Free" and self.memory[i]["size"] >= process_size:
                self.memory[i]["size"] -= process_size
                if self.memory[i]["size"] == 0:
                    self.memory[i]["status"] = "Full"
                self.last_allocated_block = i
                return f"Process of size {process_size} KB allocated at block {i}."

        for i in range(0, self.last_allocated_block + 1):
            if self.memory[i]["status"] == "Free" and self.memory[i]["size"] >= process_size:
                self.memory[i]["size"] -= process_size
                if self.memory[i]["size"] == 0:
                    self.memory[i]["status"] = "Full"
                self.last_allocated_block = i
                return f"Process of size {process_size} KB allocated at block {i}."

        return "No suitable block found for allocation."

    def get_memory_state(self):
        return self.memory

        