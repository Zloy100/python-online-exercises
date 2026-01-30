def run_command(cmd):
    match cmd:
        case "start": return "STARTED"
        case "stop": return "STOPPED"
        case "status": return "RUNNING"
        case _: return "UNKNOWN_COMMAND"

for c in ["start", "stop", "x"]:
    print(run_command(c))
