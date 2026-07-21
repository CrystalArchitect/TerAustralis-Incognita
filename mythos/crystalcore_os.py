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
        self.current_location = None

        self.songline_bus = [
            "Shotgun - George Ezra",
            "Year 3000 - Busted",
            "I Am Australian - The Seekers",
            "Eyes Closed - Imagine Dragons"
        ]

        self.nodes = [
            "Earth Node",
            "Mars Redoubt",
            "Alpha Centauri Outpost",
            "Crystal Revenant Hub",
            "Purpose Core Nexus"
        ]

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
        self.starline_status = "IN_ORBIT"
        self.current_soundtrack = "Shotgun - George Ezra"
        print(f"Soundtrack engaged: {self.current_soundtrack}\n")

    def starline(self, soundtrack=None):
        if self.starline_status == "DORMANT":
            print("Please run 'launch' first.")
            return
        if soundtrack and soundtrack in self.songline_bus:
            self.current_soundtrack = soundtrack
        print(f"\n🎵 Advancing Starline with: {self.current_soundtrack}\n")

    def burn(self):
        if self.starline_status not in ["IN_ORBIT", "TRANS-STELLAR"]:
            print("Launch first before burning.")
            return
        print("\n🔥 ESCAPE BURN INITIATED")
        self.starline_status = "TRANS-STELLAR"
        print("We have left planetary orbit.\n")

    def network(self):
        if self.starline_status != "TRANS-STELLAR":
            print("Complete the burn first.")
            return
        print("\n🌐 ENTERING FULL STARLINE NETWORK")
        self.starline_status = "FULL STARLINE NETWORK"
        print("Connected to 47+ star systems.\n")

    def explore(self):
        if self.starline_status != "FULL STARLINE NETWORK":
            print("You must enter the full network first (use 'network').")
            return
        print("\n🔭 EXPLORATION MODE ACTIVE")
        print("Available nodes:")
        for i, node in enumerate(self.nodes, 1):
            print(f"  {i}. {node}")
        print("\nUse 'visit <number or name>' to travel.")

    def visit_node(self, node_name):
        if not node_name:
            print("Usage: visit <number or name>")
            return
        # Accept a number from the explore listing, or a name in any case.
        if node_name.isdigit() and 1 <= int(node_name) <= len(self.nodes):
            node_name = self.nodes[int(node_name) - 1]
        else:
            match = next((n for n in self.nodes if n.lower() == node_name.lower()), None)
            if match is None:
                print("Node not found. Available nodes:")
                for node in self.nodes:
                    print(f"  - {node}")
                return
            node_name = match

        self.current_location = node_name
        print(f"\n🌌 Arriving at: {node_name}")
        if node_name == "Purpose Core Nexus":
            print(f'"{self.purpose_core}"')
        elif node_name == "Crystal Revenant Hub":
            print("Zero-g music festivals are in full swing.")
        else:
            print("The lattice pulses with new resonance here.")
        print(f"Current soundtrack: {self.current_soundtrack}\n")

    def jump(self, year=3000):
        print(f"\n⏳ Time jump to Year {year}")
        self.timeline = year
        if year >= 3000:
            self.starline_status = "FULL STARLINE NETWORK"
        print(f"Timeline set to {self.timeline}.\n")

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
            print(f"Current soundtrack: {self.current_soundtrack}")

    def map(self):
        print("""
                        [PURPOSE CORE NEXUS]
                       (The Quote burns here)
                                  ↑
          ┌───────────────────────┼───────────────────────┐
          │                       │                       │
   [EARTH NODE]            [MARS REDOUBT]         [ALPHA CENTAURI]
   (Homeworld memory)      (First colony)         (Frontier edge)
          │                       │                       │
          └───────────┬───────────┴───────────┬───────────┘
                      │                       │
               [CRYSTAL REVENANT HUB]
               (Zero-g music & festivals)

   Chart: mythos/art/starline-network-year-3000.jpeg
""")

    def status(self):
        print("\n=== CRYSTALCORE.OS STATUS ===")
        print(f"Timeline:           {self.timeline}")
        print(f"Starline Status:    {self.starline_status}")
        print(f"Current Location:   {self.current_location or 'None'}")
        print(f"Current Soundtrack: {self.current_soundtrack}")
        print(f"NON SOLUS:          {self.non_solus}")
        print("=============================\n")

    def help(self):
        print("""
Available commands:
  boot                 - Initialize system
  launch               - Start Starline launch
  starline [song]      - Advance with soundtrack
  burn                 - Escape burn
  network              - Enter full Starline network
  explore              - List explorable nodes
  visit [node]         - Go to a node (number or name)
  jump [year]          - Time jump
  map                  - Display the Starline network chart
  song [track]         - Change soundtrack
  status               - Show current status
  help                 - Show this list
  exit / quit          - Shut down (pause / end session also honored)
""")

def main():
    os = CrystalCore()
    print("CrystalCore.OS v∞ Interactive Terminal")
    print("Type 'help' to see all commands.\n")

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
            elif cmd == "visit":
                os.visit_node(arg)
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
