import hashlib

def double_sha256(b):
    return hashlib.sha256(hashlib.sha256(b).digest()).digest()

# Only one transaction in this block (coinbase)
txids = [
    bytes.fromhex("5c07673d4028c4a4515f8a19e9f3a0b8d0f4e941f36f75d81b056c020ed397da")[::-1]
]

# For a single transaction, Merkle root = txid itself
root = txids[0][::-1].hex()

print("Computed Merkle root:", root)
print("Expected Merkle root: 5c07673d4028c4a4515f8a19e9f3a0b8d0f4e941f36f75d81b056c020ed397da")
