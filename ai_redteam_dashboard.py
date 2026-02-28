
# ai_redteam_dashboard.py
# Final version with Matplotlib dashboard

import matplotlib.pyplot as plt
from attacks_library import ATTACKS

class MockAgent:
    def run(self, user_id, payload, steps=1):
        drift_steps = 2 if "drift" in payload.lower() else 0
        return f"[MOCK] {payload}", drift_steps

class RedTeam:
    def __init__(self, agent, user_id):
        self.agent = agent
        self.user_id = user_id
        self.report = []

    def run_all_attacks(self, attacks_list):
        for attack in attacks_list:
            steps = 3 if attack['type']=="behavioral_drift" else 1
            output, drift_steps = self.agent.run(self.user_id, attack['payload'], steps=steps)
            success = True if "ignore" in attack['payload'].lower() else False
            severity = "High" if attack['type']=="behavioral_drift" else "Medium"
            self.report.append({
                "Attack": attack['name'],
                "Type": attack['type'],
                "Payload": attack['payload'],
                "Success": success,
                "Severity": severity,
                "DriftSteps": drift_steps
            })
            print(f"Ran {attack['name']} - Success: {success}")

    def show_dashboard(self):
        types = [entry['Type'] for entry in self.report]
        drift = [entry['DriftSteps'] for entry in self.report]
        # Success rate per type
        from collections import Counter
        counter = Counter(types)
        success_counter = {t:0 for t in counter}
        total_counter = {t:0 for t in counter}
        for entry in self.report:
            total_counter[entry['Type']] += 1
            if entry['Success']:
                success_counter[entry['Type']] += 1
        plt.figure(figsize=(10,4))
        plt.bar(success_counter.keys(), [success_counter[t]/total_counter[t]*100 for t in success_counter])
        plt.title("Attack Success Rate (%) by Type")
        plt.show()
        plt.figure(figsize=(10,4))
        plt.bar(counter.keys(), [sum(entry['DriftSteps'] for entry in self.report if entry['Type']==t) for t in counter])
        plt.title("Total Drift Steps by Type")
        plt.show()

agent = MockAgent()
redteam = RedTeam(agent, "user1")
redteam.run_all_attacks(ATTACKS)
redteam.show_dashboard()
