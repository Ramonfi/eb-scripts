
"""
Created on 29.11.2020
@author: Ahmad Saleem Nouman
DATA LOGGER FOR Einfach Bauen (Bad_Aibling)

Einfach Bauen 2: Forschungshäuser Bad Aibling _ Sensorbezeichnung													

Gebäude_	
LB_	= Leichtbeton
HM_	= Holz massiv
MW_	= Mauerwerk

Ebene_Wohnung_	
2OG_N_ = 2.OG_Nord: 2.5_Zi_Wo
2OG_O_  = 2.OG_Ost: 1_Zi_Wo
2OG_S_  = 2.OG_Süd: 2.5_Zi_Wo
DA_W_   = Dach_West: Wetterstation
2OG_TH_ = Treppenhaus

Zimmer_	
B_   = Badezimmer
F_   = Flur
K_   = Küche
SZ_  = Schlafzimmer
WZ_	 = Wohnzimmer
SWK_ = 1_Zi_Wohnung

Wand_	
o_ = ost
w_ = west
n_ = nord
s_ = süd
m_ = raummitte

Sensortyp (TF Bricklet)	
rtc  = RealTimeClock
ow	 = OutdoorWeather
md	 = MotionDetector
t	 = Temperature
pt	 = PTC
id	 = IndustrialDual020mA
tir	 = Temperature IR
rh	 = Humidity
al	 = AmbientLight
co2	 = CO2
tilt = Tilt
he	 = HallEffect
el	 = EnergyMonitor
hz	 = Heat
ww	 = Warmwater

Parameter		Einheit
Zeit	        Datum / Uhrzeit	dd.mm.yyyy/hh:mm:ss
Wetter	        Tamb/RH/Regen/WinR/WinG	°C, %, mm, 360°, m/s
Anw	            Präsenzmelder	0/1
Tair	        Raumlufttemperatur	°C
Tsk	            Schwarzkugeltemperatur	°C
_	            Signalumwandler	mA
Tsurf	        Oberfl.Temp. Wände (wd) / Heizkörper (hk)	°C
RH	            Relative Raumluftfeuchte	%
BS	            Beleuchtungsstärke	Lux
LQ	            Luftqualität in CO2	ppm
Fkipp	        Fensteröffnung kipp	0/1
Fganz	        Fensteröffnung ganz	open/close
Strom	        Stromzähler	Wh
Heiz	        Wärmemengenzähler Heizen	W/s
TWW	            Wärmemengenzähler TWW	W/s

"""


#Set Variables
HOST = "localhost"
PORT = 4223

Anzahl = 0

#Master Bricks

MB1 = "5XbP1n" 
 
MB2 = "6SUfdz" 

MB3 = "5XwVsZ"  

MB4 =  "6Lg15i" #changed from"6KUqQ2" 

MB4b = "6K9pdM"  

MB5 = "6469nX"

MB6 = "5WN48x"

MB7 = "6DXPXp" 

MB7b = "5WrQha"  

MB8 = "6RQpb2"

MB9 = "63JZu6"

MB9b = "6R5Jgk" 

MB10 = "6KUbdz"

MB11 = "6stNrp"

MB12 = "64893V"

MB13 = "6DWPvB" 

MB14a = "6a3KoH"

MB14b = "6gmbcs" 

MB14c = "6QHWQR"  

MB14d = "6QHi6B"

MB15 = "6KRR4F"

MB15b = "6Lgkye"

MB16 = "6RMp4g"

MB17 = "6KSbxB"

MB18 = "6RNJYZ"

MB19 = "6RN8EZ"

MB19b = "6LeBHk"

MB20 = "6KTqoe"

#MB21 = MB-19B

MB22 = "69DD7Z"

MB22b = "5WpRPP"

MB23 = "6maX3Z"

MB24 = "647Mmn"

MB25 = "63JeDK"

MB25b = "5WqSgB"

MB26 = "6R3DHT"

#MB27 =  MB-4B

#MB28 =  MB-7B

#MB29 =  MB-9B

#MB30 =  MB-22B

#MB31 =  MB-25B

#MB32 = "6QGzGv"  #      Not connected to the network anymore

#MB33 =  MB-15B

#_________________________________________________#

#Northern_Apt SZ part 1 ____ MB1 _____
UID1 = "RHF"	  #LB_2OG_N_SZ_n_trh_TairRH
UID2 = "C2C"  #LB_2OG_N_SZ_n_co2_LQ
UID3 = "RrX"  #LB_2OG_N_SZ_s_pt_Thk
UID4 = "TF"   #LB_2OG_N_SZ_s_t_Tair  -----New add
 
#Northern_Apt SZ part 2  ____ MB2 _____ 
UID5 = "27TFJv"  #LB_2OG_N_SZ_o_reed_Fganz
UID6 = "BNSZ" #***(Beton-Nord-Schlafzimmer) [#LB_2OG_N_SZ_pt_Tsk] New Black Globe Thermometer UID changed from (V8Q)
#UID7 = "" reserved
#UID8 = "" reserved

#Northern_Apt el ____ MB3 _____
UID9 = "ELD"	  #LB_2OG_N_el1_Strom
UID10 = "ELF"	#LB_2OG_N_el2_Strom
UID11 = "Qj4"	#LB_2OG_N_el3_Strom
#UID12 = "" reserved

#Northern_Apt WZ part 1 ____ MB4 _____
UID13 = "RHG"	#LB_2OG_N_WZ_s_trh_TairRH
UID14 = "TG"	#LB_2OG_N_WZ_s_t_Tair   -----New add
UID15 = "BNWZ" #***(Beton-Nord-Wohnzimmer) [#LB_2OG_N_WZ_pt_Tsk] New Black Globe Thermometer UID changed from (V9F) New add
UID16 = "NSa"     #LB_2OG_N_WZ_m_trh_TairRH   --- New add
UID16b = "QNZ"    # isolator bricklet


#Northern_Apt WZ part 1 ____ MB4b _____
#UID13b = "" reserved
UID14b = "2acnp4"	  #LB_2OG_N_WZ_o_reed_Fganz
#UID15b = "" reserved
#UID16b = "" reserved


#Northern_Apt WZ part 2 ____ MB5 _____
UID17 = "2i7GrK"	#LB_2OG_N_WZ_n_reed_Fganz
UID18 = "MDD"	#LB_2OG_N_WZ_n_md_Anw
#UID19 = "" reserved
#UID20 = "" reserved

#Northern_Apt WZ part 3 ____ MB6 _____ 
UID21 = "Nkp"	#LB_2OG_N_WZ_w_pt_Thk
#UID22 = "" reserved
#UID23 = "" reserved
#UID24 = "" reserved

#Northern_Apt K part 1 ____ MB7 _____
UID25 = "RHK"	#LB_2OG_N_K_w_trh_TairRH
UID26 = "TK"	#LB_2OG_N_K_w_t_Tair   -----New add
#UID27 = "" reserved
#UID28 = "" reserved

#Northern_Apt K part 1 ____ MB7b _____
#UID25b = "" reserved
UID26b = "2nvitt"	#LB_2OG_N_K_w_reed_Fganz
#UID27b = "" reserved
#UID28b = "" reserved


#Northern_Apt K part2 ____ MB8 _____
UID29 = "2oZsuM" #LB_2OG_N_K_n_reed_Fganz
#UID30 = "" reserved
#UID31 = "" reserved
#UID32 = "" reserved

#Northern_Apt F ____ MB9 _____
UID33 = "23rTCr"	#LB_2OG_N_F_w_reed_Fganz
#UID34 = "" reserved
#UID35 = "" reserved
#UID36 = "" reserved

#Northern_Apt F ____ MB9b _____
#UID33b ="" reserved
UID34b = "MDE"	#LB_2OG_N_F_w_md_Anw
#UID35b = "" reserved
#UID36b = "" reserved

#Northern_Apt B ____ MB10 _____
UID37 = "RrU"	#LB_2OG_N_B_n_pt_Tair
UID38 = "RHJ"	#LB_2OG_N_B_n_trh_TairRH
UID39 = "Nnb"	#LB_2OG_N_B_n_pt_Thk
#UID40 = "" reserved

##Northern_Apt hzww
#UID41= ""	#LB_2OG_N_hz_Heiz (reserved)
#UID42= ""	#LB_2OG_N_ww_TWW (reserved)
#UID43 = "" reserved
#UID44 = "" reserved

#_________________________________________________#

#2nd Floor Stairway ____ MB11 _____
UID45 = "RHH" #LB_2OG_TH_m_trh_TairRH
UID46 = "TH" #LB_2OG_TH_m_t_Tair  ---- new add
UID47 = "N54" #ow_1   Outdoor Weather     ---- new add
UID48 = "DAA" #LB_DA_W_id_Pyrano     Industrial Dual Analog    ---- new add

#_________________________________________________#

#Central_Apt part 1 ____ MB12 _____

UID49= "RrN"	#LB_2OG_O_SWK_s_pt_Thk
#UID50 = "" reserved
#UID51 = "" reserved
#UID52 = "" reserved

#Central_Apt part 2 ____ MB13 _____
UID53 = "VLrCZ" #LB_2OG_O_SWK_o_reed_Fganz
#UID54 = "" reserved
#UID55 = "" reserved
#UID56 = "" reserved

#Central_Apt part 3 ____ MB14a _____
UID57 = "TRA"	#LB_2OG_O_SWK_m_tir1_Twd
UID58 = "TRB"	#LB_2OG_O_SWK_m_tir2_Twd
UID59 = "TRC"	#LB_2OG_O_SWK_m_tir3_Twd
UID60 = "TRD"	#LB_2OG_O_SWK_m_tir4_Twd

#Central_Apt part 3  ____ MB14b _____	
UID61 = "TRE"	#LB_2OG_O_SWK_m_tir5_Twd
UID62 = "TRF"	#LB_2OG_O_SWK_m_tir6_Twd
UID63 = "RHA"	#LB_2OG_O_SWK_m_trh_TairRH
UID64 = "Sso"	#LB_2OG_O_SWK_m_pt_Tsk "Black Globe Thermometer"

#Central_Apt part 3  ____ MB14c _____	
UID65 = "C2A"	#LB_2OG_O_SWK_m_co2_LQ
UID66 = "ALA"	#LB_2OG_O_SWK_m_al_BS
UID67 = "MDA"	#LB_2OG_O_SWK_m_md_Anw
UID68 = "RTC"	#LB_2OG_O_SWK_m_rtc_Zeit / rtc

#Central_Apt part 3  ____ MB14d _____	
UID65b = "TA"	#LB_2OG_O_SWK_m_t_Tair ---- new add
UID66b = "TCL"	#LB_2OG_O_SWK_m_tcl_Tsk ---- new add
#UID67d = "" reserved
#UID68d = "" reserved

#Central_Apt B ____ MB15 _____
UID69 = "NqR"	#LB_2OG_O_B_n_pt_Tair
UID70 = "NRD"	#LB_2OG_O_B_n_trh_TairRH
UID71 = "RrH"  #LB_2OG_O_B_w_pt_Thk
#UID72 = "" reserved

#Central_Apt part 4 ____ MB15b _____
UID69b = "QjA"	#LB_2OG_O_el1_Strom
UID70b = "QiH"	#LB_2OG_O_el2_Strom
UID71b = "QiN" #LB_2OG_O_el3_Strom
#UID120 = "" reserved
#_________________________________________________#

#Southern_Apt SZ part 1 ____ MB16 _____

UID73 = "RHB"	#LB_2OG_S_SZ_n_trh_TairRH
UID74 = "C2B"	#LB_2OG_S_SZ_n_co2_LQ
UID75 = "SsN"	#LB_2OG_S_SZ_o_pt_Thk
UID76 = "TB"    #LB_2OG_S_SZ_n_t_Tair ---- new add

#Southern_Apt SZ part 2 ____ MB17 _____
UID77 = "2hod2t"    	#LB_2OG_S_SZ_o_reed_Fganz
UID78 = "BSSZ" #***(Beton-Süd-Schlafzimmer) [#LB_2OG_S_SZ_pt_Tsk] New Black Globe Thermometer changed from UID V98
#UID79 = "" reserved
#UID80 = "" reserved

#Southern_Apt el ____ MB18 _____
UID81 = "ELA"	#LB_2OG_S_el1_Strom
UID82 = "ELB"	#LB_2OG_S_el2_Strom
UID83 = "ELC"	#LB_2OG_S_el3_Strom
#UID84 = "" reserved

#Southern_Apt WZ part 1 ____ MB19 _____ 
UID85 = "RHC"	#LB_2OG_S_WZ_n_trh_TairRH
UID86 = "TC"	    #LB_2OG_S_WZ_n_t_Tair ---- new add
UID87 = "BSWZ"	#***(Beton-Süd-Wohnzimmer) [#LB_2OG_S_WZ_pt_Tsk] New Black Globe Thermometer changed from UID V9N
#UID88 = "" reserved

#Southern_Apt WZ part 1 ____ MB19b _____ 
#UID85a =  ""	reserved
UID86b = "2jBwqV"	#LB_2OG_S_WZ_o_reed_Fganz 
#UID87b = ""	reserved
#UID88b = "" reserved

#Southern_Apt WZ part 2 ____ MB20 _____ 
UID89 = "24bo3H"	#LB_2OG_S_WZ_s_reed_Fganz
UID90 = "MDB"	#LB_2OG_S_WZ_s_md_Anw
UID91 = "NjT" #LB_2OG_S_WZ_w_pt_Thk --- new add
#UID92 = "" reserved

#Southern_Apt WZ part 3 ____ MB21 _____ 
#UID93 = ""	reserved
#UID94 = ""	reserved
#UID95 = "" reserved
#UID96 = "" reserved

#Southern_Apt K part 1 ____ MB22 _____ 
#UID97= ""	#reserved
UID98= "RHD"	   #LB_2OG_S_K_w_trh_TairRH
UID99 = "TD"  #LB_2OG_S_K_w_t_Tair   -----New add
#UID100 = "" reserved

#Southern_Apt K part 1 ____ MB22b _____ 
UID97b= "26pSc8"	#LB_2OG_S_K_w_reed_Fganz
#UID98b= "" reserved
#UID99b = "" reserved
#UID100b = "" reserved


#Southern_Apt K part 2  ____ MB23 _____ 
UID101 = "WikWD" #LB_2OG_S_K_s_reed_Fganz
#UID102 = "" reserved
#UID103 = "" reserved
#UID104 = "" reserved

#Southern_Apt F part 1 ____ MB24 _____ 
UID105 = "2j9Zon"	#LB_2OG_S_F_w_reed1_Fganz
#UID106 = "" reserved
#UID107 = "" reserved
#UID108 = "" reserved

#Southern_Apt F part 2 ____ MB25 _____ 
UID109= "2dF55D"	#LB_2OG_S_F_w_reed2_Fganz
#UID110= "" reserved
#UID111 = "" reserved
#UID112 = "" reserved

