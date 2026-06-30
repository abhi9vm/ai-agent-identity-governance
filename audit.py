import json
from datetime import datetime

LOG_FILE = "audit_log.json"

def write_audit_log(agent_id, agent_name, action, decision):

    entry = {
        "agent_id":   agent_id,
        "agent_name": agent_name,
        "action":     action,
        "decision":   decision,
        "time":       datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    try:
        with open(LOG_FILE, "r") as f:
            logs = json.load(f)
    except FileNotFoundError:
        logs = []

    logs.append(entry)

    with open(LOG_FILE, "w") as f:
        json.dump(logs, f, indent=4)

    print(f"AUDIT LOG — {agent_name} | {action} | {decision}")


def show_audit_log():
    """Displays the full audit trail."""
    try:
        with open(LOG_FILE, "r") as f:
            logs = json.load(f)
    except FileNotFoundError:
        print("Audit log is empty.")
        return

    print("\nFull Audit Log ")
    for entry in logs:
        print(f"{entry['time']} | {entry['agent_name']} | {entry['action']} | {entry['decision']}")