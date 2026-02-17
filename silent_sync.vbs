Set WinScriptHost = CreateObject("WScript.Shell")
WinScriptHost.Run "powershell.exe -ExecutionPolicy Bypass -WindowStyle Hidden -File ""C:\Users\Gustavo\.gemini\antigravity\brain\sync_brain.ps1""", 0
Set WinScriptHost = Nothing
