from advent.utils import first


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
            row_tuple = tuple(map(int, row.strip().split(' ')))
            checksum_result += first(a / b for a in row_tuple for b in row_tuple if a > b and a % b == 0)
        return checksum_result
