## tempcln.py

Simple utility to remove all temporary files from the `Windows\Temp` and `Windows\Prefetch` directories and user specific directory like `C:\Users\{WIN_USERS}\AppData\Local\Temp` except `Public` or `Default` accounts.  

> It does **_not removes_** the temp files which are being used by the operating system or any other application.

The Executable `tmpcln.exe` and can be executed directly on a Windows Machine without any external dependency or python interpreter. Just evoke the `exe` file and it will detect all temp directories and clean them. 