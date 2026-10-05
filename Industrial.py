# ============================================================
# CATEGORY 8 - 3
# INDUSTRIAL MANUFACTURING USING KNOWLEDGE BASE
# Facts, Rules, Forward Chaining and Backward Chaining
# ============================================================


# -----------------------------
# INITIAL FACTS
# -----------------------------

facts = {
    "machine_running",
    "high_temperature",
    "high_vibration"
}


# -----------------------------
# KNOWLEDGE BASE RULES
# -----------------------------

rules = [

    ({"high_temperature"},
     "cooling_required"),

    ({"high_vibration"},
     "inspection_required"),

    ({"high_temperature", "high_vibration"},
     "machine_fault"),

    ({"machine_fault"},
     "stop_machine"),

    ({"low_material"},
     "order_material"),

    ({"machine_running", "normal_temperature"},
     "continue_production"),

    ({"quality_problem"},
     "inspect_product"),

    ({"machine_fault", "quality_problem"},
     "production_stop")

]


# ============================================================
# FORWARD CHAINING
# ============================================================

def forward_chaining(facts, rules):

    inferred = set(facts)

    print("\n--- Forward Chaining ---")

    changed = True

    while changed:

        changed = False

        for conditions, conclusion in rules:

            if conditions.issubset(inferred):

                if conclusion not in inferred:

                    print(
                        "Rule Fired:",
                        " AND ".join(conditions),
                        "->",
                        conclusion
                    )

                    inferred.add(conclusion)

                    changed = True

    return inferred


# ============================================================
# BACKWARD CHAINING
# ============================================================

def backward_chaining(goal, facts, rules, visited=None):

    if visited is None:
        visited = set()

    # If goal is already known
    if goal in facts:
        return True

    # Avoid repeated checking
    if goal in visited:
        return False

    visited.add(goal)

    # Search for rule that concludes the goal
    for conditions, conclusion in rules:

        if conclusion == goal:

            print(
                "Checking:",
                " AND ".join(conditions),
                "->",
                conclusion
            )

            # Check all conditions recursively
            if all(
                backward_chaining(condition, facts, rules, visited)
                for condition in conditions
            ):
                return True

    return False


# ============================================================
# MAIN PROGRAM
# ============================================================

print("Initial Manufacturing Conditions:")

for fact in facts:
    print("-", fact)


# ============================================================
# FORWARD CHAINING
# ============================================================

final_facts = forward_chaining(facts, rules)

print("\nKnowledge Base after Forward Chaining:")

for fact in final_facts:
    print("-", fact)


# ============================================================
# MANUFACTURING DECISION
# ============================================================

print("\n--- Manufacturing Decision ---")

if "production_stop" in final_facts:

    print("Action: STOP PRODUCTION")

elif "stop_machine" in final_facts:

    print("Action: STOP MACHINE")

elif "machine_fault" in final_facts:

    print("Action: MACHINE FAULT DETECTED")

elif "cooling_required" in final_facts:

    print("Action: START COOLING SYSTEM")

elif "inspection_required" in final_facts:

    print("Action: INSPECT MACHINE")

elif "continue_production" in final_facts:

    print("Action: CONTINUE PRODUCTION")

else:

    print("Action: NO ACTION REQUIRED")


# ============================================================
# BACKWARD CHAINING
# ============================================================

print("\n--- Backward Chaining ---")

goal = input(
    "\nEnter goal to verify "
    "(machine_fault/stop_machine/cooling_required/"
    "inspection_required/order_material): "
).lower()


if backward_chaining(goal, facts, rules):

    print("\nGoal", goal, "can be proved.")

else:

    print("\nGoal", goal, "cannot be proved.")