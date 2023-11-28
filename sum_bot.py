import torch
from transformers import AutoTokenizer, AutoModelWithLMHead

tokenizer=AutoTokenizer.from_pretrained('T5-base')
model=AutoModelWithLMHead.from_pretrained('T5-base', return_dict=True)

def break_into_lists(text, max_words_per_list=512):
    result_lists = []

    for i in range(0, len(text), max_words_per_list):
        result_lists.append(''.join(text[i:i + max_words_per_list]))

    return result_lists

def summarize(sequence):

    """
    We'll have to calc a good minimum length for summarization
    """
    if len(sequence) < 100:
        return 'Input is below minimum length. '
    
    max_length = int(0.75*len(list(sequence)))
    #min_length = int(0.5*len(list(sequence)))
    
    if len(list(sequence)) > 512:
        sequence_list = break_into_lists(sequence)
        
        final_output = ""
        
        for l in sequence_list:
            s = ''
            for x in l:
                s += x
                
            inputs=tokenizer.encode("summarize" + s,return_tensors='pt', max_length=512, truncation=True)
            output = model.generate(inputs, min_length=10, max_length=100)

            #summary=tokenizer.decode(output[0], skip_special_tokens=True)
            """We'll Have to clean the output here."""
            cleaned_output = ' '.join(tokenizer.decode(output[0]).split())
            processed_string = cleaned_output.replace("  ", " ")
            final_output += processed_string
            
        return final_output
            
    inputs=tokenizer.encode("summarize" +sequence,return_tensors='pt', max_length=512, truncation=True)
    output = model.generate(inputs, min_length=min_length, max_length=max_length)

    #summary=tokenizer.decode(output[0], skip_special_tokens=True)
    """We'll Have to clean the output here."""
    cleaned_output = ' '.join(tokenizer.decode(output[0]).split())
    processed_string = cleaned_output.replace("  ", " ")
    
    return processed_string

