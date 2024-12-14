import unittest
import csv
from memory_manager import NextFitMemoryManager


class AutomatedTestRunner:
    def __init__(self, test_cases, output_csv="test_results.csv"):
        """
        Initialize the test runner with test cases and the output CSV file.

        Args:
            test_cases (list): List of test case methods to execute.
            output_csv (str): Path to the output CSV file.
        """
        self.test_cases = test_cases
        self.output_csv = output_csv

    def run_tests(self):
        """
        Run all test cases and save the results to the CSV file.
        """
        results = []
        for test_case in self.test_cases:
            for result in test_case():
                results.append(result)

        self.save_results_to_csv(results)

    def save_results_to_csv(self, results):
        """
        Save the test results to a CSV file.

        Args:
            results (list): List of test results with details.
        """
        with open(self.output_csv, mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Test Case ID", "Description", "Input", "Expected Output", "Actual Output", "Status"])
            writer.writerows(results)


class TestNextFitMemoryManager:
    def __init__(self):
        self.manager = NextFitMemoryManager([200, 300, 100, 500, 50])
        self.test_case_id = 1

    def generate_test_case_id(self):
        """Generate and increment the test case ID."""
        case_id = f"TC{str(self.test_case_id).zfill(3)}"
        self.test_case_id += 1
        return case_id

    def test_allocate_memory_success(self):
        """Test successful memory allocations."""
        test_results = []
        process_sizes = [150, 250, 80, 50, 100]
        expected_blocks = [0, 1, 2, 4, 2]

        for process_size, block in zip(process_sizes, expected_blocks):
            description = f"Allocate process of size {process_size} KB."
            expected = f"Process of size {process_size} KB allocated at block {block}."
            actual = self.manager.allocate_memory(process_size)
            status = "Pass" if expected in actual else "Fail"
            test_results.append((self.generate_test_case_id(), description, f"Process size: {process_size} KB", expected, actual, status))

        return test_results

    def test_allocate_memory_failure(self):
        """Test allocation failure when no block fits."""
        test_results = []

        process_size = 600
        description = "Allocate memory failure when no block is large enough."
        expected = "No suitable block found for allocation."
        actual = self.manager.allocate_memory(process_size)
        status = "Pass" if expected == actual else "Fail"
        test_results.append((self.generate_test_case_id(), description, f"Process size: {process_size} KB", expected, actual, status))

        process_size = 700
        description = "Allocate memory failure when no block is large enough."
        expected = "No suitable block found for allocation."
        actual = self.manager.allocate_memory(process_size)
        status = "Pass" if expected == actual else "Fail"
        test_results.append((self.generate_test_case_id(), description, f"Process size: {process_size} KB", expected, actual, status))

        return test_results

    def test_allocate_memory_wrap_around(self):
        """Test Next Fit wrapping back to earlier blocks."""
        self.manager.allocate_memory(150)  # Allocates at block 0
        self.manager.allocate_memory(250)  # Allocates at block 1
        self.manager.allocate_memory(400)  # Allocates at block 3
        process_size = 80
        description = "Allocate memory wrapping back to earlier blocks."
        expected = "Process of size 80 KB allocated at block 2."
        actual = self.manager.allocate_memory(process_size)
        status = "Pass" if expected in actual else "Fail"
        return [(self.generate_test_case_id(), description, f"Process size: {process_size} KB", expected, actual, status)]

    def test_allocate_zero_or_negative_size(self):
        """Test allocation of zero or negative sizes."""
        test_results = []

        process_size = 0
        description = "Allocate zero-size memory."
        expected = "No suitable block found for allocation."
        actual = self.manager.allocate_memory(process_size)
        status = "Pass" if expected == actual else "Fail"
        test_results.append((self.generate_test_case_id(), description, f"Process size: {process_size} KB", expected, actual, status))

        process_size = -50
        description = "Allocate negative-size memory."
        expected = "No suitable block found for allocation."
        actual = self.manager.allocate_memory(process_size)
        status = "Pass" if expected == actual else "Fail"
        test_results.append((self.generate_test_case_id(), description, f"Process size: {process_size} KB", expected, actual, status))

        return test_results

    def test_exact_block_size_allocation(self):
        """Test allocation of a process that exactly matches a block size."""
        self.manager = NextFitMemoryManager([200, 300, 100, 500, 50])
        process_size = 100
        description = "Allocate process that exactly matches a block size."
        expected = "Process of size 100 KB allocated at block 2."
        actual = self.manager.allocate_memory(process_size)
        status = "Pass" if expected in actual else "Fail"
        return [(self.generate_test_case_id(), description, f"Process size: {process_size} KB", expected, actual, status)]

    def test_multiple_small_allocations(self):
        """Test multiple small allocations to check fragmentation handling."""
        self.manager = NextFitMemoryManager([200, 300, 100, 500, 50])
        test_results = []
        process_sizes = [50, 50, 50, 50, 50]
        expected_blocks = [0, 0, 1, 1, 2]

        for process_size, block in zip(process_sizes, expected_blocks):
            description = f"Allocate small process of size {process_size} KB."
            expected = f"Process of size {process_size} KB allocated at block {block}."
            actual = self.manager.allocate_memory(process_size)
            status = "Pass" if expected in actual else "Fail"
            test_results.append((self.generate_test_case_id(), description, f"Process size: {process_size} KB", expected, actual, status))

        return test_results

    def test_large_allocation_after_small_allocations(self):
        """Test large allocation after several small allocations."""
        self.manager = NextFitMemoryManager([200, 300, 100, 500, 50])
        self.manager.allocate_memory(50)  # Allocates at block 0
        self.manager.allocate_memory(50)  # Allocates at block 0
        self.manager.allocate_memory(50)  # Allocates at block 1
        self.manager.allocate_memory(50)  # Allocates at block 1
        process_size = 400
        description = "Allocate large process after several small allocations."
        expected = "Process of size 400 KB allocated at block 3."
        actual = self.manager.allocate_memory(process_size)
        status = "Pass" if expected in actual else "Fail"
        return [(self.generate_test_case_id(), description, f"Process size: {process_size} KB", expected, actual, status)]


if __name__ == "__main__":
    # Define test cases
    test_manager = TestNextFitMemoryManager()
    test_cases = [
        test_manager.test_allocate_memory_success,
        test_manager.test_allocate_memory_failure,
        test_manager.test_allocate_memory_wrap_around,
        test_manager.test_allocate_zero_or_negative_size,
        test_manager.test_exact_block_size_allocation,
        test_manager.test_multiple_small_allocations,
        test_manager.test_large_allocation_after_small_allocations,
    ]

    # Run tests and save results
    runner = AutomatedTestRunner(test_cases)
    runner.run_tests()
    print(f"Test results saved to {runner.output_csv}")
