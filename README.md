# Memory Manager - Next Fit Algorithm

## Overview
This is a simple memory management simulation that implements the **Next Fit** memory allocation algorithm. The program allows users to allocate and free memory blocks, simulating how memory management works in an operating system.

## Features
- **Display Memory**: View the current state of memory blocks, showing their size and allocation status (Free or Allocated).
- **Allocate Memory**: Allocate memory for a process using the Next Fit algorithm, which begins searching for a free block from where the last allocation occurred.
- **Free Memory**: Free a specific memory block, making it available for future allocations.
- **Exit**: Exit the program.

## How It Works
The memory is initialized with predefined block sizes, and each block is initially marked as "Free." When a user tries to allocate memory, the system uses the Next Fit algorithm to find the next available block large enough to fit the requested size, starting from the last allocated block. If a suitable block is found, its size is reduced, and it is marked as "Allocated." When memory is freed, the status of the block is updated to "Free."

### Key Concepts:
1. **Memory Blocks**: The memory is divided into fixed-size blocks.
2. **Next Fit Allocation**: The program searches for available blocks from where the last allocation was made.
3. **Free/Allocated Blocks**: Each block can either be free or allocated to a process.

## Accsess Demo Application

**ec2-43-204-234-224.ap-south-1.compute.amazonaws.com:5000

