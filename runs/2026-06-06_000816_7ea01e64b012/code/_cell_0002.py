
import caveclient
print("caveclient version:", caveclient.__version__)

# Try connecting — this will reveal if the network is reachable
try:
    client = caveclient.CAVEclient('minnie65_public')
    print("Connected OK. Server:", client.server_address)
    print("Datastack:", client.datastack_name)
except Exception as e:
    print("Connection error:", type(e).__name__, str(e))
