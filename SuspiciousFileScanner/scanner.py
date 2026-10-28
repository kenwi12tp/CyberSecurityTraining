#assignment description
#You're a junior security analyst working for a company. Your boss suspects that someone has placed suspicious files on a company computer.
#Your job is to build a Python program that reads a file containing a list of filenames and identifies potentially dangerous ones.


#for this excercise i will treat ".exe",".bat", ".ps1", ".vbs" those file types as suspicios files
#.bat because its a batchfile that could run a script on a pc
#.exe because its an executable that could be malware
#.ps1 which is a powershell script which could run straight up commands in the powershell
#.vbs could run a script on microsofts VBScript technology
suspicious_files = [".exe", ".bat", ".ps1", ".vbs"]