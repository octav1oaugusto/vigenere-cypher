import itertools
from cypher.vigenere import Decifrador
from util.frequencia_util import ENGLISH_FREQ, PORTUGUES_FREQ

ALFABETO = "abcdefghijklmnopqrstuvwxyz"

class AtaqueAnaliseFrequencia:
    chave = ""
    keys = []

    def __init__(self, texto):
        for key in reversed(self.solve_vigenere(texto)):
            self.keys.append(key)

    def __str__(self):
        return self.keys

    def get_keys(self):
        return self.keys

    def vigenere(self, plaintext, key, a_is_zero=True):
        key_iter = itertools.cycle(map(ord, key))
        return "".join(
            chr(ord('a') + (
                (next(key_iter) - ord('a') + ord(letter) - ord('a'))
                + (0 if a_is_zero else 2)
            ) % 26) if letter in ALFABETO
            else letter
            for letter in plaintext.lower()
        )

    def vigenere_decrypt(self, ciphertext, key, a_is_zero=True):
        inverse = "".join(chr(ord('a') +
                              ((26 if a_is_zero else 22) -
                               (ord(k) - ord('a'))
                               ) % 26) for k in key)
        return self.vigenere(ciphertext, inverse, a_is_zero)

    def compare_freq(self, text):
        if not text:
            return None
        text = [t for t in text.lower() if t in ALFABETO]
        freq = [0] * 26
        total = float(len(text))
        for l in text:
            freq[ord(l) - ord('a')] += 1
        return sum(abs(f / total - E) for f, E in zip(freq, self.FREQ))

    def solve_vigenere(self, text, key_min_size=None, key_max_size=None, a_is_zero=True):
        best_keys = []
        key_min_size = key_min_size or 1
        key_max_size = key_max_size or 20

        text_letters = [c for c in text.lower() if c in ALFABETO]

        for key_length in range(key_min_size, key_max_size):
            key = [None] * key_length
            for key_index in range(key_length):
                letters = "".join(itertools.islice(
                    text_letters, key_index, None, key_length))
                shifts = []
                for key_char in ALFABETO:
                    shifts.append(
                        (self.compare_freq(Decifrador(
                            letters, key_char).texto_processado), key_char)
                    )
                key[key_index] = min(shifts, key=lambda x: x[0])[1]
            best_keys.append("".join(key))

        best_keys.sort(key=lambda key: self.compare_freq(
            self.vigenere_decrypt(text, key, True)))
        return best_keys[:2]

class AtaqueAnaliseFrequenciaPT(AtaqueAnaliseFrequencia):
    def __init__(self, texto):
        self.FREQ = PORTUGUES_FREQ
        super().__init__(texto)

class AtaqueAnaliseFrequenciaENG(AtaqueAnaliseFrequencia):
    def __init__(self, texto):
        self.FREQ = ENGLISH_FREQ
        super().__init__(texto)
