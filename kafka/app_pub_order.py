import asyncio
import random

from faststream import FastStream, Logger
from faststream.kafka import KafkaBroker
from pydantic import BaseModel, Field

version = "0.1.0"
title = "My FastStream coin service"
description = "Description of my FastStream coin service"


# class Name(BaseModel):
#     name: str = Field(..., description="Name of the person")


class Greeting(BaseModel):
    greeting: str = Field(..., description="Greeting message")


class Product(BaseModel):

    product_name : str  = Field(..., description="Product message")

class Customer(BaseModel):
    customer_name : str = Field(..., description="Name of the person")

## TODO develop collection for each person on star-coin
def get_coins_for_free(customer_names):
    lov_coins = ['1 cent','1 denga','1 dieneżka','1 dime','1 fenig','1 grosz','1 kopiejka','1 marka','1 penni','1 rubel','1 szyling','1 złoty','½ dolara','½ kopiejki','⅓ talara','⅙ talara','10 fenigow','10 groszy','10 kopiejek','10 marek','10 penniä','10 soldi','10 złotych','100 milów','1000 złotych','15 kopiejek','2 kopiejki','2 lity','2 marek','2 para','2 szylingi (floren)','2 złote','20 fenigow','20 kopiejek','25 kopiejek','25 penniä','3 fenigi','3 grosze','3 pensy','5 fenigow','5 groszy','5 kopiejek','5 penniä','5 złotych','50 centymów','50 groszy','50 kopiejek','50 penniä','6 pensów']
    if customer_names == "Ana":
        coin_name = lov_coins[1]
    else:
        coin_name = random.choice(lov_coins)
    
    return coin_name

# zookeeper port 2181
broker = KafkaBroker("localhost:29092")
app = FastStream(broker, title=title, version=version, description=description)

customer_calls = broker.publisher(
    "greetings",
    description="Produces a message on greetings after receiving a meesage on customer_names",
)


@broker.subscriber("customer_names", description="Consumes messages from customer_names topic and produces messages to greetings topic")
async def on_names(msg: Customer, logger: Logger) -> None:
    coin_name = get_coins_for_free( msg.customer_name)
    order_result = f"Order for {msg.customer_name} is getting {coin_name}"
    logger.info(order_result)
    greeting = Product(product_name=order_result)
    await customer_calls.publish(greeting)


@app.after_startup
async def publish_names() -> None:
    async def _publish_names() -> None:
        customer_names = [
            "Ana",
            "Mario",
            "Pedro",
            "João",
            "Gustavo",
            "Joana",
            "Mariana",
            "Juliana",
        ]
        while True:
            # Try to replace it with order-trade coins algorithm
            chosen_name = random.choice(customer_names)  # nosec
            
            await broker.publish(Customer(customer_name = chosen_name ), topic="customer_names")
            
            await asyncio.sleep(3)

    asyncio.create_task(_publish_names())
