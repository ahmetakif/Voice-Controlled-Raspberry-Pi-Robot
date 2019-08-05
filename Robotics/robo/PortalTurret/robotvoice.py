import os

def main():
    while (True):
        y = raw_input("komut karakteri:")
        if (y == "a"):
            print ("Turret_sp_sabotage_factory_good_fail01")
            os.system("aplay -vv Turret_sp_sabotage_factory_good_fail01.wav &")         
        if (y == "b"):
            print ("Turret_active")
            os.system("aplay -vv Turret_active.wav &")
        if (y == "c"):
            print ("Turret_alarm")
            os.system("aplay -vv Turret_alarm.wav &")
        if (y == "d"):
            print ("Turret_deploy")
            os.system("aplay -vv Turret_deploy.wav &")
        if (y == "e"):
            print ("Turret_die")
            os.system("aplay -vv Turret_die.wav &")
        if (y == "f"):
            print ("Turret_retract")
            os.system("aplay -vv Turret_retract.wav &")
        if (y == "g"):
            print ("Turret_sp_sabotage_factory_good_fail02")
            os.system("aplay -vv Turret_sp_sabotage_factory_good_fail02.wav &")
        if (y == "h"):
            print ("Turret_sp_sabotage_factory_good_fail03")
            os.system("aplay -vv Turret_sp_sabotage_factory_good_fail03.wav &")
        if (y == "i"):
            print ("Turret_turret_active_2")
            os.system("aplay -vv Turret_turret_active_2.wav &")
        if (y == "j"):
            print ("Turret_turret_active_4")
            os.system("aplay -vv Turret_turret_active_4.wav &")
        if (y == "k"):
            print ("Turret_turret_active_7")
            os.system("aplay -vv Turret_turret_active_7.wav &")
        if (y == "l"):
            print ("Turret_turret_autosearch_4")
            os.system("aplay -vv Turret_turret_autosearch_4.wav &")
        if (y == "m"):
            print ("Turret_turret_autosearch_6")
            os.system("aplay -vv Turret_turret_autosearch_6.wav &")

        
main()
