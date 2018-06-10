class MemoryReallocation(object):
    def __init__(self):
        pass

    def reallocate(self, banks):
        current_banks = tuple([int(i) for i in banks.split()])

        # Save the initial state of the world
        seen_banks = {current_banks}
        seen_banks_at_cycle = {}
        count = 1
        while True:
            current_banks = self.spread(current_banks)
            if current_banks in seen_banks:
                return count, count - seen_banks_at_cycle[current_banks] + 1
            count += 1
            seen_banks.add(current_banks)
            seen_banks_at_cycle[current_banks] = count

    def spread(self, banks):
        """
        Distribute the largest bank across the other memory banks evenly
        :param banks:
        :return: A rebalanced banks
        """
        # Find the max bank
        banks_list = list(banks)
        max_bank_value = max(banks_list)
        max_bank_index = banks_list.index(max_bank_value)

        # Clear out the memory block
        banks_list[max_bank_index] = 0
        for i in range(max_bank_index + 1, max_bank_index + 1 + max_bank_value):
            banks_list[i % len(banks_list)] += 1
        return tuple(banks_list)


"""

Out of curiosity, the debugger would also like to know the size of the loop: starting from a state that has already been seen, how many block redistribution cycles must be performed before that same state is seen again?

In the example above, 2 4 1 2 is seen again after four cycles, and so the answer in that example would be 4.

How many cycles are in the infinite loop that arises from the configuration in your puzzle input?
"""
