local api = {}
local ws = require("CC-mastermind.API.ws")

local calls = {}

function calls.INIT()
    ws.Send(os.getComputerID())
end

function api.Call()
    ws.Send("NEXT")
    local msg = ws.Receive()
    if msg == "CLOSE" then
        return true
    end
    local success, result, any = pcall(calls[msg])
    if not success then
        print("Error while executing api call: " .. msg)
        print("The function might not be implemented")
        os.reboot()
    end
    ws.Send("COMPLETE")
    return false
end

return api