import asyncio
import websockets

async def serve(websocket, path):
    # Envoie de l'adresse de l'utilisateur
    await websocket.send("8 Rue de Londres, Paris")

# Lancement du serveur WebSocket
asyncio.get_event_loop().run_until_complete(
    websockets.serve(serve, 'localhost', 8765)
)
asyncio.get_event_loop().run_forever()