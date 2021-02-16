#!/bin/python3
from collections import deque
import copy

def word_ladder(start_word, end_word, dictionary_file='words5.dict'):
    '''
    Returns a list satisfying the following properties:

    1. the first element is `start_word`
    2. the last element is `end_word`
    3. elements at index i and i+1 are `_adjacent`
    4. all elements are entries in the `dictionary_file` file

    For example, running the command
    ```
    word_ladder('stone','money')
    ```
    may give the output
    ```
    ['stone', 'shone', 'phone', 'phony', 'peony', 'penny', 'benny', 'bonny', 'boney', 'money']
    ```
    but the possible outputs are not unique,
    so you may also get the output
    ```
    ['stone', 'shone', 'shote', 'shots', 'soots', 'hoots', 'hooty', 'hooey', 'honey', 'money']
    ```
    (We cannot use doctests here because the outputs are not unique.)

    Whenever it is impossible to generate a word ladder between the two words,
    the function returns `None`.
    '''
    dict = []
    ladder = [start_word]
    if _adjacent(start_word, end_word):
        return [start_word, end_word]
    if start_word == end_word:
        return [start_word]
    with open(dictionary_file, 'r') as f:
        for word in f.readlines():
            dict.append(word.strip('\n'))    
    
    ladders = deque()
    ladders.append(ladder)
    while ladders:
        current_ladder = ladders.popleft()
        for word in set(dict):
            if _adjacent(word, current_ladder[-1]):
                if word == end_word:
                    return current_ladder + [word]
                new_ladder = copy.deepcopy(current_ladder)
                new_ladder.append(word)
                dict.remove(word)
                ladders.append(new_ladder)

def verify_word_ladder(ladder):
    '''
    Returns True if each entry of the input list is adjacent to its neighbors;
    otherwise returns False.

    >>> verify_word_ladder(['stone', 'shone', 'phone', 'phony'])
    True
    >>> verify_word_ladder(['stone', 'shone', 'phony'])
    False
    '''
    if (ladder == []) or (ladder == None):
        return False
    for k, word in enumerate(ladder):
        if k == len(ladder) - 1:
            return True
        else:
            if not _adjacent(word, ladder[k + 1]):
                    return False

def _adjacent(word1, word2):
    '''
    Returns True if the input words differ by only a single character;
    returns False otherwise.

    >>> _adjacent('phone','phony')
    True
    >>> _adjacent('stone','money')
    False
    '''
    diffs = 0
    if len(word1) != len(word2):
        return False
    for k, letter in enumerate(word1):
        if word2[k] != letter:
            diffs += 1
    if diffs == 1:
        return True
    else:
        return False
