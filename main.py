import tkinter as tk
from tkinter import ttk
from tkinter import Canvas, Frame, Scrollbar
import pandas as pd

#Function to Load Threat Types Table 
def load_threat_types_table(parent_frame):
    threat_df = pd.read_csv("data/threat_types.csv")

    table = ttk.Treeview(parent_frame, columns=("Threat", "Severity"), show="headings", height=6)
    table.heading("Threat", text="Threat")
    table.heading("Severity", text="Severity")

    for _, row in threat_df.iterrows():
        severity = row["Severity"].lower()
        tag = severity if severity in ["high", "medium", "low"] else ""
        table.insert("", "end", values=(row["Threat"], row["Severity"]), tags=(tag,))

    table.tag_configure("high", background="red", foreground="white")
    table.tag_configure("medium", background="orange", foreground="black")
    table.tag_configure("low", background="yellow", foreground="black")

    table.pack(padx=5, pady=5)

#Function to Load Attacker Profiles
def load_attacker_profiles(parent_frame):
    df = pd.read_csv("data/attacker_profiles.csv")

    canvas = Canvas(parent_frame, bg="black", highlightthickness=0)
    scrollbar = Scrollbar(parent_frame, orient="vertical", command=canvas.yview)
    scrollable_frame = Frame(canvas, bg="black")

    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(
            scrollregion=canvas.bbox("all")
        )
    )

    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    for _, row in df.iterrows():
        card = tk.Frame(scrollable_frame, bg="#222", bd=1, relief="ridge", padx=10, pady=8)
        tk.Label(card, text=row["Name"], font=("Helvetica", 12, "bold"), fg="white", bg="#222").pack(anchor="w")
        tk.Label(card, text=f"Role: {row['Role']}", fg="lightgray", bg="#222").pack(anchor="w")
        tk.Label(card, text=f"Last Seen: {row['LastSeen']}", fg="lightgray", bg="#222").pack(anchor="w")
        tk.Label(card, text=row["Description"], wraplength=250, justify="left", fg="white", bg="#222").pack(anchor="w", pady=(5, 0))
        card.pack(fill="x", pady=5, padx=5)

#Function to Load CloudTrail Logs 
def load_cloudtrail_logs(tree):
    df = pd.read_csv("logs/cloudtrail_logs.csv")

    for row in tree.get_children():
        tree.delete(row)

    for _, row in df.iterrows():
        tree.insert("", "end", values=(row["Time"], row["Event"], row["User"], row["IP"], row["Status"]))

#Main App Window 
root = tk.Tk()
root.title("SIEM-SIM: Cloud Log Dashboard")
root.geometry("1300x900")
root.configure(bg="#1e1e1e")

root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(0, weight=1)

#Dashboard Frame
dashboard_frame = tk.Frame(root, bg="#1e1e1e")
dashboard_frame.grid(row=0, column=0, sticky="nsew", padx=20, pady=20)

for i in range(3):
    dashboard_frame.grid_columnconfigure(i, weight=1)
for i in range(5):
    dashboard_frame.grid_rowconfigure(i, weight=1)

#Top Metrics Bar 
top_bar = tk.LabelFrame(dashboard_frame, text="Threat Summary Metrics", bg="black", fg="white")
top_bar.grid(row=0, column=0, columnspan=3, padx=10, pady=(0, 20), sticky="nsew")

for i in range(5):
    metric = tk.Label(top_bar, text=f"Metric {i+1}", fg="white", bg="#333", width=18, height=5)
    metric.grid(row=0, column=i, padx=10, pady=10)

#Left: Filters Panel
filter_frame = tk.LabelFrame(dashboard_frame, text="Log Filters", bg="black", fg="white")
filter_frame.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

#Left Below Filters: Attacker Profiles
profile_frame = tk.LabelFrame(dashboard_frame, text="Threat Actor Profile", bg="black", fg="white")
profile_frame.grid(row=2, column=0, rowspan=2, padx=10, pady=10, sticky="nsew")
load_attacker_profiles(profile_frame)

#Center: Log Viewer 
log_frame = tk.LabelFrame(dashboard_frame, text="Log Viewer", bg="black", fg="white")
log_frame.grid(row=1, column=1, rowspan=2, padx=10, pady=10, sticky="nsew")

log_tree = ttk.Treeview(log_frame, columns=("Time", "Event", "User", "IP", "Status"), show="headings", height=12)
log_tree.pack(side=tk.LEFT, fill="both", expand=True)
load_cloudtrail_logs(log_tree)

for col in ("Time", "Event", "User", "IP", "Status"):
    log_tree.heading(col, text=col)

scrollbar = ttk.Scrollbar(log_frame, orient="vertical", command=log_tree.yview)
scrollbar.pack(side=tk.RIGHT, fill="y")
log_tree.configure(yscrollcommand=scrollbar.set)

#Right: Visual Analytics 
chart_frame = tk.LabelFrame(dashboard_frame, text="Visual Analytics", bg="black", fg="white")
chart_frame.grid(row=1, column=2, rowspan=2, padx=10, pady=(10, 5), sticky="nsew")
tk.Label(chart_frame, text="Graphs coming soon...", fg="white", bg="black").pack(pady=20)

#Row 3 Right: Threat Escalation Timeline 
timeline_frame = tk.LabelFrame(dashboard_frame, text="Threat Escalation Timeline", bg="black", fg="white")
timeline_frame.grid(row=3, column=2, padx=10, pady=(5, 10), sticky="nsew")
tk.Label(timeline_frame, text="Line graph coming soon...", fg="white", bg="black").pack(pady=10)

#Row 3 Center: Threat Severity Breakdown 
severity_frame = tk.LabelFrame(dashboard_frame, text="Threat Severity Breakdown", bg="black", fg="white")
severity_frame.grid(row=3, column=1, padx=10, pady=10, sticky="nsew")

tk.Label(severity_frame, text="HIGH (Red)", bg="red", fg="white", width=15).grid(row=0, column=0, padx=5, pady=5)
tk.Label(severity_frame, text="MEDIUM (Orange)", bg="orange", fg="black", width=15).grid(row=0, column=1, padx=5, pady=5)
tk.Label(severity_frame, text="LOW (Yellow)", bg="yellow", fg="black", width=15).grid(row=0, column=2, padx=5, pady=5)

#Row 4 Center: Threat Types Table 
threat_table_frame = tk.LabelFrame(dashboard_frame, text="Threat Types", bg="black", fg="white")
threat_table_frame.grid(row=4, column=1, padx=10, pady=10, sticky="nsew")
load_threat_types_table(threat_table_frame)

#Run App 
root.mainloop()