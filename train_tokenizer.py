from pathlib import Path
from tokenizers import ByteLevelBPETokenizer

paths = ['./dataset/oscar.eo.txt']

tokenizer = ByteLevelBPETokenizer()

# Customize training
tokenizer.train(files=paths, vocab_size=52000, min_frequency=2, special_tokens=[
    "<s>",
    "<pad>",
    "</s>",
    "<unk>",
    "<mask>",
])

tokenizer.save_model("./bert-tokenizer")

