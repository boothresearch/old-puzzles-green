def find_anagrams(word, candidates):
    result = []
    word_sorted = sorted(word.lower())
    for i in range(len(candidates)):
        if word.lower() != candidates[i].lower() and word_sorted == sorted(candidates[i].lower()):
            result.append(candidates[i])
    return result
