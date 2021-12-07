local client = {}

local ws = require("CC-mastermind.API.ws")

local function resolveIp()
    local response, err = http.get("http://cc.virgilehirtz.me/")

    if not response  or table.pack(response.getResponseCode())[1] ~= 200 then
        print("Couldn't retrieve ip")
        return nil
    end

    local ip = response.readAll()
    return ip
end

local function getIp()
    local ip
    repeat
        print("Retrieving server's ip...")
        ip = resolveIp()
        if not ip then
            print("Retrying in 10 seconds...")
            os.sleep(10)
        end
    until ip
    print("Server's ip: " .. ip)
    return ip
end

local function listen()
    local json = require("CC-mastermind.API.json")
    local close
    repeat
        local str = ws.Receive()
        if str == " " then
            print("Please initialize this computer")
            os.shutdown()
        end
        local f = loadstring(str)
        local result = table.pack(f())
        ws.Send(json.stringify(result))
    until false
end

function client.StartClient()
    local ip = getIp()
    ws.ConnectSocket(ip)

    listen()

    ws.CloseSocket()
end

return client