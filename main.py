
# TRESSÉ – Hair Salon Appointment Management System
# Module 6 Final Project
# Student Name: Prisca Muleka
# ============================================================

# ------------------------------------------------------------
# Step 1: Import Tkinter Libraries
# I import Tkinter so I can create a graphical user interface.
# ------------------------------------------------------------
import tkinter as tk
from tkinter import messagebox


# ------------------------------------------------------------
# Step 2: Create Simple Classes
# I use classes to represent clients and appointments.
# ------------------------------------------------------------
class Client:
    def __init__(self, name, phone):
        self.name = name.strip()
        self.phone = phone.strip()

    def __str__(self):
        return f"{self.name} ({self.phone})"


class Appointment:
    def __init__(self, client, service, date, time):
        self.client = client
        self.service = service.strip()
        self.date = date.strip()
        self.time = time.strip()

    def __str__(self):
        return f"{self.date} {self.time} | {self.client.name} - {self.service}"


# ------------------------------------------------------------
# Step 3: Create Data Collections
# I store clients and appointments in lists (simple for students).
# ------------------------------------------------------------
clients = []          # list of Client objects
appointments = []     # list of Appointment objects


# ------------------------------------------------------------
# Step 4: Create the Main Application Window
# This window is the main screen of the application.
# ------------------------------------------------------------
root = tk.Tk()
root.title("TRESSÉ - Hair Salon App")
root.geometry("700x450")
root.resizable(False, False)


# ------------------------------------------------------------
# Step 5: Add Title and Main Frames
# I use frames to organize the layout into sections.
# ------------------------------------------------------------
title_label = tk.Label(root, text="TRESSÉ Hair Salon", font=("Arial", 18, "bold"))
title_label.pack(pady=10)

content_frame = tk.Frame(root)
content_frame.pack(padx=15, pady=10, fill="both", expand=True)

left_frame = tk.LabelFrame(content_frame, text="Client & Appointment Info", padx=10, pady=10)
left_frame.grid(row=0, column=0, sticky="n")

right_frame = tk.LabelFrame(content_frame, text="Appointments", padx=10, pady=10)
right_frame.grid(row=0, column=1, padx=15, sticky="n")


# ------------------------------------------------------------
# Step 6: Create Input Fields (Client + Appointment)
# I create labels and entry boxes so the user can type information.
# ------------------------------------------------------------
# Client Name
name_label = tk.Label(left_frame, text="Client Name:")
name_label.grid(row=0, column=0, sticky="w", pady=5)
name_entry = tk.Entry(left_frame, width=25)
name_entry.grid(row=0, column=1, pady=5)

# Phone Number
phone_label = tk.Label(left_frame, text="Phone Number:")
phone_label.grid(row=1, column=0, sticky="w", pady=5)
phone_entry = tk.Entry(left_frame, width=25)
phone_entry.grid(row=1, column=1, pady=5)

# Service Dropdown
service_label = tk.Label(left_frame, text="Service:")
service_label.grid(row=2, column=0, sticky="w", pady=5)

service_var = tk.StringVar()
service_var.set("Braids")  # default
service_dropdown = tk.OptionMenu(
    left_frame,
    service_var,
    "Braids",
    "Twists",
    "Silk Press",
    "Haircut",
    "Wash & Blow Dry"
)
service_dropdown.config(width=20)
service_dropdown.grid(row=2, column=1, pady=5)

# Appointment Date
date_label = tk.Label(left_frame, text="Date (MM/DD/YYYY):")
date_label.grid(row=3, column=0, sticky="w", pady=5)
date_entry = tk.Entry(left_frame, width=25)
date_entry.grid(row=3, column=1, pady=5)

# Appointment Time
time_label = tk.Label(left_frame, text="Time (ex: 2:30 PM):")
time_label.grid(row=4, column=0, sticky="w", pady=5)
time_entry = tk.Entry(left_frame, width=25)
time_entry.grid(row=4, column=1, pady=5)


# ------------------------------------------------------------
# Step 7: Create Output Area (Listbox)
# I display scheduled appointments in a listbox on the right side.
# ------------------------------------------------------------
appt_listbox = tk.Listbox(right_frame, width=45, height=18)
appt_listbox.pack()


# ------------------------------------------------------------
# Step 8: Helper Functions
# These functions handle adding clients and scheduling appointments.
# ------------------------------------------------------------
def refresh_appointments_list():
    appt_listbox.delete(0, tk.END)
    if len(appointments) == 0:
        appt_listbox.insert(tk.END, "No appointments scheduled yet.")
    else:
        for appt in appointments:
            appt_listbox.insert(tk.END, str(appt))


def clear_fields(keep_phone=False):
    name_entry.delete(0, tk.END)
    if not keep_phone:
        phone_entry.delete(0, tk.END)
    date_entry.delete(0, tk.END)
    time_entry.delete(0, tk.END)
    service_var.set("Braids")


def add_client():
    name = name_entry.get().strip()
    phone = phone_entry.get().strip()

    if name == "" or phone == "":
        messagebox.showwarning("Missing Info", "Please enter both client name and phone number.")
        return

    # Prevent duplicate phone numbers
    for c in clients:
        if c.phone == phone:
            messagebox.showinfo("Client Exists", "A client with this phone number already exists.")
            return

    new_client = Client(name, phone)
    clients.append(new_client)
    messagebox.showinfo("Success", f"Client added: {new_client}")

    clear_fields(keep_phone=True)


def schedule_appointment():
    name = name_entry.get().strip()
    phone = phone_entry.get().strip()
    service = service_var.get().strip()
    date = date_entry.get().strip()
    time = time_entry.get().strip()

    if phone == "":
        messagebox.showwarning("Missing Info", "Please enter the client phone number.")
        return

    # Find client by phone
    client_found = None
    for c in clients:
        if c.phone == phone:
            client_found = c
            break

    if client_found is None:
        # If user typed name too, we can add them quickly
        if name == "":
            messagebox.showwarning("Client Not Found", "Client not found. Please add the client first.")
            return
        client_found = Client(name, phone)
        clients.append(client_found)

    if date == "" or time == "":
        messagebox.showwarning("Missing Info", "Please enter appointment date and time.")
        return

    new_appt = Appointment(client_found, service, date, time)
    appointments.append(new_appt)

    messagebox.showinfo("Success", "Appointment scheduled!")
    refresh_appointments_list()
    clear_fields(keep_phone=True)


def view_appointments():
    refresh_appointments_list()


# ------------------------------------------------------------
# Step 9: Create Buttons
# Buttons allow the user to run functions easily.
# ------------------------------------------------------------
add_client_btn = tk.Button(left_frame, text="Add Client", width=22, command=add_client)
add_client_btn.grid(row=5, column=0, columnspan=2, pady=(10, 5))

schedule_btn = tk.Button(left_frame, text="Schedule Appointment", width=22, command=schedule_appointment)
schedule_btn.grid(row=6, column=0, columnspan=2, pady=5)

view_btn = tk.Button(left_frame, text="View Appointments", width=22, command=view_appointments)
view_btn.grid(row=7, column=0, columnspan=2, pady=5)

clear_btn = tk.Button(left_frame, text="Clear Fields", width=22, command=clear_fields)
clear_btn.grid(row=8, column=0, columnspan=2, pady=5)


# ------------------------------------------------------------
# Step 10: Start the Application (MUST BE LAST)
# This keeps the window open and running.
# ------------------------------------------------------------
refresh_appointments_list()
root.mainloop()
