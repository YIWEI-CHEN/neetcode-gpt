import torch
import torch.nn as nn
from torchtyping import TensorType
from typing import List

class Solution:
    def get_dataset(self, positive: List[str], negative: List[str]) -> TensorType[float]:
        # 1. Build vocabulary: collect all unique words, sort them, assign integer IDs starting at 1
        # 2. Encode each sentence by replacing words with their IDs
        # 3. Combine positive + negative into one list of tensors
        # 4. Pad shorter sequences with 0s using nn.utils.rnn.pad_sequence(tensors, batch_first=True)
        sentences = positive + negative
        if not sentences:
            return torch.empty((0, 0), dtypes=torch.float32)
        
        vocabulary = sorted({
            word
            for sentence in sentences
            for word in sentence.split()
        })

        word2id = {
            word: token_id
            for token_id, word in enumerate(vocabulary, start=1)
        }

        encoded = [
            torch.tensor([word2id[word] for word in sentence.split()], dtype=torch.float32)
            for sentence in sentences
        ]

        return nn.utils.rnn.pad_sequence(
            encoded,
            batch_first=True,
            padding_value=0.0
        )
