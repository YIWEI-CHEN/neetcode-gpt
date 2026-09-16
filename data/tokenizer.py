from typing import List, Tuple
from collections import Counter

class Solution:
    def get_merges(self, corpus: str, num_merges: int) -> List[List[str]]:
        # 1. Split corpus into a list of individual characters
        # 2. For each merge step:
        #    a. Count frequency of all adjacent token pairs
        #    b. Find the most frequent pair (break ties lexicographically)
        #    c. Merge all non-overlapping occurrences left to right
        #    d. Record the merge as [token_a, token_b]
        # 3. Return the list of merges performed
        
        def get_stats(tokens: List[str]) -> Counter:
            counts = Counter()
            for pair in zip(tokens, tokens[1:]):
                counts[pair] += 1
            return counts

        def merge(tokens: List[str], pair: Tuple[str, str]) -> List[str]:
            res = []
            i = 0
            while i < len(tokens):
                if i < len(tokens) and tokens[i] == pair[0] and tokens[i + 1] == pair[1]:
                    res.append(pair[0] + pair[1])
                    i += 2
                else:
                    res.append(tokens[i])
                    i += 1
            return res
            
                

        tokens = list(corpus)
        res = []

        for _ in range(num_merges):
            if len(tokens) < 2:
                break
            
            stats = get_stats(tokens)
            best_freq = max(stats.values())
            best_pairs = [pair for pair, freq in stats.items() if freq == best_freq]

            selected = min(best_pairs)
            res.append([selected[0], selected[1]])

            tokens = merge(tokens, selected)

        return res
