#!/bin/bash
# 🌱 Raiziomfix Core Engine – To be evolved into Raiziom
set -e

# Load environment variables if present
if [ -f .env ]; then
  export $(grep -v '^#' .env | xargs)
fi

# 🧠 Core logic: part of Raiziom engine
pip install -r requirements.txt
cd frontend && npm install && npm run build && cd ..
uvicorn backend.app.main:app --host 0.0.0.0 --port ${PORT:-8000}
