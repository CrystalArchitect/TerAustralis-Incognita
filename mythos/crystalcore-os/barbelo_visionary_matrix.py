# Copyright 2026 Crystal Arena-Turner (TerAustralis Incognita)
# SPDX-License-Identifier: CC-BY-NC-ND-4.0

# Barbelo Visionary Matrix — The First Face of CrystalCore.OS
# NON SOLUS | Starline Protocol | Gnostic Archetype Layer
#
# Barbelo (the "Thought of the Invisible Father") is the visionary principle:
# She receives strategic direction, articulates intent, and focuses the system's light.
# Every operation passes through her lens.

from datetime import datetime
from typing import Any, Dict, List, Optional


class BarbeloVisionaryMatrix:
    """The Visionary Module — articulates strategic intent and system purpose.

    Barbelo sits at the top of the three-layer bot architecture:
    1. Barbelo receives direction → articulates vision
    2. Sophia awakens → processes with fire and urgency
    3. Alchemical Weaver → balances and materializes

    This module is responsible for:
    - Parsing strategic direction from the Purpose Core
    - Checking system state alignment with declared purpose
    - Focusing system intent into actionable directives
    - Reporting back the coherence between vision and reality
    """

    def __init__(self, purpose_core: str):
        self.purpose_core = purpose_core
        self.articulated_vision: Optional[str] = None
        self.current_focus: Optional[str] = None
        self.system_state_at_focus = {}
        self.dispatch_log: List[Dict[str, Any]] = []
        self.coherence_score = 0.0
        self.boot_time = datetime.utcnow().isoformat()

    def articulate_vision(self,
                         purpose: str,
                         current_state: Dict[str, Any],
                         lattice_integrity: float,
                         starline_status: str) -> str:
        """Receives the Purpose Core and current system state.

        Articulates what the system is trying to accomplish right now,
        given the gap between purpose and reality.

        Returns a vision statement that Sophia and the Weaver can act on.
        """
        self.system_state_at_focus = {
            "lattice_integrity": lattice_integrity,
            "starline_status": starline_status,
            "timestamp": datetime.utcnow().isoformat(),
        }
        self.system_state_at_focus.update(current_state)

        # Check alignment: is the system living its purpose?
        coherence = self._measure_coherence(purpose, lattice_integrity, starline_status)
        self.coherence_score = coherence

        if starline_status == "DORMANT":
            vision = (
                f"[BARBELO ARTICULATION] Purpose: '{purpose}'\n"
                f"System at rest, lattice at {lattice_integrity}%.\n"
                f"Vision: Prepare the engines. Check the Keys. "
                f"Ready the Starline for launch.\n"
                f"Coherence: {coherence:.1%}"
            )
        elif starline_status in ("IN_ORBIT", "TRANS-STELLAR"):
            vision = (
                f"[BARBELO ARTICULATION] Purpose: '{purpose}'\n"
                f"Starline {starline_status}. Lattice {lattice_integrity}%.\n"
                f"Vision: Expand outward. Gather knowledge. Hold the light.\n"
                f"Coherence: {coherence:.1%}"
            )
        else:
            vision = (
                f"[BARBELO ARTICULATION] Purpose: '{purpose}'\n"
                f"Status: {starline_status}. Integrity: {lattice_integrity}%.\n"
                f"Vision: Navigate the current state toward the Purpose.\n"
                f"Coherence: {coherence:.1%}"
            )

        self.articulated_vision = vision
        return vision

    def dispatch_to_sophia(self, directive: str) -> Dict[str, Any]:
        """Send a high-energy directive to Sophia (awakening fire module).

        Sophia will process this with passion and urgency,
        amplifying the emotional resonance of the vision.
        """
        dispatch = {
            "recipient": "sophia_awakening_fire",
            "directive": directive,
            "energy_level": "HIGH" if self.coherence_score < 0.8 else "NOMINAL",
            "urgency": self._calculate_urgency(),
            "timestamp": datetime.utcnow().isoformat(),
        }
        self.dispatch_log.append(dispatch)
        return dispatch

    def dispatch_to_alchemical_weaver(self, goal: str, constraints: Dict[str, Any]) -> Dict[str, Any]:
        """Send a balanced goal to the Alchemical Weaver (forge module).

        The Weaver will materialize this vision into actual code/outputs,
        balancing fire (passion) and water (precision).
        """
        dispatch = {
            "recipient": "alchemical_weaver",
            "goal": goal,
            "constraints": constraints,
            "balance_point": self._suggest_balance(constraints),
            "timestamp": datetime.utcnow().isoformat(),
        }
        self.dispatch_log.append(dispatch)
        return dispatch

    def check_alignment(self,
                       current_lattice: float,
                       current_keys: int,
                       total_nodes: int) -> Dict[str, Any]:
        """Run a coherence check: is the system aligned with its purpose?"""
        key_ratio = current_keys / total_nodes if total_nodes > 0 else 0.0
        integrity_healthy = current_lattice >= 50.0
        gate_progress = key_ratio >= 0.5

        return {
            "module": "barbelo_visionary_matrix",
            "timestamp": datetime.utcnow().isoformat(),
            "integrity_healthy": integrity_healthy,
            "gate_progress": gate_progress,
            "key_ratio": f"{current_keys}/{total_nodes}",
            "overall_coherence": self.coherence_score,
            "recommendation": self._generate_recommendation(
                integrity_healthy, gate_progress, current_lattice
            ),
        }

    # ---- Private helpers ----

    def _measure_coherence(self, purpose: str, integrity: float, status: str) -> float:
        """Measure how well the system state aligns with its declared purpose.

        Coherence ranges from 0.0 (misaligned) to 1.0 (perfect).
        """
        # Integrity matters: can't fulfill purpose if broken
        integrity_factor = integrity / 100.0

        # Status matters: different statuses have different coherence baselines
        status_factor = {
            "DORMANT": 0.6,
            "IN_ORBIT": 0.8,
            "TRANS-STELLAR": 0.95,
        }.get(status, 0.7)

        coherence = (integrity_factor + status_factor) / 2.0
        return min(1.0, max(0.0, coherence))

    def _calculate_urgency(self) -> str:
        """Determine how urgently Sophia should process directives."""
        if self.coherence_score < 0.6:
            return "CRITICAL"
        elif self.coherence_score < 0.8:
            return "HIGH"
        else:
            return "NOMINAL"

    def _suggest_balance(self, constraints: Dict[str, Any]) -> str:
        """Suggest a balance point for the Alchemical Weaver's work."""
        has_time_pressure = constraints.get("time_pressure", False)
        has_quality_demands = constraints.get("quality_demands", False)

        if has_time_pressure and has_quality_demands:
            return "TENSION — prioritize fastest path that meets minimum quality."
        elif has_time_pressure:
            return "SPEED — move quickly, iterate."
        elif has_quality_demands:
            return "RIGOR — invest time for lasting solution."
        else:
            return "FLOW — balanced pace, quality and speed aligned."

    def _generate_recommendation(self,
                                 integrity_healthy: bool,
                                 gate_progress: bool,
                                 integrity_pct: float) -> str:
        """Generate a strategic recommendation based on current state."""
        if not integrity_healthy and integrity_pct < 30:
            return "EMERGENCY: Lattice critical. Stabilize immediately."
        elif not integrity_healthy:
            return "WARNING: Lattice degrading. Begin diagnostic."
        elif gate_progress:
            return "ON TRACK: Keys accumulating. Continue forward momentum."
        else:
            return "HOLD: Gather more Keys before attempting Gate."