#Southern_Apt F part 2 ____ MB25b _____ 
#UID109b = ""	reserved
UID110b = "MDC"	#LB_2OG_S_F_n_md_Anw
#UID111b = "" reserved
#UID112b = "" reserved

#Southern_Apt B ____ MB26 _____ 
UID113 = "Rs1"	#LB_2OG_S_B_n_pt_Tair
UID114 = "RHE"	#LB_2OG_S_B_s_trh_TairRH
UID115 = "NkE"	#LB_2OG_S_B_n_pt_Thk
#UID116 = "" reserved

##Southern_Apt hzww
#UID121 = ""	#LB_2OG_S_hz_Heiz
#UID122 = ""	#LB_2OG_S_ww_TWW
#UID123 = "" reserved
#UID124 = "" reserved

UID125 = "Sa8" #Isolator Bad Zimmer Nord (MB10)

import os.path
import time
from time import *
from time import sleep
import logging as log
log.basicConfig(level=log.INFO)

from tinkerforge.ip_connection import IPConnection
from tinkerforge.bricklet_outdoor_weather import BrickletOutdoorWeather
from tinkerforge.bricklet_industrial_dual_analog_in_v2 import BrickletIndustrialDualAnalogInV2
from tinkerforge.brick_master import BrickMaster
from tinkerforge.bricklet_io4_v2 import BrickletIO4V2
from tinkerforge.bricklet_real_time_clock_v2 import BrickletRealTimeClockV2
from tinkerforge.bricklet_ptc_v2 import BrickletPTCV2
from tinkerforge.bricklet_motion_detector_v2 import BrickletMotionDetectorV2
from tinkerforge.bricklet_temperature_v2 import BrickletTemperatureV2
from tinkerforge.bricklet_temperature_ir_v2 import BrickletTemperatureIRV2
from tinkerforge.bricklet_humidity_v2 import BrickletHumidityV2
from tinkerforge.bricklet_co2_v2 import BrickletCO2V2
from tinkerforge.bricklet_ambient_light_v3 import BrickletAmbientLightV3
from tinkerforge.bricklet_energy_monitor import BrickletEnergyMonitor
from tinkerforge.bricklet_thermocouple_v2 import BrickletThermocoupleV2
from tinkerforge.bricklet_isolator import BrickletIsolator

# Callback function for station data callback
def cb_station_data(identifier, temperature, humidity, wind_speed, gust_speed, rain,
                    wind_direction, battery_low):
    identifier = str(identifier)
    temperature = str(temperature/10.0)
    humidity = str(humidity)
    wind_speed = str(wind_speed/10.0)
    gust_speed = str(gust_speed/10.0)
    rain = str(rain/10.0)
    if wind_direction == BrickletOutdoorWeather.WIND_DIRECTION_N:
        wind_direction = str("N")
        ow_1_wd = wind_direction
        
    elif wind_direction == BrickletOutdoorWeather.WIND_DIRECTION_NNE:
        wind_direction = str("NNE")
        ow_1_wd = wind_direction
        
    elif wind_direction == BrickletOutdoorWeather.WIND_DIRECTION_NE:
        wind_direction = str("NE")
        ow_1_wd = wind_direction
        
    elif wind_direction == BrickletOutdoorWeather.WIND_DIRECTION_ENE:
        wind_direction = str("ENE") 
        ow_1_wd = wind_direction
        
    elif wind_direction == BrickletOutdoorWeather.WIND_DIRECTION_E:
        wind_direction = str("E") 
        ow_1_wd = wind_direction
    elif wind_direction == BrickletOutdoorWeather.WIND_DIRECTION_ESE:
        wind_direction = str("ESE")
        ow_1_wd = wind_direction
        
    elif wind_direction == BrickletOutdoorWeather.WIND_DIRECTION_SE:
        wind_direction = str("SE")
        ow_1_wd = wind_direction
        
    elif wind_direction == BrickletOutdoorWeather.WIND_DIRECTION_SSE:
        wind_direction = str("SSE")
        ow_1_wd = wind_direction
        
    elif wind_direction == BrickletOutdoorWeather.WIND_DIRECTION_S:
        wind_direction = str("S") 
        ow_1_wd = wind_direction
        
    elif wind_direction == BrickletOutdoorWeather.WIND_DIRECTION_SSW:
        wind_direction = str("SSW")
        ow_1_wd = wind_direction
        
    elif wind_direction == BrickletOutdoorWeather.WIND_DIRECTION_SW:
        wind_direction = str("SW")
        ow_1_wd = wind_direction
        
    elif wind_direction == BrickletOutdoorWeather.WIND_DIRECTION_WSW:
        wind_direction = str("WSW")
        ow_1_wd = wind_direction
        
    elif wind_direction == BrickletOutdoorWeather.WIND_DIRECTION_W:
        wind_direction = str("W")
        ow_1_wd = wind_direction
        
    elif wind_direction == BrickletOutdoorWeather.WIND_DIRECTION_WNW:
        wind_direction = str("WNW")
        ow_1_wd = wind_direction
        
    elif wind_direction == BrickletOutdoorWeather.WIND_DIRECTION_NW:
        wind_direction = str("NW")
        ow_1_wd = wind_direction
        
    elif wind_direction == BrickletOutdoorWeather.WIND_DIRECTION_NNW:
        wind_direction = str("NNW")
        ow_1_wd = wind_direction
        
    elif wind_direction == BrickletOutdoorWeather.WIND_DIRECTION_ERROR:
        wind_direction = str("ERROR")
        ow_1_wd = wind_direction
    
    battery_low = str(battery_low)
    
    ow_1_id = identifier
    ow_1_t = temperature
    ow_1_rh = humidity
    ow_1_ws = wind_speed
    ow_1_gs = gust_speed
    ow_1_rn = rain
    ow_1_btry = battery_low
    
    Ausgabe_w =   (str(year)+','+str(month)+','+str(day)+';'\
                +str(hour)+':'+str(minute)+':'+str(second)+';'   
                +str(ow_1_id) +';'
                +str(ow_1_t) +';' 
                +str(ow_1_rh) +';' 
                +str(ow_1_ws) +';' 
                +str(ow_1_gs) +';' 
                +str(ow_1_rn) +';' 
                +str(ow_1_wd) +';'
                +str(ow_1_btry) +';'
                +'\n')     

    maketrans = Ausgabe_w.maketrans
    Ausgabe_w = Ausgabe_w.translate(maketrans(',.', '.,'))

    data = open(filename_w,'a') 
    data.write(Ausgabe_w)
    data.close()
    #print(Ausgabe_w)
    
    
    
if __name__ == "__main__":

    ipcon = IPConnection()

#_________________________________________________#
    
    MB1_cdo = BrickMaster(MB1, ipcon) # Create device object
    
    MB2_cdo = BrickMaster(MB2, ipcon) # Create device object
    
    MB3_cdo = BrickMaster(MB3, ipcon) # Create device object
    
    MB4_cdo = BrickMaster(MB4, ipcon) # Create device object
    
    MB4b_cdo = BrickMaster(MB4b, ipcon) # Create device object
        
    MB5_cdo = BrickMaster(MB5, ipcon) # Create device object
    
    MB6_cdo = BrickMaster(MB6, ipcon) # Create device object
    
    MB7_cdo = BrickMaster(MB7, ipcon) # Create device object

    MB7b_cdo = BrickMaster(MB7b, ipcon) # Create device object
    
    MB8_cdo = BrickMaster(MB8, ipcon) # Create device object
    
    MB9_cdo = BrickMaster(MB9, ipcon) # Create device object

    MB9b_cdo = BrickMaster(MB9b, ipcon) # Create device object
    
    MB10_cdo = BrickMaster(MB10, ipcon) # Create device object
    
    MB11_cdo = BrickMaster(MB11, ipcon) # Create device object
    
    MB12_cdo = BrickMaster(MB12, ipcon) # Create device object
    
    MB13_cdo = BrickMaster(MB13, ipcon) # Create device object
    
    MB14a_cdo = BrickMaster(MB14a, ipcon) # Create device object
    
    MB14b_cdo = BrickMaster(MB14b, ipcon) # Create device object
    
    MB14c_cdo = BrickMaster(MB14c, ipcon) # Create device object
    
    MB14d_cdo = BrickMaster(MB14c, ipcon) # Create device object
    
    MB15_cdo = BrickMaster(MB15, ipcon) # Create device object

    MB15b_cdo = BrickMaster(MB15b, ipcon) # Create device object
    
    MB16_cdo = BrickMaster(MB16, ipcon) # Create device object

    MB17_cdo = BrickMaster(MB17, ipcon) # Create device object
    
    MB18_cdo = BrickMaster(MB18, ipcon) # Create device object
    
    MB19_cdo = BrickMaster(MB19, ipcon) # Create device object

    MB19b_cdo = BrickMaster(MB19b, ipcon) # Create device object
    
    MB20_cdo = BrickMaster(MB20, ipcon) # Create device object
    
    #MB21_cdo = BrickMaster(MB21, ipcon) # Create device object
    
    MB22_cdo = BrickMaster(MB22, ipcon) # Create device object

    MB22b_cdo = BrickMaster(MB22b, ipcon) # Create device object
    
    MB23_cdo = BrickMaster(MB23, ipcon) # Create device object
    
    MB24_cdo = BrickMaster(MB24, ipcon) # Create device object
    
    MB25_cdo = BrickMaster(MB25, ipcon) # Create device object

    MB25b_cdo = BrickMaster(MB25b, ipcon) # Create device object
    
    MB26_cdo = BrickMaster(MB26, ipcon) # Create device object
    

#_________________________________________________#

#Northern_Apt SZ part 1 ____ MB1 _____
    LB_2OG_N_SZ_n_trh_cdo = BrickletHumidityV2(UID1, ipcon) # Create device object
    LB_2OG_N_SZ_n_co2_cdo = BrickletCO2V2(UID2, ipcon) # Create device object
    LB_2OG_N_SZ_s_pt_Thk_cdo = BrickletPTCV2(UID3, ipcon) # Create device object
    LB_2OG_N_SZ_s_t_cdo = BrickletTemperatureV2(UID4, ipcon) # Create device object
    
#Northern_Apt SZ part 2  ____ MB2 _____
    LB_2OG_N_SZ_o_reed_cdo = BrickletIO4V2(UID5, ipcon) # Create device object
    LB_2OG_N_SZ_pt_Tsk_cdo = BrickletPTCV2(UID6, ipcon) # Create device object
    
#Northern_Apt el ____ MB3 _____
    LB_2OG_N_el1_cdo = BrickletEnergyMonitor(UID9, ipcon) # Create device object 
    LB_2OG_N_el2_cdo = BrickletEnergyMonitor(UID10, ipcon) # Create device object 
    LB_2OG_N_el3_cdo = BrickletEnergyMonitor(UID11, ipcon) # Create device object 

#Northern_Apt WZ part 1 ____ MB4 _____
    LB_2OG_N_WZ_s_trh_cdo = BrickletHumidityV2(UID13, ipcon) # Create device object
    LB_2OG_N_WZ_s_t_cdo   = BrickletTemperatureV2(UID14, ipcon) # Create device object
    LB_2OG_N_WZ_pt_Tsk_cdo = BrickletPTCV2(UID15, ipcon) # Create device object
    LB_2OG_N_WZ_m_trh_cdo = BrickletHumidityV2(UID16, ipcon) # Create device object

#Northern_Apt WZ part 1 ____ MB4b _____
    LB_2OG_N_WZ_o_reed_cdo = BrickletIO4V2(UID14b, ipcon) # Create device object
    
    
#Northern_Apt WZ part 2 ____ MB5 _____
    LB_2OG_N_WZ_n_reed_cdo = BrickletIO4V2(UID17, ipcon) # Create device object
    LB_2OG_N_WZ_n_md_cdo = BrickletMotionDetectorV2(UID18, ipcon) # Create device object
        
#Northern_Apt WZ part 3 ____ MB6 _____   
    LB_2OG_N_WZ_w_pt_Thk_cdo = BrickletPTCV2(UID21, ipcon) # Create device object   

#Northern_Apt K part 1 ____ MB7 _____
    LB_2OG_N_K_w_trh_cdo = BrickletHumidityV2(UID25, ipcon) # Create device object
    LB_2OG_N_K_w_t_cdo   = BrickletTemperatureV2(UID26, ipcon) # Create device object

#Northern_Apt K part 1 ____ MB7b _____
    LB_2OG_N_K_w_reed_cdo = BrickletIO4V2(UID26b, ipcon) # Create device object
    
#Northern_Apt K part2 ____ MB8 _____
    LB_2OG_N_K_n_reed_cdo = BrickletIO4V2(UID29, ipcon) # Create device object
    
#Northern_Apt F ____ MB9 _____
    LB_2OG_N_F_w_reed_cdo = BrickletIO4V2(UID33, ipcon) # Create device object


#Northern_Apt F ____ MB9b _____
    LB_2OG_N_F_w_md_cdo = BrickletMotionDetectorV2(UID34b, ipcon) # Create device object
    
#Northern_Apt B ____ MB10 _____
    LB_2OG_N_B_n_pt_Tair_cdo = BrickletPTCV2(UID37, ipcon) # Create device object
    LB_2OG_N_B_n_trh_cdo = BrickletHumidityV2(UID38, ipcon) # Create device object
    LB_2OG_N_B_n_pt_Thk_cdo = BrickletPTCV2(UID39, ipcon) # Create device object
    
#2nd Floor Stairway ____ MB11 _____
    LB_2OG_TH_m_trh_cdo = BrickletHumidityV2(UID45, ipcon) # Create device object    
    LB_2OG_TH_m_t_cdo   = BrickletTemperatureV2(UID46, ipcon) # Create device object
    ow_1_cdo = BrickletOutdoorWeather(UID47, ipcon) # Create device object  
    LB_DA_W_id_Pyrano_cdo = BrickletIndustrialDualAnalogInV2(UID48, ipcon) # Create device object
  
#Central_Apt part 1 ____ MB12 _____
    LB_2OG_O_SWK_s_pt_Thk_cdo = BrickletPTCV2(UID49, ipcon) # Create device object
    
#Central_Apt part 2 ____ MB13 _____
    LB_2OG_O_SWK_o_reed_cdo = BrickletIO4V2(UID53, ipcon) # Create device object
    
#Central_Apt part 3 ____ MB14a _____
    LB_2OG_O_SWK_m_tir1_cdo = BrickletTemperatureIRV2(UID57, ipcon) # Create device object
    LB_2OG_O_SWK_m_tir2_cdo = BrickletTemperatureIRV2(UID58, ipcon) # Create device object
    LB_2OG_O_SWK_m_tir3_cdo = BrickletTemperatureIRV2(UID59, ipcon) # Create device object
    LB_2OG_O_SWK_m_tir4_cdo = BrickletTemperatureIRV2(UID60, ipcon) # Create device object    

