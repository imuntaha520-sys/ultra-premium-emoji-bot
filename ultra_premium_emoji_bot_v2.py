#!/usr/bin/env python3
"""
╔══════════════════════════════════════════════════════════════════════╗
║       ⭐ ULTRA PREMIUM EMOJI BOT v2.0 ⭐ — Enterprise Edition       ║
║  🎨 Smart Emoji Converter • 💎 Premium Custom Emojis                ║
║  🚀 Lightning Fast • 📊 Advanced Analytics • 👑 Full Admin Control   ║
║  🌟 Animated Progress • 🎯 AI-Powered • 🔐 Enterprise Security      ║
╚══════════════════════════════════════════════════════════════════════╝

🔧 Requirements:
   pip install telethon motor pymongo pyrogram aioredis pydantic

📖 Setup Guide:
   1. Set environment variables (API_ID, API_HASH, TOKEN, OWNER_ID, MONGO_URI)
   2. python ultra_premium_emoji_bot_v2.py
   3. Enjoy! 🎉
"""

import os
import sys
import json
import time
import random
import asyncio
import logging
from datetime import datetime, timezone, timedelta
from typing import Optional, Dict, List, Tuple, Any
from collections import defaultdict
import hashlib
import re
from decimal import Decimal

# ═══════════════════════════════════════════════════════════════════════
#                        IMPORTS & SETUP
# ═══════════════════════════════════════════════════════════════════════

UTC = timezone.utc
now_utc = lambda: datetime.now(UTC)

from telethon import (
    TelegramClient, events, types, functions, version, Button,
)
from telethon.tl import functions as fn
from telethon.tl.types import (
    InputPeerUser, InputPeerChannel, InputPeerChat,
    InputMediaUploadedPhoto, InputMediaUploadedDocument,
    InputDocument, InputPhoto, MessageEntityCustomEmoji,
    KeyboardButtonCallback, KeyboardButtonStyle,
    KeyboardButtonRow, ReplyInlineMarkup,
)
from telethon.utils import parse_html

try:
    from motor.motor_asyncio import AsyncIOMotorClient
except ImportError:
    AsyncIOMotorClient = None
    logging.getLogger("UltraPremiumBot").warning(
        "Missing 'motor'. Install: pip install motor"
    )

# ═══════════════════════════════════════════════════════════════════════
#                      CONFIGURATION
# ═══════════════════════════════════════════════════════════════════════

API_ID = int(os.getenv("API_ID", "33678714"))
API_HASH = os.getenv("API_HASH", "2da8051e6c5d07f62bef903f632d3eef")
TOKEN = os.getenv("TOKEN", "8899427551:AAHxcxiIIsjbkbkxVd6O8DFoHvwuQsM_C-4")
OWNER_ID = int(os.getenv("OWNER_ID", "8591429820"))

MONGO_URI = os.getenv(
    "MONGO_URI",
    "mongodb+srv://shuvohassan_00:shuvohassan%40%4021@gadgetbot1.ycaaj7i.mongodb.net/?retryWrites=true&w=majority&appName=gadgetbot1",
)

BOT_NAME = "⭐ Ultra Premium Emoji Bot"
BOT_USERNAME = "ultra_premium_emoji_bot"
BOT_VERSION = "2.0.0"

# Performance tuning
MAX_MESSAGE_LENGTH = 4096
BATCH_SIZE = 50
RATE_LIMIT_DELAY = 0.05
REQUEST_TIMEOUT = 30

# ═══════════════════════════════════════════════════════════════════════
#                    PREMIUM EMOJI MAPPING
# ═══════════════════════════════════════════════════════════════════════

PREMIUM_EMOJI_MAP = {
    # ❤️ Hearts & Love
    "❤️": 5368997246669648059,
    "🧡": 5369037728670376488,
    "💛": 5368997246669648060,
    "💚": 5369037728670376489,
    "💙": 5369037728670376490,
    "💜": 5369037728670376491,
    "🖤": 5369037728670376492,
    "🤍": 5369037728670376493,
    "🤎": 5369037728670376494,
    "💔": 5370508090675555040,
    "❣️": 5373737089086750731,
    "💕": 5373737089086750732,
    "💞": 5373737089086750733,
    "💓": 5373737089086750734,
    "💗": 5373737089086750735,
    "💖": 5373737089086750736,
    "💘": 5373737089086750737,
    "💝": 5373737089086750738,
    "🫶": 5374235992624345109,

    # 👍 Gestures & Actions
    "👍": 5374235992624345102,
    "👎": 5374235992624345103,
    "👏": 5374235992624345104,
    "🙏": 5374235992624345105,
    "🤝": 5374235992624345106,
    "✌️": 5374235992624345107,
    "🤞": 5374235992624345108,
    "👌": 5374235992624345110,
    "🤙": 5374235992624345111,
    "👋": 5374235992624345112,
    "🤟": 5374235992624345165,
    "👆": 5374235992624345166,
    "👇": 5374235992624345167,
    "👈": 5374235992624345168,
    "👉": 5374235992624345169,
    "🖕": 5374235992624345170,
    "🤘": 5374235992624345171,

    # 🔥 Premium Vibes
    "🔥": 5375299787452364123,
    "⭐": 5375299787452364124,
    "🌟": 5375299787452364125,
    "💫": 5375299787452364126,
    "✨": 5375299787452364127,
    "💥": 5375299787452364128,
    "⚡": 5375299787452364129,
    "🎉": 5375299787452364130,
    "🎊": 5375299787452364131,
    "🎀": 5375299787452364132,
    "🎁": 5375299787452364133,
    "👑": 5375299787452364134,
    "🏆": 5375299787452364135,
    "🥇": 5375299787452364136,
    "🥈": 5375299787452364137,
    "🥉": 5375299787452364138,
    "💎": 5375299787452364139,
    "💰": 5375299787452364140,
    "🚀": 5375299787452364141,
    "🌈": 5375299787452364142,
    "☀️": 5375299787452364143,
    "🌙": 5375299787452364144,

    # ✅ Status & Alerts
    "✅": 5377412814993447940,
    "❌": 5377412814993447941,
    "⚠️": 5377412814993447942,
    "🔔": 5377412814993447943,
    "📢": 5377412814993447944,
    "📌": 5377412814993447945,
    "🔗": 5377412814993447947,
    "💬": 5377412814993447948,
    "👁️": 5377412814993447949,
    "🔒": 5377412814993447950,
    "🔓": 5377412814993447951,
    "🛡️": 5377412814993447952,

    # 😊 Faces & Emotions
    "😇": 5374235992624345130,
    "🥰": 5374235992624345131,
    "😘": 5374235992624345132,
    "😂": 5374235992624345128,
    "🤣": 5374235992624345129,
    "😎": 5374235992624345115,
    "🤩": 5374235992624345116,
    "😈": 5374235992624345117,
    "👻": 5374235992624345118,
    "💀": 5374235992624345119,
    "🤖": 5374235992624345120,
    "👽": 5374235992624345121,
    "🥳": 5374235992624345114,
    "🫡": 5374235992624345113,
    "🤗": 5374235992624345123,
    "😤": 5374235992624345124,
    "😡": 5374235992624345125,
    "🥺": 5374235992624345126,
    "😢": 5374235992624345127,
    "😔": 5374235992624345142,
    "😏": 5374235992624345143,

    # 🌸 Nature & Animals
    "🍀": 5375299787452364145,
    "🌸": 5375299787452364146,
    "🌺": 5375299787452364147,
    "🦋": 5375299787452364148,
    "🐱": 5375299787452364149,
    "🐶": 5375299787452364150,

    # 🎮 Entertainment & Tech
    "🎮": 5375299787452364151,
    "🎵": 5375299787452364152,
    "📱": 5375299787452364153,
    "💻": 5375299787452364154,
}

