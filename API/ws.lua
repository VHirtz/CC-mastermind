local ws = {}
local socket

function ws.ConnectSocket(ip)
    print("Connecting to socket")
    local err
    repeat
        socket, err = http.websocket("ws://" .. ip .. ":80/ws")
        if not socket then
            print("Connection failed")
            print("Retrying in 10 seconds...")
            os.sleep(10)
        end
    until socket
    print("Connected to socket")
end

function ws.CloseSocket()
    print("Closing socket...")
    socket.close()
    print("Socket closed")
end

function ws.Send(msg)
    print("Sending: " .. msg)
    socket.send(msg)
end

function ws.Receive()
    local msg, bool = socket.receive(10)
    if not msg then
        print("Error while waiting for socket")
        print("Rebooting in 10 seconds...")
        os.sleep(10)
        os.reboot()
    end

    print("Received: " .. msg)

    return msg
end

return ws