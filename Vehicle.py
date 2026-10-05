# ============================================================
# CATEGORY 8 - 2
# AUTONOMOUS VEHICLE USING KNOWLEDGE BASE
# Facts, Rules, Forward Chaining and Backward Chaining
# ============================================================


# -----------------------------
# INITIAL FACTS
# -----------------------------

facts = {
    "green_light",
    "road_clear"
}


# -----------------------------
# RULES
# -----------------------------

rules = [
    ({"red_light"}, "stop"),
    ({"pedestrian_present"}, "stop"),
    ({"obstacle_detected"}, "avoid_obstacle"),
    ({"green_light", "road_clear"}, "move"),
    ({"obstacle_detected", "road_clear"}, "slow_down"),
    ({"rain", "road_wet"}, "reduce_speed"),
    ({"traffic_jam"}, "slow_down"),
    ({"emergency_vehicle"}, "give_way")
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

    # Goal is already a fact
    if goal in facts:
        return True

    # Prevent loops
    if goal in visited:
        return False

    visited.add(goal)

    # Search for a rule that produces the goal
    for conditions, conclusion in rules:

        if conclusion == goal:

            print(
                "Checking:",
                " AND ".join(conditions),
                "->",
                conclusion
            )

            # All conditions must be satisfied
            if all(
                backward_chaining(condition, facts, rules, visited)
                for condition in conditions
            ):
                return True

    return False


# ============================================================
# MAIN PROGRAM
# ============================================================

print("Initial Vehicle Environment:")

for fact in facts:
    print("-", fact)


# Forward chaining
final_facts = forward_chaining(facts, rules)

print("\nKnowledge Base after Forward Chaining:")

for fact in final_facts:
    print("-", fact)


# -----------------------------
# VEHICLE DECISION
# -----------------------------

print("\n--- Vehicle Decision ---")

if "stop" in final_facts:
    print("Vehicle Action: STOP")

elif "avoid_obstacle" in final_facts:
    print("Vehicle Action: AVOID OBSTACLE")

elif "slow_down" in final_facts:
    print("Vehicle Action: SLOW DOWN")

elif "reduce_speed" in final_facts:
    print("Vehicle Action: REDUCE SPEED")

elif "move" in final_facts:
    print("Vehicle Action: MOVE FORWARD")

else:
    print("Vehicle Action: WAIT")


# ============================================================
# BACKWARD CHAINING
# ============================================================

print("\n--- Backward Chaining ---")

goal = input(
    "\nEnter action to verify "
    "(move/stop/slow_down/avoid_obstacle): "
).lower()

if backward_chaining(goal, facts, rules):

    print("\nGoal", goal, "can be proved.")

else:

    print("\nGoal", goal, "cannot be proved.")