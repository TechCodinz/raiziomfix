# RaiziomFix

AI Plugin Marketplace

## Credit Based System

The backend includes a very small in-memory wallet implementation. New users
receive trial credits when they sign up. Credits are deducted for every agent
action via the `/action` endpoint. Users can inspect their wallet balance and
transaction logs using `/wallet/{email}` and `/earnings/{email}`.

Funds can be added using `/add_funds` with a payment provider of `paystack` or
`stripe`. If environment variables `PAYSTACK_KEY` or `STRIPE_KEY` are not
supplied the payment call is mocked but credits are still granted, making the
system usable without real payment keys.

### Running Locally

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8000 --app-dir backend/app
```

### Example Usage

```bash
# sign up
curl -X POST http://localhost:8000/signup -H 'Content-Type: application/json' \
  -d '{"email":"user@example.com","password":"pass"}'

# perform an action costing credits
curl -X POST http://localhost:8000/action -H 'Content-Type: application/json' \
  -d '{"email":"user@example.com","action":"run-agent"}'

# add more credits (mocked if keys are missing)
curl -X POST http://localhost:8000/add_funds -H 'Content-Type: application/json' \
  -d '{"email":"user@example.com","amount":5,"provider":"paystack"}'

# view wallet balance
curl http://localhost:8000/wallet/user@example.com
```
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
