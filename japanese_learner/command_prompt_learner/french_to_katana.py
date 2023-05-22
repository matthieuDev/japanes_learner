'''

'''
import json, epitran
from nltk import ngrams

change_phon = {
    'ɛ': 'ə',
    'e': 'ə',
    'ɔ̃': 'on',
    'ɔ': 'on',
    'ɑ̃': 'an',
    'ɑ': 'an',
    '̃ ': '',
    '̃': '',
    'l': 'ʀ',
}

class french_to_katana:
    def __init__(self, which_alphabet='hiragana', epitran_code='fra-Latn') :
        assert which_alphabet in ('hiragana', 'katakana')
        
        save_file = f'{which_alphabet}2letter.json'
        with open (save_file, encoding='utf8') as f :
            self.translator2letters = json.load(f)
        self.epi = epitran.Epitran(epitran_code)

        self.phon_translator2letters = {
            tuple(self.epi.transliterate(let.replace('sh', 'ch'))): jap_let 
            for jap_let, let in self.translator2letters.items()
        }

    def phenotic_fr(self, s):
        s = s.replace('er', 'é').replace('ez', 'é')
        phons = self.epi.transliterate(s)
        if phons[-1] == s[-1] and phons[-1] in 'dpqstr' :
            phons = phons[:-1]
        phons = ''.join([change_phon.get(let, let) for let in phons if change_phon.get(let, let)])
        return phons
    def phenotic_fr2jap_let(self, phons) :
        retake = 0
        res = ''
        for let in ngrams(phons, 3 , pad_right=True):
            
            if let[0] is None :
                break
            if retake > 0 :
                retake -= 1
            else :
                #print(res, let, phons)
                found_smthg = False
                for test_let, size_let in [
                    (let, 3),
                    (let[:2], 2),
                    (let[:2] + ('y',), 2),
                    (let[:1], 1),
                    (let[:1] + ('y',), 1),
                    (let[:1] + ('ə',), 1),
                ]:
                    if test_let in self.phon_translator2letters :
                        res += self.phon_translator2letters[test_let]
                        retake = size_let - 1
                        found_smthg =  True
                        break
                if not found_smthg and let[0] == 'ʃ':
                    res += self.phon_translator2letters[tuple('ʃi')]
                    found_smthg =  True

                if not found_smthg:
                    if not let in {
                        ('t', None, None),
                    } :
                        print('problem', retake, let, '/', phons)

        return res if res else phons

    def fr2katakana(self, text):
        phons = self.phenotic_fr(text)
        return ' '.join([self.phenotic_fr2jap_let(word) for word in phons.split(' ')])