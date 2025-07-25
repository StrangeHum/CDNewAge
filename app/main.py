# docker run --rm -p 15672:15672  rabbitmq:3.10.7-management
# docker run -d --name rabbitmq --hostname rabbitmq -p 15672:15672 -p 5672:5672 rabbitmq:3.10.7-management
# from fastapi import FastAPI
# import uvicorn

# app = FastAPI()


# @app.get("/users")
# async def make_order():
#     return [{"id": 1, "name": "src"}]


# @app.get("/foo")
# async def make_foo():
#     return [{"id": 1, "name": "foo"}]


from fastapi import FastAPI
from faststream.rabbit.fastapi import RabbitRouter

app = FastAPI()
router = RabbitRouter("amqp://guest:guest@localhost:5672/")


@router.get("/")
async def foo():
    return {"data": "OK"}


@router.post("/order")
async def make_order(name: str):
    await router.broker.publish(
        f"Новый заказ: {name}",
        queue="orders",
    )
    return {"data": "OK"}


app.include_router(router)