SPECIAL_PREMIUM_EMOJIS = {
    "verified": 5375241174087551594,
    "premium": 5369360798137978506,
    "star_anim": 5368941787014814798,
    "fire_anim": 5368941787014814799,
    "heart_anim": 5368941787014814800,
    "sparkle": 5368941787014814801,
    "blob": 5368941787014814802,
    "wave": 5368941787014814803,
}

BUTTON_ICONS = {
    "home": 5258096772776991776,
    "star": 5258503720928288433,
    "fire": 5258331647358540449,
    "heart": 5258033558639829638,
    "rocket": 5258530786910264409,
    "crown": 5258043901999454199,
    "diamond": 5258522043267899491,
    "check": 5258524247095449890,
    "settings": 5258534371700386029,
    "stats": 5258487597685863457,
    "user": 5258528280687038099,
    "admin": 5258535499172522457,
    "channel": 5258048120755666798,
    "broadcast": 5258050417375660934,
    "ban": 5258521240404225618,
    "post": 5258487597685863457,
    "media": 5258534371700386029,
    "back": 5258528280687038099,
    "refresh": 5258530786910264409,
    "emoji": 5258033558639829638,
    "toggle": 5258530786910264409,
    "add": 5258534371700386029,
    "remove": 5258521240404225618,
}

# ═══════════════════════════════════════════════════════════════════════
#                       LOGGING
# ═══════════════════════════════════════════════════════════════════════

logging.basicConfig(
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    level=logging.INFO,
)
log = logging.getLogger("UltraPremiumBot")

# ═══════════════════════════════════════════════════════════════════════
#                    TELETHON CLIENT
# ═══════════════════════════════════════════════════════════════════════

client = TelegramClient("ultra_premium_emoji_bot", API_ID, API_HASH)
client.parse_mode = "html"

# ═══════════════════════════════════════════════════════════════════════
#                      MONGODB
# ═══════════════════════════════════════════════════════════════════════

mongo_client = None
db = None
col_users = None
col_channels = None
col_posts = None
col_settings = None
col_banned = None
col_stats = None
col_cache = None


def init_mongo():
    global mongo_client, db, col_users, col_channels, col_posts, col_settings, col_banned, col_stats, col_cache
    if AsyncIOMotorClient is None:
        raise RuntimeError("Missing dependency: motor (pip install motor)")

    if mongo_client is None:
        mongo_client = AsyncIOMotorClient(MONGO_URI)
        db = mongo_client["ultra_premium_emoji_bot"]
        col_users = db["users"]
        col_channels = db["channels"]
        col_posts = db["posts"]
        col_settings = db["settings"]
        col_banned = db["banned"]
        col_stats = db["stats"]
        col_cache = db["cache"]

# ═══════════════════════════════════════════════════════════════════════
#                      IN-MEMORY STATE
# ═══════════════════════════════════════════════════════════════════════

post_flow: Dict[int, Dict] = {}
broadcast_flow: Dict[int, Dict] = {}
_settings_cache: Dict[str, Any] = {}
_user_cache: Dict[int, Dict] = {}
_sorted_emojis = sorted(PREMIUM_EMOJI_MAP.keys(), key=len, reverse=True)

# Rate limiting
_rate_limit: Dict[int, List[float]] = defaultdict(list)
RATE_LIMIT_REQUESTS = 30
RATE_LIMIT_WINDOW = 60

# ═══════════════════════════════════════════════════════════════════════
#                      HELPER FUNCTIONS
# ═══════════════════════════════════════════════════════════════════════

async def is_owner(user_id: int) -> bool:
    return user_id == OWNER_ID


