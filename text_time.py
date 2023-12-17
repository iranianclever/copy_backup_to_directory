import time
from schedule import every, repeat, run_pending

name = 'Amirhossein'
age = 16

@repeat(every(1).minutes, name=name, age=age)
def job(name, age):
	print(f'I am {name} scheduled job {age}')

while True:
	run_pending()
	time.sleep(1)