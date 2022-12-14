import re
import nltk 
nltk.download('punkt')

from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize, sent_tokenize

def get_subwords_span(substring_list, fullstring_list):
    clean_stems = []
    for (substring, fullstring) in list(zip(substring_list, fullstring_list)):
        if substring.isalpha():
            match = re.match(substring, fullstring)
            if match is not None:
                clean_stems.append(re.match(substring, fullstring).span())
            else:
                clean_stems.append((0, len(substring)-1))
        else:
            clean_stems.append((0, len(substring)))
    return clean_stems

def speed_read_by_words(full_text:str):
    ps = PorterStemmer()
    words = word_tokenize(full_text.replace('"', '\\"'))
    words_stems = [ps.stem(word, to_lowercase=False) for word in words]
    substring_span = get_subwords_span(words_stems, words)

    bold_text = []
    for i, (start, end) in enumerate(substring_span):
        word = words[i]
        if word[start:end].isalpha():
            bold_text.append('**' + word[start:end] + '**' + word[end:])
        else:
            bold_text.append(words[i][start:end])
    return " ".join(bold_text).replace('\\', '')

def speed_read_by_sentence(full_text:str):

    # Tokenize the full text into sentences
    text_sentences = sent_tokenize(full_text)

    ## Run speed reading over sentences and return the result
    return "\n\n".join(
        [
            speed_read_by_words(sentence) for sentence in text_sentences
        ]
    )