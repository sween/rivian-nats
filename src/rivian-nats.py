import asyncio
import nats
import os

async def main():
    # Connect to NATS!
    nc = await nats.connect("nats.deezwatts.com:42222")

    # Receive messages on 'foo'
    sub = await nc.subscribe("deezwatts")

    # Publish a message to 'foo'
    # await nc.publish("foo", b'Hello from Python!')

    # Process a message
    msg = await sub.next_msg()
    print("Received:", msg)

    # Speak to the Rivian
    os.system('echo %s | festival --tts' % msg)
    # Close NATS connection
    await nc.close()

if __name__ == '__main__':
    asyncio.run(main())