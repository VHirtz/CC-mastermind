local client = {}

local ws = require("CC-mastermind.API.ws")

local function resolveIp()
    file = open("ip", "r")
    local ip = file.readAll()
    file.close()
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
            print("Computer id: " .. os.getComputerID())
            exit()
        end
        local f = loadstring("return " .. str)
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