#!/bin/bash

# You can preload Hugging Face files here if needed

# Start the FastAPI server
uvicorn app.main:app --host 0.0.0.0 --port 10000