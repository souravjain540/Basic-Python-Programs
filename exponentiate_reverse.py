#!/usr/bin/env python3
"""exponentiate_reverse.py

Compute n ** reverse(n). Example: 54 -> 54**45

Usage:
    python exponentiate_reverse.py 54

Notes:
- The reversed exponent is computed from the absolute value of the input's digits.
- Very large results may be extremely big; use small inputs for quick runs.
"""
from __future__ import annotations
import argparse
import sys


def reverse_int(n: int) -> int:
    """Return the integer formed by reversing the decimal digits of n.

    Examples:
        54 -> 45
        120 -> 21 (leading zeros dropped)
        -13 -> 31
    """
    s = str(abs(n))
    rs = s[::-1].lstrip("0") or "0"
    rev = int(rs)
    return rev if n >= 0 else rev


def exponentiate_reverse(n: int) -> int:
    """Return n ** reverse_int(n).

    Uses the absolute reversed digits as the exponent (so the exponent is non-negative).
    """
    exp = reverse_int(n)
    return pow(n, exp)


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    p = argparse.ArgumentParser(
        prog="exponentiate_reverse",
        description="Compute n raised to the power formed by reversing the digits of n",
    )
    p.add_argument("n", type=int, help="integer base (e.g. 54)")
    return p.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    n = args.n
    try:
        result = exponentiate_reverse(n)
    except OverflowError:
        print("Result too large to compute with Python's pow()", file=sys.stderr)
        return 2
    print(result)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
