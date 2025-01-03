from typing import List

# Memory Allocation
# Given an array of 0s and 1s, interpret every 8 bits as one block. A contiguous subarray of 0's that starts at the beginning of each block is considered "free memory". For example, given [0011111111111100], the free memory in each block is calculated as follows:

# Block 1: [00111111] (Free memory size: 2)
# Block 2: [11111100] (Free memory: 0)
# Input
# A list of queries in the format (i, j).

# Output
# A list where each element corresponds to one query. The output has the same size as the list of queries.

# Query Types
# Allocate Memory (i = 0): For a query like (0,5), find the earliest block where 5 consecutive 0's are available at the start of the block. Return the starting index of this block. If no suitable block is found, return -1. When memory is successfully allocated, mark those bits as 1, indicating the block is no longer available.
# Example: (0,5) -> Find a block with at least 5 consecutive 0's at the start; return the starting index.
# Release Memory (i = 1): For a query like (1,3), release the memory of the 3rd successful allocation. This query is always valid (i.e., there will always be 3 successful allocate memory queries before a release memory query with value 3). Return the size of the memory being released. Mark these bits as 0, indicating the block is available again.
# Example: (1,3) -> Release the 3rd successful memory allocation; return the size of the released memory.