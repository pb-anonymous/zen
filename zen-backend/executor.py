import os
import subprocess
import platform
import winreg
from pptx import Presentation # type: ignore
import webbrowser

GENERATED_DIR = "generated_code"
os.makedirs(GENERATED_DIR, exist_ok=True)

# URI protocols for Windows apps
APP_PROTOCOLS = {
    "spotify": "spotify:",
    "whatsapp": "whatsapp:",
    "discord": "discord:",
    "telegram": "tg:",
    "calculator": "calc:",
    "calc": "calc:",
    "camera": "microsoft.windows.camera:",
    "store": "ms-windows-store:",
    "microsoft store": "ms-windows-store:",
    "edge": "microsoft-edge:",
    "mail": "mailto:",
    "calendar": "outlookcal:",
    "settings": "ms-settings:",
    "vscode": "vscode:",
    "vs code": "vscode:",
    "code": "vscode:",
    "teams": "msteams:",
    "itunes": "itunes:",
}

# Known executable names / aliases
APP_ALIASES = {
    "notepad": "notepad.exe",
    "notes": "notepad.exe",
    "file manager": "explorer.exe",
    "explorer": "explorer.exe",
    "files": "explorer.exe",
    "chrome": "chrome.exe",
    "google chrome": "chrome.exe",
    "firefox": "firefox.exe",
    "opera": "opera.exe",
    "opera gx": "opera.exe",
    "edge": "msedge.exe",
    "cmd": "cmd.exe",
    "terminal": "wt.exe",
    "powershell": "powershell.exe",
    "word": "winword.exe",
    "excel": "excel.exe",
    "powerpoint": "powerpnt.exe",
    "paint": "mspaint.exe",
    "task manager": "taskmgr.exe",
    "taskmgr": "taskmgr.exe",
    "control panel": "control.exe",
    "photoshop": "photoshop.exe",
    "vscode": "code.cmd",
    "vs code": "code.cmd",
    "code": "code.cmd",
}

def open_file_in_editor(file_path):
    """Opens a generated file in VS Code, Notepad, or default app on the user's desktop"""
    abs_path = os.path.abspath(file_path)
    ext = os.path.splitext(file_path)[1].lower()

    if ext in ['.pptx', '.pdf', '.docx', '.xlsx']:
        try:
            os.startfile(abs_path)
            return True
        except:
            return False

    # For code and text files, prefer VS Code, fallback to Notepad
    try:
        subprocess.Popen(['code', abs_path], shell=True)
        return True
    except:
        pass

    try:
        subprocess.Popen(['notepad.exe', abs_path])
        return True
    except:
        pass

    try:
        os.startfile(abs_path)
        return True
    except:
        return False

def open_app(app_name):
    """Opens ANY app on Windows reliably using protocols, WindowsApps, or executable paths"""
    app_clean = app_name.lower().strip()
    print(f"🔍 Attempting to open app: '{app_clean}'")

    # 1. URI Protocol (Fastest and 100% reliable for apps like Spotify, WhatsApp, Calc)
    if app_clean in APP_PROTOCOLS:
        try:
            proto = APP_PROTOCOLS[app_clean]
            print(f"  [1/5] Trying URI protocol: {proto}")
            os.startfile(proto)
            print(f"✓ Opened {app_name} via protocol {proto}")
            return True
        except Exception as e:
            print(f"  [1/5] Protocol failed: {e}")

    # 2. WindowsApps execution aliases (%LOCALAPPDATA%\Microsoft\WindowsApps)
    try:
        win_apps_dir = os.path.expandvars(r"%LOCALAPPDATA%\Microsoft\WindowsApps")
        if os.path.exists(win_apps_dir):
            for file in os.listdir(win_apps_dir):
                file_lower = file.lower()
                target_exe = f"{app_clean}.exe"
                if file_lower == target_exe or file_lower == app_clean or file_lower.startswith(app_clean + ".exe"):
                    full_path = os.path.join(win_apps_dir, file)
                    print(f"  [2/5] Launching from WindowsApps: {full_path}")
                    os.startfile(full_path)
                    print(f"✓ Opened {app_name} via WindowsApps")
                    return True
    except Exception as e:
        print(f"  [2/5] WindowsApps failed: {e}")

    # 3. Known app command aliases (notepad.exe, chrome.exe, explorer.exe, etc.)
    cmd = APP_ALIASES.get(app_clean, app_clean)
    try:
        print(f"  [3/5] Trying os.startfile('{cmd}')")
        os.startfile(cmd)
        print(f"✓ Opened {app_name} via os.startfile")
        return True
    except Exception as e:
        print(f"  [3/5] os.startfile failed: {e}")

    # 4. Try cmd start
    try:
        print(f"  [4/5] Trying cmd start for: {cmd}")
        subprocess.Popen(f'start "" "{cmd}"', shell=True)
        res = subprocess.run(["where.exe", cmd], capture_output=True, text=True, timeout=2)
        if res.returncode == 0:
            print(f"✓ Opened {app_name} via cmd start")
            return True
    except Exception as e:
        print(f"  [4/5] cmd start failed: {e}")

    # 5. Targeted search in Program Files and LocalAppData Programs
    search_dirs = [
        os.path.expandvars(r"%LOCALAPPDATA%\Programs"),
        os.getenv('ProgramFiles'),
        os.getenv('ProgramFiles(x86)')
    ]
    print(f"  [5/5] Searching standard install locations...")
    for base_dir in search_dirs:
        if not base_dir or not os.path.exists(base_dir):
            continue
        try:
            for item in os.listdir(base_dir):
                item_lower = item.lower()
                if app_clean in item_lower:
                    item_path = os.path.join(base_dir, item)
                    if os.path.isfile(item_path) and item_path.lower().endswith('.exe'):
                        os.startfile(item_path)
                        print(f"✓ Found and opened: {item_path}")
                        return True
                    elif os.path.isdir(item_path):
                        for subfile in os.listdir(item_path):
                            if subfile.lower().endswith('.exe') and (app_clean in subfile.lower()):
                                exe_path = os.path.join(item_path, subfile)
                                os.startfile(exe_path)
                                print(f"✓ Found and opened: {exe_path}")
                                return True
        except Exception:
            pass

    print(f"✗ Could not find or open app: {app_name}")
    return False

