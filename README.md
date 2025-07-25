# RaiziomFix

A minimal AI plugin marketplace demo with FastAPI backend and React frontend.

## Backend

```bash
cd backend
pip install -r ../requirements.txt
uvicorn app.main:app --reload
```

## Frontend

```bash
cd frontend
npm install
npm start
```

The backend exposes simple authentication endpoints (`/register`, `/login`), plugin listing at `/plugins`, idea handling via `/idea`, and a toy AI endpoint `/ai/respond`.

Use the token returned from `/login` in the `token` query parameter for authenticated routes.
