class CorruptionChecksum(object):
    @staticmethod
    def calc_checksum(checksum_input):
        checksum_result = 0
        for row in checksum_input.splitlines():
            row_tuple = tuple(map(int, row.strip().split(' ')))
            checksum_result += max(row_tuple) - min(row_tuple)
        return checksum_result

    @staticmethod
    def calc_even_divisible_checksum(checksum_input):
        checksum_result = 0
        for row in checksum_input.splitlines():
            row_increasing = sorted(tuple(map(int, row.strip().split(' '))))
            row_decreasing = sorted(tuple(map(int, row.strip().split(' '))), reverse=True)
            for col_i in row_decreasing:
                for col_j in row_increasing:
                    if col_i > col_j and col_i % col_j == 0:
                        checksum_result += col_i / col_j
        return checksum_result
