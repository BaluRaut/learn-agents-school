"""A REAL agent in pure Python — the whole loop, readable. (Lessons 02–07)

think → act → observe → repeat, with tools, a scratchpad, and guardrails.
The "brain" is swappable:

    python3 agent/agent.py            # a scripted toy brain solves the picnic goal
    python3 agent/agent.py --drive    # YOU are the brain: pick every action

Swap ScriptedBrain for an LLM API call and this becomes a production-shaped
agent harness — that's the point: the LOOP is the agent; the model is a part.
"""
import ast
import json
import math
import operator as op
import sys

# ══════════════════════ 1) THE TOOLS 🧰 (lesson 03) ══════════════════════
# Read-tools flow freely; WRITE-tools are gated by the harness (lesson 05).

SCHOOL_DB = {
    "class 3A": "Class 3A has 12 students.",
    "class 3B": "Class 3B has 11 students.",
    "picnic rules": "School rule: order 1 pizza per 3 students, round UP. 🍕",
}

_ALLOWED = {ast.Add: op.add, ast.Sub: op.sub, ast.Mult: op.mul,
            ast.Div: op.truediv, ast.USub: op.neg, ast.Pow: op.pow}

def _safe_eval(node):
    """A calculator that can't be tricked into running code (lesson 05!)."""
    if isinstance(node, ast.Expression):
        return _safe_eval(node.body)
    if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)):
        return node.value
    if isinstance(node, ast.BinOp) and type(node.op) in _ALLOWED:
        return _ALLOWED[type(node.op)](_safe_eval(node.left), _safe_eval(node.right))
    if isinstance(node, ast.UnaryOp) and type(node.op) in _ALLOWED:
        return _ALLOWED[type(node.op)](_safe_eval(node.operand))
    if (isinstance(node, ast.Call) and isinstance(node.func, ast.Name)
            and node.func.id == "ceil" and len(node.args) == 1):
        return math.ceil(_safe_eval(node.args[0]))
    raise ValueError("only numbers, + - * / **, and ceil() are allowed")

def tool_calc(args):
    return str(_safe_eval(ast.parse(args["expression"], mode="eval")))

def tool_lookup(args):
    topic = args["topic"].lower()
    for key, fact in SCHOOL_DB.items():
        if key.lower() in topic or topic in key.lower():
            return fact
    return f"No entry for {args['topic']!r}. Known topics: {list(SCHOOL_DB)}"

def tool_write_note(args):
    with open("note.txt", "a") as f:
        f.write(args["text"] + "\n")
    return f"📝 wrote to note.txt: {args['text']!r}"

TOOLS = {
    "calc":       {"fn": tool_calc,       "writes": False,
                   "help": 'calc {"expression": "ceil((12+11)/3)"} — safe math'},
    "lookup":     {"fn": tool_lookup,     "writes": False,
                   "help": 'lookup {"topic": "class 3A"} — the school database'},
    "write_note": {"fn": tool_write_note, "writes": True,
                   "help": 'write_note {"text": "..."} — WRITES a file (gated!)'},
    "done":       {"fn": None,            "writes": False,
                   "help": 'done {"answer": "..."} — finish with your answer'},
}

# ══════════════════════ 2) THE BRAINS 🧠 ══════════════════════
class ScriptedBrain:
    """A toy planner so the demo runs without an API key. A real agent
    replaces THIS CLASS with one LLM call: 'here is the goal + scratchpad
    + tool list — what next?' (AI course L11). Everything else stays."""

    def decide(self, goal, scratchpad):
        seen = "\n".join(scratchpad)
        if "3A has" not in seen:
            return "lookup", {"topic": "class 3A"}, "how many kids in 3A?"
        if "3B has" not in seen:
            return "lookup", {"topic": "class 3B"}, "and in 3B?"
        if "1 pizza per 3" not in seen:
            return "lookup", {"topic": "picnic rules"}, "what's the pizza rule?"
        if "[calc" not in seen:
            return "calc", {"expression": "ceil((12+11)/3)"}, "apply the rule"
        if "wrote to note.txt" not in seen:
            return "write_note", {"text": "Picnic plan: order 8 pizzas for 23 kids."}, "save the plan"
        return "done", {"answer": "Order 8 pizzas 🍕 (23 kids, 1 per 3, rounded up). Plan saved."}, "all steps done"

class HumanBrain:
    """--drive mode: you ARE the model. Feel the loop from the inside."""

    def decide(self, goal, scratchpad):
        print("   🧰 tools: " + " · ".join(t["help"] for t in TOOLS.values()))
        raw = input("   🧠 your move> ").strip()
        name, _, arg_str = raw.partition(" ")
        return name, json.loads(arg_str or "{}"), "(human decision)"

# ══════════════════════ 3) THE LOOP 🔁 (lesson 02) + GUARDRAILS 🚧 (lesson 05) ══
MAX_STEPS = 8          # runaway protection: no infinite loops on my lunch money

def run(goal, brain, auto_approve=False):
    print(f"📋 GOAL: {goal}\n")
    scratchpad = []                                   # the memory (lesson 04)
    for step in range(1, MAX_STEPS + 1):
        name, args, thought = brain.decide(goal, scratchpad)
        print(f"── step {step} ─ THINK 💭 {thought}")
        print(f"           ACT   🧰 {name} {json.dumps(args)}")

        if name == "done":
            print(f"\n✅ ANSWER: {args.get('answer','(none)')}")
            return
        if name not in TOOLS:
            observation = f"unknown tool {name!r} — try one of {list(TOOLS)}"
        elif TOOLS[name]["writes"] and not auto_approve:   # 🚧 the write gate
            ok = input(f"           GATE  🚧 '{name}' CHANGES things. Allow? [y/N] ")
            observation = TOOLS[name]["fn"](args) if ok.lower() == "y" \
                else "❌ denied by the human — pick another way"
        else:
            try:
                observation = TOOLS[name]["fn"](args)
            except Exception as e:
                observation = f"tool error: {e}"       # errors are data (MCP L06!)
        print(f"           LOOK  👀 {observation}\n")
        scratchpad.append(f"[{name} {json.dumps(args)}] -> {observation}")

    print(f"🛑 stopped: hit MAX_STEPS={MAX_STEPS} — a guardrail, not a bug (lesson 05)")

if __name__ == "__main__":
    drive = "--drive" in sys.argv
    run(goal="How many pizzas for the class picnic (3A + 3B)? Save the plan to a note.",
        brain=HumanBrain() if drive else ScriptedBrain(),
        auto_approve="--yes" in sys.argv)
