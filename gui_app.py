import customtkinter as ctk
import threading
import sys
import io
from app import main as start_recon  # Maan lete hain app.py mein function 'main' hai

class TerminalRedirector(io.StringIO):
    def __init__(self, text_widget):
        super().__init__()
        self.text_widget = text_widget

    def write(self, string):
        self.text_widget.insert("end", string)
        self.text_widget.see("end")

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

        self.btn = ctk.CTkButton(self, text="Launch Recon", command=self.run_task, fg_color="#1f538d")
        self.btn.pack(pady=10)

        self.output_area = ctk.CTkTextbox(self, width=850, height=400, font=("Consolas", 12))
        self.output_area.pack(pady=20)

    def run_task(self):
        target = self.entry.get()
        if not target: return
        
        self.output_area.delete("1.0", "end")
        
        # Terminal output ko GUI mein redirect karna
        sys.stdout = TerminalRedirector(self.output_area)
        
        # Thread chalu karna taake app hang na ho
        thread = threading.Thread(target=self.execute_logic, args=(target,))
        thread.start()

    def execute_logic(self, target):
        try:
            # Ye aapke app.py ko run karega
            start_recon(target) 
        except Exception as e:
            print(f"\n[!] Error: {str(e)}")
        finally:
            sys.stdout = sys.__stdout__ # Wapas normal kar dena

if __name__ == "__main__":
    app = ReconLitePro()
    app.mainloop()
