from celery import Celery
from core.config import settings

gen_worker_app = Celery(
    "gen_worker",
    broker=settings.REDIS_URL,
    backend=settings.REDIS_URL,
)

generation_model = None
generation_tokenizer = None

@gen_worker_app.task
def generate_text(prompt: str, model_name: str = "distilgpt2") -> str:
    """Generate text using a specified model."""
    global generation_model, generation_tokenizer

    if generation_model is None or generation_tokenizer is None:
        from transformers import AutoModelForCausalLM, AutoTokenizer
        generation_model = AutoModelForCausalLM.from_pretrained(model_name)
        generation_tokenizer = AutoTokenizer.from_pretrained(model_name)

    inputs = generation_tokenizer(prompt, return_tensors="pt")
    outputs = generation_model.generate(**inputs)
    generated_text = generation_tokenizer.decode(outputs[0], skip_special_tokens=True)

    return generated_text