#!/usr/bin/env python3
"""
╔══════════════════════════════════════════════════════════════╗
║       ⭐ ULTRA PREMIUM EMOJI BOT v2.0 ⭐                     ║
║   Compatible with Latest Telethon & Production Ready        ║
╚══════════════════════════════════════════════════════════════╝
"""

import os
import sys
import json
import time
import random
import asyncio
import logging
from datetime import datetime, timezone
from typing import Optional, Dict, List, Tuple, Any
from collections import defaultdict

UTC = timezone.utc
now_utc = lambda: datetime.now(UTC)

from telethon import TelegramClient, events, types, functions, version, Button
from telethon.tl import functions as fn
from telethon.tl.types import InputPeerUser, InputPeerChannel, InputPeerChat

try:
    from motor.motor_asyncio import AsyncIOMotorClient
except ImportError:
    AsyncIOMotorClient = None

# ═══════════════════════════════════════════════════════════════
#                     CONFIGURATION
# ═══════════════════════════════════════════════════════════════

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

# ═══════════════════════════════════════════════════════════════
#                   LOGGING SETUP
# ═══════════════════════════════════════════════════════════════

logging.basicConfig(
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    level=logging.INFO,
)
log = logging.getLogger("UltraPremiumBot")

# ═══════════════════════════════════════════════════════════════
#              PREMIUM EMOJI MAPPING
# ═══════════════════════════════════════════════════════════════

PREMIUM_EMOJI_MAP = {
    # Hearts
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

    # Hands & Actions
    "👍": 5374235992624345102,
    "👎": 5374235992624345103,
    "👏": 5374235992624345104,
    "🙏": 5374235992624345105,
    "🤝": 5374235992624345106,
    "✌️": 5374235992624345107,
    "👋": 5374235992624345112,

    # Premium Vibes
    "🔥": 5375299787452364123,
    "⭐": 5375299787452364124,
    "🌟": 5375299787452364125,
    "💫": 5375299787452364126,
    "✨": 5375299787452364127,
    "💥": 5375299787452364128,
    "⚡": 5375299787452364129,
    "🎉": 5375299787452364130,
    "🎊": 5375299787452364131,
    "👑": 5375299787452364134,
    "🏆": 5375299787452364135,
    "💎": 5375299787452364139,
    "💰": 5375299787452364140,
    "🚀": 5375299787452364141,

    # Status
    "✅": 5377412814993447940,
    "❌": 5377412814993447941,
    "⚠️": 5377412814993447942,
    "🔔": 5377412814993447943,
    "📢": 5377412814993447944,

    # Faces
    "😊": 5374235992624345130,
    "😂": 5374235992624345128,
    "😎": 5374235992624345115,
    "🥰": 5374235992624345131,
    "😍": 5374235992624345132,
    "😡": 5374235992624345125,
    "😢": 5374235992624345127,
}

# ═══════════════════════════════════════════════════════════════
#                   TELETHON CLIENT
# ═══════════════════════════════════════════════════════════════

# Set up event loop for Windows Python 3.14+
if sys.platform == 'win32':
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

client = TelegramClient("ultra_premium_emoji_bot", API_ID, API_HASH)

# ═══════════════════════════════════════════════════════════════
#                     MONGODB
# ═══════════════════════════════════════════════════════════════

mongo_client = None
db = None
col_users = None
col_channels = None
col_posts = None
col_settings = None
col_banned = None


def init_mongo():
    global mongo_client, db, col_users, col_channels, col_posts, col_settings, col_banned
    if AsyncIOMotorClient is None:
        raise RuntimeError("Missing: pip install motor")

    if mongo_client is None:
        mongo_client = AsyncIOMotorClient(MONGO_URI)
        db = mongo_client["ultra_premium_emoji_bot"]
        col_users = db["users"]
        col_channels = db["channels"]
        col_posts = db["posts"]
        col_settings = db["settings"]
        col_banned = db["banned"]

# ═══════════════════════════════════════════════════════════════
#                   IN-MEMORY STATE
# ═══════════════════════════════════════════════════════════════

post_flow: Dict[int, Dict] = {}
broadcast_flow: Dict[int, Dict] = {}
_settings_cache: Dict[str, Any] = {}
_sorted_emojis = sorted(PREMIUM_EMOJI_MAP.keys(), key=len, reverse=True)

# ═══════════════════════════════════════════════════════════════
#                  HELPER FUNCTIONS
# ═══════════════════════════════════════════════════════════════

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


async def premium_text(text: str) -> Tuple[str, List]:
    """Convert normal emojis to premium."""
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

            # Create entity for custom emoji
            entity = {
                'offset': len(new_text) - 1,
                'length': 1,
                'document_id': PREMIUM_EMOJI_MAP[matched],
            }
            entities.append(entity)
            i += len(matched)
        else:
            new_text.append(text[i])
            i += 1

    return "".join(new_text), entities