def get_website_for_app(app_name):
    """Get official website/web version for an app"""
    app_lower = app_name.lower().strip()
    
    websites = {
        "whatsapp": "https://web.whatsapp.com/",
        "spotify": "https://open.spotify.com/",
        "telegram": "https://web.telegram.org/",
        "discord": "https://discord.com/",
        "slack": "https://app.slack.com/",
        "microsoft store": "https://www.microsoft.com/en-us/store",
        "store": "https://www.microsoft.com/en-us/store",
        "github": "https://github.com/",
        "gmail": "https://mail.google.com/",
        "youtube": "https://www.youtube.com/",
    }
    
    return websites.get(app_lower, f"https://www.google.com/search?q={app_name}")

def execute_plan(plan):
    results = []

    for step in plan.get("actions", []):
        action = step.get("type")

        # =======================
        # OPEN APPLICATION
        # =======================
        if action == "open_application":
            name = step.get("name", "").strip()

            if open_app(name):
                results.append(f"✓ Opened {name}")
            else:
                # Fallback: Try to open website
                website = get_website_for_app(name)
                try:
                    webbrowser.open(website)
                    results.append(f"✓ {name} desktop app not found. Opened web version: {website}")
                except:
                    results.append(f"Could not open {name} or web version")

        # =======================
        # OPEN WEBSITE
        # =======================
        elif action == "open_website":
            url = step.get("url", "")
            try:
                webbrowser.open(url)
                results.append(f"✓ Opened website: {url}")
            except Exception as e:
                results.append(f"Could not open website: {e}")

        # =======================
        # WRITE FILE
        # =======================
        elif action == "write_file":
            file_name = step.get("file_name", "output.txt")
            content = step.get("content", "")
            path = os.path.join(GENERATED_DIR, file_name)

            with open(path, "w", encoding="utf-8") as f:
                f.write(content)

            # Open file in VS Code or Notepad on desktop
            open_file_in_editor(path)

            ext = os.path.splitext(file_name)[1].lstrip('.').lower() or "text"
            results.append(f"✓ Created and opened **{file_name}**:\n```{ext}\n{content}\n```")

        # =======================
        # CREATE PPT (REAL)
        # =======================
        elif action == "create_ppt":
            prs = Presentation()

            title_slide = prs.slides.add_slide(prs.slide_layouts[0])
            title_slide.shapes.title.text = step.get("title", "Presentation")

            for s in step.get("slides", []):
                slide = prs.slides.add_slide(prs.slide_layouts[1])
                slide.shapes.title.text = s.get("title", "")
                slide.placeholders[1].text = s.get("content", "")

            path = os.path.join(GENERATED_DIR, step.get("title", "Presentation") + ".pptx")
            prs.save(path)

            if platform.system() == "Windows":
                os.startfile(path)
            else:
                subprocess.Popen(["xdg-open", path])
            results.append(f"✓ Created and opened PowerPoint: **{step.get('title', 'Presentation')}.pptx**")

        # =======================
        # RESPOND
        # =======================
        elif action == "respond":
            results.append(step.get("message", ""))

    return "\n\n".join(results)
