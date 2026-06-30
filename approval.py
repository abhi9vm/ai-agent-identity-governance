import json

PENDING_FILE = "pending_approvals.json"

HIGH_RISK_ACTIONS = ["delete", "export"]

def requires_approval(action):
    return action in HIGH_RISK_ACTIONS


def add_to_pending(agent_id, agent_name, action):
    request = {
        "agent_id":   agent_id,
        "agent_name": agent_name,
        "action":     action,
        "status":     "PENDING"
    }

    try:
        with open(PENDING_FILE, "r") as f:
            requests = json.load(f)
    except FileNotFoundError:
        requests = []

    requests.append(request)

    with open(PENDING_FILE, "w") as f:
        json.dump(requests, f, indent=4)

    print(f"PENDING — Manager approval required: {agent_name} → {action}")


def show_pending_requests():
    try:
        with open(PENDING_FILE, "r") as f:
            requests = json.load(f)
    except FileNotFoundError:
        print("No pending requests.")
        return

    print("\n--- Pending Approvals (Manager Action Required) ---")
    for i, r in enumerate(requests):
        print(f"{i+1}. {r['agent_name']} requests '{r['action']}' — Status: {r['status']}")


def manager_decision(index, decision):
    """Manager approves or rejects a pending request."""
    with open(PENDING_FILE, "r") as f:
        requests = json.load(f)

    requests[index]["status"] = decision 

    with open(PENDING_FILE, "w") as f:
        json.dump(requests, f, indent=4)

    print(f"MANAGER DECISION — {decision}: {requests[index]['agent_name']} → {requests[index]['action']}")