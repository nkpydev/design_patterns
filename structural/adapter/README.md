# Adapter Pattern

## Purpose:
Allow incompatible interfaces to work together, ex. Payment Gateways

## Scenario:
- Your old sytem uses 'Paypal Gateway'
- New system uses 'Razorpay Gateway'

## When to use
- Switching vendors
- Migrating systems with different APIs
- Avoiding rewriting of the existing client code

## How it works?
- The 'Payment Adapter' wraps 'RazorPayGateway' and exposes the 'process_payment(amount)' method to the client.

## Example Output:
```cmd
Old Method - Paypal
Processing payment of: 499.99 via Paypal!
New Method - Rayzorpay
Processing payment of: 799.99 via Rayzorpay!
```