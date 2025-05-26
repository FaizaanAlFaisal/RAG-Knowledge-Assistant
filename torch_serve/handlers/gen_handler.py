from transformers import AutoTokenizer, AutoModelForCausalLM
from ts.torch_handler.base_handler import BaseHandler
import torch

class GenHandler(BaseHandler):
    def initialize(self, ctx):
        self.device = torch.device("cpu")
        model_dir = ctx.system_properties.get("model_dir")
        self.tokenizer = AutoTokenizer.from_pretrained(model_dir)
        self.model = AutoModelForCausalLM.from_pretrained(model_dir).to(self.device)

    def preprocess(self, data):
        prompt = data[0].get("body")
        if isinstance(prompt, (bytes, bytearray)):
            prompt = prompt.decode("utf-8")
        return self.tokenizer(prompt, return_tensors="pt").to(self.device)

    def inference(self, inputs):
        outputs = self.model.generate(**inputs, max_new_tokens=50, num_beams=2)
        return self.tokenizer.decode(outputs[0], skip_special_tokens=True)

    def postprocess(self, output):
        return {"response": output}
