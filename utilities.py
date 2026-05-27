#!/usr/bin/env python3
"""
╔═════════════════════════════════════════════════════════════════╗
║     🚀 ULTRA BOT UTILITIES & ADVANCED FEATURES v2.0            ║
║  Extra commands, decorations, animations & premium features    ║
╚═════════════════════════════════════════════════════════════════╝

This module provides advanced utilities and animations for the bot.
Import this to get access to additional premium features.
"""

import asyncio
import random
from typing import List, Tuple
from datetime import datetime, timezone

UTC = timezone.utc
now_utc = lambda: datetime.now(UTC)

# ═══════════════════════════════════════════════════════════════════
#                    ANIMATED DECORATIONS
# ═══════════════════════════════════════════════════════════════════

class AnimatedFrames:
    """Collection of animated frames for progress indicators."""

    # Loading spinners
    SPINNER_1 = ["⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧", "⠇", "⠏"]
    SPINNER_2 = ["◐", "◓", "◑", "◒"]
    SPINNER_3 = ["✕", "✖", "✗"]
    SPINNER_4 = ["⣾", "⣽", "⣻", "⢿", "⡿", "⣟", "⣯", "⣷"]

    # Progress bars
    PROGRESS_1 = ["▁", "▂", "▃", "▄", "▅", "▆", "▇", "█"]
    PROGRESS_2 = ["◤", "◥", "◢", "◣"]

    # Flashing effects
    FLASH = ["✨", "💫", "🌟"]
    WAVE = ["▐", "▌"]

    # Pulse effects
    PULSE = ["●", "○"]
    HEART_BEAT = ["💓", "💗", "💖"]

    @staticmethod
    def get_spinner_1(index: int) -> str:
        return AnimatedFrames.SPINNER_1[index % len(AnimatedFrames.SPINNER_1)]

    @staticmethod
    def get_spinner_2(index: int) -> str:
        return AnimatedFrames.SPINNER_2[index % len(AnimatedFrames.SPINNER_2)]

    @staticmethod
    def get_progress_bar(percentage: int) -> str:
        """Generate a visual progress bar (0-100)."""
        filled = percentage // 10
        empty = 10 - filled
        return f"[{'█' * filled}{'░' * empty}] {percentage}%"


