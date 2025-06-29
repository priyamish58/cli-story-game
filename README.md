# CLI Story Game - Multi-Genre Adventure 🎮

Welcome to **CLI Story Game**, a multi-genre **command-line choose-your-own-adventure game** written in Python. From fantasy magic to mysterious fogs, heartwarming romance, and light-hearted comedy—you get to choose your world and path.

## 🕹️ Features
- Text-based CLI gameplay
- Interactive stories with multiple endings
- Four switchable themes:
  - 🧙‍♂️ Fantasy — *The Ember Stone*
  - 🕵️ Mystery — *Echoes in the Fog*
  - 💖 Romance — *Hearts Ablaze*
  - 😂 Comedy — *Toast of Destiny*
- Rich story structure using YAML
- ASCII art title banners by genre

## 📂 Folder Structure
```
cli_game/
├── game.py           # Main game script
├── fantasy.yaml       # Fantasy story
├── mystery.yaml       # Mystery story
├── romance.yaml       # Romance story
├── comedy.yaml        #comedy story
├── requirements.txt  # Dependencies
└── README.md         # Project overview
```

## ▶️ Getting Started
### 1. Clone the Repo
```bash
git clone https://github.com/your-username/cli-story-game.git
cd cli-story-game
```

### 2. Create Virtual Environment (Optional)
```bash
python -m venv venv
source venv/bin/activate     # Linux/macOS
venv\Scripts\activate        # Windows
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the Game
```bash
python game.py
```

## 🛠️ Requirements
- Python 3.8+
- Modules: `pyyaml`, `colorama`

Install manually if needed:
```bash
pip install pyyaml colorama
```

## 🎨 Change Story Theme
At the start of the game, users are prompted to choose their preferred theme by entering a number from the menu. Based on the selection, the corresponding story and ASCII banner are loaded automatically.


## 📦 Packaging (Optional)
You can skip this step if you're only running the game locally or sharing the source code (game.py and story.yaml). However, if you'd like to turn the game into a standalone executable:

Use `pyinstaller`:
```bash
pip install pyinstaller
pyinstaller --onefile game.py
```
The executable will be available in the `dist/` folder.

---

## ✨ Credits
Built with ❤️ using Python, YAML, and the powerful capabilities of **Amazon Q CLI**.

This project was ideated, developed, and structured as part of the **Amazon Q CLI Challenge**, showcasing how AI and command-line interfaces can bring interactive storytelling to life.

Storylines and visuals designed for the **Amazon Q CLI Challenge**.

---

Want to contribute or give feedback? Feel free to open issues or PRs!




