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