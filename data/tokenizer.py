from typing import List, Dict, Tuple


class Solution:
    def get_merges(self, corpus: str, num_merges: int) -> List[List[str]]:
        # 1. Split corpus into a list of individual characters
        # 2. For each merge step:
        #    a. Count frequency of all adjacent token pairs
        #    b. Find the most frequent pair (break ties lexicographically)
        #    c. Merge all non-overlapping occurrences left to right
        #    d. Record the merge as [token_a, token_b]
        # 3. Return the list of merges performed
        
        def get_stats(tokens: List[str]) -> Dict:
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

        chars = list(corpus)
        ans = []

        for _ in range(num_merges):
            if len(chars) < 2:
                break

            stats = get_stats(chars)
            most_freq = max(stats.values())
            best_pairs = [pair for pair, freq in stats.items() if freq == most_freq]
            the_pair = min(best_pairs)

            ans.append([the_pair[0], the_pair[1]])
            chars = merge(chars, the_pair)
        return ans