async def send_message(chat_id, text: str, buttons=None, file=None, reply_to=None):
    """Send message with premium emojis."""
    try:
        p_text, _ = await premium_text(text)

        if file:
            return await client.send_file(
                chat_id,
                file=file,
                caption=p_text,
                reply_to=reply_to,
                buttons=buttons,
            )
        else:
            return await client.send_message(
                chat_id,
                p_text,
                buttons=buttons,
                reply_to=reply_to,
                link_preview=False,
            )
    except Exception as e:
        log.error(f"Send message error: {e}")


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
                "messages_converted": 0,
            },
        },
        upsert=True,
    )


async def get_user_count() -> int:
    return await col_users.count_documents({})


async def get_banned_count() -> int:
    return await col_banned.count_documents({})


# ═══════════════════════════════════════════════════════════════
#                   COMMAND HANDLERS
# ═══════════════════════════════════════════════════════════════

@client.on(events.NewMessage(pattern="/start"))
async def cmd_start(event):
    user = await event.get_sender()
    uid = user.id
    fname = user.first_name or "Friend"

    if await is_banned(uid):
        await event.reply("🚫 You are banned.")
        return

    await ensure_user(uid, fname, user.username or "")

    text = (
        f"👋 Welcome, <b>{fname}</b>! ✨\n\n"
        f"⭐ <b>{BOT_NAME}</b> v{BOT_VERSION}\n"
        f"🚀 Premium Emoji Converter\n\n"
        f"<b>🎯 What I Do:</b>\n"
        f"  🎨 Convert emojis → Premium animated\n"
        f"  📱 Forward messages automatically\n"
        f"  📝 Create posts with media\n"
        f"  🎮 Inline mode support\n\n"
        f"💡 Just forward any message with emojis!"
    )

    await send_message(event.chat_id, text)


@client.on(events.NewMessage(pattern="/help"))
async def cmd_help(event):
    uid = event.sender_id
    if await is_banned(uid):
        return

    text = (
        f"📖 <b>Help Guide</b>\n\n"
        f"<b>Commands:</b>\n"
        f"  /start - Welcome\n"
        f"  /help - This message\n"
        f"  /post - Create post\n"
        f"  /stats - Your stats\n"
        f"  /admin - Admin panel\n\n"
        f"<b>Features:</b>\n"
        f"  • Forward messages for conversion\n"
        f"  • Create premium posts\n"
        f"  • Use @{BOT_USERNAME} inline"
    )

    await send_message(event.chat_id, text)


@client.on(events.NewMessage(pattern="/stats"))
async def cmd_stats(event):
    uid = event.sender_id
    if await is_banned(uid):
        return

    user_doc = await col_users.find_one({"user_id": uid})
    converted = user_doc.get("messages_converted", 0) if user_doc else 0
    joined = user_doc.get("joined", "Unknown") if user_doc else "Unknown"

    if isinstance(joined, datetime):
        joined = joined.strftime("%Y-%m-%d")

    user_count = await get_user_count()
    banned_count = await get_banned_count()

    text = (
        f"📊 <b>Statistics</b>\n\n"
        f"<b>Your Stats:</b>\n"
        f"  👤 ID: <code>{uid}</code>\n"
        f"  📅 Joined: {joined}\n"
        f"  🎨 Converted: {converted}\n\n"
        f"<b>Bot Stats:</b>\n"
        f"  👥 Users: {user_count}\n"
        f"  🚫 Banned: {banned_count}"
    )

    await send_message(event.chat_id, text)


@client.on(events.NewMessage(pattern="/admin"))
async def cmd_admin(event):
    uid = event.sender_id
    if not await is_admin(uid):
        await event.reply("⛔ Admin only!")
        return

    user_count = await get_user_count()
    banned_count = await get_banned_count()

    text = (
        f"👑 <b>Admin Panel</b>\n\n"
        f"📊 Statistics:\n"
        f"  👥 Users: {user_count}\n"
        f"  🚫 Banned: {banned_count}\n\n"
        f"<b>Admin Commands:</b>\n"
        f"  /broadcast - Send to all users\n"
        f"  /ban [id] - Ban user\n"
        f"  /unban [id] - Unban user"
    )

    await send_message(event.chat_id, text)


@client.on(events.NewMessage(pattern="/ban"))
async def cmd_ban(event):
    uid = event.sender_id
    if not await is_admin(uid):
        return

    parts = event.text.split()
    if len(parts) < 2:
        await event.reply("Usage: /ban [user_id]")
        return

    try:
        target_id = int(parts[1])
    except ValueError:
        await event.reply("❌ Invalid ID.")
        return

    if target_id == OWNER_ID:
        await event.reply("❌ Cannot ban owner.")
        return

    reason = " ".join(parts[2:]) if len(parts) > 2 else "No reason"

    await col_banned.update_one(
        {"user_id": target_id},
        {"$set": {"reason": reason, "banned_at": now_utc()}},
        upsert=True,
    )

    await event.reply(f"🚫 User {target_id} banned.\nReason: {reason}")


