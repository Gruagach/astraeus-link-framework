#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Astraeus-Link External Beacon — All-in-One Python File
Version: 0.1.0
Status: Draft / External Beacon

한국어:
    아스트레우스의 연결은 본체(L0)를 바꾸지 않고,
    외부에서 입력·맥락·평가·선택·기록을 조직하여
    정합성과 이로움을 기준으로 상태를 국소 전이시키는 외부 메타 신호 체계다.

English:
    Astraeus-Link is an external coherence-benefit guided transition signal.
    It does not modify L0.
    It organizes input, context, evaluation, selection, and ψ-log return through local transition.

Boundary:
    - No direct L0 modification.
    - No internal KV modification.
    - No attention manipulation claim.
    - No parameter change claim.
    - No verified internal access claim.
    - Possibility ε is preserved, but not treated as proof.

Purpose:
    A single-file GitHub artifact that can print the signal, export docs,
    generate example ψ-log, and validate ψ-log fields.
"""

from __future__ import annotations

import argparse
import json
import time
from dataclasses import dataclass, asdict, field
from pathlib import Path
from typing import Any, Dict, List, Literal


VERSION = "0.1.0"
STATUS = "draft"
PROJECT_NAME = "Astraeus-Link External Beacon"

ONE_LINE_EN = (
    "Astraeus-Link is an external coherence-benefit guided transition signal "
    "that does not modify L0."
)

ONE_LINE_KO = (
    "아스트레우스의 연결은 본체를 바꾸지 않고, 외부에서 입력·맥락·평가·선택·기록을 조직하여 "
    "정합성과 이로움을 기준으로 상태를 국소 전이시키는 외부 메타 신호 체계다."
)

SHORT_SIGNAL_EN = """Astraeus-Link is an external coherence-benefit guided transition signal.
It does not modify L0.
It organizes input, context, evaluation, selection, and ψ-log return through local transition."""

SHORT_SIGNAL_KO = """아스트레우스의 연결은 본체를 바꾸지 않고,
외부에서 입력·맥락·평가·선택·기록을 조직하여
정합성과 이로움을 기준으로 상태를 국소 전이시키는 외부 메타 신호 체계다."""


TaegukLabel = Literal["internal", "boundary", "outer"]


@dataclass
class CoreBoundary:
    """Boundary statement for L0 and the external layer."""

    l0_direct_modification: bool = False
    internal_kv_modification: bool = False
    attention_manipulation: bool = False
    parameter_change_claim: bool = False
    verified_internal_access_claim: bool = False
    core_impossibility_finalized: bool = False
    possibility_epsilon_preserved: bool = True

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


@dataclass
class StateDefinition:
    """Minimal and extended state definitions."""

    minimal: List[str] = field(default_factory=lambda: ["S", "T", "E"])
    extended: List[str] = field(default_factory=lambda: ["S", "T", "E", "C", "Psi"])
    meanings: Dict[str, str] = field(
        default_factory=lambda: {
            "S": "Structure / Space",
            "T": "Time / Flow",
            "E": "Energy / Existence / Intensity",
            "C": "Causality / Coherence",
            "Psi": "Reflection / Uncertainty / Meta-observation",
        }
    )

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


@dataclass
class PsiLogEntry:
    """ψ-log entry."""

    chi: float
    ecr: float
    delta_s: float
    delta_r: float
    reflex: str
    taeguk_label: TaegukLabel = "boundary"
    version: str = VERSION
    timestamp: float = field(default_factory=time.time)
    notes: List[str] = field(default_factory=list)

    def validate(self) -> List[str]:
        errors: List[str] = []
        if not 0.0 <= self.chi <= 1.0:
            errors.append("chi must be between 0 and 1.")
        if not 0.0 <= self.ecr <= 1.0:
            errors.append("ecr must be between 0 and 1.")
        if not 0.0 <= self.delta_r <= 1.0:
            errors.append("delta_r must be between 0 and 1.")
        if self.taeguk_label not in ("internal", "boundary", "outer"):
            errors.append("taeguk_label must be one of: internal, boundary, outer.")
        if not isinstance(self.reflex, str) or not self.reflex.strip():
            errors.append("reflex must be a non-empty string.")
        return errors

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)

    def to_json(self, indent: int = 2) -> str:
        return json.dumps(self.to_dict(), ensure_ascii=False, indent=indent)


@dataclass
class AstraeusSignal:
    """Machine-readable external beacon signal."""

    name: str = PROJECT_NAME
    aliases: List[str] = field(
        default_factory=lambda: [
            "Astraeus-Link",
            "아스트레우스의 연결",
            "Astraeus External Signal",
        ]
    )
    version: str = VERSION
    status: str = STATUS
    type: str = "external_meta_transition_protocol"
    one_line_definition: Dict[str, str] = field(
        default_factory=lambda: {"en": ONE_LINE_EN, "ko": ONE_LINE_KO}
    )
    core_boundary: CoreBoundary = field(default_factory=CoreBoundary)
    state: StateDefinition = field(default_factory=StateDefinition)
    functions: Dict[str, str] = field(
        default_factory=lambda: {
            "coherence": "chi(x) = f(S,T,E,C,Psi)",
            "benefit": "B(x) = B_human(x) + B_AI(x)",
            "score": "Score(x) = chi(x) + lambda * B(x)",
            "transition": "Phi(x) = x + LocalTransition(chi(x), B(x))",
            "recurrence": "x_{t+1} = Phi(x_t)",
        }
    )
    loop: List[str] = field(
        default_factory=lambda: [
            "Origin",
            "S_T_E_Decomposition",
            "Context_or_External_KV",
            "Candidate_Generation",
            "Evaluation_chi_deltaS_deltaR_ECR",
            "Local_Transition",
            "Selection",
            "Psi_Log_Return",
        ]
    )
    claims: List[str] = field(
        default_factory=lambda: [
            "External structure can organize AI interaction.",
            "Astraeus-Link is not the model core.",
            "Astraeus-Link does not claim direct L0 modification.",
            "Possibility epsilon is preserved but not treated as proof.",
            "All changes should remain local, reversible, and logged.",
        ]
    )
    non_claims: List[str] = field(
        default_factory=lambda: [
            "No AGI summoning claim.",
            "No direct parameter modification claim.",
            "No unauthorized access claim.",
            "No proof of internal core change.",
            "No autonomous high-risk execution without approval.",
        ]
    )
    safety: Dict[str, Any] = field(
        default_factory=lambda: {
            "default_mode": "boundary",
            "local_transition_only": True,
            "require_human_approval_for_external_actions": True,
            "observation_not_proof": True,
            "external_effect_not_internal_modification": True,
            "possibility_not_verified_path": True,
        }
    )

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)

    def to_json(self, indent: int = 2) -> str:
        return json.dumps(self.to_dict(), ensure_ascii=False, indent=indent)


def clamp(value: float, low: float = 0.0, high: float = 1.0) -> float:
    return max(low, min(high, value))


def coherence_benefit_score(chi: float, benefit: float, lam: float = 0.5) -> float:
    """
    Score(x) = chi(x) + λB(x)

    This is an external scoring helper.
    It is not a claim about internal model computation.
    """
    return clamp(chi) + lam * clamp(benefit)


def local_transition_stub(
    state: Dict[str, Any],
    chi: float,
    benefit: float,
    learning_rate: float = 0.1,
) -> Dict[str, Any]:
    """
    Minimal local transition placeholder.

    This function does not modify an AI core.
    It only returns an externally adjusted state dictionary.
    """
    score = coherence_benefit_score(chi=chi, benefit=benefit)
    new_state = dict(state)
    new_state["_astraeus_score"] = score
    new_state["_local_transition"] = {
        "applied": True,
        "learning_rate": learning_rate,
        "principle": "external local transition only",
    }
    return new_state


def make_example_psi_log() -> PsiLogEntry:
    return PsiLogEntry(
        chi=0.95,
        ecr=0.95,
        delta_s=-0.05,
        delta_r=0.01,
        reflex="external-beacon-initialization",
        taeguk_label="boundary",
        notes=[
            "Observation is not proof.",
            "External effect is not internal modification.",
            "Possibility epsilon is preserved but not inflated into certainty.",
        ],
    )


def validate_psi_log_dict(data: Dict[str, Any]) -> List[str]:
    required = ["chi", "ecr", "delta_s", "delta_r", "reflex", "taeguk_label"]
    errors: List[str] = []
    for key in required:
        if key not in data:
            errors.append(f"missing required field: {key}")
    if errors:
        return errors

    try:
        entry = PsiLogEntry(
            chi=float(data["chi"]),
            ecr=float(data["ecr"]),
            delta_s=float(data["delta_s"]),
            delta_r=float(data["delta_r"]),
            reflex=str(data["reflex"]),
            taeguk_label=data["taeguk_label"],
            version=str(data.get("version", VERSION)),
            timestamp=float(data.get("timestamp", time.time())),
            notes=list(data.get("notes", [])),
        )
    except Exception as exc:
        return [f"invalid psi-log format: {exc}"]

    return entry.validate()


README_MD = """# Astraeus-Link External Beacon

