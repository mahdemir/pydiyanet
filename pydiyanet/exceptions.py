"""Exceptions for Diyanet API client."""

from __future__ import annotations


class DiyanetApiError(Exception):
    """Base exception for Diyanet API errors."""


class DiyanetAuthError(DiyanetApiError):
    """Exception to indicate authentication failure."""


class DiyanetConnectionError(DiyanetApiError):
    """Exception to indicate connection failure."""
