PERMISSIONS = {
    "read_only": ["read"],
    "writer":    ["read", "write"],
    "admin":     ["read", "write", "delete"]
}

def check_access(role, action):
    allowed = PERMISSIONS.get(role, [])

    if action in allowed:
        print(f"ALLOW — '{role}' role is permitted to '{action}'")
    else:
        print(f"DENY — '{role}' role is not permitted to '{action}'")