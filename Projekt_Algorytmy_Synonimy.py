from nltk.corpus import wordnet
from translate import Translator


def translate_to_language(text, language):
    translator = Translator(to_lang=language)
    translation = translator.translate(text)
    return translation

def get_synonyms_antonyms(word, language='eng'):
    synonyms = set()
    antonyms = set()

    synsets = wordnet.synsets(word, lang=language)
    for syn in synsets:
        for lemma in syn.lemmas():
            synonyms.add(lemma.name())
            if lemma.antonyms():
                antonyms.add(lemma.antonyms()[0].name())

    return synonyms, antonyms

def get_examples(word, language='eng'):
    examples = []

    synsets = wordnet.synsets(word, lang=language)
    for syn in synsets:
        examples.extend(syn.examples())

    return examples

def classify_word(word, language='eng'):
    synsets = wordnet.synsets(word, lang=language)
    if synsets:
        return synsets[0].pos()
    else:
        return None

def get_full_class_name(word, language='eng'):
    synsets = wordnet.synsets(word, lang=language)
    if synsets:
        pos_tag = synsets[0].pos()
        pos_map = {
            'n': 'rzeczownik',
            'v': 'czasownik',
            'r': 'przysłówek',
            'a': 'przymiotnik'
        }
        return pos_map.get(pos_tag, 'nieznane')
    else:
        return None

def znajdz_synonimy(slowo):
    synonimy = set()
    for synset in wordnet.synsets(slowo, lang='pol'):
        for lemma in synset.lemmas('pol'):
            synonimy.add(lemma.name())
    return synonimy

def znajdz_antonimy(slowo):
    antonimy = set()
    for synset in wordnet.synsets(slowo, lang='pol'):
        for lemma in synset.lemmas('pol'):
            if lemma.antonyms():
                antonimy.add(lemma.antonyms()[0].name())
    return antonimy

def main():
    exit_program = False
    while True:
        language = input("\nPodaj język ('eng' dla angielskiego, 'pol' dla polskiego): ")
        if language in ['eng', 'pol']:
            break
        print("Błąd: Niepoprawny język. Wybierz 'eng' lub 'pol'.")

    while True and not exit_program:
        word = input("Podaj słowo lub wyrażenie (lub 'exit' aby zakończyć): ")
        if word.lower() == 'exit':
            break

        while True:
            synonyms, antonyms = get_synonyms_antonyms(word, language)
            examples = get_examples(word, language)
            word_class = classify_word(word, language)
            full_class_name = get_full_class_name(word, language)

            if language == 'pol':
                synonyms = znajdz_synonimy(word)
                antonyms = znajdz_antonimy(word)

            print("\nSynonimy:", synonyms)
            print("Antonimy:", antonyms)
            print("Przykłady użycia:", examples)
            print("Klasa gramatyczna:", full_class_name)

            next_search = input("Czy chcesz wyszukać kolejne słowo? (Tak/Nie): ")
            if next_search.lower() != 'tak':
                exit_program = True
                break

            change_language = input("Czy chcesz zmienić język? (Tak/Nie): ")
            if change_language.lower() == 'tak':
                while True:
                    language = input("\nPodaj język ('eng' dla angielskiego, 'pol' dla polskiego): ")
                    if language in ['eng', 'pol']:
                        break
                    print("Błąd: Niepoprawny język. Wybierz 'eng' lub 'pol'.")

            word = input("Podaj kolejne słowo lub wyrażenie: ")

if __name__ == "__main__":
    main()