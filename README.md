# Merge Sort Algorithm with Performance Profiling

This project implements the Merge Sort algorithm in Python and measures its execution performance using `cProfile`. The script recursively sorts randomly generated lists of integers and increases the list size to analyze sorting efficiency.

## Features
- Implements the Merge Sort algorithm (divide-and-conquer approach).
- Measures execution time for different list sizes.
- Uses `cProfile` for performance analysis.
- Recursively generates lists with increasing sizes up to 10,000 elements.

## How It Works
1. The `merge_sort` function recursively divides and sorts an unsorted list.
2. The `merge` function merges two sorted lists into a single sorted list.
3. The `vectors` function generates random lists, sorts them using Merge Sort, and measures execution time.
4. The `main` function initializes the sorting process with a list size of 1000 and progressively increases it.
5. The script is executed with `cProfile.run("main()")` to analyze performance.

## Installation
Ensure you have Python 3 installed on your system. Clone the repository or download the script.

## Usage
Run the script using:

```bash
Merge_sort.py
```

The script will execute the Merge Sort algorithm and display execution times for different list sizes.

## Performance Profiling
The script utilizes Python’s built-in `cProfile` module to track execution time and function calls.

## License
This project is open-source and available for free use.
