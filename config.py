"""
╔═════════════════════════════════════════════════════════════════╗
║        CONFIGURATION FILE - ULTRA PREMIUM EMOJI BOT v2.0       ║
║              Fill these settings before running bot             ║
╚═════════════════════════════════════════════════════════════════╝
"""

import os
from datetime import timezone

UTC = timezone.utc

# ═══════════════════════════════════════════════════════════════════
#                      TELEGRAM API SETTINGS
# ═══════════════════════════════════════════════════════════════════

# Get from https://my.telegram.org/apps
API_ID = int(os.getenv("API_ID", "33678714"))
API_HASH = os.getenv("API_HASH", "2da8051e6c5d07f62bef903f632d3eef")

# Get from @BotFather
BOT_TOKEN = os.getenv("TOKEN", "8899427551:AAHxcxiIIsjbkbkxVd6O8DFoHvwuQsM_C-4")

# Your Telegram user ID (send /id to @userinfobot)
OWNER_ID = int(os.getenv("OWNER_ID", "8591429820"))

# ═══════════════════════════════════════════════════════════════════
#                      MONGODB SETTINGS
# ═══════════════════════════════════════════════════════════════════

MONGO_URI = os.getenv(
    "MONGO_URI",
    "mongodb+srv://shuvohassan_00:shuvohassan%40%4021@gadgetbot1.ycaaj7i.mongodb.net/?retryWrites=true&w=majority&appName=gadgetbot1",
)

# ═══════════════════════════════════════════════════════════════════
#                         BOT SETTINGS
# ═══════════════════════════════════════════════════════════════════

BOT_NAME = "⭐ Ultra Premium Emoji Bot"
BOT_USERNAME = "ultra_premium_emoji_bot"
BOT_VERSION = "2.0.0"

# Message parsing mode
PARSE_MODE = "html"  # or "markdown"

# ═══════════════════════════════════════════════════════════════════
#                     PERFORMANCE SETTINGS
# ═══════════════════════════════════════════════════════════════════

# Maximum message length (Telegram limit is 4096)
MAX_MESSAGE_LENGTH = 4096

# Batch size for database operations
BATCH_SIZE = 50

# Rate limiting (messages per window)
RATE_LIMIT_REQUESTS = 30
RATE_LIMIT_WINDOW = 60  # seconds

# Broadcast rate limit
BROADCAST_DELAY = 0.05  # seconds between each broadcast message

# Request timeout
REQUEST_TIMEOUT = 30  # seconds

# ═══════════════════════════════════════════════════════════════════
#                     FEATURE FLAGS
# ═══════════════════════════════════════════════════════════════════

# Enable/disable features
FEATURES = {
    "emoji_conversion": True,       # Convert normal emojis to premium
    "inline_mode": True,             # Enable inline mode
    "post_creation": True,           # Enable post creation
    "broadcast": True,               # Enable broadcasts
    "admin_panel": True,             # Enable admin panel
    "analytics": True,               # Enable analytics tracking
    "rate_limiting": True,           # Enable rate limiting
    "maintenance_mode": False,       # Maintenance mode (blocks non-admins)
}

# ═══════════════════════════════════════════════════════════════════
#                       TEXT TEMPLATES
# ═══════════════════════════════════════════════════════════════════

MESSAGES = {
    "start": (
        "👋 Welcome, <b>{name}</b>! ✨\n\n"
        "⭐ <b>{bot_name}</b> v{version}\n"
        "🚀 Your Premium Emoji Companion\n\n"
        "💡 Forward any message to convert emojis to premium!"
    ),

    "banned": "🚫 You are banned from this bot.",

    "admin_only": "⛔ This is an admin-only command.",

    "rate_limited": "⏱️ Please wait a moment before trying again.",

    "maintenance": "🛠️ Bot is under maintenance. Try again later.",

    "error": "❌ An error occurred. Please try again later.",

    "success": "✅ Operation completed successfully!",
}

# ═══════════════════════════════════════════════════════════════════
#                    DATABASE COLLECTIONS
# ═══════════════════════════════════════════════════════════════════

COLLECTIONS = {
    "users": "users",           # User profiles & stats
    "channels": "channels",     # Connected channels
    "posts": "posts",           # Created posts
    "settings": "settings",     # Bot settings
    "banned": "banned",         # Banned users
    "stats": "stats",           # Global statistics
    "cache": "cache",           # Cache data
    "logs": "logs",             # Activity logs
}

# ═══════════════════════════════════════════════════════════════════
#                      EMOJI SETTINGS
# ═══════════════════════════════════════════════════════════════════