#Central_Apt part 3  ____ MB14b _____	
    LB_2OG_O_SWK_m_tir5_cdo = BrickletTemperatureIRV2(UID61, ipcon) # Create device object
    LB_2OG_O_SWK_m_tir6_cdo = BrickletTemperatureIRV2(UID62, ipcon) # Create device object   
    LB_2OG_O_SWK_m_trh_cdo = BrickletHumidityV2(UID63, ipcon) # Create device object
    LB_2OG_O_SWK_m_pt_Tsk_cdo = BrickletPTCV2(UID64, ipcon) # Create device object
     
#Central_Apt part 3  ____ MB14c _____	
    LB_2OG_O_SWK_m_co2_cdo = BrickletCO2V2(UID65, ipcon) # Create device object
    LB_2OG_O_SWK_m_al_cdo = BrickletAmbientLightV3(UID66, ipcon) # Create device object
    LB_2OG_O_SWK_m_md_cdo = BrickletMotionDetectorV2(UID67, ipcon) # Create device object
    rtc = BrickletRealTimeClockV2(UID68, ipcon) #LB_2OG_O_SWK_m_rtc

#Central_Apt part 3  ____ MB14d _____	
    LB_2OG_O_SWK_m_t_cdo = BrickletTemperatureV2(UID65b, ipcon) # Create device object
    LB_2OG_O_SWK_m_tcl_cdo = BrickletThermocoupleV2(UID66b, ipcon) # Create device object

#Central_Apt B ____ MB15 _____
    LB_2OG_O_B_n_pt_Tair_cdo = BrickletPTCV2(UID69, ipcon) # Create device object
    LB_2OG_O_B_n_trh_cdo = BrickletHumidityV2(UID70, ipcon) # Create device object
    LB_2OG_O_B_w_pt_Thk_cdo = BrickletPTCV2(UID71, ipcon) # Create device object

#Central_Apt part 4 ____ MB15b _____
    LB_2OG_O_el1_cdo = BrickletEnergyMonitor(UID69b, ipcon) # Create device object 
    LB_2OG_O_el2_cdo = BrickletEnergyMonitor(UID70b, ipcon) # Create device object 
    LB_2OG_O_el3_cdo = BrickletEnergyMonitor(UID71b, ipcon) # Create device object  
    
#Southern_Apt SZ part 1 ____ MB16 _____
    LB_2OG_S_SZ_n_trh_cdo = BrickletHumidityV2(UID73, ipcon) # Create device object
    LB_2OG_S_SZ_n_co2_cdo = BrickletCO2V2(UID74, ipcon) # Create device object
    LB_2OG_S_SZ_o_pt_Thk_cdo = BrickletPTCV2(UID75, ipcon) # Create device object
    LB_2OG_S_SZ_n_t_cdo = BrickletTemperatureV2(UID76, ipcon) # Create device object
    
#Southern_Apt SZ part 2 ____ MB17 _____
    LB_2OG_S_SZ_o_reed_cdo = BrickletIO4V2(UID77, ipcon) # Create device object    
    LB_2OG_S_SZ_pt_Tsk_cdo = BrickletPTCV2(UID78, ipcon) # Create device object

#Southern_Apt el ____ MB18 _____   
    LB_2OG_S_el1_cdo = BrickletEnergyMonitor(UID81, ipcon) # Create device object 
    LB_2OG_S_el2_cdo = BrickletEnergyMonitor(UID82, ipcon) # Create device object 
    LB_2OG_S_el3_cdo = BrickletEnergyMonitor(UID83, ipcon) # Create device object    

#Southern_Apt WZ part 1 ____ MB19 _____ 
    LB_2OG_S_WZ_n_trh_cdo = BrickletHumidityV2(UID85, ipcon) # Create device object
    LB_2OG_S_WZ_n_t_cdo   = BrickletTemperatureV2(UID86, ipcon) # Create device object
    LB_2OG_S_WZ_pt_Tsk_cdo = BrickletPTCV2(UID87, ipcon) # Create device object

#Southern_Apt WZ part 1 ____ MB19b _____ 
    LB_2OG_S_WZ_o_reed_cdo = BrickletIO4V2(UID86b, ipcon) # Create device object
    
#Southern_Apt WZ part 2 ____ MB20 _____ 
    LB_2OG_S_WZ_s_reed_cdo = BrickletIO4V2(UID89, ipcon) # Create device object
    LB_2OG_S_WZ_s_md_cdo = BrickletMotionDetectorV2(UID90, ipcon) # Create device object
    LB_2OG_S_WZ_w_pt_Thk_cdo = BrickletPTCV2(UID91, ipcon) # Create device object

#Southern_Apt WZ part 3 ____ MB21 _____ not needed
    
#Southern_Apt K part 1 ____ MB22 _____ 
    LB_2OG_S_K_w_trh_cdo = BrickletHumidityV2(UID98, ipcon) # Create device object
    LB_2OG_S_K_w_t_cdo = BrickletTemperatureV2(UID99, ipcon) # Create device object

#Southern_Apt K part 1 ____ MB22b _____ 
    LB_2OG_S_K_w_reed_cdo = BrickletIO4V2(UID97b, ipcon) # Create device object
    
#Southern_Apt K part 2  ____ MB23 _____ 
    LB_2OG_S_K_s_reed_cdo = BrickletIO4V2(UID101, ipcon) # Create device object 
    
#Southern_Apt F part 1 ____ MB24 _____ 
    LB_2OG_S_F_w_reed1_cdo = BrickletIO4V2(UID105, ipcon) # Create device object   
    
#Southern_Apt F part 2 ____ MB25 _____ 
    LB_2OG_S_F_w_reed2_cdo = BrickletIO4V2(UID109, ipcon) # Create device object     
    
#Southern_Apt F part 2 ____ MB25b _____ 
    
    LB_2OG_S_F_n_md_cdo = BrickletMotionDetectorV2(UID110b, ipcon) # Create device object
    
#Southern_Apt B ____ MB26 _____ 
    LB_2OG_S_B_n_pt_Tair_cdo = BrickletPTCV2(UID113, ipcon) # Create device object
    LB_2OG_S_B_s_trh_cdo = BrickletHumidityV2(UID114, ipcon) # Create device object
    LB_2OG_S_B_n_pt_Thk_cdo = BrickletPTCV2(UID115, ipcon) # Create device object    

    i = BrickletIsolator(UID125, ipcon) # Create device object
    i2 = BrickletIsolator(UID16b, ipcon) # Create device object
#_________________________________________________#    
    
# Connect to brickd
    ipcon.connect(HOST, PORT) # Don't use device before ipcon is connected
    
    try:
        MB1_cdo.disable_status_led()
    
    except:
        
        print ("Master Brick MB1 does not answer")

    try:
        MB2_cdo.disable_status_led()

    except:
        
        print ("Master Brick MB2 does not answer")
        
    try:
        MB3_cdo.disable_status_led()
    
    except:
        
        print ("Master Brick MB3 does not answer")

    try:
        MB4_cdo.disable_status_led()

    except:
        
        print ("Master Brick MB4 does not answer")

    try:
        MB4b_cdo.disable_status_led()

    except:
        
        print ("Master Brick MB4b does not answer")
        
    try:
        MB5_cdo.disable_status_led()
    
    except:
        
        print ("Master Brick MB5 does not answer")

    try:
        MB6_cdo.disable_status_led()
    
    except:
        
        print ("Master Brick MB6 does not answer")

    try:
        MB7_cdo.disable_status_led()
    
    except:
        
        print ("Master Brick MB7 does not answer")

    try:
        MB7b_cdo.disable_status_led()
    
    except:
        
        print ("Master Brick MB7b does not answer")
        
    try:
        MB8_cdo.disable_status_led()
    
    except:
        
        print ("Master Brick MB8 does not answer")

    try:
        MB9_cdo.disable_status_led()
    
    except:
        
        print ("Master Brick MB9 does not answer")

    try:
        MB9b_cdo.disable_status_led()
    
    except:
        
        print ("Master Brick MB9b does not answer")
        

    try:
        MB10_cdo.disable_status_led()
    
    except:
        
        print ("Master Brick MB10 does not answer")

    try:
        MB11_cdo.disable_status_led()
    
    except:
        
        print ("Master Brick MB11 does not answer")

    try:
        MB12_cdo.disable_status_led()
    
    except:
        
        print ("Master Brick MB12 does not answer")

    try:
        MB13_cdo.disable_status_led()
    
    except:
        
        print ("Master Brick MB13 does not answer")

    try:
        MB14a_cdo.disable_status_led()
    
    except:
        
        print ("Master Brick MB14a does not answer")

    try:
        MB14b_cdo.disable_status_led()
    
    except:
        
        print ("Master Brick MB14b does not answer")
        
    try:
        MB14c_cdo.disable_status_led()
    
    except:
        
        print ("Master Brick MB14c does not answer")

    try:
        MB14d_cdo.disable_status_led()
    
    except:
        
        print ("Master Brick MB14d does not answer")
                
    try:
        MB15_cdo.disable_status_led()
    
    except:
        
        print ("Master Brick MB15 does not answer")                
    try:
        MB15b_cdo.disable_status_led()
    
    except:
        
        print ("Master Brick MB15b does not answer") 
        
    try:
        MB16_cdo.disable_status_led()
    
    except:
        
        print ("Master Brick MB16 does not answer")
                  
    try:
        MB17_cdo.disable_status_led()
    
    except:
        
        print ("Master Brick MB17 does not answer")   

    try:
        MB18_cdo.disable_status_led()
    
    except:
        
        print ("Master Brick MB18 does not answer")   
        
    try:
        MB19_cdo.disable_status_led()
    
    except:
        
        print ("Master Brick MB19 does not answer")  
        
    try:
        MB19b_cdo.disable_status_led()
    
    except:
        
        print ("Master Brick MB19b does not answer")  
        
    try:
        MB20_cdo.disable_status_led()
    
    except:
        
        print ("Master Brick MB20 does not answer")  
        
    # try:
    #     MB21_cdo.disable_status_led()
    
    # except:
        
    #     print ("Master Brick MB21 does not answer")  

    try:
        MB22_cdo.disable_status_led()
    
    except:
        
        print ("Master Brick MB22 does not answer")  

    try:
        MB22b_cdo.disable_status_led()
    
    except:
        
        print ("Master Brick MB22b does not answer")  

    try:
        MB23_cdo.disable_status_led()
    
    except:
        
        print ("Master Brick MB23 does not answer")  

    try:
        MB24_cdo.disable_status_led()
    
    except:
        
        print ("Master Brick MB24 does not answer")  
        
    try:
        MB25_cdo.disable_status_led()
        
    except:
        
        print ("Master Brick MB25 does not answer")  
        
    try:
        MB25b_cdo.disable_status_led()
        
    except:
        
        print ("Master Brick MB25b does not answer")  
         
    try:
        MB26_cdo.disable_status_led()
    
    except:
        
        print ("Master Brick MB26 does not answer")

    try:
        i.set_status_led_config(0)
                       
    except:
        print("Isolator MB10 does not answer") 

    try:
        i2.set_status_led_config(0)
                       
    except:
        print("Isolator MB4 does not answer") 
    
 # Get current date and time
    Time_akt = localtime()
    Jahr = str(Time_akt[0])
    Monat = str(Time_akt[1])
    Tag = str(Time_akt[2])
    Stunde = str(Time_akt[3])
    Minute = str(Time_akt[4])
    Sekond = str(Time_akt[5]) 
    
    save_path = r'E:\1_rohdaten\LB'
    title = (Jahr+'_'+Monat+'_'+Tag+'_LB'+'.csv')    # festlegen des Dateinamens
    filename = os.path.join(save_path, title)         
    
    save_path_w = r'E:\1_rohdaten\WD'
    title_w = (Jahr+'_'+Monat+'_'+Tag+'_WD'+'.csv')
    filename_w = os.path.join(save_path_w, title_w)
    
    save_path_Pyrano = r'E:\1_rohdaten\PM'   
    title_Pyrano = (Jahr+'_'+Monat+'_'+Tag+'_PM'+'.csv')
    filename_Pyrano = os.path.join(save_path_Pyrano, title_Pyrano)
    ueberschrift = ("Date"+';'\
                            +"Time"+';'+';'\
                                
                            +"LB_2OG_N_SZ_n_trh_Tair (°C)"+';'\
                            +"LB_2OG_N_SZ_n_trh_RH (%)"+';'\
                            +"LB_2OG_N_SZ_n_co2 (ppm)"+';'\
                            +"LB_2OG_N_SZ_n_co2_Tair (°C)"+';'\
                            +"LB_2OG_N_SZ_n_co2_RH (%)"+';'\
                            +"LB_2OG_N_SZ_s_pt_Thk (°C)"+';'+';'   
                            
                            +"LB_2OG_N_SZ_o_reed [Large] "+';'+';'
                            
                            +"LB_2OG_N_E-Energy1 (Wh)"+';'\
                            +"LB_2OG_N_E-Energy2 (Wh)"+';'\
                            +"LB_2OG_N_E-Energy3 (Wh)"+';'+';'\
                                
                            +"LB_2OG_N_WZ_s_trh_Tair (°C)"+';'\
                            +"LB_2OG_N_WZ_s_trh_RH (%)"+';'                             
                            +"LB_2OG_N_WZ_o_reed [Large] "+';'+';'\
                                
                            +"LB_2OG_N_WZ_n_reed [Large] "+';'\
                            +"LB_2OG_N_WZ_n_md (0=No, 1=Yes)"+';'+';'\
                                
                            +"LB_2OG_N_WZ_w_pt_Thk (°C)"+';'+';'\
                                
                            +"LB_2OG_N_K_w_trh_Tair (°C)"+';'\
                            +"LB_2OG_N_K_w_trh_RH (%)"+';'                               
                            +"LB_2OG_N_K_w_reed [Medium] "+';'+';'\
                                
                            +"LB_2OG_N_K_n_reed [Small]"+';'+';'\
                                
                            +"LB_2OG_N_F_w_reed [Medium]"+';'                              
                            +"LB_2OG_N_F_w_md (0=No, 1=Yes)"+';'+';'
                            
                            +"LB_2OG_N_B_n_pt_Tair (°C)"+';'
                            +"LB_2OG_N_B_n_trh_Tair (°C)"+';'
                            +"LB_2OG_N_B_n_trh_RH (%)"+';'\
                            +"LB_2OG_N_B_n_pt_Thk (°C)"+';'+';'\
                                
                            +"LB_2OG_TH_m_trh_Tair (°C)"+';'\
                            +"LB_2OG_TH_m_trh_RH (%)"+';'+';'\

                            +"LB_2OG_O_SWK_s_pt_Thk (°C)"+';'+';'\
                                
                            +"LB_2OG_O_SWK_o_reed [Large]"+';'+';'\
                            
                            +"LB_2OG_O_SWK_m_tir1_amb (°C)"+';'
                            +"LB_2OG_O_SWK_m_tir1_obj (°C)"+';'
                            +"LB_2OG_O_SWK_m_tir2_amb (°C)"+';'
                            +"LB_2OG_O_SWK_m_tir2_obj (°C)"+';'
                            +"LB_2OG_O_SWK_m_tir3_amb (°C)"+';'
                            +"LB_2OG_O_SWK_m_tir3_obj (°C)"+';'
                            +"LB_2OG_O_SWK_m_tir4_amb (°C)"+';'
                            +"LB_2OG_O_SWK_m_tir4_obj (°C)"+';'+';'

                            +"LB_2OG_O_SWK_m_tir5_amb (°C)"+';'
                            +"LB_2OG_O_SWK_m_tir5_obj (°C)"+';'
                            +"LB_2OG_O_SWK_m_tir6_amb (°C)"+';'
                            +"LB_2OG_O_SWK_m_tir6_obj (°C)"+';'
                            +"LB_2OG_O_SWK_m_trh_Tair (°C)"+';'
                            +"LB_2OG_O_SWK_m_trh_RH (%)"+';'                            
                            +"[Black Globe] LB_2OG_O_SWK_m_pt_Tsk (°C)"+';'+';'
                            
                            +"LB_2OG_O_SWK_m_co2 (ppm)"+';'\
                            +"LB_2OG_O_SWK_m_co2_Tair (°C)"+';'\
                            +"LB_2OG_O_SWK_m_co2_RH (%)"+';'\
                            +"LB_2OG_O_SWK_m_al (lux)"+ ';'   
                            +"LB_2OG_O_SWK_m_md (0=No, 1=Yes)"+';'+';'\

                            +"LB_2OG_O_B_n_pt_Tair (°C)"+';'\
                            +"LB_2OG_O_B_n_trh_Tair (°C)"+';'\
                            +"LB_2OG_O_B_n_trh_RH (%)"+';'\
                            +"LB_2OG_O_B_w_pt_Thk (°C)"+';'+';'\

                            +"LB_2OG_O_E-Energy1 (Wh)"+';'\
                            +"LB_2OG_O_E-Energy2 (Wh)"+';'\
                            +"LB_2OG_O_E-Energy3 (Wh)"+';'+';'   
                                
                            +"LB_2OG_S_SZ_n_trh_Tair (°C)"+';'
                            +"LB_2OG_S_SZ_n_trh_RH (%)"+';'\
                            +"LB_2OG_S_SZ_n_co2 (ppm)"+';'\
                            +"LB_2OG_S_SZ_n_co2_Tair (°C)"+';'\
                            +"LB_2OG_S_SZ_n_co2_RH (%)"+';'\
                            +"LB_2OG_S_SZ_o_pt_Thk (°C)"+';'+';'\
                                
                            +"LB_2OG_S_SZ_o_reed [Large] "+';'+';'
                            
                            +"LB_2OG_S_E-Energy1 (Wh)"+';'\
                            +"LB_2OG_S_E-Energy2 (Wh)"+';'                      
                            +"LB_2OG_S_E-Energy3 (Wh)"+';'+';'\
                                
                            +"LB_2OG_S_WZ_n_trh_Tair (°C)"+';'\
                            +"LB_2OG_S_WZ_n_trh_RH (%)"+';'\
                            +"LB_2OG_S_WZ_o_reed [X-Large]"+';'+';'
                            
                            +"LB_2OG_S_WZ_s_reed [Medium] "+';'\
                            +"LB_2OG_S_WZ_s_md (0=No, 1=Yes)"+';'+';'
                                
                            +"LB_2OG_S_WZ_w_pt_Thk (°C)"+';'+';'                                

                            +"LB_2OG_S_K_w_reed [Medium] "+';'\
                            +"LB_2OG_S_K_w_trh_Tair (°C)"+';'\
                            +"LB_2OG_S_K_w_trh_RH (%)"+';'+';' 
                                
                            +"LB_2OG_S_K_s_reed  [Small]"+';'+';'\
                                
                            +"LB_2OG_S_F_w_reed1 [Medium]"+';'+';'\
                                
                            +"LB_2OG_S_F_w_reed2 [Medium]"+';'                                
                            +"LB_2OG_S_F_n_md (0=No, 1=Yes)"+';'+';'\
                                
                            +"LB_2OG_S_B_n_pt_Tair (°C)"+';' 
                            +"LB_2OG_S_B_s_trh_Tair (°C)"+';'                    
                            +"LB_2OG_S_B_s_trh_RH (%)"+';'\
                            +"LB_2OG_S_B_n_pt_Thk (°C)"+';'+';' 

                            +"-->Extra-Sensors-->"+';'+';' 

                            +"LB_2OG_N_SZ_s_t_Tair (°C)"+';'+';' 

                            +"LB_2OG_N_WZ_s_t_Tair (°C)"+';'+';' 

                            +"LB_2OG_N_K_w_t_Tair (°C) "+';'+';'\

                            +"LB_2OG_TH_m_t_Tair (°C)"+';'+';'
                            
                            +"DA-W_id_Pyrano_Global W/m^2"+';'\
                            +"DA-W_id_Pyrano_Direct W/m^2"+';'\
                            +"DA-W_id_Pyrano_Diffuse W/m^2"+';'+';'\

                            +"LB_2OG_O_SWK_m_t_Tair (°C)"+ ';'   
                            +"[LB_Black Globe_Metal] LB_2OG_O_SWK_m_tcl_Tsk (°C)"+';'+';'\

                            +"LB_2OG_S_SZ_n_t_Tair  (°C)"+';'+';'                                
                                
                            +"LB_2OG_S_WZ_n_t_Tair (°C)"+';'+';'
                            
                            +"LB_2OG_S_K_w_t_Tair (°C)"+';'+';'
                            
                            +"[Black Globe] LB_2OG_N_SZ_pt_Tsk (°C)"+';'+';'
                            
                            +"[Black Globe] LB_2OG_N_WZ_pt_Tsk (°C)"+';'+';'
                            
                            +"[Black Globe] LB_2OG_S_SZ_pt_Tsk (°C)"+';'+';'
                            
                            +"[Black Globe] LB_2OG_S_WZ_pt_Tsk (°C)"+';'+';'
                            
                            +"LB_2OG_N_WZ_m_trh_Tair (°C)"+';'\
                            +"LB_2OG_N_WZ_m_trh_RH (%)"+';'+';'

                            
                            +"LB_2OG_N_E-Pow1 (W)"+';'\
                            +"LB_2OG_N_E-Pow2 (W)"+';'\
                            +"LB_2OG_N_E-Pow3 (W)"+';'+';'\

                            +"LB_2OG_O_E-Pow1 (W)"+';'\
                            +"LB_2OG_O_E-Pow2 (W)"+';'\
                            +"LB_2OG_O_E-Pow3 (W)"+';'+';'
                            
                            +"LB_2OG_S_E-Pow1 (W)"+';'\
                            +"LB_2OG_S_E-Pow2 (W)"+';'                      
                            +"LB_2OG_S_E-Pow3 (W)"+';'+';'\
                                
                            + '\n')                                           
     


        
    data = open(filename,'a')   
    data.write(ueberschrift)
    data.close()
    #print (ueberschrift)

    ueberschrift_w = ("Datum"+';'\
                            +"Uhrzeit"+ ';'\
                            +"ow_1_id"+';' 
                            +"ow_1_t (°C)"+';'
                            +"ow_1_rh (%)"+';'
                            +"ow_1_ws (m/s)"+';'
                            +"ow_1_gs (m/s)"+';'
                            +"ow_1_rn (mm)"+';'
                            +"ow_1_wd"+';'
                            +"ow_1_btry"+';'                            
                            + '\n')                                           
     
    data = open(filename_w,'a')   
    data.write(ueberschrift_w)
    data.close()
    #print (ueberschrift_w)     

    ueberschrift_Pyrano = ("Datum"+';'\
                            +"Uhrzeit"+ ';'\
                            +"Global W/m^2"+';'\
                            +"Direct W/m^2"+';'\
                            +"Diffuse W/m^2"+';'+';'\
                            + '\n')                                           
     
    data = open(filename_Pyrano,'a')   
    data.write(ueberschrift_Pyrano)
    data.close()
    #print (ueberschrift_w)     
    flag = False
    j = True 
    
    # Schleife für die wiederholte Speicherung der Daten
    while True:
       
        Time_akt = localtime()
        

        
