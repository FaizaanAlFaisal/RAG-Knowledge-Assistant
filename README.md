# RAG-Knowledge-Assistant

A lightweight Retrieval-Augmented Generation (RAG) knowledge assistant built with Python and pgvector for vector search, and a Next.js frontend using shadcn UI components.



## Overview

This project combines retrieval-based information access with generative text capabilities to build a smart knowledge assistant. It uses:

- **Python backend** for embedding, retrieval, and generation
- **pgvector** for efficient vector similarity search inside PostgreSQL
- **Default pretrained models** for embedding and generation:
  - Embedding: `sentence-transformers/all-MiniLM-L6-v2`
  - Generation: `distilgpt2`
- **Next.js frontend** built with [shadcn UI](https://ui.shadcn.com/) for a clean, responsive interface


## Features

- Embed and store documents with a small chat history in PostgreSQL using pgvector
- Retrieve relevant knowledge with vector similarity search
- Generate responses conditioned on retrieved documents
- Lightweight, fast, and easy to deploy
