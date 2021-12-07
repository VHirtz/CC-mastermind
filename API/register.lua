local args = { ... }
if #args ~= 1 then
    error("Usage: ./register.lua 'program'")
end

http.get("http://cc.virgilehirtz.me/pushId", {pcid=tostring(os.getComputerID()), program=args[1]})