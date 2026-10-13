import pygame
import random
import math
import json
import os
import array
import sys
import asyncio

# Initialize Pygame
pygame.init()
pygame.font.init()
try:
    pygame.mixer.init(frequency=44100, size=-16, channels=2, buffer=512)
except Exception as e:
    print(f"Mixer init note: {e}")

# --- CONFIGURATION & CONSTANTS ---
DEFAULT_WIDTH, DEFAULT_HEIGHT = 800, 900
FPS = 60

# --- PROCEDURAL SOUND SYNTHESIZER ---
class SoundSynthesizer:
    def __init__(self):
        self.running = True
        self.enabled = True
        self.sounds = {}
        self._generate_sounds()

    def _generate_sine_wave(self, frequency, duration, sample_rate=44100, volume=0.3):
        n_samples = int(sample_rate * duration)
        buf = array.array('h')
        amplitude = 32767 * volume
        for i in range(n_samples):
            env = 1.0
            if i < 200:
                env = i / 200.0
            elif i > n_samples - 500:
                env = (n_samples - i) / 500.0
                
            t = float(i) / sample_rate
            value = int(amplitude * env * math.sin(2.0 * math.pi * frequency * t))
            buf.append(value)
            buf.append(value)
        return pygame.mixer.Sound(buffer=buf)

    def _generate_chord(self, freqs, duration, volume=0.2):
        sample_rate = 44100
        n_samples = int(sample_rate * duration)
        buf = array.array('h')
        amplitude = (32767 * volume) / len(freqs)
        for i in range(n_samples):
            env = 1.0
            if i < 300:
                env = i / 300.0
            elif i > n_samples - 800:
                env = (n_samples - i) / 800.0
                
            t = float(i) / sample_rate
            val = sum(math.sin(2.0 * math.pi * f * t) for f in freqs)
            sample_val = int(amplitude * env * val)
            buf.append(sample_val)
            buf.append(sample_val)
        return pygame.mixer.Sound(buffer=buf)

    def _generate_sounds(self):
        try:
            self.sounds["move"] = self._generate_sine_wave(320, 0.04, volume=0.15)
            self.sounds["merge"] = self._generate_sine_wave(587.33, 0.1, volume=0.25)
            self.sounds["click"] = self._generate_sine_wave(440, 0.03, volume=0.2)
            self.sounds["undo"] = self._generate_sine_wave(261.63, 0.08, volume=0.2)
            self.sounds["win"] = self._generate_chord([523.25, 659.25, 783.99, 1046.50], 0.4, volume=0.3)
            self.sounds["gameover"] = self._generate_chord([220.00, 207.65, 196.00], 0.5, volume=0.25)
        except Exception as e:
            print(f"Sound generation notice: {e}")
            self.enabled = False

    def play(self, sound_name):
        if self.enabled and sound_name in self.sounds:
            try:
                self.sounds[sound_name].play()
            except Exception:
                pass


