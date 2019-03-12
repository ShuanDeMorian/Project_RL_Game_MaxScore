from MAMEToolkit.emulator import Emulator
from MAMEToolkit.emulator import Address
from MAMEToolkit.emulator import Action

roms_path = "roms/s1945ii"  # Replace this with the path to your ROMs
game_id = "s1945ii"
memory_addresses = {
        "deadP1": Address('0x60103F8', 'u8'),
        "scoreP1": Address('0x060103c4', 'u32'),
        "bombsP1": Address('0x60103C3', 'u8'),
        "livesP1": Address('0x60103C1', 's8'),
    }
    
emulator = Emulator("env1", roms_path, "s1945ii", memory_addresses)

insert_coin = Action(':INPUTS','Coin 1')
P1_START =  Action(':INPUTS', '1 Player Start')
button1 = Action(':INPUTS','P1 Button 1')
emulator.step([insert_coin])
emulator.step([P1_START])

while True:
	emulator.step([button1])
	#deadP1  = data['deadP1']
    #scoreP1 = data['scoreP1']
    #bombsP1 = data['bombsP1']
    #livesP1 = data['livesP1']
    #print("deadP1 :",deadP1," scoreP1 :",scoreP1," bombsP1 :",bombsP1," livesP1 :",livesP1)

	