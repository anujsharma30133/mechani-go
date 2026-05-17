# 🛵 MechaniGo

MechaniGo is a doorstep vehicle repair and service platform built using Streamlit. We connect bike and scooty owners with verified mechanics instantly, bringing professional vehicle service directly to your location.

## 🌟 Features

- 🎨 Beautiful dark UI with modern design
- 📱 Mobile responsive design
- 🔧 Mechanic booking form with validation
- 💼 Comprehensive services section
- ℹ️ About project section
- 📧 Contact form
- 🟠 Modern orange accent theme
- ✨ Smooth animations and transitions
- 🌙 Dark mode by default

---

## 📋 Project Overview

### Problem Statement
Vehicle owners in India face major problems during breakdown situations. Finding trusted mechanics, transparent pricing, and emergency support is extremely difficult, especially in Tier 2 and Tier 3 cities.

### Solution
MechaniGo is an on-demand doorstep mechanic platform that connects users with verified nearby mechanics using a smart digital platform.

### Target Users
- College Students
- Working Professionals
- Women Riders
- Families
- Tier 2 & Tier 3 City Residents

---

## 🚀 Services Offered

| Service | Price |
|---------|-------|
| 🛞 Puncture Repair | ₹149 |
| 🔋 Battery Replacement | ₹599 |
| 🛢 Oil Change | ₹399 |
| ⚙️ Engine Check | ₹499 |
| 🚿 General Servicing | ₹799 |
| 🧰 Emergency Breakdown | ₹999 |

---

## 📊 Platform Stats

- **10K+** Active Users
- **2K+** Verified Mechanics
- **25+** Cities Covered
- **24/7** Customer Support

---

## 🛠 Tech Stack

- **Frontend**: Streamlit
- **Language**: Python
- **Styling**: Custom CSS
- **Fonts**: Poppins (Google Fonts)

---

## 📦 Installation

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Install Requirements

```bash
pip install -r requirements.txt
```

### Required Packages

```
streamlit==1.28.1
python-dateutil==2.8.2
```

---

## 🚀 Run Locally

### 1. Clone the Repository

```bash
git clone https://github.com/anujsharma30133/mechani-go.git
cd mechani-go
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the Application

```bash
streamlit run app.py
```

The application will open in your default browser at `http://localhost:8501`

---

## 📁 Project Structure

```
mechani-go/
│
├── app.py                 # Main Streamlit application
├── requirements.txt       # Python dependencies
├── README.md             # Project documentation
└── .gitignore           # Git ignore file
```

---

## 🎯 How MechaniGo Works

### Step 1: 📱 Book Service
Select your vehicle issue and book a nearby mechanic with just a few clicks.

### Step 2: 📍 Track Mechanic
Real-time tracking lets you see exactly when your mechanic will arrive at your location.

### Step 3: ✅ Repair Complete
Get your vehicle repaired safely with transparent pricing and digital payment options.

---

## 📝 Usage Guide

### Book a Mechanic

1. Navigate to "Book Mechanic" page
2. Fill in your details:
   - Full Name
   - Phone Number (10 digits)
   - City
   - Vehicle Type (Bike/Scooty/Car)
   - Service Type
   - Location Description
3. Click "Book Now"
4. You'll receive a booking confirmation with all details

### View Services

- Visit the "Our Services" page to see all available services and pricing
- Services are available 24/7

### Contact Us

- Fill the contact form on the "Contact" page
- We'll respond to your inquiry as soon as possible

---

## 🎨 Customization

### Colors
The main colors used in the application:
- **Primary Orange**: `#E8570A`
- **Primary Dark**: `#ff6b1a`
- **Background Dark**: `#0F1117`
- **Background Darker**: `#151821`
- **Border Color**: `#2A2D36`

### Fonts
- Font Family: **Poppins** (Google Fonts)
- Weights: 300, 400, 500, 600, 700

To customize, modify the CSS in `app.py`:
```python
st.markdown("""
<style>
/* Your custom CSS here */
</style>
""", unsafe_allow_html=True)
```

---

## 🔐 Form Validation

### Booking Form
- ✅ All fields required
- ✅ Phone number must be exactly 10 digits
- ✅ Location must not be empty

### Contact Form
- ✅ All fields required
- ✅ Email must contain "@" symbol
- ✅ Message must not be empty

---

## 📱 Responsive Design

The application is fully responsive and works on:
- 💻 Desktop (1200px+)
- 📱 Tablet (768px - 1199px)
- 📲 Mobile (< 768px)

---

## 🌐 Deployment

### Deploy on Streamlit Cloud

1. Push your code to GitHub
2. Go to [Streamlit Cloud](https://streamlit.io/cloud)
3. Click "New app"
4. Select your repository and branch
5. Choose `app.py` as the main file
6. Click "Deploy"

### Deploy on Heroku

```bash
heroku create your-app-name
git push heroku main
heroku open
```

### Deploy on AWS

Use AWS Elastic Beanstalk or EC2 with proper Streamlit configuration.

---

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

---

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

---

## 👥 Team

- **Founder/Developer**: Anuj Sharma (@anujsharma30133)

---

## 📞 Support

For support, email us at support@mechani-go.com or open an issue on GitHub.

---

## 🚀 Future Enhancements

- [ ] Real-time mechanic tracking with Google Maps API
- [ ] Payment gateway integration
- [ ] User authentication and profiles
- [ ] Mechanic ratings and reviews
- [ ] Service history tracking
- [ ] SMS/Email notifications
- [ ] Mobile app (iOS & Android)
- [ ] Multi-language support
- [ ] Emergency SOS feature
- [ ] Insurance integration

---

## 📊 Statistics

- Lines of Code: ~300+
- Features: 5+ main sections
- Supported Vehicles: 3 types
- Services: 6 categories
- Cities: 25+

---

## 🔗 Links

- **GitHub**: [MechaniGo Repository](https://github.com/anujsharma30133/mechani-go)
- **Live Demo**: Coming Soon
- **Website**: [mechani-go.com](https://mechani-go.com) (Coming Soon)

---

## ⭐ Show Your Support

If you find this project helpful, please consider giving it a ⭐ on GitHub!

---

## 📝 Changelog

### Version 1.0.0 (2026-05-17)
- Initial release
- Core features implemented
- Dark theme UI
- Form validation
- Mobile responsive design

---

## 🙏 Acknowledgments

- [Streamlit](https://streamlit.io/) - For the amazing framework
- [Google Fonts](https://fonts.google.com/) - For Poppins font
- [Unsplash](https://unsplash.com/) - For quality images

---

**Made with ❤️ by Anuj Sharma**

© 2026 MechaniGo — Your Mechanic. Your Doorstep. Anytime. Anywhere.
