class CorruptionChecksum(object):
    @staticmethod
    def calc_checksum(checksum_input):
        checksum_result = 0
        for row in checksum_input.splitlines():
            row_tuple = tuple(map(int, row.replace('\t', ' ').strip().split(' ')))
            checksum_result += max(row_tuple) - min(row_tuple)
        return checksum_result