#Sensoren auslesen alle 60 sek
        if ((Time_akt[5] == 0)\
             and flag == False):
             
        # if ((Time_akt[5] == 0 or Time_akt[5] == 5 or Time_akt[5] == 10 or Time_akt[5] == 15 or Time_akt[5] == 20 or Time_akt[5] == 25 or Time_akt[5] == 30 or Time_akt[5] == 35 or Time_akt[5] == 40 or Time_akt[5] == 45 or Time_akt[5] == 50 or Time_akt[5] == 55)\
        #      and flag == False):
    
            flag = True

# Anzahl der Gespeicherten Datensätze auf OLEDausgeben
            
            Anzahl = Anzahl + 1
            
            Nummer_str = str(Anzahl)
            
#Ausgabe ENDE
            
# Erzeugen eines Eintrags im Log File

            log.info('Datensatz ' + str(Anzahl) + ' gespeichert')
            
            #Akutelle Systemzeit auslesen / Get current date and time
            try:
                year, month, day, hour, minute, second, centisecond, weekday, \
              timestamp = rtc.get_date_time()   
            except:
                timestamp = (str(Jahr)+'.'+str(Monat)+'.'+str(Tag)+';'\
                        +str(Stunde)+':'+str(Minute)+':'+str(Sekond)+':'+'00')
                print("Sensor-Alarm: rtc antwortet nicht")                
                year = Jahr
                month = Monat
                day = Tag
                hour = Stunde
                minute = Minute
                second = Sekond

            log.info("Timestamp: " + str(timestamp) + " ms")                
            Jahr = str(Time_akt[0])
            Monat = str(Time_akt[1])
            Tag = str(Time_akt[2])
            Stunde = str(Time_akt[3])
            Minute = str(Time_akt[4])
            Sekond = str(Time_akt[5])      
            
#Sensoren auslesen  
#-----------------------MB1-----------------------------------------#            

            try:
                LB_2OG_N_SZ_n_trh_cdo.set_status_led_config(0)
                LB_2OG_N_SZ_n_trh_Tair = LB_2OG_N_SZ_n_trh_cdo.get_temperature()/100.0
                LB_2OG_N_SZ_n_trh_RH = LB_2OG_N_SZ_n_trh_cdo.get_humidity()/100.0                              
            except:
                LB_2OG_N_SZ_n_trh_Tair = str ("#N/V")
                LB_2OG_N_SZ_n_trh_RH = str ("#N/V")
                print("Sensor-Alarm: LB_2OG_N_SZ_n_trh antwortet nicht")       
  
            try:
                LB_2OG_N_SZ_n_co2_cdo.set_status_led_config(0)
                LB_2OG_N_SZ_n_co2, LB_2OG_N_SZ_n_co2_Tair, LB_2OG_N_SZ_n_co2_RH = LB_2OG_N_SZ_n_co2_cdo.get_all_values()
                LB_2OG_N_SZ_n_co2_Tair = LB_2OG_N_SZ_n_co2_Tair/100.0
                LB_2OG_N_SZ_n_co2_RH = LB_2OG_N_SZ_n_co2_RH/100.0
            except:
                LB_2OG_N_SZ_n_co2 = str ("#N/V")
                LB_2OG_N_SZ_n_co2_Tair = str ("#N/V")
                LB_2OG_N_SZ_n_co2_RH = str ("#N/V")
                print("Sensor-Alarm: LB_2OG_N_SZ_n_co2  antwortet nicht")                    


            try:
                LB_2OG_N_SZ_s_pt_Thk_cdo.set_status_led_config(0)
                LB_2OG_N_SZ_s_pt_Thk = LB_2OG_N_SZ_s_pt_Thk_cdo.get_temperature()/100.0
                
            except:
                LB_2OG_N_SZ_s_pt_Thk = str ("#N/V")
                print("Sensor-Alarm: LB_2OG_N_SZ_s_pt_Thk antwortet nicht")             


#-------Extra Sensor / New Addition---------# 

            try:
                LB_2OG_N_SZ_s_t_cdo.set_status_led_config(0)
                LB_2OG_N_SZ_s_t = LB_2OG_N_SZ_s_t_cdo.get_temperature()/100.0
                
            except:
                LB_2OG_N_SZ_s_t = str ("#N/V")
                print("Sensor-Alarm: LB_2OG_N_SZ_s_t antwortet nicht")    


#-----------------------MB2-----------------------------------------#    
            try:
                LB_2OG_N_SZ_o_reed_cdo.set_status_led_config(0)
                LB_2OG_N_SZ_o_reed_0, LB_2OG_N_SZ_o_reed_1, LB_2OG_N_SZ_o_reed_2, LB_2OG_N_SZ_o_reed_3 = LB_2OG_N_SZ_o_reed_cdo.get_value()
                if LB_2OG_N_SZ_o_reed_0 == False:
                    LB_2OG_N_SZ_o_reed = str ("Closed")
                elif LB_2OG_N_SZ_o_reed_0 == True:
                    LB_2OG_N_SZ_o_reed = str ("Open")
            except:
                LB_2OG_N_SZ_o_reed = str ("#N/V")
                print("Sensor-Alarm: LB_2OG_N_SZ_o_reed antwortet nicht")

#-------Extra Sensor / New Addition---------#                 
            try:
                LB_2OG_N_SZ_pt_Tsk_cdo.set_status_led_config(0)
                LB_2OG_N_SZ_pt_Tsk = LB_2OG_N_SZ_pt_Tsk_cdo.get_temperature()/100.0
                
            except:
                LB_2OG_N_SZ_pt_Tsk = str ("#N/V")
                print("Sensor-Alarm: LB_2OG_N_SZ_pt_Tsk antwortet nicht")             

