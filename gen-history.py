#!/usr/bin/env python3
"""Generate docs/history-and-future.html — reuses gen-site.py's helpers."""
exec(open('gen-site.py').read())   # loads head/MARKER/B/S/D/t/sm/num/arr/flow/seq + regenerates main pages

TIMELINE = flow(
 [(30,40,160,80,"⚙️ scripts &amp; RPA","wind-up toys",1),
  (220,40,160,80,"🗣️ chatbots","'22-23: all advice",2),
  (410,40,170,80,"🧰 tool calling","2023: first passes",3),
  (610,40,160,80,"🔁 agent loops","'23-24: hype+crash",4),
  (800,40,110,80,"🔌 today","gated + MCP",5),
  (220,160,540,70,"📉 the AutoGPT lesson: loops without guardrails and evals ran in circles —","the crash taught the field lessons 05 and 06",0)],
 [(190,80,216,80,0),(380,80,406,80,0),(580,80,606,80,0),(770,80,796,80,0),(670,120,520,156,1)],
 "each era kept the previous one's gift and fixed its gap", H=260)

DIAL = ('<svg viewBox="0 0 940 300" role="img">'
 f'<line class="arr" x1="60" y1="80" x2="900" y2="80"/>'
 f'{sm(80,50,"less agency")}{sm(860,50,"more agency")}'
 f'{S} x="40" y="100" width="150" height="80" rx="10"/>{sm(115,128,"0 · answer only")}{sm(115,150,"a chatbot reply")}{num(60,80,0)}'
 f'{S} x="210" y="100" width="150" height="80" rx="10"/>{sm(285,128,"1 · one tool call")}{sm(285,150,"model fills arguments")}{num(285,80,1)}'
 f'{S} x="380" y="100" width="150" height="80" rx="10"/>{sm(455,128,"2 · chooses tools")}{sm(455,150,"which + when")}{num(455,80,2)}'
 f'{B} x="550" y="100" width="150" height="80" rx="10"/>{sm(625,128,"3 · multi-step loop")}{sm(625,150,"think·act·observe")}{num(625,80,3)}'
 f'{B} x="720" y="100" width="190" height="80" rx="10"/>{sm(815,124,"4 · loops that WRITE")}{sm(815,146,"gated by humans 🚧")}{sm(815,168,"5 · long-horizon + budgets")}{num(815,80,4)}'
 f'{sm(470,225,"“agentic” is a DIAL, not a switch — turn it only as far as your guardrails and evals have earned")}'
 f'{sm(470,260,"grammar: agent (the noun) · agency (the property: pursuing goals via chosen actions) · agentic (the adjective)")}'
 '</svg>')

FUTURE = ('<svg viewBox="0 0 940 300" role="img">'
 f'{B} x="40" y="40" width="280" height="110" rx="12"/>{t(180,70,"📈 near (now-ish)")}{sm(180,96,"longer tasks · computer use ·")}{sm(180,118,"real memory · evals as standard ·")}{sm(180,140,"MCP tool ecosystems 🔌")}{num(40,40,1)}'
 f'{B} x="350" y="40" width="280" height="110" rx="12"/>{t(490,70,"🏢 next")}{sm(490,96,"teams of agents with foremen ·")}{sm(490,118,"agent-ops as a job · humans shift")}{sm(490,140,"to reviewing &amp; goal-setting 🚧")}{num(350,40,2)}'
 f'{B} x="660" y="40" width="250" height="110" rx="12"/>{t(785,70,"❓ open questions")}{sm(785,96,"reliability at long horizons ·")}{sm(785,118,"injection &amp; security · audit &amp;")}{sm(785,140,"accountability · workflow change")}{num(660,40,3)}'
 f'{S} x="140" y="185" width="660" height="80" rx="12"/>{t(470,215,"🧭 the safe bet: the LOOP stays; the leash lengthens as guardrails + evals mature")}{sm(470,241,"whatever the headlines say, it will still be think→act→observe with better tools and better brakes")}'
 '</svg>')

