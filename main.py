import asyncio

from aiogram import Bot, Dispatcher, Router

from Commandlar import router as command_router
from ish_joyistate import router as ish_router
from ustoz_kerak import router as ustoz_router

router = Router()
router.include_router(command_router)
router.include_router(ish_router)
router.include_router(ustoz_router)



async  def main()->None:
    bot = Bot(token="7486082803:AAF92xBsZn3dcfcTH9M3yYMBCqEu8XfFo4U")

    dp = Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    asyncio.run(main())