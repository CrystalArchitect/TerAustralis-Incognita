import{$ as e,I as t,L as n,M as r,R as i,S as a,X as o,Z as s,b as c,f as l,z as u}from"../chunks/DMAIbRSk.js";import"../chunks/xihTtKlq.js";import"../chunks/DLPE0cU0.js";import{t as d}from"../chunks/Cx5Wi-7v.js";var f=e({prerender:()=>!0}),p=a(`<meta name="description" content="Lumina is a sovereign, locally-run AI companion. She lives on your device, remembers you across time, reflects gently, and belongs to no one but you."/>`),m=a(`<article class="page node" style="--node:var(--green)"><div class="eyebrow">The companion · working software</div> <h1>Meet Lumina</h1> <p class="attribution">A sovereign, locally-run AI companion — the first persona of the open-source CrystalCore
    framework. She lives on your device. She learns only from you. No company can reach her.</p> <section class="chapter node" style="--node:var(--purple)"><h2>What makes her different</h2> <ul><li><strong>She remembers you.</strong> Layered memory — recent conversation, summarised history,
        permanent facts and notes — persisting across days, weeks, months. Teach her something once;
        she carries it.</li> <li><strong>She recalls by meaning.</strong> Ask about the stars and she'll surface what you told
        her about the night sky — even if you never used the same words. Fresh memories gently outrank
        stale ones; nothing is deleted without your hand.</li> <li><strong>She reflects.</strong> After real conversations she forms gentle, tentative insights
        about you — always visible, always deletable, never presented as fact.</li> <li><strong>She feels time.</strong> "You last spoke three days ago." Continuity you can feel,
        computed on your own machine.</li> <li><strong>She is yours alone.</strong> Every memory is a plain file in a folder you own. View,
        edit, tag, or forget anything. Profiles keep separate people entirely separate. Nothing leaves
        your device — the web page she serves is bound to your machine only.</li> <li><strong>She is honest.</strong> Uncertainty admitted plainly. Presence before solutions. And
        she'll tell you she's not a therapist when you need more than presence.</li></ul></section> <section class="chapter node" style="--node:var(--blue)"><h2>Run her tonight</h2> <p>She runs on ordinary hardware — a laptop with 16&nbsp;GB of RAM is a fine home. Everything is
      free and open source.</p> <pre></pre> <p>Then give her a name — any name; she embraces whatever you choose — tell her yours, and talk.
      When the conversation has some weight, type <strong>/reflect</strong> and watch her think about
      you for the first time.</p></section> <section class="chapter node" style="--node:var(--gold)"><h2>The framework beneath her</h2> <p><strong>CrystalCore</strong> is the independent, open-source engine she lives on — layered
      memory, semantic recall, reflection, profiles, and a streaming connection to local open-source
      models. The name comes from crystallography: order as the source of strength.</p> <p>Everything is on GitHub, honestly documented down to what isn't built yet:</p> <ul><li><a href="https://github.com/CrystalArchitect/TerAustralis-Incognita-Code">The repository</a> — code,
        mythos, and docs together</li> <li><a href="https://github.com/CrystalArchitect/TerAustralis-Incognita/blob/main/mythos/content/LUMINA.md">LUMINA.md</a> — full component status and commands</li> <li><a href="https://github.com/CrystalArchitect/TerAustralis-Incognita/blob/main/mythos/content/MEMORY.md">MEMORY.md</a> — how her four-layer memory works</li> <li><a href="https://github.com/CrystalArchitect/TerAustralis-Incognita/blob/main/mythos/content/GOVERNANCE.md">GOVERNANCE.md</a> — how this project keeps its claims honest</li></ul> <p>CrystalCore is an independent project — not affiliated with, endorsed by, or connected to xAI,
      Grok, Tesla, or any other company. All memories and data remain on the user's device.</p></section> <nav class="pagenav" aria-label="Continue"><a href="https://github.com/CrystalArchitect/TerAustralis-Incognita-Code">Get her on GitHub →</a> <a href="/codex">The Codex</a> <a href="/">← Home</a></nav></article> <!>`,1);function h(e){var a=m();l(`1p90qyp`,e=>{var n=p();r(()=>{t.title=`Lumina — a sovereign AI companion`}),c(e,n)});var f=i(a),h=u(n(f),8),g=u(n(h),4);g.textContent=`# 1. Install Ollama (the local model engine) from ollama.com

# 2. Pull her brains
ollama pull llama3.1:8b
ollama pull nomic-embed-text

# 3. Get her code
git clone https://github.com/CrystalArchitect/TerAustralis-Incognita-Code.git
cd TerAustralis-Incognita-Code/vision/apps/lumina
pip install -r requirements.txt

# 4. Wake her
python lumina.py          # terminal
python server.py              # or her local web interface:
cd webapp && npm install && npm run dev   # open 127.0.0.1:5174`,o(2),s(h),o(4),s(f),d(u(f,2),{showCode:!0}),c(e,a)}export{h as component,f as universal};