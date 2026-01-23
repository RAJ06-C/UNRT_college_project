
import subprocess
import sys
import time
import socket
import os
import shutil
import platform
from pyfiglet import Figlet

f = Figlet(font="slant")
ascii_art = f.renderText("UNRT BY GROUP2")

# ANSI Color Codes for "Beautiful" Output
class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

# Enable Windows ANSI support
if os.name == 'nt':
    os.system('color')

GROUP_NAME = "CYBER SENTINELS"
TOOL_NAME = "Unified Network Reconnaissance Toolkit (UNRT)"
OS_TYPE = platform.system()

def print_banner():
    # Clear screen based on OS
    if OS_TYPE == "Windows":
        os.system("cls")
    else:
        os.system("clear")

    banner = f"""
{Colors.CYAN}{Colors.BOLD}
=============================================================================
{ascii_art}
=============================================================================

      {Colors.HEADER}{TOOL_NAME}{Colors.CYAN}
      Developed solely for Educational & Ethical Testing Purposes
      Developer: {Colors.WARNING}Raj kumar{Colors.CYAN}
      By Group: {Colors.WARNING}{GROUP_NAME}{Colors.CYAN}
      Running on: {Colors.GREEN}{OS_TYPE}{Colors.CYAN}

=============================================================================
{Colors.ENDC}
    """
    print(banner)
    time.sleep(1)

def get_target():
    print(f"{Colors.GREEN}[+] Please enter the target (IP, Hostname, or URL):{Colors.ENDC} ", end="")
    target = input().strip()
    
    # URL sanitation
    if target.startswith("http://"):
        target = target[7:]
    elif target.startswith("https://"):
        target = target[8:]
    
    target = target.rstrip("/")
    print(f"\n{Colors.BLUE}[*] Target acquired: {Colors.BOLD}{target}{Colors.ENDC}")
    return target

def resolve_target(target):
    try:
        ip = socket.gethostbyname(target)
        print(f"{Colors.BLUE}[*] Resolved {target} to {ip}{Colors.ENDC}")
        return ip
    except socket.gaierror:
        print(f"{Colors.WARNING}[!] Could not resolve hostname. Proceeding with raw input.{Colors.ENDC}")
        return target

def check_tool_availability(tool_cmd):
    """
    Checks if a tool is available in the system PATH.
    Returns the executable path or None.
    """
    # Simply check the first word of the command
    executable = tool_cmd.split()[0]
    return shutil.which(executable)

def run_command(command, tool_label, description):
    print(f"\n{Colors.HEADER}========================================")
    print(f"[*] Starting {tool_label}")
    print(f"    Desc: {description}")
    print(f"========================================{Colors.ENDC}\n")
    
    # 1. Check if tool exists
    if not check_tool_availability(command):
        print(f"{Colors.WARNING}[!] Tool '{command.split()[0]}' not found in system PATH.")
        if OS_TYPE == "Windows" and command.split()[0] in ['hping3', 'unicornscan']:
            print(f"    Note: {command.split()[0]} is typically a Linux tool.")
            print(f"    Recommendation: Run this script via WSL or install a Windows port.")
        print(f"    Skipping...{Colors.ENDC}")
        return

    print(f"{Colors.CYAN}[DEBUG] Executing: {command}{Colors.ENDC}\n")
    
    try:
        process = subprocess.Popen(
            command, 
            shell=True, 
            stdout=subprocess.PIPE, 
            stderr=subprocess.PIPE,
            text=True,
            bufsize=1,
            universal_newlines=True
        )

        # Real-time output
        if process.stdout:
            for line in process.stdout:
                sys.stdout.write(f"{Colors.GREEN}   > {line.strip()}{Colors.ENDC}\n")
                sys.stdout.flush()

        process.wait()
        
        if process.returncode != 0:
            print(f"\n{Colors.FAIL}[!] {tool_label} process finished with errors.{Colors.ENDC}")
            # Show stderr specifically if it failed
            err_output = process.stderr.read()
            if err_output:
                print(f"{Colors.FAIL}Error Details:\n{err_output}{Colors.ENDC}")
        else:
            print(f"\n{Colors.BLUE}[*] {tool_label} completed successfully.{Colors.ENDC}")

    except Exception as e:
        print(f"\n{Colors.FAIL}[!] Critical Error running {tool_label}: {e}{Colors.ENDC}")

