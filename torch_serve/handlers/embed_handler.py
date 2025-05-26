from ts.torch_handler.base_handler import BaseHandler
from sentence_transformers import SentenceTransformer

class EmbeddingHandler(BaseHandler):
    def initialize(self, ctx):
        self.model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

    def preprocess(self, data):
        text = data[0].get("body")
        if isinstance(text, (bytes, bytearray)):
            text = text.decode("utf-8")
        return text

    def inference(self, text):
        embedding = self.model.encode([text])[0]
        return embedding.tolist()

    def postprocess(self, result):
        return {"embedding": result}