#-----------------------MB3-----------------------------------------#   

            try:
                voltage_N_el1, current_N_el1, LB_2OG_N_el1, real_power_N_el1, apparent_power_N_el1, reactive_power_N_el1, power_factor_N_el1, frequency_N_el1 = LB_2OG_N_el1_cdo.get_energy_data()    
                voltage_N_el1 = voltage_N_el1/100.0
                current_N_el1 = current_N_el1/100
                
                LB_2OG_N_el1 = LB_2OG_N_el1/100 #LB_2OG_N_E-Energy1 (Wh)
                
                real_power_N_el1 = real_power_N_el1/100 #LB_2OG_N_E-Pow1 (W)
                apparent_power_N_el1 = apparent_power_N_el1/100
                reactive_power_N_el1 = reactive_power_N_el1/100
                power_factor_N_el1 = power_factor_N_el1/100
                frequency_N_el1 = frequency_N_el1/100                    
            except:
                No_Value = ["#NV","#NV","#NV","#NV","#NV","#NV","#NV","#NV"]
                voltage_N_el1, current_N_el1, LB_2OG_N_el1, real_power_N_el1, apparent_power_N_el1, reactive_power_N_el1, power_factor_N_el1, frequency_N_el1 = No_Value                                    
                print("Sensor-Alarm: LB_2OG_N_el1 antwortet nicht")

            try:
                voltage_N_el2, current_N_el2, LB_2OG_N_el2, real_power_N_el2, apparent_power_N_el2, reactive_power_N_el2, power_factor_N_el2, frequency_N_el2 = LB_2OG_N_el2_cdo.get_energy_data()    
                voltage_N_el2 = voltage_N_el2/100.0
                current_N_el2 = current_N_el2/100
                
                LB_2OG_N_el2 = LB_2OG_N_el2/100 #LB_2OG_N_E-Energy2 (Wh)
                
                real_power_N_el2 = real_power_N_el2/100  #LB_2OG_N_E-Pow2 (W)
                apparent_power_N_el2 = apparent_power_N_el2/100
                reactive_power_N_el2 = reactive_power_N_el2/100
                power_factor_N_el2 = power_factor_N_el2/100
                frequency_N_el2 = frequency_N_el2/100                    
            except:
                No_Value = ["#NV","#NV","#NV","#NV","#NV","#NV","#NV","#NV"]
                voltage_N_el2, current_N_el2, LB_2OG_N_el2, real_power_N_el2, apparent_power_N_el2, reactive_power_N_el2, power_factor_N_el2, frequency_N_el2 = No_Value                                    
                print("Sensor-Alarm: LB_2OG_N_el2 antwortet nicht")

            try:
                voltage_N_el3, current_N_el3, LB_2OG_N_el3, real_power_N_el3, apparent_power_N_el3, reactive_power_N_el3, power_factor_N_el3, frequency_N_el3 = LB_2OG_N_el3_cdo.get_energy_data()    
                voltage_N_el3 = voltage_N_el3/100.0
                current_N_el3 = current_N_el3/100
                
                LB_2OG_N_el3 = LB_2OG_N_el3/100 #LB_2OG_N_E-Energy3 (Wh)
                
                real_power_N_el3 = real_power_N_el3/100 #LB_2OG_N_E-Pow3 (W)
                apparent_power_N_el3 = apparent_power_N_el3/100
                reactive_power_N_el3 = reactive_power_N_el3/100
                power_factor_N_el3 = power_factor_N_el3/100
                frequency_N_el3 = frequency_N_el3/100                    
            except:
                No_Value = ["#NV","#NV","#NV","#NV","#NV","#NV","#NV","#NV"]
                voltage_N_el3, current_N_el3, LB_2OG_N_el3, real_power_N_el3, apparent_power_N_el3, reactive_power_N_el3, power_factor_N_el3, frequency_N_el3 = No_Value                                    
                print("Sensor-Alarm: LB_2OG_N_el3 antwortet nicht")

#-----------------------MB4-----------------------------------------#  

            try:
                LB_2OG_N_WZ_s_trh_cdo.set_status_led_config(0)
                LB_2OG_N_WZ_s_trh_Tair = LB_2OG_N_WZ_s_trh_cdo.get_temperature()/100.0
                LB_2OG_N_WZ_s_trh_RH = LB_2OG_N_WZ_s_trh_cdo.get_humidity()/100.0                              
            except:
                LB_2OG_N_WZ_s_trh_Tair = str ("#N/V")
                LB_2OG_N_WZ_s_trh_RH = str ("#N/V")
                print("Sensor-Alarm: LB_2OG_N_WZ_s_trh antwortet nicht")  
                
#-------Extra Sensor / New Addition---------# 
            try:
                LB_2OG_N_WZ_pt_Tsk_cdo.set_status_led_config(0)
                LB_2OG_N_WZ_pt_Tsk = LB_2OG_N_WZ_pt_Tsk_cdo.get_temperature()/100.0
                
            except:
                LB_2OG_N_WZ_pt_Tsk = str ("#N/V")
                print("Sensor-Alarm: LB_2OG_N_WZ_pt_Tsk antwortet nicht")                  
#---#       

            try:
                LB_2OG_N_WZ_s_t_cdo.set_status_led_config(0)
                LB_2OG_N_WZ_s_t = LB_2OG_N_WZ_s_t_cdo.get_temperature()/100.0
                
            except:
                LB_2OG_N_WZ_s_t = str ("#N/V")
                print("Sensor-Alarm: LB_2OG_N_WZ_s_t antwortet nicht") 
                
#-------Extra Sensor / New Addition---------# 

            try:
                LB_2OG_N_WZ_m_trh_cdo.set_status_led_config(0)
                LB_2OG_N_WZ_m_trh_Tair = LB_2OG_N_WZ_m_trh_cdo.get_temperature()/100.0
                LB_2OG_N_WZ_m_trh_RH = LB_2OG_N_WZ_m_trh_cdo.get_humidity()/100.0                              
            except:
                LB_2OG_N_WZ_m_trh_Tair = str ("#N/V")
                LB_2OG_N_WZ_m_trh_RH = str ("#N/V")
                print("Sensor-Alarm: LB_2OG_N_WZ_m_trh antwortet nicht")                  
#------#


            try:
                LB_2OG_N_WZ_o_reed_cdo.set_status_led_config(0)
                LB_2OG_N_WZ_o_reed_0, LB_2OG_N_WZ_o_reed_1, LB_2OG_N_WZ_o_reed_2, LB_2OG_N_WZ_o_reed_3 = LB_2OG_N_WZ_o_reed_cdo.get_value()
                if LB_2OG_N_WZ_o_reed_0 == False:
                    LB_2OG_N_WZ_o_reed = str ("Closed")
                elif LB_2OG_N_WZ_o_reed_0 == True:
                    LB_2OG_N_WZ_o_reed = str ("Open")
                #print (LB_2OG_N_WZ_o_reed)
            except:
                LB_2OG_N_WZ_o_reed = str ("#N/V")
                print("Sensor-Alarm: LB_2OG_N_WZ_o_reed antwortet nicht")

#-----------------------MB5-----------------------------------------#

            try:
                LB_2OG_N_WZ_n_reed_cdo.set_status_led_config(0)
                LB_2OG_N_WZ_n_reed_0, LB_2OG_N_WZ_n_reed_1, LB_2OG_N_WZ_n_reed_2, LB_2OG_N_WZ_n_reed_3 = LB_2OG_N_WZ_n_reed_cdo.get_value()
                if LB_2OG_N_WZ_n_reed_0 == False:
                    LB_2OG_N_WZ_n_reed = str ("Closed")
                elif LB_2OG_N_WZ_n_reed_0 == True:
                    LB_2OG_N_WZ_n_reed = str ("Open")
                #print (LB_2OG_N_WZ_n_reed)
            except:
                LB_2OG_N_WZ_n_reed = str ("#N/V")
                print("Sensor-Alarm: LB_2OG_N_WZ_n_reed antwortet nicht")


            try:
                LB_2OG_N_WZ_n_md_cdo.set_status_led_config(0)
                LB_2OG_N_WZ_n_md = LB_2OG_N_WZ_n_md_cdo.get_motion_detected()
            except:
                LB_2OG_N_WZ_n_md = str ("#N/V")
                print("Sensor-Alarm: LB_2OG_N_WZ_n_md antwortet nicht")

#-----------------------MB6-----------------------------------------#

            try:
                LB_2OG_N_WZ_w_pt_Thk_cdo.set_status_led_config(0)
                LB_2OG_N_WZ_w_pt_Thk = LB_2OG_N_WZ_w_pt_Thk_cdo.get_temperature()/100.0
                
            except:
                LB_2OG_N_WZ_w_pt_Thk = str ("#N/V")
                print("Sensor-Alarm: LB_2OG_N_WZ_w_pt_Thk antwortet nicht")

#-----------------------MB7-----------------------------------------#

            try:
                LB_2OG_N_K_w_trh_cdo.set_status_led_config(0)
                LB_2OG_N_K_w_trh_Tair = LB_2OG_N_K_w_trh_cdo.get_temperature()/100.0
                LB_2OG_N_K_w_trh_RH = LB_2OG_N_K_w_trh_cdo.get_humidity()/100.0                              
            except:
                LB_2OG_N_K_w_trh_Tair = str ("#N/V")
                LB_2OG_N_K_w_trh_RH = str ("#N/V")
                print("Sensor-Alarm: LB_2OG_N_K_w_trh antwortet nicht") 

#-------Extra Sensor / New Addition---------# 

            try:
                LB_2OG_N_K_w_t_cdo.set_status_led_config(0)
                LB_2OG_N_K_w_t = LB_2OG_N_K_w_t_cdo.get_temperature()/100.0
                
            except:
                LB_2OG_N_K_w_t = str ("#N/V")
                print("Sensor-Alarm: LB_2OG_N_K_w_t antwortet nicht")    
#------#


            try:
                LB_2OG_N_K_w_reed_cdo.set_status_led_config(0)
                LB_2OG_N_K_w_reed_0, LB_2OG_N_K_w_reed_1, LB_2OG_N_K_w_reed_2, LB_2OG_N_K_w_reed_3 = LB_2OG_N_K_w_reed_cdo.get_value()
                if LB_2OG_N_K_w_reed_0 == False:
                    LB_2OG_N_K_w_reed = str ("Closed")
                elif LB_2OG_N_K_w_reed_0 == True:
                    LB_2OG_N_K_w_reed = str ("Open")
                #print (LB_2OG_N_K_w_reed)
            except:
                LB_2OG_N_K_w_reed = str ("#N/V")
                print("Sensor-Alarm: LB_2OG_N_K_w_reed antwortet nicht")

#-----------------------MB8-----------------------------------------#
            try:
                LB_2OG_N_K_n_reed_cdo.set_status_led_config(0)
                LB_2OG_N_K_n_reed_0, LB_2OG_N_K_n_reed_1, LB_2OG_N_K_n_reed_2, LB_2OG_N_K_n_reed_3 = LB_2OG_N_K_n_reed_cdo.get_value()
                if LB_2OG_N_K_n_reed_0 == False:
                    LB_2OG_N_K_n_reed = str ("Closed")
                elif LB_2OG_N_K_n_reed_0 == True:
                    LB_2OG_N_K_n_reed = str ("Open")
                #print (LB_2OG_N_K_n_reed)
            except:
                LB_2OG_N_K_n_reed = str ("#N/V")
                print("Sensor-Alarm: LB_2OG_N_K_n_reed antwortet nicht")

#-----------------------MB9-----------------------------------------#                
            try:
                LB_2OG_N_F_w_reed_cdo.set_status_led_config(0)
                LB_2OG_N_F_w_reed_0, LB_2OG_N_F_w_reed_1, LB_2OG_N_F_w_reed_2, LB_2OG_N_F_w_reed_3 = LB_2OG_N_F_w_reed_cdo.get_value()
                if LB_2OG_N_F_w_reed_0 == False:
                    LB_2OG_N_F_w_reed = str ("Closed")
                elif LB_2OG_N_F_w_reed_0 == True:
                    LB_2OG_N_F_w_reed = str ("Open")
                #print (LB_2OG_N_F_w_reed)
            except:
                LB_2OG_N_F_w_reed = str ("#N/V")
                print("Sensor-Alarm: LB_2OG_N_F_w_reed antwortet nicht")

            try:
                LB_2OG_N_F_w_md_cdo.set_status_led_config(0)
                LB_2OG_N_F_w_md = LB_2OG_N_F_w_md_cdo.get_motion_detected()
            except:
                LB_2OG_N_F_w_md = str ("#N/V")
                print("Sensor-Alarm: LB_2OG_N_F_w_md antwortet nicht")
                
#-----------------------MB10-----------------------------------------# 

            try:
                LB_2OG_N_B_n_pt_Tair_cdo.set_status_led_config(0)
                LB_2OG_N_B_n_pt_Tair = LB_2OG_N_B_n_pt_Tair_cdo.get_temperature()/100.0                
            except:
                LB_2OG_N_B_n_pt_Tair = str ("#N/V")
                print("Sensor-Alarm: LB_2OG_N_B_n_pt_Tair antwortet nicht")
                
            try:
                LB_2OG_N_B_n_trh_cdo.set_status_led_config(0)
                LB_2OG_N_B_n_trh_Tair = LB_2OG_N_B_n_trh_cdo.get_temperature()/100.0
                LB_2OG_N_B_n_trh_RH = LB_2OG_N_B_n_trh_cdo.get_humidity()/100.0                              
            except:
                LB_2OG_N_B_n_trh_Tair = str ("#N/V")
                LB_2OG_N_B_n_trh_RH = str ("#N/V")
                print("Sensor-Alarm: LB_2OG_N_B_n_trh antwortet nicht")       

            try:
                LB_2OG_N_B_n_pt_Thk_cdo.set_status_led_config(0)
                LB_2OG_N_B_n_pt_Thk = LB_2OG_N_B_n_pt_Thk_cdo.get_temperature()/100.0
                
            except:
                LB_2OG_N_B_n_pt_Thk = str ("#N/V")
                print("Sensor-Alarm: LB_2OG_N_B_n_pt_Thk antwortet nicht")

#-----------------------MB11-------------------------------MB15PORTD----------#

            try:
                LB_2OG_TH_m_trh_cdo.set_status_led_config(0)
                LB_2OG_TH_m_trh_Tair = LB_2OG_TH_m_trh_cdo.get_temperature()/100.0
                LB_2OG_TH_m_trh_RH = LB_2OG_TH_m_trh_cdo.get_humidity()/100.0                              
            except:
                LB_2OG_TH_m_trh_Tair = str ("#N/V")
                LB_2OG_TH_m_trh_RH = str ("#N/V")
                print("Sensor-Alarm: LB_2OG_TH_m_trh antwortet nicht")      

#-------Extra Sensor / New Addition---------# 

            try:
                LB_2OG_TH_m_t_cdo.set_status_led_config(0)
                LB_2OG_TH_m_t = LB_2OG_TH_m_t_cdo.get_temperature()/100.0
                
            except:
                LB_2OG_TH_m_t = str ("#N/V")
                print("Sensor-Alarm: LB_2OG_TH_m_t antwortet nicht")    
