import tkinter as tk

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

class MemoryManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Memory Manager")
        self.memory_manager = NextFitMemoryManager([200, 300, 100, 500, 50])

        self.setup_ui()

    def setup_ui(self):
        self.process_size_label = tk.Label(self.root, text="Process Size (KB):")
        self.process_size_label.pack(pady=10)

        self.process_size_entry = tk.Entry(self.root)
        self.process_size_entry.pack(pady=10)

        self.allocate_button = tk.Button(self.root, text="Allocate Memory", command=self.allocate_memory)
        self.allocate_button.pack(pady=10)

        self.result_label = tk.Label(self.root, text="")
        self.result_label.pack(pady=10)

        self.canvas = tk.Canvas(self.root, width=400, height=300, bg="white")
        self.canvas.pack(pady=10)

        self.draw_memory()

    def allocate_memory(self):
        process_size = int(self.process_size_entry.get())
        result = self.memory_manager.allocate_memory(process_size)
        self.result_label.config(text=result)
        self.draw_memory()

    def draw_memory(self):
        self.canvas.delete("all")
        memory_state = self.memory_manager.get_memory_state()
        block_height = 30
        block_width = 300
        start_x = 50
        start_y = 20

        for index, block in enumerate(memory_state):
            y = start_y + index * (block_height + 10)
            color = "green" if block["status"] == "Free" else "red"
            self.canvas.create_rectangle(start_x, y, start_x + block_width, y + block_height, fill=color)
            self.canvas.create_text(start_x + 10, y + 15, anchor="w", text=f"Block {index}: {block['size']} KB, {block['status']}")

            if index == self.memory_manager.last_allocated_block:
                self.canvas.create_line(start_x - 20, y + block_height / 2, start_x, y + block_height / 2, arrow=tk.LAST)
                self.canvas.create_text(start_x - 30, y + block_height / 2, anchor="e", text="Pointer")

if __name__ == "__main__":
    root = tk.Tk()
    app = MemoryManagerApp(root)
    root.mainloop()
