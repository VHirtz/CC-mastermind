local args = { ... }
if #args ~= 2 then
    error("Usage: ./register.lua 'program' 'server'")
end

-- resolve ip
local response, err = http.get(args[2])

if not response  or table.pack(response.getResponseCode())[1] ~= 200 then
    print("Couldn't retrieve ip")
    return nil
end

local ip = response.readAll()


file = fs.open("ip", "w")
file.write(ip)
file.close()

http.get(server .. "/pushId", {pcid=tostring(os.getComputerID()), program=args[1]})
