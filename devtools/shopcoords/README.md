# Temporary Shop Coordinate Helper

This is a temporary survey utility, not part of the final MLO resource.

## Install on your test server

1. Copy this entire folder to `resources/[dev]/grove_shopcoords` (or another resources folder).
2. Add `ensure grove_shopcoords` to the test server configuration.
3. Restart/reload the resource and connect as a player.
4. Stand at a survey point and run `/shopcoords` in chat.
5. Copy the output from F8/client console and note which point it represents.
6. Repeat for:
   - Clothing shop center
   - Clothing shop entrance
   - Jewelry shop center in the adjacent lot
   - Jewelry shop entrance
7. Remove the `ensure` line and delete/disable this helper after collecting the measurements.

## Important

- Use this only on a server where you are authorized to add resources.
- Coordinates are the player's current position; stand on the ground at the intended location.
- The heading is the player's facing direction. Face toward the intended shop frontage when recording an entrance point.
- Record screenshots as well: coordinates alone do not show footprint, existing props, road clearance, or neighboring map geometry.
- This helper does not spawn, move, replace, or delete map objects.
