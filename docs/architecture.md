# SignalLedger Architecture

SignalLedger is structured as a small number of explicit layers so each stage of the trading research lifecycle can be tested independently.

## Source Ingestion

The ingestion layer polls or streams public primary sources and stores the raw source payloads with reliable timestamps.

Examples:
- SEC EDGAR filings
- investor relations press releases
- earnings transcripts
- macro and regulatory calendars

Key responsibilities:
- source-specific adapters
- request throttling and retries
- raw document storage
- source timestamps and fetch timestamps

## Data Quality

Before a document becomes a signal candidate, SignalLedger should validate:
- duplicate documents
- missing sections or truncated content
- delayed publication timestamps
- malformed or partial payloads

This layer protects the research stack from subtle data leakage and timestamp errors.

## Normalization and Event Store

Raw inputs are converted into a shared event model. Every event should have enough structure to support replay, backtesting, and auditability.

Core normalized fields:
- source
- published timestamp
- ingested timestamp
- entity
- event type
- raw text
- extracted metadata

This becomes the event ledger that the rest of the system reads from.

## Event Extraction

Extraction identifies what happened.

Examples:
- guidance raise or cut
- offering announcement
- executive departure
- buyback authorization
- merger or acquisition
- litigation or regulatory action

This layer should start with explicit, testable logic before adding more flexible model-based extraction.

## Signal Scoring

Scoring estimates whether the extracted event might be tradable.

Representative dimensions:
- novelty
- expected direction
- expected magnitude
- confidence
- liquidity suitability

The output is a ranked event, not a guaranteed trade.

## Research and Validation

This layer measures whether the proposed signals actually work.

Required checks:
- event studies by horizon
- walk-forward validation
- leakage checks
- regime sensitivity
- performance after fees, spread, and slippage

If the signal does not survive realistic assumptions, it should not advance.

## Paper Trading and Execution

Paper trading should come before any live deployment.

Execution concerns:
- position sizing
- market and limit order behavior
- liquidity constraints
- latency tracking
- trade logging

Live execution should only reuse already-validated research logic.

## Monitoring and Attribution

Once orders exist, SignalLedger should explain performance rather than just report it.

Useful outputs:
- net PnL after costs
- hit rate and drawdown
- fill quality
- source-level contribution
- post-trade attribution by event type

The goal is not just to make predictions, but to understand why the system performs the way it does.
