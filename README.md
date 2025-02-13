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


# Output Of TASK 1

![Image](https://github.com/user-attachments/assets/7ffe8fc0-738c-48be-a6d3-4328a26f3e11)

# TASK DESCRIPTION OF TASK 2
This script is designed to scan a given website for two common types of web application vulnerabilities: SQL Injection (SQLi) and Cross-Site Scripting (XSS). It checks whether the website is susceptible to these attacks and reports back if any vulnerabilities are found.
Key Components

    Libraries Used:

        requests: This library is used to make HTTP requests to the website.

        BeautifulSoup: This library helps parse HTML content, making it easier to extract information from web pages.

    SQL Injection Payloads: These are specially crafted strings that are used to test whether the website is vulnerable to SQL Injection. Examples include:

    xss_payloads = ['<script>alert(1)</script>', '<img src="x" onerror="alert(1)">', '<svg/onload=alert(1)>']
Functions

    check_sql_injection(url, params):

        This function takes a URL and a list of parameters to test.

        It iterates over each parameter and each SQL injection payload, modifying the URL to include the payload.

        It then sends a request to the modified URL and checks the response for signs of SQL Injection vulnerability (like "error" or "warning" messages).

        If it detects a vulnerability, it prints a message and returns True.

    check_xss(url, params):

        This function works similarly to the SQL injection checker but for XSS vulnerabilities.

        It iterates over each parameter and each XSS payload, modifying the URL to include the payload.

        It sends a request to the modified URL and checks if the payload appears in the response.

        If it detects a vulnerability, it prints a message and returns True.

    scan_url(url):

        This function is the main scanning function.

        It sends a request to the given URL and checks if the page can be fetched successfully.

        It then parses the HTML content using BeautifulSoup to find all forms on the page and extract the parameters.

        It calls the SQL injection and XSS checking functions with the extracted parameters.

        It prints whether any vulnerabilities were found.

    Main Function:

        This part of the script prompts the user to enter a URL to scan.

        It validates the URL to ensure it starts with "http://" or "https://".

        It calls the scan_url function to start the scanning process

# Output of Task 2

![Screenshot from 2025-02-13 13-35-54](https://github.com/user-attachments/assets/7f960b05-746e-4bd3-8ee7-d1b63ba2f51b)





