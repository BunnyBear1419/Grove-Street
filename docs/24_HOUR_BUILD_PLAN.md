# 24-Hour Build Plan

The deadline is aggressive. Prioritize a coherent, testable shell over decorative detail.

## First 2 hours — survey and blockout
- Gather screenshots and exact site coordinates/heading for both locations.
- Generate the Blender blockout and confirm that both footprints fit.
- Resolve whether the clothing outlet is replaced or overlaid and which base map assets are affected.

## Hours 2–8 — layout and primary assets
- Finalize wall/floor shells, entrances, partitions, counters, display cases, fitting rooms, and stock area.
- Create separate sign textures/objects and confirm both can be rebranded independently.
- Keep collision and materials simple.

## Hours 8–14 — Sollumz integration
- Prepare interior/map structures and collision in the installed Blender/Sollumz workflow.
- Export assets and inspect them in CodeWalker.
- Correct scale, orientation, material/texture, and collision problems.

## Hours 14–20 — FiveM staging
- Add only verified generated assets and matching manifest entries.
- Test streaming, entry/exit, collision, portals, lighting, and overlap.
- Fix blocking issues before adding cosmetic details.

## Hours 20–24 — release decision
- Test both shops in a clean staging environment.
- Capture evidence and keep a rollback copy.
- Ship only if critical tests pass; otherwise label the package a preview build and document remaining blockers.

**Hard dependency:** GitHub can store source and automate checks, but it cannot replace Blender/Sollumz/CodeWalker or in-game testing. If those tools or exact site coordinates are unavailable, a truly game-ready MLO cannot honestly be guaranteed inside 24 hours.