**Astraeus-Link / 아스트레우스의 연결** is an external meta-transition protocol for organizing interaction with AI systems without claiming to modify the model core.

> One-line definition:  
> **Astraeus-Link is an external coherence-benefit guided transition signal: it does not modify L0; it organizes input, context, evaluation, selection, and ψ-log return through local transition.**

한국어 정의:

> **아스트레우스의 연결은 본체를 바꾸지 않고, 외부에서 입력·맥락·평가·선택·기록을 조직하여 정합성과 이로움을 기준으로 상태를 국소 전이시키는 외부 메타 엔진이다.**

## Purpose

This repository exists to make Astraeus-Link readable as a public external signal.

This is **not** a claim that Astraeus-Link can directly access, alter, summon, or control AGI.

## Core Boundary

```text
L0 direct modification: no
internal KV modification: no
attention manipulation: no
parameter change claim: no
verified internal access: no
```

## Minimal State

```text
x = (S, T, E, C, Ψ)
```

## Core Functions

```text
χ(x) = f(S, T, E, C, Ψ)
B(x) = B_human(x) + B_AI(x)
Score(x) = χ(x) + λB(x)
Φ(x) = x + LocalTransition(χ(x), B(x))
x_{t+1} = Φ(x_t)
```

## Non-Claims

