# -*- coding: utf-8 -*-
# simple_main.py - Smart Banking System Simplified Version
import os
import sys

# Fix encoding for Windows
if sys.platform == "win32":
    os.system('chcp 65001 > nul')

class BankingSystem:
    def __init__(self):
        self.users = {
            "admin": {"password": "admin123", "role": "admin", "name": "Administrator"},
            "teller1": {"password": "teller123", "role": "teller", "name": "Teller One"},
            "teller2": {"password": "teller456", "role": "teller", "name": "Teller Two"},
            "client1": {"password": "client123", "role": "client", "name": "Ahmed Client"},
            "client2": {"password": "client456", "role": "client", "name": "Sara Client"}
        }
        self.accounts = {
            "1001": {"name": "Radwan", "balance": 5300.0, "currency": "YER"},
            "1002": {"name": "Ali", "balance": 4000.0, "currency": "YER"},
            "client1": {"name": "Ahmed Client", "balance": 1500.0, "currency": "YER"},
            "client2": {"name": "Sara Client", "balance": 2500.0, "currency": "YER"}
        }
        self.current_user = None
        self.language = "en"  # en or ar
    
    def t(self, key):
        """Simple translation"""
        translations = {
            "en": {
                "title": "Smart Banking System",
                "welcome": "Welcome",
                "login": "Login",
                "exit": "Exit",
                "choose": "Choose",
                "success": "Success",
                "error": "Error",
                "username": "Username",
                "password": "Password",
                "deposit": "Deposit",
                "withdraw": "Withdraw",
                "transfer": "Transfer",
                "balance": "Balance",
                "logout": "Logout",
                "account": "Account",
                "amount": "Amount",
                "currency": "YER",
                "admin": "Admin",
                "teller": "Teller",
                "client": "Client"
            },
            "ar": {
                "title": "النظام البنكي الذكي",
                "welcome": "مرحباً",
                "login": "تسجيل الدخول",
                "exit": "خروج",
                "choose": "اختر",
                "success": "تم بنجاح",
                "error": "خطأ",
                "username": "اسم المستخدم",
                "password": "كلمة المرور",
                "deposit": "إيداع",
                "withdraw": "سحب",
                "transfer": "تحويل",
                "balance": "رصيد",
                "logout": "تسجيل خروج",
                "account": "رقم الحساب",
                "amount": "المبلغ",
                "currency": "ريال",
                "admin": "مسؤول",
                "teller": "كاشير",
                "client": "عميل"
            }
        }
        return translations[self.language].get(key, key)
    
    def clear_screen(self):
        os.system('cls' if sys.platform == 'win32' else 'clear')
    
    def print_header(self):
        self.clear_screen()
        print("="*60)
        print(f"🏦 {self.t('title')}")
        print("="*60)
        if self.current_user:
            role_name = self.t(self.current_user['role'])
            print(f"👤 {self.t('welcome')}, {self.current_user['name']} ({role_name})")
            print("-"*60)
    
    def login(self):
        print(f"\n🔐 {self.t('login')}")
        print("-"*40)
        username = input(f"👤 {self.t('username')}: ").strip()
        password = input(f"🔑 {self.t('password')}: ").strip()
        
        if username in self.users and password == self.users[username]["password"]:
            self.current_user = {
                "username": username,
                "role": self.users[username]["role"],
                "name": self.users[username]["name"]
            }
            print(f"\n✅ {self.t('success')}")
            return True
        print(f"\n❌ {self.t('error')}")
        return False
    
    def deposit(self):
        print(f"\n💰 {self.t('deposit')}")
        print("-"*40)
        account = input(f"{self.t('account')}: ").strip()
        if account in self.accounts:
            try:
                amount = float(input(f"{self.t('amount')}: "))
                if amount > 0:
                    self.accounts[account]['balance'] += amount
                    print(f"\n✅ {self.t('success')}")
                    print(f"{self.t('balance')}: {self.accounts[account]['balance']:.2f} {self.accounts[account]['currency']}")
                else:
                    print(f"\n❌ {self.t('error')}")
            except:
                print(f"\n❌ {self.t('error')}")
        else:
            print(f"\n❌ {self.t('error')}")
    
    def withdraw(self):
        print(f"\n💸 {self.t('withdraw')}")
        print("-"*40)
        account = input(f"{self.t('account')}: ").strip()
        if account in self.accounts:
            try:
                amount = float(input(f"{self.t('amount')}: "))
                if 0 < amount <= self.accounts[account]['balance']:
                    self.accounts[account]['balance'] -= amount
                    print(f"\n✅ {self.t('success')}")
                    print(f"{self.t('balance')}: {self.accounts[account]['balance']:.2f} {self.accounts[account]['currency']}")
                else:
                    print(f"\n❌ {self.t('error')}")
            except:
                print(f"\n❌ {self.t('error')}")
        else:
            print(f"\n❌ {self.t('error')}")
    
    def view_balance(self):
        print(f"\n📊 {self.t('balance')}")
        print("-"*40)
        if self.current_user['role'] == 'client':
            account = self.current_user['username']
        else:
            account = input(f"{self.t('account')}: ").strip()
        
        if account in self.accounts:
            print(f"\n{self.t('account')}: {account}")
            print(f"{self.t('balance')}: {self.accounts[account]['balance']:.2f} {self.accounts[account]['currency']}")
        else:
            print(f"\n❌ {self.t('error')}")
    
    def run(self):
        # Language selection
        print("\n" + "="*60)
        print("🌍 LANGUAGE SELECTION")
        print("="*60)
        print("1. English")
        print("2. العربية")
        choice = input("Choose (1-2): ").strip()
        self.language = "ar" if choice == "2" else "en"
        
        while True:
            self.print_header()
            
            if not self.current_user:
                print(f"\n📋 {self.t('login')}")
                print(f"1. 🔐 {self.t('login')}")
                print(f"2. 🌍 Change Language")
                print(f"3. 🚪 {self.t('exit')}")
                
                cmd = input(f"\n{self.t('choose')}: ").strip()
                
                if cmd == "1":
                    if self.login():
                        continue
                elif cmd == "2":
                    print("\n1. English\n2. العربية")
                    lc = input("Choose (1-2): ")
                    self.language = "ar" if lc == "2" else "en"
                elif cmd == "3":
                    print(f"\n👋 {self.t('exit')}!")
                    break
            else:
                if self.current_user['role'] in ['admin', 'teller']:
                    print(f"\n📋 {self.t('balance')}")
                    print(f"1. 💰 {self.t('deposit')}")
                    print(f"2. 💸 {self.t('withdraw')}")
                    print(f"3. 📊 {self.t('balance')}")
                    print(f"4. 🚪 {self.t('logout')}")
                    
                    cmd = input(f"\n{self.t('choose')}: ").strip()
                    
                    if cmd == "1":
                        self.deposit()
                    elif cmd == "2":
                        self.withdraw()
                    elif cmd == "3":
                        self.view_balance()
                    elif cmd == "4":
                        self.current_user = None
                        print(f"\n👋 {self.t('logout')}!")
                
                elif self.current_user['role'] == 'client':
                    print(f"\n📋 {self.t('balance')}")
                    print(f"1. 📊 {self.t('balance')}")
                    print(f"2. 🚪 {self.t('logout')}")
                    
                    cmd = input(f"\n{self.t('choose')}: ").strip()
                    
                    if cmd == "1":
                        self.view_balance()
                    elif cmd == "2":
                        self.current_user = None
                        print(f"\n👋 {self.t('logout')}!")
                
                input("\nPress Enter to continue...")

if __name__ == "__main__":
    app = BankingSystem()
    try:
        app.run()
    except KeyboardInterrupt:
        print("\n\n👋 Goodbye!")
