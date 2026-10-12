# 8-Hour Sprint: Blender + Sollumz Available, No CodeWalker

## Starting point
Confirmed available: Blender and Sollumz.
Not confirmed: CodeWalker, a FiveM staging server, exact target coordinates, or current Sollumz export configuration.

**Target:** produce the strongest defensible MVP in eight hours. A Blender blockout or exported asset is not, by itself, a complete/game-ready MLO.

## Immediate decision
Do not spend the first hour installing optional tooling. Start with the current Blender/Sollumz installation and build the two separate spaces. If CodeWalker can be installed quickly and safely, use it; otherwise continue and mark that validation gate as outstanding.

## Updated schedule

### 0:00–0:20 — Check prerequisites
- Open Blender and confirm the Sollumz add-on loads.
- Confirm the installed Sollumz version and its supported export workflow.
- Confirm whether a FiveM staging server/resource can be tested.
- Capture screenshots of the existing clothing outlet and adjacent parking lot; note coordinates/heading if available.
- Back up current resource/map files.

### 0:20–1:15 — Generate the graybox
- Run `blender/generate_dual_shop_blockout.py`.
- Inspect the separate clothing and jewelry footprints.
- Check entrance openings, fitting bays, stockroom, display cases, service counter, and secure office.
- Save a versioned `.blend` file and screenshots.
- Treat dimensions as provisional until aligned to actual GTA world coordinates.

### 1:15–3:15 — Essential modeling
- Keep the clothing outlet conversion simple: shell, entrance, rails, checkout, fitting rooms, staff/storage area.
- Keep the jewelry shop separate: shell, display cases, service counter, rear secure office.
- Create independent editable signs for both brands.
- Reuse a small material palette; keep geometry and collision simple.
- Avoid custom gameplay, complex animated props, elaborate decor, and unnecessary high-poly detail.

### 3:15–4:45 — Sollumz preparation
- Use the export procedure supported by the installed Sollumz version.
- Check object transforms, naming, materials, textures, collision setup, and output files.
- Do not add guessed manifest entries or claim successful export unless the files actually exist and can be inspected.
- Preserve the editable Blender source and a copy of all generated output.

### 4:45–5:15 — CodeWalker decision gate
- If CodeWalker is already available or can be installed without derailing the sprint, inspect the exported assets.
- Otherwise record CodeWalker validation as **not performed** and proceed to staging only if the export output is usable.

### 5:15–6:45 — FiveM staging test (if available)
- Test in a separate staging resource/server, not the live server.
- Check resource load, streaming, entrances, collision, wall/floor seams, original-map overlap, textures, and lighting.
- Check client/server console output and capture screenshots.
- If no staging server is available, do not label the package playable or game-ready.

### 6:45–7:30 — Fix critical issues
1. Export/resource failures.
2. Broken collision, missing textures, or invisible geometry.
3. Incorrect location/heading/elevation or overlap with the original map.
4. Blocked entrances or trapped players.
5. Cosmetic polish only after critical checks pass.

### 7:30–8:00 — Package
- Include source, actual generated assets, install instructions, screenshots, backup/rollback notes, and known limitations.
- Report which checks were run and which were not.
- Label honestly as a prototype, staging candidate, or tested release based on evidence.

## Validation status labels
- **Model prototype:** editable Blender scene; no claim of FiveM functionality.
- **Export candidate:** Sollumz output exists and passes available structural checks; not yet confirmed in-game.
- **Staging-tested:** loads in a FiveM test server and passes the checks actually recorded.
- **Production-ready:** all required asset, map-placement, collision, streaming, overlap, and performance checks have passed. Do not use this label without evidence.

## Highest-risk blockers
- No exact map coordinates/heading/elevation for the two target footprints.
- No CodeWalker inspection.
- Unknown availability of a FiveM staging server.
- Sollumz version/export compatibility not yet confirmed.

If any blocker prevents a real MLO, deliver the Blender prototype plus a precise blocker list instead of guessing coordinates or shipping unverified files.
