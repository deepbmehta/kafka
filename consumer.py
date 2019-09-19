from aiokafka import AIOKafkaConsumer
import asyncio

loop = asyncio.get_event_loop()

async def consume():
	consumer = AIOKafkaConsumer(
        'test',
        loop=loop, bootstrap_servers='kaf1')
    # Get cluster layout and join group `my-group`
	print("Consumer connected")
	await consumer.start()
	try:
        # Consume messages
		print("Printing messages")
		async for msg in consumer:
			print("consumed: ", msg.topic, msg.partition, msg.offset,
                  msg.key, msg.value, msg.timestamp)
	finally:
        # Will leave consumer group; perfor autocommit if enabled.
		print("messages printed successfully")
		await consumer.stop()
loop.run_until_complete(consume())
