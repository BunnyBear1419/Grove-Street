# Build and Release Checklist

## A. Site survey and blockout
- [ ] Capture reference screenshots of the existing Grove Street clothing outlet and adjacent parking lot.
- [ ] Confirm whether the existing interior is replaced, covered, or selectively modified.
- [ ] Record exact world origin, heading, footprint, elevation, road/sidewalk clearance, and neighboring collision.
- [ ] Generate and inspect both Blender blockout footprints.
- [ ] Review circulation, accessible routes, entrance clearance, and egress.
- [ ] Keep both sign objects independently editable.

## B. Clothing boutique
- [ ] Sales floor, checkout, and display rails.
- [ ] Two fitting-room bays with usable openings and collision.
- [ ] Stockroom/staff zone.
- [ ] No fixtures block entrances or walkways.
- [ ] UVs/materials reviewed and texture reuse planned.

## C. Jewelry boutique
- [ ] Separate shop footprint in the adjacent parking lot.
- [ ] Showroom with glass display cases.
- [ ] Service/checkout counter.
- [ ] Secure rear office with staff-only access.
- [ ] Glass and lighting tested in-game.
- [ ] Independent sign and brand accent.

## D. Sollumz / CodeWalker
- [ ] Confirm Blender and Sollumz versions.
- [ ] Assign supported materials and texture dictionaries.
- [ ] Build and verify collision assets.
- [ ] Configure interior room/portal/occlusion data as required by the chosen design.
- [ ] Export and validate assets in CodeWalker.
- [ ] Add only real generated files and matching manifest/data_file entries.
- [ ] Check dependencies and asset naming/casing.

## E. FiveM staging tests
- [ ] Back up the server/map resource before testing.
- [ ] Verify both shops stream without missing assets or console errors.
- [ ] Check collision at every doorway, fitting room, counter, and display.
- [ ] Confirm players cannot walk through walls or become trapped.
- [ ] Check for overlap/flicker with original store and parking-lot assets.
- [ ] Test day/night lighting and glass reflections.
- [ ] Test with multiple clients.
- [ ] Measure client performance and texture memory on representative hardware.
- [ ] Capture approval screenshots/video.

## Release gate
Do not call this production-ready until generated assets pass in-game validation. GitHub CI only checks source structure/basic sanity; it cannot validate FiveM streaming or performance.