def main():
    try:
        print_banner()
        target_host = get_target()
        target_ip = resolve_target(target_host)
        
        print(f"\n{Colors.BOLD}Starting Unified Network Reconnaissance Toolkit (UNRT)...{Colors.ENDC}")
        time.sleep(2)

        # =================================================================
        # SCANNING MODULES
        # =================================================================

        # 1. NMAP
        # Uses -A for aggressive scan (OS detection, version detection, script scanning, traceroute)
        # Uses -T4 for faster execution
        nmap_args = "-T4 -A -v"
        if OS_TYPE == "Windows":
             # Sometimes Windows Nmap needs unprivileged mode if user is not Admin, 
             # remove -sS or use --unprivileged if raw sockets fail, but -A usually handles it or fails gracefully.
             pass
        run_command(f"nmap {nmap_args} {target_ip}", "Nmap Comprehensive Scan", "Port scan, OS detection, Version info")

        # 2. HPING3 (Packet Crafting)
        # Linux usually requires sudo for hping3. Windows usually doesn't have it.
        # Fallback to 'ping' or 'tracert' if hping3 is missing on Windows? 
        # For now, we attempt to run it if it exists.
        if OS_TYPE == "Linux":
            # sudo need might be an issue if script isn't run as root, but let's assume root or sudo permissions.
            hping_cmd = f"hping3 -c 4 -S -p 80 {target_ip}"
            run_command(hping_cmd, "Hping3 Connectivity", "Sending TCP SYN packets to port 80")
        else:
            # On Windows, we can use ping as a simple alternative if hping3 is missing
            if check_tool_availability("hping3"):
                run_command(f"hping3 -c 4 -S -p 80 {target_ip}", "Hping3 Connectivity", "Sending TCP SYN packets")
            else:
                # Fallback purely for demonstration
                run_command(f"ping -n 4 {target_ip}", "Ping (Fallback for Hping3)", "Standard ICMP Echo Request")

        # 3. DIRSEARCH (Web Content Scanner)
        # Assumes 'dirsearch' is in path. If python module, might need 'python -m dirsearch'
        dirsearch_exec = "dirsearch"
        if not shutil.which("dirsearch"):
             # Try determining if it's installed via pip but not in path
             dirsearch_exec = f"{sys.executable} -m dirsearch"
        
        # Extensions: php, html, js, txt
        run_command(f"{dirsearch_exec} -u http://{target_host} -e php,html,js,txt", "Dirsearch Web Scanner", "Brute-forcing web directories")

        # 4. NETCAT (NC/NCAT)
        # Windows often uses 'ncat', Linux 'nc'
        nc_tool = "nc"
        if not shutil.which("nc"):
            if shutil.which("ncat"):
                nc_tool = "ncat"
        
        # -z: Zero-I/O mode (scanning), -v: Verbose, -w 2: Timeout
        # Scanning common ports 20-80 for demo
        run_command(f"{nc_tool} -v -z -w 2 {target_ip} 20-80", "Netcat Port Sweep", "Simple TCP connect scan for ports 20-80")

        # 5. UNICORNSCAN
        # Rare on Windows.
        if OS_TYPE == "Linux":
            run_command(f"unicornscan -v {target_ip}:a", "Unicornscan", "Asynchronous TCP scan")
        else:
            if check_tool_availability("unicornscan"):
                run_command(f"unicornscan -v {target_ip}:a", "Unicornscan", "Asynchronous TCP scan")
            else:
                print(f"\n{Colors.WARNING}[*] Unicornscan is primarily a Linux tool. Skipping on Windows.{Colors.ENDC}")

        print(f"\n{Colors.HEADER}=====================================================")
        print(f"   UNRT Scan Sequence Completed for: {target_host}")
        print(f"====================================================={Colors.ENDC}")

    except KeyboardInterrupt:
        print(f"\n\n{Colors.FAIL}[!] User aborted operations.{Colors.ENDC}")
        sys.exit(0)

if __name__ == "__main__":
    main()
