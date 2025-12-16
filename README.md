# MeloLab 🎵

💡 **Compose the perfect melody in just a few clicks**  

MeloLab is a lightweight, algorithm-based melody generator designed for musicians who want creative inspiration without losing control. Unlike many AI music tools, MeloLab **doesn’t replace your creativity** — it helps you explore melodic ideas while you stay in the driver’s seat.  

It uses a **Markov chain algorithm** to generate melodies from user-selected MIDI rhythms and “flavors” (musical sequences) — fast, flexible, and computationally light.

LinkedIn Article: https://www.linkedin.com/pulse/what-composing-perfect-melody-just-click-away-balamurali-balu-jg5uc

---

## Features

- **Endless Variations:** Generate infinite melodies from the same rhythm and flavor.  
- **Rhythm-Pitch Flexibility:** Rhythm and pitch are separate, allowing full experimentation.  
- **Lightweight & Efficient:** No GPU-heavy AI models required.  
- **Creative Augmentation:** Inspires ideas without replacing the composer.  
- **Cost-Effective:** Runs locally; no expensive subscriptions needed.  

---

## How It Works
<img width="600" height="642" alt="image" src="https://github.com/user-attachments/assets/6419b7f1-a93b-4ccb-8fd6-045c13c4bb5e" />

1. **Select a Rhythm MIDI File**  
   - Create a rhythm pattern in your DAW and export it as MIDI.  
   - MeloLab reads only timing and duration; pitch is generated separately.  

2. **Enter BPM**  
   - Set your desired tempo.  

3. **Choose a Flavor**  
   - Flavors are predefined sequences of notes (from songs or scales).  
   - MeloLab analyzes note transitions to guide melody generation.  

4. **Generate Melody**  
   - MeloLab uses a Markov chain to produce a melodic sequence aligned with your rhythm.  

5. **Export & Use**  
   - The generated melody is saved as a MIDI file, ready to import into your DAW.  

---

## Installation

```bash
git clone https://github.com/<your-username>/MeloLab.git
cd MeloLab
pip install -r requirements.txt
