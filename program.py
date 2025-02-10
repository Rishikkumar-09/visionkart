from tkinter import messagebox, ttk, Toplevel, Entry
import cv2
from PIL import Image, ImageTk
from fpdf import FPDF
from ttkthemes import ThemedTk
import numpy as np
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders


SENDER_EMAIL = "visionkart@gmail.com"  # Replace with your Gmail address
SENDER_PASSWORD = "tazj juiq dukn kasd"  # Replace with your Gmail password (or App Password if 2FA enabled)


# Initialize face detector and global variables
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)
cart_items = []  # List to store cart items
current_filter_index = 0
height_offset = 0  # Adjustable height for glasses

# List of filter images, names, and prices
filter_paths = [
    r"C:\Picart-Sunglasses-PNG-Picture.png",#replace with u r image path
    r"C:\Pictures\over.png",
    r"C:\Pictures\pilot.png",
    r"C:\Pictures\cat.png",
    r"C\Pictures\gold sun glasses.png",
    r"C:\Pictures\brownline.png",
    r"C:\\oval-removebg-preview.png",
]
filter_names = ["1 Sunglasses", "2 Oversized frames", "3 Pilot frames", "4 Cat frames",
                "5 Gold Sunglasses", "6 Brownline frames", "7 Oval frames"]
filter_prices = [100, 90, 30, 150, 200, 80, 70]  # Prices corresponding to the filters

# Load all filters into a list
filters = []
for path in filter_paths:
    try:
        filters.append(Image.open(path))
    except Exception as e:
        print(f"Error loading filter {path}: {e}")
current_filter = filters[current_filter_index]

# Initialize Tkinter with a themed window
root = ThemedTk(theme="arc")
root.title("Virtual Lens Frame Try-On System")
root.geometry("1200x800")
root.resizable(True, True)

font_style = ("Helvetica", 12)

# Labels and buttons for the UI
filter_label = ttk.Label(root,
                         text=f"Filter: {filter_names[current_filter_index]} | Price: ${filter_prices[current_filter_index]}",
                         font=("Arial", 16))
filter_label.grid(row=0, column=0, padx=10, pady=10, columnspan=3)

video_label = ttk.Label(root)
video_label.grid(row=1, column=0, columnspan=3, pady=10)

cart_frame = ttk.Frame(root, borderwidth=2, relief="solid")
cart_frame.grid(row=1, column=3, padx=10, pady=10, rowspan=3, sticky="ns")
cart_label = ttk.Label(cart_frame, text="Cart Items", font=("Arial", 16))
cart_label.pack(pady=5)

cart_tree = ttk.Treeview(cart_frame, columns=("Name", "Price"), show="headings", height=20)
cart_tree.heading("Name", text="Name")
cart_tree.heading("Price", text="Price")
cart_tree.column("Name", width=150)
cart_tree.column("Price", width=100)
cart_tree.pack(pady=10)


# Update cart display
def update_cart_display():
    for row in cart_tree.get_children():
        cart_tree.delete(row)
    for item in cart_items:
        cart_tree.insert("", "end", values=(item["name"], f"${item['price']}"))


# Add to cart functionality
def add_to_cart():
    global current_filter_index, cart_items
    selected_filter = {
        "name": filter_names[current_filter_index],
        "price": filter_prices[current_filter_index]
    }
    cart_items.append(selected_filter)
    update_cart_display()
    messagebox.showinfo("Cart", f"{selected_filter['name']} added to the cart!")


btn_add_to_cart = ttk.Button(root, text="Add to Cart", command=add_to_cart, width=20)
btn_add_to_cart.grid(row=3, column=0, padx=10, pady=10, columnspan=3)


# Switch filters
def switch_filter(direction):
    global current_filter_index, current_filter
    current_filter_index = (current_filter_index + direction) % len(filters)
    current_filter = filters[current_filter_index]
    filter_label.config(
        text=f"Filter: {filter_names[current_filter_index]} | Price: ${filter_prices[current_filter_index]}")

