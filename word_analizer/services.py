import math
from typing import Any, Dict, List

import nltk
from nltk import RegexpTokenizer, pos_tag
from nltk.corpus import stopwords
from nltk.probability import FreqDist
from nltk.stem import SnowballStemmer, WordNetLemmatizer
from nltk.tokenize import word_tokenize


nltk.download("stopwords")
stop_words = set(stopwords.words("english"))


def remove_punctuation_and_tockenize(text: str) -> str:
    """Removes punctutation signs from the text, makes it lower case and tokenizes it."""
    text = text.lower()
    tokenizer = RegexpTokenizer(r"\w+")
    return tokenizer.tokenize(text)


def remove_stop_words(text):
    """Removes english stop words such as ['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', "you're", "you've", "you'll"] """
    return [w for w in remove_punctuation_and_tockenize(text) if not w in stop_words]


def create_freqdist(text):
    """Creates a FreqDict of a given list of tokenized words."""
    return FreqDist(remove_stop_words(text)).items()


def max_freq(text):
    """Gets the biggest word frequency in the text"""
    return max([freq for _, freq in create_freqdist(text)])


def calc_most_freq(text):
    """Finds most frequent words (if percerntage of frequency is more than 67%) in the text."""
    return {
        word: freq
        for word, freq in create_freqdist(text)
        if freq / max_freq(text) >= 0.67
    }


def avg_freq(text):
    """Finds average frequent words (if percerntage of frequency is more than 34% but less than 66%) in the text."""
    return {
        word: freq
        for word, freq in create_freqdist(text)
        if freq / max_freq(text) <= 0.66 and freq / max_freq(text) >= 0.34
    }


def calc_least_freq(text):
    """Finds least frequent words (if percerntage of frequency is less than 34%) in the text."""
    return {
        word: freq
        for word, freq in create_freqdist(text)
        if freq / max_freq(text) <= 0.33
    }
