import customtkinter as ctk
import math

# Grundkonfiguration: Dark Mode und Blaues Farbschema
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class ModernCalc(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("NEON-CALC 3000")
        self.geometry("400x500")
        self.attributes("-alpha", 0.95)  # Leicht transparent für den coolen Look

        # --- UI Layout ---
        self.grid_columnconfigure((0, 1, 2, 3), weight=1)
        self.grid_rowconfigure((0, 1, 2, 3, 4), weight=1)

        # Anzeige / Display
        self.result_var = ctk.StringVar(value="0")
        self.display = ctk.CTkLabel(self, textvariable=self.result_var, 
                                    font=ctk.CTkFont(size=40, weight="bold"),
                                    anchor="e", fg_color="#1A1A1A", 
                                    corner_radius=10, height=80)
        self.display.grid(row=0, column=0, columnspan=4, padx=20, pady=20, sticky="nsew")

        # Eingabefelder (für a und b laut deiner Aufgabe)
        self.entry_a = ctk.CTkEntry(self, placeholder_text="Zahl A", font=("Orbitron", 16), justify="center")
        self.entry_a.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky="ew")

        self.entry_b = ctk.CTkEntry(self, placeholder_text="Zahl B", font=("Orbitron", 16), justify="center")
        self.entry_b.grid(row=1, column=2, columnspan=2, padx=10, pady=10, sticky="ew")

        # Buttons mit Hover-Effekt und Neon-Farben
        ops = [
            ('+', "#1f538d"), ('-', "#1f538d"), 
            ('*', "#1f538d"), ('/', "#1f538d")
        ]

        for i, (op, color) in enumerate(ops):
            btn = ctk.CTkButton(self, text=op, 
                                command=lambda o=op: self.calculate(o),
                                font=ctk.CTkFont(size=25, weight="bold"),
                                fg_color=color,
                                hover_color="#5e17eb", # Lila-Glow beim Drüberfahren
                                corner_radius=15,
                                height=60)
            btn.grid(row=2, column=i, padx=5, pady=10)

        # Extra-Effekt: Ein "Clear" Button, der alles zurücksetzt
        self.clear_btn = ctk.CTkButton(self, text="RESET SYSTEM", 
                                       command=self.reset,
                                       fg_color="#BF616A", hover_color="#ff0000")
        self.clear_btn.grid(row=3, column=0, columnspan=4, padx=20, pady=10, sticky="ew")

        # Statuszeile
        self.status = ctk.CTkLabel(self, text="SYSTEM READY", font=("Consolas", 10), text_color="#00FF00")
        self.status.grid(row=4, column=0, columnspan=4)

    def calculate(self, op):
        try:
            val_a = float(self.entry_a.get())
            val_b = float(self.entry_b.get())
            
            if op == '+': res = val_a + val_b
            elif op == '-': res = val_a - val_b
            elif op == '*': res = val_a * val_b
            elif op == '/': res = val_a / val_b if val_b != 0 else "NAN"
            
            # Animationseffekt simulieren: Text kurz ändern
            self.result_var.set(str(res))
            self.status.configure(text="CALCULATION COMPLETE", text_color="#00FF00")
            
        except:
            self.result_var.set("ERROR")
            self.status.configure(text="INPUT CORRUPTED", text_color="#FF0000")

    def reset(self):
        self.entry_a.delete(0, 'end')
        self.entry_b.delete(0, 'end')
        self.result_var.set("0")
        self.status.configure(text="SYSTEM REBOOTED", text_color="#00FF00")

if __name__ == "__main__":
    app = ModernCalc()
    app.mainloop()