btn_prev_filter = ttk.Button(root, text="<< Previous Filter", command=lambda: switch_filter(-1), width=20)
btn_prev_filter.grid(row=4, column=0, padx=10, pady=10)

btn_next_filter = ttk.Button(root, text="Next Filter >>", command=lambda: switch_filter(1), width=20)
btn_next_filter.grid(row=4, column=2, padx=10, pady=10)


# Generate invoice function provided by you
def generate_invoice(customer_details, cart_items, shop_logo=None, offer_image=None, offerxn_image=None):
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    # Add Shop Logo
    if shop_logo:
        pdf.image(shop_logo, x=10, y=10, w=50)  # Adjust size and position

    # Shop Details
    pdf.set_xy(10, 60)
    pdf.set_font("Arial", "B", size=16)
    pdf.cell(0, 10, "Visionkart", ln=True, align="C")
    pdf.set_font("Arial", size=12)
    pdf.cell(0, 10, "123 Main Street, City, State, ZIP Code", ln=True, align="C")
    pdf.cell(0, 10, "Phone: +1 234-567-890 | Email: shop@example.com", ln=True, align="C")

    # Customer Details
    pdf.ln(15)
    pdf.set_font("Arial", "B", size=12)
    pdf.cell(0, 10, "Customer Details:", ln=True)
    pdf.set_font("Arial", size=12)
    pdf.cell(0, 10, f"Name: {customer_details.get('name', 'N/A')}", ln=True)
    pdf.cell(0, 10, f"Mobile: {customer_details.get('mobile', 'N/A')}", ln=True)
    pdf.cell(0, 10, f"Email: {customer_details.get('email', 'N/A')}", ln=True)

    # Invoice Header
    pdf.ln(15)
    pdf.set_font("Arial", "B", size=12)
    pdf.cell(60, 10, "Product Name", 1, align="C")
    pdf.cell(60, 10, "Price", 1, align="C")
    pdf.ln(10)

    # Cart Items
    total_amount = 0
    pdf.set_font("Arial", size=12)
    for item in cart_items:
        pdf.cell(60, 10, item['name'], 1)
        pdf.cell(60, 10, f"${item['price']:.2f}", 1, align="C")
        pdf.ln(10)
        total_amount += item['price']

    # Total Amount
    pdf.set_font("Arial", "B", size=12)
    pdf.cell(60, 10, "Total", 1)
    pdf.cell(60, 10, f"${total_amount:.2f}", 1, align="C")

    # Offer Images
    pdf.ln(20)
    if offer_image:
        pdf.image(offer_image, x=20, y=pdf.get_y(), w=50)  # Left-aligned offer image
    if offerxn_image:
        pdf.image(offerxn_image, x=140, y=pdf.get_y(), w=50)  # Right-aligned offer image

    # Save PDF
    pdf.output("invoice.pdf")
    messagebox.showinfo("Success", "Invoice generated and saved as 'invoice.pdf'.")



# Popup window for customer details
def open_customer_details_popup(customer_details=None):
    popup = Toplevel(root)
    popup.title("Customer Details")
    popup.geometry("300x200")

    ttk.Label(popup, text="Customer Name:").grid(row=0, column=0, padx=10, pady=10)
    name_entry = Entry(popup)
    name_entry.grid(row=0, column=1, padx=10, pady=10)

    ttk.Label(popup, text="Mobile:").grid(row=1, column=0, padx=10, pady=10)
    mobile_entry = Entry(popup)
    mobile_entry.grid(row=1, column=1, padx=10, pady=10)

    ttk.Label(popup, text="Email:").grid(row=2, column=0, padx=10, pady=10)
    email_entry = Entry(popup)
    email_entry.grid(row=2, column=1, padx=10, pady=10)

    def send_email(to_email, invoice_path):
        try:
            # Set up the email
            msg = MIMEMultipart()
            msg['From'] = SENDER_EMAIL
            msg['To'] = to_email
            msg['Subject'] = "Your Invoice from Visionkart"
            body = "Please find your invoice attached. Thank you for shopping with Visionkart!"
            msg.attach(MIMEText(body, 'plain'))

            # Attach the PDF
            with open(invoice_path, "rb") as attachment:
                part = MIMEBase('application', 'octet-stream')
                part.set_payload(attachment.read())
                encoders.encode_base64(part)
                part.add_header('Content-Disposition', f'attachment; filename={invoice_path}')
                msg.attach(part)

            # Connect to Gmail SMTP server
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(SENDER_EMAIL, SENDER_PASSWORD)
            server.send_message(msg)
            server.quit()

            messagebox.showinfo("Success", "Invoice sent successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to send email: {e}")