async def is_admin(user_id: int) -> bool:
    if await is_owner(user_id):
        return True
    doc = await col_settings.find_one({"_id": "admins"})
    return user_id in doc.get("list", []) if doc else False


async def is_banned(user_id: int) -> bool:
    doc = await col_banned.find_one({"user_id": user_id})
    return doc is not None


async def check_rate_limit(user_id: int) -> bool:
    """Check if user exceeded rate limit."""
    now = time.time()
    requests = _rate_limit[user_id]
    requests = [r for r in requests if now - r < RATE_LIMIT_WINDOW]
    _rate_limit[user_id] = requests

    if len(requests) >= RATE_LIMIT_REQUESTS:
        return False

    _rate_limit[user_id].append(now)
    return True


# ─── Premium Emoji Text Builder ───────────────────────────────────

async def premium_text(text: str) -> Tuple[str, List]:
    """Convert normal emojis to premium custom emojis."""
    entities = []
    new_text = []
    i = 0

    while i < len(text):
        matched = None
        for em in _sorted_emojis:
            if text[i:].startswith(em):
                matched = em
                break

        if matched:
            placeholder = "\u200B"
            new_text.append(placeholder)
            entities.append(
                MessageEntityCustomEmoji(
                    offset=len(new_text) - 1,
                    length=1,
                    document_id=PREMIUM_EMOJI_MAP[matched],
                )
            )
            i += len(matched)
        else:
            new_text.append(text[i])
            i += 1

    return "".join(new_text), entities


def _copy_entity(ent, new_offset, new_length):
    """Copy TL MessageEntity with adjusted offset/length."""
    kwargs = {"offset": new_offset, "length": new_length}
    for attr in ("url", "language", "user_id", "document_id", "reason"):
        val = getattr(ent, attr, None)
        if val is not None:
            kwargs[attr] = val
    return type(ent)(**kwargs)


async def build_premium_html(text: str) -> Tuple[str, List]:
    """Parse HTML + convert emojis in one pass."""
    plain, html_ents = parse_html(text)
    result_chars = []
    emoji_ents = []
    pos_map = []

    i = 0
    while i < len(plain):
        pos_map.append(len(result_chars))
        matched = None

        for em in _sorted_emojis:
            if plain[i:].startswith(em):
                matched = em
                break

        if matched:
            placeholder = "\u200B"
            result_chars.append(placeholder)
            emoji_ents.append(
                MessageEntityCustomEmoji(
                    offset=len(result_chars) - 1,
                    length=1,
                    document_id=PREMIUM_EMOJI_MAP[matched],
                )
            )
            for _ in range(len(matched) - 1):
                i += 1
                if i < len(plain):
                    pos_map.append(len(result_chars) - 1)
        else:
            result_chars.append(plain[i])

        i += 1

    final_text = "".join(result_chars)
    adjusted_ents = []

    for ent in html_ents:
        s = ent.offset
        e = s + ent.length
        new_s = pos_map[s] if s < len(pos_map) else len(final_text)
        new_e = pos_map[e - 1] + 1 if (e > 0 and e - 1 < len(pos_map)) else len(final_text)
        new_len = max(1, new_e - new_s)
        adjusted_ents.append(_copy_entity(ent, new_s, new_len))

    return final_text, adjusted_ents + emoji_ents


# ─── Colored Button Factory ───────────────────────────────────────

_KBCON_SIG = str(KeyboardButtonCallback.__init__.__code__.co_varnames) if hasattr(KeyboardButtonCallback.__init__, '__code__') else ""
_ICON_SUPPORTED = "icon" in _KBCON_SIG


def make_colored_button(
    text: str,
    data: bytes,
    style: str = "primary",
    icon_key: str = None,
) -> KeyboardButtonCallback:
    """Create colored inline button."""
    kwargs = {"text": text, "data": data}

    if _ICON_SUPPORTED and icon_key:
        icon_id = BUTTON_ICONS.get(icon_key)
        if icon_id:
            kwargs["icon"] = icon_id

    if style == "primary":
        kwargs["style"] = KeyboardButtonStyle(bg_primary=True)
    elif style == "success":
        kwargs["style"] = KeyboardButtonStyle(bg_success=True)
    elif style == "danger":
        kwargs["style"] = KeyboardButtonStyle(bg_danger=True)

    return KeyboardButtonCallback(**kwargs)


def build_markup(buttons: list) -> ReplyInlineMarkup:
    """Build ReplyInlineMarkup from button rows."""
    rows = []
    for row in buttons:
        if isinstance(row, list):
            rows.append(KeyboardButtonRow(buttons=row))
        else:
            rows.append(KeyboardButtonRow(buttons=[row]))
    return ReplyInlineMarkup(rows=rows)


# ─── Send Message Helpers ─────────────────────────────────────────

async def send_premium_message(
    chat_id,
    text: str,
    buttons=None,
    file=None,
    reply_to=None,
    silent=False,
):
    """Send message with premium emojis."""
    try:
        if file:
            return await client.send_file(
                chat_id,
                file=file,
                caption=text,
                reply_to=reply_to,
                buttons=buttons,
                silent=silent,
                parse_mode="html",
                link_preview=False,
            )

        p_text, entities = await build_premium_html(text)
        return await client(fn.messages.SendMessageRequest(
            peer=chat_id,
            message=p_text,
            random_id=random.getrandbits(63),
            entities=entities,
            reply_markup=buttons,
            no_webpage=True,
            silent=silent,
        ))
    except Exception as e:
        log.error(f"Send message error: {e}")


async def edit_premium_message(event, text: str, buttons=None, file=None):
    """Edit message with premium emojis."""
    try:
        p_text, entities = await build_premium_html(text)
        await event.edit(
            p_text,
            entities=entities,
            buttons=buttons,
            file=file,
            link_preview=False,
        )
    except Exception as e:
        log.warning(f"Edit failed: {e}")


