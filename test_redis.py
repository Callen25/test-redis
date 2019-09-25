import redis


r = redis.Redis(
    host='localhost',
    port=6379,
    password=''
)

r.append('key', 'value')

print(r.get('key'))
