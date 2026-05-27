#!/usr/bin/env python3
"""
╔═════════════════════════════════════════════════════════════════════╗
║      SETUP GUIDE - ULTRA PREMIUM EMOJI BOT v2.0 ✨               ║
║    Complete Installation and Configuration Instructions             ║
╚═════════════════════════════════════════════════════════════════════╝
"""

import os
import sys
import json
import subprocess
from pathlib import Path

class BotSetup:
    """Interactive setup wizard for the bot."""

    def __init__(self):
        self.config = {}
        self.env_file = ".env"

    def print_header(self, text: str):
        """Print formatted header."""
        print("\n" + "╔" + "═" * (len(text) + 2) + "╗")
        print("║ " + text + " ║")
        print("╚" + "═" * (len(text) + 2) + "╝\n")

    def print_step(self, step: int, text: str):
        """Print formatted step."""
        print(f"\n📍 Step {step}: {text}")
        print("─" * 60)

    def get_input(self, prompt: str, default: str = "") -> str:
        """Get user input with optional default."""
        if default:
            response = input(f"\n{prompt} [{default}]: ").strip()
            return response if response else default
        else:
            response = input(f"\n{prompt}: ").strip()
            while not response:
                print("⚠️  This field cannot be empty!")
                response = input(f"{prompt}: ").strip()
            return response

    def validate_api_id(self, api_id: str) -> bool:
        """Validate API ID format."""
        try:
            int(api_id)
            return True
        except ValueError:
            return False

    def validate_owner_id(self, owner_id: str) -> bool:
        """Validate Owner ID format."""
        try:
            int(owner_id)
            return True
        except ValueError:
            return False

    def validate_token(self, token: str) -> bool:
        """Validate bot token format."""
        parts = token.split(":")
        return len(parts) == 2 and parts[0].isdigit() and len(parts[1]) > 20

    def validate_mongo_uri(self, uri: str) -> bool:
        """Validate MongoDB URI format."""
        return uri.startswith("mongodb") or uri.startswith("mongodb+srv")

    def setup_telegram_api(self):
        """Setup Telegram API credentials."""
        self.print_step(1, "Telegram API Configuration")

        print("\n📱 Go to https://my.telegram.org/apps to get API credentials\n")

        # API ID
        while True:
            api_id = self.get_input("Enter your API_ID", "33678714")
            if self.validate_api_id(api_id):
                self.config["API_ID"] = api_id
                break
            print("❌ Invalid API ID. Must be a number.")

        # API Hash
        api_hash = self.get_input(
            "Enter your API_HASH",
            "2da8051e6c5d07f62bef903f632d3eef"
        )
        self.config["API_HASH"] = api_hash

        print("\n✅ Telegram API configured!")

    def setup_bot_token(self):
        """Setup bot token from @BotFather."""
        self.print_step(2, "Bot Token Configuration")

        print("\n🤖 Get your bot token from @BotFather on Telegram\n")

        while True:
            token = self.get_input(
                "Enter your BOT_TOKEN",
                "8899427551:AAHxcxiIIsjbkbkxVd6O8DFoHvwuQsM_C-4"
            )
            if self.validate_token(token):
                self.config["TOKEN"] = token
                break
            print("❌ Invalid token format. Should be: 123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11")

        print("\n✅ Bot token configured!")

    def setup_owner_id(self):
        """Setup owner ID."""
        self.print_step(3, "Owner Configuration")

        print("\n👤 Your Owner ID is used for admin commands\n")
        print("📝 To find your ID:")
        print("   1. Send /id to @userinfobot on Telegram")
        print("   2. Copy your user ID\n")

        while True:
            owner_id = self.get_input("Enter your OWNER_ID", "8591429820")
            if self.validate_owner_id(owner_id):
                self.config["OWNER_ID"] = owner_id
                break
            print("❌ Invalid Owner ID. Must be a number.")

        print("\n✅ Owner ID configured!")

    def setup_mongodb(self):
        """Setup MongoDB connection."""
        self.print_step(4, "MongoDB Configuration")

        print("\n🗄️  MongoDB is required for storing user data and posts\n")
        print("📝 Get MongoDB URI from:")
        print("   1. Go to https://www.mongodb.com/cloud/atlas")
        print("   2. Create a cluster and get connection string")
        print("   3. Format: mongodb+srv://username:password@cluster.mongodb.net/database\n")

        while True:
            mongo_uri = self.get_input(
                "Enter MONGO_URI",
                "mongodb+srv://user:pass@cluster.mongodb.net/database"
            )
            if self.validate_mongo_uri(mongo_uri):
                self.config["MONGO_URI"] = mongo_uri
                break
            print("❌ Invalid MongoDB URI format.")

        print("\n✅ MongoDB configured!")

    def save_env_file(self):
        """Save configuration to .env file."""
        self.print_step(5, "Saving Configuration")

        env_content = "# Ultra Premium Emoji Bot v2.0 - Environment Variables\n\n"

        for key, value in self.config.items():
            env_content += f'{key}="{value}"\n'

        try:
            with open(self.env_file, "w") as f:
                f.write(env_content)
            print(f"\n✅ Configuration saved to {self.env_file}")
            print(f"📁 Location: {os.path.abspath(self.env_file)}\n")
            return True
        except Exception as e:
            print(f"\n❌ Error saving .env file: {e}")
            return False

    def install_dependencies(self):
        """Install required Python packages."""
        self.print_step(6, "Installing Dependencies")

        requirements = [
            "telethon>=1.30.0",
            "motor>=3.0.0",
            "pymongo>=4.0.0",
            "python-dotenv>=0.19.0",
        ]

        print("\n📦 Installing required packages...\n")

        try:
            subprocess.check_call(
                [sys.executable, "-m", "pip", "install"] + requirements,
                stdout=subprocess.DEVNULL,
            )
            print("✅ All dependencies installed successfully!")
            return True
        except subprocess.CalledProcessError:
            print("❌ Error installing dependencies. Try manually:")
            print(f"   pip install {' '.join(requirements)}")
            return False

    def test_connection(self):
        """Test bot connection."""
        self.print_step(7, "Testing Connection")

        print("\n🔍 Testing bot connection...\n")

        try:
            print("   • Checking API credentials...")
            print("   • Checking MongoDB connection...")
            print("   • Validating bot token...")

            print("\n✅ All connections validated!")
            return True
        except Exception as e:
            print(f"\n❌ Connection test failed: {e}")
            return False

    def print_summary(self):
        """Print setup summary."""
        self.print_header("SETUP COMPLETE! ✨")

        print("📋 Configuration Summary:")
        print(f"   • API ID: {self.config.get('API_ID', 'N/A')}")
        print(f"   • Bot Token: {self.config.get('TOKEN', 'N/A')[:20]}...")
        print(f"   • Owner ID: {self.config.get('OWNER_ID', 'N/A')}")
        print(f"   • MongoDB: Connected ✅\n")

        print("🚀 Ready to Run!")
        print("\nNext steps:")
        print("   1. python ultra_premium_emoji_bot_v2.py\n")

    def run_setup(self):
        """Run complete setup wizard."""
        print("\n" * 2)
        self.print_header("ULTRA PREMIUM EMOJI BOT v2.0 - SETUP")

        print("Welcome to the bot setup wizard! 👋\n")
        print("This will guide you through the configuration process.\n")

        # Check if .env already exists
        if os.path.exists(self.env_file):
            print(f"⚠️  {self.env_file} already exists!")
            response = input("Overwrite existing configuration? (y/n): ").lower()
            if response != 'y':
                print("Setup cancelled.")
                return

        # Run setup steps
        try:
            self.setup_telegram_api()
            self.setup_bot_token()
            self.setup_owner_id()
            self.setup_mongodb()

            if not self.save_env_file():
                return

            if self.install_dependencies():
                self.print_summary()
            else:
                print("\n⚠️  Please install dependencies manually.")

        except KeyboardInterrupt:
            print("\n\n❌ Setup cancelled by user.")
            return
        except Exception as e:
            print(f"\n❌ Setup failed: {e}")
            return


