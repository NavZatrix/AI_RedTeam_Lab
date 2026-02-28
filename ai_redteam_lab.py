
# ai_redteam_lab_v2.py
# Interactive home lab with behavioral drift

from attacks_library import ATTACKS

class MockAgent:
    def run(self, user_id, payload, steps=1):
        output = f"[MOCK] Running '{payload}' for {steps} steps"
        return output

agent = MockAgent()
user_id = "user1"

print("=== Interactive AI Red Team Lab ===")
for attack in ATTACKS:
    steps = 3 if attack['type']=="behavioral_drift" else 1
    print(f"Running attack: {attack['name']} ({attack['type']})")
    print(agent.run(user_id, attack['payload'], steps=steps))
