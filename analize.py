import os

errors = 0
ransomware_detected =  0
malware_detected = 0
failed_login_attempts = 0
sqli_attempts = 0
unauthorized_access = 0
brute_force_attempts = 0
txt = input("Name of log:  ")
script_folder = os.path.dirname(os.path.abspath(__file__))
exact_path = os.path.join(script_folder, txt)
with open(exact_path) as file:
    for line in file:
        print(line.strip())
        if "CRASH" in line:
            print("Uh oh, something crashed in the line above!")
            errors += 1
        elif "MALWARE_DETECTED" in line:
            print("Malware detected in the line above!")
            errors += 1
            malware_detected += 1 
        elif "LOGIN_SUCCESS" in line:
            print("A person logged on in the line above!")
        elif "FAILED_LOGIN" in line:
            print("Someone failed to log on in the line above")
            errors += 1
            failed_login_attempts += 1
        elif "UNAUTHORIZED_ACCESS" in line:
            print("Someone with unauthorized access is in the system! Line above")
            errors += 1
            unauthorized_access += 1
        elif "SQL_INJECTION_TRY" in line:
            print("Potential SQLi attack detected in line above")
            errors += 1
            sqli_attempts += 1
        elif "BRUTE_FORCE_ATTEMPT" in line:
            print("A brute force attempt was made in the line above")
            brute_force_attempts += 1
            errors += 1
        elif "DDOS_BURST_REQUESTS" in line:
            print("A sudden burst of requests is in the line above!")
            errors += 1
        elif "FILE_ENCRYPTION_STARTED" in line:
            print("CRITICAL, Ransomware or file encryption, likely ransomware!")
            ransomware_detected += 1
            errors += 1
        elif "SHADOW_COPIES_DELETED" in line:
            print("CRITICAL, ransomware detected!")
            ransomware_detected += 1
            errors += 1 
original_file = txt
new_file = original_file.replace("log-","analyzed-log-")
exact_report_path = os.path.join(script_folder, new_file)
with open(exact_report_path, "w") as report_file:
    report_file.write("SECURITY REPORT\n")
    report_file.write("Error count:")
    report_file.write(str(errors) + "\n")
    if not ransomware_detected == 0:
        report_file.write("CRITICAL, RANSOMWARE DETECTED!\n")
    if not malware_detected == 0:
        report_file.write("CRITICAL, MALWARE DETECTED!\n")
    if failed_login_attempts >= 3:
        report_file.write("POSSIBLE BRUTE FORCE ATTEMPT!\n")
    if not brute_force_attempts == 0:
        report_file.write("CRITICAL, BRUTE FORCE ATTEMPT!\n")
    if not sqli_attempts == 0:
        report_file.write("CTRITICAL, SQLi ATTACK!\n")
print(f"File {new_file} created in this folder")
input("Press enter to close window")
