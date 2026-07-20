# 🎮 2048 - Glass Edition

A modern, feature-rich Python implementation of the classic **2048** puzzle game, enhanced with glassmorphic aesthetics, dual color themes, procedural audio, multi-grid options, and game state undo capabilities.

![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)
![Pygame](https://img.shields.io/badge/Pygame-2.0%2B-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

---

## ✨ Features

- 💎 **Glassmorphic Aesthetic UI**: Translucent glass card containers, crisp full-color tile blocks, and interactive reactive buttons with smooth hover scaling.
- 🎨 **Dual Visual Themes**:
  - **Raven Night Mode**: Deep obsidian dark mode (`#0F172A`) with vibrant neon tiles and indigo glass borders.
  - **Ivory Soft Mode**: Warm ivory sand background (`#F8F6F0`) with classic tile colors.
- 📐 **Multiple Grid Sizes**: Choose between **3x3** (Fast/Challenge), **4x4** (Classic), or **5x5** (Relaxed/Big Board).
- ↺ **Multi-Step Undo Engine**: Revert up to 10 previous moves using the `U` key or the **↺ UNDO** button.
- 🏆 **Score & High Score Persistence**: Live score updates with floating `+Score` animations and auto-saving high scores to `highscore.json`.
- 🎵 **Procedural Sound Engine**: Dynamic sound synthesizer for tile slides, merges, clicks, undo, victory, and game over—requiring no external `.wav` asset files.
- ⏸ **Interactive Overlays**:
  - Structured **Start Menu** with mode selection and grid options.
  - **Pause Menu Overlay** (`P` / `ESC`) to resume, restart, switch theme, or quit.
  - **Victory Overlay** (reaching 2048) with an option to continue playing in **Endless Mode**.
  - **Game Over Overlay** with score summary and instant try-again button.

---

## 🛠️ Requirements & Installation

### Prerequisites
- **Python 3.8+**
- **Pygame 2.0+**

### Install Dependencies
Run the following command in your terminal:
```bash
pip install pygame
```

---

## 🚀 Running the Game

Launch the game by executing `2048.py`:

```bash
python 2048.py
```

---

## 🎮 Game Controls

| Key / Action | Function |
| :--- | :--- |
| **`Arrow Keys` / `W`, `A`, `S`, `D`** | Slide & merge tiles (Up, Down, Left, Right) |
| **`U`** or **↺ UNDO Button** | Revert last move (up to 10 steps back) |
| **`P` / `ESC`** or **⏸ PAUSE Button** | Pause / Resume game |
| **`M`** | Toggle audio sound effects ON / OFF |
| **Mouse Hover & Left Click** | Interact with buttons and menus |

---

## 📂 Project Structure

```
2048-2-game/
├── 2048.py          # Main game engine, sound synthesizer, UI & rendering
├── highscore.json   # Auto-generated local high scores store
└── README.md        # Project documentation
```

---

## 💡 How to Play

1. Use the **Arrow Keys** or **WASD** to slide all tiles across the grid in a given direction.
2. When two tiles with the **same number** touch, they **merge into one** with double the value (e.g., $2 + 2 = 4$, $4 + 4 = 8$).
3. Each turn, a new tile ($2$ or $4$) spawns randomly in an empty slot.
4. Reach the **2048** tile to win! You can choose to keep playing in **Endless Mode** to chase higher scores ($4096$, $8192$, etc.).
5. If the grid fills up and no valid moves remain, the game is over.

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).