class MemoryReallocation(object):
    def __init__(self):
        pass

    def reallocate(self, banks):
        current_banks = tuple([int(i) for i in banks.split()])

        # Save the initial state of the world
        seen_banks = {current_banks}
        count = 1
        while True:
            current_banks = self.spread(current_banks)
            if current_banks in seen_banks:
                return count
            count += 1
            seen_banks.add(current_banks)

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