##
    def submit_customer_details(invoice_path="invoice.pdf"):
        customer_details = {
            "name": name_entry.get(),
            "mobile": mobile_entry.get(),
            "email": email_entry.get()
        }
        if customer_details["name"] and customer_details["mobile"] and customer_details["email"]:
            popup.destroy()

            generate_invoice(customer_details, cart_items,
                             shop_logo=r"C\20-removebg-preview.png", # Path to your logo
            offer_image=r"CPictures\offer.png",
                             offerxn_image=r"\—Pngtree—buy 1 get free offer_9443261.png")
            send_email(customer_details["email"], invoice_path)
            # Notify the user that the invoice was generated successfully
        else:
            messagebox.showerror("Error", "Please fill in all customer details!")

    submit_btn = ttk.Button(popup, text="Submit", command=submit_customer_details)
    submit_btn.grid(row=3, column=0, columnspan=2, pady=20)
##
# Button to trigger the customer details popup and generate invoice
btn_generate_invoice = ttk.Button(root, text="Generate Invoice", command=open_customer_details_popup, width=20)
btn_generate_invoice.grid(row=5, column=0, padx=10, pady=10, columnspan=3)


def overlay_filter(x, y, w, h):
    global height_offset
    filter_resized = current_filter.resize((w, int(h / 2)))  # Resize to fit face width, and half the face height
    filter_array = cv2.cvtColor(np.array(filter_resized), cv2.COLOR_RGBA2BGRA)

    # Adjust position of the glasses using height_offset
    filter_y = y + int(h / 4) + height_offset  # Slightly above the center of the face height
    filter_x = x

    # Overlay the filter on the face
    for i in range(filter_array.shape[0]):
        for j in range(filter_array.shape[1]):
            if filter_array[i, j, 3] > 0:  # Apply only non-transparent pixels
                if 0 <= filter_y + i < frame.shape[0] and 0 <= filter_x + j < frame.shape[1]:  # Boundary check
                    frame[filter_y + i, filter_x + j] = filter_array[i, j, :3]
    return frame

# Height adjustment slider
def update_height_offset(val):
    global height_offset
    height_offset = int(val)

height_slider = ttk.Scale(root, from_=-50, to=50, orient="horizontal", command=update_height_offset)
height_slider.set(0)  # Set default offset to 0
height_slider_label = ttk.Label(root, text="Adjust Glasses Height", font=("Arial", 12))
height_slider_label.grid(row=6, column=0, padx=10, pady=10, columnspan=3)
height_slider.grid(row=7, column=0, padx=10, pady=10, columnspan=3)

# Live video feed
def video_loop():
    global frame
    ret, frame = cap.read()
    if ret:
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(100, 100))

        for (x, y, w, h) in faces:
            frame = overlay_filter(x, y, w, h)

        frame_pil = Image.fromarray(frame)
        frame_tk = ImageTk.PhotoImage(frame_pil)
        video_label.config(image=frame_tk)
        video_label.image = frame_tk

    root.after(10, video_loop)

root.after(10, video_loop)

root.mainloop()
