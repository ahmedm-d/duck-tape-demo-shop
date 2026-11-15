# Duck Tape demo shop

Public, deliberately imperfect fixture. No customer code or credentials. Do not deploy.
Tests and the loopback-only HTTP endpoint use the Python standard library.

## Call graph

app.quote_handler -> receipt.build_receipt -> pricing.total_cents -> coupons.apply_coupon.
Pricing/coupons read config; receipt reads metadata, which reads config and health.

## Team constraints

- Money uses integer cents, never floats.
- WELCOME10 discounts the quantity-adjusted subtotal by 10 percent before tax.
- Round discount down to whole cents; apply configured tax and round tax down too.
- Preserve total_cents, currency and label. Unknown coupons must be rejected.
- Omitted coupons preserve behavior. Preserve item validation and the 100-line limit.

## Intentional coupon defect

PR #1 fixed quantity; its repair and regressions remain. The new coupon incorrectly
subtracts ten cents. The 100-cent smoke case passes because ten percent is ten cents.
The missing large/small subtotal coverage is deliberate.

Input: {"items":[{"price_cents":1000,"quantity":2}],"coupon":"WELCOME10"}
Current total_cents: 2189. Required: 1980 (2000 - 200 discount + 180 tax).
A one-cent subtotal stays one cent: its rounded-down discount and tax are zero.

Use a real model repair with new failing-before/passing-after regression tests.
No fixture model response or pre-applied coupon repair is supplied.

## Baseline and advisory input

Run: python -m unittest discover -s tests -v
Expected baseline: nine passing tests. CI runs the same command.
requirements.lock is deliberately old advisory-matching input, not installed by CI.
The application does not import Requests at runtime. An affected version does not
establish exploitability. Keep actual OSV source URLs and timestamps visible.

## Staged demo PRs

A separate unsafe receipt-preview PR is for cited, read-only model review. Keep it
unmerged. Its escaping regression deliberately fails; do not execute HTML payloads.
A second PR replaces health.py with service_identity.py. Merge only when the
presenter reaches graph refresh. Refresh the Duck Tape index to see new/deleted
source and edges, with previous snapshots retained as historical evidence.

Imported/model-generated source executes only in Duck Tape's approved sandbox.
