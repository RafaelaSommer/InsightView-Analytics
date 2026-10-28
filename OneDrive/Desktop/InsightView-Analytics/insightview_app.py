"""
InsightView Analytics — aplicativo principal.
Execute com: python insightview_app.py
"""
from src.ui.main_window import InsightViewApp

if __name__ == "__main__":
    app = InsightViewApp()
    app.mainloop()
