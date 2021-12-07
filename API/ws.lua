local ws = {}

function ws.CloseSocket()
    print("Closing socket...")
    ws.socket.close()
    print("Socket closed")
end

function ws.Send(msg)
    print("Sending: " .. msg)
    ws.socket.send(msg)
end

function ws.Receive()
    local msg, bool = ws.socket.receive()
    if not msg then
        print("Error while waiting for socket")
        print("Rebooting in 10 seconds...")
        os.sleep(10)
        os.reboot()
    end

    print("Received: " .. msg)

    return msg
end

function ws.ConnectSocket(ip)
    print("Connecting to socket")
    local err
    repeat
        ws.socket, err = http.websocket("ws://" .. ip .. ":80/ws")
        if not ws.socket then
            print("Connection failed")
            print("Retrying in 10 seconds...")
            os.sleep(10)
        end
    until ws.socket
    ws.Send(string(os.getComputerID()))
    print("Connected to socket")
end

return ws