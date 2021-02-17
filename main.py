import asyncio
import time

from mpets import MpetsApi


async def main():
    mpets = MpetsApi()
    await mpets.start()
    time0 = time.time()
    await mpets.best("charm", 1)
    print(time.time() - time0)


if __name__ == '__main__':
    asyncio.run(main())



