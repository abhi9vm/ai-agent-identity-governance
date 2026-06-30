from rbac import check_access, PERMISSIONS
from audit import write_audit_log, show_audit_log
from approval import requires_approval, add_to_pending, show_pending_requests, manager_decision


class Agent:
    def __init__(self, agent_id, name, role, owner_team):
        self.agent_id   = agent_id
        self.name       = name
        self.role       = role
        self.owner_team = owner_team
        self.status     = "active"

    def request_action(self, action):
        print(f"\nAgent '{self.name}' is requesting: '{action}'")

        allowed = action in PERMISSIONS.get(self.role, [])

        if not allowed:
            print(f"DENY — '{self.role}' role is not permitted to '{action}'")
            write_audit_log(self.agent_id, self.name, action, "DENY")
            return

        if requires_approval(action):
            add_to_pending(self.agent_id, self.name, action)
            write_audit_log(self.agent_id, self.name, action, "PENDING")
        else:
            print(f"ALLOW — '{self.role}' role is permitted to '{action}'")
            write_audit_log(self.agent_id, self.name, action, "ALLOW")


robot1 = Agent("robot_001", "Invoice Bot", "read_only", "Finance Team")
robot2 = Agent("robot_002", "Report Bot",  "writer",    "HR Team")
robot3 = Agent("robot_003", "Cleanup Bot", "admin",     "IT Team")

print("--- Live Access Requests ---")
robot1.request_action("read")
robot2.request_action("write")
robot3.request_action("delete")

show_pending_requests()
manager_decision(0, "APPROVED")
show_audit_log()