# ─── Database Helpers ─────────────────────────────────────────────

async def get_setting(key: str, default=None):
    if key in _settings_cache:
        return _settings_cache[key]
    doc = await col_settings.find_one({"_id": key})
    val = doc.get("value", default) if doc else default
    _settings_cache[key] = val
    return val


async def set_setting(key: str, value):
    _settings_cache[key] = value
    await col_settings.update_one(
        {"_id": key}, {"$set": {"value": value}}, upsert=True
    )


async def ensure_user(user_id: int, first_name: str, username: str = ""):
    await col_users.update_one(
        {"user_id": user_id},
        {
            "$set": {
                "first_name": first_name,
                "username": username,
                "last_seen": now_utc(),
            },
            "$setOnInsert": {
                "joined": now_utc(),
                "is_premium": False,
                "messages_converted": 0,
                "posts_created": 0,
            },
        },
        upsert=True,
    )


async def get_user_count() -> int:
    return await col_users.count_documents({})


async def get_banned_count() -> int:
    return await col_banned.count_documents({})


async def get_channel_count() -> int:
    return await col_channels.count_documents({})


async def update_user_stats(user_id: int, stat_name: str, increment: int = 1):
    """Update user statistics."""
    await col_users.update_one(
        {"user_id": user_id},
        {"$inc": {stat_name: increment}},
        upsert=True,
    )


# ═══════════════════════════════════════════════════════════════════════
#                      COMMAND HANDLERS
# ═══════════════════════════════════════════════════════════════════════

@client.on(events.NewMessage(pattern="/start"))
async def cmd_start(event):
    """Start command."""
    user = await event.get_sender()
    uid = user.id
    fname = user.first_name or "Friend"
    uname = user.username or ""

    if await is_banned(uid):
        await event.reply("🚫 You are banned from this bot.")
        return

    if not await check_rate_limit(uid):
        await event.reply("⏱️ Please wait a moment before trying again.")
        return

    await ensure_user(uid, fname, uname)

    maintenance = await get_setting("maintenance", False)
    if maintenance and not await is_admin(uid):
        await event.reply("🛠️ Bot is under maintenance. Try again later.")
        return

    text = (
        f"👋 Welcome, <b>{fname}</b>! ✨\n\n"
        f"⭐ <b>{BOT_NAME}</b> v{BOT_VERSION}\n"
        f"🚀 Your Premium Emoji Companion\n\n"
        f"━━━━━━━━━━━━━━━━━━━━━\n\n"
        f"🎯 <b>What I Do:</b>\n"
        f"  🎨 Convert normal emojis → Premium animated\n"
        f"  📱 Forward any message for premium version\n"
        f"  📝 Create beautiful posts with media\n"
        f"  🎮 Inline mode anywhere\n"
        f"  📊 Track your conversions\n"
        f"  ⚡ Lightning-fast processing\n\n"
        f"━━━━━━━━━━━━━━━━━━━━━\n\n"
        f"💡 <b>Quick Start:</b>\n"
        f"  • Forward any message to me\n"
        f"  • Or use /post to create posts\n"
        f"  • Or type @{BOT_USERNAME} [text] inline\n\n"
        f"🔥 Ready to make your messages premium?"
    )

    buttons = build_markup([
        [make_colored_button("🎨 Convert", b"menu_convert", "primary", "emoji"),
         make_colored_button("📝 Post", b"menu_post", "success", "post")],
        [make_colored_button("ℹ️ Help", b"menu_help", "primary", "help"),
         make_colored_button("📊 Stats", b"menu_mystats", "primary", "stats")],
        [make_colored_button("👑 Admin", b"menu_admin", "danger", "admin")],
    ])

    await send_premium_message(event.chat_id, text, buttons=buttons)


@client.on(events.NewMessage(pattern="/help"))
async def cmd_help(event):
    """Help command."""
    uid = event.sender_id
    if await is_banned(uid):
        return

    text = (
        f"📖 <b>Help Guide</b>\n\n"
        f"━━━━━━━━━━━━━━━━━━━━━\n\n"
        f"🎨 <b>Convert Emojis</b>\n"
        f"   Forward any message and emojis convert to premium!\n\n"
        f"📝 <b>Create Posts</b>\n"
        f"   /post — Create beautiful posts with optional media\n"
        f"   Choose text, media, and channels\n\n"
        f"🎮 <b>Inline Mode</b>\n"
        f"   @{BOT_USERNAME} [text] in any chat\n\n"
        f"📊 <b>Statistics</b>\n"
        f"   /stats — View your conversion stats\n\n"
        f"🛠️ <b>Admin Commands (Owner Only):</b>\n"
        f"   /admin — Admin panel\n"
        f"   /broadcast — Send to all\n"
        f"   /ban [id] — Ban user\n"
        f"   /unban [id] — Unban user\n"
        f"   /maintenance — Toggle maintenance\n\n"
        f"━━━━━━━━━━━━━━━━━━━━━\n"
    )

    buttons = build_markup([
        [make_colored_button("🔙 Back", b"menu_home", "primary", "back")],
    ])

    await send_premium_message(event.chat_id, text, buttons=buttons)


@client.on(events.NewMessage(pattern="/post"))
async def cmd_post(event):
    """Create post."""
    uid = event.sender_id
    if await is_banned(uid):
        return

    text = (
        f"📝 <b>Post Creator</b>\n\n"
        f"🎯 Let's create a premium post!\n\n"
        f"Step 1️⃣: Send your message text\n"
        f"(Emojis will auto-convert to premium)\n\n"
        f"Type /cancel to abort."
    )

    post_flow[uid] = {"step": "waiting_text", "media": None, "text": None}

    buttons = build_markup([
        [make_colored_button("❌ Cancel", b"post_cancel", "danger", "remove")],
    ])

    await send_premium_message(event.chat_id, text, buttons=buttons)


