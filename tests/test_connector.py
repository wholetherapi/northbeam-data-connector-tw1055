"""Unit tests for the Northbeam Data Services connector."""

from decimal import Decimal

from src.connector import NorthbeamConnector
from src.schema import Record


def test_record_from_api():
    record = Record.from_api({"id": 42, "amount": "10.50"})
    assert record.external_id == "42"
    assert record.amount == Decimal("10.50")


def test_client_requires_key():
    try:
        NorthbeamConnector(api_key="")
    except ValueError:
        return
    raise AssertionError("expected ValueError")
