import tkinter as tk
from tkinter import filedialog, messagebox
import subprocess
import os

class VPNUploaderGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("OpenVPN Connector")
        self.root.geometry("450x300")
        self.root.resizable(False, False)
        self.root.configure(bg="#2b2b2b")

        header_frame = tk.Frame(root, bg="#3c3c3c", pady=10)
        header_frame.pack(fill=tk.X)

        header_label = tk.Label(header_frame, text="OpenVPN Configuration", fg="#ffffff", bg="#3c3c3c",
                                font=("Segoe UI", 16, "bold"))
        header_label.pack()

        content_frame = tk.Frame(root, bg="#2b2b2b", pady=20)
        content_frame.pack(expand=True)

        self.label = tk.Label(content_frame, text="Select your .ovpn configuration file:", fg="#e0e0e0", bg="#2b2b2b",
                              font=("Segoe UI", 11))
        self.label.pack(pady=10)

        file_display_frame = tk.Frame(content_frame, bg="#3c3c3c", bd=1, relief="solid", padx=10, pady=8)
        file_display_frame.pack(fill=tk.X, padx=50, pady=5)

        self.file_label = tk.Label(file_display_frame, text="No file selected", fg="#808080", bg="#3c3c3c",
                                    font=("Segoe UI", 10, "italic"))
        self.file_label.pack(fill=tk.X)

        button_frame = tk.Frame(content_frame, bg="#2b2b2b", pady=15)
        button_frame.pack()

        self.browse_button = tk.Button(button_frame, text="Browse File", command=self.browse_file,
                                       bg="#007acc", fg="white", font=("Segoe UI", 10, "bold"),
                                       width=15, relief="flat", activebackground="#005a9e", activeforeground="white")
        self.browse_button.grid(row=0, column=0, padx=10)

        self.connect_button = tk.Button(button_frame, text="Connect VPN", command=self.connect_vpn,
                                        bg="#28a745", fg="white", font=("Segoe UI", 10, "bold"),
                                        width=15, relief="flat", activebackground="#218838", activeforeground="white")
        self.connect_button.grid(row=0, column=1, padx=10)

        self.file_path = None

    def browse_file(self):
        file = filedialog.askopenfilename(filetypes=[("OpenVPN files", "*.ovpn"), ("All files", "*.*")])
        if file:
            self.file_path = file
            self.file_label.config(text=os.path.basename(file), fg="#90ee90")
        else:
            self.file_label.config(text="No file selected", fg="#808080")

    def connect_vpn(self):
        if not self.file_path:
            messagebox.showerror("Error", "Please select an .ovpn file first.", parent=self.root)
            return
        
        try:
            subprocess.Popen(["openvpn", "--config", self.file_path], 
                             stdout=subprocess.DEVNULL,
                             stderr=subprocess.DEVNULL)
            messagebox.showinfo("VPN Connection", "Attempting to connect to VPN...", parent=self.root)
        except FileNotFoundError:
            messagebox.showerror("Error", "OpenVPN executable not found. Please ensure OpenVPN is installed and accessible in your system's PATH.", parent=self.root)
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}", parent=self.root)

if __name__ == "__main__":
    root = tk.Tk()
    app = VPNUploaderGUI(root)
    root.mainloop()