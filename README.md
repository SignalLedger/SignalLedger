# SignalLedger

SignalLedger is an event-driven quant research project focused on turning public primary sources into structured market signals.

The project is designed to ingest machine-readable market catalysts, convert them into normalized events, score their expected impact, and evaluate whether they remain profitable after realistic trading costs and risk controls.

## What SignalLedger Does

- ingests public primary sources such as SEC filings, investor relations releases, transcripts, and macro calendars
- normalizes raw documents into timestamped event records
- extracts event type, entity, and supporting metadata into a reusable event ledger
- scores events for novelty, direction, confidence, and expected magnitude
- runs event studies, backtests, and paper portfolios before any live deployment
- enforces risk controls so research PnL is not confused with deployable profit

## Why It Has a Competitive Advantage

SignalLedger is designed to compete on process quality rather than on vague claims of having a magic prediction model.

- It starts with primary sources instead of delayed commentary. SEC filings, investor relations releases, transcripts, and regulatory documents often contain market-moving information before that information is fully summarized by financial media.
- It converts raw documents into a structured event ledger. That creates a reusable history of what happened, when it happened, and how the market reacted, which is more defensible than a one-off sentiment score.
- It measures signal quality with timestamps, validation, and attribution. Many hobby trading bots stop at prediction; SignalLedger is built to test whether the signal survives latency, slippage, spread, and changing market regimes.
- It focuses on event types where speed and structure matter. A system that consistently detects offerings, guidance changes, executive departures, or regulatory actions can outperform slower discretionary workflows.
- It treats risk control as part of the edge. A weaker raw signal with disciplined sizing and deployment rules can outperform a stronger-looking signal that ignores execution reality.
- It can improve over time as coverage expands. Every new source adapter, normalized event type, and post-trade review makes the system more useful without changing the core architecture.

The intended edge is not secret information. The intended edge is faster ingestion, better structuring, tighter validation, and more disciplined execution on public or properly licensed information.

## Workflow

Core workflow:
- ingest primary sources such as SEC filings, investor relations releases, and transcripts
- normalize them into timestamped events
- classify and score event impact
- simulate and paper trade decisions under realistic cost assumptions
- review PnL, risk, and post-trade attribution before any live deployment

Project workflow diagram: `docs/workflow.mmd`

## Repo Layout

- `docs/workflow.mmd`: end-to-end Mermaid workflow diagram
- `docs/architecture.md`: system components and data flow
- `docs/pnl-model.md`: how expected value, costs, and deployment fit together
- `src/signalledger/`: starter Python package for core project models
- `tests/`: starter tests for the package scaffold

## Getting Started

1. Use Python 3.11 or newer.
2. Create a virtual environment.
3. Install the package in editable mode with `pip install -e .`.
4. Build ingestion, normalization, and backtesting modules incrementally.
5. Keep all work on public or properly licensed data only.

## First Milestones

1. Build a filing and press-release ingestion layer.
2. Normalize incoming documents into one event schema.
3. Backtest a small set of event types on liquid US equities.
4. Add paper trading and post-trade attribution.
5. Only consider live execution after out-of-sample validation.

## Notes

- SignalLedger is not a promise of profit.
- Strong backtests still fail if costs, latency, and liquidity are modeled poorly.
- The project should prefer transparent, testable event logic over vague AI-only predictions.
