#!/usr/bin/env python3
"""Generate the learn-agents-school docs: index, lesson-diagrams, patterns."""
GH = "https://github.com/BaluRaut/learn-agents-school/blob"
P1, P2 = "#0d9488", "#be123c"

L = [
 (1,"lesson-01-what-is-an-agent","01-what-is-an-agent","📋 What is an agent","Answers vs outcomes — the reciter vs the doer with a hall pass.",35,P1),
 (2,"lesson-02-the-loop","02-the-loop","🔁 The loop","Think → act → observe — how you run errands, and how agents do.",35,P1),
 (3,"lesson-03-tools","03-tools","🧰 Tools","The belt: labels are half the intelligence; reads flow, writes gate.",40,P1),
 (4,"lesson-04-memory","04-memory","📔 Memory","Scratchpad, the small desk, compaction — and the homework diary.",40,P1),
 (5,"lesson-05-guardrails","05-guardrails","🚧 Guardrails","Field-trip rules: curfew, write gates, hardened tools, full logs.",40,P1),
 (6,"lesson-06-failures","06-failures","💥 Failure modes","Confidently wrong, with momentum — five ways it breaks, and evals.",45,P2),
 (7,"lesson-07-build-an-agent","07-build-an-agent","🔬 Build an agent","Read agent.py whole: 130 lines, every concept at a line number.",45,P2),
 (8,"lesson-08-patterns","08-patterns","🌍 Agent patterns","Planners, critics, teams, human gates — and when NOT to.",40,P2),
]

BASE_CSS = """
  :root { --bg:#f8fafc; --card:#fff; --ink:#0f172a; --muted:#475569; --line:#e2e8f0; --accent:#0d9488; --ok:#16a34a; --blue:#2563eb; }
  @media (prefers-color-scheme: dark) { :root { --bg:#0b1220; --card:#131c2e; --ink:#e2e8f0; --muted:#94a3b8; --line:#253349; } }
  * { margin:0; padding:0; box-sizing:border-box; }
  body { background:var(--bg); color:var(--ink); font-family:-apple-system,"Segoe UI",Helvetica,Arial,sans-serif; line-height:1.6; }
  .wrap { max-width:1280px; margin:0 auto; padding:28px 20px 60px; }
  @media (min-width: 1660px) { .wrap { max-width: 1580px; } }
  a { color:var(--blue); } h1 { font-size:2rem; line-height:1.25; } h2 { font-size:1.4rem; margin:44px 0 6px; }
  .sub { color:var(--muted); max-width:74ch; }
  .chips { display:flex; flex-wrap:wrap; gap:8px; margin:16px 0 8px; }
  .chip { border:1px solid var(--line); background:var(--card); border-radius:999px; padding:6px 14px; font-size:.85rem; color:var(--muted); }
  .grid { display:grid; grid-template-columns:repeat(auto-fill,minmax(240px,1fr)); gap:14px; margin-top:16px; }
  .lesson { background:var(--card); border:1px solid var(--line); border-top:5px solid var(--c,var(--accent)); border-radius:14px; padding:16px; display:flex; flex-direction:column; gap:6px; }
  .lesson .top { display:flex; align-items:center; gap:10px; }
  .lesson .num { flex:none; width:30px; height:30px; border-radius:50%; background:var(--c,var(--accent)); color:#fff; display:inline-flex; align-items:center; justify-content:center; font-weight:800; font-size:.9rem; }
  .lesson h3 { font-size:1.02rem; line-height:1.3; } .lesson .ana { color:var(--muted); font-size:.9rem; }
  .lesson code { font-size:.78rem; background:var(--bg); border:1px solid var(--line); border-radius:6px; padding:1px 6px; }
  .lesson a.go { margin-top:auto; font-weight:600; font-size:.9rem; text-decoration:none; } .lesson a.go+a.go { margin-top:0; } .lesson a.go:hover { text-decoration:underline; }
  .callout { background:var(--card); border:1px solid var(--line); border-left:6px solid var(--ok); border-radius:14px; padding:18px 20px; margin-top:16px; }
  pre { background:var(--card); border:1px solid var(--line); border-radius:12px; padding:14px 16px; overflow-x:auto; font-size:.88rem; margin-top:12px; }
  .btn { display:inline-block; background:var(--accent); color:#fff; border-radius:10px; padding:10px 18px; text-decoration:none; font-weight:700; margin:14px 10px 0 0; }
  .btn.alt { background:transparent; color:var(--ink); border:1px solid var(--line); }
  .vs { display:grid; grid-template-columns:repeat(auto-fit,minmax(280px,1fr)); gap:14px; margin-top:16px; }
  .vcol { background:var(--card); border:1px solid var(--line); border-radius:14px; padding:18px; } .vcol h3 { margin-bottom:8px; }
  .vcol ul { margin-left:18px; color:var(--muted); font-size:.93rem; }
  .toc { display:flex; flex-wrap:wrap; gap:8px; margin:18px 0 6px; }
  .toc a { border:1px solid var(--line); background:var(--card); border-radius:999px; padding:5px 12px; font-size:.82rem; color:var(--muted); text-decoration:none; }
  .toc a:hover { color:var(--ink); border-color:var(--muted); }
  footer { margin-top:56px; border-top:1px solid var(--line); padding-top:18px; color:var(--muted); font-size:.88rem; }
"""
DSEC_CSS = """
  .dsec { background:var(--card); border:1px solid var(--line); border-top:6px solid var(--c,var(--accent)); border-radius:16px; padding:22px 22px 16px; margin-top:26px; scroll-margin-top:16px; }
  .dsec h2 { font-size:1.25rem; display:flex; align-items:center; gap:10px; }
  .dsec h2 .ln { flex:none; width:32px; height:32px; border-radius:50%; background:var(--c,var(--accent)); color:#fff; display:inline-flex; align-items:center; justify-content:center; font-size:.95rem; font-weight:800; }
  .dsec p.d { color:var(--muted); font-size:.95rem; margin:6px 0 4px; }
  .dsec svg { width:100%; height:auto; display:block; margin-top:10px; } .dsec .foot { margin-top:8px; font-size:.92rem; }
  .box { fill:var(--card); stroke:var(--c,var(--accent)); stroke-width:2; }
  .soft { fill:var(--bg); stroke:var(--line); stroke-width:1.5; }
  .dead { fill:var(--bg); stroke:var(--muted); stroke-width:1.5; stroke-dasharray:6 5; }
  .t { font:600 14px -apple-system,"Segoe UI",sans-serif; fill:var(--ink); }
  .s { font:12px -apple-system,"Segoe UI",sans-serif; fill:var(--muted); } .m { text-anchor:middle; }
  .arr { stroke:#64748b; stroke-width:2; fill:none; marker-end:url(#arw); } .dash { stroke-dasharray:6 5; }
  .life { stroke:#94a3b8; stroke-width:1.5; stroke-dasharray:4 5; }
  .nc { fill:var(--c,var(--accent)); } .nt { font:700 12px -apple-system,sans-serif; fill:#fff; text-anchor:middle; }
"""
MARKER = '<svg width="0" height="0" style="position:absolute"><defs><marker id="arw" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0 L10 5 L0 10 z" fill="#64748b"/></marker></defs></svg>'