# Maximum emojis to convert per message
MAX_EMOJIS_PER_MESSAGE = 50

# Emoji replacement character (zero-width space)
EMOJI_PLACEHOLDER = "\u200B"

# ═══════════════════════════════════════════════════════════════════
#                      LOGGING SETTINGS
# ═══════════════════════════════════════════════════════════════════

LOG_LEVEL = "INFO"  # DEBUG, INFO, WARNING, ERROR, CRITICAL

LOG_FORMAT = "%(asctime)s [%(levelname)s] %(name)s: %(message)s"

LOG_FILE = "bot.log"

# ═══════════════════════════════════════════════════════════════════
#                    SECURITY SETTINGS
# ═══════════════════════════════════════════════════════════════════

# Enable user verification before processing
VERIFY_USERS = True

# Auto-ban after X failed login attempts
AUTO_BAN_THRESHOLD = 5

# Require admin confirmation for sensitive operations
REQUIRE_ADMIN_CONFIRMATION = True

# ═══════════════════════════════════════════════════════════════════
#                    ADVANCED SETTINGS
# ═══════════════════════════════════════════════════════════════════

# Cache settings (TTL in seconds)
CACHE_TTL = {
    "user": 3600,          # 1 hour
    "settings": 86400,     # 24 hours
    "channels": 3600,      # 1 hour
}

# Analytics tracking
TRACK_ANALYTICS = True
ANALYTICS_INTERVAL = 3600  # Update analytics every hour

# Enable debug mode (verbose logging)
DEBUG_MODE = os.getenv("DEBUG", "False").lower() == "true"

# ═══════════════════════════════════════════════════════════════════
#                      ENDPOINTS & URLS
# ═══════════════════════════════════════════════════════════════════

# External API endpoints (if any)
EXTERNAL_APIS = {
    "stats": None,
    "emoji_database": None,
}

# ═══════════════════════════════════════════════════════════════════
#                    VALIDATION & LIMITS
# ═══════════════════════════════════════════════════════════════════

# Username validation
VALID_USERNAME_PATTERN = r"^[a-zA-Z0-9_]{5,32}$"

# User ID validation
MIN_USER_ID = 1
MAX_USER_ID = 9999999999

# Message length limits
MIN_MESSAGE_LENGTH = 1
MAX_MESSAGE_LENGTH = 4096

# Post title limits
POST_TITLE_MIN = 1
POST_TITLE_MAX = 100

# ═══════════════════════════════════════════════════════════════════
#                     DEFAULT VALUES
# ═══════════════════════════════════════════════════════════════════

DEFAULTS = {
    "posts_per_page": 10,
    "users_per_page": 20,
    "channels_per_page": 15,
    "posts_page": 1,
    "language": "en",
    "timezone": "UTC",
    "theme": "dark",
}

# ═══════════════════════════════════════════════════════════════════
#                   SUPPORT & HELP
# ═══════════════════════════════════════════════════════════════════

SUPPORT_LINKS = {
    "github": "https://github.com/yourusername/ultra-premium-emoji-bot",
    "support_chat": "https://t.me/yourchannel",
    "docs": "https://docs.example.com",
    "issues": "https://github.com/yourusername/ultra-premium-emoji-bot/issues",
}

# ═══════════════════════════════════════════════════════════════════
#                    ENVIRONMENT CHECK
# ═══════════════════════════════════════════════════════════════════

def check_required_env_vars():
    """Check if all required environment variables are set."""
    required = ["API_ID", "API_HASH", "TOKEN", "OWNER_ID"]
    missing = []

    for var in required:
        if not os.getenv(var):
            missing.append(var)

    if missing:
        raise RuntimeError(
            f"Missing required environment variables: {', '.join(missing)}\n"
            f"Please set them before running the bot."
        )


if __name__ == "__main__":
    print("╔" + "═" * 60 + "╗")
    print("║  Configuration File - Ultra Premium Emoji Bot v2.0      ║")
    print("╚" + "═" * 60 + "╝\n")

    print("Current Configuration:")
    print(f"  Bot Name: {BOT_NAME}")
    print(f"  Bot Username: @{BOT_USERNAME}")
    print(f"  Version: {BOT_VERSION}")
    print(f"  API ID: {API_ID}")
    print(f"  Owner ID: {OWNER_ID}")
    print(f"  Parse Mode: {PARSE_MODE}\n")

    print("Features Enabled:")
    for feature, enabled in FEATURES.items():
        status = "✅" if enabled else "❌"
        print(f"  {status} {feature}")

    print("\nConfiguration loaded successfully!")
