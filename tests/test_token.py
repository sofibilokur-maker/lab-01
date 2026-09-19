"""Тести для tokenize()."""
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from findex.tokenizer import tokenize


def test_basic_words():
    assert list(tokenize("Hello world")) == ["hello", "world"]


def test_apostrophe_inside_word():
    assert list(tokenize("don't stop")) == ["don't", "stop"]


def test_hyphen_inside_word():
    assert list(tokenize("mother-in-law visits")) == ["mother-in-law", "visits"]


def test_numbers_integer():
    assert list(tokenize("I have 42 apples")) == ["i", "have", "42", "apples"]


def test_numbers_decimal():
    assert list(tokenize("pi is 3.14 approx")) == ["pi", "is", "3.14", "approx"]


def test_punctuation_stripped():
    assert list(tokenize("Wow! Really? Yes.")) == ["wow", "really", "yes"]


def test_quotes_around_word_stripped():
    # апостроф на межі слова (лапки) не входить у токен
    assert list(tokenize("she said 'hello' to him")) == ["she", "said", "hello", "to", "him"]


def test_unicode_normalization():
    # NFKC: повноширинна цифра → звичайна
    assert list(tokenize("\uff11\uff12\uff13")) == ["123"]


def test_empty_string():
    assert list(tokenize("")) == []


def test_mixed_case():
    assert list(tokenize("HeLLo WORLD")) == ["hello", "world"]