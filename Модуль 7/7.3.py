import string

class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}

        for file_name in self.file_names:
            try:
                with open(file_name, 'r', encoding='utf-8') as file:
                    content = file.read().lower()
                    translator = str.maketrans('', '', string.punctuation.replace('-', ''))
                    content = content.translate(translator)
                    words = content.split()
                    all_words[file_name] = words
            except FileNotFoundError:
                print(f"Файл {file_name} не найден.")

        return all_words

    def find(self, word):
        word = word.lower()
        results = {}
        all_words = self.get_all_words()

        for file_name, words in all_words.items():
            if word in words:
                results[file_name] = words.index(word) + 1

        return results

    def count(self, word):
        word = word.lower()
        results = {}
        all_words = self.get_all_words()

        for file_name, words in all_words.items():
            results[file_name] = words.count(word)

        return results


finder2 = WordsFinder('../file1.txt')
print(finder2.get_all_words())
print(finder2.find('TEXT'))
print(finder2.count('teXT'))
