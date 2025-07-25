
#!/bin/bash
set -e

# Load environment variables if .env exists
if [ -f .env ]; then
  export $(grep -v '^#' .env | xargs)
fi

# Start backend
uvicorn backend.app.main:app --host 0.0.0.0 --port ${PORT:-8000} &
BACKEND_PID=$!

# Build frontend
cd frontend
npm install
npm run build
cd ..

wait $BACKEND_PID
#!/bin/sh
pip install -r requirements.txt
uvicorn backend/app/main:app --host 0.0.0.0 --port 8000
