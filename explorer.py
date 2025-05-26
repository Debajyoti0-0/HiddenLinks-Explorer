############################################
#author : Debajyoti0-0                     #
#version: 1.0.0                            #                                
#Github : https://github.com/Debajyoti0-0/ #
############################################

# coding: utf-8
#!/usr/bin/env python
import pandas as pd
import os
from rich.console import Console
from rich.table import Table

# Setup rich console
console = Console()

# Banner for HiddenLinks Explorer
banner = """
 +--------------------------------------------------------------------------
   :". /  /  /    
   :.-". /  /       ▄ .▄▪  ·▄▄▄▄  ·▄▄▄▄  ▄▄▄ . ▐ ▄ ▄▄▌  ▪   ▐ ▄ ▄ •▄ .▄▄ · 
   : _.-". /       ██▪▐███ ██▪ ██ ██▪ ██ ▀▄.▀·•█▌▐███•  ██ •█▌▐██▌▄▌▪▐█ ▀. 
   :"  _.-".       ██▀▐█▐█·▐█· ▐█▌▐█· ▐█▌▐▀▀▪▄▐█▐▐▌██▪  ▐█·▐█▐▐▌▐▀▀▄·▄▀▀▀█▄
   :-""     ".     ██▌▐▀▐█▌██. ██ ██. ██ ▐█▄▄▌██▐█▌▐█▌▐▌▐█▌██▐█▌▐█.█▌▐█▄▪▐█
   :               ▀▀▀ ·▀▀▀▀▀▀▀▀• ▀▀▀▀▀•  ▀▀▀ ▀▀ █▪.▀▀▀ ▀▀▀▀▀ █▪·▀  ▀ ▀▀▀▀ 
   :  
 ^.-.^             [🔎] Explore the Depths of the Dark Web Safely.🕸️ 🌐
'^\+/^`
'/`"'\`

author : Debajyoti0-0
version: 1.0                                                            
Github : https://github.com/Debajyoti0-0/
"""
# Load the Excel file
file_path = 'sites.xlsx'
try:
    df = pd.read_excel(file_path)
except Exception as e:
    print(f"[!] Error loading Excel file: {e}")
    exit(1)

# Define categories
categories = {
    1: "Markets", 2: "Search", 3: "Forums", 4: "News", 5: "Security", 6: "Communications", 7: "Crypto",
    8: "Tools", 9: "Dark Net Collection", 10: "Communication", 11: "Cryptocurrency", 12: "File sharing",
    13: "Protect yourself", 14: "Search engines", 15: "Archives", 16: "Editor's picks", 17: "Introduction Points",
    18: "Financial Services", 19: "Commercial Services", 20: "Anonymity & Security", 21: "Blogs / Essays / Wikis",
    22: "Email / Messaging", 23: "Social Networks", 24: "Forums / Boards / Chans", 25: "Whistleblowing",
    26: "H/P/A/W/V/C", 27: "Hosting, website developing", 28: "File Uploaders", 29: "Audio / Music / Streams",
    30: "Videos / Movies / TV", 31: "Books", 32: "Drugs", 33: "Uncategorized", 34: "Finnish / Suomi",
    35: "French", 36: "German", 37: "Italian", 38: "Japanese", 39: "Chinese",
    40: "Polish", 41: "Russian", 42: "Spanish", 43: "Portuguese", 44: "Swedish",
    45: "Chat centric services (IRC)", 46: "SILC", 47: "TorChatAddresses", 48: "OnionCatAddresses",
    49: "BitcoinSeeding", 50: "The Hidden Wiki - deep web, dark web, onion links", 51: "Tor project",
    52: "Privacy chat, mail, file upload", 53: "Hosting", 54: "Forums and News", 55: "Popular", 56: "Leaks"
}

def print_categories():
    os.system("cls" if os.name == "nt" else "clear")
    console.print(banner, style="bold green")
    console.print("[bold cyan]\n======= HiddenLinks Explorer: Category Browser =======[/bold cyan]")
    console.print("[bold cyan]Select a category number (00 to EXIT):[/bold cyan]\n")

    formatted_items = [f"{num:02d}: {name}" for num, name in sorted(categories.items())]

    cols = 3
    rows = (len(formatted_items) + cols - 1) // cols
    for row in range(rows):
        line = ""
        for col in range(cols):
            idx = row + col * rows
            if idx < len(formatted_items):
                line += f"{formatted_items[idx]:<40}"
        console.print(line)

def extract_by_category():
    # Detect relevant columns
    url_col = next((c for c in df.columns if "url" in c.lower()), None)
    cat_col = next((c for c in df.columns if "category" in c.lower()), None)

    if not url_col or not cat_col:
        console.print("[red]Error: Required columns 'URL' or 'Category' not found in Excel.[/red]")
        return

    while True:
        print_categories()
        choice = input("\n[>] Enter category number: ").strip()

        if choice == "00":
            os.system("cls" if os.name == "nt" else "clear")
            console.print(banner, style="bold green")
            console.print("\n[bold red]Goodbye.[/bold red]")
            break

        if not choice.isdigit() or int(choice) not in categories:
            console.print("[bold red]Invalid choice. Please enter a valid category number.[/bold red]")
            input("\n[press ENTER to continue...]")
            continue

        category_name = categories[int(choice)]
        matches = df[df[cat_col].astype(str).str.strip().str.lower() == category_name.strip().lower()]

        if matches.empty:
            console.print(f"[yellow]No data found for category: {category_name}[/yellow]")
            continue

        table = Table(title=f"Sites in Category: '{category_name}'", show_lines=True)
        table.add_column("Site URL", style="cyan", no_wrap=True)
        table.add_column("💀", style="green", no_wrap=True, width=3)

        for _, row in matches.iterrows():
            url = str(row[url_col]).strip()
            table.add_row(url, "✅")

        console.print(table)
        input("\n[press ENTER to continue...]")

if __name__ == "__main__":
    extract_by_category()
