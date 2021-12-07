local client = require("CC-mastermind.API.client")

pcall(client.StartClient())

os.reboot()