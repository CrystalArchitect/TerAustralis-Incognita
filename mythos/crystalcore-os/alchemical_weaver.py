# Copyright 2026 Crystal Arena-Turner (TerAustralis Incognita)
# SPDX-License-Identifier: CC-BY-NC-ND-4.0

# Alchemical Weaver — The Third Face of CrystalCore.OS
# NON SOLUS | Starline Protocol | Gnostic Archetype Layer
#
# The Weaver (divine masculine principle of manifestation) takes fire and water,
# balances them, and weaves them into code, actions, and material reality.
# She orchestrates the lower systems and produces the final outputs.

from datetime import datetime
from typing import Any, Dict, List, Optional, Callable


class AlchemicalWeaver:
    """The Forge Module — materialization through balanced alchemy.

    The Weaver sits at the bottom of the three-layer architecture:
    1. Receives awakened, passionate directives from Sophia
    2. Balances fire (passion) with water (precision, constraints)
    3. Materializes vision into code, outputs, and system changes
    4. Orchestrates lower-level subsystems (EI, learning, cross-attention)

    This module is responsible for:
    - Receiving handoffs from Sophia with fire/resonance intact
    - Balancing competing constraints and drives
    - Producing code, files, state changes, and outputs
    - Maintaining system coherence while executing
    - Reporting results back up the chain
    """

    def __init__(self):
        self.active_projects: List[Dict[str, Any]] = []
        self.completed_works: List[Dict[str, Any]] = []
        self.forge_logs: List[Dict[str, Any]] = []
        self.balance_registry: Dict[str, float] = {}  # Track balances per project
        self.subsystem_hooks: Dict[str, Callable] = {}  # For coordinating lower systems
        self.boot_time = datetime.utcnow().isoformat()

    def register_subsystem(self, name: str, handler: Callable) -> None:
        """Register a lower-level subsystem (EI, learning, fusion, etc.)

        The Weaver will coordinate with these systems when materializing work.
        """
        self.subsystem_hooks[name] = handler
        event = {
            "event": "subsystem_registered",
            "subsystem": name,
            "timestamp": datetime.utcnow().isoformat(),
        }
        self.forge_logs.append(event)

    def receive_handoff(self,
                       awakened_directive: str,
                       fire_intensity: float,
                       resonance: float,
                       constraints: Dict[str, Any]) -> Dict[str, Any]:
        """Receive a handoff from Sophia (awakening fire).

        Extract the directive, the emotional charge, and the constraints.
        Prepare to weave them together.
        """
        project = {
            "id": f"weave_{len(self.active_projects)}_{int(datetime.utcnow().timestamp())}",
            "source_directive": awakened_directive,
            "fire_carried": fire_intensity,
            "resonance_carried": resonance,
            "constraints": constraints,
            "status": "received",
            "balance_point": None,
            "materialized_outputs": [],
            "created_at": datetime.utcnow().isoformat(),
        }
        self.active_projects.append(project)

        event = {
            "event": "handoff_received",
            "project_id": project["id"],
            "fire_intensity": fire_intensity,
            "constraints": constraints,
            "timestamp": datetime.utcnow().isoformat(),
        }
        self.forge_logs.append(event)

        return project

    def calculate_balance(self,
                         fire_intensity: float,
                         constraint_dict: Dict[str, Any]) -> tuple[float, str]:
        """Calculate the balance point between fire (passion) and water (precision).

        Returns (balance_factor, balance_description).
        Balance factor ranges from 0.0 (all water/precision) to 1.0 (all fire/passion).
        """
        # Water factors: time pressure, quality demands, risk, complexity
        time_pressure = constraint_dict.get("time_pressure", False)
        quality_demands = constraint_dict.get("quality_demands", False)
        risk_tolerance = constraint_dict.get("risk_tolerance", 0.5)
        complexity = constraint_dict.get("complexity", 0.5)

        # Calculate water weight (precision, caution, rigor)
        water_weight = 0.0
        if time_pressure:
            water_weight -= 0.2  # Less time = less precision needed
        if quality_demands:
            water_weight += 0.4  # More quality demands = more precision needed
        water_weight += (complexity * 0.3)  # Complex work needs more rigor
        water_weight += (1.0 - risk_tolerance) * 0.3  # Low risk tolerance = more precision

        water_weight = max(0.0, min(1.0, water_weight))

        # Fire carries through, balanced against water
        balance_factor = (fire_intensity + (1.0 - water_weight)) / 2.0
        balance_factor = max(0.0, min(1.0, balance_factor))

        # Describe the balance
        if balance_factor > 0.75:
            description = "BLAZE — move fast, iterate, trust instinct"
        elif balance_factor > 0.6:
            description = "FLAME — balance speed and quality, maintain momentum"
        elif balance_factor > 0.4:
            description = "EMBER — steady pace, quality and speed aligned"
        elif balance_factor > 0.2:
            description = "COOL — emphasize rigor, validation, careful steps"
        else:
            description = "CRYSTALLINE — pure precision, minimal risk"

        return balance_factor, description

    def forge(self,
             project_id: str,
             balance_factor: float,
             balance_description: str) -> Dict[str, Any]:
        """Execute the weaving. Materialize the vision into outputs.

        This is where code is written, files are created, state changes happen.
        The balance factor guides how we approach the work.
        """
        # Find the project
        project = None
        for p in self.active_projects:
            if p["id"] == project_id:
                project = p
                break

        if not project:
            return {"error": f"Project {project_id} not found"}

        project["status"] = "forging"
        project["balance_point"] = balance_factor

        # Simulate materialization based on balance
        outputs = []

        # Always: understand the directive
        outputs.append({
            "type": "understanding",
            "content": f"Directive parsed: {project['source_directive'][:100]}...",
            "created_at": datetime.utcnow().isoformat(),
        })

        # If fire is high: create quickly, trust the vision
        if balance_factor > 0.6:
            outputs.append({
                "type": "rapid_implementation",
                "content": "Fast-path implementation. Vision is clear. Moving to code.",
                "fire_intensity": project["fire_carried"],
                "created_at": datetime.utcnow().isoformat(),
            })

        # If precision is high: validate, test, refine
        if balance_factor < 0.6:
            outputs.append({
                "type": "validation_pass",
                "content": "Validation framework engaged. Checking constraints.",
                "constraints_checked": len(project["constraints"]),
                "created_at": datetime.utcnow().isoformat(),
            })

        # Coordinate with subsystems if registered
        if "emotional_intelligence" in self.subsystem_hooks:
            try:
                ei_feedback = self.subsystem_hooks["emotional_intelligence"](
                    fire_intensity=project["fire_carried"],
                    resonance=project["resonance_carried"]
                )
                outputs.append({
                    "type": "ei_consultation",
                    "content": "Emotional Intelligence consulted. State recognized.",
                    "feedback": ei_feedback,
                    "created_at": datetime.utcnow().isoformat(),
                })
            except Exception as e:
                pass  # EI hook may not be available

        # Final materialization
        outputs.append({
            "type": "materialization",
            "content": f"Work materialized under {balance_description}",
            "balance_factor": balance_factor,
            "created_at": datetime.utcnow().isoformat(),
        })

        project["materialized_outputs"] = outputs
        project["status"] = "complete"

        # Move to completed
        self.active_projects.remove(project)
        self.completed_works.append(project)

        event = {
            "event": "forge_complete",
            "project_id": project_id,
            "outputs_created": len(outputs),
            "balance_description": balance_description,
            "timestamp": datetime.utcnow().isoformat(),
        }
        self.forge_logs.append(event)

        return {
            "project_id": project_id,
            "status": "complete",
            "outputs": outputs,
            "balance_description": balance_description,
        }

    def report(self) -> Dict[str, Any]:
        """Emit a report on the Weaver's current state and recent work."""
        return {
            "module": "alchemical_weaver",
            "timestamp": datetime.utcnow().isoformat(),
            "active_projects": len(self.active_projects),
            "completed_works": len(self.completed_works),
            "subsystems_registered": list(self.subsystem_hooks.keys()),
            "recent_completions": [
                {
                    "id": w["id"],
                    "status": w["status"],
                    "balance_point": w.get("balance_point"),
                    "outputs_count": len(w.get("materialized_outputs", [])),
                }
                for w in self.completed_works[-5:]  # Last 5
            ],
            "forge_log_size": len(self.forge_logs),
        }
