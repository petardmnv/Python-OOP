class vowels:
    def __init__(self, s):
        self.s = s
        self.i = -1

    def __iter__(self):
        return self

    def __next__(self):
        while self.i < (len(self.s) - 1):
            self.i += 1
            if self.is_vowel(self.s[self.i]):
                return self.s[self.i]
        raise StopIteration

    @staticmethod
    def is_vowel(c: str):
        vowels: str = "aeuoyi"
        if c.lower() in vowels:
            return True
        return False


my_string = vowels('Abcedifuty0o')
for char in my_string:
    print(char)