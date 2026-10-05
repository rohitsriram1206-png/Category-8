# ============================================================
# CATEGORY 8 - 1
# MEDICAL DIAGNOSIS USING KNOWLEDGE BASE
# Facts, Rules, Forward Chaining and Backward Chaining
# ============================================================


# -----------------------------
# KNOWLEDGE BASE
# -----------------------------

facts = {
    "fever",
    "cough",
    "body_pain"
}


rules = [
    ({"fever", "cough", "body_pain"}, "flu"),
    ({"fever", "cough"}, "respiratory_infection"),
    ({"fever", "rash"}, "measles"),
    ({"cough", "breathing_problem"}, "bronchitis"),
    ({"fever", "headache"}, "viral_fever"),
    ({"sore_throat", "cough"}, "throat_infection")
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

            # Check whether all conditions are satisfied
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

    # Goal is already known
    if goal in facts:
        return True

    # Avoid infinite loops
    if goal in visited:
        return False

    visited.add(goal)

    # Find rules that can conclude the goal
    for conditions, conclusion in rules:

        if conclusion == goal:

            print(
                "Checking rule:",
                " AND ".join(conditions),
                "->",
                conclusion
            )

            # Check whether every condition can be proved
            if all(
                backward_chaining(condition, facts, rules, visited)
                for condition in conditions
            ):
                return True

    return False


# ============================================================
# MAIN PROGRAM
# ============================================================

print("Initial Patient Symptoms:")

for fact in facts:
    print("-", fact)


# Forward chaining
final_facts = forward_chaining(facts, rules)

print("\nFacts after Forward Chaining:")

for fact in final_facts:
    print("-", fact)


# Diagnosis
print("\n--- Diagnosis ---")

if "flu" in final_facts:
    print("Possible Diagnosis: FLU")

elif "measles" in final_facts:
    print("Possible Diagnosis: MEASLES")

elif "bronchitis" in final_facts:
    print("Possible Diagnosis: BRONCHITIS")

elif "viral_fever" in final_facts:
    print("Possible Diagnosis: VIRAL FEVER")

else:
    print("Diagnosis could not be determined.")


# Backward chaining
print("\n--- Backward Chaining ---")

goal = input(
    "\nEnter disease to verify "
    "(flu/measles/bronchitis/viral_fever): "
).lower()

if backward_chaining(goal, facts, rules):
    print("\nGoal", goal, "can be proved.")

else:
    print("\nGoal", goal, "cannot be proved.")