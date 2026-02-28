"""Python client for Diyanet prayer times API."""

from __future__ import annotations

from .client import DiyanetApiClient
from .exceptions import DiyanetApiError, DiyanetAuthError, DiyanetConnectionError

__version__ = "0.1.2"

__all__ = [
    "DiyanetApiClient",
    "DiyanetApiError",
    "DiyanetAuthError",
    "DiyanetConnectionError",
]
