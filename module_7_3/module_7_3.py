class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}
        for file_name in self.file_names:
            with open(file_name, 'r', encoding='utf-8') as file:
                words = file.read().lower()
                for i in [',', '.', '=', '!', '?', ';', ':', ' - ']:
                    words = words.replace(i, '')
                all_words[file_name] = words.split()
        return all_words

    def find(self, word):
        word = word.lower()
        all_words = self.get_all_words()
        list_words = {}
        for file_name, words in all_words.items():
            if word in words:
                list_words[file_name] = words.index(word) + 1
        return list_words

    def count(self, word):
        word = word.lower()
        all_words = self.get_all_words()
        word_counts = {}
        for file_name, words in all_words.items():
            word_counts[file_name] = words.count(word)
        return word_counts


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())
print(finder2.find('TEXT'))
print(finder2.count('teXT'))
print()

finder3 = WordsFinder('Mother Goose - Monday’s Child.txt',)
print(finder3.get_all_words())
print(finder3.find('Child'))
print(finder3.count('Child'))
print()

finder4 = WordsFinder('Rudyard Kipling - If.txt',)
print(finder4.get_all_words())
print(finder4.find('if'))
print(finder4.count('if'))
print()

finder5 = WordsFinder('Walt Whitman - O Captain! My Captain!.txt')
print(finder5.get_all_words())
print(finder5.find('captain'))
print(finder5.count('captain'))
