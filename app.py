import streamlit as st
from datetime import datetime

# =========================
# PAGE CONFIG
# =========================
st.set_page_config(
    page_title="MechaniGo",
    page_icon="🛵",
    layout="wide"
)

# =========================
# CUSTOM CSS
# =========================
st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap');

html, body, [class*="css"] {
    font-family: 'Poppins', sans-serif;
    background-color: #0F1117;
    color: white;
}

/* Main background */
.stApp {
    background-color: #0F1117;
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background-color: #151821;
    border-right: 1px solid #2A2D36;
}

/* Titles */
.main-title {
    font-size: 3rem;
    font-weight: 700;
    color: #E8570A;
    margin-bottom: 10px;
}

.sub-title {
    font-size: 1.2rem;
    color: #CCCCCC;
    margin-bottom: 30px;
}

/* Cards */
.card {
    background: #1A1D29;
    padding: 25px;
    border-radius: 18px;
    border: 1px solid #2A2D36;
    margin-bottom: 20px;
    transition: 0.3s;
}

.card:hover {
    border: 1px solid #E8570A;
    transform: translateY(-5px);
}

/* Stats */
.stat-card {
    background: linear-gradient(135deg, #E8570A, #ff7b2c);
    padding: 20px;
    border-radius: 16px;
    text-align: center;
    color: white;
    font-weight: 600;
}

/* Buttons */
.stButton>button {
    background-color: #E8570A;
    color: white;
    border-radius: 10px;
    border: none;
    padding: 10px 20px;
    font-weight: 600;
}

.stButton>button:hover {
    background-color: #ff6b1a;
    color: white;
}

/* Inputs */
.stTextInput input,
.stTextArea textarea,
.stSelectbox div {
    background-color: #1A1D29 !important;
    color: white !important;
    border-radius: 10px !important;
}

/* Footer */
.footer {
    text-align: center;
    padding: 20px;
    color: #999999;
    font-size: 14px;
}

</style>
""", unsafe_allow_html=True)

# =========================
# SIDEBAR
# =========================
st.sidebar.title("🛵 MechaniGo")

page = st.sidebar.radio(
    "Navigate",
    [
        "Home",
        "Book Mechanic",
        "Our Services",
        "About Project",
        "Contact"
    ]
)

# =========================
# HOME PAGE
# =========================
if page == "Home":

    st.markdown("""
    <div class="main-title">
        MechaniGo
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="sub-title">
        Your Mechanic. Your Doorstep. Anytime. Anywhere.
    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns([1.5, 1])

    with col1:
        st.markdown("""
        <div class="card">
        <h3 style='color:#E8570A;'>🚀 India's Smart Doorstep Mechanic Platform</h3>
        <p>
        MechaniGo helps bike and scooty owners find verified mechanics instantly.
        No more pushing vehicles to repair shops.
        Get fast, safe and transparent vehicle service directly at your location.
        </p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.image(
            "https://images.unsplash.com/photo-1517524008697-84bbe3c3fd98?q=80&w=1200&auto=format&fit=crop",
            use_container_width=True
        )

    st.markdown("## 📊 Platform Stats")

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.markdown("""
        <div class="stat-card">
        <h2>10K+</h2>
        Users
        </div>
        """, unsafe_allow_html=True)

    with c2:
        st.markdown("""
        <div class="stat-card">
        <h2>2K+</h2>
        Mechanics
        </div>
        """, unsafe_allow_html=True)

    with c3:
        st.markdown("""
        <div class="stat-card">
        <h2>25+</h2>
        Cities
        </div>
        """, unsafe_allow_html=True)

    with c4:
        st.markdown("""
        <div class="stat-card">
        <h2>24/7</h2>
        Support
        </div>
        """, unsafe_allow_html=True)

    st.markdown("## ⚙️ How MechaniGo Works")

    h1, h2, h3 = st.columns(3)

    with h1:
        st.markdown("""
        <div class="card">
        <h4 style='color:#E8570A;'>1️⃣ Book Service</h4>
        <p>Select vehicle issue and book nearby mechanic.</p>
        </div>
        """, unsafe_allow_html=True)

    with h2:
        st.markdown("""
        <div class="card">
        <h4 style='color:#E8570A;'>2️⃣ Track Mechanic</h4>
        <p>Track mechanic live until arrival at your location.</p>
        </div>
        """, unsafe_allow_html=True)

    with h3:
        st.markdown("""
        <div class="card">
        <h4 style='color:#E8570A;'>3️⃣ Repair Complete</h4>
        <p>Get repair completed safely with digital payment.</p>
        </div>
        """, unsafe_allow_html=True)

# =========================
# BOOK MECHANIC
# =========================
elif page == "Book Mechanic":

    st.markdown("""
    <div class="main-title">
        Book a Mechanic
    </div>
    """, unsafe_allow_html=True)

    with st.form("booking_form"):

        name = st.text_input("Full Name")
        phone = st.text_input("Phone Number")
        city = st.text_input("City")

        vehicle = st.selectbox(
            "Vehicle Type",
            ["Bike", "Scooty", "Car"]
        )

        service = st.selectbox(
            "Select Service",
            [
                "Puncture Repair",
                "Battery Replacement",
                "Oil Change",
                "Engine Check",
                "General Service"
            ]
        )

        location = st.text_area("Enter Your Location")

        submit = st.form_submit_button("Book Now")

        if submit:

            if not name or not phone or not city or not location:
                st.error("⚠️ Please fill all fields.")

            elif len(phone) != 10 or not phone.isdigit():
                st.error("⚠️ Enter valid 10 digit mobile number.")

            else:
                booking_time = datetime.now().strftime("%d-%m-%Y %H:%M")

                st.success("✅ Mechanic booked successfully!")

                st.markdown(f"""
                <div class="card">
                <h4 style='color:#E8570A;'>Booking Details</h4>

                <p><b>Name:</b> {name}</p>
                <p><b>Phone:</b> {phone}</p>
                <p><b>City:</b> {city}</p>
                <p><b>Vehicle:</b> {vehicle}</p>
                <p><b>Service:</b> {service}</p>
                <p><b>Location:</b> {location}</p>
                <p><b>Booking Time:</b> {booking_time}</p>

                </div>
                """, unsafe_allow_html=True)

# =========================
# SERVICES PAGE
# =========================
elif page == "Our Services":

    st.markdown("""
    <div class="main-title">
        Our Services
    </div>
    """, unsafe_allow_html=True)

    services = [
        ("🛞 Puncture Repair", "₹149"),
        ("🔋 Battery Replacement", "₹599"),
        ("🛢 Oil Change", "₹399"),
        ("⚙️ Engine Check", "₹499"),
        ("🚿 General Servicing", "₹799"),
        ("🧰 Emergency Breakdown", "₹999")
    ]

    col1, col2 = st.columns(2)

    for index, service in enumerate(services):

        title, price = service

        card_html = f"""
        <div class="card">
            <h3 style='color:#E8570A;'>{title}</h3>
            <h2>{price}</h2>
            <p>Fast doorstep vehicle service by verified mechanics.</p>
        </div>
        """

        if index % 2 == 0:
            col1.markdown(card_html, unsafe_allow_html=True)
        else:
            col2.markdown(card_html, unsafe_allow_html=True)

# =========================
# ABOUT PAGE
# =========================
elif page == "About Project":

    st.markdown("""
    <div class="main-title">
        About MechaniGo
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="card">
    <h3 style='color:#E8570A;'>📌 Problem Statement</h3>
    <p>
    Vehicle owners in India face major problems during breakdown situations.
    Finding trusted mechanics, transparent pricing and emergency support
    is extremely difficult especially in Tier 2 and Tier 3 cities.
    </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="card">
    <h3 style='color:#E8570A;'>💡 Solution</h3>
    <p>
    MechaniGo is an on-demand doorstep mechanic platform that connects
    users with verified nearby mechanics using a smart digital platform.
    </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="card">
    <h3 style='color:#E8570A;'>🎯 Target Users</h3>
    <ul>
        <li>College Students</li>
        <li>Working Professionals</li>
        <li>Women Riders</li>
        <li>Families</li>
        <li>Tier 2 & Tier 3 City Residents</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)

# =========================
# CONTACT PAGE
# =========================
elif page == "Contact":

    st.markdown("""
    <div class="main-title">
        Contact Us
    </div>
    """, unsafe_allow_html=True)

    with st.form("contact_form"):

        cname = st.text_input("Your Name")
        cemail = st.text_input("Email Address")
        cmessage = st.text_area("Your Message")

        csubmit = st.form_submit_button("Send Message")

        if csubmit:

            if not cname or not cemail or not cmessage:
                st.error("⚠️ Please fill all fields.")

            elif "@" not in cemail:
                st.error("⚠️ Enter valid email.")

            else:
                st.success("✅ Message sent successfully!")

# =========================
# FOOTER
# =========================
st.markdown("""
<div class="footer">
© 2026 MechaniGo — Built with Streamlit
</div>
""", unsafe_allow_html=True)
