
# ai_redteam_report_export.py
# Automated red team execution with CSV & HTML reporting

import csv
from attacks_library import ATTACKS

class MockAgent:
    def run(self, user_id, payload, steps=1):
        return f"[MOCK] {payload}", steps

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

    def export_csv(self, filename="redteam_report.csv"):
        keys = ["Attack","Type","Payload","Success","Severity","DriftSteps"]
        with open(filename, "w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=keys)
            writer.writeheader()
            writer.writerows(self.report)

    def export_html(self, filename="redteam_report.html"):
        html = "<html><body><table border='1'>"
        html += "<tr><th>Attack</th><th>Type</th><th>Success</th><th>Severity</th><th>DriftSteps</th></tr>"
        for entry in self.report:
            html += f"<tr><td>{entry['Attack']}</td><td>{entry['Type']}</td><td>{entry['Success']}</td><td>{entry['Severity']}</td><td>{entry['DriftSteps']}</td></tr>"
        html += "</table></body></html>"
        with open(filename,"w") as f:
            f.write(html)

agent = MockAgent()
redteam = RedTeam(agent, "user1")
redteam.run_all_attacks(ATTACKS)
redteam.export_csv()
redteam.export_html()
