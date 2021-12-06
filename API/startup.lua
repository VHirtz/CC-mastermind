-- Requirements check

if not http then
    error("The http api is needed to operate")
end

local api = require("/api")

-- Resolving server ip

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
