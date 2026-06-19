# STORIES.md
**Project:** game‑guardian  
**Owner:** Axentx – Product Engineering Lead  
**Target Release:** MVP (v0.1) → Full Release (v1.0)  

---  

## Table of Contents
1. [Epics Overview](#epics-overview)  
2. [User Story Backlog](#user-story-backlog)  
   - [Epic 1 – Core Monitoring & Data Capture](#epic‑1)  
   - [Epic 2 – AI‑Powered Predictive Analytics](#epic‑2)  
   - [Epic 3 – Real‑Time Intervention & Recovery](#epic‑3)  
   - [Epic 4 – User Experience & Configuration](#epic‑4)  
   - [Epic 5 – Reporting & Community Integration](#epic‑5)  
3. [Prioritisation & MVP Scope](#prioritisation)  

---  

## Epics Overview
| Epic | Description | MVP Inclusion |
|------|-------------|---------------|
| **Epic 1 – Core Monitoring & Data Capture** | Collect low‑level system metrics (CPU, GPU, RAM, temperature, power, driver events) with minimal overhead. | ✅ |
| **Epic 2 – AI‑Powered Predictive Analytics** | Feed captured data into an on‑device inference engine (vLLM) to predict imminent crashes or hard resets. | ✅ |
| **Epic 3 – Real‑Time Intervention & Recovery** | When a crash is predicted, automatically apply mitigations (e.g., throttle GPU, adjust fan curves, pause background tasks) and optionally trigger a safe‑save snapshot. | ✅ |
| **Epic 4 – User Experience & Configuration** | Provide a lightweight UI/Tray icon, customizable profiles per game, and opt‑in telemetry consent. | ✅ |
| **Epic 5 – Reporting & Community Integration** | Export crash‑prevention logs, share anonymised insights with the Axentx knowledge base, and integrate with Discord/Steam overlay for alerts. | ❌ (post‑MVP) |

---  

## User Story Backlog  

### Epic 1 – Core Monitoring & Data Capture
| # | User Story | Acceptance Criteria |
|---|------------|----------------------|
| 1 | **As a gamer, I want the guardian to run silently in the background, so that I’m not distracted while playing.** | • Guardian starts on system boot or on‑demand via tray icon.<br>• Consumes < 5 % CPU and < 50 MB RAM on idle.<br>• No visible UI unless user opens the dashboard. |
| 2 | **As a system admin, I want the tool to collect high‑frequency hardware metrics, so that the AI model has accurate data.** | • Samples CPU, GPU, RAM, temperature, power draw, and driver error codes at ≥ 100 Hz.<br>• Stores a rolling buffer of the last 30 seconds in memory (circular buffer). |
| 3 | **As a privacy‑concerned user, I want all raw telemetry to stay on my machine unless I opt‑in, so that my data isn’t sent without consent.** | • Default setting = “local only”.<br>• Opt‑in toggle in Settings persists to `config.json`.<br>• When disabled, no network traffic is generated. |
| 4 | **As a developer, I want a well‑documented SDK to access the metric stream, so that we can extend the product later.** | • `src/monitoring/` exposes a C++/C# API with `Start()`, `Stop()`, `Subscribe(callback)`.<br>• API docs generated via Doxygen and included in the repo. |

### Epic 2 – AI‑Powered Predictive Analytics
| # | User Story | Acceptance Criteria |
|---|------------|----------------------|
| 5 | **As a gamer, I want the system to predict a crash at least 5 seconds before it happens, so I can avoid losing progress.** | • Prediction horizon ≥ 5 s with ≥ 90 % precision on the validation set (internal benchmark).<br>• In‑game test shows ≤ 1 false‑positive per hour. |
| 6 | **As a product engineer, I want the AI model to run on‑device using vLLM, so that latency is minimal and no cloud dependency exists.** | • Model loaded via vLLM inference engine.<br>• End‑to‑end latency (capture → prediction) ≤ 30 ms on a typical gaming PC (i7‑10700K + RTX 3060). |
| 7 | **As a data scientist, I want the model to be updatable via a signed package, so that we can improve accuracy without reinstalling the app.** | • `guardian update --model <file>` validates signature and swaps the model file.<br>• No service interruption; inference resumes within 2 s. |

### Epic 3 – Real‑Time Intervention & Recovery
| # | User Story | Acceptance Criteria |
|---|------------|----------------------|
| 8 | **As a gamer, I want the guardian to automatically throttle the GPU when a crash is imminent, so that the system stays stable.** | • On predicted crash, GPU clock is reduced by 15 % within 200 ms.<br>• System remains responsive; FPS drop ≤ 5 % for the duration. |
| 9 | **As a gamer, I want an optional “Save‑State” snapshot to be created before a forced reset, so I can resume where I left off.** | • When enabled, Guardian writes a memory dump of the game process to a user‑specified folder (< 200 MB).<br>• Snapshot completes within 2 s and does not crash the game. |
| 10 | **As a power‑user, I want to define custom mitigation scripts (e.g., kill background apps), so I can tailor the response.** | • Settings UI allows adding shell commands per mitigation type.<br>• Scripts execute with normal user privileges and log success/failure. |

### Epic 4 – User Experience & Configuration
| # | User Story | Acceptance Criteria |
|---|------------|----------------------|
| 11 | **As a gamer, I want a simple tray icon with status colors (green = stable, yellow = risk, red = intervening), so I can glance at health.** | • Tray icon changes color in real‑time based on prediction confidence.<br>• Hover tooltip shows “Stable / Risk: X % / Intervening”. |
| 12 | **As a gamer, I want per‑game profiles (e.g., “Fortnite – aggressive throttling”), so the tool behaves optimally for each title.** | • Profiles stored in `profiles/<game>.json`.<br>• Auto‑detect running game via process name and load matching profile. |
| 13 | **As a user, I want a quick‑start wizard that walks me through permissions (e.g., driver access), so I can get running without reading docs.** | • Wizard runs on first launch, requests required admin rights, validates driver access, and creates default profile. |
| 14 | **As a gamer, I want in‑game overlay notifications (optional), so I’m aware of interventions without alt‑tabbing.** | • Overlay uses DirectX/OpenGL hook; shows non‑intrusive banner “Guardian throttling GPU – risk 78%”.<br>• Can be toggled off in Settings. |

### Epic 5 – Reporting & Community Integration (Post‑MVP)
| # | User Story | Acceptance Criteria |
|---|------------|----------------------|
| 15 | **As a community manager, I want anonymised crash‑prevention logs to be uploaded to the Axentx knowledge base, so we can improve models globally.** | • When user opts‑in, logs (hashed hardware IDs, timestamps, prediction confidence) are sent via HTTPS to `api.axentx.io/guardian/logs`.<br>• Upload occurs in background, < 2 s impact. |
| 16 | **As a gamer, I want to share a “Guardian Score” on Discord/Steam, so friends can see my system stability.** | • Integration button opens OAuth flow for Discord/Steam.<br>• Score generated from last 7 days of stability metrics and posted to selected channel. |

---  

## Prioritisation & MVP Scope  
The MVP (v0.1) will deliver **Epics 1‑4** fully, providing a functional, low‑overhead monitoring + AI prediction + automatic mitigation + basic UI.  

| MVP Feature | Included? |
|-------------|-----------|
| Background monitoring & metric buffer | ✅ |
| On‑device vLLM inference | ✅ |
| 5‑second‑ahead crash prediction | ✅ |
| GPU throttling & optional save‑state | ✅ |
| Tray icon + per‑game profiles | ✅ |
| Quick‑start wizard & privacy opt‑in | ✅ |
| Overlay notifications (optional) | ✅ |
| Model update mechanism | ✅ |
| Reporting / community sharing | ❌ (post‑MVP) |
| Advanced custom scripts UI | ✅ (basic) |
| Full SDK documentation | ✅ |

Stories are ordered to reflect dependencies: data capture → inference → mitigation → UI → optional features.  

---  

*Prepared by the Game‑Guardian Product Engineering Lead, 2026‑06‑19.*