# --- THEME ENGINE ---
class Theme:
    IVORY = "Ivory Soft"
    RAVEN = "Raven Night"

    PALETTES = {
        IVORY: {
            "name": "Ivory Soft",
            "bg_color": (248, 246, 240),
            "glass_card_bg": (255, 255, 255, 210),
            "glass_card_border": (220, 212, 198, 255),
            "grid_bg": (232, 224, 212, 230),
            "grid_cell": (216, 206, 192, 180),
            "text_main": (55, 48, 40),
            "text_muted": (135, 122, 108),
            "text_accent": (217, 119, 6),
            "accent_glow": (245, 158, 11, 200),
            "btn_bg": (242, 235, 222, 230),
            "btn_hover": (255, 255, 255, 255),
            "btn_text": (55, 48, 40),
            "tile_colors": {
                2:    ((238, 228, 218), (119, 110, 101)),
                4:    ((237, 224, 200), (119, 110, 101)),
                8:    ((242, 177, 121), (255, 255, 255)),
                16:   ((245, 149, 99),  (255, 255, 255)),
                32:   ((246, 124, 95),  (255, 255, 255)),
                64:   ((246, 94, 59),   (255, 255, 255)),
                128:  ((237, 207, 114), (255, 255, 255)),
                256:  ((237, 204, 97),  (255, 255, 255)),
                512:  ((237, 200, 80),  (255, 255, 255)),
                1024: ((237, 197, 63),  (255, 255, 255)),
                2048: ((237, 194, 46),  (255, 255, 255)),
                4096: ((139, 92, 246),  (255, 255, 255)),
                8192: ((236, 72, 153),  (255, 255, 255)),
            }
        },
        RAVEN: {
            "name": "Raven Night",
            "bg_color": (15, 23, 42),
            "glass_card_bg": (30, 41, 59, 210),
            "glass_card_border": (99, 102, 241, 140),
            "grid_bg": (22, 30, 46, 230),
            "grid_cell": (33, 45, 66, 180),
            "text_main": (248, 250, 252),
            "text_muted": (148, 163, 184),
            "text_accent": (56, 189, 248),
            "accent_glow": (56, 189, 248, 200),
            "btn_bg": (33, 45, 66, 230),
            "btn_hover": (51, 65, 85, 255),
            "btn_text": (248, 250, 252),
            "tile_colors": {
                2:    ((30, 41, 59),   (248, 250, 252)),
                4:    ((51, 65, 85),   (248, 250, 252)),
                8:    ((217, 119, 6),  (255, 255, 255)),
                16:   ((234, 88, 12),  (255, 255, 255)),
                32:   ((220, 38, 38),  (255, 255, 255)),
                64:   ((225, 29, 72),  (255, 255, 255)),
                128:  ((124, 58, 237), (255, 255, 255)),
                256:  ((109, 40, 217), (255, 255, 255)),
                512:  ((37, 99, 235),  (255, 255, 255)),
                1024: ((8, 145, 178),  (255, 255, 255)),
                2048: ((16, 185, 129), (255, 255, 255)),
                4096: ((219, 39, 119), (255, 255, 255)),
                8192: ((168, 85, 247), (255, 255, 255)),
            }
        }
    }


# --- GLASSMORPHIC GRAPHICS HELPERS ---
def draw_glass_panel(surface, rect, bg_rgba, border_rgba, radius=16, border_width=2):
    x, y, w, h = rect
    panel_surf = pygame.Surface((w, h), pygame.SRCALPHA)
    pygame.draw.rect(panel_surf, bg_rgba, (0, 0, w, h), border_radius=radius)
    if border_width > 0:
        pygame.draw.rect(panel_surf, border_rgba, (0, 0, w, h), width=border_width, border_radius=radius)
    surface.blit(panel_surf, (x, y))


# --- REACTIVE GLASS BUTTON ---
class GlassButton:
    def __init__(self, rect, text, font, callback=None):
        self.rect = pygame.Rect(rect)
        self.text = text
        self.font = font
        self.callback = callback
        self.is_hovered = False
        self.scale = 1.0
        self.target_scale = 1.0

    def update(self, mouse_pos):
        self.is_hovered = self.rect.collidepoint(mouse_pos)
        self.target_scale = 1.04 if self.is_hovered else 1.0
        self.scale += (self.target_scale - self.scale) * 0.3

    def draw(self, surface, theme_dict):
        sw = int(self.rect.width * self.scale)
        sh = int(self.rect.height * self.scale)
        sx = self.rect.centerx - sw // 2
        sy = self.rect.centery - sh // 2
        scaled_rect = (sx, sy, sw, sh)

        bg = theme_dict["btn_hover"] if self.is_hovered else theme_dict["btn_bg"]
        border = theme_dict["glass_card_border"]
        if self.is_hovered:
            border = theme_dict["accent_glow"]

        draw_glass_panel(surface, scaled_rect, bg, border, radius=12, border_width=2)

        text_color = theme_dict["btn_text"]
        if self.is_hovered and "text_accent" in theme_dict:
            text_color = theme_dict["text_accent"]

        rendered_text = self.font.render(self.text, True, text_color)
        text_rect = rendered_text.get_rect(center=(self.rect.centerx, self.rect.centery))
        surface.blit(rendered_text, text_rect)

    def handle_event(self, event, sound_mgr=None):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.is_hovered:
                if sound_mgr:
                    sound_mgr.play("click")
                if self.callback:
                    self.callback()
                return True
        return False


