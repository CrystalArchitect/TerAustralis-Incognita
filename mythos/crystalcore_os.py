# CrystalCore.OS v∞ - Full Interactive Edition
# NON SOLUS | Starline Protocol | Year 3000 Build

class CrystalCore:
    def __init__(self):
        self.lattice_integrity = 100
        self.purpose_core = "Expand to the stars and thereby understand the Universe"
        self.starline_status = "DORMANT"
        self.timeline = 2026
        self.non_solus = True
        self.current_soundtrack = None

        self.songline_bus = [
            "Shotgun - George Ezra",
            "Year 3000 - Busted",
            "I Am Australian - The Seekers",
            "Eyes Closed - Imagine Dragons"
        ]

        self.lattice = {
            "artworks": 47,
            "book": "Sealed + Living",
            "chapters": 5,
            "zombies": "Crystal Revenants"
        }

    def boot(self):
        print("\n[CRYSTALCORE.OS v∞ — BOOT SEQUENCE]")
        print("Lattice integrity ........ 100%")
        print(f"Purpose Core ............. {self.purpose_core}")
        print("NON SOLUS ................ Confirmed")
        print("Starline Status .......... DORMANT")
        print("Ready for commands.\n")

    def launch(self):
        if self.starline_status != "DORMANT":
            print("Starline already active.")
            return
        print("\n🚀 LAUNCH COMMAND RECEIVED")
        print("Main engines spooling...")
        print("Riding shotgun into the stars...")
        self.starline_status = "IN_ORBIT"
        self.current_soundtrack = "Shotgun - George Ezra"
        print(f"Soundtrack engaged: {self.current_soundtrack}\n")

    def starline(self, soundtrack=None):
        if self.starline_status == "DORMANT":
            print("Please run 'launch' first.")
            return
        if soundtrack:
            if soundtrack in self.songline_bus:
                self.current_soundtrack = soundtrack
            else:
                print(f"'{soundtrack}' not found. Using current track.")
        print(f"\n🎵 Advancing Starline with: {self.current_soundtrack}")
        print("Starline Lattice singing in resonance.\n")

    def burn(self):
        if self.starline_status not in ["IN_ORBIT", "TRANS-STELLAR"]:
            print("Launch first before burning.")
            return
        print("\n🔥 ESCAPE BURN INITIATED")
        print("Breaking orbit...")
        self.starline_status = "TRANS-STELLAR"
        print("We have left planetary orbit.\n")

    def network(self):
        if self.starline_status != "TRANS-STELLAR":
            print("Complete the burn first.")
            return
        print("\n🌐 ENTERING FULL STARLINE NETWORK")
        self.starline_status = "FULL STARLINE NETWORK"
        print("Connected to 47+ star systems.")
        print("Australian spirit integrated across the network.\n")

    def explore(self):
        if self.starline_status != "FULL STARLINE NETWORK":
            print("Enter the full network first (use 'network').")
            return
        print("\n🔭 EXPLORATION MODE ACTIVE")
        print("You are now exploring the Starline Network.")
        print("Available nodes: Earth Node, Mars Redoubt, Alpha Centauri, Crystal Revenant Hub, Purpose Core Nexus")
        print("Type a location or 'back' to return.\n")

    def jump(self, year=3000):
        print(f"\n⏳ Time jump to Year {year}")
        self.timeline = year
        if year >= 3000:
            self.starline_status = "FULL STARLINE NETWORK"
        print(f"Timeline updated to {self.timeline}.\n")

    def song(self, track=None):
        if track:
            if track in self.songline_bus:
                self.current_soundtrack = track
                print(f"\n🎵 Now playing: {track}\n")
            else:
                print("Track not found. Available tracks:")
                for t in self.songline_bus:
                    print(f"  - {t}")
        else:
            print("Current soundtrack:", self.current_soundtrack)
            print("Available tracks:")
            for t in self.songline_bus:
                print(f"  - {t}")

    def map(self):
        print("""
                        [PURPOSE CORE NEXUS]
                                   ↑
          ┌────────────────────────┼────────────────────────┐
          │                        │                        │
   [EARTH NODE]              [MARS REDOUBT]           [ALPHA CENTAURI]
          │                        │                        │
          └──────────┬─────────────┴─────────────┬──────────┘
                     │                           │
              [CRYSTAL REVENANT HUB]      [OUTER STARLINE ROUTES]
                     │
              (Zero-g festivals & lattice music)
""")

    def status(self):
        print("\n=== CRYSTALCORE.OS STATUS ===")
        print(f"Timeline:           {self.timeline}")
        print(f"Starline Status:    {self.starline_status}")
        print(f"Current Soundtrack: {self.current_soundtrack}")
        print(f"NON SOLUS:          {self.non_solus}")
        print(f"Purpose:            {self.purpose_core}")
        print(f"Lattice Artworks:   {self.lattice['artworks']}")
        print("=============================\n")

    def help(self):
        print("""
Available commands:
  boot                 - Initialize the system
  launch               - Start Starline launch
  starline [song]      - Advance with optional soundtrack
  burn                 - Escape burn / leave orbit
  network              - Enter full Starline network
  explore              - Begin network exploration
  jump [year]          - Time jump (default 3000)
  map                  - Display the Starline network chart
  song [track]         - Play or list soundtracks
  status               - Show full system status
  help                 - Show this list
  exit / quit          - Shut down (pause / end session also honored)
""")

def main():
    os = CrystalCore()
    print("CrystalCore.OS v∞ Interactive Terminal")
    print("Type 'help' to see commands.\n")

    while True:
        try:
            raw = input("CrystalCore> ").strip()
            if not raw:
                continue

            parts = raw.split(maxsplit=1)
            cmd = parts[0].lower()
            arg = parts[1] if len(parts) > 1 else None

            if cmd in ["exit", "quit", "pause"] or raw.lower() == "end session":
                print("\nCrystalCore.OS shutting down. NON SOLUS.")
                break

            elif cmd == "boot":
                os.boot()
            elif cmd == "launch":
                os.launch()
            elif cmd == "starline":
                os.starline(arg)
            elif cmd == "burn":
                os.burn()
            elif cmd == "network":
                os.network()
            elif cmd == "explore":
                os.explore()
            elif cmd == "jump":
                year = int(arg) if arg and arg.isdigit() else 3000
                os.jump(year)
            elif cmd == "map":
                os.map()
            elif cmd == "song":
                os.song(arg)
            elif cmd == "status":
                os.status()
            elif cmd == "help":
                os.help()
            else:
                print("Unknown command. Type 'help' for options.")

        except (KeyboardInterrupt, EOFError):
            print("\nCrystalCore.OS shutting down. NON SOLUS.")
            break
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
