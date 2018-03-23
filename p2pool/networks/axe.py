from p2pool.axe import networks

PARENT = networks.nets['axe']
SHARE_PERIOD = 20 # seconds
CHAIN_LENGTH = 24*60*60//20 # shares
REAL_CHAIN_LENGTH = 24*60*60//20 # shares
TARGET_LOOKBEHIND = 100 # shares  //with that the pools share diff is adjusting faster, important if huge hashing power comes to the pool
SPREAD = 10 # blocks
IDENTIFIER = '3A4E0C8EE3D735C8'.decode('hex')
PREFIX = '3A4E0ABD3A8CC80D'.decode('hex')
COINBASEEXT = '0D2F5032506F6F6C2D444153482F'.decode('hex')
P2P_PORT = 8999
MIN_TARGET = 0
MAX_TARGET = 2**256//2**20 - 1
PERSIST = True
WORKER_PORT = 7903
BOOTSTRAP_ADDRS = 
ANNOUNCE_CHANNEL = '#p2pool-axe'
VERSION_CHECK = lambda v: v >= 010100
