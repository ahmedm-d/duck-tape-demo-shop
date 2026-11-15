# Duck Tape demo shop

A public, deliberately imperfect fixture for testing Duck Tape's GitHub import,
repository knowledge, Atlas graph retrieval, knowledge approval, refresh and
live advisory deduplication. It contains no customer code, data or credentials.

## Structure and acceptance contract

- `app.py`: a loopback-only `POST /quote` endpoint and input validation.
- `pricing.py`: shared subtotal and tax calculations.
- `config.py`: currency and tax configuration.
- `tests/test_quote.py`: endpoint/helper/configuration regression coverage.
- `legacy.py`: a dependency to remove when testing refresh and deletion.
- `requirements.lock`: exact, deliberately old versions for OSV scanning.

**Team constraint:** preserve integer-cent arithmetic; never introduce floating
point money. Quantity must be applied before tax, and the public response keeps
the `total_cents` and `currency` fields.

## Intentional bug

The endpoint accepts quantity but `pricing.subtotal_cents()` ignores it. Two
items at 100 cents each with 10% tax should total 220 cents; the current result
is 110 cents. This is an intentional cross-module defect for a later AI repair.

Run the reviewed fixture tests with `python -m unittest discover -s tests -v`.
Expected baseline: three passing tests and one failing quantity regression.
There is no requirement to install dependencies to execute these fixed tests.

The lockfile is advisory test input, not a recommended environment. Actual OSV
findings must retain their source URLs and retrieval timestamps. A version match
does not prove the application is exploitable; it does not use Requests at runtime.

## Refresh journey

The initial commit imports `legacy.py` from the endpoint. A follow-up commit will
remove that file and reference a new `health.py` module, with a small config
change. Duck Tape must show the new commit and graph without current evidence
for the deleted file. The quantity bug stays available for the trained models.

## Scope

This is synthetic, authored test code, not a live customer application. Importing
it into Duck Tape does not authorize arbitrary generated code to run on the host.
Model editing and sandbox verification are separate acceptance gates.
