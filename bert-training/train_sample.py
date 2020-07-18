# !pip uninstall -y tensorflow
# # Install `transformers` from master
# !pip install git+https://github.com/huggingface/transformers
# !pip list | grep -E 'transformers|tokenizers'
# # transformers version at notebook update --- 2.11.0
# # tokenizers version at notebook update --- 0.8.0rc1

from pathlib import Path
from tokenizers import ByteLevelBPETokenizer

dpath = 'dataset/sample1000000.txt'

# Initialize a tokenizer
tokenizer = ByteLevelBPETokenizer()

# Customize training
tokenizer.train(files=dpath, vocab_size=52_000, min_frequency=2, special_tokens=[
    "<s>",
    "<pad>",
    "</s>",
    "<unk>",
    "<mask>",
])

# !mkdir bert-model
tokenizer.save_model("bert-model2")

from tokenizers.implementations import ByteLevelBPETokenizer
from tokenizers.processors import BertProcessing


tokenizer = ByteLevelBPETokenizer(
    "./bert-model2/vocab.json",
    "./bert-model2/merges.txt",
)

tokenizer._tokenizer.post_processor = BertProcessing(
    ("</s>", tokenizer.token_to_id("</s>")),
    ("<s>", tokenizer.token_to_id("<s>")),
)
tokenizer.enable_truncation(max_length=512)
tokenizer.encode("Mi estas Julien.")
tokenizer.encode("Mi estas Julien.").tokens

from transformers import RobertaConfig

config = RobertaConfig(
    vocab_size=52_000,
    max_position_embeddings=514,
    num_attention_heads=12,
    num_hidden_layers=6,
    type_vocab_size=1,
)

from transformers import RobertaTokenizerFast
tokenizer = RobertaTokenizerFast.from_pretrained("./bert-model2", max_len=512)

from transformers import RobertaForMaskedLM
model = RobertaForMaskedLM(config=config)

from transformers import LineByLineTextDataset
dataset = LineByLineTextDataset(
    tokenizer=tokenizer,
    file_path=dpath,
    block_size=128,
)

from transformers import DataCollatorForLanguageModeling
data_collator = DataCollatorForLanguageModeling(
    tokenizer=tokenizer, mlm=True, mlm_probability=0.15
)

from transformers import Trainer, TrainingArguments
training_args = TrainingArguments(
    output_dir="./bert-model2",
    overwrite_output_dir=True,
    num_train_epochs=1,
    per_gpu_train_batch_size=64,
    save_steps=10_000,
    save_total_limit=2,
)

trainer = Trainer(
    model=model,
    args=training_args,
    data_collator=data_collator,
    train_dataset=dataset,
    prediction_loss_only=True,
)

trainer.train()

trainer.save_model("./bert-model2")


