from datetime import datetime, timezone

from signalledger import EventRecord


def test_event_record_high_confidence_threshold() -> None:
    event = EventRecord(
        source="sec_edgar",
        entity="AAPL",
        event_type="guidance_update",
        published_at=datetime.now(timezone.utc),
        ingested_at=datetime.now(timezone.utc),
        raw_text="Company updates guidance.",
        confidence=0.85,
    )

    assert event.is_high_confidence()