def head(title, desc):
    return (f'<!DOCTYPE html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n'
      f'<meta name="viewport" content="width=device-width, initial-scale=1">\n<title>{title}</title>\n'
      f'<meta name="description" content="{desc}">\n<style>{BASE_CSS}{DSEC_CSS}</style>\n</head>\n<body>\n')

B='<rect class="box"'; S='<rect class="soft"'; D='<rect class="dead"'; DASH=' dash'
def t(x,y,s): return f'<text class="t m" x="{x}" y="{y}">{s}</text>'
def sm(x,y,s): return f'<text class="s m" x="{x}" y="{y}">{s}</text>'
def num(x,y,n): return f'<g transform="translate({x},{y})"><circle r="11" class="nc"/><text class="nt" dy="4">{n}</text></g>'
def arr(a,b,c,d,dash=""): return f'<line class="arr{dash}" x1="{a}" y1="{b}" x2="{c}" y2="{d}"/>'

def seq(participants, messages, note=None):
    W = 940
    xs = [int(W*(i+0.5)/len(participants)) for i in range(len(participants))]
    y = 96; body = []; out = []
    for m in messages:
        if m[0] == 'note':
            body.append(f'<rect class="soft" x="90" y="{y-16}" width="{W-180}" height="30" rx="8"/>' + sm(W//2, y+4, m[1]))
            y += 46; continue
        frm, to, n, label = m
        x1, x2 = xs[frm], xs[to]
        if frm == to:
            body.append(arr(x1, y, x1+70, y) + arr(x1+70, y, x1+70, y+18) + arr(x1+70, y+18, x1+4, y+18))
            body.append(sm(x1+170, y+10, label)); body.append(num(x1-20, y, n)); y += 46
        else:
            dash = DASH if x2 < x1 else ""
            body.append(arr(x1, y, x2 + (-6 if x2>x1 else 6), y, dash))
            body.append(sm((x1+x2)//2, y-10, label)); body.append(num((x1+x2)//2, y+16, n)); y += 46
    H = y + 20
    for i, p in enumerate(participants):
        out.append(f'<rect class="box" x="{xs[i]-85}" y="16" width="170" height="44" rx="10"/>' + t(xs[i], 44, p))
        out.append(f'<line class="life" x1="{xs[i]}" y1="60" x2="{xs[i]}" y2="{H-10}"/>')
    if note: out.append(sm(W//2, H-2, note)); H += 14
    return f'<svg viewBox="0 0 {W} {H}" role="img">' + "".join(out) + "".join(body) + '</svg>'

SVG = {}
SVG[1]=(f'<svg viewBox="0 0 940 300" role="img">{D} x="40" y="60" width="380" height="180" rx="14"/>{t(230,95,"🗣️ chatbot — answers")}{sm(230,125,"&#39;how many pizzas?&#39; →")}{sm(230,147,"&#39;probably 6-8?&#39; — words,")}{sm(230,169,"from memory, maybe wrong")}{num(40,60,1)}'
 f'{B} x="480" y="40" width="420" height="220" rx="14"/>{t(690,75,"📋 agent — outcomes")}{S} x="505" y="95" width="170" height="60" rx="10"/>{sm(590,120,"🧠 model in a LOOP")}{sm(590,142,"think→act→observe")}{S} x="700" y="95" width="175" height="60" rx="10"/>{sm(787,120,"🧰 tools + 🎫 hall pass")}{sm(787,142,"lookup · calc · write")}'
 f'{sm(690,190,"✅ counted 23 kids, computed 8 pizzas,")}{sm(690,212,"SAVED the plan — the job is DONE")}{num(480,40,2)}'
 f'{arr(675,125,696,125)}{sm(470,290,"same brain — the difference is the loop and the pass · run it: python3 agent/agent.py")}{num(105,290,3)}</svg>')
SVG[2]=seq(["🧠 brain","🏫 harness","🌍 world"],
 [(0,0,1,"THINK 💭 'need the class size' — reasoning as text"),
  (0,1,2,'ACT 🧰 lookup {"topic":"class 3A"}'),
  (1,2,3,"executes the tool"),
  (2,1,4,"'Class 3A has 12 students.'"),
  (1,0,5,"OBSERVE 👀 → onto the scratchpad"),
  ('note',"🔁 repeat, smarter each beat — until done {answer} (or MAX_STEPS 🕐)")],
 "the THINK beat is next-token prediction; the loop is a conversation with reality")
SVG[3]=(f'<svg viewBox="0 0 940 300" role="img">{B} x="40" y="40" width="280" height="220" rx="14"/>{t(180,72,"🧰 the belt (TOOLS)")}{S} x="65" y="90" width="230" height="45" rx="8"/>{sm(180,118,"lookup — READ · &#39;ask the office&#39;")}{S} x="65" y="145" width="230" height="45" rx="8"/>{sm(180,173,"calc — READ · &#39;safe math&#39;")}{S} x="65" y="200" width="230" height="45" rx="8"/>{sm(180,228,"write_note — WRITE 🚧 gated!")}{num(40,40,1)}'
 f'{B} x="390" y="70" width="240" height="100" rx="12"/>{t(510,102,"🧠 model")}{sm(510,128,"picks by READING the labels —")}{sm(510,150,"labels are half the intelligence")}{num(390,70,2)}'
 f'{B} x="700" y="70" width="210" height="100" rx="12"/>{t(805,102,"🏫 harness")}{sm(805,128,"executes · gates writes ·")}{sm(805,150,"returns observations")}{num(700,70,3)}'
 f'{arr(320,140,386,120)}{arr(630,120,696,120)}{arr(805,170,510,230,DASH)}{sm(660,225,"observation → the desk")}'
 f'{sm(470,285,"never eval() what a model wrote — see _safe_eval: an allowlist, not trust 🔒")}</svg>')
SVG[4]=(f'<svg viewBox="0 0 940 300" role="img">{B} x="40" y="40" width="440" height="180" rx="14"/>{t(260,72,"🪑 the desk — finite!")}{S} x="65" y="90" width="180" height="50" rx="8"/>{sm(155,120,"📋 goal + to-do")}{S} x="260" y="90" width="195" height="50" rx="8"/>{sm(357,112,"📔 scratchpad:")}{sm(357,132,"[lookup 3A]→12 kids…")}'
 f'{S} x="65" y="155" width="390" height="45" rx="8"/>{sm(260,183,"💭 THINK reads all of it, every beat")}{num(40,40,1)}'
 f'{B} x="550" y="40" width="360" height="80" rx="12"/>{t(730,68,"🗜️ compaction")}{sm(730,94,"10 jottings → 1 summary line, when the desk fills")}{num(550,40,2)}'
 f'{B} x="550" y="140" width="360" height="80" rx="12"/>{t(730,168,"📁 durable memory OUTSIDE")}{sm(730,194,"write_note / files / DB / RAG over past runs")}{num(550,140,3)}'
 f'{arr(480,130,546,80,DASH)}{arr(480,160,546,180)}{sm(470,275,"&#39;it forgot step 3&#39; and &#39;it falls apart after 30 steps&#39; are BOTH desk problems — now you know the fix first")}</svg>')
SVG[5]=(f'<svg viewBox="0 0 940 300" role="img">{B} x="330" y="30" width="280" height="70" rx="12"/>{t(470,58,"🔁 the loop wants to run forever,")}{sm(470,84,"touch everything, trust every input")}'
 f'{B} x="40" y="140" width="260" height="60" rx="12"/>{sm(170,165,"🕐 MAX_STEPS + budgets")}{sm(170,187,"bounded loops, bounded bills")}{num(40,140,1)}'
 f'{B} x="330" y="140" width="280" height="60" rx="12"/>{sm(470,165,"🚧 write gates — reads flow,")}{sm(470,187,"writes wait for a human [y/N]")}{num(330,140,2)}'
 f'{B} x="640" y="140" width="270" height="60" rx="12"/>{sm(775,165,"🔒 hardened tools + scoped creds")}{sm(775,187,"allowlists, least privilege (AWS L03)")}{num(640,140,3)}'
 f'{B} x="180" y="220" width="270" height="60" rx="12"/>{sm(315,245,"🧾 full logs — every beat,")}{sm(315,267,"numbered, replayable")}{num(180,220,4)}'
 f'{B} x="490" y="220" width="270" height="60" rx="12"/>{sm(625,245,"📦 sandboxes — blast radius")}{sm(625,267,"= one container 🍱")}{num(490,220,5)}'
 f'{arr(400,100,220,136)}{arr(470,100,470,136)}{arr(540,100,720,136)}</svg>')
SVG[6]=(f'<svg viewBox="0 0 940 300" role="img">{D} x="40" y="30" width="270" height="70" rx="12"/>{sm(175,55,"💥 compounding: wrong fact at step 2")}{sm(175,77,"→ polished wrong answer at step 9")}{num(40,30,1)}'
 f'{D} x="340" y="30" width="270" height="70" rx="12"/>{sm(475,55,"🔄 loops: the same act,")}{sm(475,77,"again and again and again")}{num(340,30,2)}'
 f'{D} x="640" y="30" width="270" height="70" rx="12"/>{sm(775,55,"📝 injection: instructions")}{sm(775,77,"hiding inside tool results")}{num(640,30,3)}'
 f'{D} x="190" y="115" width="270" height="70" rx="12"/>{sm(325,140,"🎯 goal drift:")}{sm(325,162,"&#39;helpful&#39; side quests")}{num(190,115,4)}'
 f'{D} x="490" y="115" width="270" height="70" rx="12"/>{sm(625,140,"🙋 fake done: declared success,")}{sm(625,162,"no actual outcome")}{num(490,115,5)}'
 f'{B} x="190" y="210" width="570" height="70" rx="14"/>{t(475,238,"📊 EVALS — scored scenarios, run on every change")}{sm(475,262,"outcome checks · step budgets · gate audits · a deterministic world to assert against")}'
 f'{arr(325,185,400,206)}{arr(625,185,550,206)}{arr(175,100,300,215,DASH)}{arr(775,100,650,215,DASH)}</svg>')
SVG[7]=(f'<svg viewBox="0 0 940 300" role="img">{B} x="40" y="50" width="270" height="200" rx="14"/>{t(175,82,"1 🧰 TOOLS")}{sm(175,110,"the belt: labels + writes-flags")}{sm(175,132,"+ _safe_eval (hardened)")}{sm(175,160,"SCHOOL_DB = a deterministic")}{sm(175,182,"world — evals assert against it")}{num(40,50,1)}'
 f'{B} x="340" y="50" width="270" height="200" rx="14"/>{t(475,82,"2 🧠 BRAINS — swappable")}{sm(475,110,"ScriptedBrain: toy planner")}{sm(475,132,"HumanBrain: --drive (you!)")}{sm(475,164,"← ONE LLM call slots here;")}{sm(475,186,"the harness never changes")}{num(340,50,2)}'
 f'{B} x="640" y="50" width="270" height="200" rx="14"/>{t(775,82,"3 🔁 run() — the loop")}{sm(775,110,"MAX_STEPS curfew 🕐")}{sm(775,132,"write gate 🚧 (one if!)")}{sm(775,154,"errors-as-observations")}{sm(775,176,"scratchpad.append = memory")}{sm(775,204,"prints every beat 🧾")}{num(640,50,3)}'
 f'{sm(470,285,"~130 lines, no framework — every framework is this file with more adjectives")}</svg>')
SVG[8]=(f'<svg viewBox="0 0 940 300" role="img">{B} x="40" y="40" width="160" height="70" rx="12"/>{sm(120,68,"🙅 steps fixed?")}{sm(120,90,"→ a SCRIPT")}{num(40,40,1)}'
 f'{B} x="230" y="40" width="160" height="70" rx="12"/>{sm(310,68,"🗣️ one answer?")}{sm(310,90,"→ one model call")}{num(230,40,2)}'
 f'{B} x="420" y="40" width="200" height="70" rx="12"/>{sm(520,63,"🧍 path varies by discovery?")}{sm(520,85,"→ SOLO agent + tools")}{sm(520,103,"(start here!)")}{num(420,40,3)}'
 f'{B} x="650" y="40" width="260" height="70" rx="12"/>{sm(780,68,"🗺️ long/structured? + planner")}{sm(780,90,"🧑‍🏫 quality-critical? + critic")}{num(650,40,4)}'
 f'{B} x="230" y="150" width="330" height="70" rx="12"/>{sm(395,175,"🚧 irreversible steps? + human gates")}{sm(395,197,"(always — drafts flow, signatures gate)")}{num(230,150,5)}'
 f'{B} x="590" y="150" width="320" height="70" rx="12"/>{sm(750,175,"👯 truly parallel? + a team —")}{sm(750,197,"with a foreman &amp; checkable artifacts")}{num(590,150,6)}'
 f'{arr(200,75,226,75)}{arr(390,75,416,75)}{arr(620,75,646,75)}{arr(780,110,500,146)}{arr(560,185,586,185)}'
 f'{sm(470,270,"every pattern = the same loop, wrapped — the best architects say &#39;this doesn&#39;t need an agent&#39; weekly 🙅")}</svg>')

def dsec(n):
    _,slug,folder,title,ana,_,color = L[n-1]
    return (f'\n<section class="dsec" id="l{n:02d}" style="--c:{color}">\n'
      f'  <h2><span class="ln">{n}</span> {title}</h2>\n  <p class="d">{ana}</p>\n  {SVG[n]}\n'
      f'  <p class="foot"><a href="{GH}/{slug}/lessons/{folder}/README.md">Read full lesson {n:02d} →</a></p>\n</section>\n')
ALL_DSECS = "".join(dsec(n) for n in range(1,9))

def card(n):
    _,slug,folder,title,ana,_,color = L[n-1]
    return (f'    <div class="lesson" style="--c:{color}"><div class="top"><span class="num">{n}</span><h3>{title}</h3></div>'
      f'<span class="ana">{ana}</span><code>{slug}</code>'
      f'<a class="go" href="{GH}/{slug}/lessons/{folder}/README.md">Read lesson →</a>'
      f'<a class="go" href="lesson-diagrams.html#l{n:02d}">See the diagram ↗</a></div>')

INDEX = head("Learn AI Agents the school way — with a runnable agent",
  "8 lessons on AI agents with a real zero-dependency agent in the repo: the think-act-observe loop, tools, memory, guardrails, failure modes, and 5 patterns with sequence diagrams.") + MARKER + f'''
<div class="wrap">
  <header>
    <h1>📋 Learn AI Agents the school way</h1>
    <p class="sub">Chatbots answer; <b>agents achieve</b>. This school teaches the loop that makes the
    difference — and ships it: <b>a real agent in the repo</b>, ~130 lines of pure Python, zero
    dependencies, no API key. Run it, drive it, break it, eval it, read every line.</p>
    <div class="chips">
      <span class="chip">🔁 think→act→observe</span><span class="chip">🧰 tools &amp; belts</span>
      <span class="chip">📔 memory</span><span class="chip">🚧 guardrails</span>
      <span class="chip">💥 failure modes</span><span class="chip">👯 5 patterns</span>
    </div>
  </header>

  <div class="vs">
    <div class="vcol" style="border-top:5px solid {P1}">
      <h3>🔁 Part 1 — THE MACHINE (1–5)</h3>
      <ul>
        <li>answers vs outcomes — the doer with a hall pass 🎫</li>
        <li>the loop: think → act → observe, on repeat</li>
        <li>the belt: labels are half the intelligence 🧰</li>
        <li>the pad, the small desk — and the field-trip rules 🚧</li>
      </ul>
    </div>
    <div class="vcol" style="border-top:5px solid {P2}">
      <h3>💥 Part 2 — REALITY (6–8)</h3>
      <ul>
        <li>five failure modes + the evals that catch them 📊</li>
        <li>read the agent whole: 130 honest lines 🔬</li>
        <li>patterns: planners, critics, teams, human gates 👯</li>
        <li>…and the rarest skill: knowing when NOT to 🙅</li>
      </ul>
    </div>
  </div>

  <pre><code># the 60-second wow — a goal becomes an outcome:
git clone https://github.com/BaluRaut/learn-agents-school.git &amp;&amp; cd learn-agents-school
python3 agent/agent.py            # a scripted brain runs the picnic errand
python3 agent/agent.py --drive    # YOU are the brain: pick every action</code></pre>

  <h2 id="big-picture">🗺️ The big picture — one diagram, both worlds</h2>
  <p class="sub">Click for the <a href="images/big-picture-4k.png">4K version</a>.</p>
  <figure style="background:var(--card);border:1px solid var(--line);border-radius:14px;padding:14px;margin-top:16px">
    <a href="images/big-picture-4k.png"><img src="images/big-picture.svg" alt="The big picture: the agent machine (loop, tools, memory, guardrails) and reality (failures, evals, patterns)" loading="lazy" style="width:100%;height:auto;border-radius:8px;background:#fff"></a>
  </figure>

  <h2 id="lessons">🎓 The 8 lessons</h2>
  <p class="sub">One git branch = one idea; branch 05 contains lessons 01–05. Deep-dive companion to
  the <a href="https://baluraut.github.io/learn-ai-school/">AI course</a>'s lesson 11 — and the
  <a href="https://baluraut.github.io/learn-mcp-school/">MCP school</a> supplies the tool belt. Curious how we got here and where it goes? Read <a href="history-and-future.html"><b>before · why · agentic · future</b></a>.</p>
  <div class="grid">
{chr(10).join(card(n) for n in range(1,9))}
  </div>

  <div class="callout">👯 <b>The showcase:</b> <a href="patterns.html">5 agent patterns</a> — solo doer,
  planner+executor, critic loop, human-in-the-loop, the team — each with a numbered flow diagram
  AND a full sequence diagram.</div>

  <h2 id="diagrams">📐 The lesson diagrams — follow the numbers</h2>
  <p class="sub">Teal = the machine, red = reality. Lesson 02 is a sequence diagram — the loop in
  its natural notation. Also on a <a href="lesson-diagrams.html">standalone page</a>.</p>
{ALL_DSECS}
  <a class="btn" href="{GH}/lesson-01-what-is-an-agent/lessons/01-what-is-an-agent/README.md">Start Lesson 01 →</a>
  <a class="btn alt" href="patterns.html">👯 The 5 patterns</a>
  <a class="btn alt" href="history-and-future.html">⏮️ Before · why · agentic · future</a>
  <a class="btn alt" href="lesson-diagrams.html">📐 All 8 lesson diagrams</a>
  <a class="btn alt" href="https://baluraut.github.io/learn-mcp-school/">🔌 The MCP school</a>

  <footer>
    Learn Agents School · the loop is in the repo ·
    <a href="https://github.com/BaluRaut/learn-agents-school">github.com/BaluRaut/learn-agents-school</a> ·
    siblings: <a href="https://baluraut.github.io/learn-ai-school/">AI</a> ·
    <a href="https://baluraut.github.io/learn-mcp-school/">MCP</a>
  </footer>
</div>
</body>
</html>
'''

DIAGRAMS = head("Lesson diagrams — Learn Agents School",
  "All 8 agent lessons as numbered diagrams — the loop, tools, memory, guardrails, failures, patterns.") + MARKER + f'''
<div class="wrap">
<header>
  <p><a href="index.html">← Back to the course home</a></p>
  <h1>📐 The 8 lessons as diagrams</h1>
  <p class="sub">Teal = the machine (1–5) · red = reality (6–8). Follow the circled numbers.</p>
  <nav class="toc">
    <a href="#l01">1 What is an agent</a><a href="#l02">2 The loop</a><a href="#l03">3 Tools</a>
    <a href="#l04">4 Memory</a><a href="#l05">5 Guardrails</a><a href="#l06">6 Failures</a>
    <a href="#l07">7 Build</a><a href="#l08">8 Patterns</a>
  </nav>
</header>
{ALL_DSECS}
<footer>
  Learn Agents School · <a href="index.html">Course home</a> · <a href="patterns.html">Patterns</a> ·
  <a href="https://github.com/BaluRaut/learn-agents-school">GitHub</a>
</footer>
</div>
</body>
</html>
'''

# ---------- patterns page: flow + sequence each ----------
def flow(boxes, arrows, note=None, H=230):
    out = [f'<svg viewBox="0 0 940 {H}" role="img">']
    for (x,y,w,h,title,sub,n) in boxes:
        out.append(f'{B} x="{x}" y="{y}" width="{w}" height="{h}" rx="12"/>' + t(x+w//2, y+30, title) + (sm(x+w//2, y+54, sub) if sub else ""))
        if n: out.append(num(x, y, n))
    for (a,b,c,d,dash) in arrows:
        out.append(arr(a,b,c,d, DASH if dash else ""))
    if note: out.append(sm(470, H-12, note))
    out.append('</svg>')
    return "".join(out)

def pat(idx, id_, title, story, flow_svg, seq_svg, when):
    return f'''
<section class="dsec" id="{id_}" style="--c:{P2}">
  <h2><span class="ln">{idx}</span> {title}</h2>
  <p class="d">{story}</p>
  <p class="sub" style="margin-top:10px"><b>The flow, numbered:</b></p>
  {flow_svg}
  <p class="sub" style="margin-top:14px"><b>The sequence, message by message:</b></p>
  {seq_svg}
  <p class="d" style="margin-top:10px">💡 <b>When it pays for itself:</b> {when}</p>
</section>'''

PT1_FLOW = flow(
 [(30,40,180,70,"📋 goal","one errand",1),(280,40,200,70,"🔁 the loop","think·act·observe",2),
  (550,40,180,70,"🧰 the belt","lookup·calc·write🚧",3),(280,140,200,70,"✅ outcome","+ full log 🧾",4)],
 [(210,75,276,75,0),(480,75,546,75,0),(640,110,420,145,0)],
 "agent/agent.py IS this pattern — most real value ships in this shape")
PT1_SEQ = seq(["🧑 user","🧍 agent","🧰 tools"],
 [(0,1,1,"goal: pizzas + save the plan"),(1,2,2,"lookup / calc — reads flow"),(2,1,3,"facts → pad"),
  (1,0,4,"🚧 'write the note?' — gate"),(0,1,5,"✓ allow"),(1,2,6,"write_note"),(1,0,7,"✅ done: 8 pizzas, plan saved")])
PT2_FLOW = flow(
 [(30,40,200,70,"🗺️ planner","breaks the project down",1),(300,40,220,70,"📋 checklist","1 research · 2 draft · 3 cite",2),
  (590,40,200,70,"🧍 executor(s)","work item by item",3),(300,140,220,70,"✅ assembled result","",4)],
 [(230,75,296,75,0),(520,75,586,75,0),(690,110,470,145,0)],
 "the to-do list from lesson 04, promoted to a first-class artifact")
PT2_SEQ = seq(["🧑 user","🗺️ planner","🧍 executor","🧰 tools"],
 [(0,1,1,"'research report on X'"),(1,1,2,"THINK: decompose into 3 items"),(1,2,3,"item 1: gather sources"),
  (2,3,4,"search / read"),(3,2,5,"sources → pad"),(2,1,6,"item 1 done (artifact!)"),
  ('note',"…items 2 and 3 the same way — plan survives any single item failing…"),(1,0,7,"assembled report 📋")])
PT3_FLOW = flow(
 [(30,40,190,70,"✍️ writer","drafts the code",1),(290,40,220,70,"🧑‍🏫 critic","runs the TESTS (ground truth)",2),
  (580,40,180,70,"❌ feedback","what failed, exactly",3),(290,140,220,70,"✅ pass → ship","",4)],
 [(220,75,286,75,0),(510,75,576,75,0),(670,110,400,136,1),(400,110,400,136,0)],
 "the best critics are merciless and mechanical: test runners, compilers, linters")
PT3_SEQ = seq(["✍️ writer","🧑‍🏫 critic","🧪 tests"],
 [(0,1,1,"draft v1"),(1,2,2,"run the suite"),(2,1,3,"2 failures, with tracebacks"),
  (1,0,4,"feedback: exact failures"),(0,0,5,"THINK: fix both"),(0,1,6,"draft v2"),
  (1,2,7,"run again"),(2,1,8,"all green ✅"),(1,0,9,"pass — ship it")])
PT4_FLOW = flow(
 [(30,40,220,70,"🧍 agent prepares","diff · summary · risks",1),(320,40,220,70,"🚧 human reviews","the ONE irreversible step",2),
  (610,40,150,70,"✓ approve","",3),(610,140,150,70,"🚀 execute","deploy · send · pay",4)],
 [(250,75,316,75,0),(540,75,606,75,0),(685,110,685,136,0)],
 "drafts flow, signatures gate — the pattern civilization runs on (see also: ArgoCD's sync button)")
PT4_SEQ = seq(["🧍 agent","🏫 host","🧑 human","🌍 world"],
 [(0,0,1,"prepare: diff, tests, rollback plan"),(0,1,2,"proposes deploy(v2)"),
  (1,2,3,"🚧 shows the FULL change: 'allow?'"),(2,1,4,"✓ (or edit, or deny)"),
  (1,3,5,"execute the deploy"),(3,1,6,"healthy ✅"),(1,0,7,"proceed"),(0,2,8,"report + log link 🧾")])
PT5_FLOW = flow(
 [(30,40,180,70,"👷 foreman","owns the outcome",1),(270,40,190,70,"🔎 researcher","gathers facts",2),
  (520,40,180,70,"✍️ writer","drafts from facts",3),(760,40,150,70,"🧐 checker","verifies claims",4),
  (270,140,430,70,"✅ one responsible output","checkable artifacts at every handoff",5)],
 [(210,75,266,75,0),(460,75,516,75,0),(700,75,756,75,0),(835,110,600,145,0)],
 "powerful for parallel work — and it multiplies cost + compounding, so the foreman is not optional")
PT5_SEQ = seq(["👷 foreman","🔎 researcher","✍️ writer","🧐 checker"],
 [(0,1,1,"subtask: facts on X (with sources)"),(1,0,2,"facts.json 📄 — an artifact, not vibes"),
  (0,2,3,"draft from facts.json ONLY"),(2,0,4,"draft.md"),(0,3,5,"verify every claim vs sources"),
  (3,0,6,"2 claims unsupported ❌"),(0,2,7,"fix or cut those two"),(2,0,8,"draft v2"),(0,0,9,"ship — one owner, one output ✅")])

PATTERNS = head("5 agent patterns — Learn Agents School",
  "Five agent patterns — solo, planner-executor, critic loop, human-in-the-loop, team — each with a numbered flow diagram and a sequence diagram.") + MARKER + f'''
<div class="wrap">
<header>
  <p><a href="index.html">← Back to the course home</a></p>
  <h1>👯 The five agent patterns</h1>
  <p class="sub">Every pattern is the same think→act→observe loop, wrapped differently — drawn
  twice: the <b>numbered flow</b> and the <b>sequence diagram</b>. Companion to
  <a href="{GH}/lesson-08-patterns/lessons/08-patterns/README.md">lesson 08</a> — which also covers
  pattern zero: <b>no agent at all</b> 🙅.</p>
  <nav class="toc">
    <a href="#p1">1 Solo doer</a><a href="#p2">2 Planner+executor</a><a href="#p3">3 Critic loop</a>
    <a href="#p4">4 Human-in-the-loop</a><a href="#p5">5 The team</a>
  </nav>
</header>
{pat(1,"p1","🧍 The solo doer — one loop, one belt",
  "Our agent.py: goal in, loop runs, reads flow, the write gates, outcome + log out.",
  PT1_FLOW, PT1_SEQ,
  "almost always — start here and only add structure when the task proves it needs it.")}
{pat(2,"p2","🗺️ Planner + executor — structure beats heroics",
  "Decompose first, then work the checklist; the plan survives any single item failing.",
  PT2_FLOW, PT2_SEQ,
  "long or multi-part tasks where a raw loop drifts (L06 #4) or overflows the desk (L04).")}
{pat(3,"p3","🧑‍🏫 The critic loop — generate, grade, fix",
  "A writer drafts; a merciless grader (best: actual tests) bounces it back until green.",
  PT3_FLOW, PT3_SEQ,
  "quality-critical output with a checkable definition of good — code, citations, structured data.")}
{pat(4,"p4","🚧 Human-in-the-loop — drafts flow, signatures gate",
  "The agent does ALL the preparation; a person owns the one irreversible click.",
  PT4_FLOW, PT4_SEQ,
  "anything touching production, money, or other people — always, not optionally.")}
{pat(5,"p5","👯 The team — parallel work, checkable handoffs",
  "Researcher, writer, checker — each its own loop; a foreman owns the single output.",
  PT5_FLOW, PT5_SEQ,
  "genuinely parallel workstreams; skip it until the solo + critic combo actually falls short.")}
<footer>
  Learn Agents School · <a href="index.html">Course home</a> ·
  <a href="lesson-diagrams.html">Lesson diagrams</a> ·
  <a href="https://github.com/BaluRaut/learn-agents-school">GitHub</a>
</footer>
</div>
</body>
</html>
'''

import os
os.makedirs('docs', exist_ok=True)
open('docs/index.html','w').write(INDEX)
open('docs/lesson-diagrams.html','w').write(DIAGRAMS)
open('docs/patterns.html','w').write(PATTERNS)
print("generated: index dsec =", INDEX.count('class="dsec"'),
      "| diagrams =", DIAGRAMS.count('class="dsec"'),
      "| patterns =", PATTERNS.count('class="dsec"'))