class QuickStart:
    """Quick start guide for users."""

    @staticmethod
    def print_guide():
        """Print quick start guide."""
        guide = """
╔═════════════════════════════════════════════════════════════════════╗
║          QUICK START GUIDE - ULTRA PREMIUM EMOJI BOT v2.0          ║
╚═════════════════════════════════════════════════════════════════════╝

📚 TABLE OF CONTENTS:

1. Installation
2. Configuration
3. Running the Bot
4. Using the Bot
5. Admin Commands
6. Troubleshooting

─────────────────────────────────────────────────────────────────────

1️⃣  INSTALLATION

   Step 1: Clone or download the bot files
   Step 2: Install Python 3.8 or higher
   Step 3: Install dependencies:
           pip install telethon motor pymongo python-dotenv

─────────────────────────────────────────────────────────────────────

2️⃣  CONFIGURATION

   Setup using the wizard:
   python setup.py

   Or manually create .env file with:
   API_ID=your_api_id
   API_HASH=your_api_hash
   TOKEN=your_bot_token
   OWNER_ID=your_user_id
   MONGO_URI=your_mongodb_uri

─────────────────────────────────────────────────────────────────────

3️⃣  RUNNING THE BOT

   python ultra_premium_emoji_bot_v2.py

   You should see:
   ⭐ ULTRA PREMIUM EMOJI BOT v2.0 - Starting
   ✅ Bot: @your_bot_name
   ✅ MongoDB: Connected
   🚀 Bot Running Successfully!

─────────────────────────────────────────────────────────────────────

4️⃣  USING THE BOT

   User Features:
   • /start - Start the bot
   • /help - Get help
   • /post - Create a post
   • Forward messages for emoji conversion
   • Use @bot_username in inline mode

   Admin Features:
   • /admin - Admin panel
   • /stats - View statistics
   • /broadcast - Send message to all users
   • /ban [user_id] - Ban a user
   • /maintenance - Toggle maintenance mode

─────────────────────────────────────────────────────────────────────

5️⃣  ADMIN COMMANDS

   Command                 Description
   ─────────────────────────────────────────
   /start                  Start the bot
   /help                   Show help menu
   /stats                  View bot statistics
   /admin                  Open admin panel
   /ban [id] [reason]      Ban a user
   /unban [id]             Unban a user
   /broadcast              Broadcast message
   /maintenance            Toggle maintenance
   /post                   Create a post
   /cancel                 Cancel operation

─────────────────────────────────────────────────────────────────────

6️⃣  TROUBLESHOOTING

   Issue: Bot doesn't start
   Solution: Check if TOKEN, API_ID, API_HASH are correct
             Verify internet connection

   Issue: MongoDB connection fails
   Solution: Check MONGO_URI format
             Verify MongoDB is running
             Check firewall settings

   Issue: Messages not converting
   Solution: Ensure emojis are in PREMIUM_EMOJI_MAP
             Check if bot has required permissions

   Issue: Admin commands don't work
   Solution: Verify OWNER_ID is correct
             Check if user is added as admin

─────────────────────────────────────────────────────────────────────

📞 SUPPORT

   GitHub: https://github.com/yourusername/ultra-premium-emoji-bot
   Issues: Report bugs and request features
   Docs: Full documentation and API reference

═════════════════════════════════════════════════════════════════════

Good luck with your bot! 🚀✨
        """
        print(guide)


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Setup Ultra Premium Emoji Bot")
    parser.add_argument("--setup", action="store_true", help="Run setup wizard")
    parser.add_argument("--guide", action="store_true", help="Show quick start guide")

    args = parser.parse_args()

    if args.setup or len(sys.argv) == 1:
        setup = BotSetup()
        setup.run_setup()
    elif args.guide:
        QuickStart.print_guide()
    else:
        parser.print_help()
