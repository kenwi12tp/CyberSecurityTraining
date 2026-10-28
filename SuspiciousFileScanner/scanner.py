#assignment description
#You're a junior security analyst working for a company. Your boss suspects that someone has placed suspicious files on a company computer.
#Your job is to build a Python program that reads a file containing a list of filenames and identifies potentially dangerous ones.


#for this excercise i will treat ".exe",".bat", ".ps1", ".vbs" those file types as suspicios files
#.bat because its a batchfile that could run a script on a pc
#.exe because its an executable that could be malware
#.ps1 which is a powershell script which could run straight up commands in the powershell
#.vbs could run a script on microsofts VBScript technology aka a old scripting form
suspicious_files_identifier = [".exe", ".bat", ".ps1", ".vbs"]
suspicious_files=[]
formated_files = []
try:
    with open("files.txt", "r") as file:
        lines = file.readlines()
        for line in lines:
            newline = line.strip("\n")
            formated_files.append(newline)
        print(formated_files)
        for file in formated_files:
            if file[-4:] in suspicious_files_identifier:
                print(file)
                suspicious_files.append(file)

    with open("security_report.txt", "w") as report:
        report.write(f"Suspicious Files\n----------------\n")
        for file in suspicious_files:
            report.write(f"{file}\n")
        report.write(f"total suspicious files: {len(suspicious_files)}")


except FileNotFoundError:
    print("ERROR: The file does not exist!")