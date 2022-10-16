import torch
from transformers import T5Tokenizer, T5ForConditionalGeneration, T5Config
import time 


def summarizer(text):

    start = time.time()

    model = T5ForConditionalGeneration.from_pretrained('t5-small')
    tokenizer = T5Tokenizer.from_pretrained('t5-small')
    device = torch.device('cpu')


    preprocess_text = text.strip().replace("\n","")
    t5_prepared_Text = "summarize: " + preprocess_text
    #print ("original text preprocessed: \n", preprocess_text)

    tokenized_text = tokenizer.encode(t5_prepared_Text, return_tensors="pt").to(device)


    # summmarize 
    summary_ids = model.generate(tokenized_text,
                                    num_beams=4,
                                    no_repeat_ngram_size=2,
                                    min_length=30,
                                    max_length=100,
                                    early_stopping=True)

    output = tokenizer.decode(summary_ids[0], skip_special_tokens=True)

    output = output.strip()
    output = output.capitalize()

    end = time.time()
    ts = end -start
    ts = round(ts,4)
    output = output + '.\n\nThe length of the Original Text entered = ' + str(len(text)) + '\nThe length of the Summarized Text = ' + str(len(output))
    output = output + '\nTime of execution = ' + str(ts) + 's'

   #print("\n\nSummarized text: \n",output)
    return output

