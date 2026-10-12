# 8-Hour MVP Sprint Plan

This is a **best-effort prototype sprint**, not a promise of production readiness. The eight-hour target assumes Blender and a compatible Sollumz setup are already installed, the target map can be inspected immediately, and someone can launch a FiveM staging server for testing. If any of those dependencies are missing, the honest deliverable may be a polished Blender blockout plus a clearly documented integration backlog.

## Scope freeze: only what is needed to prove the idea

- Clothing shop: simple shell, open entrance, checkout, rails, two fitting bays, compact stock/staff area, independent sign.
- Jewelry shop: separate shell in the adjacent lot, display cases, service counter, secure rear office, independent sign.
- Minimal shared materials, simple geometry and collision plan.
- No custom gameplay scripts, complex animated props, elaborate exterior landscaping, custom high-poly assets, or optional decorative rooms in this sprint.
- Do not replace or hide original map assets until the exact target coordinates and a rollback plan are confirmed.

## Hour-by-hour execution

### 0:00–0:30 — Dependency and location gate
- Confirm Blender, Sollumz, CodeWalker and FiveM test access.
- Capture the current clothing outlet and adjacent parking lot in-game.
- Record exact location/heading/elevation or decide to keep the work as an unplaced prototype.
- Back up the current resource and relevant map files.

**Gate:** if tools or exact location are unavailable, switch immediately to a reviewable prototype; do not guess production coordinates.

### 0:30–1:30 — Generate and review the blockout
- Run `blender/generate_dual_shop_blockout.py`.
- Inspect dimensions, entrance openings, circulation, shop separation and fitting/office layout.
- Adjust only critical scale/placement issues.
- Save a versioned Blender file and take review screenshots.

### 1:30–3:30 — Build the minimum visual pass
- Use modular, low-complexity meshes and a small shared material set.
- Finish the clothing rails, fitting bays, checkout and stock zone.
- Finish jewelry display cases, service counter and staff-only rear office.
- Create independently editable shop signs.
- Keep glass and lighting simple to reduce rendering and material problems.

### 3:30–5:00 — Export and structural validation
- Use the installed, compatible Sollumz workflow to prepare only the required assets.
- Verify scale, transforms, texture paths, collision and naming.
- Open the output in CodeWalker and correct blocking export issues.
- Do not add guessed manifest data entries; add only entries required by actual exported files.

### 5:00–6:30 — FiveM staging test
- Install into a separate test resource/server, never directly over the live map.
- Verify both shop locations, entrances/exits, collision, wall/floor seams and interaction clearance.
- Check for overlap with original map geometry and missing textures.
- Review client/server console output and capture screenshots.

### 6:30–7:30 — Fix only release blockers
Prioritize in this order:
1. Crash, resource-load or streaming failures.
2. Missing/corrupt assets or broken collision.
3. Incorrect placement, blocked entrances or overlap with original map.
4. Major lighting/material readability problems.
5. Cosmetic polish only if all earlier gates pass.

### 7:30–8:00 — Package and report truthfully
- Save a rollback copy and version the tested build.
- Include install instructions and known limitations.
- Capture evidence of what was actually tested.
- Label the package **prototype**, **staging candidate**, or **tested release** according to the evidence—not the deadline.

## Minimum acceptance checklist

- [ ] Two physically separate shop spaces are present.
- [ ] Both signs can be changed independently.
- [ ] Clothing layout includes rails, checkout, two fitting bays and stock/staff zone.
- [ ] Jewelry layout includes display cases, service counter and secure rear office.
- [ ] Entrances, floors and walls have usable collision.
- [ ] No major overlap with the original map.
- [ ] Resource loads without blocking errors in a FiveM staging test.
- [ ] Backup, install notes and screenshots are included.

## What eight hours cannot guarantee

A deadline cannot replace installed-tool access, correct world coordinates, export compatibility or in-game validation. Do not call this production-ready solely because a Blender file exists or GitHub checks pass. If the export/in-game gates fail, deliver the reviewable prototype and exact blocker list rather than a broken live resource.