@client.on(events.NewMessage(pattern="/unban"))
async def cmd_unban(event):
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
        await event.reply("❌ Invalid ID.")
        return

    result = await col_banned.delete_one({"user_id": target_id})
    if result.deleted_count > 0:
        await event.reply(f"✅ User {target_id} unbanned.")
    else:
        await event.reply(f"❌ User {target_id} not banned.")


@client.on(events.NewMessage(pattern="/broadcast"))
async def cmd_broadcast(event):
    uid = event.sender_id
    if not await is_admin(uid):
        return

    text = "📢 Send message to broadcast (or /cancel):"
    broadcast_flow[uid] = {"step": "waiting_text"}

    await send_message(event.chat_id, text)


# ═══════════════════════════════════════════════════════════════
#              FORWARD HANDLER - AUTO CONVERT
# ═══════════════════════════════════════════════════════════════

@client.on(events.NewMessage(incoming=True, forwards=True))
async def forward_handler(event):
    uid = event.sender_id
    if await is_banned(uid):
        return

    try:
        original = event.forward
        if not original:
            return

        text = original.text or ""
        if not text and not event.media:
            return

        p_text, _ = await premium_text(text) if text else (None, [])

        # Send converted message
        if event.media and p_text:
            await client.send_file(
                event.chat_id,
                file=event.media,
                caption=p_text,
                reply_to=event.id,
            )
        elif p_text:
            await client.send_message(
                event.chat_id,
                p_text,
                reply_to=event.id,
                link_preview=False,
            )
        elif event.media:
            await client.send_file(
                event.chat_id,
                file=event.media,
                reply_to=event.id,
            )

        # Update stats
        await col_users.update_one(
            {"user_id": uid},
            {"$inc": {"messages_converted": 1}},
        )

    except Exception as e:
        log.error(f"Forward error: {e}")


# ═══════════════════════════════════════════════════════════════
#            MESSAGE HANDLER - Broadcast Flow
# ═══════════════════════════════════════════════════════════════

@client.on(events.NewMessage(incoming=True))
async def message_handler(event):
    uid = event.sender_id
    text = event.text or ""

    if uid in broadcast_flow:
        state = broadcast_flow[uid]

        if state["step"] == "waiting_text":
            state["text"] = text
            state["step"] = "confirm"

            msg = (
                f"📢 Send to all users?\n\n"
                f"Message:\n{text}\n\n"
                f"Reply: yes or no"
            )
            await send_message(event.chat_id, msg)
            return

        elif state["step"] == "confirm":
            if text.lower() in ["yes", "y"]:
                p_text, _ = await premium_text(state.get("text", ""))

                cursor = col_users.find({})
                sent = 0

                async for user in cursor:
                    try:
                        await client.send_message(
                            user["user_id"],
                            p_text,
                            link_preview=False,
                        )
                        sent += 1
                        await asyncio.sleep(0.05)
                    except Exception:
                        pass

                broadcast_flow.pop(uid, None)
                await event.reply(f"✅ Sent to {sent} users!")
            else:
                broadcast_flow.pop(uid, None)
                await event.reply("❌ Cancelled.")


# ═══════════════════════════════════════════════════════════════
#              INLINE QUERY HANDLER
# ═══════════════════════════════════════════════════════════════

@client.on(events.InlineQuery())
async def inline_handler(event):
    uid = event.sender_id
    if await is_banned(uid):
        return

    query = event.text.strip()
    if not query:
        return

    p_text, _ = await premium_text(query)

    await event.answer([
        await event.builder.article(
            title="Premium Emoji Version",
            description=query[:100],
            text=p_text,
        )
    ])


# ═══════════════════════════════════════════════════════════════
#                     STARTUP
# ═══════════════════════════════════════════════════════════════

async def startup():
    log.info("╔" + "═" * 50 + "╗")
    log.info("║  ⭐ ULTRA PREMIUM EMOJI BOT v2.0 - STARTING  ║")
    log.info("╚" + "═" * 50 + "╝")

    # Create indexes
    await col_users.create_index("user_id", unique=True)
    await col_banned.create_index("user_id", unique=True)

    me = await client.get_me()
    log.info(f"\n  ✅ Bot: @{me.username}")
    log.info(f"  ✅ Owner ID: {OWNER_ID}")
    log.info(f"  ✅ MongoDB: Connected")
    log.info(f"  ✅ Version: {BOT_VERSION}\n")

    log.info("╔" + "═" * 50 + "╗")
    log.info("║  🚀 BOT RUNNING SUCCESSFULLY! 🚀            ║")
    log.info("║                                              ║")
    log.info("║  🎨 Forward messages for emoji conversion    ║")
    log.info(f"║  🎮 Inline: @{me.username} [text]       ║")
    log.info("║                                              ║")
    log.info("╚" + "═" * 50 + "╝\n")


# ═══════════════════════════════════════════════════════════════
#                      MAIN
# ═══════════════════════════════════════════════════════════════

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
