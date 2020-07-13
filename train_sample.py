from pathlib import Path
from tokenizers import ByteLevelBPETokenizer
import logging

logging.info('start .... ')

paths = ['./tmp_data.txt']

# Initialize a tokenizer
"""bwpt = BertWordPieceTokenizer(
    unk_token='[UNK]',
    sep_token='[SEP]',
    cls_token='[CLS]',
    clean_text=True,
)"""

tokenizer = ByteLevelBPETokenizer()

# Customize training
tokenizer.train(files=paths, vocab_size=52_000, min_frequency=2, special_tokens=[
    "<s>",
    "<pad>",
    "</s>",
    "<unk>",
    "<mask>",
])

"""
bwpt.train(
    files=paths,
    vocab_size=30000,
    min_frequency=3,
    limit_alphabet=1000,
    special_tokens=['[PAD]', '[UNK]', '[CLS]', '[MASK]', '[SEP]']
)
"""

# tokenizer.save_model("./bert-tokenizer", "sms-model")

tokenizer.save_model("bert-tokenizer")

logging.info('saved tokenizer model .... ')

"""
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

# testing

"""

from transformers import RobertaConfig

config = RobertaConfig(
    vocab_size=52_000,
    max_position_embeddings=514,
    num_attention_heads=12,
    num_hidden_layers=6,
    type_vocab_size=1,
)

from transformers import RobertaTokenizerFast

tokenizer = RobertaTokenizerFast.from_pretrained("./bert-tokenizer", max_len=512)

from transformers import RobertaModel

model = RobertaModel(config=config)

from transformers import LineByLineTextDataset

dataset = LineByLineTextDataset(
    tokenizer=tokenizer,
    file_path="./tmp_data.txt",
    block_size=128,
)

from transformers import DataCollatorForLanguageModeling

data_collator = DataCollatorForLanguageModeling(
    tokenizer=tokenizer, mlm=True, mlm_probability=0.15
)

from transformers import Trainer, TrainingArguments

training_args = TrainingArguments(
    output_dir="./bert-model",
    overwrite_output_dir=True,
    num_train_epochs=1,
    per_gpu_train_batch_size=64,
    save_steps=10000,
    save_total_limit=2,
)

trainer = Trainer(
    model=model,
    args=training_args,
    data_collator=data_collator,
    train_dataset=dataset,
    prediction_loss_only=True,
)

logging.info('training model .... ')

trainer.train()

trainer.save_model("./bert-model")

logging.info('model saved .... ')

