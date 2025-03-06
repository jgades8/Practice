import hashlib
import json

# List of traits to hash
traits = ["Craftsman", "Pragmatic", "Curious", "Methodical", "Driven", "Collaborator"]


def gen_hash(traits):
    hashes = []
    for trait in traits:
        hash_obj = hashlib.blake2b(trait.encode('utf-8'), key=b"Close-01c89a09", digest_size=64)
        hex_digest = hash_obj.hexdigest()
        hashes.append(hex_digest)
    json_hashes = json.dumps(hashes)
    return json_hashes


hashes = gen_hash(traits)
print(hashes)
