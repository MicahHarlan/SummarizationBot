import torch
from transformers import AutoTokenizer, AutoModelWithLMHead

tokenizer=AutoTokenizer.from_pretrained('T5-base')
model=AutoModelWithLMHead.from_pretrained('T5-base', return_dict=True)

def summarize(sequence):

    """
    We'll have to calc a good minimum length for summarization
    """
    inputs=tokenizer.encode("summarize" +sequence,return_tensors='pt', max_length=512, truncation=True)
    output = model.generate(inputs, min_length=80, max_length=100)

    summary=tokenizer.decode(output[0],)
    """We'll Have to clean the output here."""
    return summary

