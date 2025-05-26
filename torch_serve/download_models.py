from transformers import AutoTokenizer, AutoModelForCausalLM
from sentence_transformers import SentenceTransformer

# Download generation model and tokenizer
model_name = "distilgpt2"
AutoModelForCausalLM.from_pretrained(model_name).save_pretrained("/home/model-server/distilgpt2")
AutoTokenizer.from_pretrained(model_name).save_pretrained("/home/model-server/distilgpt2")

# Preload embedding model (cache)
SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")