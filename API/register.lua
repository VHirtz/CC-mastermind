local args = { ... }
if #args < 1 then
    error("Usage: ./register.lua 'program' [server] [port]")
end
port = 80
server = "cc.virgilehirtze.me"
if #args >= 2 then
    server = argv[2]
if #args == 3 then
    port = argv[3]
end
-- resolve ip
local response, err = http.get("http://" .. server .. ":" .. port)

if not response  or table.pack(response.getResponseCode())[1] ~= 200 then
    print("Couldn't retrieve ip")
    return nil
end

local ip = response.readAll()


file = fs.open("ip", "w")
file.write(ip .. ":" .. port)
file.close()

http.get("http://" .. server .. ":" .. port .."/pushId", {pcid=tostring(os.getComputerID()), program=args[1]})
