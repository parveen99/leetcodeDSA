import asyncio


# coroutine function
async def main():
    print("Hello world from ASYNC")

# main()  #couroutine function was never awaited ( coroutine object)

# print(main()) #<coroutine object main at 0x1031b2810>

# asyncio.run(main()) #handle awaiting this coroutine

#await can only be used inside a async function, inside a coroutine
async def fetch_data(delay):
    print("Starting fetch data funct")
    await asyncio.sleep(delay)
    print("Done awaiting")
    return {"hello": "done"}

async def main_1():
    res = await fetch_data(5)
    
    print(res)


asyncio.run(main_1())