import os
import logging
from sentence_transformers import SentenceTransformer
from transformers import AutoTokenizer, AutoModelForCausalLM

def download_models():
    base_dir = os.path.dirname(os.path.abspath(__file__))

    # download and save distilgpt2 generation model + tokenizer if not already downloaded
    gen_model = "distilgpt2"
    gen_model_dir = os.path.join(base_dir, "distilgpt2")
    
    if not os.path.exists(gen_model_dir):
        os.makedirs(gen_model_dir)
        print(f"Downloading distilgpt2 model to {gen_model_dir} ...")
        
        model = AutoModelForCausalLM.from_pretrained(gen_model)
        tokenizer = AutoTokenizer.from_pretrained(gen_model)
        
        model.save_pretrained(gen_model_dir)
        tokenizer.save_pretrained(gen_model_dir)
        
        logging.info(f"Generation model ({gen_model}) downloaded and saved.")


    # download and save sentence-transformers embedding model if not already downloaded
    embed_model = "sentence-transformers/all-MiniLM-L6-v2"
    embed_model_dir = os.path.join(base_dir, embed_model.split("/")[-1])
    
    if not os.path.exists(embed_model_dir):
        os.makedirs(embed_model_dir)
        print(f"Downloading '{gen_model}' to '{embed_model_dir}' ...")
    
        embed_model = SentenceTransformer(gen_model)
        embed_model.save(embed_model_dir)
    
        logging.info(f"Embedding model ({gen_model}) downloaded and saved.")


if __name__ == "__main__":
    download_models()