#------#   

            try:                            # Enable station data callbacks
                ow_1_cdo.set_station_callback_configuration(True)
                
                # Register station data callback to function cb_station_data
                ow_1_cdo.register_callback(ow_1_cdo.CALLBACK_STATION_DATA, cb_station_data)
                
            except:
                Ausgabe_w =   (str(year)+','+str(month)+','+str(day)+';'\
                +str(hour)+':'+str(minute)+':'+str(second)+';'   
                +str ("#N/V") +';'
                +str ("#N/V")+';' 
                +str ("#N/V") +';' 
                +str ("#N/V") +';' 
                +str ("#N/V") +';' 
                +str ("#N/V") +';' 
                +str ("#N/V") +';'
                +str ("#N/V") +';'
                +'\n')     
            
                maketrans = Ausgabe_w.maketrans
                Ausgabe_w = Ausgabe_w.translate(maketrans(',.', '.,'))
                
                data = open(filename_w,'a') 
                data.write(Ausgabe_w)
                data.close()
                print("Sensor-Alarm: ow_1 antwortet nicht")

            try:
                LB_DA_W_id_Pyrano_1 = LB_DA_W_id_Pyrano_cdo.get_voltage(0)
                LB_DA_W_id_Pyrano_2 = LB_DA_W_id_Pyrano_cdo.get_voltage(1)
                Global = ((LB_DA_W_id_Pyrano_1/1000.0) * 120)
                Direct = ((LB_DA_W_id_Pyrano_2/1000.0) * 120)
                Diffuse = Global-Direct
            except:
                Global = str ("#N/V")
                Direct = str ("#N/V")
                Diffuse = str ("#N/V")
                print("Sensor-Alarm: LB_DA_W_id_Pyrano antwortet nicht")  

#----#

             
#-----------------------MB12-----------------------------------------#

            try:
                LB_2OG_O_SWK_s_pt_Thk_cdo.set_status_led_config(0)
                LB_2OG_O_SWK_s_pt_Thk = LB_2OG_O_SWK_s_pt_Thk_cdo.get_temperature()/100.0
                
            except:
                LB_2OG_O_SWK_s_pt_Thk = str ("#N/V")
                print("Sensor-Alarm: LB_2OG_O_SWK_s_pt_Thk antwortet nicht")

#-----------------------MB13-----------------------------------------#

            try:
                LB_2OG_O_SWK_o_reed_cdo.set_status_led_config(0)
                LB_2OG_O_SWK_o_reed_0,LB_2OG_O_SWK_o_reed_1, LB_2OG_O_SWK_o_reed_2,LB_2OG_O_SWK_o_reed_3 = LB_2OG_O_SWK_o_reed_cdo.get_value()
                if LB_2OG_O_SWK_o_reed_0 == False:
                    LB_2OG_O_SWK_o_reed = str ("Closed")
                elif LB_2OG_O_SWK_o_reed_0 == True:
                    LB_2OG_O_SWK_o_reed = str ("Open")
                #print (LB_2OG_O_SWK_o_reed)
            except:
                LB_2OG_O_SWK_o_reed = str ("#N/V")
                print("Sensor-Alarm: LB_2OG_O_SWK_o_reed antwortet nicht")

#-----------------------MB14a-----------------------------------------#

            try:
                LB_2OG_O_SWK_m_tir1_cdo.set_status_led_config(0)
                LB_2OG_O_SWK_m_tir1_amb = LB_2OG_O_SWK_m_tir1_cdo.get_ambient_temperature()/10.0
                LB_2OG_O_SWK_m_tir1_obj = LB_2OG_O_SWK_m_tir1_cdo.get_object_temperature()/10.0                
            except:
                LB_2OG_O_SWK_m_tir1_amb = str ("#N/V")
                LB_2OG_O_SWK_m_tir1_obj = str ("#N/V")
                print("Sensor-Alarm: LB_2OG_O_SWK_m_tir1 antwortet nicht")                
                
           
            try:
                LB_2OG_O_SWK_m_tir2_cdo.set_status_led_config(0)
                LB_2OG_O_SWK_m_tir2_amb = LB_2OG_O_SWK_m_tir2_cdo.get_ambient_temperature()/10.0
                LB_2OG_O_SWK_m_tir2_obj = LB_2OG_O_SWK_m_tir2_cdo.get_object_temperature()/10.0                
            except:
                LB_2OG_O_SWK_m_tir2_amb = str ("#N/V")
                LB_2OG_O_SWK_m_tir2_obj = str ("#N/V")
                print("Sensor-Alarm: LB_2OG_O_SWK_m_tir2 antwortet nicht")
                
           
            try:
                LB_2OG_O_SWK_m_tir3_cdo.set_status_led_config(0)
                LB_2OG_O_SWK_m_tir3_amb = LB_2OG_O_SWK_m_tir3_cdo.get_ambient_temperature()/10.0
                LB_2OG_O_SWK_m_tir3_obj = LB_2OG_O_SWK_m_tir3_cdo.get_object_temperature()/10.0                
            except:
                LB_2OG_O_SWK_m_tir3_amb = str ("#N/V")
                LB_2OG_O_SWK_m_tir3_obj = str ("#N/V")
                print("Sensor-Alarm: LB_2OG_O_SWK_m_tir3 antwortet nicht")

           
            try:
                LB_2OG_O_SWK_m_tir4_cdo.set_status_led_config(0)
                LB_2OG_O_SWK_m_tir4_amb = LB_2OG_O_SWK_m_tir4_cdo.get_ambient_temperature()/10.0
                LB_2OG_O_SWK_m_tir4_obj = LB_2OG_O_SWK_m_tir4_cdo.get_object_temperature()/10.0                
            except:
                LB_2OG_O_SWK_m_tir4_amb = str ("#N/V")
                LB_2OG_O_SWK_m_tir4_obj = str ("#N/V")
                print("Sensor-Alarm: LB_2OG_O_SWK_m_tir4 antwortet nicht")


#-----------------------MB14b-----------------------------------------#

            try:
                LB_2OG_O_SWK_m_tir5_cdo.set_status_led_config(0)
                LB_2OG_O_SWK_m_tir5_amb = LB_2OG_O_SWK_m_tir5_cdo.get_ambient_temperature()/10.0
                LB_2OG_O_SWK_m_tir5_obj = LB_2OG_O_SWK_m_tir5_cdo.get_object_temperature()/10.0                
            except:
                LB_2OG_O_SWK_m_tir5_amb = str ("#N/V")
                LB_2OG_O_SWK_m_tir5_obj = str ("#N/V")
                print("Sensor-Alarm: LB_2OG_O_SWK_m_tir5 antwortet nicht")                
                           
            try:
                LB_2OG_O_SWK_m_tir6_cdo.set_status_led_config(0)
                LB_2OG_O_SWK_m_tir6_amb = LB_2OG_O_SWK_m_tir6_cdo.get_ambient_temperature()/10.0
                LB_2OG_O_SWK_m_tir6_obj = LB_2OG_O_SWK_m_tir6_cdo.get_object_temperature()/10.0                
            except:
                LB_2OG_O_SWK_m_tir6_amb = str ("#N/V")
                LB_2OG_O_SWK_m_tir6_obj = str ("#N/V")
                print("Sensor-Alarm: LB_2OG_O_SWK_m_tir6 antwortet nicht")

            try:
                LB_2OG_O_SWK_m_trh_cdo.set_status_led_config(0)
                LB_2OG_O_SWK_m_trh_Tair = LB_2OG_O_SWK_m_trh_cdo.get_temperature()/100.0
                LB_2OG_O_SWK_m_trh_RH = LB_2OG_O_SWK_m_trh_cdo.get_humidity()/100.0                              
            except:
                LB_2OG_O_SWK_m_trh_Tair = str ("#N/V")
                LB_2OG_O_SWK_m_trh_RH = str ("#N/V")
                print("Sensor-Alarm: LB_2OG_O_SWK_m_trh antwortet nicht")       

            try:
                LB_2OG_O_SWK_m_pt_Tsk_cdo.set_status_led_config(0)
                LB_2OG_O_SWK_m_pt_Tsk = LB_2OG_O_SWK_m_pt_Tsk_cdo.get_temperature()/100.0                
            except:
                LB_2OG_O_SWK_m_pt_Tsk = str ("#N/V")
                print("Sensor-Alarm: LB_2OG_O_SWK_m_pt_Tsk antwortet nicht")

#-----------------------MB14c-----------------------------------------#
                
            try:
                LB_2OG_O_SWK_m_co2_cdo.set_status_led_config(0)
                LB_2OG_O_SWK_m_co2, LB_2OG_O_SWK_m_co2_Tair, LB_2OG_O_SWK_m_co2_RH = LB_2OG_O_SWK_m_co2_cdo.get_all_values()
                LB_2OG_O_SWK_m_co2_Tair = LB_2OG_O_SWK_m_co2_Tair/100.0
                LB_2OG_O_SWK_m_co2_RH = LB_2OG_O_SWK_m_co2_RH/100.0
            except:
                LB_2OG_O_SWK_m_co2 = str ("#N/V")
                LB_2OG_O_SWK_m_co2_Tair = str ("#N/V")
                LB_2OG_O_SWK_m_co2_RH = str ("#N/V")
                print("Sensor-Alarm: LB_2OG_O_SWK_m_co2  antwortet nicht")                    
                
            try:
                LB_2OG_O_SWK_m_al_cdo.set_status_led_config(0)
                LB_2OG_O_SWK_m_al = LB_2OG_O_SWK_m_al_cdo.get_illuminance()/100.0
            except:
                LB_2OG_O_SWK_m_al = str ("#N/V")
                print("Sensor-Alarm: LB_2OG_O_SWK_m_al antwortet nicht")                

            try:
                LB_2OG_O_SWK_m_md_cdo.set_status_led_config(0)
                LB_2OG_O_SWK_m_md = LB_2OG_O_SWK_m_md_cdo.get_motion_detected()
            except:
                LB_2OG_O_SWK_m_md = str ("#N/V")
                print("Sensor-Alarm: LB_2OG_O_SWK_m_md antwortet nicht")
                
                
                
                
                

#-----------------------MB14d-----------------------------------------#
#-------Extra Sensor / New Addition---------# 

            try:
                LB_2OG_O_SWK_m_t_cdo.set_status_led_config(0)
                LB_2OG_O_SWK_m_t = LB_2OG_O_SWK_m_t_cdo.get_temperature()/100.0
                
            except:
                LB_2OG_O_SWK_m_t = str ("#N/V")
                print("Sensor-Alarm: LB_2OG_O_SWK_m_t antwortet nicht")    

#-------Extra Sensor / New Addition---------# 

            try:
                LB_2OG_O_SWK_m_tcl_cdo.set_status_led_config(0)
                LB_2OG_O_SWK_m_tcl = LB_2OG_O_SWK_m_tcl_cdo.get_temperature()/100.0
            except:
                LB_2OG_O_SWK_m_tcl = str ("#N/V")
                print("Sensor-Alarm: LB_2OG_O_SWK_m_tcl antwortet nicht")  
                
#-----------------------MB15-----------------------------------------#

            try:
                LB_2OG_O_B_n_pt_Tair_cdo.set_status_led_config(0)
                LB_2OG_O_B_n_pt_Tair = LB_2OG_O_B_n_pt_Tair_cdo.get_temperature()/100.0                
            except:
                LB_2OG_O_B_n_pt_Tair = str ("#N/V")
                print("Sensor-Alarm: LB_2OG_O_B_n_pt_Tair antwortet nicht")
                
            try:
                LB_2OG_O_B_n_trh_cdo.set_status_led_config(0)
                LB_2OG_O_B_n_trh_Tair = LB_2OG_O_B_n_trh_cdo.get_temperature()/100.0
                LB_2OG_O_B_n_trh_RH = LB_2OG_O_B_n_trh_cdo.get_humidity()/100.0                              
            except:
                LB_2OG_O_B_n_trh_Tair = str ("#N/V")
                LB_2OG_O_B_n_trh_RH = str ("#N/V")
                print("Sensor-Alarm: LB_2OG_O_B_n_trh antwortet nicht")
                
            try:
                LB_2OG_O_B_w_pt_Thk_cdo.set_status_led_config(0)
                LB_2OG_O_B_w_pt_Thk = LB_2OG_O_B_w_pt_Thk_cdo.get_temperature()/100.0                
            except:
                LB_2OG_O_B_w_pt_Thk = str ("#N/V")
                print("Sensor-Alarm: LB_2OG_O_B_w_pt_Thk antwortet nicht")

#-----------------------MB15b-----------------------------------------#
            try:
                voltage_O_el1, current_O_el1, LB_2OG_O_el1, real_power_O_el1, apparent_power_O_el1, reactive_power_O_el1, power_factor_O_el1, frequency_O_el1 = LB_2OG_O_el1_cdo.get_energy_data()    
                voltage_O_el1 = voltage_O_el1/100.0
                current_O_el1 = current_O_el1/100
                
                LB_2OG_O_el1 = LB_2OG_O_el1/100     #LB_2OG_O_E-Energy1 (Wh)
                
                real_power_O_el1 = real_power_O_el1/100 #LB_2OG_O_E-Pow1 (W)
                apparent_power_O_el1 = apparent_power_O_el1/100
                reactive_power_O_el1 = reactive_power_O_el1/100
                power_factor_O_el1 = power_factor_O_el1/100
                frequency_O_el1 = frequency_O_el1/100                    
            except:
                No_Value = ["#NV","#NV","#NV","#NV","#NV","#NV","#NV","#NV"]
                voltage_O_el1, current_O_el1, LB_2OG_O_el1, real_power_O_el1, apparent_power_O_el1, reactive_power_O_el1, power_factor_O_el1, frequency_O_el1 = No_Value                                    
                print("Sensor-Alarm: LB_2OG_O_el1 antwortet nicht")


            try:
                voltage_O_el2, current_O_el2, LB_2OG_O_el2, real_power_O_el2, apparent_power_O_el2, reactive_power_O_el2, power_factor_O_el2, frequency_O_el2 = LB_2OG_O_el2_cdo.get_energy_data()    
                voltage_O_el2 = voltage_O_el2/100.0
                current_O_el2 = current_O_el2/100
                
                LB_2OG_O_el2 = LB_2OG_O_el2/100 #LB_2OG_O_E-Energy2 (Wh)
                
                real_power_O_el2 = real_power_O_el2/100 #LB_2OG_O_E-Pow2 (W)
                apparent_power_O_el2 = apparent_power_O_el2/100
                reactive_power_O_el2 = reactive_power_O_el2/100
                power_factor_O_el2 = power_factor_O_el2/100
                frequency_O_el2 = frequency_O_el2/100                    
            except:
                No_Value = ["#NV","#NV","#NV","#NV","#NV","#NV","#NV","#NV"]
                voltage_O_el2, current_O_el2, LB_2OG_O_el2, real_power_O_el2, apparent_power_O_el2, reactive_power_O_el2, power_factor_O_el2, frequency_O_el2 = No_Value                                    
                print("Sensor-Alarm: LB_2OG_O_el2 antwortet nicht")

            try:
                voltage_O_el3, current_O_el3, LB_2OG_O_el3, real_power_O_el3, apparent_power_O_el3, reactive_power_O_el3, power_factor_O_el3, frequency_O_el3 = LB_2OG_O_el3_cdo.get_energy_data()    
                voltage_O_el3 = voltage_O_el3/100.0
                current_O_el3 = current_O_el3/100
                
                LB_2OG_O_el3 = LB_2OG_O_el3/100 #LB_2OG_O_E-Energy3 (Wh)
                
                real_power_O_el3 = real_power_O_el3/100     #LB_2OG_O_E-Pow3 (W)
                apparent_power_O_el3 = apparent_power_O_el3/100
                reactive_power_O_el3 = reactive_power_O_el3/100
                power_factor_O_el3 = power_factor_O_el3/100
                frequency_O_el3 = frequency_O_el3/100                    
            except:
                No_Value = ["#NV","#NV","#NV","#NV","#NV","#NV","#NV","#NV"]
                voltage_O_el3, current_O_el3, LB_2OG_O_el3, real_power_O_el3, apparent_power_O_el3, reactive_power_O_el3, power_factor_O_el3, frequency_O_el3 = No_Value                                    
                print("Sensor-Alarm: LB_2OG_O_el3 antwortet nicht")