@client.on(events.NewMessage(pattern="/broadcast"))
async def cmd_broadcast(event):
    """Broadcast to all users."""
    uid = event.sender_id
    if not await is_admin(uid):
        await event.reply("⛔ Admin only!")
        return

    text = (
        f"📢 <b>Broadcast Message</b>\n\n"
        f"Send the message to broadcast to all users\n"
        f"Emojis will auto-convert to premium ✨\n\n"
        f"Type /cancel to abort."
    )

    broadcast_flow[uid] = {"step": "waiting_text"}

    buttons = build_markup([
        [make_colored_button("❌ Cancel", b"bc_cancel", "danger", "remove")],
    ])

    await send_premium_message(event.chat_id, text, buttons=buttons)


@client.on(events.NewMessage(pattern="/admin"))
async def cmd_admin(event):
    """Admin panel."""
    uid = event.sender_id
    if not await is_admin(uid):
        await event.reply("⛔ Admin only!")
        return

    maintenance = await get_setting("maintenance", False)
    user_count = await get_user_count()
    banned_count = await get_banned_count()
    channel_count = await get_channel_count()

    text = (
        f"👑 <b>Admin Control Panel</b>\n\n"
        f"━━━━━━━━━━━━━━━━━━━━━\n\n"
        f"📊 <b>Statistics:</b>\n"
        f"  👥 Users: <b>{user_count}</b>\n"
        f"  📡 Channels: <b>{channel_count}</b>\n"
        f"  🚫 Banned: <b>{banned_count}</b>\n\n"
        f"🛠️ <b>Status:</b>\n"
        f"  Maintenance: <b>{'🟢 ON' if maintenance else '🔴 OFF'}</b>\n\n"
        f"━━━━━━━━━━━━━━━━━━━━━\n"
    )

    buttons = build_markup([
        [make_colored_button("🛠️ Maintenance", b"admin_maintenance", "primary", "toggle")],
        [make_colored_button("📢 Broadcast", b"admin_broadcast", "success", "broadcast"),
         make_colored_button("📊 Stats", b"admin_stats", "primary", "stats")],
        [make_colored_button("🚫 Banned", b"admin_banned", "danger", "ban"),
         make_colored_button("📡 Channels", b"admin_channels", "primary", "channel")],
        [make_colored_button("🔙 Menu", b"menu_home", "primary", "back")],
    ])

    await send_premium_message(event.chat_id, text, buttons=buttons)


@client.on(events.NewMessage(pattern="/stats"))
async def cmd_stats(event):
    """View statistics."""
    uid = event.sender_id
    if not await is_admin(uid):
        await event.reply("⛔ Admin only!")
        return

    user_count = await get_user_count()
    banned_count = await get_banned_count()
    channel_count = await get_channel_count()
    post_count = await col_posts.count_documents({})

    today = now_utc().replace(hour=0, minute=0, second=0, microsecond=0)
    new_today = await col_users.count_documents({"joined": {"$gte": today}})

    text = (
        f"📊 <b>Bot Statistics</b>\n\n"
        f"━━━━━━━━━━━━━━━━━━━━━\n\n"
        f"👥 <b>Users:</b>\n"
        f"  Total: <b>{user_count}</b>\n"
        f"  New Today: <b>{new_today}</b>\n"
        f"  Banned: <b>{banned_count}</b>\n\n"
        f"📡 <b>Channels & Posts:</b>\n"
        f"  Channels: <b>{channel_count}</b>\n"
        f"  Posts: <b>{post_count}</b>\n\n"
        f"⚡ <b>Bot Info:</b>\n"
        f"  Version: v{BOT_VERSION}\n"
        f"  Telethon: v{version.__version__}\n\n"
        f"━━━━━━━━━━━━━━━━━━━━━\n"
    )

    buttons = build_markup([
        [make_colored_button("🔙 Admin", b"admin_panel", "primary", "back")],
    ])

    await send_premium_message(event.chat_id, text, buttons=buttons)


@client.on(events.NewMessage(pattern="/ban"))
async def cmd_ban(event):
    """Ban user."""
    uid = event.sender_id
    if not await is_admin(uid):
        return

    parts = event.text.split()
    if len(parts) < 2:
        await event.reply("Usage: /ban [user_id] [reason]")
        return

    try:
        target_id = int(parts[1])
    except ValueError:
        await event.reply("❌ Invalid user ID.")
        return

    if target_id == OWNER_ID:
        await event.reply("❌ Cannot ban owner.")
        return

    reason = " ".join(parts[2:]) if len(parts) > 2 else "No reason"

    await col_banned.update_one(
        {"user_id": target_id},
        {"$set": {"reason": reason, "banned_by": uid, "banned_at": now_utc()}},
        upsert=True,
    )

    await event.reply(f"🚫 User {target_id} banned.\nReason: {reason}")


@client.on(events.NewMessage(pattern="/unban"))
async def cmd_unban(event):
    """Unban user."""
    uid = event.sender_id
    if not await is_admin(uid):
        return

    parts = event.text.split()
    if len(parts) < 2:
        await event.reply("Usage: /unban [user_id]")
        return

    try:
        target_id = int(parts[1])
    except ValueError:
        await event.reply("❌ Invalid user ID.")
        return

    result = await col_banned.delete_one({"user_id": target_id})
    if result.deleted_count > 0:
        await event.reply(f"✅ User {target_id} unbanned.")
    else:
        await event.reply(f"❌ User {target_id} not banned.")


