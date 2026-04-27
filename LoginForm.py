import tkinter as tk
from tkinter import messagebox
import pyotp
import qrcode
from PIL import Image, ImageTk

def create_qr_code():
    # Generate the URI needed by Google Authenticator
    uri = pyotp.totp.TOTP(secret).provisioning_uri(name='user@example.com', issuer_name='SecureApp')
    qr = qrcode.make(uri)
    # Convert QR code to a PIL image
    qr_pil = qr.get_image().convert('RGB')
    qr_pil.save("temp_qr.png")  # Save temporarily to ensure proper handling
    qr_image = ImageTk.PhotoImage(file="temp_qr.png")
    
    qr_label.pack()

def verify_otp():
    entered_otp = otp_entry.get()
    totp = pyotp.TOTP(secret)
    if totp.verify(entered_otp):
        messagebox.showinfo("Login Success", "The OTP is correct. Login successful!")
    else:
        messagebox.showerror("Login Failed", "Invalid OTP. Please try again!")

# Generate a random base32 secret for OTP. In a real application, this should be unique per user and stored securely.
secret = pyotp.random_base32()

# Setup the main window
root = tk.Tk()
root.title("2FA Login Form with Google Authenticator")

# Label and image for the QR Code
qr_label = tk.Label(root)
qr_label.pack()

# Button to generate and display QR Code
qr_button = tk.Button(root, text="Generate QR Code", command=create_qr_code)
qr_button.pack()

# Instructions label
instruction_label = tk.Label(root, text="Scan the QR code with Google Authenticator and enter the OTP below:")
instruction_label.pack()

# Label and entry for the OTP
otp_label = tk.Label(root, text="Enter OTP:")
otp_label.pack()

otp_entry = tk.Entry(root)
otp_entry.pack()

# Button to verify the OTP
verify_button = tk.Button(root, text="Verify OTP", command=verify_otp)
verify_button.pack()

# Running the application
root.mainloop()
