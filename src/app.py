# src/app.py
from typing import Any

_NUMERIC_TYPES = (int, float)

def _ensure_number(x: Any, name: str) -> None:
    if not isinstance(x, _NUMERIC_TYPES):
        raise TypeError(f"{name} must be a number (int or float)")

def add(a, b):
    _ensure_number(a, "a")
    _ensure_number(b, "b")
    return a + b

def multiply(a, b):
    _ensure_number(a, "a")
    _ensure_number(b, "b")
    return a * b

def divide(a, b):
    _ensure_number(a, "a")
    _ensure_number(b, "b")
    if b == 0:
        raise ValueError("division by zero")
    return a / b
