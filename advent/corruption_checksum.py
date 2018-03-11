from advent.utils import first, array


class CorruptionChecksum(object):
    @staticmethod
    def calc_checksum(checksum_input):
        checksum_result = 0
        for row in array(checksum_input):
            checksum_result += max(row) - min(row)
        return checksum_result

    @staticmethod
    def calc_even_divisible_checksum(checksum_input):
        checksum_result = 0
        for row in array(checksum_input):
            checksum_result += first(a / b for a in row for b in row if a > b and a % b == 0)
        return checksum_result
