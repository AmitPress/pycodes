import asyncio
import time

def pour_coffee():
    print('Pouring Coffee...')
    time.sleep(2)
    print('Poured Coffee!')

def pour_juice():
    print('Pouring Juice...')
    time.sleep(1)
    print('Poured Coffee!')

async def fry_egg():
    print('Frying Egg...')
    await asyncio.sleep(4)
    print('Fried Egg!')
async def fry_bacon():
    print('Frying Bacon...')
    await asyncio.sleep(3)
    print('Fried Bacon!')
async def toast_bread():
    print('Toasting Bread...')
    await asyncio.sleep(6)
    print('Toasted Bread!')
def jam_toast():
    print('Jamming Toast...')
    time.sleep(2)
    print('Jammed Toast')

async def make_breakfast():
    start = time.time()
    pour_juice()
    await fry_egg()
    await fry_bacon()
    await toast_bread()
    jam_toast()
    pour_coffee()
    end = time.time()
    print(f'{end-start:.1f}min')
asyncio.run(make_breakfast())