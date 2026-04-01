# SignalLedger PnL Model

SignalLedger should treat PnL as a deployment filter, not as a vanity metric.

## Core Principle

Research profits are not real profits unless they survive:
- commissions
- bid-ask spread
- slippage
- borrow costs for shorts
- liquidity limits
- timing delays between publication, detection, and execution

## Expected Value

At the trade level, the simplest expected value model is:

```text
expected_value = (win_rate * average_win) - (loss_rate * average_loss) - trading_costs
```

That number only matters if it is estimated out of sample and remains stable across different periods.

## Required Inputs

Every signal candidate should be evaluated with at least:
- event type
- timestamp of source publication
- timestamp of detection
- instrument liquidity
- entry and exit assumptions
- estimated spread and slippage
- gross return and net return

## PnL Layers

SignalLedger should track:
- gross PnL
- net PnL after transaction costs
- PnL by source
- PnL by event type
- PnL by holding period
- PnL by market regime

This helps avoid false confidence from one narrow slice of performance.

## Deployment Rules

A signal should not be live-traded unless it shows:
- positive net expected value
- enough sample size to be credible
- acceptable drawdown behavior
- robust performance in walk-forward tests
- stable behavior across multiple time periods

## Common Failure Modes

Most beginner strategies fail because of:
- lookahead bias
- survivorship bias
- poor timestamp quality
- ignoring spread and market impact
- overfitting to a small event sample
- trading names that are too illiquid

SignalLedger should be built to surface those failures early.
