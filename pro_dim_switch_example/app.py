from sinric import SinricPro
from sinric import SinricProUdp
from credentials import appKey, deviceId, secretKey
from time import sleep

def Events():
    while True:
        # Select as per your requirements
        # REMOVE THE COMMENTS TO USE
        # client.event_handler.raiseEvent(deviceId1, 'setPowerState',data={'state': 'On'})
        sleep(2) #Sleep for 2 seconds 

def onPowerState(did, state):
    # Alexa, turn ON/OFF Device
    print(did, state)
    return True, state


eventsCallbacks={
    "Events": Events
}

callbacks = {
'powerState': onPowerState
}

if __name__ == '__main__':
    client = SinricPro(appKey, deviceId, callbacks,event_callbacks=eventsCallbacks, enable_trace=False,secretKey=secretKey)
    udp_client = SinricProUdp(callbacks,deviceId)
    udp_client.enableUdpPrint(False)  # Set it to True to start logging request Offline Request/Response
    client.handle_all(udp_client)