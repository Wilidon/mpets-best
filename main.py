import asyncio
import time

from mpets import MpetsApi


async def main():
    for i in range(1, 10):
        mpets = MpetsApi()
        await mpets.start()
        time0 = time.time()
        await mpets.best("charm", i)
        print(time.time() - time0)


if __name__ == '__main__':
    asyncio.run(main())



