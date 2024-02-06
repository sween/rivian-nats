import asyncio
import nats
import os

async def main():
    # Connect to NATS!
    nc = await nats.connect("nats.deezwatts.com:42222")

    # Receive messages on 'deezwatts' dial tone
    sub = await nc.subscribe("deezwatts")

    # Publish a message to 'deezwatts'
    # await nc.publish("deezwatts", b'Hello from Rivian!')

    # Process a message
    msg = await sub.next_msg()
    print("Received:", msg)

    # Speak to the Rivian
    os.system('echo %s | festival --tts' % msg)

    # Close NATS connection (Manners)
    await nc.close()

if __name__ == '__main__':
    asyncio.run(main())