from advent.utils import array


class HighEntropyPassphrases(object):
    @staticmethod
    def is_valid(phrase):
        """
        A new system policy has been put in place that requires all accounts to use a passphrase instead of simply
        a password. A passphrase consists of a series of words (lowercase letters) separated by spaces.
        To ensure security, a valid passphrase must contain no duplicate words.
        :param phrase:
        :return:
        """
        tokens = array(phrase)[0]
        return len(tokens) == len(set(tokens))

    @staticmethod
    def is_valid_without_permutations(phrase):
        sorted_tokens = []
        for token in array(phrase)[0]:
            sorted_tokens.append(''.join(sorted(token)))
        return len(sorted_tokens) == len(set(sorted_tokens))
