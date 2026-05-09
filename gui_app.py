import customtkinter as ctk
import threading
import sys
import io
import time
from datetime import datetime

# Error Fix: Forcefully matching the argument requirement
try:
    from app import main as original_main
    def start_recon(target):
        # Agar app.py argument nahi leta to ye handle kar lega
        try:
            original_main(target)
        except TypeError:
            original_main() 
except ImportError:
    def start_recon(target): print(f"[!] Core module app.py missing.")

class TerminalRedirector:
    def __init__(self, text_widget):
        self.text_widget = text_widget
    def write(self, string):
        self.text_widget.insert("end", string)
        self.text_widget.see("end")
        self.text_widget.update_idletasks()
    def flush(self): pass

class ReconLiteUltra(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("ReconLite Pro v2.0 | Cyber Security Suite")
        self.geometry("1100x700")
        
        # Color Palette
        self.bg_color = "#0f0f12"
        self.accent_color = "#1f6aa5" # Neon Blue
        self.configure(fg_color=self.bg_color)

        # --- SIDEBAR ---
        self.sidebar = ctk.CTkFrame(self, width=200, corner_radius=0, fg_color="#16161d")
        self.sidebar.pack(side="left", fill="y")
        
        self.logo = ctk.CTkLabel(self.sidebar, text="RECON\nLITE", font=("Orbitron", 28, "bold"), text_color=self.accent_color)
        self.logo.pack(pady=30)
        
        self.status_lbl = ctk.CTkLabel(self.sidebar, text="● SYSTEM READY", text_color="#2ecc71", font=("Consolas", 12))
        self.status_lbl.pack(pady=10)

        # --- MAIN BODY ---
        self.main_container = ctk.CTkFrame(self, fg_color="transparent")
        self.main_container.pack(side="right", fill="both", expand=True, padx=20, pady=20)

        # Header
        self.header = ctk.CTkLabel(self.main_container, text="Target Intelligence Gathering", font=("Segoe UI", 22, "bold"))
        self.header.pack(anchor="w", pady=(0, 20))

        # Input Area (Modern Style)
        self.input_frame = ctk.CTkFrame(self.main_container, fg_color="#1c1c24", corner_radius=10)
        self.input_frame.pack(fill="x", pady=10)
        
        self.entry = ctk.CTkEntry(self.input_frame, placeholder_text="Enter target (e.g. scanme.nmap.org)", 
                                  width=600, height=45, border_width=0, fg_color="transparent")
        self.entry.pack(side="left", padx=10, pady=10)

        self.btn = ctk.CTkButton(self.input_frame, text="LAUNCH SCAN", font=("Arial", 13, "bold"),
                                 fg_color=self.accent_color, hover_color="#144870", height=40, width=120,
                                 command=self.run_task)
        self.btn.pack(side="right", padx=10)

        # Output Box (Terminal Style)
        self.output_area = ctk.CTkTextbox(self.main_container, fg_color="#000000", text_color="#00ff41", # Classic Hacker Green
                                          font=("Consolas", 14), border_width=1, border_color="#333333")
        self.output_area.pack(fill="both", expand=True, pady=10)

    def run_task(self):
        target = self.entry.get()
        if not target: return
        
        self.status_lbl.configure(text="● SCANNING...", text_color="#e67e22")
        self.output_area.delete("1.0", "end")
        self.output_area.insert("end", f"[{datetime.now().strftime('%H:%M:%S')}] INITIALIZING CYBER RECON ON: {target}\n")
        self.output_area.insert("end", "-"*80 + "\n")
        
        sys.stdout = TerminalRedirector(self.output_area)
        threading.Thread(target=self.execute_logic, args=(target,), daemon=True).start()

    def execute_logic(self, target):
        try:
            start_recon(target) 
        except Exception as e:
            print(f"\n[!] Error: {str(e)}")
        finally:
            self.status_lbl.configure(text="● SYSTEM READY", text_color="#2ecc71")
            sys.stdout = sys.__stdout__

if __name__ == "__main__":
    app = ReconLiteUltra()
    app.mainloop()
