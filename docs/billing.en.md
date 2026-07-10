# Billing System

English | [繁體中文](billing.md)

## Flow

1. The user runs `/upgrade` in Discord ([app/cogs/billing.py](../app/cogs/billing.py)).
2. `BillingService.create_checkout_session` calls Stripe to create a Checkout Session and returns the payment link.
3. Once payment completes, Stripe fires a `checkout.session.completed` webhook to `POST /webhooks/stripe` ([app/api/routes/webhooks.py](../app/api/routes/webhooks.py)).
4. The webhook handler calls `SubscriptionService.activate`, writing that guild's subscription state to the database.
5. Any subsequent command uses `PermissionService.has_plan()` (via the `require_plan` decorator in [app/core/permissions.py](../app/core/permissions.py)) to decide whether the guild is entitled to a premium feature.

## Plans

Default plans are defined in [scripts/seed_data.py](../scripts/seed_data.py): `free` / `pro` / `enterprise`, each with a `features` JSON column describing available features and limits.

## Cancellation

Stripe's `customer.subscription.deleted` event triggers `SubscriptionService.cancel`, setting the subscription status to `cancelled`; the guild is then treated as being back on the Free plan.
