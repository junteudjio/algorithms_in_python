__author__ = 'Junior Teudjio'



class CaesarCipher:
    def __init__(self, shift):
        lower_encoder = [None] * 26
        lower_decoder = [None] * 26
        upper_encoder = [None] * 26
        upper_decoder = [None] * 26

        for i in range(26):
            lower_encoder[i] =chr((i + shift) % 26 + ord('a'))
            lower_decoder[i] =chr((i - shift) % 26 + ord('a'))

            upper_encoder[i] =chr((i + shift) % 26 + ord('A'))
            upper_decoder[i] =chr((i - shift) % 26 + ord('A'))

        self._encoders = {
            'lower': ''.join(lower_encoder),
            'upper': ''.join(upper_encoder)
        }

        self._decoders = {
            'lower': ''.join(lower_decoder),
            'upper': ''.join(upper_decoder)
        }

    def encrypt(self, msg):
        return self._transform(msg, self._encoders)

    def decrypt(self, msg):
        return self._transform(msg, self._decoders)

    def _transform(self, msg, codes):
        original = list(msg)
        for i, c in enumerate(original):
            if c.isupper():
                j = ord(c) - ord('A')
                original[i] = codes['upper'][j]
            elif c.islower():
                j = ord(c) - ord('a')
                original[i] = codes['lower'][j]
        return ''.join(original)


if __name__ == '__main__':
    caesar_cipher = CaesarCipher(shift=3)
    print 'CaesarCipher(shift=3).encrypt("abcxyz ! ABCXYZ") =', caesar_cipher.encrypt('abcxyz ! ABCXYZ')
    print 'CaesarCipher(shift=3).encrypt("Love you mum !") =', caesar_cipher.encrypt('Love you mum !')

    print 'CaesarCipher(shift=3).decrypt("defabc ! DEFABC") =', caesar_cipher.decrypt('defabc ! DEFABC')
    print 'CaesarCipher(shift=3).decrypt("Oryh brx pxp !") =', caesar_cipher.decrypt('Oryh brx pxp !')