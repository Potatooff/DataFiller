import torch
from transformers import PegasusForConditionalGeneration, PegasusTokenizer
model_name = 'tuner007/pegasus_paraphrase'
torch_device = 'cuda' if torch.cuda.is_available() else 'cpu'
tokenizer = PegasusTokenizer.from_pretrained(model_name)
model = PegasusForConditionalGeneration.from_pretrained(model_name).to(torch_device)


# input text is the text you want to change keeping the same meaning
# Return sequence is how many sentence of the same meaning you want to create (it has its limit)
# num beans is like the diversity of the meaning The higher it is the more lost it can get the less it is the more accurate it can be
def get_response(input_text,num_return_sequences,num_beams):  
  batch = tokenizer([input_text],truncation=True,padding='longest',max_length=200, return_tensors="pt").to(torch_device)
  translated = model.generate(**batch,max_length=150,num_beams=num_beams, num_return_sequences=num_return_sequences, temperature=1)  # temperature is if you want the bot to be more create set it more than 5 else dont change
  tgt_text = tokenizer.batch_decode(translated, skip_special_tokens=True)
  return tgt_text

# Code found from hugging face!

