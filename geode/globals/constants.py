# Solidity
import os

ZERO_BYTES = b''
ZERO_ADDRESS = "0x0000000000000000000000000000000000000000"
ZERO_BYTES32 = b'\x00' * 32

ETH = 10 ** 18
ETH2GWEI = 10 ** 9
DENOMINATOR = 10 ** 10

DEPOSIT_CLI_VERSION = '2.4.0'
WORD_LIST_PATH = os.path.join('geode', 'utils', 'bls')


# Execution-spec constants taken from https://github.com/ethereum/consensus-specs/blob/dev/specs/phase0/beacon-chain.md
DOMAIN_DEPOSIT = bytes.fromhex('03000000')
ETH1_ADDRESS_WITHDRAWAL_PREFIX = bytes.fromhex('01')

MIN_DEPOSIT_AMOUNT = 2 ** 0 * ETH
MAX_DEPOSIT_AMOUNT = 2 ** 5 * ETH

# Network
REFRESH_RATE = 60  # in seconds
MAX_ATTEMPT = 60
ATTEMPT_RATE = 0.1  # in seconds
