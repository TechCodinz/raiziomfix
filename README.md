# RaiziomFix

RaiziomFix is a simple demo of a marketplace with a FastAPI backend and a React frontend.
It includes a minimal assistant widget and example API endpoints.

## Requirements
- Python 3.11+
- Node.js 18+

## Setup
1. Install backend dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Install frontend dependencies and build:
   ```bash
   cd frontend
   npm install
   npm run build
   cd ..
   ```
3. Copy `.env.example` to `.env` and set your values.

## Running locally
Start the backend and frontend for development:
```bash
cd frontend
npm run dev
```
The React app will run on port 3000 and the FastAPI server on port 8000.

## Deployment
You can deploy using the provided `Dockerfile`, `render.yaml`, or `Procfile`.
A helper script `deploy.sh` builds the frontend and launches the backend with `uvicorn`.

## License
This project is licensed under the MIT License.
