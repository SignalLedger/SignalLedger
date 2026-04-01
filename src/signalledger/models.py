from dataclasses import dataclass, field
from datetime import datetime


@dataclass(slots=True)
class EventRecord:
    """Normalized event produced from a primary source document."""

    source: str
    entity: str
    event_type: str
    published_at: datetime
    ingested_at: datetime
    raw_text: str
    confidence: float = 0.0
    metadata: dict[str, str] = field(default_factory=dict)

    def is_high_confidence(self, threshold: float = 0.8) -> bool:
        return self.confidence >= threshold
