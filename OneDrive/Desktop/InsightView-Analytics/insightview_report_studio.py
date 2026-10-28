"""InsightView Report Studio — importação e exportação de relatórios Excel."""
import os
import tkinter as tk
from tkinter import filedialog, messagebox
import customtkinter as ctk
import pandas as pd

from src.data.excel_reader import read_table
from src.data.data_cleaner import infer_dates
from src.analytics.area_detector import detect_area
from src.export.excel_exporter import export_report
from src.config.themes import BG, PANEL, TEXT, MUTED, ACCENT, BLUE, BORDER, AREAS

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class ReportStudio(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("InsightView Report Studio")
        self.geometry("900x620")
        self.minsize(760, 520)
        self.configure(fg_color=BG)
        self.df = pd.DataFrame()
        self.path = ""
        self.area_var = tk.StringVar(value="Automático")
        self._ui()

    def _ui(self):
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(2, weight=1)
        header = ctk.CTkFrame(self, fg_color=BG)
        header.grid(row=0, column=0, sticky="ew", padx=28, pady=(24, 12))
        ctk.CTkLabel(header, text="InsightView Report Studio", text_color=TEXT,
                     font=ctk.CTkFont(size=27, weight="bold")).pack(anchor="w")
        ctk.CTkLabel(header, text="Importe uma base, selecione a área e gere um relatório Excel profissional.",
                     text_color=MUTED, font=ctk.CTkFont(size=12)).pack(anchor="w", pady=(5, 0))
        actions = ctk.CTkFrame(self, fg_color=BG)
        actions.grid(row=1, column=0, sticky="ew", padx=28, pady=8)
        ctk.CTkButton(actions, text="Carregar Excel / CSV", command=self.load,
                      fg_color=ACCENT, hover_color="#27B99A", text_color="#07151D",
                      height=40).pack(side="left", padx=(0, 12))
        ctk.CTkLabel(actions, text="Área analisada:", text_color=MUTED).pack(side="left", padx=(0, 8))
        ctk.CTkOptionMenu(actions, values=AREAS, variable=self.area_var,
                          fg_color=PANEL, button_color=BLUE, width=210).pack(side="left")
        ctk.CTkButton(actions, text="Exportar relatório Excel", command=self.export,
                      fg_color=BLUE, hover_color="#3D7FE0", height=40).pack(side="right")
        self.info = ctk.CTkTextbox(self, fg_color=PANEL, text_color=TEXT, corner_radius=14,
                                   font=ctk.CTkFont(size=12))
        self.info.grid(row=2, column=0, sticky="nsew", padx=28, pady=(8, 18))
        self.info.insert("1.0", "Bem-vindo ao Report Studio.\n\n1. Carregue um arquivo .xlsx, .xls ou .csv.\n2. Selecione a área empresarial, se necessário.\n3. Exporte o relatório para o local desejado.\n\nO relatório pode incluir Dashboard, Dados, KPIs, Estatísticas, análise por categoria e comparação temporal conforme as colunas disponíveis.")
        self.info.configure(state="disabled")
        ctk.CTkLabel(self, text="InsightView Analytics • Report Studio • v1.0.0",
                     text_color=MUTED, font=ctk.CTkFont(size=10)).grid(row=3, column=0, sticky="e", padx=28, pady=(0, 12))

    def load(self):
        path = filedialog.askopenfilename(title="Selecionar base de dados",
            filetypes=[("Planilhas e CSV", "*.xlsx *.xls *.csv"), ("Todos os arquivos", "*.*")])
        if not path:
            return
        try:
            self.df = infer_dates(read_table(path))
            self.path = path
            detected = detect_area(self.df, path, self.area_var.get())
            self.info.configure(state="normal")
            self.info.delete("1.0", "end")
            self.info.insert("1.0",
                f"ARQUIVO CARREGADO\n{os.path.basename(path)}\n\n"
                f"Registros: {len(self.df):,}\nColunas: {len(self.df.columns)}\n"
                f"Valores ausentes: {int(self.df.isna().sum().sum())}\n"
                f"Linhas duplicadas: {int(self.df.duplicated().sum())}\n"
                f"Área detectada/s selecionada: {detected}\n\n"
                f"Colunas:\n" + "\n".join(f"• {c}" for c in self.df.columns) +
                "\n\nPrévia (até 30 linhas):\n" + self.df.head(30).to_string(index=False))
            self.info.configure(state="disabled")
        except Exception as exc:
            messagebox.showerror("Erro ao carregar arquivo", str(exc))

    def export(self):
        if self.df.empty:
            messagebox.showinfo("Sem dados", "Carregue uma planilha antes de exportar.")
            return
        path = filedialog.asksaveasfilename(title="Salvar relatório", defaultextension=".xlsx",
            initialfile="InsightView_Relatorio.xlsx", filetypes=[("Excel Workbook", "*.xlsx")],
            confirmoverwrite=True)
        if not path:
            return
        try:
            area = detect_area(self.df, self.path, self.area_var.get())
            export_report(path, self.df, self.df, area, os.path.basename(self.path), use_filtered=True)
            messagebox.showinfo("Concluído", f"Relatório salvo em:\n{path}")
        except Exception as exc:
            messagebox.showerror("Erro na exportação", str(exc))

if __name__ == "__main__":
    ReportStudio().mainloop()