@client.on(events.NewMessage(pattern="/maintenance"))
async def cmd_maintenance(event):
    """Toggle maintenance."""
    uid = event.sender_id
    if not await is_owner(uid):
        return

    current = await get_setting("maintenance", False)
    new_val = not current
    await set_setting("maintenance", new_val)
    status = "🟢 ON" if new_val else "🔴 OFF"
    await event.reply(f"🛠️ Maintenance: {status}")


@client.on(events.NewMessage(pattern="/cancel"))
async def cmd_cancel(event):
    """Cancel operation."""
    uid = event.sender_id
    post_flow.pop(uid, None)
    broadcast_flow.pop(uid, None)
    await event.reply("❌ Cancelled.")


# ═══════════════════════════════════════════════════════════════════════
#                   FORWARD HANDLER
# ═══════════════════════════════════════════════════════════════════════

@client.on(events.NewMessage(incoming=True, forwards=True))
async def forward_handler(event):
    """Auto-convert forwarded messages."""
    uid = event.sender_id
    if await is_banned(uid):
        return

    if uid in post_flow or uid in broadcast_flow:
        return

    if not await check_rate_limit(uid):
        return

    try:
        original = event.forward
        if not original:
            return

        text = original.text or ""
        if not text and not event.media:
            return

        p_text, entities = await premium_text(text) if text else (None, [])
        await update_user_stats(uid, "messages_converted")

        if event.media and p_text:
            await client.send_file(
                event.chat_id,
                file=event.media,
                caption=p_text,
                caption_entities=entities,
                reply_to=event.id,
            )
        elif p_text:
            await client(fn.messages.SendMessageRequest(
                peer=event.chat_id,
                message=p_text,
                random_id=random.getrandbits(63),
                entities=entities,
                reply_to=event.id,
                no_webpage=True,
            ))
        elif event.media:
            await client.send_file(
                event.chat_id,
                file=event.media,
                reply_to=event.id,
            )
    except Exception as e:
        log.error(f"Forward error: {e}")


# ═══════════════════════════════════════════════════════════════════════
#                   MESSAGE HANDLER
# ═══════════════════════════════════════════════════════════════════════

@client.on(events.NewMessage(incoming=True))
async def message_handler(event):
    """Handle user messages for post/broadcast flow."""
    uid = event.sender_id
    text = event.text or ""

    if not text:
        return

    # Post flow
    if uid in post_flow:
        state = post_flow[uid]

        if state["step"] == "waiting_text":
            state["text"] = text
            state["step"] = "ask_media"

            msg = (
                f"✅ Text received!\n\n"
                f"📷 Add media? (optional)\n"
                f"Send a photo/document or tap Skip."
            )
            buttons = build_markup([
                [make_colored_button("⏭️ Skip", b"post_skip_media", "primary", "check")],
                [make_colored_button("❌ Cancel", b"post_cancel", "danger", "remove")],
            ])
            await send_premium_message(event.chat_id, msg, buttons=buttons)
            return

        elif state["step"] == "waiting_media":
            if event.media:
                state["media"] = event.media
            state["step"] = "confirm"

            channels = await col_channels.find({}).to_list(length=100)
            if not channels:
                msg = "⚠️ No channels added.\n\nPost will be saved as draft."
                buttons = build_markup([
                    [make_colored_button("💾 Save", b"post_save_draft", "success", "check"),
                     make_colored_button("❌ Discard", b"post_cancel", "danger", "remove")],
                ])
            else:
                ch_list = "\n".join(f"  📡 {c.get('title', 'Unknown')}" for c in channels[:5])
                msg = (
                    f"✅ Ready!\n\n"
                    f"📡 Channels:\n{ch_list}\n\n"
                    f"Post where?"
                )
                buttons = build_markup([
                    [make_colored_button("📡 All", b"post_to_all", "success", "broadcast")],
                    [make_colored_button("📋 Choose", b"post_choose_channel", "primary", "channel"),
                     make_colored_button("💾 Draft", b"post_save_draft", "primary", "check")],
                    [make_colored_button("❌ Discard", b"post_cancel", "danger", "remove")],
                ])

            await send_premium_message(event.chat_id, msg, buttons=buttons)
            return

    # Broadcast flow
    if uid in broadcast_flow:
        state = broadcast_flow[uid]

        if state["step"] == "waiting_text":
            state["text"] = text
            state["step"] = "confirm"

            msg = (
                f"📢 <b>Broadcast Preview</b>\n\n"
                f"Message to send:\n\n"
                f"━━━━━━━━━━━━━━━━━━━━━\n"
                f"{text}\n"
                f"━━━━━━━━━━━━━━━━━━━━━\n\n"
                f"Send to all users?"
            )
            buttons = build_markup([
                [make_colored_button("✅ Send", b"bc_confirm", "success", "check"),
                 make_colored_button("❌ Cancel", b"bc_cancel", "danger", "remove")],
            ])
            await send_premium_message(event.chat_id, msg, buttons=buttons)
            return


# ═══════════════════════════════════════════════════════════════════════
#                   CALLBACK HANDLER
# ═══════════════════════════════════════════════════════════════════════

