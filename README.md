# CYBERSECURITY-ETHICALHACKING

**COMPANY**    :   CODTECH IT SOLUTIONS

**NAME**       :   DAFTARI AAGAM A

**INTERN ID**  :   CT12JGB

**DOMAIN**     :   CYBER SECURITY AND ETHICAL HACKING

**MENTOR NAME** :   NEELA SANTHOSH

**TASK DESCRIPTION OF TASK1** 

# File Integrity Monitoring Script: A Detailed Overview

# In the realm of cybersecurity, ensuring the integrity of files is paramount. The provided Python script serves as a basic file integrity monitoring tool, utilizing the SHA-256 hashing algorithm to detect changes in a specified file. This script is particularly useful for system administrators and security professionals who need to monitor critical files for unauthorized modifications, deletions, or corruptions.
Key Components of the Script

  #  Hash Calculation:
    The script begins with the calculate_file_hash function, which computes the SHA-256 hash of a given file. This function opens the file in binary mode and reads it in chunks of 4096 bytes to efficiently handle large files. The use of SHA-256 ensures a high level of security, as it produces a unique hash value for each unique file content. If the file is not found or an error occurs during reading, the function gracefully handles exceptions and returns None.

   # Monitoring Functionality:
    The monitor_file function is the core of the script. It initiates the monitoring process by calculating the initial hash of the specified file. The function then enters an infinite loop, where it periodically checks the file for changes based on a defined interval (defaulting to 5 seconds). This interval can be adjusted to suit the user’s needs, allowing for more or less frequent checks depending on the criticality of the file being monitored.

     # Change Detection:
    Within the loop, the script recalculates the file's hash and compares it to the previously stored hash. If a discrepancy is detected, the script alerts the user, indicating that the file has changed. It provides both the old and new hash values, allowing the user to understand the extent of the change. If no changes are detected, the script simply informs the user that the file remains unchanged.

  #  User Interaction:
    The script is designed to be user-friendly. It prints informative messages to the console, guiding the user through the monitoring process. This feedback is crucial for users who may not be familiar with the underlying mechanics of file integrity monitoring.

Practical Applications

The practical applications of this script are numerous. Organizations can use it to monitor critical configuration files, sensitive documents, or any files that, if altered, could lead to security vulnerabilities or operational disruptions. For instance, system administrators can monitor system files to detect unauthorized changes that may indicate a security breach. Similarly, businesses can track changes to financial records or customer data to ensure compliance with regulations such as GDPR or HIPAA.
