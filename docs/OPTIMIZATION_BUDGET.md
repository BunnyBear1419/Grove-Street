# Asset Optimization Targets

These are review targets, not guarantees. Measure the finished resource in-game.

## Geometry
- Reuse modular trim, shelving, counters, and repeated fixtures where practical.
- Avoid hidden internal faces and overlapping coplanar surfaces.
- Keep collision meshes simple and separate from detailed render geometry.
- Do not use high-poly bevels on small fixtures that are barely visible.
- Review doorway widths and player collision before adding detail.

## Textures and materials
- Prefer shared materials and atlases over many one-off textures.
- Keep signage textures separate per business so each brand can be replaced independently.
- Use transparency only where visually needed; glass needs in-game testing.
- Check texture dimensions, mipmaps, UV coverage, and compression in the final pipeline.
- Avoid excessive emissive surfaces and unnecessary normal-map detail.

## Interior/map integration
- Confirm room/portal/occlusion behavior for the chosen interior implementation.
- Verify collision and visibility transitions from sidewalk to shop interior.
- Avoid duplicate walls or floors over existing geometry that cause flicker.
- Use appropriate LODs and draw distances where the asset workflow supports them.
- Validate day/night lighting and nearby building overlap.

## Required evidence before release
- Screenshots of both shops from outside and inside.
- FiveM client console/server log check.
- Collision walkthrough for every public/staff area.
- Performance observation on representative hardware.
- Confirmation that original map can be restored quickly.