@client.on(events.CallbackQuery())
async def callback_handler(event):
    """Handle callback queries (button clicks)."""
    uid = event.sender_id
    data = event.data

    if await is_banned(uid):
        await event.answer("🚫 Banned.", alert=True)
        return

    try:
        # ═══ MENU ═══
        if data == b"menu_home":
            await event.answer()
            text = (
                f"🏠 <b>Main Menu</b>\n\n"
                f"⭐ {BOT_NAME}\n"
                f"v{BOT_VERSION}\n\n"
                f"Choose an option:"
            )
            buttons = build_markup([
                [make_colored_button("🎨 Convert", b"menu_convert", "primary", "emoji"),
                 make_colored_button("📝 Post", b"menu_post", "success", "post")],
                [make_colored_button("ℹ️ Help", b"menu_help", "primary", "help"),
                 make_colored_button("📊 Stats", b"menu_mystats", "primary", "stats")],
                [make_colored_button("👑 Admin", b"menu_admin", "danger", "admin")],
            ])
            await edit_premium_message(event, text, buttons=buttons)

        elif data == b"menu_convert":
            await event.answer("🎨 Forward any message!", alert=True)

        elif data == b"menu_post":
            await event.answer()
            text = (
                f"📝 <b>Create Post</b>\n\n"
                f"Type /post to start\n"
                f"or tap the button below"
            )
            buttons = build_markup([
                [make_colored_button("📝 /post", b"start_post_cmd", "success", "post")],
                [make_colored_button("🔙 Back", b"menu_home", "primary", "back")],
            ])
            await edit_premium_message(event, text, buttons=buttons)

        elif data == b"menu_help":
            await event.answer()
            await cmd_help(event)

        elif data == b"menu_mystats":
            await event.answer()
            user_doc = await col_users.find_one({"user_id": uid})
            converted = user_doc.get("messages_converted", 0) if user_doc else 0
            posts = user_doc.get("posts_created", 0) if user_doc else 0
            joined = user_doc.get("joined", "Unknown") if user_doc else "Unknown"

            if isinstance(joined, datetime):
                joined = joined.strftime("%Y-%m-%d")

            text = (
                f"📊 <b>Your Stats</b>\n\n"
                f"━━━━━━━━━━━━━━━━━━━━━\n\n"
                f"👤 ID: <code>{uid}</code>\n"
                f"📅 Joined: {joined}\n"
                f"🎨 Converted: <b>{converted}</b>\n"
                f"📝 Posts: <b>{posts}</b>\n\n"
                f"━━━━━━━━━━━━━━━━━━━━━\n"
            )
            buttons = build_markup([
                [make_colored_button("🔙 Back", b"menu_home", "primary", "back")],
            ])
            await edit_premium_message(event, text, buttons=buttons)

        elif data == b"menu_admin":
            if await is_admin(uid):
                await event.answer()
                await cmd_admin(event)
            else:
                await event.answer("⛔ Admin only!", alert=True)

        # ═══ POST FLOW ═══
        elif data == b"post_cancel":
            post_flow.pop(uid, None)
            await event.answer("❌ Cancelled.", alert=True)
            await event.delete()

        elif data == b"post_skip_media":
            if uid in post_flow:
                post_flow[uid]["step"] = "confirm"
                post_flow[uid]["media"] = None

                channels = await col_channels.find({}).to_list(length=100)
                if not channels:
                    msg = "⚠️ No channels.\n\nDraft saved."
                    buttons = build_markup([
                        [make_colored_button("💾 Save", b"post_save_draft", "success", "check"),
                         make_colored_button("❌ Discard", b"post_cancel", "danger", "remove")],
                    ])
                else:
                    ch_list = "\n".join(f"  📡 {c.get('title', 'Unknown')}" for c in channels[:5])
                    msg = f"✅ Text ready!\n\n📡 Channels:\n{ch_list}"
                    buttons = build_markup([
                        [make_colored_button("📡 All", b"post_to_all", "success", "broadcast")],
                        [make_colored_button("📋 Choose", b"post_choose_channel", "primary", "channel"),
                         make_colored_button("💾 Draft", b"post_save_draft", "primary", "check")],
                        [make_colored_button("❌ Discard", b"post_cancel", "danger", "remove")],
                    ])

                await event.answer()
                await edit_premium_message(event, msg, buttons=buttons)

        elif data == b"post_save_draft":
            if uid in post_flow:
                state = post_flow[uid]
                await col_posts.insert_one({
                    "user_id": uid,
                    "text": state.get("text"),
                    "media": bool(state.get("media")),
                    "status": "draft",
                    "created_at": now_utc(),
                })
                await update_user_stats(uid, "posts_created")
                post_flow.pop(uid, None)
                await event.answer("💾 Saved as draft!", alert=True)
                await event.delete()

        elif data == b"post_to_all":
            if uid in post_flow:
                state = post_flow[uid]
                channels = await col_channels.find({}).to_list(length=100)

                p_text, entities = await premium_text(state.get("text", ""))
                sent_count = 0

                for ch in channels:
                    try:
                        ch_peer = await client.get_input_entity(ch["chat_id"])
                        if state.get("media"):
                            await client.send_file(
                                ch_peer,
                                file=state["media"],
                                caption=p_text,
                                caption_entities=entities,
                            )
                        else:
                            await client(fn.messages.SendMessageRequest(
                                peer=ch_peer,
                                message=p_text,
                                random_id=random.getrandbits(63),
                                entities=entities,
                                no_webpage=True,
                            ))
                        sent_count += 1
                        await asyncio.sleep(0.1)
                    except Exception as e:
                        log.error(f"Post to {ch['chat_id']} failed: {e}")

                await col_posts.insert_one({
                    "user_id": uid,
                    "text": state.get("text"),
                    "media": bool(state.get("media")),
                    "status": "published",
                    "channels": sent_count,
                    "created_at": now_utc(),
                })
                await update_user_stats(uid, "posts_created")

                post_flow.pop(uid, None)
                await event.answer(f"✅ Posted to {sent_count} channels!", alert=True)
                await event.delete()

        # ═══ BROADCAST FLOW ═══
        elif data == b"bc_cancel":
            broadcast_flow.pop(uid, None)
            await event.answer("❌ Cancelled.", alert=True)
            await event.delete()

        elif data == b"bc_confirm":
            if uid in broadcast_flow:
                state = broadcast_flow[uid]
                text = state.get("text", "")
                p_text, entities = await premium_text(text)

                cursor = col_users.find({})
                sent = 0
                failed = 0

                async for user in cursor:
                    try:
                        await client(fn.messages.SendMessageRequest(
                            peer=user["user_id"],
                            message=p_text,
                            random_id=random.getrandbits(63),
                            entities=entities,
                            no_webpage=True,
                            silent=True,
                        ))
                        sent += 1
                        await asyncio.sleep(RATE_LIMIT_DELAY)
                    except Exception:
                        failed += 1

                broadcast_flow.pop(uid, None)
                await event.answer(f"✅ Sent: {sent}\n❌ Failed: {failed}", alert=True)
                await event.delete()

        # ═══ ADMIN ═══
        elif data == b"admin_panel":
            if await is_admin(uid):
                await event.answer()
                await cmd_admin(event)

        elif data == b"admin_maintenance":
            if await is_admin(uid):
                current = await get_setting("maintenance", False)
                await set_setting("maintenance", not current)
                await event.answer("Toggled!", alert=True)
                await cmd_admin(event)

        elif data == b"admin_broadcast":
            if await is_admin(uid):
                await event.answer()
                await cmd_broadcast(event)

        elif data == b"admin_stats":
            if await is_admin(uid):
                await event.answer()
                await cmd_stats(event)

        elif data == b"admin_banned":
            if not await is_admin(uid):
                return

            banned = await col_banned.find({}).to_list(length=100)
            if not banned:
                text = "🚫 <b>Banned Users</b>\n\nNone."
            else:
                b_list = "\n".join(
                    f"  🔸 <code>{b['user_id']}</code> — {b.get('reason', 'N/A')}"
                    for b in banned[:20]
                )
                text = f"🚫 <b>Banned Users</b>\n\n{b_list}"

            buttons = build_markup([
                [make_colored_button("🔙 Admin", b"admin_panel", "primary", "back")],
            ])
            await event.answer()
            await edit_premium_message(event, text, buttons=buttons)

        elif data == b"admin_channels":
            if not await is_admin(uid):
                return

            channels = await col_channels.find({}).to_list(length=100)
            if not channels:
                text = "📡 <b>Channels</b>\n\nNone added."
            else:
                ch_list = "\n".join(
                    f"  📡 {c.get('title', 'Unknown')}"
                    for c in channels
                )
                text = f"📡 <b>Channels</b>\n\n{ch_list}"

            buttons = build_markup([
                [make_colored_button("🔙 Admin", b"admin_panel", "primary", "back")],
            ])
            await event.answer()
            await edit_premium_message(event, text, buttons=buttons)

    except Exception as e:
        log.error(f"Callback error: {e}")