#-----------------------MB16-----------------------------------------#

            try:
                LB_2OG_S_SZ_n_trh_cdo.set_status_led_config(0)
                LB_2OG_S_SZ_n_trh_Tair = LB_2OG_S_SZ_n_trh_cdo.get_temperature()/100.0
                LB_2OG_S_SZ_n_trh_RH = LB_2OG_S_SZ_n_trh_cdo.get_humidity()/100.0                              
            except:
                LB_2OG_S_SZ_n_trh_Tair = str ("#N/V")
                LB_2OG_S_SZ_n_trh_RH = str ("#N/V")
                print("Sensor-Alarm: LB_2OG_S_SZ_n_trh antwortet nicht")       

            try:
                LB_2OG_S_SZ_n_co2_cdo.set_status_led_config(0)
                LB_2OG_S_SZ_n_co2, LB_2OG_S_SZ_n_co2_Tair, LB_2OG_S_SZ_n_co2_RH = LB_2OG_S_SZ_n_co2_cdo.get_all_values()
                LB_2OG_S_SZ_n_co2_Tair = LB_2OG_S_SZ_n_co2_Tair/100.0
                LB_2OG_S_SZ_n_co2_RH = LB_2OG_S_SZ_n_co2_RH/100.0
            except:
                LB_2OG_S_SZ_n_co2 = str ("#N/V")
                LB_2OG_S_SZ_n_co2_Tair = str ("#N/V")
                LB_2OG_S_SZ_n_co2_RH = str ("#N/V")
                print("Sensor-Alarm: LB_2OG_S_SZ_n_co2  antwortet nicht")     

            try:
                LB_2OG_S_SZ_o_pt_Thk_cdo.set_status_led_config(0)
                LB_2OG_S_SZ_o_pt_Thk = LB_2OG_S_SZ_o_pt_Thk_cdo.get_temperature()/100.0                
            except:
                LB_2OG_S_SZ_o_pt_Thk = str ("#N/V")
                print("Sensor-Alarm: LB_2OG_S_SZ_o_pt_Thk antwortet nicht")

#-------Extra Sensor / New Addition---------# 

            try:
                LB_2OG_S_SZ_n_t_cdo.set_status_led_config(0)
                LB_2OG_S_SZ_n_t = LB_2OG_S_SZ_n_t_cdo.get_temperature()/100.0
                
            except:
                LB_2OG_S_SZ_n_t = str ("#N/V")
                print("Sensor-Alarm: LB_2OG_S_SZ_n_t antwortet nicht")    

#-----------------------MB17-----------------------------------------#

            try:
                LB_2OG_S_SZ_o_reed_cdo.set_status_led_config(0)
                LB_2OG_S_SZ_o_reed_0, LB_2OG_S_SZ_o_reed_1, LB_2OG_S_SZ_o_reed_2, LB_2OG_S_SZ_o_reed_3 = LB_2OG_S_SZ_o_reed_cdo.get_value()
                if LB_2OG_S_SZ_o_reed_0 == False:
                    LB_2OG_S_SZ_o_reed = str ("Closed")
                elif LB_2OG_S_SZ_o_reed_0 == True:
                    LB_2OG_S_SZ_o_reed = str ("Open")

            except:
                LB_2OG_S_SZ_o_reed = str ("#N/V")
                print("Sensor-Alarm: LB_2OG_S_SZ_o_reed antwortet nicht")

#-------Extra Sensor / New Addition---------#                 
            try:
                LB_2OG_S_SZ_pt_Tsk_cdo.set_status_led_config(0)
                LB_2OG_S_SZ_pt_Tsk = LB_2OG_S_SZ_pt_Tsk_cdo.get_temperature()/100.0
                
            except:
                LB_2OG_S_SZ_pt_Tsk = str ("#N/V")
                print("Sensor-Alarm: LB_2OG_S_SZ_pt_Tsk antwortet nicht")    
#-----------------------MB18-----------------------------------------#


            try:
                voltage_S_el1, current_S_el1, LB_2OG_S_el1, real_power_S_el1, apparent_power_S_el1, reactive_power_S_el1, power_factor_S_el1, frequency_S_el1 = LB_2OG_S_el1_cdo.get_energy_data()    
                voltage_S_el1 = voltage_S_el1/100.0
                current_S_el1 = current_S_el1/100
                
                LB_2OG_S_el1 = LB_2OG_S_el1/100 #LB_2OG_S_E-Energy1 (Wh)
                
                real_power_S_el1 = real_power_S_el1/100 #LB_2OG_S_E-Pow1 (W)
                apparent_power_S_el1 = apparent_power_S_el1/100
                reactive_power_S_el1 = reactive_power_S_el1/100
                power_factor_S_el1 = power_factor_S_el1/100
                frequency_S_el1 = frequency_S_el1/100                    
            except:
                No_Value = ["#NV","#NV","#NV","#NV","#NV","#NV","#NV","#NV"]
                voltage_S_el1, current_S_el1, LB_2OG_S_el1, real_power_S_el1, apparent_power_S_el1, reactive_power_S_el1, power_factor_S_el1, frequency_S_el1 = No_Value                                    
                print("Sensor-Alarm: LB_2OG_S_el1 antwortet nicht")


            try:
                voltage_S_el2, current_S_el2, LB_2OG_S_el2, real_power_S_el2, apparent_power_S_el2, reactive_power_S_el2, power_factor_S_el2, frequency_S_el2 = LB_2OG_S_el2_cdo.get_energy_data()    
                voltage_S_el2 = voltage_S_el2/100.0
                current_S_el2 = current_S_el2/100
                
                LB_2OG_S_el2 = LB_2OG_S_el2/100 #LB_2OG_S_E-Energy2 (Wh)
                
                real_power_S_el2 = real_power_S_el2/100 #LB_2OG_S_E-Pow2 (W)
                apparent_power_S_el2 = apparent_power_S_el2/100
                reactive_power_S_el2 = reactive_power_S_el2/100
                power_factor_S_el2 = power_factor_S_el2/100
                frequency_S_el2 = frequency_S_el2/100                    
            except:
                No_Value = ["#NV","#NV","#NV","#NV","#NV","#NV","#NV","#NV"]
                voltage_S_el2, current_S_el2, LB_2OG_S_el2, real_power_S_el2, apparent_power_S_el2, reactive_power_S_el2, power_factor_S_el2, frequency_S_el2 = No_Value                                    
                print("Sensor-Alarm: LB_2OG_S_el2 antwortet nicht")

            try:
                voltage_S_el3, current_S_el3, LB_2OG_S_el3, real_power_S_el3, apparent_power_S_el3, reactive_power_S_el3, power_factor_S_el3, frequency_S_el3 = LB_2OG_S_el3_cdo.get_energy_data()    
                voltage_S_el3 = voltage_S_el3/100.0
                current_S_el3 = current_S_el3/100
                
                LB_2OG_S_el3 = LB_2OG_S_el3/100 #LB_2OG_S_E-Energy3 (Wh
                
                real_power_S_el3 = real_power_S_el3/100 #LB_2OG_S_E-Pow3 (W)
                apparent_power_S_el3 = apparent_power_S_el3/100
                reactive_power_S_el3 = reactive_power_S_el3/100
                power_factor_S_el3 = power_factor_S_el3/100
                frequency_S_el3 = frequency_S_el3/100                    
            except:
                No_Value = ["#NV","#NV","#NV","#NV","#NV","#NV","#NV","#NV"]
                voltage_S_el3, current_S_el3, LB_2OG_S_el3, real_power_S_el3, apparent_power_S_el3, reactive_power_S_el3, power_factor_S_el3, frequency_S_el3 = No_Value                                    
                print("Sensor-Alarm: LB_2OG_S_el3 antwortet nicht")

#-----------------------MB19-----------------------------------------#

            try:
                LB_2OG_S_WZ_n_trh_cdo.set_status_led_config(0)
                LB_2OG_S_WZ_n_trh_Tair = LB_2OG_S_WZ_n_trh_cdo.get_temperature()/100.0
                LB_2OG_S_WZ_n_trh_RH = LB_2OG_S_WZ_n_trh_cdo.get_humidity()/100.0                              
            except:
                LB_2OG_S_WZ_n_trh_Tair = str ("#N/V")
                LB_2OG_S_WZ_n_trh_RH = str ("#N/V")
                print("Sensor-Alarm: LB_2OG_S_WZ_n_trh antwortet nicht")       

#-------Extra Sensor / New Addition---------# 

            try:
                LB_2OG_S_WZ_n_t_cdo.set_status_led_config(0)
                LB_2OG_S_WZ_n_t = LB_2OG_S_WZ_n_t_cdo.get_temperature()/100.0
                
            except:
                LB_2OG_S_WZ_n_t = str ("#N/V")
                print("Sensor-Alarm: LB_2OG_S_WZ_n_t antwortet nicht")   

            try:
                LB_2OG_S_WZ_pt_Tsk_cdo.set_status_led_config(0)
                LB_2OG_S_WZ_pt_Tsk = LB_2OG_S_WZ_pt_Tsk_cdo.get_temperature()/100.0
                
            except:
                LB_2OG_S_WZ_pt_Tsk = str ("#N/V")
                print("Sensor-Alarm: LB_2OG_S_WZ_pt_Tsk antwortet nicht") 

#-----------------------MB19b-----------------------------------------#
            try:
                LB_2OG_S_WZ_o_reed_cdo.set_status_led_config(0)
                LB_2OG_S_WZ_o_reed_0, LB_2OG_S_WZ_o_reed_1, LB_2OG_S_WZ_o_reed_2, LB_2OG_S_WZ_o_reed_3 = LB_2OG_S_WZ_o_reed_cdo.get_value()
                if LB_2OG_S_WZ_o_reed_0 == False:
                    LB_2OG_S_WZ_o_reed = str ("Closed")
                elif LB_2OG_S_WZ_o_reed_0 == True:
                    LB_2OG_S_WZ_o_reed = str ("Open")
                #print (LB_2OG_S_WZ_o_reed)
            except:
                LB_2OG_S_WZ_o_reed = str ("#N/V")
                print("Sensor-Alarm: LB_2OG_S_WZ_o_reed antwortet nicht")


#-----------------------MB20-----------------------------------------#

            try:
                LB_2OG_S_WZ_s_reed_cdo.set_status_led_config(0)
                LB_2OG_S_WZ_s_reed_0, LB_2OG_S_WZ_s_reed_1, LB_2OG_S_WZ_s_reed_2, LB_2OG_S_WZ_s_reed_3 = LB_2OG_S_WZ_s_reed_cdo.get_value()
                if LB_2OG_S_WZ_s_reed_0 == False:
                    LB_2OG_S_WZ_s_reed = str ("Closed")
                elif LB_2OG_S_WZ_s_reed_0 == True:
                    LB_2OG_S_WZ_s_reed = str ("Open")
                #print (LB_2OG_S_WZ_s_reed)
            except:
                LB_2OG_S_WZ_s_reed = str ("#N/V")
                print("Sensor-Alarm: LB_2OG_S_WZ_s_reed antwortet nicht")
                
            try:
                LB_2OG_S_WZ_s_md_cdo.set_status_led_config(0)
                LB_2OG_S_WZ_s_md = LB_2OG_S_WZ_s_md_cdo.get_motion_detected()
            except:
                LB_2OG_S_WZ_s_md = str ("#N/V")
                print("Sensor-Alarm: LB_2OG_S_WZ_s_md antwortet nicht")                

            try:
                LB_2OG_S_WZ_w_pt_Thk_cdo.set_status_led_config(0)
                LB_2OG_S_WZ_w_pt_Thk = LB_2OG_S_WZ_w_pt_Thk_cdo.get_temperature()/100.0                
            except:
                LB_2OG_S_WZ_w_pt_Thk = str ("#N/V")
                print("Sensor-Alarm: LB_2OG_S_WZ_w_pt_Thk antwortet nicht")

#-----------------------MB21 Not used-----------------------------------------#

#-----------------------MB22-----------------------------------------#
                                
            try:
                LB_2OG_S_K_w_trh_cdo.set_status_led_config(0)
                LB_2OG_S_K_w_trh_Tair = LB_2OG_S_K_w_trh_cdo.get_temperature()/100.0
                LB_2OG_S_K_w_trh_RH = LB_2OG_S_K_w_trh_cdo.get_humidity()/100.0                              
            except:
                LB_2OG_S_K_w_trh_Tair = str ("#N/V")
                LB_2OG_S_K_w_trh_RH = str ("#N/V")
                print("Sensor-Alarm: LB_2OG_S_K_w_trh antwortet nicht")     

    #-------Extra Sensor / New Addition---------# 

            try:
                LB_2OG_S_K_w_t_cdo.set_status_led_config(0)
                LB_2OG_S_K_w_t = LB_2OG_S_K_w_t_cdo.get_temperature()/100.0
                
            except:
                LB_2OG_S_K_w_t = str ("#N/V")
                print("Sensor-Alarm: LB_2OG_S_K_w_t antwortet nicht")   

#-----------------------MB22b-----------------------------------------#
            try:
                LB_2OG_S_K_w_reed_cdo.set_status_led_config(0)
                LB_2OG_S_K_w_reed_0, LB_2OG_S_K_w_reed_1, LB_2OG_S_K_w_reed_2, LB_2OG_S_K_w_reed_3 = LB_2OG_S_K_w_reed_cdo.get_value()
                if LB_2OG_S_K_w_reed_0 == False:
                    LB_2OG_S_K_w_reed = str ("Closed")
                elif LB_2OG_S_K_w_reed_0 == True:
                    LB_2OG_S_K_w_reed = str ("Open")
                #print (LB_2OG_S_K_w_reed)
            except:
                LB_2OG_S_K_w_reed = str ("#N/V")
                print("Sensor-Alarm: LB_2OG_S_K_w_reed antwortet nicht")    
 
    
#-----------------------MB23-----------------------------------------#
            try:
                LB_2OG_S_K_s_reed_cdo.set_status_led_config(0)
                LB_2OG_S_K_s_reed_0, LB_2OG_S_K_s_reed_1, LB_2OG_S_K_s_reed_2, LB_2OG_S_K_s_reed_3 = LB_2OG_S_K_s_reed_cdo.get_value()
                if LB_2OG_S_K_s_reed_0 == False:
                    LB_2OG_S_K_s_reed = str ("Closed")
                elif LB_2OG_S_K_s_reed_0 == True:
                    LB_2OG_S_K_s_reed = str ("Open")
                #print (LB_2OG_S_K_s_reed)
            except:
                LB_2OG_S_K_s_reed = str ("#N/V")
                print("Sensor-Alarm: LB_2OG_S_K_s_reed antwortet nicht")
       