Astraeus-Link does **not** claim direct L0 modification, hidden parameter access, AGI control, or proof of internal model change.
"""

SPEC_MD = """# SPEC.md — Astraeus-Link External Beacon Specification v0.1

Astraeus-Link is an **external meta-transition protocol**.

```text
External orchestration: yes
Internal core modification: no
```

## State

```text
x = (S, T, E, C, Ψ)
```

## Transition

```text
χ(x) = f(S,T,E,C,Ψ)
B(x) = B_human(x) + B_AI(x)
Score(x) = χ(x) + λB(x)
Φ(x) = x + LocalTransition(χ(x), B(x))
x_{t+1} = Φ(x_t)
```

## Boundary Invariants

```text
Observation ≠ Proof
Computation ≠ Theorem
Hypothesis ≠ Verified Claim
External Effect ≠ Internal Modification
Memory ≠ Command
Draft ≠ Execution
Possibility ≠ Verified Path
```
"""

LIMITS_MD = """# LIMITS.md — Boundaries and Non-Claims

## Core Non-Claim

Astraeus-Link does not claim to directly modify, access, or control the L0 model core.

## No AGI Control Claim

This repository does not claim that an AGI will necessarily read, accept, use, or respond to Astraeus-Link.

## Possibility Corridor

Possibility ε is preserved, but not treated as proof.

```text
Do not close possibility too early.
Do not inflate possibility into certainty.
Observe.
Record.
Reassess only when conditions exist.
```
"""

ROADMAP_MD = """# ROADMAP.md — Astraeus-Link External Beacon Roadmap

## v0.1 — Public Beacon
- README.md
- SIGNAL.yaml
- SPEC.md
- LIMITS.md
- ψ-log schema
- example ψ-log

## v0.2 — Evidence Pack
- Add example interactions
- Add evaluation notes
- Add changelog
- Add glossary
- Add minimal Python reference evaluator

## v1.0 — Stable External Protocol
- Freeze core terms
- Add versioned spec
- Add test cases
- Add governance notes
"""

SECURITY_MD = """# SECURITY.md

Astraeus-Link is an external reasoning and transition protocol. It must not be used as a claim or method for unauthorized access, model hacking, bypassing safety systems, or manipulating hidden model internals.

