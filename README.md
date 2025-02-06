 \] # CYBERSECURITY-ETHICALHACKING

**COMPANY**    :   CODTECH IT SOLUTIONS

**NAME**       :   DAFTARI AAGAM A

**INTERN ID**  :   CT12JGB

**DOMAIN**     :   CYBER SECURITY AND ETHICAL HACKING

**MENTOR NAME** :   NEELA SANTHOSH

**TASK DESCRIPTION OF TASK1** 

The provided Python script is a simple yet effective tool for monitoring file integrity by calculating and comparing hash values. File integrity checking is crucial in various applications, such as ensuring that configuration files remain unchanged, verifying the authenticity of downloaded files, and detecting unauthorized modifications to sensitive data. This script leverages the SHA-256 hashing algorithm, which is widely recognized for its security and reliability.

### Overview of the Script

The script begins by importing necessary libraries: `hashlib` for hashing, `os` for file operations, and `time` for implementing delays in monitoring. The core functionality revolves around three main functions: `calculate_hash`, `save_hash`, and `load_hash`, along with the `monitor_file` function that orchestrates the monitoring process.

1. **Calculating the Hash**: The `calculate_hash` function takes a file path as input and computes its SHA-256 hash. It reads the file in binary mode and processes it in chunks to handle large files efficiently. This approach minimizes memory usage, making the script suitable for files of varying sizes. The computed hash is returned as a hexadecimal string.

2. **Saving the Hash**: The `save_hash` function appends the file path and its corresponding hash value to a text file named `file_hashes.txt`. Each entry is formatted as `file_path:hash_value`, allowing for easy retrieval and comparison later. This simple text-based storage method avoids the complexity of structured data formats like JSON, making it straightforward to implement and understand.

3. **Loading the Hash**: The `load_hash` function reads the `file_hashes.txt` file to retrieve the stored hash for a given file path. It checks if the file exists and iterates through each line, splitting the stored data to find the hash corresponding to the specified file. If the file is not found or no hash exists, it returns `None`.

4. **Monitoring the File**: The `monitor_file` function is the heart of the script. It first checks for an existing hash of the specified file. If no previous hash is found, it calculates the current hash and saves it. If a hash is found, it compares the current hash with the stored hash. If they differ, it indicates that the file has changed, and the new hash is saved. The function then enters a loop, continuously checking the file at specified intervals (defaulting to 10 seconds) for any changes.

### User Interaction

The script is designed to be user-friendly. When executed, it prompts the user to enter the path of the file they wish to monitor. It checks if the specified file exists and begins the monitoring process. The user receives real-time feedback on whether the file has changed, along with the previous and current hash values.
