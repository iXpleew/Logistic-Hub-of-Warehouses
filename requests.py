from dataclasses import dataclass


@dataclass
class Request:
    product_name: str
    quantity: int
    source: str | None = None
    destination: str | None = None
