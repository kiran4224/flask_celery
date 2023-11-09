import redis

def test():
    # Connecting to Redis
    r = redis.Redis(host='apm_redis', port=6379, db=0)

    ######## String Operations #####################
    # SET key to hold the string value
    r.set('mykey', 'Hello')

    # GET the value of key
    value = r.get('mykey')
    # print("GET Operation: ", value.decode('utf-8'))

    # Append a value to a key
    r.append('mykey', ' World')

    # SET key to hold string value if key does not exist
    r.setnx('mykey', 'New Value')

    # Overwrite part of a string at key starting at the specified offset
    r.setrange('mykey', 6, 'Redis')

    # Get the length of the value stored at key
    length = r.strlen('mykey')
    # print("STRLEN Operation: ", length)

    # Increment the integer value of a key by the given amount
    r.set('mycounter', 5)
    r.incrby('mycounter', 3)

    # Decrement the integer value of a key by the given number
    r.decrby('mycounter', 2)

    # Set the value and expiration of a key
    r.setex('myexpkey', 30, 'Temporary Value')

    ################# Hash Operations ##################
    r.hset('myhash', 'field1', 'value1')
    r.hset('myhash', 'field2', 'value2')
    hash_value = r.hgetall('myhash')
    # print("Hash Operation - HGETALL: ", hash_value)

    # List Operations
    r.rpush('mylist', 'a')
    r.rpush('mylist', 'b')
    r.rpush('mylist', 'c')
    list_value = r.lrange('mylist', 0, -1)
    # print("List Operation - LRANGE: ", list_value)

    # Set Operations
    r.sadd('myset', 'a')
    r.sadd('myset', 'b')
    r.sadd('myset', 'c')
    set_value = r.smembers('myset')
    # print("Set Operation - SMEMBERS: ", set_value)

    # Sorted Set Operations
    r.zadd('mysortedset', {'a': 1, 'b': 2, 'c': 3})
    sorted_set_value = r.zrange('mysortedset', 0, -1, withscores=True)
    # print("Sorted Set Operation - ZRANGE: ", sorted_set_value)

    # Increment Operation
    r.set('counter', 0)
    r.incr('counter')
    r.incr('counter')
    counter_value = r.get('counter')
    # print("Increment Operation: ", counter_value)

    # Delete Operation
    r.delete('key1')
    deleted_value = r.get('key1')
    # print("Delete Operation: ", deleted_value)
