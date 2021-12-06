local client = {}

local function resolveIp()
    local response, err = http.get("http://cc.virgilehirtz.me")

    if not response  or table.pack(response.getResponseCode())[1] ~= 200 then
        print("Couldn't retrieve ip")
        return nil
    end

    local content = response.readAll()
    local pattern_start, pattern_end = string.find(content, "src=\"http://")
    local ip_large = string.sub(content, pattern_end + 1, pattern_end + 15)
    pattern_start, pattern_end = string.find(ip_large, "\"")

    local ip = string.sub(ip_large, 1, pattern_start - 1)

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
    local api = require("CC-mastermind.API.api")
    local close
    repeat
        print("New api call cycle")
        close = api.Call()
    until close
end

function client.StartClient()
    local ws = require("CC-mastermind.API.ws")

    local ip = getIp()
    ws.ConnectSocket(ip)

    listen()

    ws.CloseSocket()
end

return client