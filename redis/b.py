from redis.sentinel import Sentinel

if __name__ == "__main__":
    sentinel = Sentinel([('localhost', 26379)], socket_timeout=0.1)