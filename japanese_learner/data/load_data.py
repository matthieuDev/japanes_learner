import json, japanese_learner

data_folder = f'{japanese_learner.__path__[0]}/data/'
def load_hiragana2letter() :
    save_file = data_folder + 'hiragana2letter.json'
    with open (save_file, encoding='utf8') as f :
        hiragana2letter = json.load(f)
    return hiragana2letter

def load_katakana2letter() :
    save_file = data_folder + 'katakana2letter.json'
    with open (save_file, encoding='utf8') as f :
        katakana2letter = json.load(f)
    return katakana2letter

translater2letter_loader = {
    'hiragana' : load_hiragana2letter,
    'katakana' : load_katakana2letter,
}

def load_most_used_words_fr() :
    with open (data_folder + 'most_used_words_fr.json', encoding='utf8') as f :
        most_used_words = json.load(f)
    return most_used_words