RegisterCommand('shopcoords', function()
    local ped = PlayerPedId()
    if not DoesEntityExist(ped) then
        print('[grove_shopcoords] Player ped is not available yet.')
        return
    end

    local coords = GetEntityCoords(ped)
    local heading = GetEntityHeading(ped)
    local line = ('[grove_shopcoords] x=%.3f, y=%.3f, z=%.3f, heading=%.2f'):format(
        coords.x, coords.y, coords.z, heading
    )

    print(line)
    TriggerEvent('chat:addMessage', {
        color = { 70, 200, 170 },
        multiline = false,
        args = { 'Shop Survey', line }
    })
end, false)

print('[grove_shopcoords] Loaded. Stand at a survey point and run /shopcoords.')
