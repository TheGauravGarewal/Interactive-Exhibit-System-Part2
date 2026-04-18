# Interactive Exhibit System – Part 2 (Automation & Smart Control)

This is the second phase of the Interactive Exhibit System project, where the basic video playback setup from Part 1 is upgraded into a fully automated, sensor-driven exhibit suitable for real-world deployment.

---

## 🚀 What’s New in Part 2

Compared to Part 1, this version introduces:

- ✅ Dual IR sensor-based interaction
- ✅ Automatic video switching (Intro ↔ Main)
- ✅ Seamless playback using mpv (no flicker / no screen flash)
- ✅ Auto-start on system boot (no manual execution)
- ✅ Clean fullscreen display (no controls, no cursor, no UI)
- ✅ Real-time communication between Arduino and Raspberry Pi

---

## 🧠 How It Works

1. System powers ON  
2. Intro video starts automatically (loop mode)  
3. When BOTH IR sensors are triggered:
   → Main video plays  
4. If triggered again during main:
   → Returns to intro  
5. If main video finishes:
   → Intro resumes automatically  
6. System resets and waits for next interaction  

---

## 🆚 Part 1 vs Part 2

| Feature                     | Part 1 | Part 2 |
|---------------------------|--------|--------|
| Manual video playback     | ✅     | ❌     |
| Automatic startup         | ❌     | ✅     |
| Sensor-based triggering   | ❌     | ✅     |
| Smooth transitions        | ❌     | ✅     |
| Real-world deployment     | ❌     | ✅     |

---

## 🛠️ Tech Stack

- Raspberry Pi 3B+
- Arduino (for sensor input)
- Python
- mpv Media Player
- Serial Communication (USB)

---

## ⚙️ Setup Instructions

### 1. Install Dependencies

```bash
sudo apt update
sudo apt install mpv -y
pip3 install pyserial --break-system-packages
