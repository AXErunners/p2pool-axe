from p2pool.axe import networks

PARENT = networks.nets['axe_testnet']
SHARE_PERIOD = 20 # seconds
CHAIN_LENGTH = 24*60*60//20 # shares
REAL_CHAIN_LENGTH = 24*60*60//20 # shares
TARGET_LOOKBEHIND = 100 # shares  //with that the pools share diff is adjusting faster, important if huge hashing power comes to the pool
SPREAD = 10 # blocks
IDENTIFIER = 'b6deb1e514fe2427'.decode('hex')
PREFIX = '198b444f6821e3b3'.decode('hex')
COINBASEEXT = '0e2f5032506f6f6c2d74415845332f'.decode('hex')
P2P_PORT = 18997
MIN_TARGET = 0
MAX_TARGET = 2**256//2**20 - 1
PERSIST = False
WORKER_PORT = 17923
BOOTSTRAP_ADDRS = '149.248.61.149 45.77.1.27 207.148.15.191'.split(' ')
ANNOUNCE_CHANNEL = ''
VERSION_CHECK = lambda v: True