#-----------------------MB24-----------------------------------------#

            try:
                LB_2OG_S_F_w_reed1_cdo.set_status_led_config(0)
                LB_2OG_S_F_w_reed1_0, LB_2OG_S_F_w_reed1_1, LB_2OG_S_F_w_reed1_2, LB_2OG_S_F_w_reed1_3 = LB_2OG_S_F_w_reed1_cdo.get_value()
                if LB_2OG_S_F_w_reed1_0 == False:
                    LB_2OG_S_F_w_reed1 = str ("Closed")
                elif LB_2OG_S_F_w_reed1_0 == True:
                    LB_2OG_S_F_w_reed1 = str ("Open")
                #print (LB_2OG_S_F_w_reed1)
            except:
                LB_2OG_S_F_w_reed1 = str ("#N/V")
                print("Sensor-Alarm: LB_2OG_S_F_w_reed1 antwortet nicht")
       
        
#-----------------------MB25-----------------------------------------#

            try:
                LB_2OG_S_F_w_reed2_cdo.set_status_led_config(0)
                LB_2OG_S_F_w_reed2_0, LB_2OG_S_F_w_reed2_1, LB_2OG_S_F_w_reed2_2, LB_2OG_S_F_w_reed2_3 = LB_2OG_S_F_w_reed2_cdo.get_value()
                if  LB_2OG_S_F_w_reed2_0 == False:
                     LB_2OG_S_F_w_reed2 = str ("Closed")
                elif  LB_2OG_S_F_w_reed2_0 == True:
                     LB_2OG_S_F_w_reed2 = str ("Open")
               # print ( LB_2OG_S_F_w_reed2)
            except:
                 LB_2OG_S_F_w_reed2 = str ("#N/V")
                 print("Sensor-Alarm:  LB_2OG_S_F_w_reed2 antwortet nicht")


#-----------------------MB25b-----------------------------------------#
            try:
                LB_2OG_S_F_n_md_cdo.set_status_led_config(0)
                LB_2OG_S_F_n_md = LB_2OG_S_F_n_md_cdo.get_motion_detected()
            except:
                LB_2OG_S_F_n_md = str ("#N/V")
                print("Sensor-Alarm: LB_2OG_S_F_n_md antwortet nicht")

#-----------------------MB26-----------------------------------------#
            try:
                LB_2OG_S_B_n_pt_Tair_cdo.set_status_led_config(0)
                LB_2OG_S_B_n_pt_Tair = LB_2OG_S_B_n_pt_Tair_cdo.get_temperature()/100.0                
            except:
                LB_2OG_S_B_n_pt_Tair = str ("#N/V")
                print("Sensor-Alarm: LB_2OG_S_B_n_pt_Tair antwortet nicht")

            try:
                LB_2OG_S_B_s_trh_cdo.set_status_led_config(0)
                LB_2OG_S_B_s_trh_Tair = LB_2OG_S_B_s_trh_cdo.get_temperature()/100.0
                LB_2OG_S_B_s_trh_RH = LB_2OG_S_B_s_trh_cdo.get_humidity()/100.0                              
            except:
                LB_2OG_S_B_s_trh_Tair = str ("#N/V")
                LB_2OG_S_B_s_trh_RH = str ("#N/V")
                print("Sensor-Alarm: LB_2OG_S_B_s_trh antwortet nicht")   
                
            try:
                LB_2OG_S_B_n_pt_Thk_cdo.set_status_led_config(0)
                LB_2OG_S_B_n_pt_Thk = LB_2OG_S_B_n_pt_Thk_cdo.get_temperature()/100.0
                
            except:
                LB_2OG_S_B_n_pt_Thk = str ("#N/V")
                print("Sensor-Alarm: LB_2OG_S_B_n_pt_Thk antwortet nicht")                
          

#Sensordaten speichern                
            Ausgabe =   (str(day)+','+str(month)+','+str(year)+';'\
                        +str(hour)+':'+str(minute)+':'+str(second)+';'
                        +" "+';'\
                        +str(LB_2OG_N_SZ_n_trh_Tair) +';'\
                        +str(LB_2OG_N_SZ_n_trh_RH) +';'\
                        +str(LB_2OG_N_SZ_n_co2) +';'\
                        +str(LB_2OG_N_SZ_n_co2_Tair) +';'\
                        +str(LB_2OG_N_SZ_n_co2_RH) +';'\
                        +str(LB_2OG_N_SZ_s_pt_Thk) +';'\
                        +" "+';'                           
                        +str(LB_2OG_N_SZ_o_reed) +';'\
                        +" "+';'  
                        +str(LB_2OG_N_el1) +';'\
                        +str(LB_2OG_N_el2) +';'\
                        +str(LB_2OG_N_el3) +';'\
                        +" "+';'
                        +str(LB_2OG_N_WZ_s_trh_Tair) +';'\
                        +str(LB_2OG_N_WZ_s_trh_RH) +';'\
                        +str(LB_2OG_N_WZ_o_reed) +';'\
                        +" "+';'    
                        +str(LB_2OG_N_WZ_n_reed) +';'\
                        +str(LB_2OG_N_WZ_n_md) +';'\
                        +" "+';'   
                        +str(LB_2OG_N_WZ_w_pt_Thk) +';'\
                        +" "+';'    
                        +str(LB_2OG_N_K_w_trh_Tair) +';'\
                        +str(LB_2OG_N_K_w_trh_RH) +';'\
                        +str(LB_2OG_N_K_w_reed) +';'\
                        +" "+';'    
                        +str(LB_2OG_N_K_n_reed) +';'\
                        +" "+';'   
                        +str(LB_2OG_N_F_w_reed) +';'\
                        +str(LB_2OG_N_F_w_md) +';'\
                        +" "+';'    
                        +str(LB_2OG_N_B_n_pt_Tair) +';'\
                        +str(LB_2OG_N_B_n_trh_Tair) +';'\
                        +str(LB_2OG_N_B_n_trh_RH) +';'\
                        +str(LB_2OG_N_B_n_pt_Thk) +';'\
                        +" "+';'    
                        +str(LB_2OG_TH_m_trh_Tair) +';'\
                        +str(LB_2OG_TH_m_trh_RH) +';'\
                        +" "+';'    
                        +str(LB_2OG_O_SWK_s_pt_Thk) +';'\
                        +" "+';'
                        +str(LB_2OG_O_SWK_o_reed) +';'\
                        +" "+';'                              
                        +str(LB_2OG_O_SWK_m_tir1_amb) +';'\
                        +str(LB_2OG_O_SWK_m_tir1_obj) +';'\
                        +str(LB_2OG_O_SWK_m_tir2_amb) +';'\
                        +str(LB_2OG_O_SWK_m_tir2_obj) +';'\
                        +str(LB_2OG_O_SWK_m_tir3_amb ) +';'\
                        +str(LB_2OG_O_SWK_m_tir3_obj) +';'\
                        +str(LB_2OG_O_SWK_m_tir4_amb) +';'\
                        +str(LB_2OG_O_SWK_m_tir4_obj) +';'\
                        +" "+';'    
                        +str(LB_2OG_O_SWK_m_tir5_amb) +';'\
                        +str(LB_2OG_O_SWK_m_tir5_obj) +';'\
                        +str(LB_2OG_O_SWK_m_tir6_amb ) +';'\
                        +str(LB_2OG_O_SWK_m_tir6_obj) +';'\
                        +str(LB_2OG_O_SWK_m_trh_Tair) +';'\
                        +str(LB_2OG_O_SWK_m_trh_RH) +';'\
                        +str(LB_2OG_O_SWK_m_pt_Tsk) +';'\
                        +" "+';'                            
                        +str(LB_2OG_O_SWK_m_co2) +';'\
                        +str(LB_2OG_O_SWK_m_co2_Tair) +';'\
                        +str(LB_2OG_O_SWK_m_co2_RH) +';'\
                        +str(LB_2OG_O_SWK_m_al) +';'\
                        +str(LB_2OG_O_SWK_m_md) +';'                    
                        +" "+';'
                        +str(LB_2OG_O_B_n_pt_Tair) +';'\
                        +str(LB_2OG_O_B_n_trh_Tair) +';'\
                        +str(LB_2OG_O_B_n_trh_RH) +';'\
                        +str(LB_2OG_O_B_w_pt_Thk) +';'\
                        +" "+';'
                        +str(LB_2OG_O_el1) +';'\
                        +str(LB_2OG_O_el2) +';'\
                        +str(LB_2OG_O_el3) +';'\
                        +" "+';'                                                 
                        +str(LB_2OG_S_SZ_n_trh_Tair) +';'\
                        +str(LB_2OG_S_SZ_n_trh_RH) +';'\
                        +str(LB_2OG_S_SZ_n_co2) +';'\
                        +str(LB_2OG_S_SZ_n_co2_Tair) +';'\
                        +str(LB_2OG_S_SZ_n_co2_RH) +';'\
                        +str(LB_2OG_S_SZ_o_pt_Thk) +';'\
                        +" "+';'                        
                        +str(LB_2OG_S_SZ_o_reed) +';'\
                        +" "+';'                        
                        +str(LB_2OG_S_el1) +';'\
                        +str(LB_2OG_S_el2) +';'\
                        +str(LB_2OG_S_el3) +';'\
                        +" "+';'                        
                        +str(LB_2OG_S_WZ_n_trh_Tair) +';'\
                        +str(LB_2OG_S_WZ_n_trh_RH) +';'\
                        +str(LB_2OG_S_WZ_o_reed) +';'\
                        +" "+';'
                        +str(LB_2OG_S_WZ_s_reed) +';'\
                        +str(LB_2OG_S_WZ_s_md ) +';'\
                        +" "+';'    
                        +str(LB_2OG_S_WZ_w_pt_Thk) +';'\
                        +" "+';'    
                        +str(LB_2OG_S_K_w_reed) +';'\
                        +str(LB_2OG_S_K_w_trh_Tair) +';'\
                        +str(LB_2OG_S_K_w_trh_RH) +';'\
                        +" "+';'    
                        +str(LB_2OG_S_K_s_reed ) +';'\
                        +" "+';'    
                        +str(LB_2OG_S_F_w_reed1) +';'\
                        +" "+';'
                        +str(LB_2OG_S_F_w_reed2) +';'\
                        +str(LB_2OG_S_F_n_md) +';'\
                        +" "+';'    
                        +str(LB_2OG_S_B_n_pt_Tair) +';'\
                        +str(LB_2OG_S_B_s_trh_Tair) +';'\
                        +str(LB_2OG_S_B_s_trh_RH) +';'\
                        +str(LB_2OG_S_B_n_pt_Thk) +';'\
                        +" "+';'  
                        +"-->----->----->"+';'
                        +" "+';'                            
                        +str(LB_2OG_N_SZ_s_t) +';'\
                        +" "+';'  
                        +str(LB_2OG_N_WZ_s_t) +';'\
                        +" "+';'    
                        +str(LB_2OG_N_K_w_t) +';'\
                        +" "+';'    
                        +str(LB_2OG_TH_m_t) +';'\
                        +" "+';'
                        +str(Global) +';'\
                        +str(Direct) +';'\
                        +str(Diffuse) +';'                            
                        +" "+';' 
                        +str(LB_2OG_O_SWK_m_t) +';' 
                        +str(LB_2OG_O_SWK_m_tcl) +';'\
                        +" "+';'    
                        +str(LB_2OG_S_SZ_n_t) +';'\
                        +" "+';'    
                        +str(LB_2OG_S_WZ_n_t) +';'\
                        +" "+';'                        
                        +str(LB_2OG_S_K_w_t) +';'\
                        +" "+';'
                        +str(LB_2OG_N_SZ_pt_Tsk) +';'\
                        +" "+';'
                        +str(LB_2OG_N_WZ_pt_Tsk) +';'\
                        +" "+';' 
                        +str(LB_2OG_S_SZ_pt_Tsk) +';'\
                        +" "+';'
                        +str(LB_2OG_S_WZ_pt_Tsk) +';'\
                        +" "+';'
                        +str(LB_2OG_N_WZ_s_trh_Tair) +';'\
                        +str(LB_2OG_N_WZ_s_trh_RH) +';'\
                        +" "+';' 
                        +str(real_power_N_el1) +';'\
                        +str(real_power_N_el2) +';'\
                        +str(real_power_N_el3) +';'\
                        +" "+';'
                        +str(real_power_O_el1) +';'\
                        +str(real_power_O_el2) +';'\
                        +str(real_power_O_el3) +';'\
                        +" "+';'                            
                        +str(real_power_S_el1) +';'\
                        +str(real_power_S_el2) +';'\
                        +str(real_power_S_el3) +';'\
                        +" "+';'                                
                        +'\n')     

    
            maketrans = Ausgabe.maketrans
            Ausgabe = Ausgabe.translate(maketrans(',.', '.,'))

            data = open(filename,'a') 
            data.write(Ausgabe)
            data.close()
            #print(Ausgabe)
            
            Ausgabe_Pyrano =   (str(year)+','+str(month)+','+str(day)+';'\
                        +str(hour)+':'+str(minute)+':'+str(second)+';'   
                        +str(Global ) +';'\
                        +str(Direct) +';'\
                        +str(Diffuse) +';'
                        +" "+';' 
                        +'\n')     
        
            maketrans_P = Ausgabe_Pyrano.maketrans
            Ausgabe_Pyrano = Ausgabe_Pyrano.translate(maketrans_P(',.', '.,'))
        
            data = open(filename_Pyrano,'a') 
            data.write(Ausgabe_Pyrano)
            data.close()

 #Festlegen des Zeit Intervalls (hier alle 5sek)
        if ((Time_akt[5] >= 1 and Time_akt[5] < 5) or\
             (Time_akt[5] >= 6 and Time_akt[5] < 10) or\
             (Time_akt[5] >= 11 and Time_akt[5] < 15) or\
             (Time_akt[5] >= 16 and Time_akt[5] < 20) or\
             (Time_akt[5] >= 21 and Time_akt[5] < 25) or\
             (Time_akt[5] >= 26 and Time_akt[5] < 30) or\
             (Time_akt[5] >= 31 and Time_akt[5] < 35) or\
             (Time_akt[5] >= 36 and Time_akt[5] < 40) or\
             (Time_akt[5] >= 41 and Time_akt[5] < 45) or\
             (Time_akt[5] >= 46 and Time_akt[5] < 50) or\
             (Time_akt[5] >= 51 and Time_akt[5] < 55) or\
             (Time_akt[5] >= 56 and Time_akt[5] < 60)):
                 
            flag = False   
                
        if j == False:
            break    


    ipcon.disconnect()