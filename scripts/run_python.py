#!/usr/bin/env python3
from __future__ import annotations

import argparse
import importlib.util
import json
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
SOLUTIONS_DIR = ROOT / "python" / "solutions"
CASES_DIR = ROOT / "python" / "cases"
GREEN = "\033[32m"
RED = "\033[31m"
RESET = "\033[0m"


def color(text: str, code: str) -> str:
    if not sys.stdout.isatty():
        return text
    return f"{code}{text}{RESET}"


def find_solution(problem: str) -> Path:
    problem_id = problem.zfill(4) if problem.isdigit() else problem
    matches = sorted(SOLUTIONS_DIR.glob(f"{problem_id}_*.py"))
    if not matches:
        direct = SOLUTIONS_DIR / f"{problem}.py"
        if direct.exists():
            return direct
        raise SystemExit(f"No solution found for {problem!r} in {SOLUTIONS_DIR}")
    if len(matches) > 1:
        names = ", ".join(path.name for path in matches)
        raise SystemExit(f"Multiple solutions match {problem!r}: {names}")
    return matches[0]


def load_solution(path: Path) -> object:
    spec = importlib.util.spec_from_file_location(path.stem, path)
    if spec is None or spec.loader is None:
        raise SystemExit(f"Cannot import {path}")

    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    if not hasattr(module, "Solution"):
        raise SystemExit(f"{path} does not define class Solution")
    return module.Solution()


def load_json(value: str) -> Any:
    try:
        return json.loads(value)
    except json.JSONDecodeError as exc:
        raise SystemExit(f"Invalid JSON: {exc}") from exc


def load_cases(problem: str) -> dict[str, Any]:
    problem_id = problem.zfill(4) if problem.isdigit() else problem
    path = CASES_DIR / f"{problem_id}.json"
    if not path.exists():
        raise SystemExit(f"No case file found: {path}")
    return load_json(path.read_text(encoding="utf-8"))


def call_method(solution: object, method_name: str, args: list[Any]) -> Any:
    if not hasattr(solution, method_name):
        raise SystemExit(f"Solution does not define method {method_name!r}")
    method = getattr(solution, method_name)
    return method(*args)


def run_cases(problem: str) -> int:
    solution = load_solution(find_solution(problem))
    data = load_cases(problem)
    method_name = data["method"]

    failures = 0
    for index, case in enumerate(data["cases"], start=1):
        args = case.get("args", [])
        expected = case.get("expected")
        actual = call_method(solution, method_name, args)
        ok = actual == expected
        status = color("PASS", GREEN) if ok else color("FAIL", RED)
        print(f"{status} case {index}: actual={actual!r} expected={expected!r}")
        failures += 0 if ok else 1

    return failures


def run_inline(problem: str, method_name: str, args_json: str) -> int:
    solution = load_solution(find_solution(problem))
    args = load_json(args_json)
    if not isinstance(args, list):
        raise SystemExit("--args must be a JSON array, for example '[\"abc\"]'")
    actual = call_method(solution, method_name, args)
    print(repr(actual))
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Run a LeetCode-style Python Solution method locally."
    )
    parser.add_argument("problem", help="Problem id, for example 1, 0001, or 0003")
    parser.add_argument("--method", help="Method name to call for inline args")
    parser.add_argument("--args", help="JSON array of method arguments")
    args = parser.parse_args()

    if args.method or args.args:
        if not args.method or args.args is None:
            raise SystemExit("Use --method and --args together")
        return run_inline(args.problem, args.method, args.args)

    return run_cases(args.problem)


if __name__ == "__main__":
    raise SystemExit(main())
