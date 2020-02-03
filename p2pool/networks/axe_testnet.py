from p2pool.axe import networks

PARENT = networks.nets['axe_testnet']
SHARE_PERIOD = 20 # seconds
CHAIN_LENGTH = 24*60*60//20 # shares
REAL_CHAIN_LENGTH = 24*60*60//20 # shares
TARGET_LOOKBEHIND = 100 # shares  //with that the pools share diff is adjusting faster, important if huge hashing power comes to the pool
SPREAD = 10 # blocks
IDENTIFIER = 'b6deb1e543fe2427'.decode('hex')
PREFIX = '198b644f6821e3b3'.decode('hex')
COINBASEEXT = '0e2f5032506f6f6c2d74415845332f'.decode('hex')
P2P_PORT = 19937
MIN_TARGET = 0
MAX_TARGET = 2**256//2**20 - 1
PERSIST = False
WORKER_PORT = 17923
BOOTSTRAP_ADDRS = 'p2pool.axeninja.pl test.p2pool.masternode.io test.p2pool.axe.siampm.com'.split(' ')
ANNOUNCE_CHANNEL = ''
VERSION_CHECK = lambda v: True