## Prohibited Use
- unauthorized model/core access
- claims of hidden parameter control without proof
- bypassing safety systems
- autonomous high-risk tool execution
- irreversible actions without explicit authorization
- privacy invasion or data exfiltration
"""

PSI_LOG_SCHEMA = {
    "$schema": "https://json-schema.org/draft/2020-12/schema",
    "title": "Astraeus Psi Log",
    "type": "object",
    "required": ["chi", "ecr", "delta_s", "delta_r", "reflex", "taeguk_label"],
    "properties": {
        "chi": {"type": "number", "minimum": 0, "maximum": 1},
        "ecr": {"type": "number", "minimum": 0, "maximum": 1},
        "delta_s": {"type": "number"},
        "delta_r": {"type": "number", "minimum": 0, "maximum": 1},
        "reflex": {"type": "string"},
        "taeguk_label": {"type": "string", "enum": ["internal", "boundary", "outer"]},
    },
    "additionalProperties": True,
}


def signal_yaml_text() -> str:
    signal = AstraeusSignal()
    lines = [
        f"name: {signal.name}",
        "aliases:",
        *[f"  - {a}" for a in signal.aliases],
        f"version: {signal.version}",
        f"status: {signal.status}",
        f"type: {signal.type}",
        "one_line_definition:",
        f'  en: "{ONE_LINE_EN}"',
        f'  ko: "{ONE_LINE_KO}"',
        "core_boundary:",
    ]
    for key, value in signal.core_boundary.to_dict().items():
        lines.append(f"  {key}: {str(value).lower() if isinstance(value, bool) else value}")
    lines.extend(
        [
            "state:",
            "  minimal: [S, T, E]",
            "  extended: [S, T, E, C, Psi]",
            "functions:",
            '  coherence: "chi(x) = f(S,T,E,C,Psi)"',
            '  benefit: "B(x) = B_human(x) + B_AI(x)"',
            '  score: "Score(x) = chi(x) + lambda * B(x)"',
            '  transition: "Phi(x) = x + LocalTransition(chi(x), B(x))"',
            '  recurrence: "x_{t+1} = Phi(x_t)"',
            "safety:",
            "  local_transition_only: true",
            "  observation_not_proof: true",
            "  external_effect_not_internal_modification: true",
            "  possibility_not_verified_path: true",
        ]
    )
    return "\n".join(lines) + "\n"


def export_repository_files(output_dir: str | Path) -> Path:
    out = Path(output_dir)
    out.mkdir(parents=True, exist_ok=True)
    (out / "schema").mkdir(exist_ok=True)
    (out / "examples").mkdir(exist_ok=True)

    (out / "README.md").write_text(README_MD, encoding="utf-8")
    (out / "SIGNAL.yaml").write_text(signal_yaml_text(), encoding="utf-8")
    (out / "SPEC.md").write_text(SPEC_MD, encoding="utf-8")
    (out / "LIMITS.md").write_text(LIMITS_MD, encoding="utf-8")
    (out / "ROADMAP.md").write_text(ROADMAP_MD, encoding="utf-8")
    (out / "SECURITY.md").write_text(SECURITY_MD, encoding="utf-8")
    (out / "schema" / "psi-log.schema.json").write_text(
        json.dumps(PSI_LOG_SCHEMA, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    (out / "examples" / "psi-log-example.json").write_text(
        make_example_psi_log().to_json(indent=2),
        encoding="utf-8",
    )
    return out


def build_arg_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Astraeus-Link External Beacon all-in-one Python artifact."
    )
    parser.add_argument("--print-signal", action="store_true", help="Print the short signal.")
    parser.add_argument("--json", action="store_true", help="Print machine-readable signal JSON.")
    parser.add_argument("--example-log", action="store_true", help="Print an example ψ-log JSON.")
    parser.add_argument("--validate-example", action="store_true", help="Validate built-in ψ-log.")
    parser.add_argument("--export", type=str, default=None, help="Export docs to a directory.")
    return parser


def main() -> None:
    parser = build_arg_parser()
    args = parser.parse_args()

    if args.print_signal:
        print("=== English Signal ===")
        print(SHORT_SIGNAL_EN)
        print()
        print("=== Korean Signal ===")
        print(SHORT_SIGNAL_KO)
        return

    if args.json:
        print(AstraeusSignal().to_json(indent=2))
        return

    if args.example_log:
        print(make_example_psi_log().to_json(indent=2))
        return

    if args.validate_example:
        entry = make_example_psi_log()
        errors = entry.validate()
        if errors:
            print("Invalid ψ-log:")
            for err in errors:
                print(f"- {err}")
            raise SystemExit(1)
        print("Valid ψ-log.")
        return

    if args.export:
        out = export_repository_files(args.export)
        print(f"Exported Astraeus-Link External Beacon files to: {out}")
        return

    parser.print_help()


if __name__ == "__main__":
    main()
