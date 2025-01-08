import os
import re


class WordsFinder:
    def __init__(self, directory="."):

        self.file_names = self._find_txt_files(directory)

    def _find_txt_files(self, directory):

        found_files = []
        for root, _, files in os.walk(directory):
            for file in files:
                if file.lower().endswith(".txt"):
                    found_files.append(os.path.join(root, file))
        return found_files

    def get_all_words(self):
        all_words = {}
        punctuation = r"[,.!=?;:-]"
        for file_name in self.file_names:
            try:
                with open(file_name, 'r', encoding='utf-8') as f:
                    all_text = f.read().lower()
                    words = re.sub(punctuation, '', all_text).replace(" - ", " ").split()
                    all_words[file_name] = words
            except FileNotFoundError:
                continue
        return all_words

    def find(self, word):

        word = word.lower()
        results = {}
        for name, words in self.get_all_words().items():
            try:
                results[name] = words.index(word) + 1
            except ValueError:
                results[name] = None
        return results

    def count(self, word):

        word = word.lower()
        results = {}
        for name, words in self.get_all_words().items():
            results[name] = words.count(word)
        return results


finder3 = WordsFinder(".")
print(finder3.get_all_words())
print(finder3.find("TEXT"))
print(finder3.count("teXT"))
