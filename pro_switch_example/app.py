from sinric import SinricPro
from sinric import SinricProUdp
from credentials import apiKey, deviceId


def onPowerState(did, state):
    # Alexa, turn ON/OFF Device
    print(did, state)
    return True, state


callbacks = {
    'powerState': onPowerState
}

if __name__ == '__main__':
    client = SinricPro(apiKey, deviceId, callbacks, enable_trace=False, enable_track=False)
    udp_client = SinricProUdp(callbacks)
    udp_client.enableUdpPrint(False)  # Set it to True to start printing request UDP JSON
    client.handle_all(udp_client)
