FROM pytorch/torchserve:latest-cpu

RUN pip install --no-cache-dir transformers sentence-transformers

COPY handlers/ /home/model-server/custom_handlers/
COPY download_models.py /home/model-server/

RUN python /home/model-server/download_models.py

RUN torch-model-archiver \
    --model-name embed \
    --handler custom_handlers/embed_handler.py \
    --extra-files custom_handlers/embed_handler.py \
    --export-path model_store \
    --force && \
  torch-model-archiver \
    --model-name gen \
    --handler custom_handlers/gen_handler.py \
    --extra-files custom_handlers/gen_handler.py \
    --model-file-path /home/model-server/distilgpt2 \
    --serialized-file none \
    --export-path model_store \
    --force

COPY config.properties /home/model-server/

CMD ["torchserve", "--start", "--model-store", "model_store", "--models", "gen=gen.mar,embed=embed.mar", "--ts-config", "/home/model-server/config.properties"]