HISTORY = head("Before · why · agentic · future — Learn Agents School",
  "The history of AI agents (what came before, why agents were born), what the word agentic actually means, and a grounded outlook on where agents are going.") + MARKER + f'''
<div class="wrap">
<header>
  <p><a href="index.html">← Back to the course home</a></p>
  <h1>⏮️ Before · why · "agentic" · the future</h1>
  <p class="sub">Every tool replaced something worse and points at something next. This page tells the
  agents story in four parts: <b>what came before</b>, <b>why agents were born</b>, <b>what the word
  "agentic" actually means</b>, and <b>an honest look ahead</b>.</p>
  <nav class="toc">
    <a href="#before">⏮️ Before</a><a href="#why">🐣 Why agents were born</a>
    <a href="#agentic">🤔 What "agentic" means</a><a href="#future">🔮 The future</a>
  </nav>
</header>

<section class="dsec" id="before" style="--c:#0d9488">
  <h2><span class="ln">⏮️</span> Before agents — the five eras</h2>
  <p class="d">Each era kept the previous one's gift and fixed its gap.</p>
  {TIMELINE}
  <p class="d" style="margin-top:12px"><b>⚙️ Scripts &amp; RPA (the long before):</b> automation meant
  wind-up toys — exact recorded steps, brittle as glass. RPA bots clicked pixel coordinates and
  shattered when a button moved. Anything requiring judgment stayed human.</p>
  <p class="d"><b>🗣️ Chatbots (2022–23):</b> suddenly machines could REASON in language — brilliant
  advisors with no hands. "Here's how you'd book that trip" … but nothing got booked. All advice,
  zero outcomes (lesson 01's reciter).</p>
  <p class="d"><b>🧰 Tool calling (2023):</b> model APIs learned to emit structured function calls —
  the first hall passes 🎫. One call per turn: useful, but a human still drove the sequence.</p>
  <p class="d"><b>🔁 Agent loops (2023–24):</b> ReAct wired reasoning to tools in a LOOP — and the
  hype arrived: AutoGPT-style "fully autonomous" agents amazed on demos and then ran in circles,
  burned tokens, drifted off-goal. <b>The crash was the curriculum:</b> loops without guardrails
  (L05) and evals (L06) fail — publicly.</p>
  <p class="d"><b>🔌 Today:</b> production agents are narrower and humbler — scoped tools, write
  gates, budgets, logs — and MCP standardizes the tool belt so capabilities are shared parts, not
  private wiring. Boring-on-purpose is winning again (the k8s course's motto returns).</p>
</section>

<section class="dsec" id="why" style="--c:#0d9488">
  <h2><span class="ln">🐣</span> Why agents were born — six forces</h2>
  <p class="d">No single invention — a convergence:</p>
  <div class="vs">
    <div class="vcol"><h3>💰 The advice–outcome gap</h3><ul>
      <li>advice is cheap; OUTCOMES are what work actually is</li>
      <li>the whole economic prize sat one loop away from chatbots</li></ul></div>
    <div class="vcol"><h3>🧠 Models crossed the planning bar</h3><ul>
      <li>good-enough multi-step reasoning + reliable structured output</li>
      <li>before that bar, loops just compounded nonsense faster</li></ul></div>
    <div class="vcol"><h3>🧰 Tool-calling APIs</h3><ul>
      <li>vendors made "model proposes a call" a first-class primitive</li>
      <li>the harness pattern became easy to build (you read one in L07!)</li></ul></div>
    <div class="vcol"><h3>🪑 Bigger desks</h3><ul>
      <li>long contexts made scratchpads + tool results fit (L04)</li>
      <li>without room to observe, the loop starves</li></ul></div>
    <div class="vcol"><h3>🔌 Standard plugs (MCP)</h3><ul>
      <li>tools became an ecosystem, not per-app wiring</li>
      <li>N×M adapters → N+M (the MCP school's whole story)</li></ul></div>
    <div class="vcol"><h3>📉 The hype crash itself</h3><ul>
      <li>2023's failures taught guardrails, evals, human gates</li>
      <li>maturity, not magic, is what shipped in the end</li></ul></div>
  </div>
</section>

<section class="dsec" id="agentic" style="--c:#be123c">
  <h2><span class="ln">🤔</span> What does "agentic" actually mean?</h2>
  <p class="d"><b>Agency</b> = the capacity to pursue a goal by choosing and taking actions.
  <b>Agentic</b> = the adjective: how much of that capacity a system has. It's a DIAL, not a switch:</p>
  {DIAL}
  <p class="d" style="margin-top:12px"><b>"Agentic workflow"</b> = a pipeline where model-driven steps
  choose the path (vs a fixed script). <b>"Agentic AI"</b> in a product pitch = ask lesson 01's
  checklist: what's the goal? which tools? what loop? which guardrails? No answers = a chatbot in a
  trench coat 🕵️. And the dial has a price sticker: every notch right multiplies capability AND
  the need for L05's rules — turn it only as far as your evals prove you've earned.</p>
</section>

<section class="dsec" id="future" style="--c:#be123c">
  <h2><span class="ln">🔮</span> The future — an honest outlook</h2>
  <p class="d">Informed extrapolation, not prophecy — hold it loosely:</p>
  {FUTURE}
  <p class="d" style="margin-top:12px"><b>📈 Near:</b> longer-horizon tasks (hours, not minutes) as
  memory and self-verification improve · <b>computer use</b> (agents driving real UIs) maturing from
  demo to tool · evals and observability becoming as standard as tests are for code · MCP-style
  ecosystems making belts a marketplace.</p>
  <p class="d"><b>🏢 Next:</b> teams of agents with foreman patterns (L08) in real org charts ·
  "agent ops" as a role (budgets, logs, evals, incident review — the k8s course's instincts, for
  loops) · humans shifting up the stack: setting goals, reviewing diffs, owning the signatures 🚧.</p>
  <p class="d"><b>❓ Open questions the field hasn't earned answers to:</b> reliability over very
  long horizons (compounding never sleeps — L06) · security against injection when agents read the
  open web · accountability and audit when loops act at scale · and how work itself reorganizes
  around drafts-flow-signatures-gate. Anyone selling certainty on these is selling. 😄</p>
  <p class="d"><b>🧭 The safe bet:</b> the loop stays. Whatever the headlines, it will still be
  think → act → observe — with better tools, longer leashes, and (if we're wise) better brakes.
  You already know the machine; the future is mostly its knobs.</p>
</section>

<footer>
  Learn Agents School · <a href="index.html">Course home</a> ·
  <a href="patterns.html">The 5 patterns</a> ·
  <a href="lesson-diagrams.html">Lesson diagrams</a> ·
  <a href="https://github.com/BaluRaut/learn-agents-school">GitHub</a>
</footer>
</div>
</body>
</html>
'''

open('docs/history-and-future.html','w').write(HISTORY)
print("history page:", len(HISTORY), "bytes | sections:", HISTORY.count('class="dsec"'))
