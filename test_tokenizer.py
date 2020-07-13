from tokenizers.implementations import ByteLevelBPETokenizer
from tokenizers.processors import BertProcessing

tokenizer = ByteLevelBPETokenizer(
    "./bert-tokenizer/vocab.json",
    "./bert-tokenizer/merges.txt",
)

from tokenizers.processors import BertProcessing

tokenizer._tokenizer.post_processor = BertProcessing(
    ("</s>", tokenizer.token_to_id("</s>")),
    ("<s>", tokenizer.token_to_id("<s>")),
)
tokenizer.enable_truncation(max_length=512)

### Testing

tokenizer.encode('TOBB ETU NLP&IR team')

