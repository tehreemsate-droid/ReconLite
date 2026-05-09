import customtkinter as ctk
import threading
import sys
import io
# 'app' se import karte waqt dhyan rakhein ke app.py mein 'main' function mojood ho
try:
    from app import main as start_recon 
except ImportError:
    def start_recon(target): print(f"[!] Error: app.py not found or main() missing.\nTarget was: {target}")

class TerminalRedirector:
    def __init__(self, text_widget):
        self.text_widget = text_widget

    def write(self, string):
        # GUI thread mein update karne ke liye lambda use hota hai
        self.text_widget.insert("end", string)
        self.text_widget.see("end")
        self.text_widget.update_idletasks() # Foran screen par dikhane ke liye

    def flush(self):
        pass

class ReconLitePro(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("ReconLite Pro v2.0")
        self.geometry("900x650")
        ctk.set_appearance_mode("dark")

        # UI Elements
        self.header = ctk.CTkLabel(self, text="RECON LITE PROFESSIONAL", font=("Impact", 30))
        self.header.pack(pady=20)

        self.entry = ctk.CTkEntry(self, width=500, placeholder_text="Target: e.g. example.com")
        self.entry.pack(pady=10)

        # command=lambda yahan isliye hai taake '1 argument' wala error khatam ho jaye
        self.btn = ctk.CTkButton(self, text="Launch Recon", command=lambda: self.run_task(), fg_color="#1f538d")
        self.btn.pack(pady=10)

        self.output_area = ctk.CTkTextbox(self, width=850, height=400, font=("Consolas", 12))
        self.output_area.pack(pady=20)

    def run_task(self):
        target = self.entry.get()
        if not target: 
            self.output_area.insert("end", "[!] Please enter a target URL first.\n")
            return
        
        self.output_area.delete("1.0", "end")
        self.output_area.insert("end", f"[*] Starting Professional Recon on: {target}\n" + "="*60 + "\n")
        
        # Terminal output redirector
        self.redir = TerminalRedirector(self.output_area)
        sys.stdout = self.redir
        
        # Thread taake GUI freeze na ho
        thread = threading.Thread(target=self.execute_logic, args=(target,), daemon=True)
        thread.start()

    def execute_logic(self, target):
        try:
            # Important: ensure start_recon function accepts exactly one argument
            start_recon(target) 
        except TypeError as te:
            print(f"\n[!] Function Error: {str(te)}")
            print("[*] Hint: Check if app.py main() accepts 'target' as an argument.")
        except Exception as e:
            print(f"\n[!] Unexpected Error: {str(e)}")
        finally:
            sys.stdout = sys.__stdout__ # Terminal wapas normal kar dein

if __name__ == "__main__":
    app = ReconLitePro()
    app.mainloop()
