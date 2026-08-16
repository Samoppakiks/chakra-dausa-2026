> **Got this folder from someone? Unzip it and tell your AI: "Read START-HERE.md in this folder and follow it."** It will load the desk (answer any question on the 2026 Rajasthan reservation lottery, with the clause quoted) and the builder (your district's page + sheets from your documents), and ask which you want first. See `START-HERE.md`.

# आरक्षण लॉटरी हेल्प-डेस्क · Rajasthan reservation-lottery desk (Claude skill)

A Claude skill that answers questions about seat/office reservation and the reservation lottery for Rajasthan's 2026 local-body elections — panchayat (जिला परिषद / पंचायत समिति / ग्राम पंचायत wards, सरपंच, प्रधान, प्रमुख) and urban (nagar nigam / parishad / palika wards) — from the actual text of the Act, Rules, circulars and court rulings, with the state's own 2026 practice shown beside the text, and a calculator for how many SC/ST/OBC/women seats a body gets.

**Who it is for:** Collectors, SDMs, ADMs, election-cell staff, DEO/DLB staff, party agents, journalists — anyone in Rajasthan who has to compute, conduct, record or defend a reservation draw.

## Install (any of these)
- **Claude Code / Claude desktop:** copy this whole folder to `~/.claude/skills/rajasthan-reservation-lottery-desk/` and start a new session. Then just ask — the skill triggers on reservation/lottery questions — or type `/rajasthan-reservation-lottery-desk <your question>`.
- **claude.ai (web/app) with Skills enabled:** upload the folder as a skill (Settings → Skills → add), or attach the zip.
- **No Claude at hand:** open `references/faq.md` — it is readable on its own.

## Ask it things like
- "पंचायत समिति में 15 वार्ड, SC जनसंख्या 10004, ST 29388, कुल 56907 — कितने स्थान किस वर्ग को?"
- "Odd number of seats — women's total rounds up or down? Is there an HC ruling?"
- "SC+ST+OBC 50% से ऊपर जा रहा है — किसे घटाएँ, कैसे?"
- "What exactly does rule 7(13) exclude, and for how long?"
- "Fresh cycle या continuing cycle — 2026 में सरपंच के लिए क्या लागू है?"
- "State's letter gives OBC 4 for a 23-ward समिति — is that right, and what if it isn't?"
- "कार्यवाही विवरण में कौन-कौन सी घोषणाएँ लिखनी हैं?"

## What is inside
| file | what |
|---|---|
| `SKILL.md` | the answer protocol Claude follows (verdict → clause → state practice → what to record / who decides) |
| `references/faq.md` | 29 answered questions + letter lines to the department |
| `references/rules-verbatim.md` | Act ss.15–16, Rules rr.5–10, municipal r.5, Circulars 62/64, Notification 42, DLB letters, RHC rulings — verbatim, with source-quality notes |
| `references/reservation-code.md` | THE RESERVATION CODE — the numbered decision tree, declarations D-1…D-36 |
| `references/edge-cases.md` | 89 edge cases, answered and status-tagged |
| `references/state-questions.md` | Q-1…Q-16 — the only questions the state must answer, in Hindi, with defaults |
| `references/courts.md` | verified quotes: K. Krishna Murthy 2010, Vikas Gawali 2021, Manak Chand 2010, Virender Singh 2020, Jai Singh 2019 |
| `references/state-practice.md` | the state's 2026 arithmetic as observed (Pramukh 20/41, ZP 7/10/1, PS sheets, DLB ⅓) |
| `references/glossary.md` | on-screen term → what the office says |
| `scripts/quota.py` | the calculator (`python3 scripts/quota.py --selftest` reproduces the Dausa numbers) |

## The clickable tool (worked Dausa example, every tier)
https://samoppakiks.github.io/chakra-dausa-2026/ — opens on a phone; derivations behind "गणना विस्तार में देखें".

## Honesty rules baked in
Text over practice over office habit; every silence named (declare or refer); no invented citations; party-facing answers quote a rule where one exists and say nothing where none exists. Version 1.0 · 16 Aug 2026 · built from the Dausa 2026 exercise (private repo Samoppakiks/dausa-avsar). Corrections welcome — send the clause.
