# import logging
# from redis import Redis
# from redis.connection import ConnectionPool

# # Step 1: Dummy config
# class config:
#     REDIS_HOST = "localhost"
#     REDIS_PORT = 6379
#     REDIS_POOL_CONNECTIONS = 5

# # Step 2: Logger setup
# logger = logging.getLogger(__name__)
# logging.basicConfig(level=logging.INFO)

# # Step 3: Base Config class
# class Config:
#     def __init__(self, db):
#         self._client = None
#         self.connection_pool = None
#         self.db = db

#     @property
#     def redis_client(self):
#         if self._client is None:
#             self._client = self._get_redis_client()
#         return self._client

#     def _get_redis_client(self):
#         if self.db is None:
#             self.db = 0  # Default DB index
#         if self.connection_pool is None:
#             self.connection_pool = ConnectionPool(
#                 host=config.REDIS_HOST,
#                 port=config.REDIS_PORT,
#                 db=self.db,
#                 max_connections=config.REDIS_POOL_CONNECTIONS,
#             )
#         return Redis(
#             connection_pool=self.connection_pool,
#             decode_responses=True
#         )

# # Step 4: RedisCache class
# class RedisCache(Config):
#     def __init__(self, db=0):
#         super().__init__(db)

#     def health(self):
#         try:
#             if self.redis_client.ping():
#                 logger.info("✅ Redis is alive")
#                 return True
#         except Exception as e:
#             logger.error(f"❌ Redis ping failed: {e}")
#         return False

#     def set_value(self, key, value):
#         self.redis_client.set(key, value)
#         logger.info(f"Set {key} = {value}")

#     def get_value(self, key):
#         value = self.redis_client.get(key)
#         logger.info(f"Get {key} = {value}")
#         return value

# # Step 5: Try it out
# if __name__ == "__main__":
#     cache = RedisCache()

#     # Health check
#     if cache.health():
#         # Set a value
#         cache.set_value("user:1", "Aravind")

#         # Retrieve it
#         name = cache.get_value("user:1")

#         print(f"\n📌 Value from Redis: {name}")

# import json
# from redis import Redis

# class SimpleRedisCache:
#     def __init__(self):
#         self._client = None

#     @property
#     def redis_client(self):
#         if self._client is None:
#             self._client = Redis(host='localhost', port=6379, db=0, decode_responses=True)
#         return self._client

#     def read(self, key, is_json=True, response={}):
#         try:
#             data = self.redis_client.get(key)
#             if data is None:
#                 return response
#             else:
#                 if is_json:
#                     return json.loads(data)
#                 else:
#                     return data
#         except Exception as e:  # noqa
#             return response

#     def write(self, key, value):
#         # Automatically serialize to JSON if value is a dict
#         if isinstance(value, dict):
#             value = json.dumps(value)
#         self.redis_client.set(key, value)
# if __name__ == "__main__":
#     cache = SimpleRedisCache()

#     # Writing a value to Redis
#     data_to_cache = {"id": 1, "name": "Aravind", "role": "Engineer"}
#     cache.write("user:1001", data_to_cache)

#     # Reading it back
#     result = cache.read("user:1001")
#     print("Result from Redis (as JSON):", result)

#     # Reading raw string (non-JSON)
#     result_raw = cache.read("user:1001", is_json=False)
#     print("Result from Redis (raw string):", result_raw)

#     # Reading a non-existent key
#     missing = cache.read("user:9999", response={"message": "Not found"})
#     print("Missing key response:", missing)

import redis
import json

# Connect to Redis (adjust host/port if needed)
r = redis.Redis(host='localhost', port=6379, decode_responses=True)

# Hash name
hash_name = "user:1001"

# Step 1: Set values using HSET
r.hset(hash_name, "name", "Aravind")
r.hset(hash_name, "email", "aravind@example.com")
r.hset(hash_name, "roles", json.dumps(["admin", "editor"]))  # Store list as JSON string

# Step 2: Read a single value using HGET
print("Name:", r.hget(hash_name, "name"))

# Step 3: Read and parse a list
roles_raw = r.hget(hash_name, "roles")
roles = json.loads(roles_raw)
print("Roles:", roles)

# Step 4: Get all key-value pairs using HGETALL
print("Full Hash:", r.hgetall(hash_name))

# Step 5: Check if a key exists inside the hash
print("Does 'email' exist?:", r.hexists(hash_name, "email"))

# Step 6: Delete a field
r.hdel(hash_name, "email")
print("After deleting email:", r.hgetall(hash_name))

# Step 7: Get all keys in the hash
print("Keys inside hash:", r.hkeys(hash_name))
