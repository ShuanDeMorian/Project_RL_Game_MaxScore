from MAMEToolkit.emulator import Emulator
from MAMEToolkit.emulator import Address

roms_path = "roms/s1945ii"  # Replace this with the path to your ROMs
game_id = "s1945ii"
memory_addresses = {
        "deadP1": Address('0x60103F8', 'u8'),
        "scoreP1": Address('0x060103c4', 'u32'),
        "bombsP1": Address('0x60103C3', 'u8'),
        "livesP1": Address('0x60103C1', 's8'),
    }
    
emulator = Emulator("env1", roms_path, "s1945ii", memory_addresses)