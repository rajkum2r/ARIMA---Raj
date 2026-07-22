# ARIA MAX — Executive AI Command Center v6 (FINAL) 👑

The finished product. Versions v1–v5 remain in sibling folders for comparison.
Rule unchanged: **zero cloud — everything lives on your devices.**

## Run

```bash
cd aria-max
python serve.py            # → http://localhost:8323
```

## The three platform packages (in this folder)

| File | Platform | How to install |
|---|---|---|
| **ARIA-MAX-laptop.zip** | Windows / macOS / Linux laptop | Unzip → `python serve.py` (or open index.html). For a real **.exe**: `cd electron && npm i -D electron electron-builder && npx electron .` (run now) / `npx electron-builder --win portable` (build ARIA MAX.exe) |
| **ARIA-MAX-android-kit.zip** | Android | Unzip → `npm install && npm run android` (Android Studio → Build APK). Or instant: serve on the laptop, scan the QR (Settings → Install), Chrome ⋮ → Install app |
| **ARIA-MAX-ios-kit.zip** | iPhone / iPad | Unzip on a Mac → `npm install && npm run ios` (Xcode). Or instant: Safari → Share → Add to Home Screen |

A browser cannot compile .exe/.apk by itself — these kits with one `npm` command are the direct honest path; the PWA/QR route needs zero tools.

## Everything new in v6 (your final correction list)

1. **+30 cinematic scenes** (36 total): each of the 6 worlds in Dawn/Dusk/Night/Emerald/Rose colour-grades — scene picker in Settings.
2. **Tamil speech strengthened**: 10 🪷 Tamil personas that speak with ta-IN voices (பல்லவி, அமுதா, தென்றல்…), **English + தமிழ் together** reply mode, Tamil confirmations & commands. (Install the free “Pallavi” Tamil voice: Windows Settings → Speech → Add voices.)
3. **Profile enlarged** (52 px, rounded) + click it to view the full photo/GIF/video.
4. **Knowledge v3**: hub/center panels now show the **actual records inside** (titles + status/due/progress), custom-node forms, **plus 10 camera angles** (Front/Top/Side/Iso/Low/Bird/Close/Wide/Dutch/🎢 Sweep) on top of the 20 layouts.
5. **Insights v3**: **👑 Master view** — Today/Week/Month/Quarter/Half-year/Year chips showing finished, created, upcoming and overdue with throughput % — plus a **90-day every-task timeline**.
6. **Dashboard command center**: live tiles for Health, Family (next birthday), Files, Goals, Money, Journal, Studio, Knowledge, Recorder.
7. **Avatars**: proportion fixes on the 24 humans + **20 creature characters** (cat, dog, panda, fox, bear, rabbit, tiger, lion, koala, monkey, owl, eagle, parrot, penguin, duck, frog, butterfly, bee, dragonfly, dolphin) with flapping wings, blinking eyes, talking beaks/jaws → **45 avatars** total.
8. **Task voice-fill**: one 🎙 button fills title + date + time + priority + project from a single sentence.
9. **⭐ Keeps**: categorized important vault (Email/Legal/Finance/Work/Research/Personal/Confidential) — star files, keep notes.
10. **Calendar v3**: **day sheet** like your Tamil calendar (big date, weekday, holiday, 🌑 அமாவாசை / 🌕 பௌர்ணமி moon phases, family birthdays, tasks due) + moon marks on the grid.
11. **Meetings**: List / **Timeline** / **Stats** views (per-month chart, action completion).
12. **R&D v2**: experiments log with results, **material purchases with ₹ totals**, spend/experiment stats bar.
13. **Ideas Vault key** 🔐: its own unlock key, separate from the app lock.
14. **Family v2**: call-every-N-days reminders with overdue badges, **WhatsApp one-tap**, "✓ called now", anniversaries, morning call-list nudge.
15. **Health v2**: 💧 water counter, **BP measurement reminders** at your chosen morning/evening times (spoken).
16. **Studio Sound Lab**: 3-band EQ with presets (Bass boost, Voice boost, Concert, Soft), playback speed, **ambience mixer** (rain/ocean/wind/fire under your music).
17. **🔴 Recorder + Translator**: record meetings offline with live transcript, transcribe/translate on demand, **live speak→translate→speak** between 8 languages (translation needs any free AI key).
18. **New sections you didn't name**: 🎯 Goals (OKRs with key-result checklists), 💰 Money (voice: "spent 500 on food"), 📔 Journal (mood + streak + 30-day chart).
19. **Export/Share extended** to Goals, Money, Journal, Keeps — Word/Excel/PDF/PNG/Share everywhere.

## First-run checklist
Settings → connect 💽 disk vault → run 🔎 voice diagnostic → pick avatar 🎭 + persona → set lock method 🛡 → scan 📲 QR on your phone → set LAN sync for laptop↔phone.
