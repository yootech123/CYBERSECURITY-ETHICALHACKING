import hashlib
import os
import time

def calculate_hash(file_path):
    """Calculate the SHA-256 hash of a file."""
    hash_sha256 = hashlib.sha256()
    with open(file_path, 'rb') as f:
        # Read the file in chunks to avoid memory issues with large files
        for byte_block in iter(lambda: f.read(4096), b""):
            hash_sha256.update(byte_block)
    return hash_sha256.hexdigest()

def save_hash(file_path, hash_value):
    """Save the hash value to a text file."""
    with open('file_hashes.txt', 'a') as f:
        f.write(f"{file_path}:{hash_value}\n")

def load_hash(file_path):
    """Load the hash value from the text file."""
    if not os.path.isfile('file_hashes.txt'):
        return None
    with open('file_hashes.txt', 'r') as f:
        for line in f:
            stored_path, stored_hash = line.strip().split(':')
            if stored_path == file_path:
                return stored_hash
    return None

def monitor_file(file_path, check_interval=10):
    """Monitor the file for changes."""
    print(f"Monitoring changes to: {file_path}")
    previous_hash = load_hash(file_path)
    current_hash = calculate_hash(file_path)

    if previous_hash is None:
        print(f"No previous hash found. Saving current hash: {current_hash}")
        save_hash(file_path, current_hash)
    elif previous_hash != current_hash:
        print(f"File has changed! Previous hash: {previous_hash}, Current hash: {current_hash}")
        save_hash(file_path, current_hash)
    else:
        print(f"No changes detected. Current hash: {current_hash}")

    # Continuously monitor the file
    while True:
        time.sleep(check_interval)
        current_hash = calculate_hash(file_path)
        if previous_hash != current_hash:
            print(f"File has changed! Previous hash: {previous_hash}, Current hash: {current_hash}")
            save_hash(file_path, current_hash)
            previous_hash = current_hash
        else:
            print(f"No changes detected. Current hash: {current_hash}")

if __name__ == "__main__":
    # Specify the file to monitor
    file_to_monitor = input("Enter the path of the file to monitor: ")
    if os.path.isfile(file_to_monitor):
        monitor_file(file_to_monitor)
    else:
        print("The specified file does not exist.")

