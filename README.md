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
AI Plugin Marketplace

## Payments

The project includes a simple Stripe integration to create checkout sessions for
purchasing credits. Configure the following environment variables in your `.env`
file:

```
STRIPE_SECRET_KEY=sk_test_your_key
STRIPE_PUBLIC_KEY=pk_test_your_key
STRIPE_PRICE_ID=price_id_from_stripe
FRONTEND_URL=http://localhost:3000
```

Run the backend with these variables and the dashboard will provide a **Buy
Credits** button that redirects to Stripe Checkout.
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
