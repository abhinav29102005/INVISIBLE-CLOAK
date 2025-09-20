# 🪄 INVISIBLE CLOAK ✨

<div align="center">

![Magic Wand](https://readme-typing-svg.herokuapp.com?font=Fira+Code&weight=600&size=28&duration=3000&pause=1000&color=FF6B35&center=true&vCenter=true&random=false&width=600&lines=✨+HHarry+Potter's+Magic+Brought+to+Life!+✨;🎭+Real-Time+Invisibility+Cloak+🎭;🔮+OpenCV+%2B+Python+%3D+Pure+Magic+🔮)

<img src="https://user-images.githubusercontent.com/74038190/212284100-561aa473-3905-4a80-b561-0d28506553ee.gif" width="700">

### *"Of course it is happening inside your head, Harry, but why on earth should that mean it is not real?"*

<img src="https://user-images.githubusercontent.com/74038190/212284087-bbe7e430-757e-4901-90bf-4cd2ce3e1852.gif" width="500">

</div>

---

## 🌟 Project Overview

<div align="center">
<img src="https://user-images.githubusercontent.com/74038190/225813708-98b745f2-7d22-48cf-9150-083f1b00d6c9.gif" width="500">
</div>

This project brings the **magical invisibility cloak** from Harry Potter to life using cutting-edge computer vision! 🎩✨ 

Transform yourself into a wizard with real-time invisibility effects powered by **Python** and **OpenCV**. The system uses advanced chroma key technology (similar to green screen) to create seamless invisibility illusions.

<div align="center">
<img src="https://user-images.githubusercontent.com/74038190/212748842-9fcbad5b-6173-4175-8a61-521f3dbb7514.gif" width="400">
</div>

---

## 🚀 Features

<div align="center">
<img src="https://user-images.githubusercontent.com/74038190/212284158-e840e285-664b-44d7-b79b-e264b5e54825.gif" width="400">
</div>

| Feature | Description |
|---------|-------------|
| 🎥 **Real-Time Processing** | Live video stream processing with zero lag |
| 🖼️ **Smart Background Capture** | Automatic background detection and replacement |
| 🎭 **Chroma Key Magic** | Advanced color-based invisibility algorithm |
| 📱 **Mobile Integration** | Works with IP webcam from your smartphone |
| 🖥️ **Full-Screen Experience** | Immersive full-screen magical experience |
| 🎮 **Interactive Controls** | Easy-to-use quit button and keyboard shortcuts |
| ⚡ **High Performance** | Optimized for smooth real-time operation |

---

## 🛠️ Tech Stack

<div align="center">
<img src="https://user-images.githubusercontent.com/74038190/212257467-871d32b7-e401-42e8-a166-fcfd7baa4c6b.gif" width="200">
</div>

<div align="center">

### Core Technologies

<img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="python" width="60" height="60"/>
<img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/opencv/opencv-original.svg" alt="opencv" width="60" height="60"/>
<img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/numpy/numpy-original.svg" alt="numpy" width="60" height="60"/>

</div>

| Technology | Purpose | Version |
|------------|---------|---------|
| ![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white) | Core Programming Language | 3.7+ |
| ![OpenCV](https://img.shields.io/badge/OpenCV-27338e?style=for-the-badge&logo=OpenCV&logoColor=white) | Computer Vision & Image Processing | 4.0+ |
| ![NumPy](https://img.shields.io/badge/Numpy-777BB4?style=for-the-badge&logo=numpy&logoColor=white) | Numerical Computing & Array Operations | Latest |

---

## 📋 Prerequisites

<div align="center">
<img src="https://user-images.githubusercontent.com/74038190/212257454-16e3712e-945a-4ca2-b238-408ad0bf87e6.gif" width="200">
</div>

### System Requirements
- **Python 3.7+** installed on your system
- **Webcam** or **IP Camera** setup
- **Red colored cloth/object** for the cloak effect
- **Stable lighting conditions** for best results

### Required Libraries

```bash
pip install opencv-python numpy
```

<div align="center">
<img src="https://user-images.githubusercontent.com/74038190/212257472-08e52665-c503-4bd9-aa20-f5a4dae769b5.gif" width="200">
</div>

---

## ⚡ Quick Start

<div align="center">
<img src="https://user-images.githubusercontent.com/74038190/212257468-1e9a91f1-b626-4baa-b15d-5c385dfa7c7a.gif" width="300">
</div>

### 1. 📱 Setup Mobile IP Webcam

<details>
<summary>📱 Android Setup</summary>

1. Install **"IP Webcam"** from Google Play Store
2. Open the app and tap **"Start Server"**
3. Note the IP address (e.g., `http://192.168.1.100:8080/video`)
4. Ensure both devices are on the **same Wi-Fi network**

</details>

<details>
<summary>🍎 iOS Setup</summary>

1. Install **"EpocCam"** or similar IP webcam app
2. Follow the app's setup instructions
3. Get the streaming URL
4. Connect to the same Wi-Fi network

</details>

### 2. 🔧 Configure the Code

```python
# Update this line in invisible_cloak.py
camera_url = "http://YOUR_PHONE_IP:8080/video"
```

### 3. 🎬 Run the Magic

```bash
python invisible_cloak.py
```

<div align="center">
<img src="https://user-images.githubusercontent.com/74038190/212257465-7ce8d493-cac5-494e-982a-5a9deb852c4b.gif" width="250">
</div>

### 4. 🎭 Become Invisible!

1. **Step out of frame** during background capture (3-5 seconds)
2. **Put on your red cloak** and step back into frame
3. **Wave your hands** and watch the magic happen! ✨
4. **Click "Quit"** or press `q` to exit

---

## 🎨 How It Works

<div align="center">
<img src="https://user-images.githubusercontent.com/74038190/212257460-738ff738-247f-4445-a718-cdd0ca76e2db.gif" width="300">
</div>

### The Magic Behind the Scenes

1. **Background Capture** 🖼️
   - System captures a clean background image
   - Stores this as reference for invisibility effect

2. **Color Detection** 🎨
   - Identifies red color range in HSV color space
   - Creates a mask for the cloak area

3. **Chroma Key Processing** 🔄
   - Replaces masked red areas with background
   - Blends the result seamlessly

4. **Real-Time Rendering** ⚡
   - Processes 30+ FPS for smooth experience
   - Updates display in real-time

<div align="center">

```mermaid
graph TB
    A[📹 Video Input] --> B[🎨 Color Detection]
    B --> C[🖼️ Background Replacement]
    C --> D[✨ Magic Output]
    E[📸 Background Capture] --> C
    
    style A fill:#ff6b6b
    style B fill:#4ecdc4
    style C fill:#45b7d1
    style D fill:#96ceb4
    style E fill:#feca57
```

</div>

---

## 🎮 Controls & Usage

<div align="center">
<img src="https://user-images.githubusercontent.com/74038190/212257463-4d082cb4-7483-4eaf-bc25-6dde2628aabd.gif" width="200">
</div>

### Keyboard Shortcuts
| Key | Action |
|-----|--------|
| `Q` | Quit Application |
| `ESC` | Emergency Exit |
| `SPACE` | Recapture Background |

### Mouse Controls
- **Click "Quit" Button** - Clean exit from application

---

## 🛠️ Troubleshooting

<div align="center">
<img src="https://user-images.githubusercontent.com/74038190/212257456-4d709462-8b95-429f-ba9c-4f05ba11b31d.gif" width="200">
</div>

<details>
<summary>🔧 Common Issues & Solutions</summary>

### Camera Connection Issues
```
❌ Error: Could not open video device
✅ Solution: 
   - Ensure IP webcam app is running
   - Check Wi-Fi connection
   - Verify IP address is correct
```

### Color Detection Problems
```
❌ Issue: Cloak not disappearing properly
✅ Solution:
   - Use bright, solid red colored cloth
   - Ensure good lighting conditions
   - Adjust HSV values in code if needed
```

### Performance Issues
```
❌ Issue: Laggy video output
✅ Solution:
   - Close other heavy applications
   - Use a solid colored background
   - Ensure stable network connection
```

</details>

---

## 🎯 Future Enhancements

<div align="center">
<img src="https://user-images.githubusercontent.com/74038190/212257461-58e91aed-f2a4-4816-92a7-1ebf1b5d76b0.gif" width="200">
</div>

- [ ] 🌈 Multiple color cloak support
- [ ] 🤖 AI-powered edge detection
- [ ] 📱 Mobile app version
- [ ] 🎨 Custom background selection
- [ ] 🎵 Sound effects integration
- [ ] 🎭 Multiple person support
- [ ] 📊 Performance analytics

---

## 🤝 Contributing

<div align="center">
<img src="https://user-images.githubusercontent.com/74038190/212257455-05ff3cc9-b988-48c6-9ba7-bb40c3fd0f7c.gif" width="250">
</div>

We welcome contributions! Here's how you can help:

1. 🍴 **Fork** the repository
2. 🌿 **Create** your feature branch (`git checkout -b feature/AmazingFeature`)
3. 💾 **Commit** your changes (`git commit -m 'Add some AmazingFeature'`)
4. 📤 **Push** to the branch (`git push origin feature/AmazingFeature`)
5. 🔀 **Open** a Pull Request

---

## 📄 License

<div align="center">
<img src="https://user-images.githubusercontent.com/74038190/212257459-bc9c0d84-5245-4b5e-8f4a-7b6e54f6a8eb.gif" width="150">
</div>

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

---

## 🌟 Show Your Support

<div align="center">

If you found this project helpful, please consider:

[![Stars](https://img.shields.io/github/stars/abhinav29102005/INVISIBLE-CLOAK?style=social)](https://github.com/abhinav29102005/INVISIBLE-CLOAK/stargazers)
[![Forks](https://img.shields.io/github/forks/abhinav29102005/INVISIBLE-CLOAK?style=social)](https://github.com/abhinav29102005/INVISIBLE-CLOAK/network/members)
[![Issues](https://img.shields.io/github/issues/abhinav29102005/INVISIBLE-CLOAK)](https://github.com/abhinav29102005/INVISIBLE-CLOAK/issues)

<img src="https://user-images.githubusercontent.com/74038190/212284115-f47cd8ff-2ffb-4b04-b5bf-4d1c14c0247f.gif" width="200">

**Give it a ⭐ if you liked this project!**

</div>

---

## 👨‍💻 Connect With Me

<div align="center">

<img src="https://user-images.githubusercontent.com/74038190/212257454-16e3712e-945a-4ca2-b238-408ad0bf87e6.gif" width="100">

### Abhinav Singh

*Computer Vision Enthusiast | Python Developer | Magic Creator*

<div align="center">

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://linkedin.com/in/bigboyaks)
[![Gmail](https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:asingh3_be24@thapar.edu)
[![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/abhinav29102005)

</div>

<img src="https://user-images.githubusercontent.com/74038190/212284100-561aa473-3905-4a80-b561-0d28506553ee.gif" width="300">

### *"Magic is not about having special powers, it's about making the impossible seem possible through technology!"* ✨

</div>

---

<div align="center">
<img src="https://user-images.githubusercontent.com/74038190/212284087-bbe7e430-757e-4901-90bf-4cd2ce3e1852.gif" width="400">

**Made with ❤️ and a touch of magic**

![Visitor Count](https://profile-counter.glitch.me/INVISIBLE-CLOAK/count.svg)

</div>
