#!/usr/bin/python3

def best_score(a_dictionary):
    if not a_dictionary:
        return None

    max_val = max(a_dictionary.values())
    best_key = [key for key, value in a_dictionary.items() if value == max_val]

    if len(best_key) == 1:
        return best_key[0]
    else:
        return None
