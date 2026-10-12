# Immediate Next Steps — Start of 8-Hour Sprint

Confirmed by the project owner:
- Blender and Sollumz are installed; Sollumz loads correctly.
- FiveM resource testing is available.
- No location screenshots or coordinates are ready yet.
- CodeWalker is not installed.

## Step 1 — Do not model final placement yet (first 20–30 minutes)

1. Start the FiveM server and connect as a player.
2. Travel to the existing Grove Street clothing shop that should be converted.
3. Take screenshots from outside facing the shop, from the sidewalk/road showing its context, and inside if the existing interior is accessible.
4. Walk to the adjacent parking lot intended for the separate jewelry shop. Take screenshots facing the lot from the street and from the lot toward the clothing store.
5. Capture coordinates and heading at each intended shop center using the temporary helper in `devtools/shopcoords/` (see its README). Also capture a point at each intended entrance.
6. Keep original map geometry enabled. Do not delete or replace map assets yet.

If the shop is not in the expected place, stop and send the screenshots before placing anything.

## Step 2 — Run the coordinate helper

The helper is a separate temporary FiveM resource and does not need to be added to the MLO resource's production manifest.

- Copy `devtools/shopcoords/` to your server's resources directory as a folder named `grove_shopcoords`.
- Add `ensure grove_shopcoords` to your test server config, restart the test server, and connect.
- Stand at the target location and run `/shopcoords` in chat.
- The command prints the player's coordinates and heading to F8/client console and chat.
- Repeat at the clothing shop center, clothing entrance, jewelry shop center, and jewelry entrance.
- Remove `ensure grove_shopcoords` and the helper resource after collecting the data.

Use this only on a server where you can add a temporary resource. Do not put the helper into the final production resource.

## Step 3 — Upload references here

Send the exterior/context screenshots and the four coordinate/heading readings. If you can only get a screenshot first, send that; do not invent coordinates. From those references, choose whether the first build should be a placed prototype or a location-independent interior blockout.

## Step 4 — Build only after the location gate passes

- Run `blender/generate_dual_shop_blockout.py` and inspect the blockout.
- Adjust dimensions and transform to match surveyed footprints.
- Check entrances and circulation, then create the two signs independently.
- Use the installed Sollumz version's supported export workflow.
- Validate the actual exported files before adding any required entries to `fxmanifest.lua`.
- Test only in a separate FiveM staging resource with a rollback copy.

## Time budget from now

- 0:00–0:30: survey/screenshots/coordinates
- 0:30–1:15: blockout alignment
- 1:15–3:15: minimum interiors and signs
- 3:15–4:45: Sollumz export and structural checks
- 4:45–6:45: FiveM staging tests and critical fixes
- 6:45–8:00: final fixes, packaging, and test report

The schedule is a target, not a guarantee. If correct placement or export cannot be verified, deliver a clearly labelled prototype instead of claiming a game-ready MLO.
