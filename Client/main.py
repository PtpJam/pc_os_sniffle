from Client.Controller.DataSocket_Controller import DataPC_Singleton
from Client.Controller.jsonEncoder_Controller import jsonEncoder
from Client.Model.socketConnect import socketConnect

def main():
    jsonData = jsonEncoder().toJson(DataPC_Singleton().getDataPC())
    socketConnect().sendDataPC(jsonData)

if __name__ == "__main__":
    main()


