# Grove Street Dual-Shop MLO

A custom FiveM environment project for two separate businesses near Grove Street:

1. **Clothing boutique** — conversion concept for the existing Grove Street clothing-store outlet.
2. **Jewelry boutique** — a separate shop concept for the adjacent parking lot.

The design target is urban and street-inspired but polished, with independently rebrandable signs, readable circulation, restrained geometry, and an optimization-first asset pipeline.

> **Build status:** this repository starts with editable project source and a Blender blockout generator. It is **not yet a compiled, game-ready MLO**. Production deployment requires Blender + Sollumz asset authoring, CodeWalker validation, real-world coordinate placement, and in-game FiveM tests.

## Accelerated MVP plan
See [`docs/8_HOUR_MVP_SPRINT.md`](docs/8_HOUR_MVP_SPRINT.md) for a strict eight-hour prototype sprint, acceptance gates, and scope limits. This is a best-effort plan, not a guarantee of game-ready completion.

## Partner concept presentation
See [`docs/CONCEPT_GALLERY.md`](docs/CONCEPT_GALLERY.md) for the partner-facing gallery page and image checklist. Concept images will be labelled clearly and kept separate from verified in-game screenshots.

## Project files
- `config.lua` — independently editable names, accents, and provisional blockout dimensions.
- `fxmanifest.lua` — FiveM resource manifest scaffold.
- `blender/generate_dual_shop_blockout.py` — generates a reviewable graybox for both shops.
- `BUILD_CHECKLIST.md` — production and validation gates.
- `tools/validate_project.py` — structure and source sanity checks.
- `.github/workflows/validate.yml` — automated validation on push/PR.

## Generate the blockout
1. Install Blender.
2. Open the **Scripting** workspace.
3. Load `blender/generate_dual_shop_blockout.py` and click **Run Script**.
4. The script saves `grove_street_dual_shop_blockout.blend` beside itself by default.

Or run from a terminal:
```powershell
blender --background --python blender/generate_dual_shop_blockout.py
```

The blockout is a layout aid, not a Sollumz exporter. Its dimensions and spacing are provisional; survey the real target area before final placement.

## Planned spaces

### Clothing boutique
- Sales floor, checkout, clothing rails / displays
- Two fitting-room bays
- Stockroom / staff zone
- Independently editable sign and accent

### Jewelry boutique
- Separate footprint in adjacent parking lot
- Showroom with display cases
- Service counter
- Secure rear office
- Independently editable sign and accent

## Production pipeline
1. Survey the existing clothing outlet and adjacent lot; record exact coordinates, heading, elevation, and footprint.
2. Refine geometry, UVs, materials, signage textures, collision, and circulation in Blender.
3. Use a compatible Sollumz workflow to prepare game assets and interior structures.
4. Validate generated assets with CodeWalker and configure the actual manifest/data files.
5. Test in FiveM for streaming, collisions, portals, lighting, overlap, and performance.
6. Keep a rollback copy before replacing or hiding any original map assets.

Optimization targets: reusable modular meshes, sensible texture atlases, simple collision, restrained transparency, appropriate LODs/draw distances, and no duplicate overlapping surfaces. Runtime profiling is required; source checks cannot prove performance.

## Run checks
```bash
python tools/validate_project.py
```

Passing GitHub Actions means the source scaffold passed basic checks. It does **not** certify that an MLO loads or performs correctly in FiveM.
