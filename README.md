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
