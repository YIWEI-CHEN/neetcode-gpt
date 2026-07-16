from typing import List

class Solution:
    def get_merges(self, corpus: str, num_merges: int) -> List[List[str]]:
        # 1. Split corpus into a list of individual characters
        # 2. For each merge step:
        #    a. Count frequency of all adjacent token pairs
        #    b. Find the most frequent pair (break ties lexicographically)
        #    c. Merge all non-overlapping occurrences left to right
        #    d. Record the merge as [token_a, token_b]
        # 3. Return the list of merges performed

        def get_stat(tokens: List[str]) -> Counter:
            counts = {}
            for pair in zip(tokens, tokens[1:]):
                counts[pair] = counts.get(pair, 0) + 1
            return counts
        
        def merge(tokens: List[str], pair: Tuple[str, str]) -> List[str]:
            result = []
            i = 0
            while i < len(tokens):
                if i < len(tokens) - 1 and tokens[i] == pair[0] and tokens[i + 1] == pair[1]:
                    result.append(pair[0] + pair[1])
                    i += 2
                else:
                    result.append(tokens[i])
                    i += 1
            return result

        
        tokens = list(corpus)
        res = []
        for i in range(num_merges):
            if len(tokens) < 2:
                break
            stats = get_stat(tokens)
            best_freq = max(stats.values())
            best_pairs = [pair for pair, val in stats.items() if val == best_freq]
            pair = min(best_pairs)
            res.append([pair[0], pair[1]])
            tokens = merge(tokens, pair)
        
        return res


