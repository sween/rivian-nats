import asyncio
from nats.aio.client import Client as NATS
import os

async def run(loop):
    nc = NATS()
    
    async def disconnected_cb():
        print("Got disconnected...")

    async def reconnected_cb():
        print("Got reconnected...")

    await nc.connect("nats.deezwatts.com:42222",
                     reconnected_cb=reconnected_cb,
                     disconnected_cb=disconnected_cb,
                     max_reconnect_attempts=-1)
                     #loop=loop)
    print(nc.is_connected)

    # Use queue named 'deezwatts' for distributing requests
    # among subscribers.
    sub = await nc.subscribe("deezwatts")
    #await nc.subscribe("help", "deezwatts", help_request)

    print("Listening for requests on 'deezwatts' subject...")
    for i in range(1, 1000000):
        await asyncio.sleep(1)
        try:
            # Process a message
            msg = await sub.next_msg()
            print("Received:", msg.data)
            print(type(msg.data))
            # Speak to the Rivian
            os.system('echo %s | festival --tts' % msg.data.decode())
        except Exception as e:
            print("Status: " + str(e))

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(run(loop))
    loop.run_forever()
    loop.close()