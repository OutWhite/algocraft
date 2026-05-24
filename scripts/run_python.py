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


def load_solution(path: Path) -> tuple[object, object]:
    spec = importlib.util.spec_from_file_location(path.stem, path)
    if spec is None or spec.loader is None:
        raise SystemExit(f"Cannot import {path}")

    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    if not hasattr(module, "Solution"):
        raise SystemExit(f"{path} does not define class Solution")
    return module, module.Solution()


def list_to_linked_list(module: object, values: list[Any]) -> Any:
    if not hasattr(module, "ListNode"):
        raise SystemExit("Solution module does not define ListNode")

    dummy = module.ListNode(0)
    current = dummy
    for value in values:
        current.next = module.ListNode(value)
        current = current.next
    return dummy.next


def list_to_linked_list_cycle(module: object, value: list[Any]) -> Any:
    if not isinstance(value, list) or len(value) != 2:
        raise SystemExit("linked_list_cycle args must be [values, pos]")

    values, pos = value
    if not isinstance(values, list) or not isinstance(pos, int):
        raise SystemExit("linked_list_cycle args must be [list, int]")
    if pos < -1 or pos >= len(values):
        raise SystemExit("linked_list_cycle pos must be -1 or a valid index")

    nodes = [module.ListNode(item) for item in values]
    for index in range(len(nodes) - 1):
        nodes[index].next = nodes[index + 1]
    if nodes and pos != -1:
        nodes[-1].next = nodes[pos]
    return nodes[0] if nodes else None


def linked_list_to_list(node: Any) -> list[Any]:
    values = []
    while node is not None:
        values.append(node.val)
        node = node.next
    return values


def prepare_args(module: object, args: list[Any], arg_types: list[str]) -> list[Any]:
    if len(args) != len(arg_types):
        raise SystemExit("arg_types length must match args length")

    prepared = []
    for value, value_type in zip(args, arg_types):
        if value_type == "linked_list":
            prepared.append(list_to_linked_list(module, value))
        elif value_type == "linked_list_cycle":
            prepared.append(list_to_linked_list_cycle(module, value))
        else:
            prepared.append(value)
    return prepared


def prepare_actual(actual: Any, expected_type: str | None) -> Any:
    if expected_type == "linked_list":
        return linked_list_to_list(actual)
    return actual


def check_mutations(args: list[Any], mutations: list[dict[str, Any]]) -> list[str]:
    failures = []
    for mutation in mutations:
        arg_index = mutation["arg"]
        expected_prefix = mutation.get("prefix")
        if expected_prefix is None:
            continue

        actual_prefix = args[arg_index][: len(expected_prefix)]
        if actual_prefix != expected_prefix:
            failures.append(
                f"arg {arg_index} prefix actual={actual_prefix!r} expected={expected_prefix!r}"
            )
    return failures


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
    module, solution = load_solution(find_solution(problem))
    data = load_cases(problem)
    method_name = data["method"]

    failures = 0
    for index, case in enumerate(data["cases"], start=1):
        args = case.get("args", [])
        arg_types = case.get("arg_types", data.get("arg_types", []))
        if arg_types:
            args = prepare_args(module, args, arg_types)
        expected = case.get("expected")
        expected_type = case.get("expected_type", data.get("expected_type"))
        actual = call_method(solution, method_name, args)
        actual = prepare_actual(actual, expected_type)
        mutation_failures = check_mutations(args, case.get("mutations", []))
        ok = actual == expected and not mutation_failures
        status = color("PASS", GREEN) if ok else color("FAIL", RED)
        details = f"actual={actual!r} expected={expected!r}"
        if mutation_failures:
            details += " mutations=(" + "; ".join(mutation_failures) + ")"
        print(f"{status} case {index}: {details}")
        failures += 0 if ok else 1

    return failures


def run_inline(problem: str, method_name: str, args_json: str) -> int:
    _, solution = load_solution(find_solution(problem))
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
