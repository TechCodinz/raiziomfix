# RaiziomFix

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
