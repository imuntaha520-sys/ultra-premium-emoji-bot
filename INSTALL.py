#!/usr/bin/env python3
"""
╔═════════════════════════════════════════════════════════════════════╗
║   🚀 ULTRA PREMIUM EMOJI BOT v2.0 - INSTALLATION & STARTUP GUIDE  ║
║                     Complete Setup Instructions                     ║
╚═════════════════════════════════════════════════════════════════════╝
"""

import os
import sys
import subprocess
from pathlib import Path

class InstallationGuide:
    """Interactive installation guide."""

    @staticmethod
    def print_banner():
        """Print welcome banner."""
        banner = """
╔════════════════════════════════════════════════════════════════════╗
║                                                                    ║
║         ⭐ ULTRA PREMIUM EMOJI BOT v2.0 ⭐                       ║
║                                                                    ║
║    Your Ultimate Premium Emoji Companion for Telegram             ║
║                                                                    ║
║    🎨 Smart Emoji Converter                                       ║
║    📊 Advanced Analytics                                          ║
║    👑 Complete Admin Panel                                        ║
║    ⚡ Lightning-Fast Processing                                   ║
║    🔐 Enterprise Security                                         ║
║                                                                    ║
╚════════════════════════════════════════════════════════════════════╝
        """
        print(banner)

    @staticmethod
    def print_step(number, title, description=""):
        """Print formatted step."""
        print(f"\n📍 STEP {number}: {title}")
        print("─" * 65)
        if description:
            print(f"   {description}")

    @staticmethod
    def print_subsection(title):
        """Print subsection title."""
        print(f"\n   📌 {title}")

    @staticmethod
    def guide():
        """Print complete installation guide."""

        InstallationGuide.print_banner()

        print("""
╔════════════════════════════════════════════════════════════════════╗
║                    INSTALLATION REQUIREMENTS                       ║
╚════════════════════════════════════════════════════════════════════╝

✅ SYSTEM REQUIREMENTS:
   • Python 3.8 or higher
   • 500MB disk space
   • 100MB RAM minimum (512MB recommended)
   • Stable internet connection

✅ ACCOUNTS & CREDENTIALS NEEDED:
   • Telegram account
   • @BotFather (to create your bot)
   • API credentials from https://my.telegram.org/apps
   • MongoDB account (free tier available)

═════════════════════════════════════════════════════════════════════
""")

        InstallationGuide.print_step(
            1,
            "PREPARE YOUR SYSTEM",
            "Install Python and verify installation"
        )

        print("""
   A. Check Python Version:
      $ python3 --version
      # Should be 3.8 or higher

   B. Install pip (Python package manager):
      # On Ubuntu/Debian:
      $ sudo apt-get install python3-pip

      # On Windows:
      Download from https://bootstrap.pypa.io/get-pip.py
      $ python get-pip.py

   C. Upgrade pip:
      $ pip install --upgrade pip
""")

        InstallationGuide.print_step(
            2,
            "CLONE/DOWNLOAD BOT FILES",
            "Get the bot code to your computer"
        )

        print("""
   Option A: Clone from GitHub (recommended):
      $ git clone https://github.com/yourusername/ultra-premium-emoji-bot.git
      $ cd ultra-premium-emoji-bot

   Option B: Download manually:
      1. Visit: https://github.com/yourusername/ultra-premium-emoji-bot
      2. Click "Code" → "Download ZIP"
      3. Extract the ZIP file
      4. Open terminal in extracted folder
""")

        InstallationGuide.print_step(
            3,
            "GATHER CREDENTIALS",
            "Collect all required Telegram credentials"
        )

        print("""
   📱 GET API_ID & API_HASH:
      1. Go to https://my.telegram.org/apps
      2. Login with your Telegram account
      3. Fill the form (if first time)
      4. You'll see:
         - App api_id (e.g., 12345678)
         - App api_hash (e.g., abc123def456...)
      5. Copy these values

   🤖 GET BOT TOKEN:
      1. Open Telegram and search for @BotFather
      2. Send: /start
      3. Send: /newbot
      4. Follow instructions to name your bot
      5. You'll receive a token: 123456789:ABCdef...
      6. Copy this token

   👤 GET YOUR USER ID:
      1. Open Telegram and search for @userinfobot
      2. Send: /start
      3. You'll see your user ID
      4. Copy this number

   🗄️ SET UP MONGODB:
      1. Visit: https://www.mongodb.com/cloud/atlas
      2. Create a free account
      3. Create a new cluster
      4. Add database user (username & password)
      5. Go to "Connect" and copy connection string
      6. Format: mongodb+srv://username:password@cluster.mongodb.net/dbname

   Your credentials summary:
      API_ID: ___________________
      API_HASH: _________________
      BOT_TOKEN: ________________
      OWNER_ID: __________________
      MONGO_URI: _________________
""")

        InstallationGuide.print_step(
            4,
            "CREATE ENVIRONMENT CONFIGURATION",
            "Setup bot configuration"
        )

        print("""
   Option A: Use Interactive Setup (RECOMMENDED):
      $ python setup.py --setup

      Follow the prompts and enter your credentials.

   Option B: Manual Setup:
      1. Create a file named: .env
      2. Add these lines:

         API_ID=12345678
         API_HASH=abc123def456...
         TOKEN=123456789:ABCdef...
         OWNER_ID=987654321
         MONGO_URI=mongodb+srv://...

      3. Save the file

   Tip: On Windows, use Notepad to create .env file
        On Linux/Mac, use: nano .env
""")

        InstallationGuide.print_step(
            5,
            "INSTALL PYTHON DEPENDENCIES",
            "Install required libraries"
        )

        print("""
   Install all dependencies:
      $ pip install -r requirements.txt

   Or install individually:
      $ pip install telethon>=1.30.0
      $ pip install motor>=3.3.0
      $ pip install pymongo>=4.5.0
      $ pip install python-dotenv>=0.21.0

   Verify installation:
      $ python -c "import telethon; print(telethon.__version__)"
      # Should print version number
""")

        InstallationGuide.print_step(
            6,
            "TEST BOT CONNECTION",
            "Verify everything is working"
        )

        print("""
   Test your setup:
      $ python -c "from ultra_premium_emoji_bot_v2 import *"

   Or run basic diagnostic:
      $ python ultra_premium_emoji_bot_v2.py

   You should see:
      ⭐ ULTRA PREMIUM EMOJI BOT v2.0 - Starting
      ✅ Bot: @your_bot_name
      ✅ Owner ID: 987654321
      ✅ MongoDB: Connected
      🚀 Bot is now running!
""")

        InstallationGuide.print_step(
            7,
            "START USING YOUR BOT",
            "Deploy and use your bot"
        )

        print("""
   A. Test Bot (Local):
      $ python ultra_premium_emoji_bot_v2.py

      The bot will now be running. In Telegram:
      1. Search for your bot (@your_bot_username)
      2. Send /start
      3. Forward a message with emojis to test

   B. Deploy Bot (Production):
      See DEPLOYMENT.md for production setup using:
      • Systemd (Linux)
      • Supervisor (Process manager)
      • Docker (Containerized)
      • Cloud platforms

   C. Keep Bot Running:
      • On Linux: Use systemd service or supervisor
      • On Windows: Use Task Scheduler
      • On Cloud: Use hosting service (Heroku, Railway, etc.)
""")

        print("""
╔════════════════════════════════════════════════════════════════════╗
║                        TROUBLESHOOTING                             ║
╚════════════════════════════════════════════════════════════════════╝

❌ PROBLEM: "ModuleNotFoundError: No module named 'telethon'"
   ✅ SOLUTION: pip install telethon

❌ PROBLEM: "Invalid API_ID or API_HASH"
   ✅ SOLUTION: Double-check credentials from https://my.telegram.org/apps

❌ PROBLEM: "Bot token is invalid"
   ✅ SOLUTION: Get new token from @BotFather

❌ PROBLEM: "Cannot connect to MongoDB"
   ✅ SOLUTION: Verify MONGO_URI, check internet, check IP whitelist

❌ PROBLEM: "Bot doesn't respond"
   ✅ SOLUTION: 
      • Check bot is running: ps aux | grep python
      • Check logs for errors
      • Ensure API credentials are correct
      • Verify MongoDB is connected

❌ PROBLEM: "Permission denied on Linux"
   ✅ SOLUTION: chmod +x ultra_premium_emoji_bot_v2.py

═════════════════════════════════════════════════════════════════════
""")

        print("""
╔════════════════════════════════════════════════════════════════════╗
║                       BOT COMMANDS REFERENCE                       ║
╚════════════════════════════════════════════════════════════════════╝

USER COMMANDS:
  /start          - Start the bot
  /help           - Show help menu
  /post           - Create a post
  /stats          - View your statistics

ADMIN COMMANDS (Owner only):
  /admin          - Open admin panel
  /broadcast      - Send message to all users
  /stats          - View bot statistics
  /ban [id]       - Ban a user
  /unban [id]     - Unban a user
  /maintenance    - Toggle maintenance mode

═════════════════════════════════════════════════════════════════════
""")

        print("""
╔════════════════════════════════════════════════════════════════════╗
║                           NEXT STEPS                               ║
╚════════════════════════════════════════════════════════════════════╝

1. 📖 Read the README.md for detailed information
2. 🚀 Check DEPLOYMENT.md for production setup
3. ⚙️ Review config.py for advanced settings
4. 📞 Visit support channels for help
5. 🌟 Star the repository on GitHub!

═════════════════════════════════════════════════════════════════════

🎉 CONGRATULATIONS!
   Your Ultra Premium Emoji Bot is ready to use!

💬 NEED HELP?
   • GitHub Issues: https://github.com/yourusername/ultra-premium-emoji-bot/issues
   • Telegram Support: @yoursupport
   • Email: your.email@example.com

═════════════════════════════════════════════════════════════════════
""")

    @staticmethod
    def quick_start():
        """Print quick start guide."""
        quick = """
╔════════════════════════════════════════════════════════════════════╗
║                    QUICK START (3 MINUTES)                         ║
╚════════════════════════════════════════════════════════════════════╝

1️⃣  Install Python (if needed):
    Visit: https://python.org/downloads
    Download Python 3.10+
    Run installer

2️⃣  Download Bot:
    $ git clone https://github.com/yourusername/ultra-premium-emoji-bot
    $ cd ultra-premium-emoji-bot

3️⃣  Setup Configuration:
    $ python setup.py --setup
    (Follow interactive prompts)

4️⃣  Install Dependencies:
    $ pip install -r requirements.txt

5️⃣  Run Bot:
    $ python ultra_premium_emoji_bot_v2.py

6️⃣  Test in Telegram:
    • Find @your_bot_username
    • Send /start
    • Forward a message

Done! 🎉

═════════════════════════════════════════════════════════════════════
"""
        print(quick)


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Installation & Startup Guide")
    parser.add_argument("--full", action="store_true", help="Show full guide")
    parser.add_argument("--quick", action="store_true", help="Show quick start")

    args = parser.parse_args()

    if args.quick:
        InstallationGuide.quick_start()
    elif args.full or len(sys.argv) == 1:
        InstallationGuide.guide()
    else:
        parser.print_help()