class PremiumDecorations:
    """Premium text decorations and fancy formatting."""

    @staticmethod
    def fancy_title(text: str) -> str:
        """Create a fancy title with decorations."""
        stars = "⭐" * (len(text) // 2 + 1)
        return f"{stars}\n{text}\n{stars}"

    @staticmethod
    def box_text(text: str, style: str = "simple") -> str:
        """Create a boxed text."""
        if style == "simple":
            return f"┌{'─' * (len(text) + 2)}┐\n│ {text} │\n└{'─' * (len(text) + 2)}┘"
        elif style == "double":
            return f"╔{'═' * (len(text) + 2)}╗\n║ {text} ║\n╚{'═' * (len(text) + 2)}╝"
        elif style == "rounded":
            return f"╭{'─' * (len(text) + 2)}╮\n│ {text} │\n╰{'─' * (len(text) + 2)}╯"
        return text

    @staticmethod
    def create_separator(length: int = 30, style: str = "dash") -> str:
        """Create a separator line."""
        if style == "dash":
            return "━" * length
        elif style == "equals":
            return "═" * length
        elif style == "dots":
            return "•" * length
        elif style == "stars":
            return "⭐" * (length // 2)
        return "─" * length

    @staticmethod
    def create_list_item(text: str, icon: str = "•") -> str:
        """Create a formatted list item."""
        return f"{icon} {text}"

    @staticmethod
    def create_status_badge(status: str) -> str:
        """Create a status badge."""
        badges = {
            "online": "🟢 Online",
            "offline": "🔴 Offline",
            "busy": "🟠 Busy",
            "premium": "👑 Premium",
            "verified": "✅ Verified",
            "vip": "💎 VIP",
        }
        return badges.get(status, status)


class ProgressAnimator:
    """Animated progress updates."""

    def __init__(self, total: int, description: str = ""):
        self.total = total
        self.current = 0
        self.description = description
        self.start_time = now_utc()

    def get_progress_text(self) -> str:
        """Get formatted progress text."""
        percentage = int((self.current / self.total) * 100) if self.total > 0 else 0
        bar = AnimatedFrames.get_progress_bar(percentage)

        elapsed = (now_utc() - self.start_time).total_seconds()

        text = f"{self.description}\n\n{bar}\n"
        text += f"Progress: {self.current}/{self.total} "
        text += f"({percentage}%)\n"
        text += f"Time: {int(elapsed)}s"

        return text

    def update(self, amount: int = 1):
        """Update progress."""
        self.current = min(self.current + amount, self.total)

    def is_complete(self) -> bool:
        """Check if progress is complete."""
        return self.current >= self.total


# ═══════════════════════════════════════════════════════════════════
#                      TEXT FORMATTING
# ═══════════════════════════════════════════════════════════════════

class TextFormatter:
    """Advanced text formatting utilities."""

    @staticmethod
    def to_bold(text: str) -> str:
        return f"<b>{text}</b>"

    @staticmethod
    def to_italic(text: str) -> str:
        return f"<i>{text}</i>"

    @staticmethod
    def to_underline(text: str) -> str:
        return f"<u>{text}</u>"

    @staticmethod
    def to_strikethrough(text: str) -> str:
        return f"<s>{text}</s>"

    @staticmethod
    def to_code(text: str) -> str:
        return f"<code>{text}</code>"

    @staticmethod
    def to_pre(text: str, language: str = "") -> str:
        return f"<pre><code class=\"language-{language}\">{text}</code></pre>"

    @staticmethod
    def create_link(text: str, url: str) -> str:
        return f'<a href="{url}">{text}</a>'

    @staticmethod
    def create_mention_link(text: str, user_id: int) -> str:
        return f'<a href="tg://user?id={user_id}">{text}</a>'

    @staticmethod
    def create_spoiler(text: str) -> str:
        return f"<tg-spoiler>{text}</tg-spoiler>"

    @staticmethod
    def multiline(lines: List[str], indent: int = 0) -> str:
        """Create multiline formatted text."""
        prefix = " " * indent
        return "\n".join(f"{prefix}{line}" for line in lines)


class EmojiLibrary:
    """Extended emoji library for premium bot."""

    # Premium vibes
    PREMIUM = {
        "fire": "🔥",
        "star": "⭐",
        "heart": "❤️",
        "diamond": "💎",
        "crown": "👑",
        "rocket": "🚀",
        "sparkle": "✨",
        "tada": "🎉",
        "boom": "💥",
        "bolt": "⚡",
    }

    # Status
    STATUS = {
        "check": "✅",
        "cross": "❌",
        "warning": "⚠️",
        "info": "ℹ️",
        "question": "❓",
        "prohibited": "🚫",
        "lock": "🔒",
        "unlock": "🔓",
    }

    # Navigation
    NAV = {
        "up": "⬆️",
        "down": "⬇️",
        "left": "⬅️",
        "right": "➡️",
        "back": "🔙",
        "forward": "🔜",
        "refresh": "🔄",
        "settings": "⚙️",
    }

    # Hands
    HANDS = {
        "thumbs_up": "👍",
        "thumbs_down": "👎",
        "clap": "👏",
        "pray": "🙏",
        "handshake": "🤝",
        "wave": "👋",
        "ok": "👌",
        "point_up": "☝️",
    }

    # Faces
    FACES = {
        "happy": "😊",
        "laugh": "😂",
        "cool": "😎",
        "love": "😍",
        "sad": "😢",
        "angry": "😡",
        "shocked": "😱",
        "thinking": "🤔",
        "angel": "😇",
        "devil": "😈",
        "sunglasses": "😎",
    }

    @staticmethod
    def get_premium(key: str, default: str = "") -> str:
        return EmojiLibrary.PREMIUM.get(key, default)

    @staticmethod
    def get_status(key: str, default: str = "") -> str:
        return EmojiLibrary.STATUS.get(key, default)

    @staticmethod
    def get_nav(key: str, default: str = "") -> str:
        return EmojiLibrary.NAV.get(key, default)


# ═══════════════════════════════════════════════════════════════════
#                    MESSAGE TEMPLATES
# ═══════════════════════════════════════════════════════════════════

class MessageTemplates:
    """Pre-built message templates."""

    @staticmethod
    def welcome(name: str, bot_name: str) -> str:
        emoji = EmojiLibrary.PREMIUM["heart"]
        return (
            f"👋 Welcome, <b>{name}</b>! {emoji}\n\n"
            f"⭐ <b>{bot_name}</b>\n"
            f"Your Premium Companion\n\n"
            f"💡 Ready to get started?"
        )

    @staticmethod
    def error(message: str) -> str:
        emoji = EmojiLibrary.STATUS["cross"]
        return f"{emoji} <b>Error:</b> {message}"

    @staticmethod
    def success(message: str) -> str:
        emoji = EmojiLibrary.STATUS["check"]
        return f"{emoji} <b>Success!</b> {message}"

    @staticmethod
    def info(message: str) -> str:
        emoji = EmojiLibrary.STATUS["info"]
        return f"{emoji} <b>Info:</b> {message}"

    @staticmethod
    def warning(message: str) -> str:
        emoji = EmojiLibrary.STATUS["warning"]
        return f"{emoji} <b>Warning:</b> {message}"

    @staticmethod
    def loading(message: str = "Loading...") -> str:
        spinner = AnimatedFrames.SPINNER_1[0]
        return f"{spinner} <b>{message}</b>"

    @staticmethod
    def premium_badge() -> str:
        return "👑 <b>Premium</b>"

    @staticmethod
    def verified_badge() -> str:
        return "✅ <b>Verified</b>"


class StatisticsFormatter:
    """Format statistics and data in beautiful ways."""

    @staticmethod
    def format_stat(label: str, value, icon: str = "•") -> str:
        """Format a single statistic."""
        return f"{icon} <b>{label}:</b> {value}"

    @staticmethod
    def format_stats_table(stats: dict) -> str:
        """Format multiple statistics as a table."""
        lines = []
        max_label_len = max(len(k) for k in stats.keys()) if stats else 0

        for label, value in stats.items():
            padding = " " * (max_label_len - len(label))
            lines.append(f"  {label}{padding}: <b>{value}</b>")

        return "\n".join(lines)

    @staticmethod
    def format_user_profile(user_data: dict) -> str:
        """Format user profile information."""
        lines = [
            f"👤 <b>User Profile</b>",
            f"━━━━━━━━━━━━━━━━━━━",
            f"ID: <code>{user_data.get('user_id', 'N/A')}</code>",
            f"Name: <b>{user_data.get('name', 'Unknown')}</b>",
            f"Status: {StatisticsFormatter.format_status(user_data.get('status', 'offline'))}",
        ]

        if "joined" in user_data:
            lines.append(f"Joined: {user_data['joined']}")

        return "\n".join(lines)

    @staticmethod
    def format_status(status: str) -> str:
        """Format status with emoji."""
        statuses = {
            "online": "🟢 Online",
            "offline": "🔴 Offline",
            "premium": "👑 Premium",
        }
        return statuses.get(status, "⚪ Unknown")


# ═══════════════════════════════════════════════════════════════════
#                   BUTTON GENERATORS
# ═══════════════════════════════════════════════════════════════════

class ButtonGenerator:
    """Generate button layouts programmatically."""

    @staticmethod
    def create_confirmation_buttons(confirm_text: str = "✅ Confirm",
                                   cancel_text: str = "❌ Cancel") -> List[List]:
        """Create yes/no confirmation buttons."""
        return [
            [confirm_text],
            [cancel_text],
        ]

    @staticmethod
    def create_pagination_buttons(page: int, total_pages: int) -> List[List]:
        """Create pagination buttons."""
        buttons = []
        if page > 1:
            buttons.append("◀️ Previous")
        if page < total_pages:
            buttons.append("Next ▶️")

        return [buttons] if buttons else []

    @staticmethod
    def create_menu_buttons(items: List[str]) -> List[List]:
        """Create menu buttons from items."""
        buttons = []
        for item in items:
            buttons.append([item])
        return buttons


# ═══════════════════════════════════════════════════════════════════
#                      UTILITIES
# ═══════════════════════════════════════════════════════════════════

class TimeFormatter:
    """Format time and dates beautifully."""

    @staticmethod
    def format_duration(seconds: int) -> str:
        """Format duration in human-readable format."""
        if seconds < 60:
            return f"{seconds}s"
        elif seconds < 3600:
            mins = seconds // 60
            secs = seconds % 60
            return f"{mins}m {secs}s"
        else:
            hours = seconds // 3600
            mins = (seconds % 3600) // 60
            return f"{hours}h {mins}m"

    @staticmethod
    def format_datetime(dt: datetime, format_str: str = "%Y-%m-%d %H:%M") -> str:
        """Format datetime."""
        if isinstance(dt, datetime):
            return dt.strftime(format_str)
        return str(dt)

    @staticmethod
    def get_time_greeting() -> str:
        """Get greeting based on time of day."""
        hour = datetime.now().hour
        if hour < 12:
            return "Good Morning! 🌅"
        elif hour < 18:
            return "Good Afternoon! ☀️"
        else:
            return "Good Evening! 🌙"


class StringUtils:
    """String manipulation utilities."""

    @staticmethod
    def truncate(text: str, max_length: int, suffix: str = "...") -> str:
        """Truncate text to max length."""
        if len(text) > max_length:
            return text[:max_length - len(suffix)] + suffix
        return text

    @staticmethod
    def sanitize(text: str) -> str:
        """Sanitize text for safe display."""
        # Remove HTML/special chars
        text = text.replace("<", "&lt;").replace(">", "&gt;")
        return text

    @staticmethod
    def split_message(text: str, max_length: int = 4096) -> List[str]:
        """Split long message into chunks."""
        messages = []
        while text:
            messages.append(text[:max_length])
            text = text[max_length:]
        return messages


# ═══════════════════════════════════════════════════════════════════
#                     EXAMPLE USAGE
# ═══════════════════════════════════════════════════════════════════

if __name__ == "__main__":
    # Test decorations
    print(PremiumDecorations.box_text("ULTRA PREMIUM BOT", "double"))
    print()
    print(PremiumDecorations.create_separator(40, "stars"))
    print()

    # Test progress
    prog = ProgressAnimator(100, "Downloading...")
    for i in range(11):
        prog.update(10)
        print(prog.get_progress_text())
        print()

    # Test formatting
    print(MessageTemplates.success("Bot started successfully!"))
    print()
    print(MessageTemplates.warning("This is a test warning"))
    print()

    # Test time
    print(TimeFormatter.get_time_greeting())
    print(f"Duration: {TimeFormatter.format_duration(3665)}")