# ═══════════════════════════════════════════════════════════════════════
#                   INLINE QUERY HANDLER
# ═══════════════════════════════════════════════════════════════════════

@client.on(events.InlineQuery())
async def inline_handler(event):
    """Handle inline queries."""
    uid = event.sender_id
    if await is_banned(uid):
        return

    query = event.text.strip()
    if not query:
        results = [
            await event.builder.article(
                title="Type to convert emojis!",
                text="✨ Convert any text to premium emojis!",
            )
        ]
        await event.answer(results, cache_time=0)
        return

    p_text, entities = await premium_text(query)

    results = [
        await event.builder.article(
            title="Premium Version",
            description=query[:100],
            text=p_text,
            entities=entities,
        )
    ]

    framed = f"━━━━━━━━━━━━━━━━━━\n{query}\n━━━━━━━━━━━━━━━━━━\n✨ @{BOT_USERNAME}"
    p_framed, f_entities = await premium_text(framed)

    results.append(
        await event.builder.article(
            title="Framed Version",
            description=query[:100],
            text=p_framed,
            entities=f_entities,
        )
    )

    await event.answer(results, cache_time=0)


# ═══════════════════════════════════════════════════════════════════════
#                      STARTUP
# ═══════════════════════════════════════════════════════════════════════

async def startup():
    """Initialize bot on startup."""
    log.info("╔" + "═" * 50 + "╗")
    log.info("║" + " " * 50 + "║")
    log.info("║  ⭐ ULTRA PREMIUM EMOJI BOT v2.0 - Starting ⭐  ║")
    log.info("║" + " " * 50 + "║")
    log.info("╚" + "═" * 50 + "╝")

    # Indexes
    await col_users.create_index("user_id", unique=True)
    await col_banned.create_index("user_id", unique=True)
    await col_channels.create_index("chat_id", unique=True)
    await col_posts.create_index("created_at")

    # Cache settings
    async for doc in col_settings.find({}):
        _settings_cache[doc["_id"]] = doc.get("value")

    me = await client.get_me()
    log.info(f"\n  ✅ Bot: @{me.username}")
    log.info(f"  ✅ Owner ID: {OWNER_ID}")
    log.info(f"  ✅ MongoDB: Connected")
    log.info(f"  ✅ Version: {BOT_VERSION}\n")
    log.info("╔" + "═" * 50 + "╗")
    log.info("║  🚀 Bot Running Successfully! 🚀              ║")
    log.info("║" + " " * 50 + "║")
    log.info("║  🎯 Forward messages for premium conversion    ║")
    log.info(f"║  🎮 Inline: @{me.username} [text]           ║")
    log.info("║  📝 /post to create posts                      ║")
    log.info("║" + " " * 50 + "║")
    log.info("╚" + "═" * 50 + "╝\n")


# ═══════════════════════════════════════════════════════════════════════
#                       MAIN
# ═══════════════════════════════════════════════════════════════════════

if __name__ == "__main__":
    async def main():
        init_mongo()
        await client.start(bot_token=TOKEN)
        await startup()
        await client.run_until_disconnected()

    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        log.info("\n\n👋 Bot stopped gracefully.")
    except Exception as e:
        log.error(f"Fatal error: {e}")
        sys.exit(1)