# --- FLOATING SCORE POPUP ---
class FloatingScore:
    def __init__(self, value, x, y, font):
        self.text = f"+{value}"
        self.x = x
        self.y = y
        self.font = font
        self.alpha = 255
        self.dy = -1.5

    def update(self):
        self.y += self.dy
        self.alpha -= 6
        return self.alpha > 0

    def draw(self, surface, color):
        if self.alpha <= 0:
            return
        rendered = self.font.render(self.text, True, color)
        surf = pygame.Surface(rendered.get_size(), pygame.SRCALPHA)
        surf.blit(rendered, (0, 0))
        surf.set_alpha(max(0, self.alpha))
        surface.blit(surf, (self.x - surf.get_width() // 2, self.y))


# --- TILE CLASS ---
class Tile:
    def __init__(self, value, row, col):
        self.value = value
        self.row = row
        self.col = col
        self.x = 0
        self.y = 0
        self.target_x = 0
        self.target_y = 0
        self.scale = 0.2
        self.target_scale = 1.0
        self.merged_this_turn = False

    def update_position(self, grid_x, grid_y, cell_size, gap):
        self.target_x = grid_x + gap + self.col * (cell_size + gap)
        self.target_y = grid_y + gap + self.row * (cell_size + gap)
        
        if self.x == 0 and self.y == 0:
            self.x = self.target_x
            self.y = self.target_y
        else:
            self.x += (self.target_x - self.x) * 0.4
            self.y += (self.target_y - self.y) * 0.4

        self.scale += (self.target_scale - self.scale) * 0.3

    def trigger_pop(self):
        self.scale = 1.25

    def draw(self, surface, cell_size, theme_dict):
        tile_colors = theme_dict["tile_colors"]
        bg_color, text_color = tile_colors.get(
            self.value, 
            ((124, 58, 237), (255, 255, 255))
        )

        w = int(cell_size * self.scale)
        h = int(cell_size * self.scale)
        cx = self.x + cell_size / 2
        cy = self.y + cell_size / 2
        draw_x = cx - w / 2
        draw_y = cy - h / 2

        radius = max(8, int(cell_size * 0.14))

        tile_surf = pygame.Surface((w, h), pygame.SRCALPHA)
        pygame.draw.rect(tile_surf, bg_color, (0, 0, w, h), border_radius=radius)
        pygame.draw.rect(tile_surf, (255, 255, 255, 40), (0, 0, w, h), width=1, border_radius=radius)

        surface.blit(tile_surf, (draw_x, draw_y))

        val_str = str(self.value)
        num_len = len(val_str)
        font_size = int(cell_size * (0.45 if num_len <= 2 else (0.35 if num_len == 3 else 0.28)))
        font = pygame.font.SysFont("comicsans", font_size, bold=True)

        rendered_text = font.render(val_str, True, text_color)
        text_rect = rendered_text.get_rect(center=(cx, cy))
        surface.blit(rendered_text, text_rect)


# --- 2048 GAME ENGINE CLASS ---
class Game2048:
    def __init__(self):
        self.width = DEFAULT_WIDTH
        self.height = DEFAULT_HEIGHT
        self.grid_size = 4
        self.grid = []
        self.score = 0
        self.high_scores = self.load_high_scores()
        self.sound_mgr = SoundSynthesizer()
        self.theme_name = Theme.RAVEN
        self.state = "MENU"
        self.history_stack = []
        self.floating_scores = []
        self.keep_playing = False

        self.setup_ui()
        self.init_game()

    def load_high_scores(self):
        filename = "highscore.json"
        if os.path.exists(filename):
            try:
                with open(filename, "r") as f:
                    return json.load(f)
            except Exception:
                pass
        return {"3": 0, "4": 0, "5": 0}

    def save_high_scores(self):
        try:
            with open("highscore.json", "w") as f:
                json.dump(self.high_scores, f)
        except Exception as e:
            print(f"Error saving high score: {e}")

    def get_high_score(self):
        return self.high_scores.get(str(self.grid_size), 0)

    def update_high_score(self):
        key = str(self.grid_size)
        if self.score > self.high_scores.get(key, 0):
            self.high_scores[key] = self.score
            self.save_high_scores()

    def get_theme(self):
        return Theme.PALETTES[self.theme_name]

    def toggle_theme(self):
        self.theme_name = Theme.IVORY if self.theme_name == Theme.RAVEN else Theme.RAVEN
        self.setup_ui()

    def toggle_sound(self):
        self.sound_mgr.enabled = not self.sound_mgr.enabled

    def set_grid_size(self, size):
        self.grid_size = size
        self.init_game()

    def quit_game(self):
        self.running = False

    def init_game(self):
        self.grid = [[None for _ in range(self.grid_size)] for _ in range(self.grid_size)]
        self.score = 0
        self.history_stack = []
        self.floating_scores = []
        self.keep_playing = False
        self.spawn_tile()
        self.spawn_tile()

    def setup_ui(self):
        font_main = pygame.font.SysFont("comicsans", 22, bold=True)
        font_lg = pygame.font.SysFont("comicsans", 30, bold=True)
        
        # Start Menu Buttons
        self.btn_play = GlassButton((240, 295, 320, 54), "START GAME", font_lg, callback=lambda: self.start_game())
        self.btn_theme_menu = GlassButton((240, 362, 320, 48), f"MODE: {self.theme_name.upper()}", font_main, callback=self.toggle_theme)
        
        # Grid Size Buttons row
        self.btn_grid3 = GlassButton((220, 465, 100, 44), "3x3", font_main, callback=lambda: self.set_grid_size(3))
        self.btn_grid4 = GlassButton((350, 465, 100, 44), "4x4", font_main, callback=lambda: self.set_grid_size(4))
        self.btn_grid5 = GlassButton((480, 465, 100, 44), "5x5", font_main, callback=lambda: self.set_grid_size(5))

        # Quit Button on Start Menu
        self.btn_quit_menu = GlassButton((240, 532, 320, 48), "QUIT GAME", font_main, callback=self.quit_game)

        # Gameplay Top Header Buttons
        self.btn_undo = GlassButton((520, 115, 110, 42), "↺ UNDO", font_main, callback=self.undo_move)
        self.btn_pause = GlassButton((645, 115, 110, 42), "⏸ PAUSE", font_main, callback=self.pause_game)

        # Pause Overlay Buttons
        self.btn_resume = GlassButton((300, 315, 200, 44), "RESUME", font_lg, callback=self.resume_game)
        self.btn_restart_pause = GlassButton((300, 370, 200, 44), "RESTART", font_lg, callback=self.restart_game)
        self.btn_theme_pause = GlassButton((250, 425, 300, 44), f"MODE: {self.theme_name.upper()}", font_main, callback=self.toggle_theme)
        self.btn_main_menu = GlassButton((300, 480, 200, 44), "MAIN MENU", font_main, callback=self.goto_menu)
        self.btn_quit_pause = GlassButton((300, 535, 200, 44), "QUIT GAME", font_main, callback=self.quit_game)

        # Game Over / Victory Buttons
        self.btn_try_again = GlassButton((195, 460, 195, 52), "TRY AGAIN", font_lg, callback=self.restart_game)
        self.btn_quit_loss = GlassButton((410, 460, 195, 52), "QUIT GAME", font_lg, callback=self.quit_game)

        self.btn_keep_playing = GlassButton((195, 460, 200, 52), "KEEP PLAYING", font_lg, callback=self.continue_game)
        self.btn_quit_win = GlassButton((410, 460, 195, 52), "QUIT GAME", font_lg, callback=self.quit_game)

    def start_game(self):
        self.init_game()
        self.state = "PLAYING"

    def pause_game(self):
        self.state = "PAUSED"

    def resume_game(self):
        self.state = "PLAYING"

    def restart_game(self):
        self.init_game()
        self.state = "PLAYING"

    def goto_menu(self):
        self.state = "MENU"

    def continue_game(self):
        self.keep_playing = True
        self.state = "PLAYING"

    def save_state_to_history(self):
        snapshot_grid = []
        for r in range(self.grid_size):
            row = []
            for c in range(self.grid_size):
                tile = self.grid[r][c]
                row.append(tile.value if tile else 0)
            snapshot_grid.append(row)
        
        self.history_stack.append({
            "grid": snapshot_grid,
            "score": self.score
        })

        if len(self.history_stack) > 10:
            self.history_stack.pop(0)

    def undo_move(self):
        if not self.history_stack:
            return
        
        self.sound_mgr.play("undo")
        last_state = self.history_stack.pop()
        self.score = last_state["score"]

        grid_data = last_state["grid"]
        self.grid = [[None for _ in range(self.grid_size)] for _ in range(self.grid_size)]
        for r in range(self.grid_size):
            for c in range(self.grid_size):
                val = grid_data[r][c]
                if val > 0:
                    self.grid[r][c] = Tile(val, r, c)

        if self.state in ("GAME_OVER", "WON"):
            self.state = "PLAYING"

    def get_empty_cells(self):
        empty = []
        for r in range(self.grid_size):
            for c in range(self.grid_size):
                if self.grid[r][c] is None:
                    empty.append((r, c))
        return empty

    def spawn_tile(self):
        empty = self.get_empty_cells()
        if empty:
            r, c = random.choice(empty)
            val = 4 if random.random() < 0.1 else 2
            self.grid[r][c] = Tile(val, r, c)

    def execute_move(self, direction):
        if self.state != "PLAYING":
            return

        self.save_state_to_history()
        moved = False
        merged_score_turn = 0

        for r in range(self.grid_size):
            for c in range(self.grid_size):
                if self.grid[r][c]:
                    self.grid[r][c].merged_this_turn = False

        dr, dc = 0, 0
        r_range = range(self.grid_size)
        c_range = range(self.grid_size)

        if direction == "UP":
            dr = -1
        elif direction == "DOWN":
            dr = 1
            r_range = range(self.grid_size - 1, -1, -1)
        elif direction == "LEFT":
            dc = -1
        elif direction == "RIGHT":
            dc = 1
            c_range = range(self.grid_size - 1, -1, -1)

        for r in r_range:
            for c in c_range:
                tile = self.grid[r][c]
                if not tile:
                    continue

                curr_r, curr_c = r, c
                while True:
                    next_r = curr_r + dr
                    next_c = curr_c + dc

                    if not (0 <= next_r < self.grid_size and 0 <= next_c < self.grid_size):
                        break

                    target = self.grid[next_r][next_c]
                    if target is None:
                        self.grid[next_r][next_c] = tile
                        self.grid[curr_r][curr_c] = None
                        tile.row, tile.col = next_r, next_c
                        curr_r, curr_c = next_r, next_c
                        moved = True
                    elif target.value == tile.value and not target.merged_this_turn and not tile.merged_this_turn:
                        new_val = tile.value * 2
                        target.value = new_val
                        target.merged_this_turn = True
                        target.trigger_pop()
                        self.grid[curr_r][curr_c] = None
                        
                        self.score += new_val
                        merged_score_turn += new_val

                        font_float = pygame.font.SysFont("comicsans", 24, bold=True)
                        cell_sz, gap, gx, gy = self.get_grid_layout()
                        fx = gx + gap + next_c * (cell_sz + gap) + cell_sz // 2
                        fy = gy + gap + next_r * (cell_sz + gap)
                        self.floating_scores.append(FloatingScore(new_val, fx, fy, font_float))

                        moved = True
                        break
                    else:
                        break

        if moved:
            self.sound_mgr.play("merge" if merged_score_turn > 0 else "move")
            self.spawn_tile()
            self.update_high_score()
            self.check_game_status()
        else:
            if self.history_stack:
                self.history_stack.pop()

    def check_game_status(self):
        if not self.keep_playing:
            for r in range(self.grid_size):
                for c in range(self.grid_size):
                    if self.grid[r][c] and self.grid[r][c].value >= 2048:
                        self.state = "WON"
                        self.sound_mgr.play("win")
                        return

        if not self.get_empty_cells():
            can_merge = False
            for r in range(self.grid_size):
                for c in range(self.grid_size):
                    val = self.grid[r][c].value
                    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < self.grid_size and 0 <= nc < self.grid_size:
                            if self.grid[nr][nc].value == val:
                                can_merge = True
                                break
                    if can_merge:
                        break
                if can_merge:
                    break

            if not can_merge:
                self.state = "GAME_OVER"
                self.sound_mgr.play("gameover")

    def get_grid_layout(self):
        grid_width = 540
        grid_x = (self.width - grid_width) // 2
        grid_y = 210
        gap = 14
        cell_size = (grid_width - (gap * (self.grid_size + 1))) // self.grid_size
        return cell_size, gap, grid_x, grid_y

    def update(self, mouse_pos):
        theme_dict = self.get_theme()
        
        cell_sz, gap, gx, gy = self.get_grid_layout()
        for r in range(self.grid_size):
            for c in range(self.grid_size):
                tile = self.grid[r][c]
                if tile:
                    tile.update_position(gx, gy, cell_sz, gap)

        self.floating_scores = [fs for fs in self.floating_scores if fs.update()]

        if self.state == "MENU":
            self.btn_play.update(mouse_pos)
            self.btn_theme_menu.update(mouse_pos)
            self.btn_grid3.update(mouse_pos)
            self.btn_grid4.update(mouse_pos)
            self.btn_grid5.update(mouse_pos)
            self.btn_quit_menu.update(mouse_pos)
        elif self.state in ("PLAYING", "WON", "GAME_OVER"):
            self.btn_undo.update(mouse_pos)
            self.btn_pause.update(mouse_pos)
            if self.state == "WON":
                self.btn_keep_playing.update(mouse_pos)
                self.btn_quit_win.update(mouse_pos)
            elif self.state == "GAME_OVER":
                self.btn_try_again.update(mouse_pos)
                self.btn_quit_loss.update(mouse_pos)
        elif self.state == "PAUSED":
            self.btn_resume.update(mouse_pos)
            self.btn_restart_pause.update(mouse_pos)
            self.btn_theme_pause.update(mouse_pos)
            self.btn_main_menu.update(mouse_pos)
            self.btn_quit_pause.update(mouse_pos)

    def draw(self, surface):
        theme_dict = self.get_theme()
        surface.fill(theme_dict["bg_color"])

        if self.state == "MENU":
            self.draw_menu_screen(surface, theme_dict)
        else:
            self.draw_gameplay_screen(surface, theme_dict)

            if self.state == "PAUSED":
                self.draw_pause_overlay(surface, theme_dict)
            elif self.state == "WON":
                self.draw_victory_overlay(surface, theme_dict)
            elif self.state == "GAME_OVER":
                self.draw_gameover_overlay(surface, theme_dict)

    def draw_menu_screen(self, surface, theme_dict):
        # Hero Title Card
        draw_glass_panel(surface, (130, 60, 540, 175), theme_dict["glass_card_bg"], theme_dict["glass_card_border"], radius=24, border_width=2)

        font_title = pygame.font.SysFont("comicsans", 68, bold=True)
        title_text = font_title.render("2048", True, theme_dict["text_main"])
        surface.blit(title_text, title_text.get_rect(center=(400, 115)))

        font_sub = pygame.font.SysFont("comicsans", 20, bold=True)
        sub_text = font_sub.render("GLASS EDITION", True, theme_dict["text_accent"])
        surface.blit(sub_text, sub_text.get_rect(center=(400, 170)))

        font_info = pygame.font.SysFont("comicsans", 16)
        info_text = font_info.render("Join tiles with Arrow keys or WASD to reach 2048!", True, theme_dict["text_muted"])
        surface.blit(info_text, info_text.get_rect(center=(400, 205)))

        # Main Action Container Card
        draw_glass_panel(surface, (130, 255, 540, 510), theme_dict["glass_card_bg"], theme_dict["glass_card_border"], radius=24, border_width=2)

        self.btn_play.draw(surface, theme_dict)
        self.btn_theme_menu.draw(surface, theme_dict)

        lbl_grid = font_sub.render("SELECT GRID SIZE", True, theme_dict["text_main"])
        surface.blit(lbl_grid, lbl_grid.get_rect(center=(400, 435)))

        self.btn_grid3.draw(surface, theme_dict)
        self.btn_grid4.draw(surface, theme_dict)
        self.btn_grid5.draw(surface, theme_dict)

        sel_btn = self.btn_grid4
        if self.grid_size == 3: sel_btn = self.btn_grid3
        elif self.grid_size == 5: sel_btn = self.btn_grid5
        pygame.draw.rect(surface, theme_dict["text_accent"], sel_btn.rect.inflate(6, 6), width=3, border_radius=14)

        # Quit Button
        self.btn_quit_menu.draw(surface, theme_dict)

        hint_txt = font_info.render("Controls: Arrow Keys / WASD  |  [U]: Undo  |  [P]: Pause", True, theme_dict["text_muted"])
        surface.blit(hint_txt, hint_txt.get_rect(center=(400, 695)))

        snd_txt = f"Sound: {'ON' if self.sound_mgr.enabled else 'OFF'} (Press 'M' to toggle)"
        lbl_snd = font_info.render(snd_txt, True, theme_dict["text_muted"])
        surface.blit(lbl_snd, lbl_snd.get_rect(center=(400, 800)))

    def draw_gameplay_screen(self, surface, theme_dict):
        font_logo = pygame.font.SysFont("comicsans", 52, bold=True)
        logo_text = font_logo.render("2048", True, theme_dict["text_main"])
        surface.blit(logo_text, (45, 30))

        font_tag = pygame.font.SysFont("comicsans", 16, bold=True)
        tag_text = font_tag.render(self.theme_name.upper(), True, theme_dict["text_accent"])
        surface.blit(tag_text, (48, 90))

        draw_glass_panel(surface, (230, 30, 130, 75), theme_dict["glass_card_bg"], theme_dict["glass_card_border"], radius=14)
        font_lbl = pygame.font.SysFont("comicsans", 16, bold=True)
        font_val = pygame.font.SysFont("comicsans", 28, bold=True)
        
        lbl_s = font_lbl.render("SCORE", True, theme_dict["text_muted"])
        val_s = font_val.render(str(self.score), True, theme_dict["text_main"])
        surface.blit(lbl_s, lbl_s.get_rect(center=(295, 48)))
        surface.blit(val_s, val_s.get_rect(center=(295, 78)))

        draw_glass_panel(surface, (375, 30, 130, 75), theme_dict["glass_card_bg"], theme_dict["glass_card_border"], radius=14)
        lbl_h = font_lbl.render("BEST", True, theme_dict["text_muted"])
        val_h = font_val.render(str(self.get_high_score()), True, theme_dict["text_accent"])
        surface.blit(lbl_h, lbl_h.get_rect(center=(440, 48)))
        surface.blit(val_h, val_h.get_rect(center=(440, 78)))

        self.btn_undo.draw(surface, theme_dict)
        self.btn_pause.draw(surface, theme_dict)

        cell_sz, gap, gx, gy = self.get_grid_layout()
        grid_w = self.grid_size * (cell_sz + gap) + gap
        grid_h = grid_w

        draw_glass_panel(surface, (gx, gy, grid_w, grid_h), theme_dict["grid_bg"], theme_dict["glass_card_border"], radius=20, border_width=3)

        for r in range(self.grid_size):
            for c in range(self.grid_size):
                cx = gx + gap + c * (cell_sz + gap)
                cy = gy + gap + r * (cell_sz + gap)
                radius = max(8, int(cell_sz * 0.14))
                pygame.draw.rect(surface, theme_dict["grid_cell"], (cx, cy, cell_sz, cell_sz), border_radius=radius)

        for r in range(self.grid_size):
            for c in range(self.grid_size):
                tile = self.grid[r][c]
                if tile:
                    tile.draw(surface, cell_sz, theme_dict)

        for fs in self.floating_scores:
            fs.draw(surface, theme_dict["text_accent"])

        font_tip = pygame.font.SysFont("comicsans", 16)
        tip_text = font_tip.render("[Arrow Keys / WASD]: Move  |  [U]: Undo  |  [P / ESC]: Pause  |  [M]: Mute", True, theme_dict["text_muted"])
        surface.blit(tip_text, tip_text.get_rect(center=(400, 840)))

    def draw_pause_overlay(self, surface, theme_dict):
        overlay_surf = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
        overlay_surf.fill((0, 0, 0, 170))
        surface.blit(overlay_surf, (0, 0))

        draw_glass_panel(surface, (200, 200, 400, 440), theme_dict["glass_card_bg"], theme_dict["accent_glow"], radius=24, border_width=3)

        font_hdr = pygame.font.SysFont("comicsans", 44, bold=True)
        lbl_p = font_hdr.render("GAME PAUSED", True, theme_dict["text_main"])
        surface.blit(lbl_p, lbl_p.get_rect(center=(400, 260)))

        self.btn_resume.draw(surface, theme_dict)
        self.btn_restart_pause.draw(surface, theme_dict)
        self.btn_theme_pause.draw(surface, theme_dict)
        self.btn_main_menu.draw(surface, theme_dict)
        self.btn_quit_pause.draw(surface, theme_dict)

    def draw_victory_overlay(self, surface, theme_dict):
        overlay_surf = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
        overlay_surf.fill((0, 0, 0, 180))
        surface.blit(overlay_surf, (0, 0))

        draw_glass_panel(surface, (160, 250, 480, 340), theme_dict["glass_card_bg"], (245, 158, 11, 220), radius=24, border_width=4)

        font_win = pygame.font.SysFont("comicsans", 50, bold=True)
        lbl_w = font_win.render("YOU WIN! 🎉", True, theme_dict["text_accent"])
        surface.blit(lbl_w, lbl_w.get_rect(center=(400, 315)))

        font_sub = pygame.font.SysFont("comicsans", 22)
        lbl_s = font_sub.render(f"You reached 2048! Score: {self.score}", True, theme_dict["text_main"])
        surface.blit(lbl_s, lbl_s.get_rect(center=(400, 375)))

        self.btn_keep_playing.draw(surface, theme_dict)
        self.btn_quit_win.draw(surface, theme_dict)

    def draw_gameover_overlay(self, surface, theme_dict):
        overlay_surf = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
        overlay_surf.fill((0, 0, 0, 190))
        surface.blit(overlay_surf, (0, 0))

        draw_glass_panel(surface, (160, 250, 480, 340), theme_dict["glass_card_bg"], (225, 29, 72, 220), radius=24, border_width=4)

        font_loss = pygame.font.SysFont("comicsans", 50, bold=True)
        lbl_l = font_loss.render("GAME OVER", True, (225, 29, 72))
        surface.blit(lbl_l, lbl_l.get_rect(center=(400, 315)))

        font_sub = pygame.font.SysFont("comicsans", 22)
        lbl_s = font_sub.render(f"Final Score: {self.score}  |  Best: {self.get_high_score()}", True, theme_dict["text_main"])
        surface.blit(lbl_s, lbl_s.get_rect(center=(400, 375)))

        self.btn_try_again.draw(surface, theme_dict)
        self.btn_quit_loss.draw(surface, theme_dict)

    def handle_event(self, event):
        if event.type == pygame.QUIT:
            return False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_m:
                self.toggle_sound()
            elif event.key == pygame.K_u:
                self.undo_move()
            elif event.key in (pygame.K_ESCAPE, pygame.K_p):
                if self.state == "PLAYING":
                    self.pause_game()
                elif self.state == "PAUSED":
                    self.resume_game()

            if self.state == "PLAYING":
                if event.key in (pygame.K_LEFT, pygame.K_a):
                    self.execute_move("LEFT")
                elif event.key in (pygame.K_RIGHT, pygame.K_d):
                    self.execute_move("RIGHT")
                elif event.key in (pygame.K_UP, pygame.K_w):
                    self.execute_move("UP")
                elif event.key in (pygame.K_DOWN, pygame.K_s):
                    self.execute_move("DOWN")

        if self.state == "MENU":
            self.btn_play.handle_event(event, self.sound_mgr)
            if self.btn_theme_menu.handle_event(event, self.sound_mgr):
                self.btn_theme_menu.text = f"MODE: {self.theme_name.upper()}"
            self.btn_grid3.handle_event(event, self.sound_mgr)
            self.btn_grid4.handle_event(event, self.sound_mgr)
            self.btn_grid5.handle_event(event, self.sound_mgr)
            self.btn_quit_menu.handle_event(event, self.sound_mgr)
        elif self.state in ("PLAYING", "WON", "GAME_OVER"):
            self.btn_undo.handle_event(event, self.sound_mgr)
            self.btn_pause.handle_event(event, self.sound_mgr)
            if self.state == "WON":
                self.btn_keep_playing.handle_event(event, self.sound_mgr)
                self.btn_quit_win.handle_event(event, self.sound_mgr)
            elif self.state == "GAME_OVER":
                self.btn_try_again.handle_event(event, self.sound_mgr)
                self.btn_quit_loss.handle_event(event, self.sound_mgr)
        elif self.state == "PAUSED":
            self.btn_resume.handle_event(event, self.sound_mgr)
            self.btn_restart_pause.handle_event(event, self.sound_mgr)
            if self.btn_theme_pause.handle_event(event, self.sound_mgr):
                self.btn_theme_pause.text = f"MODE: {self.theme_name.upper()}"
            self.btn_main_menu.handle_event(event, self.sound_mgr)
            self.btn_quit_pause.handle_event(event, self.sound_mgr)

        return True


# --- MAIN APPLICATION LOOP ---
async def main():
    window = pygame.display.set_mode(
        (DEFAULT_WIDTH, DEFAULT_HEIGHT)
    )
    pygame.display.set_caption("2048 - Glass Edition")

    clock = pygame.time.Clock()
    game = Game2048()

    while game.running:
        clock.tick(FPS)
        await asyncio.sleep(0)

        mouse_pos = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if not game.handle_event(event):
                game.running = False

        if not game.running:
            break

        game.update(mouse_pos)
        game.draw(window)
        pygame.display.flip()


if __name__ == "__main__":
    asyncio.run(main())