vowels = {'A', 'E', 'O', 'I', 'U', 'Y'}


def vowel_filter(fn):
    def wapper():
        res = fn()
        return [r for r in res if r.upper() in vowels]
    return wapper


@vowel_filter
def get_letters():
    return ["a", "b", "c", "d", "E"]

print(get_letters())