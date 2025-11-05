from pybloom_live import BloomFilter

# Create a Bloom filter with capacity and acceptable false positive rate
bf = BloomFilter(capacity=1000, error_rate=0.001)

# Add a fake transaction ID
bf.add("my_txid")

# Test probabilistic membership
print("my_txid" in bf)  
print("other_txid" in bf)    

# Show internal bit array (Bloom filter representation)
print("Bloom filter bit array:", bf.bitarray)
