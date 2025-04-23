import tkinter as tk
from tkinter import ttk, colorchooser
import argparse
import json
import os

DATA_FILE = "toc_data.json"

class TOCSection:
    def __init__(self, master, title, items=None, color="#000000", remove_callback=None):
        self.master = master
        self.title = title
        self.items = items or []
        self.color = color
        self.remove_callback = remove_callback

        self.frame = ttk.Frame(master)
        self.frame.pack(fill="x", pady=5, padx=5)

        top_frame = ttk.Frame(self.frame)
        top_frame.pack(fill="x")

        self.var = tk.BooleanVar(value=True)
        self.checkbox = tk.Checkbutton(top_frame, text=self.title, variable=self.var, command=self.toggle, fg=self.color)
        self.checkbox.pack(side="left", anchor="w")

        color_btn = ttk.Button(top_frame, text="Set Color", command=self.pick_color)
        color_btn.pack(side="right", padx=5)

        remove_btn = ttk.Button(top_frame, text="Remove Section", command=self.remove_section)
        remove_btn.pack(side="right")

        self.items_frame = ttk.Frame(self.frame)
        self.items_frame.pack(fill="x", padx=20)

        self.entries = []
        for item in self.items:
            self.add_item(item)

        self.add_item_entry = ttk.Entry(self.items_frame)
        self.add_item_entry.pack(fill="x", pady=2)
        self.add_item_entry.bind("<Return>", self.add_item_from_entry)

    def toggle(self):
        if self.var.get():
            self.items_frame.pack(fill="x", padx=20)
        else:
            self.items_frame.forget()

    def pick_color(self):
        color_code = colorchooser.askcolor(title="Choose Section Title Color")
        if color_code and color_code[1]:
            self.color = color_code[1]
            self.checkbox.configure(fg=self.color)

    def add_item_from_entry(self, event=None):
        text = self.add_item_entry.get().strip()
        if text:
            self.add_item(text)
            self.add_item_entry.delete(0, tk.END)

    def add_item(self, text):
        row = ttk.Frame(self.items_frame)
        row.pack(anchor="w", fill="x", pady=1)

        label = ttk.Label(row, text="- " + text)
        label.pack(side="left", anchor="w")

        remove_btn = ttk.Button(row, text="Remove", width=7, command=lambda: self.remove_item(row, text))
        remove_btn.pack(side="right")

        self.entries.append((row, text))

    def remove_item(self, row, text):
        row.destroy()
        self.entries = [e for e in self.entries if e[1] != text]

    def remove_section(self):
        self.frame.destroy()
        if self.remove_callback:
            self.remove_callback(self)

    def to_dict(self):
        return {
            "title": self.title,
            "items": [text for _, text in self.entries],
            "color": self.color
        }

class TOCApp:
    def __init__(self, root):
        self.root = root
        self.root.title("My List")

        self.sections = []

        # Header label
        header_label = ttk.Label(root, text="Welcome", font=("Helvetica", 16, "bold"))
        header_label.pack(pady=(10, 0))

        # Entry for adding sections
        self.section_entry = ttk.Entry(root)
        self.section_entry.pack(fill="x", padx=5, pady=5)
        self.section_entry.bind("<Return>", self.add_section)

        # Scrollable area
        self.canvas = tk.Canvas(root)
        self.scrollbar = ttk.Scrollbar(root, orient="vertical", command=self.canvas.yview)
        self.scrollable_frame = ttk.Frame(self.canvas)

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        )

        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.canvas.pack(side="left", fill="both", expand=True)
        self.scrollbar.pack(side="right", fill="y")

        # Load previous data
        if os.path.exists(DATA_FILE):
            with open(DATA_FILE, "r") as f:
                data = json.load(f)
                for section in data:
                    self.create_section(section["title"], section.get("items", []), section.get("color", "#000000"))

    def add_section(self, event=None):
        title = self.section_entry.get().strip()
        if title:
            self.create_section(title)
            self.section_entry.delete(0, tk.END)

    def create_section(self, title, items=None, color="#000000"):
        section = TOCSection(self.scrollable_frame, title, items, color, self.remove_section)
        self.sections.append(section)

    def remove_section(self, section):
        if section in self.sections:
            self.sections.remove(section)

    def save_data(self):
        data = [s.to_dict() for s in self.sections]
        with open(DATA_FILE, "w") as f:
            json.dump(data, f, indent=4)
        print("TOC saved to", DATA_FILE)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--save", action="store_true", help="Save current TOC state to file and exit")
    args = parser.parse_args()

    root = tk.Tk()
    app = TOCApp(root)

    if args.save:
        app.save_data()
        root.destroy()
    else:
        def on_close():
            app.save_data()
            root.destroy()

        root.protocol("WM_DELETE_WINDOW", on_close)
        root.mainloop()

if __name__ == "__main__":
    main()
