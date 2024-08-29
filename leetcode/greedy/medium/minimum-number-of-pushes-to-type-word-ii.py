from itertools import batched

def minimumPushes(word: str) -> int:
    # represent counts/freqs of characters in [word]
    counts = [0] * 26  # a -> z (0 -> 26)
    ASCII_A = ord('a')
    for c in word:
        counts[ord(c) - ASCII_A] += 1
    
    counts.sort(reverse=True)

    total_taps = 0
    for taps, chunk in enumerate(batched(counts, 8), 1):
        # [taps] for characters-freqs in [chunk]
        total_taps += sum(map(lambda cnt: cnt * taps, chunk))

    return total_taps 

def minimumPushes_v2(word: str) -> int:
    # represent counts/freqs of characters in [word]
    counts = [0] * 26  # a -> z (0 -> 26)
    ASCII_A = ord('a')
    for c in word:
        counts[ord(c) - ASCII_A] += 1
    
    counts.sort(reverse=True)

    total_taps = 0
    # 8 is max unique button char can be mapped to
    for i, count in enumerate(counts):
        taps = (i // 8) + 1 # no of taps for a char with freqs = [count] 
        total_taps +=  count * taps 
    
    return total_taps

    
arr = 'abcde' 
print(minimumPushes(arr))