
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

MB1 = "6s7jQr" 
 
#MB2 = "Brick not needed - sensor connected to MB1"  # 

MB3 = "646rco"  # 

MB4 = "6LDqax"  # 

MB5 = "5XaSdr"  # 

#MB6 = "Brick not needed - sensor connected to MB5" # 

MB7 = "6Kve5v" # 

#MB8 = "Brick not needed - sensor connected to MB7" # 

MB9 = "6Lfyvg" #

MB10 = "6RNpv4" # 

#MB11 = "Brick not needed - sensor connected to MB15" # 

MB12 = "6RN528" # 

#MB13 = "not needed"  #

MB14a = "64thHw"  #

MB14b = "6R3HnK"  #

MB14c = "6R455i"  #

MB15 = "6KT3t4" #

MB16 = "64sTzJ" #

MB17 = "6JKEyz" #

MB18 = "69EgDB" #

MB19 = "6KS97n" #

MB20 = "5WrSHp" #

MB21 = "69EC3v" #

MB22 = "6tcGsD" #

MB23 = "645R2B" #

MB24 = "6JMZHt" #

MB25 = "64sXeA" #

MB26 = "6m9gDk" #

MB27 = "69Ggjz" #
#_________________________________________________#

#Northern_Apt SZ part 1 ____ MB1 _____
UID1 = "NFB"	  #MW_2OG_N_SZ_n_trh_TairRH
UID2 = "MdT"	  #MW_2OG_N_SZ_n_co2_LQ
UID3 = "Nn3"  	#MW_2OG_N_SZ_s_pt_Thk
UID4 = "Q4P"  #MW_2OG_N_SZ_o_reed_Fganz
 
#Northern_Apt SZ part 2  ____ MB2 _____ "not needed"

#UID5 = "" reserved
#UID6 = "" reserved
#UID7 = "" reserved
#UID8 = "" reserved

#Northern_Apt el ____ MB3 _____
UID9 = "Qi9"	  #MW_2OG_N_el1_Strom
UID10 = "Qjn"	#MW_2OG_N_el2_Strom
UID11 = "Qk1"	#MW_2OG_N_el3_Strom
#UID12 = "" reserved

#Northern_Apt WZ part 1 ____ MB4 _____
UID13 = "NQn"	#MW_2OG_N_WZ_s_trh_TairRH
UID14 = "27gpHX"	  #MW_2OG_N_WZ_o_reed_Fganz
UID15 = "V9w" # [#MW_2OG_N_SZ_pt_Tsk] New Black Globe Thermometer 
UID16 = "V3t" #[#MW_2OG_N_WZ_pt_Tsk] New Black Globe Thermometer  New add


#Northern_Apt WZ part 2 ____ MB5 _____
UID17 = "TFRKK"	#MW_2OG_N_WZ_n_reed_Fganz
UID18 = "J8S"	#MW_2OG_N_WZ_n_md_Anw
UID19 = "NhP"	#MW_2OG_N_WZ_w_pt_Thk
#UID20 = "" reserved

#Northern_Apt WZ part 3 ____ MB6 _____ "not needed"
#UID21 = "" reserved
#UID22 = "" reserved
#UID23 = "" reserved
#UID24 = "" reserved

#Northern_Apt K part 1 ____ MB7 _____
UID25 = "NRG"	#MW_2OG_N_K_w_trh_TairRH
UID26 = "Q6b"	#MW_2OG_N_K_w_reed_Fganz
UID27 = "2rmauH" #MW_2OG_N_K_n_reed_Fganz
#UID28 = "" reserved

#Northern_Apt K part2 ____ MB8 _____
#UID29 = ""	reserved
#UID30 = "" reserved
#UID31 = "" reserved
#UID32 = "" reserved

#Northern_Apt F ____ MB9 _____
UID33 = "Q5Z"	#MW_2OG_N_F_w_reed_Fganz
UID34 = "J9c"	#MW_2OG_N_F_w_md_Anw
#UID35 = "" reserved
#UID36 = "" reserved

#Northern_Apt B ____ MB10 _____
UID37 = "NcJ"	#MW_2OG_N_B_n_pt_Tair
UID38 = "NG1"	#MW_2OG_N_B_n_trh_TairRH
UID39 = "NfP"	#MW_2OG_N_B_n_pt_Thk
#UID40 = "" reserved

##Northern_Apt hzww
#UID41= ""	#MW_2OG_N_hz_Heiz (reserved)
#UID42= ""	#MW_2OG_N_ww_TWW (reserved)
#UID43 = "" reserved
#UID44 = "" reserved

#_________________________________________________#

#2nd Floor Stairway ____ MB11 _____
#UID45 = ""	reserved
#UID46 = "" reserved
#UID47 = "" reserved
#UID48 = "" reserved

#_________________________________________________#

#Central_Apt part 1 ____ MB12 _____

UID49= "SsS"	#MW_2OG_O_SWK_s_pt_Thk
UID50 = "PXd9e" #MW_2OG_O_SWK_o_reed_Fganz
#UID51 = "" New sensors 17.01.2022
#UID52 = "" //

#Central_Apt part 2 ____ MB13 _____
#UID53 = ""	//
#UID54 = "" //
#UID55 = "" //
#UID56 = "" //

#Central_Apt part 3 ____ MB14a _____
UID57 = "Ryp"	#MW_2OG_O_SWK_m_tir1_Twd
UID58 = "Rw6"	#MW_2OG_O_SWK_m_tir2_Twd
UID59 = "Rwt"	#MW_2OG_O_SWK_m_tir3_Twd
UID60 = "Rxo"	#MW_2OG_O_SWK_m_tir4_Twd

#Central_Apt part 3  ____ MB14b _____	
UID61 = "RyE"	#MW_2OG_O_SWK_m_tir5_Twd
UID62 = "Rwe"	#MW_2OG_O_SWK_m_tir6_Twd
UID63 = "NRC"	#MW_2OG_O_SWK_m_trh_TairRH
UID64 = "Stb"	#MW_2OG_O_SWK_m_pt_Tsk "Black Globe Thermometer"

#Central_Apt part 3  ____ MB14c _____	
UID65 = "McA"	#MW_2OG_O_SWK_m_co2_LQ
UID66 = "Pah"	#MW_2OG_O_SWK_m_al_BS
UID67 = "J8J"	#MW_2OG_O_SWK_m_md_Anw
UID68 = "FEo"	#MW_2OG_O_SWK_m_rtc_Zeit / rtc

#Central_Apt B ____ MB15 _____
UID69 = "Sti"	#MW_2OG_O_B_n_pt_Tair
UID70 = "NH4"	#MW_2OG_O_B_n_trh_TairRH
UID71 = "Ssr"  #MW_2OG_O_B_w_pt_Thk
UID72 = "NJd" #MW_2OG_TH_m_trh_TairRH

#_________________________________________________#

#Southern_Apt SZ part 1 ____ MB16 _____

UID73 = "NSG"	#MW_2OG_S_SZ_n_trh_TairRH
UID74 = "Me8"	#MW_2OG_S_SZ_n_co2_LQ
UID75 = "NeF"	#MW_2OG_S_SZ_o_pt_Thk
UID76 = "V8J" # [#MW_2OG_S_SZ_pt_Tsk] New Black Globe Thermometer 


#Southern_Apt SZ part 2 ____ MB17 _____
UID77 = "23YXF4"	#MW_2OG_S_SZ_o_reed_Fganz
#UID78 = "" reserved
#UID79 = "" reserved
#UID80 = "" reserved

#Southern_Apt el ____ MB18 _____
UID81 = "QjU"	#MW_2OG_S_el1_Strom
UID82 = "Qj2"	#MW_2OG_S_el2_Strom
UID83 = "QjQ"	#MW_2OG_S_el3_Strom
#UID84 = "" reserved

#Southern_Apt WZ part 1 ____ MB19 _____ 
UID85 = "NRW"	#MW_2OG_S_WZ_n_trh_TairRH
UID86 = "2n3qWZ"	#MW_2OG_S_WZ_o_reed_Fganz
#UID87 = ""	reserved
#UID88 = "" reserved

#Southern_Apt WZ part 2 ____ MB20 _____ 
UID89 = "Q6c"	#MW_2OG_S_WZ_s_reed_Fganz
UID90 = "MP3"	#MW_2OG_S_WZ_s_md_Anw
UID91 = "V9d"	#[MW_2OG_S_WZ_pt_Tsk] New Black Globe Thermometer
#UID91 = ""	reserved
#UID92 = "" reserved

#Southern_Apt WZ part 3 ____ MB21 _____ 
UID93 = "NfQ"	#MW_2OG_S_WZ_w_pt_Thk
#UID94 = ""	reserved
#UID95 = "" reserved
#UID96 = "" reserved

#Southern_Apt K part 1 ____ MB22 _____ 
UID97= "ZBNT8"	#MW_2OG_S_K_w_reed_Fganz
UID98= "NER"	   #MW_2OG_S_K_w_trh_TairRH
#UID99 = "" reserved
#UID100 = "" reserved

#Southern_Apt K part 2  ____ MB23 _____ 
UID101 = "2csnda" #MW_2OG_S_K_s_reed_Fganz
#UID102 = "" reserved
#UID103 = "" reserved
#UID104 = "" reserved

#Southern_Apt F part 1 ____ MB24 _____ 
UID105 = "Q5S"	#MW_2OG_S_F_w_reed1_Fganz
#UID106 = "" reserved
#UID107 = "" reserved
#UID108 = "" reserved

#Southern_Apt F part 2 ____ MB25 _____ 
UID109= "Q4Z"	#MW_2OG_S_F_w_reed2_Fganz
UID110= "MNG"	#MW_2OG_S_F_n_md_Anw
#UID111 = "" reserved
#UID112 = "" reserved

#Southern_Apt B ____ MB26 _____ 
UID113 = "Njm"	#MW_2OG_S_B_n_pt_Tair
UID114 = "NFL"	#MW_2OG_S_B_s_trh_TairRH
UID115 = "Njz"	#MW_2OG_S_B_n_pt_Thk
#UID116 = "" reserved

#Central_Apt part 4 ____ MB27 _____
UID117 = "Qi7"	#MW_2OG_O_el1_Strom
UID118 = "Qj1"	#MW_2OG_O_el2_Strom
UID119 = "QiG" #MW_2OG_O_el3_Strom
#UID120 = "" reserved

##Southern_Apt hzww
#UID121 = ""	#MW_2OG_S_hz_Heiz
#UID122 = ""	#MW_2OG_S_ww_TWW
#UID123 = "" reserved
#UID124 = "" reserved
UID126 = "S9L"#Isolator SZNord (MB1)

## New addition 17.01.2022

UID51 = "CLD" #MW_2OG_O_SWK_al1_BS
UID52 = "Pca"#MW_2OG_O_SWK_al2_BS
UID53 = "WRM"	#MW_2OG_O_SWK_al3_BS
UID54 = "P32" #MW_2OG_O_SWK_al4_BS
UID55 = "PbC" #MW_2OG_O_SWK_al5_BS
UID56 = "NSh" #MW_2OG_O_SWK_m_trh1_TairRH

UID127 = "NEB" #MW_Dach_trh1_TairRH
UID128 = "NJA" #MW_Dach_trh2_TairRH

import os.path
import time
from time import *
from time import sleep
import logging as log
log.basicConfig(level=log.INFO)

from tinkerforge.ip_connection import IPConnection
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
from tinkerforge.bricklet_isolator import BrickletIsolator
    
    
if __name__ == "__main__":

    ipcon = IPConnection()

#_________________________________________________#
    
    MB1_cdo = BrickMaster(MB1, ipcon) # Create device object
    
    #MB2_cdo = BrickMaster(MB2, ipcon) # Create device object
    
    MB3_cdo = BrickMaster(MB3, ipcon) # Create device object
    
    MB4_cdo = BrickMaster(MB4, ipcon) # Create device object
    
    MB5_cdo = BrickMaster(MB5, ipcon) # Create device object
    
    #MB6_cdo = BrickMaster(MB6, ipcon) # Create device object
    
    MB7_cdo = BrickMaster(MB7, ipcon) # Create device object
    
    #MB8_cdo = BrickMaster(MB8, ipcon) # Create device object
    
    MB9_cdo = BrickMaster(MB9, ipcon) # Create device object
    
    MB10_cdo = BrickMaster(MB10, ipcon) # Create device object
    
    #MB11_cdo = BrickMaster(MB11, ipcon) # Create device object
    
    MB12_cdo = BrickMaster(MB12, ipcon) # Create device object
    
    #MB13_cdo = BrickMaster(MB13, ipcon) # Create device object
    
    MB14a_cdo = BrickMaster(MB14a, ipcon) # Create device object
    
    MB14b_cdo = BrickMaster(MB14b, ipcon) # Create device object
    
    MB14c_cdo = BrickMaster(MB14c, ipcon) # Create device object
    
    MB15_cdo = BrickMaster(MB15, ipcon) # Create device object
    
    MB16_cdo = BrickMaster(MB16, ipcon) # Create device object

    MB17_cdo = BrickMaster(MB17, ipcon) # Create device object
    
    MB18_cdo = BrickMaster(MB18, ipcon) # Create device object
    
    MB19_cdo = BrickMaster(MB19, ipcon) # Create device object
    
    MB20_cdo = BrickMaster(MB20, ipcon) # Create device object
    
    MB21_cdo = BrickMaster(MB21, ipcon) # Create device object
    
    MB22_cdo = BrickMaster(MB22, ipcon) # Create device object
    
    MB23_cdo = BrickMaster(MB23, ipcon) # Create device object
    
    MB24_cdo = BrickMaster(MB24, ipcon) # Create device object
    
    MB25_cdo = BrickMaster(MB25, ipcon) # Create device object
    
    MB26_cdo = BrickMaster(MB26, ipcon) # Create device object
    
    MB27_cdo = BrickMaster(MB27, ipcon) # Create device object
#_________________________________________________#

#Northern_Apt SZ part 1 ____ MB1 _____
    MW_2OG_N_SZ_n_trh_cdo = BrickletHumidityV2(UID1, ipcon) # Create device object
    MW_2OG_N_SZ_n_co2_cdo = BrickletCO2V2(UID2, ipcon) # Create device object
    MW_2OG_N_SZ_s_pt_Thk_cdo = BrickletPTCV2(UID3, ipcon) # Create device object
    MW_2OG_N_SZ_o_reed_cdo = BrickletIO4V2(UID4, ipcon) # Create device object
#Northern_Apt SZ part 2  ____ MB2 _____

#Northern_Apt el ____ MB3 _____
    MW_2OG_N_el1_cdo = BrickletEnergyMonitor(UID9, ipcon) # Create device object 
    MW_2OG_N_el2_cdo = BrickletEnergyMonitor(UID10, ipcon) # Create device object 
    MW_2OG_N_el3_cdo = BrickletEnergyMonitor(UID11, ipcon) # Create device object 

#Northern_Apt WZ part 1 ____ MB4 _____
    MW_2OG_N_WZ_s_trh_cdo = BrickletHumidityV2(UID13, ipcon) # Create device object
    MW_2OG_N_WZ_o_reed_cdo = BrickletIO4V2(UID14, ipcon) # Create device object
    MW_2OG_N_SZ_pt_Tsk_cdo = BrickletPTCV2(UID15, ipcon) # Create device object 
    MW_2OG_N_WZ_pt_Tsk_cdo = BrickletPTCV2(UID16, ipcon) # Create device object
#Northern_Apt WZ part 2 ____ MB5 _____
    MW_2OG_N_WZ_n_reed_cdo = BrickletIO4V2(UID17, ipcon) # Create device object
    MW_2OG_N_WZ_n_md_cdo = BrickletMotionDetectorV2(UID18, ipcon) # Create device object
    MW_2OG_N_WZ_w_pt_Thk_cdo = BrickletPTCV2(UID19, ipcon) # Create device object  
        
#Northern_Apt WZ part 3 ____ MB6 _____   
  
#Northern_Apt K part 1 ____ MB7 _____
    MW_2OG_N_K_w_trh_cdo = BrickletHumidityV2(UID25, ipcon) # Create device object
    MW_2OG_N_K_w_reed_cdo = BrickletIO4V2(UID26, ipcon) # Create device object
    MW_2OG_N_K_n_reed_cdo = BrickletIO4V2(UID27, ipcon) # Create device object
#Northern_Apt K part2 ____ MB8 _____

#Northern_Apt F ____ MB9 _____
    MW_2OG_N_F_w_reed_cdo = BrickletIO4V2(UID33, ipcon) # Create device object
    MW_2OG_N_F_w_md_cdo = BrickletMotionDetectorV2(UID34, ipcon) # Create device object
 
#Northern_Apt B ____ MB10 _____
    MW_2OG_N_B_n_pt_Tair_cdo = BrickletPTCV2(UID37, ipcon) # Create device object
    MW_2OG_N_B_n_trh_cdo = BrickletHumidityV2(UID38, ipcon) # Create device object
    MW_2OG_N_B_n_pt_Thk_cdo = BrickletPTCV2(UID39, ipcon) # Create device object
    
#2nd Floor Stairway ____ MB11 _____
    
#Central_Apt part 1 ____ MB12 _____
    MW_2OG_O_SWK_s_pt_Thk_cdo = BrickletPTCV2(UID49, ipcon) # Create device object
    MW_2OG_O_SWK_o_reed_cdo = BrickletIO4V2(UID50, ipcon) # Create device object
    
#Central_Apt part 2 ____ MB13 _____

#Central_Apt part 3 ____ MB14a _____
    MW_2OG_O_SWK_m_tir1_cdo = BrickletTemperatureIRV2(UID57, ipcon) # Create device object
    MW_2OG_O_SWK_m_tir2_cdo = BrickletTemperatureIRV2(UID58, ipcon) # Create device object
    MW_2OG_O_SWK_m_tir3_cdo = BrickletTemperatureIRV2(UID59, ipcon) # Create device object
    MW_2OG_O_SWK_m_tir4_cdo = BrickletTemperatureIRV2(UID60, ipcon) # Create device object    

#Central_Apt part 3  ____ MB14c _____	
    MW_2OG_O_SWK_m_tir5_cdo = BrickletTemperatureIRV2(UID61, ipcon) # Create device object
    MW_2OG_O_SWK_m_tir6_cdo = BrickletTemperatureIRV2(UID62, ipcon) # Create device object   
    MW_2OG_O_SWK_m_trh_cdo = BrickletHumidityV2(UID63, ipcon) # Create device object
    MW_2OG_O_SWK_m_pt_Tsk_cdo = BrickletPTCV2(UID64, ipcon) # Create device object
     
#Central_Apt part 3  ____ MB14b _____	
    MW_2OG_O_SWK_m_co2_cdo = BrickletCO2V2(UID65, ipcon) # Create device object
    MW_2OG_O_SWK_m_al_cdo = BrickletAmbientLightV3(UID66, ipcon) # Create device object
    MW_2OG_O_SWK_m_md_cdo = BrickletMotionDetectorV2(UID67, ipcon) # Create device object
    rtc = BrickletRealTimeClockV2(UID68, ipcon) #MW_2OG_O_SWK_m_rtc

#Central_Apt B ____ MB15 _____
    MW_2OG_O_B_n_pt_Tair_cdo = BrickletPTCV2(UID69, ipcon) # Create device object
    MW_2OG_O_B_n_trh_cdo = BrickletHumidityV2(UID70, ipcon) # Create device object
    MW_2OG_O_B_w_pt_Thk_cdo = BrickletPTCV2(UID71, ipcon) # Create device object
    MW_2OG_TH_m_trh_cdo = BrickletHumidityV2(UID72, ipcon) # Create device object
    
#Southern_Apt SZ part 1 ____ MB16 _____
    MW_2OG_S_SZ_n_trh_cdo = BrickletHumidityV2(UID73, ipcon) # Create device object
    MW_2OG_S_SZ_n_co2_cdo = BrickletCO2V2(UID74, ipcon) # Create device object
    MW_2OG_S_SZ_o_pt_Thk_cdo = BrickletPTCV2(UID75, ipcon) # Create device object
    MW_2OG_S_SZ_pt_Tsk_cdo = BrickletPTCV2(UID76, ipcon) # Create device object
#Southern_Apt SZ part 2 ____ MB17 _____
    MW_2OG_S_SZ_o_reed_cdo = BrickletIO4V2(UID77, ipcon) # Create device object    
    
#Southern_Apt el ____ MB18 _____   
    MW_2OG_S_el1_cdo = BrickletEnergyMonitor(UID81, ipcon) # Create device object 
    MW_2OG_S_el2_cdo = BrickletEnergyMonitor(UID82, ipcon) # Create device object 
    MW_2OG_S_el3_cdo = BrickletEnergyMonitor(UID83, ipcon) # Create device object    
    
#Southern_Apt WZ part 1 ____ MB19 _____ 
    MW_2OG_S_WZ_n_trh_cdo = BrickletHumidityV2(UID85, ipcon) # Create device object
    MW_2OG_S_WZ_o_reed_cdo = BrickletIO4V2(UID86, ipcon) # Create device object

#Southern_Apt WZ part 2 ____ MB20 _____ 
    MW_2OG_S_WZ_s_reed_cdo = BrickletIO4V2(UID89, ipcon) # Create device object
    MW_2OG_S_WZ_s_md_cdo = BrickletMotionDetectorV2(UID90, ipcon) # Create device object
    MW_2OG_S_WZ_pt_Tsk_cdo = BrickletPTCV2(UID91, ipcon) # Create device object
#Southern_Apt WZ part 3 ____ MB21 _____ 
    MW_2OG_S_WZ_w_pt_Thk_cdo = BrickletPTCV2(UID93, ipcon) # Create device object

#Southern_Apt K part 1 ____ MB22 _____ 
    MW_2OG_S_K_w_reed_cdo = BrickletIO4V2(UID97, ipcon) # Create device object
    MW_2OG_S_K_w_trh_cdo = BrickletHumidityV2(UID98, ipcon) # Create device object
#Southern_Apt K part 2  ____ MB23 _____ 
    MW_2OG_S_K_s_reed_cdo = BrickletIO4V2(UID101, ipcon) # Create device object 
    
#Southern_Apt F part 1 ____ MB24 _____ 
    MW_2OG_S_F_w_reed1_cdo = BrickletIO4V2(UID105, ipcon) # Create device object   
    
#Southern_Apt F part 2 ____ MB25 _____ 
    MW_2OG_S_F_w_reed2_cdo = BrickletIO4V2(UID109, ipcon) # Create device object     
    MW_2OG_S_F_n_md_cdo = BrickletMotionDetectorV2(UID110, ipcon) # Create device object
    
#Southern_Apt B ____ MB26 _____ 
    MW_2OG_S_B_n_pt_Tair_cdo = BrickletPTCV2(UID113, ipcon) # Create device object
    MW_2OG_S_B_s_trh_cdo = BrickletHumidityV2(UID114, ipcon) # Create device object
    MW_2OG_S_B_n_pt_Thk_cdo = BrickletPTCV2(UID115, ipcon) # Create device object    

#Central_Apt part 4 ____ MB27 _____(MB15B)
    MW_2OG_O_el1_cdo = BrickletEnergyMonitor(UID117, ipcon) # Create device object 
    MW_2OG_O_el2_cdo = BrickletEnergyMonitor(UID118, ipcon) # Create device object 
    MW_2OG_O_el3_cdo = BrickletEnergyMonitor(UID119, ipcon) # Create device object  

    i = BrickletIsolator(UID126, ipcon) # Create device object
#_________________________________________________#    

## New addition 17.01.2022

    MW_2OG_O_SWK_al1_cdo = BrickletAmbientLightV3(UID51, ipcon) # Create device object
    MW_2OG_O_SWK_al2_cdo = BrickletAmbientLightV3(UID52, ipcon) # Create device object
    MW_2OG_O_SWK_al3_cdo = BrickletAmbientLightV3(UID53, ipcon) # Create device object
    MW_2OG_O_SWK_al4_cdo = BrickletAmbientLightV3(UID54, ipcon) # Create device object
    MW_2OG_O_SWK_al5_cdo = BrickletAmbientLightV3(UID55, ipcon) # Create device object
    MW_2OG_O_SWK_m_trh1_cdo = BrickletHumidityV2(UID56, ipcon) # Create device object

    MW_Dach_trh1_cdo = BrickletHumidityV2(UID127, ipcon) # Create device object
    MW_Dach_trh2_cdo = BrickletHumidityV2(UID128, ipcon) # Create device object    
# Connect to brickd
    ipcon.connect(HOST, PORT) # Don't use device before ipcon is connected
    
    try:
        MB1_cdo.disable_status_led()
    
    except:
        
        print ("Master Brick MB1 does not answer")

    # try:
    #     MB2_cdo.disable_status_led()

    # except:
        
    #     print ("Master Brick MB2 does not answer")
        
    try:
        MB3_cdo.disable_status_led()
    
    except:
        
        print ("Master Brick MB3 does not answer")

    try:
        MB4_cdo.disable_status_led()

    except:
        
        print ("Master Brick MB4 does not answer")

    try:
        MB5_cdo.disable_status_led()
    
    except:
        
        print ("Master Brick MB5 does not answer")

    # try:
    #     MB6_cdo.disable_status_led()
    
    # except:
        
    #     print ("Master Brick MB6 does not answer")

    try:
        MB7_cdo.disable_status_led()
    
    except:
        
        print ("Master Brick MB7 does not answer")
        
    # try:
    #     MB8_cdo.disable_status_led()
    
    # except:
        
    #     print ("Master Brick MB8 does not answer")

    try:
        MB9_cdo.disable_status_led()
    
    except:
        
        print ("Master Brick MB9 does not answer")


    try:
        MB10_cdo.disable_status_led()
    
    except:
        
        print ("Master Brick MB10 does not answer")

    # try:
    #     MB11_cdo.disable_status_led()
    
    # except:
        
    #     print ("Master Brick MB11 does not answer")

    try:
        MB12_cdo.disable_status_led()
    
    except:
        
        print ("Master Brick MB12 does not answer")

    # try:
    #     MB13_cdo.disable_status_led()
    
    # except:
        
    #     print ("Master Brick MB13 does not answer")

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
        MB15_cdo.disable_status_led()
    
    except:
        
        print ("Master Brick MB15 does not answer")                

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
        MB20_cdo.disable_status_led()
    
    except:
        
        print ("Master Brick MB20 does not answer")  
        
    try:
        MB21_cdo.disable_status_led()
    
    except:
        
        print ("Master Brick MB21 does not answer")  

    try:
        MB22_cdo.disable_status_led()
    
    except:
        
        print ("Master Brick MB22 does not answer")  

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
        MB26_cdo.disable_status_led()
    
    except:
        
        print ("Master Brick MB26 does not answer")
        
    try:
        MB27_cdo.disable_status_led()
    
    except:
        
        print ("Master Brick MB27 does not answer")
    try:
        i.set_status_led_config(0)
                       
    except:
        print("Isolator MB1 does not answer") 
        
 # Get current date and time
    Time_akt = localtime()
    Jahr = str(Time_akt[0])
    Monat = str(Time_akt[1])
    Tag = str(Time_akt[2])
    Stunde = str(Time_akt[3])
    Minute = str(Time_akt[4])
    Sekond = str(Time_akt[5]) 

    save_path = r'E:\Data-reserve\MW'
    title = (Jahr+'_'+Monat+'_'+Tag+'_MW'+'.csv')    # festlegen des Dateinamens
    filename = os.path.join(save_path, title)       
    
        
    ueberschrift = ("Date"+';'\
                            +"Time"+';'+';'\
                                
                            +"MW_2OG_N_SZ_n_trh_Tair (°C)"+';'\
                            +"MW_2OG_N_SZ_n_trh_RH (%)"+';'\
                            +"MW_2OG_N_SZ_n_co2 (ppm)"+';'\
                            +"MW_2OG_N_SZ_n_co2_Tair (°C)"+';'\
                            +"MW_2OG_N_SZ_n_co2_RH (%)"+';'\
                            +"MW_2OG_N_SZ_s_pt_Thk (°C)"+';'+';'   
                                
                            +"MW_2OG_N_SZ_o_reed [Large] "+';'+';'
                            
                            +"MW_2OG_N_E-Energy1 (Wh)"+';'\
                            +"MW_2OG_N_E-Energy2 (Wh)"+';'\
                            +"MW_2OG_N_E-Energy3 (Wh)"+';'+';'\
                                
                            +"MW_2OG_N_WZ_s_trh_Tair (°C)"+';'\
                            +"MW_2OG_N_WZ_s_trh_RH (%)"+';'\
                            +"MW_2OG_N_WZ_o_reed [Large] "+';'+';'\
                                
                            +"MW_2OG_N_WZ_n_reed [Large] "+';'\
                            +"MW_2OG_N_WZ_n_md (0=No, 1=Yes)"+';'+';'\
                                
                            +"MW_2OG_N_WZ_w_pt_Thk (°C)"+';'+';'\
                                
                            +"MW_2OG_N_K_w_trh_Tair (°C)"+';'\
                            +"MW_2OG_N_K_w_trh_RH (%)"+';'\
                            +"MW_2OG_N_K_w_reed [Medium] "+';'+';'\
                                
                            +"MW_2OG_N_K_n_reed [Small]"+';'+';'\
                                
                            +"MW_2OG_N_F_w_reed [Medium]"+';'                              
                            +"MW_2OG_N_F_w_md (0=No, 1=Yes)"+';'+';'
                            
                            +"MW_2OG_N_B_n_pt_Tair (°C)"+';'
                            +"MW_2OG_N_B_n_trh_Tair (°C)"+';'
                            +"MW_2OG_N_B_n_trh_RH (%)"+';'\
                            +"MW_2OG_N_B_n_pt_Thk (°C)"+';'+';'
                            
                            +"MW_2OG_TH_m_trh_Tair (°C)"+';'\
                            +"MW_2OG_TH_m_trh_RH (%)"+';'+';'\
                                
                            +"MW_2OG_O_SWK_s_pt_Thk (°C)"+';'+';'\
                                
                            +"MW_2OG_O_SWK_o_reed [Large]"+';'+';'\
                            
                            +"MW_2OG_O_SWK_m_tir1_amb (°C)"+';'
                            +"MW_2OG_O_SWK_m_tir1_obj (°C)"+';'
                            +"MW_2OG_O_SWK_m_tir2_amb (°C)"+';'
                            +"MW_2OG_O_SWK_m_tir2_obj (°C)"+';'
                            +"MW_2OG_O_SWK_m_tir3_amb (°C)"+';'
                            +"MW_2OG_O_SWK_m_tir3_obj (°C)"+';'
                            +"MW_2OG_O_SWK_m_tir4_amb (°C)"+';'
                            +"MW_2OG_O_SWK_m_tir4_obj (°C)"+';'+';'

                            +"MW_2OG_O_SWK_m_tir5_amb (°C)"+';'
                            +"MW_2OG_O_SWK_m_tir5_obj (°C)"+';'
                            +"MW_2OG_O_SWK_m_tir6_amb (°C)"+';'
                            +"MW_2OG_O_SWK_m_tir6_obj (°C)"+';'
                            +"MW_2OG_O_SWK_m_trh_Tair (°C)"+';'
                            +"MW_2OG_O_SWK_m_trh_RH (%)"+';'                            
                            +"[MW_Black Globe] MW_2OG_O_SWK_m_pt_Tsk (°C)"+';'+';'
                            
                            +"MW_2OG_O_SWK_m_co2 (ppm)"+';'\
                            +"MW_2OG_O_SWK_m_co2_Tair (°C)"+';'\
                            +"MW_2OG_O_SWK_m_co2_RH (%)"+';'\
                            +"MW_2OG_O_SWK_m_al (lux)"+ ';'+';'   
                            +"MW_2OG_O_SWK_m_md (0=No, 1=Yes)"+';'\
                                
                            +"MW_2OG_O_B_n_pt_Tair (°C)"+';'\
                            +"MW_2OG_O_B_n_trh_Tair (°C)"+';'\
                            +"MW_2OG_O_B_n_trh_RH (%)"+';'\
                            +"MW_2OG_O_B_w_pt_Thk (°C)"+';'+';'\

                            +"MW_2OG_O_E-Energy1 (Wh)"+';'\
                            +"MW_2OG_O_E-Energy2 (Wh)"+';'\
                            +"MW_2OG_O_E-Energy3 (Wh)"+';'+';'   
                                
                            +"MW_2OG_S_SZ_n_trh_Tair (°C)"+';'
                            +"MW_2OG_S_SZ_n_trh_RH (%)"+';'\
                            +"MW_2OG_S_SZ_n_co2 (ppm)"+';'\
                            +"MW_2OG_S_SZ_n_co2_Tair (°C)"+';'\
                            +"MW_2OG_S_SZ_n_co2_RH (%)"+';'\
                            +"MW_2OG_S_SZ_o_pt_Thk (°C)"+';'+';'\
                                
                            +"MW_2OG_S_SZ_o_reed [Large] "+';'+';'
                            
                            +"MW_2OG_S_E-Energy1 (Wh)"+';'\
                            +"MW_2OG_S_E-Energy2 (Wh)"+';'                      
                            +"MW_2OG_S_E-Energy3 (Wh)"+';'+';'\
                                
                            +"MW_2OG_S_WZ_n_trh_Tair (°C)"+';'\
                            +"MW_2OG_S_WZ_n_trh_RH (%)"+';'\
                            +"MW_2OG_S_WZ_o_reed [X-Large]"+';'+';'
                            
                            +"MW_2OG_S_WZ_s_reed [Medium] "+';'\
                            +"MW_2OG_S_WZ_s_md (0=No, 1=Yes)"+';'+';'\
                                
                            +"MW_2OG_S_WZ_w_pt_Thk (°C)"+';'+';'\
                                
                            +"MW_2OG_S_K_w_reed [Medium] "+';'+';'\
                            +"MW_2OG_S_K_w_trh_Tair (°C)"+';'\
                            +"MW_2OG_S_K_w_trh_RH (%)"+';'                            

                                
                            +"MW_2OG_S_K_s_reed  [Small]"+';'+';'\
                                
                            +"MW_2OG_S_F_w_reed1 [Medium]"+';'+';'\
                                
                            +"MW_2OG_S_F_w_reed2 [Medium]"+';'\
                            +"MW_2OG_S_F_n_md (0=No, 1=Yes)"+';'+';'\
                                
                            +"MW_2OG_S_B_n_pt_Tair (°C)"+';' 
                            +"MW_2OG_S_B_s_trh_Tair (°C)"+';'                    
                            +"MW_2OG_S_B_s_trh_RH (%)"+';'\
                            +"MW_2OG_S_B_n_pt_Thk (°C)"+';'+';'
                            
                            +"-->Extra-Sensors-->"+';'+';'
                            
                            +"[Black Globe] MW_2OG_N_SZ_pt_Tsk (°C)"+';'+';'
                            
                            +"[Black Globe] MW_2OG_N_WZ_pt_Tsk (°C)"+';'+';'
                            
                            +"[Black Globe] MW_2OG_S_SZ_pt_Tsk (°C)"+';'+';'
                            
                            +"[Black Globe] MW_2OG_S_WZ_pt_Tsk (°C)"+';'+';'
                            
                            +"MW_2OG_N_E-Pow1 (W)"+';'\
                            +"MW_2OG_N_E-Pow2 (W)"+';'\
                            +"MW_2OG_N_E-Pow3 (W)"+';'+';'\

                            +"MW_2OG_O_E-Pow1 (W)"+';'\
                            +"MW_2OG_O_E-Pow2 (W)"+';'\
                            +"MW_2OG_O_E-Pow3 (W)"+';'+';'
                            
                            +"MW_2OG_S_E-Pow1 (W)"+';'\
                            +"MW_2OG_S_E-Pow2 (W)"+';'                      
                            +"MW_2OG_S_E-Pow3 (W)"+';'+';'\
                            
                            +"MW_2OG_O_SWK_al1 (lux)"+ ';'
                            +"MW_2OG_O_SWK_al2 (lux)"+ ';'
                            +"MW_2OG_O_SWK_al3 (lux)"+ ';'
                            +"MW_2OG_O_SWK_al4 (lux)"+ ';'
                            +"MW_2OG_O_SWK_al5 (lux)"+ ';'                             
                            +"MW_2OG_O_SWK_m_trh1_Tair (°C)"+';'                    
                            +"MW_2OG_O_SWK_m_trh1_RH (%)"+';' +';'  
                            
                            +"MW_Dach_trh1_Tair (°C)"+';'
                            +"MW_Dach_trh1_RH (%)"+';'
                            +"MW_Dach_trh2_Tair (°C)"+';'
                            +"MW_Dach_trh2_RH (%)"+';'
                              
                            + '\n')                                           
     
    data = open(filename,'a')   
    data.write(ueberschrift)
    data.close()
    #print (ueberschrift)
    
    
    flag = False
    j = True 
    
    # Schleife für die wiederholte Speicherung der Daten
    while True:
       
        Time_akt = localtime()
        

        
#Sensoren auslesen alle 30 sek
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

#-------Extra Sensor 1 / New Addition---------#                 
            try:
                MW_2OG_N_SZ_pt_Tsk_cdo.set_status_led_config(0)
                MW_2OG_N_SZ_pt_Tsk = MW_2OG_N_SZ_pt_Tsk_cdo.get_temperature()/100.0
                
            except:
                MW_2OG_N_SZ_pt_Tsk = str ("#N/V")
                print("Sensor-Alarm: MW_2OG_N_SZ_pt_Tsk antwortet nicht")   
                
#-------Extra Sensor2 / New Addition---------# 
            try:
                MW_2OG_N_WZ_pt_Tsk_cdo.set_status_led_config(0)
                MW_2OG_N_WZ_pt_Tsk = MW_2OG_N_WZ_pt_Tsk_cdo.get_temperature()/100.0
                
            except:
                MW_2OG_N_WZ_pt_Tsk = str ("#N/V")
                print("Sensor-Alarm: MW_2OG_N_WZ_pt_Tsk antwortet nicht")

#-------Extra Sensor3 / New Addition---------#                 
            try:
                MW_2OG_S_SZ_pt_Tsk_cdo.set_status_led_config(0)
                MW_2OG_S_SZ_pt_Tsk = MW_2OG_S_SZ_pt_Tsk_cdo.get_temperature()/100.0
                
            except:
                MW_2OG_S_SZ_pt_Tsk = str ("#N/V")
                print("Sensor-Alarm: MW_2OG_S_SZ_pt_Tsk antwortet nicht")

#-------Extra Sensor4 / New Addition---------# 
            try:
                MW_2OG_S_WZ_pt_Tsk_cdo.set_status_led_config(0)
                MW_2OG_S_WZ_pt_Tsk = MW_2OG_S_WZ_pt_Tsk_cdo.get_temperature()/100.0
                
            except:
                MW_2OG_S_WZ_pt_Tsk = str ("#N/V")
                print("Sensor-Alarm: MW_2OG_S_WZ_pt_Tsk antwortet nicht")                           
#-----------------------MB1-----------------------------------------#            

            try:
                MW_2OG_N_SZ_n_trh_cdo.set_status_led_config(0)
                MW_2OG_N_SZ_n_trh_Tair = MW_2OG_N_SZ_n_trh_cdo.get_temperature()/100.0
                MW_2OG_N_SZ_n_trh_RH = MW_2OG_N_SZ_n_trh_cdo.get_humidity()/100.0                              
            except:
                MW_2OG_N_SZ_n_trh_Tair = str ("#N/V")
                MW_2OG_N_SZ_n_trh_RH = str ("#N/V")
                print("Sensor-Alarm: MW_2OG_N_SZ_n_trh antwortet nicht")       
  
            try:
                MW_2OG_N_SZ_n_co2_cdo.set_status_led_config(0)
                MW_2OG_N_SZ_n_co2, MW_2OG_N_SZ_n_co2_Tair, MW_2OG_N_SZ_n_co2_RH = MW_2OG_N_SZ_n_co2_cdo.get_all_values()
                MW_2OG_N_SZ_n_co2_Tair = MW_2OG_N_SZ_n_co2_Tair/100.0
                MW_2OG_N_SZ_n_co2_RH = MW_2OG_N_SZ_n_co2_RH/100.0
            except:
                MW_2OG_N_SZ_n_co2 = str ("#N/V")
                MW_2OG_N_SZ_n_co2_Tair = str ("#N/V")
                MW_2OG_N_SZ_n_co2_RH = str ("#N/V")
                print("Sensor-Alarm: MW_2OG_N_SZ_n_co2  antwortet nicht")                    


            try:
                MW_2OG_N_SZ_s_pt_Thk_cdo.set_status_led_config(0)
                MW_2OG_N_SZ_s_pt_Thk = MW_2OG_N_SZ_s_pt_Thk_cdo.get_temperature()/100.0
                
            except:
                MW_2OG_N_SZ_s_pt_Thk = str ("#N/V")
                print("Sensor-Alarm: MW_2OG_N_SZ_s_pt_Thk antwortet nicht")             

#-----------------------MB2-----------------------------------------#    
            try:
                MW_2OG_N_SZ_o_reed_cdo.set_status_led_config(0)
                MW_2OG_N_SZ_o_reed_0, MW_2OG_N_SZ_o_reed_1, MW_2OG_N_SZ_o_reed_2, MW_2OG_N_SZ_o_reed_3 = MW_2OG_N_SZ_o_reed_cdo.get_value()
                if MW_2OG_N_SZ_o_reed_0 == False:
                    MW_2OG_N_SZ_o_reed = str ("Closed")
                elif MW_2OG_N_SZ_o_reed_0 == True:
                    MW_2OG_N_SZ_o_reed = str ("Open")
            except:
                MW_2OG_N_SZ_o_reed = str ("#N/V")
                print("Sensor-Alarm: MW_2OG_N_SZ_o_reed antwortet nicht")

#-----------------------MB3-----------------------------------------#   

            try:
                voltage_N_el1, current_N_el1, MW_2OG_N_el1, real_power_N_el1, apparent_power_N_el1, reactive_power_N_el1, power_factor_N_el1, frequency_N_el1 = MW_2OG_N_el1_cdo.get_energy_data()    
                voltage_N_el1 = voltage_N_el1/100.0
                current_N_el1 = current_N_el1/100
                
                MW_2OG_N_el1 = MW_2OG_N_el1/100
                
                real_power_N_el1 = real_power_N_el1/100
                apparent_power_N_el1 = apparent_power_N_el1/100
                reactive_power_N_el1 = reactive_power_N_el1/100
                power_factor_N_el1 = power_factor_N_el1/100
                frequency_N_el1 = frequency_N_el1/100                    
            except:
                No_Value = ["#NV","#NV","#NV","#NV","#NV","#NV","#NV","#NV"]
                voltage_N_el1, current_N_el1, MW_2OG_N_el1, real_power_N_el1, apparent_power_N_el1, reactive_power_N_el1, power_factor_N_el1, frequency_N_el1 = No_Value                                    
                print("Sensor-Alarm: MW_2OG_N_el1 antwortet nicht")

            try:
                voltage_N_el2, current_N_el2, MW_2OG_N_el2, real_power_N_el2, apparent_power_N_el2, reactive_power_N_el2, power_factor_N_el2, frequency_N_el2 = MW_2OG_N_el2_cdo.get_energy_data()    
                voltage_N_el2 = voltage_N_el2/100.0
                current_N_el2 = current_N_el2/100
                
                MW_2OG_N_el2 = MW_2OG_N_el2/100
                
                real_power_N_el2 = real_power_N_el2/100
                apparent_power_N_el2 = apparent_power_N_el2/100
                reactive_power_N_el2 = reactive_power_N_el2/100
                power_factor_N_el2 = power_factor_N_el2/100
                frequency_N_el2 = frequency_N_el2/100                    
            except:
                No_Value = ["#NV","#NV","#NV","#NV","#NV","#NV","#NV","#NV"]
                voltage_N_el2, current_N_el2, MW_2OG_N_el2, real_power_N_el2, apparent_power_N_el2, reactive_power_N_el2, power_factor_N_el2, frequency_N_el2 = No_Value                                    
                print("Sensor-Alarm: MW_2OG_N_el2 antwortet nicht")

            try:
                voltage_N_el3, current_N_el3, MW_2OG_N_el3, real_power_N_el3, apparent_power_N_el3, reactive_power_N_el3, power_factor_N_el3, frequency_N_el3 = MW_2OG_N_el3_cdo.get_energy_data()    
                voltage_N_el3 = voltage_N_el3/100.0
                current_N_el3 = current_N_el3/100
                
                MW_2OG_N_el3 = MW_2OG_N_el3/100
                
                real_power_N_el3 = real_power_N_el3/100
                apparent_power_N_el3 = apparent_power_N_el3/100
                reactive_power_N_el3 = reactive_power_N_el3/100
                power_factor_N_el3 = power_factor_N_el3/100
                frequency_N_el3 = frequency_N_el3/100                    
            except:
                No_Value = ["#NV","#NV","#NV","#NV","#NV","#NV","#NV","#NV"]
                voltage_N_el3, current_N_el3, MW_2OG_N_el3, real_power_N_el3, apparent_power_N_el3, reactive_power_N_el3, power_factor_N_el3, frequency_N_el3 = No_Value                                    
                print("Sensor-Alarm: MW_2OG_N_el3 antwortet nicht")

#-----------------------MB4-----------------------------------------#  

            try:
                MW_2OG_N_WZ_s_trh_cdo.set_status_led_config(0)
                MW_2OG_N_WZ_s_trh_Tair = MW_2OG_N_WZ_s_trh_cdo.get_temperature()/100.0
                MW_2OG_N_WZ_s_trh_RH = MW_2OG_N_WZ_s_trh_cdo.get_humidity()/100.0                              
            except:
                MW_2OG_N_WZ_s_trh_Tair = str ("#N/V")
                MW_2OG_N_WZ_s_trh_RH = str ("#N/V")
                print("Sensor-Alarm: MW_2OG_N_WZ_s_trh antwortet nicht")      

            try:
                MW_2OG_N_WZ_o_reed_cdo.set_status_led_config(0)
                MW_2OG_N_WZ_o_reed_0, MW_2OG_N_WZ_o_reed_1, MW_2OG_N_WZ_o_reed_2, MW_2OG_N_WZ_o_reed_3 = MW_2OG_N_WZ_o_reed_cdo.get_value()
                if MW_2OG_N_WZ_o_reed_0 == False:
                    MW_2OG_N_WZ_o_reed = str ("Closed")
                elif MW_2OG_N_WZ_o_reed_0 == True:
                    MW_2OG_N_WZ_o_reed = str ("Open")
                #print (MW_2OG_N_WZ_o_reed)
            except:
                MW_2OG_N_WZ_o_reed = str ("#N/V")
                print("Sensor-Alarm: MW_2OG_N_WZ_o_reed antwortet nicht")



#-----------------------MB5-----------------------------------------#

            try:
                MW_2OG_N_WZ_n_reed_cdo.set_status_led_config(0)
                MW_2OG_N_WZ_n_reed_0, MW_2OG_N_WZ_n_reed_1, MW_2OG_N_WZ_n_reed_2, MW_2OG_N_WZ_n_reed_3 = MW_2OG_N_WZ_n_reed_cdo.get_value()
                if MW_2OG_N_WZ_n_reed_0 == False:
                    MW_2OG_N_WZ_n_reed = str ("Closed")
                elif MW_2OG_N_WZ_n_reed_0 == True:
                    MW_2OG_N_WZ_n_reed = str ("Open")
                #print (MW_2OG_N_WZ_n_reed)
            except:
                MW_2OG_N_WZ_n_reed = str ("#N/V")
                print("Sensor-Alarm: MW_2OG_N_WZ_n_reed antwortet nicht")


            try:
                MW_2OG_N_WZ_n_md_cdo.set_status_led_config(0)
                MW_2OG_N_WZ_n_md = MW_2OG_N_WZ_n_md_cdo.get_motion_detected()
            except:
                MW_2OG_N_WZ_n_md = str ("#N/V")
                print("Sensor-Alarm: MW_2OG_N_WZ_n_md antwortet nicht")

#-----------------------MB6-----------------------------------------#

            try:
                MW_2OG_N_WZ_w_pt_Thk_cdo.set_status_led_config(0)
                MW_2OG_N_WZ_w_pt_Thk = MW_2OG_N_WZ_w_pt_Thk_cdo.get_temperature()/100.0
                
            except:
                MW_2OG_N_WZ_w_pt_Thk = str ("#N/V")
                print("Sensor-Alarm: MW_2OG_N_WZ_w_pt_Thk antwortet nicht")

#-----------------------MB7-----------------------------------------#

            try:
                MW_2OG_N_K_w_trh_cdo.set_status_led_config(0)
                MW_2OG_N_K_w_trh_Tair = MW_2OG_N_K_w_trh_cdo.get_temperature()/100.0
                MW_2OG_N_K_w_trh_RH = MW_2OG_N_K_w_trh_cdo.get_humidity()/100.0                              
            except:
                MW_2OG_N_K_w_trh_Tair = str ("#N/V")
                MW_2OG_N_K_w_trh_RH = str ("#N/V")
                print("Sensor-Alarm: MW_2OG_N_K_w_trh antwortet nicht") 

            try:
                MW_2OG_N_K_w_reed_cdo.set_status_led_config(0)
                MW_2OG_N_K_w_reed_0, MW_2OG_N_K_w_reed_1, MW_2OG_N_K_w_reed_2, MW_2OG_N_K_w_reed_3 = MW_2OG_N_K_w_reed_cdo.get_value()
                if MW_2OG_N_K_w_reed_0 == False:
                    MW_2OG_N_K_w_reed = str ("Closed")
                elif MW_2OG_N_K_w_reed_0 == True:
                    MW_2OG_N_K_w_reed = str ("Open")
                #print (MW_2OG_N_K_w_reed)
            except:
                MW_2OG_N_K_w_reed = str ("#N/V")
                print("Sensor-Alarm: MW_2OG_N_K_w_reed antwortet nicht")

#-----------------------MB8-----------------------------------------#
            try:
                MW_2OG_N_K_n_reed_cdo.set_status_led_config(0)
                MW_2OG_N_K_n_reed_0, MW_2OG_N_K_n_reed_1, MW_2OG_N_K_n_reed_2, MW_2OG_N_K_n_reed_3 = MW_2OG_N_K_n_reed_cdo.get_value()
                if MW_2OG_N_K_n_reed_0 == False:
                    MW_2OG_N_K_n_reed = str ("Closed")
                elif MW_2OG_N_K_n_reed_0 == True:
                    MW_2OG_N_K_n_reed = str ("Open")
                #print (MW_2OG_N_K_n_reed)
            except:
                MW_2OG_N_K_n_reed = str ("#N/V")
                print("Sensor-Alarm: MW_2OG_N_K_n_reed antwortet nicht")

#-----------------------MB9-----------------------------------------#                
            try:
                MW_2OG_N_F_w_reed_cdo.set_status_led_config(0)
                MW_2OG_N_F_w_reed_0, MW_2OG_N_F_w_reed_1, MW_2OG_N_F_w_reed_2, MW_2OG_N_F_w_reed_3 = MW_2OG_N_F_w_reed_cdo.get_value()
                if MW_2OG_N_F_w_reed_0 == False:
                    MW_2OG_N_F_w_reed = str ("Closed")
                elif MW_2OG_N_F_w_reed_0 == True:
                    MW_2OG_N_F_w_reed = str ("Open")
                #print (MW_2OG_N_F_w_reed)
            except:
                MW_2OG_N_F_w_reed = str ("#N/V")
                print("Sensor-Alarm: MW_2OG_N_F_w_reed antwortet nicht")

            try:
                MW_2OG_N_F_w_md_cdo.set_status_led_config(0)
                MW_2OG_N_F_w_md = MW_2OG_N_F_w_md_cdo.get_motion_detected()
            except:
                MW_2OG_N_F_w_md = str ("#N/V")
                print("Sensor-Alarm: MW_2OG_N_F_w_md antwortet nicht")
                
#-----------------------MB10-----------------------------------------# 

            try:
                MW_2OG_N_B_n_pt_Tair_cdo.set_status_led_config(0)
                MW_2OG_N_B_n_pt_Tair = MW_2OG_N_B_n_pt_Tair_cdo.get_temperature()/100.0                
            except:
                MW_2OG_N_B_n_pt_Tair = str ("#N/V")
                print("Sensor-Alarm: MW_2OG_N_B_n_pt_Tair antwortet nicht")
                
            try:
                MW_2OG_N_B_n_trh_cdo.set_status_led_config(0)
                MW_2OG_N_B_n_trh_Tair = MW_2OG_N_B_n_trh_cdo.get_temperature()/100.0
                MW_2OG_N_B_n_trh_RH = MW_2OG_N_B_n_trh_cdo.get_humidity()/100.0                              
            except:
                MW_2OG_N_B_n_trh_Tair = str ("#N/V")
                MW_2OG_N_B_n_trh_RH = str ("#N/V")
                print("Sensor-Alarm: MW_2OG_N_B_n_trh antwortet nicht")       

            try:
                MW_2OG_N_B_n_pt_Thk_cdo.set_status_led_config(0)
                MW_2OG_N_B_n_pt_Thk = MW_2OG_N_B_n_pt_Thk_cdo.get_temperature()/100.0
                
            except:
                MW_2OG_N_B_n_pt_Thk = str ("#N/V")
                print("Sensor-Alarm: MW_2OG_N_B_n_pt_Thk antwortet nicht")

#-----------------------MB11-------------------------------MB15PORTD----------#

            try:
                MW_2OG_TH_m_trh_cdo.set_status_led_config(0)
                MW_2OG_TH_m_trh_Tair = MW_2OG_TH_m_trh_cdo.get_temperature()/100.0
                MW_2OG_TH_m_trh_RH = MW_2OG_TH_m_trh_cdo.get_humidity()/100.0                              
            except:
                MW_2OG_TH_m_trh_Tair = str ("#N/V")
                MW_2OG_TH_m_trh_RH = str ("#N/V")
                print("Sensor-Alarm: MW_2OG_TH_m_trh antwortet nicht")      
                
#-----------------------MB12-----------------------------------------#

            try:
                MW_2OG_O_SWK_s_pt_Thk_cdo.set_status_led_config(0)
                MW_2OG_O_SWK_s_pt_Thk = MW_2OG_O_SWK_s_pt_Thk_cdo.get_temperature()/100.0
                
            except:
                MW_2OG_O_SWK_s_pt_Thk = str ("#N/V")
                print("Sensor-Alarm: MW_2OG_O_SWK_s_pt_Thk antwortet nicht")

#-----------------------MB13-----------------------------------------#

            try:
                MW_2OG_O_SWK_o_reed_cdo.set_status_led_config(0)
                MW_2OG_O_SWK_o_reed_0,MW_2OG_O_SWK_o_reed_1, MW_2OG_O_SWK_o_reed_2,MW_2OG_O_SWK_o_reed_3 = MW_2OG_O_SWK_o_reed_cdo.get_value()
                if MW_2OG_O_SWK_o_reed_0 == False:
                    MW_2OG_O_SWK_o_reed = str ("Closed")
                elif MW_2OG_O_SWK_o_reed_0 == True:
                    MW_2OG_O_SWK_o_reed = str ("Open")
                #print (MW_2OG_O_SWK_o_reed)
            except:
                MW_2OG_O_SWK_o_reed = str ("#N/V")
                print("Sensor-Alarm: MW_2OG_O_SWK_o_reed antwortet nicht")

#-----------------------MB14a-----------------------------------------#

            try:
                MW_2OG_O_SWK_m_tir1_cdo.set_status_led_config(0)
                MW_2OG_O_SWK_m_tir1_amb = MW_2OG_O_SWK_m_tir1_cdo.get_ambient_temperature()/10.0
                MW_2OG_O_SWK_m_tir1_obj = MW_2OG_O_SWK_m_tir1_cdo.get_object_temperature()/10.0                
            except:
                MW_2OG_O_SWK_m_tir1_amb = str ("#N/V")
                MW_2OG_O_SWK_m_tir1_obj = str ("#N/V")
                print("Sensor-Alarm: MW_2OG_O_SWK_m_tir1 antwortet nicht")                
                
           
            try:
                MW_2OG_O_SWK_m_tir2_cdo.set_status_led_config(0)
                MW_2OG_O_SWK_m_tir2_amb = MW_2OG_O_SWK_m_tir2_cdo.get_ambient_temperature()/10.0
                MW_2OG_O_SWK_m_tir2_obj = MW_2OG_O_SWK_m_tir2_cdo.get_object_temperature()/10.0                
            except:
                MW_2OG_O_SWK_m_tir2_amb = str ("#N/V")
                MW_2OG_O_SWK_m_tir2_obj = str ("#N/V")
                print("Sensor-Alarm: MW_2OG_O_SWK_m_tir2 antwortet nicht")
                
           
            try:
                MW_2OG_O_SWK_m_tir3_cdo.set_status_led_config(0)
                MW_2OG_O_SWK_m_tir3_amb = MW_2OG_O_SWK_m_tir3_cdo.get_ambient_temperature()/10.0
                MW_2OG_O_SWK_m_tir3_obj = MW_2OG_O_SWK_m_tir3_cdo.get_object_temperature()/10.0                
            except:
                MW_2OG_O_SWK_m_tir3_amb = str ("#N/V")
                MW_2OG_O_SWK_m_tir3_obj = str ("#N/V")
                print("Sensor-Alarm: MW_2OG_O_SWK_m_tir3 antwortet nicht")

           
            try:
                MW_2OG_O_SWK_m_tir4_cdo.set_status_led_config(0)
                MW_2OG_O_SWK_m_tir4_amb = MW_2OG_O_SWK_m_tir4_cdo.get_ambient_temperature()/10.0
                MW_2OG_O_SWK_m_tir4_obj = MW_2OG_O_SWK_m_tir4_cdo.get_object_temperature()/10.0                
            except:
                MW_2OG_O_SWK_m_tir4_amb = str ("#N/V")
                MW_2OG_O_SWK_m_tir4_obj = str ("#N/V")
                print("Sensor-Alarm: MW_2OG_O_SWK_m_tir4 antwortet nicht")


#-----------------------MB14b-----------------------------------------#

            try:
                MW_2OG_O_SWK_m_tir5_cdo.set_status_led_config(0)
                MW_2OG_O_SWK_m_tir5_amb = MW_2OG_O_SWK_m_tir5_cdo.get_ambient_temperature()/10.0
                MW_2OG_O_SWK_m_tir5_obj = MW_2OG_O_SWK_m_tir5_cdo.get_object_temperature()/10.0                
            except:
                MW_2OG_O_SWK_m_tir5_amb = str ("#N/V")
                MW_2OG_O_SWK_m_tir5_obj = str ("#N/V")
                print("Sensor-Alarm: MW_2OG_O_SWK_m_tir5 antwortet nicht")                
                           
            try:
                MW_2OG_O_SWK_m_tir6_cdo.set_status_led_config(0)
                MW_2OG_O_SWK_m_tir6_amb = MW_2OG_O_SWK_m_tir6_cdo.get_ambient_temperature()/10.0
                MW_2OG_O_SWK_m_tir6_obj = MW_2OG_O_SWK_m_tir6_cdo.get_object_temperature()/10.0                
            except:
                MW_2OG_O_SWK_m_tir6_amb = str ("#N/V")
                MW_2OG_O_SWK_m_tir6_obj = str ("#N/V")
                print("Sensor-Alarm: MW_2OG_O_SWK_m_tir6 antwortet nicht")

            try:
                MW_2OG_O_SWK_m_trh_cdo.set_status_led_config(0)
                MW_2OG_O_SWK_m_trh_Tair = MW_2OG_O_SWK_m_trh_cdo.get_temperature()/100.0
                MW_2OG_O_SWK_m_trh_RH = MW_2OG_O_SWK_m_trh_cdo.get_humidity()/100.0                              
            except:
                MW_2OG_O_SWK_m_trh_Tair = str ("#N/V")
                MW_2OG_O_SWK_m_trh_RH = str ("#N/V")
                print("Sensor-Alarm: MW_2OG_O_SWK_m_trh antwortet nicht")       

            try:
                MW_2OG_O_SWK_m_pt_Tsk_cdo.set_status_led_config(0)
                MW_2OG_O_SWK_m_pt_Tsk = MW_2OG_O_SWK_m_pt_Tsk_cdo.get_temperature()/100.0                
            except:
                MW_2OG_O_SWK_m_pt_Tsk = str ("#N/V")
                print("Sensor-Alarm: MW_2OG_O_SWK_m_pt_Tsk antwortet nicht")

#-----------------------MB14c-----------------------------------------#
                
            try:
                MW_2OG_O_SWK_m_co2_cdo.set_status_led_config(0)
                MW_2OG_O_SWK_m_co2, MW_2OG_O_SWK_m_co2_Tair, MW_2OG_O_SWK_m_co2_RH = MW_2OG_O_SWK_m_co2_cdo.get_all_values()
                MW_2OG_O_SWK_m_co2_Tair = MW_2OG_O_SWK_m_co2_Tair/100.0
                MW_2OG_O_SWK_m_co2_RH = MW_2OG_O_SWK_m_co2_RH/100.0
            except:
                MW_2OG_O_SWK_m_co2 = str ("#N/V")
                MW_2OG_O_SWK_m_co2_Tair = str ("#N/V")
                MW_2OG_O_SWK_m_co2_RH = str ("#N/V")
                print("Sensor-Alarm: MW_2OG_O_SWK_m_co2  antwortet nicht")                    
                
            try:
                MW_2OG_O_SWK_m_al_cdo.set_status_led_config(0)
                MW_2OG_O_SWK_m_al = MW_2OG_O_SWK_m_al_cdo.get_illuminance()/100.0
            except:
                MW_2OG_O_SWK_m_al = str ("#N/V")
                print("Sensor-Alarm: MW_2OG_O_SWK_m_al antwortet nicht")                

            try:
                MW_2OG_O_SWK_m_md_cdo.set_status_led_config(0)
                MW_2OG_O_SWK_m_md = MW_2OG_O_SWK_m_md_cdo.get_motion_detected()
            except:
                MW_2OG_O_SWK_m_md = str ("#N/V")
                print("Sensor-Alarm: MW_2OG_O_SWK_m_md antwortet nicht")
#-----------------------MB15-----------------------------------------#

            try:
                MW_2OG_O_B_n_pt_Tair_cdo.set_status_led_config(0)
                MW_2OG_O_B_n_pt_Tair = MW_2OG_O_B_n_pt_Tair_cdo.get_temperature()/100.0                
            except:
                MW_2OG_O_B_n_pt_Tair = str ("#N/V")
                print("Sensor-Alarm: MW_2OG_O_B_n_pt_Tair antwortet nicht")
                
            try:
                MW_2OG_O_B_n_trh_cdo.set_status_led_config(0)
                MW_2OG_O_B_n_trh_Tair = MW_2OG_O_B_n_trh_cdo.get_temperature()/100.0
                MW_2OG_O_B_n_trh_RH = MW_2OG_O_B_n_trh_cdo.get_humidity()/100.0                              
            except:
                MW_2OG_O_B_n_trh_Tair = str ("#N/V")
                MW_2OG_O_B_n_trh_RH = str ("#N/V")
                print("Sensor-Alarm: MW_2OG_O_B_n_trh antwortet nicht")
                
            try:
                MW_2OG_O_B_w_pt_Thk_cdo.set_status_led_config(0)
                MW_2OG_O_B_w_pt_Thk = MW_2OG_O_B_w_pt_Thk_cdo.get_temperature()/100.0                
            except:
                MW_2OG_O_B_w_pt_Thk = str ("#N/V")
                print("Sensor-Alarm: MW_2OG_O_B_w_pt_Thk antwortet nicht")

#-----------------------MB27-----------------------------------------#
            try:
                voltage_O_el1, current_O_el1, MW_2OG_O_el1, real_power_O_el1, apparent_power_O_el1, reactive_power_O_el1, power_factor_O_el1, frequency_O_el1 = MW_2OG_O_el1_cdo.get_energy_data()    
                voltage_O_el1 = voltage_O_el1/100.0
                current_O_el1 = current_O_el1/100
                
                MW_2OG_O_el1 = MW_2OG_O_el1/100
                
                real_power_O_el1 = real_power_O_el1/100
                apparent_power_O_el1 = apparent_power_O_el1/100
                reactive_power_O_el1 = reactive_power_O_el1/100
                power_factor_O_el1 = power_factor_O_el1/100
                frequency_O_el1 = frequency_O_el1/100                    
            except:
                No_Value = ["#NV","#NV","#NV","#NV","#NV","#NV","#NV","#NV"]
                voltage_O_el1, current_O_el1, MW_2OG_O_el1, real_power_O_el1, apparent_power_O_el1, reactive_power_O_el1, power_factor_O_el1, frequency_O_el1 = No_Value                                    
                print("Sensor-Alarm: MW_2OG_O_el1 antwortet nicht")


            try:
                voltage_O_el2, current_O_el2, MW_2OG_O_el2, real_power_O_el2, apparent_power_O_el2, reactive_power_O_el2, power_factor_O_el2, frequency_O_el2 = MW_2OG_O_el2_cdo.get_energy_data()    
                voltage_O_el2 = voltage_O_el2/100.0
                current_O_el2 = current_O_el2/100
                
                MW_2OG_O_el2 = MW_2OG_O_el2/100
                
                real_power_O_el2 = real_power_O_el2/100
                apparent_power_O_el2 = apparent_power_O_el2/100
                reactive_power_O_el2 = reactive_power_O_el2/100
                power_factor_O_el2 = power_factor_O_el2/100
                frequency_O_el2 = frequency_O_el2/100                    
            except:
                No_Value = ["#NV","#NV","#NV","#NV","#NV","#NV","#NV","#NV"]
                voltage_O_el2, current_O_el2, MW_2OG_O_el2, real_power_O_el2, apparent_power_O_el2, reactive_power_O_el2, power_factor_O_el2, frequency_O_el2 = No_Value                                    
                print("Sensor-Alarm: MW_2OG_O_el2 antwortet nicht")

            try:
                voltage_O_el3, current_O_el3, MW_2OG_O_el3, real_power_O_el3, apparent_power_O_el3, reactive_power_O_el3, power_factor_O_el3, frequency_O_el3 = MW_2OG_O_el3_cdo.get_energy_data()    
                voltage_O_el3 = voltage_O_el3/100.0
                current_O_el3 = current_O_el3/100
                
                MW_2OG_O_el3 = MW_2OG_O_el3/100
                
                real_power_O_el3 = real_power_O_el3/100
                apparent_power_O_el3 = apparent_power_O_el3/100
                reactive_power_O_el3 = reactive_power_O_el3/100
                power_factor_O_el3 = power_factor_O_el3/100
                frequency_O_el3 = frequency_O_el3/100                    
            except:
                No_Value = ["#NV","#NV","#NV","#NV","#NV","#NV","#NV","#NV"]
                voltage_O_el3, current_O_el3, MW_2OG_O_el3, real_power_O_el3, apparent_power_O_el3, reactive_power_O_el3, power_factor_O_el3, frequency_O_el3 = No_Value                                    
                print("Sensor-Alarm: MW_2OG_O_el3 antwortet nicht")

#-----------------------MB16-----------------------------------------#

            try:
                MW_2OG_S_SZ_n_trh_cdo.set_status_led_config(0)
                MW_2OG_S_SZ_n_trh_Tair = MW_2OG_S_SZ_n_trh_cdo.get_temperature()/100.0
                MW_2OG_S_SZ_n_trh_RH = MW_2OG_S_SZ_n_trh_cdo.get_humidity()/100.0                              
            except:
                MW_2OG_S_SZ_n_trh_Tair = str ("#N/V")
                MW_2OG_S_SZ_n_trh_RH = str ("#N/V")
                print("Sensor-Alarm: MW_2OG_S_SZ_n_trh antwortet nicht")       

            try:
                MW_2OG_S_SZ_n_co2_cdo.set_status_led_config(0)
                MW_2OG_S_SZ_n_co2, MW_2OG_S_SZ_n_co2_Tair, MW_2OG_S_SZ_n_co2_RH = MW_2OG_S_SZ_n_co2_cdo.get_all_values()
                MW_2OG_S_SZ_n_co2_Tair = MW_2OG_S_SZ_n_co2_Tair/100.0
                MW_2OG_S_SZ_n_co2_RH = MW_2OG_S_SZ_n_co2_RH/100.0
            except:
                MW_2OG_S_SZ_n_co2 = str ("#N/V")
                MW_2OG_S_SZ_n_co2_Tair = str ("#N/V")
                MW_2OG_S_SZ_n_co2_RH = str ("#N/V")
                print("Sensor-Alarm: MW_2OG_S_SZ_n_co2  antwortet nicht")     

            try:
                MW_2OG_S_SZ_o_pt_Thk_cdo.set_status_led_config(0)
                MW_2OG_S_SZ_o_pt_Thk = MW_2OG_S_SZ_o_pt_Thk_cdo.get_temperature()/100.0                
            except:
                MW_2OG_S_SZ_o_pt_Thk = str ("#N/V")
                print("Sensor-Alarm: MW_2OG_S_SZ_o_pt_Thk antwortet nicht")

#-----------------------MB17-----------------------------------------#

            try:
                MW_2OG_S_SZ_o_reed_cdo.set_status_led_config(0)
                MW_2OG_S_SZ_o_reed_0, MW_2OG_S_SZ_o_reed_1, MW_2OG_S_SZ_o_reed_2, MW_2OG_S_SZ_o_reed_3 = MW_2OG_S_SZ_o_reed_cdo.get_value()
                if MW_2OG_S_SZ_o_reed_0 == False:
                    MW_2OG_S_SZ_o_reed = str ("Closed")
                elif MW_2OG_S_SZ_o_reed_0 == True:
                    MW_2OG_S_SZ_o_reed = str ("Open")
                #print (MW_2OG_S_SZ_o_reed)
            except:
                MW_2OG_S_SZ_o_reed = str ("#N/V")
                print("Sensor-Alarm: MW_2OG_S_SZ_o_reed antwortet nicht")

#-----------------------MB18-----------------------------------------#


            try:
                voltage_S_el1, current_S_el1, MW_2OG_S_el1, real_power_S_el1, apparent_power_S_el1, reactive_power_S_el1, power_factor_S_el1, frequency_S_el1 = MW_2OG_S_el1_cdo.get_energy_data()    
                voltage_S_el1 = voltage_S_el1/100.0
                current_S_el1 = current_S_el1/100
                
                MW_2OG_S_el1 = MW_2OG_S_el1/100
                
                real_power_S_el1 = real_power_S_el1/100
                apparent_power_S_el1 = apparent_power_S_el1/100
                reactive_power_S_el1 = reactive_power_S_el1/100
                power_factor_S_el1 = power_factor_S_el1/100
                frequency_S_el1 = frequency_S_el1/100                    
            except:
                No_Value = ["#NV","#NV","#NV","#NV","#NV","#NV","#NV","#NV"]
                voltage_S_el1, current_S_el1, MW_2OG_S_el1, real_power_S_el1, apparent_power_S_el1, reactive_power_S_el1, power_factor_S_el1, frequency_S_el1 = No_Value                                    
                print("Sensor-Alarm: MW_2OG_S_el1 antwortet nicht")


            try:
                voltage_S_el2, current_S_el2, MW_2OG_S_el2, real_power_S_el2, apparent_power_S_el2, reactive_power_S_el2, power_factor_S_el2, frequency_S_el2 = MW_2OG_S_el2_cdo.get_energy_data()    
                voltage_S_el2 = voltage_S_el2/100.0
                current_S_el2 = current_S_el2/100
                
                MW_2OG_S_el2 = MW_2OG_S_el2/100
                
                real_power_S_el2 = real_power_S_el2/100
                apparent_power_S_el2 = apparent_power_S_el2/100
                reactive_power_S_el2 = reactive_power_S_el2/100
                power_factor_S_el2 = power_factor_S_el2/100
                frequency_S_el2 = frequency_S_el2/100                    
            except:
                No_Value = ["#NV","#NV","#NV","#NV","#NV","#NV","#NV","#NV"]
                voltage_S_el2, current_S_el2, MW_2OG_S_el2, real_power_S_el2, apparent_power_S_el2, reactive_power_S_el2, power_factor_S_el2, frequency_S_el2 = No_Value                                    
                print("Sensor-Alarm: MW_2OG_S_el2 antwortet nicht")

            try:
                voltage_S_el3, current_S_el3, MW_2OG_S_el3, real_power_S_el3, apparent_power_S_el3, reactive_power_S_el3, power_factor_S_el3, frequency_S_el3 = MW_2OG_S_el3_cdo.get_energy_data()    
                voltage_S_el3 = voltage_S_el3/100.0
                current_S_el3 = current_S_el3/100
                
                MW_2OG_S_el3 = MW_2OG_S_el3/100
                
                real_power_S_el3 = real_power_S_el3/100
                apparent_power_S_el3 = apparent_power_S_el3/100
                reactive_power_S_el3 = reactive_power_S_el3/100
                power_factor_S_el3 = power_factor_S_el3/100
                frequency_S_el3 = frequency_S_el3/100                    
            except:
                No_Value = ["#NV","#NV","#NV","#NV","#NV","#NV","#NV","#NV"]
                voltage_S_el3, current_S_el3, MW_2OG_S_el3, real_power_S_el3, apparent_power_S_el3, reactive_power_S_el3, power_factor_S_el3, frequency_S_el3 = No_Value                                    
                print("Sensor-Alarm: MW_2OG_S_el3 antwortet nicht")

#-----------------------MB19-----------------------------------------#

            try:
                MW_2OG_S_WZ_n_trh_cdo.set_status_led_config(0)
                MW_2OG_S_WZ_n_trh_Tair = MW_2OG_S_WZ_n_trh_cdo.get_temperature()/100.0
                MW_2OG_S_WZ_n_trh_RH = MW_2OG_S_WZ_n_trh_cdo.get_humidity()/100.0                              
            except:
                MW_2OG_S_WZ_n_trh_Tair = str ("#N/V")
                MW_2OG_S_WZ_n_trh_RH = str ("#N/V")
                print("Sensor-Alarm: MW_2OG_S_WZ_n_trh antwortet nicht")       

            try:
                MW_2OG_S_WZ_o_reed_cdo.set_status_led_config(0)
                MW_2OG_S_WZ_o_reed_0, MW_2OG_S_WZ_o_reed_1, MW_2OG_S_WZ_o_reed_2, MW_2OG_S_WZ_o_reed_3 = MW_2OG_S_WZ_o_reed_cdo.get_value()
                if MW_2OG_S_WZ_o_reed_0 == False:
                    MW_2OG_S_WZ_o_reed = str ("Closed")
                elif MW_2OG_S_WZ_o_reed_0 == True:
                    MW_2OG_S_WZ_o_reed = str ("Open")
                #print (MW_2OG_S_WZ_o_reed)
            except:
                MW_2OG_S_WZ_o_reed = str ("#N/V")
                print("Sensor-Alarm: MW_2OG_S_WZ_o_reed antwortet nicht")


#-----------------------MB20-----------------------------------------#

            try:
                MW_2OG_S_WZ_s_reed_cdo.set_status_led_config(0)
                MW_2OG_S_WZ_s_reed_0, MW_2OG_S_WZ_s_reed_1, MW_2OG_S_WZ_s_reed_2, MW_2OG_S_WZ_s_reed_3 = MW_2OG_S_WZ_s_reed_cdo.get_value()
                if MW_2OG_S_WZ_s_reed_0 == False:
                    MW_2OG_S_WZ_s_reed = str ("Closed")
                elif MW_2OG_S_WZ_s_reed_0 == True:
                    MW_2OG_S_WZ_s_reed = str ("Open")
                #print (MW_2OG_S_WZ_s_reed)
            except:
                MW_2OG_S_WZ_s_reed = str ("#N/V")
                print("Sensor-Alarm: MW_2OG_S_WZ_s_reed antwortet nicht")
                
            try:
                MW_2OG_S_WZ_s_md_cdo.set_status_led_config(0)
                MW_2OG_S_WZ_s_md = MW_2OG_S_WZ_s_md_cdo.get_motion_detected()
            except:
                MW_2OG_S_WZ_s_md = str ("#N/V")
                print("Sensor-Alarm: MW_2OG_S_WZ_s_md antwortet nicht")                
                
#-----------------------MB21-----------------------------------------#

            try:
                MW_2OG_S_WZ_w_pt_Thk_cdo.set_status_led_config(0)
                MW_2OG_S_WZ_w_pt_Thk = MW_2OG_S_WZ_w_pt_Thk_cdo.get_temperature()/100.0                
            except:
                MW_2OG_S_WZ_w_pt_Thk = str ("#N/V")
                print("Sensor-Alarm: MW_2OG_S_WZ_w_pt_Thk antwortet nicht")


#-----------------------MB22-----------------------------------------#
            try:
                MW_2OG_S_K_w_reed_cdo.set_status_led_config(0)
                MW_2OG_S_K_w_reed_0, MW_2OG_S_K_w_reed_1, MW_2OG_S_K_w_reed_2, MW_2OG_S_K_w_reed_3 = MW_2OG_S_K_w_reed_cdo.get_value()
                if MW_2OG_S_K_w_reed_0 == False:
                    MW_2OG_S_K_w_reed = str ("Closed")
                elif MW_2OG_S_K_w_reed_0 == True:
                    MW_2OG_S_K_w_reed = str ("Open")
                #print (MW_2OG_S_K_w_reed)
            except:
                MW_2OG_S_K_w_reed = str ("#N/V")
                print("Sensor-Alarm: MW_2OG_S_K_w_reed antwortet nicht")
                
                
            try:
                MW_2OG_S_K_w_trh_cdo.set_status_led_config(0)
                MW_2OG_S_K_w_trh_Tair = MW_2OG_S_K_w_trh_cdo.get_temperature()/100.0
                MW_2OG_S_K_w_trh_RH = MW_2OG_S_K_w_trh_cdo.get_humidity()/100.0                              
            except:
                MW_2OG_S_K_w_trh_Tair = str ("#N/V")
                MW_2OG_S_K_w_trh_RH = str ("#N/V")
                print("Sensor-Alarm: MW_2OG_S_K_w_trh antwortet nicht")     
   
#-----------------------MB23-----------------------------------------#
            try:
                MW_2OG_S_K_s_reed_cdo.set_status_led_config(0)
                MW_2OG_S_K_s_reed_0, MW_2OG_S_K_s_reed_1, MW_2OG_S_K_s_reed_2, MW_2OG_S_K_s_reed_3 = MW_2OG_S_K_s_reed_cdo.get_value()
                if MW_2OG_S_K_s_reed_0 == False:
                    MW_2OG_S_K_s_reed = str ("Closed")
                elif MW_2OG_S_K_s_reed_0 == True:
                    MW_2OG_S_K_s_reed = str ("Open")
                #print (MW_2OG_S_K_s_reed)
            except:
                MW_2OG_S_K_s_reed = str ("#N/V")
                print("Sensor-Alarm: MW_2OG_S_K_s_reed antwortet nicht")
       
#-----------------------MB24-----------------------------------------#

            try:
                MW_2OG_S_F_w_reed1_cdo.set_status_led_config(0)
                MW_2OG_S_F_w_reed1_0, MW_2OG_S_F_w_reed1_1, MW_2OG_S_F_w_reed1_2, MW_2OG_S_F_w_reed1_3 = MW_2OG_S_F_w_reed1_cdo.get_value()
                if MW_2OG_S_F_w_reed1_0 == False:
                    MW_2OG_S_F_w_reed1 = str ("Closed")
                elif MW_2OG_S_F_w_reed1_0 == True:
                    MW_2OG_S_F_w_reed1 = str ("Open")
                #print (MW_2OG_S_F_w_reed1)
            except:
                MW_2OG_S_F_w_reed1 = str ("#N/V")
                print("Sensor-Alarm: MW_2OG_S_F_w_reed1 antwortet nicht")
       
        
#-----------------------MB25-----------------------------------------#

            try:
                MW_2OG_S_F_w_reed2_cdo.set_status_led_config(0)
                MW_2OG_S_F_w_reed2_0, MW_2OG_S_F_w_reed2_1, MW_2OG_S_F_w_reed2_2, MW_2OG_S_F_w_reed2_3 = MW_2OG_S_F_w_reed2_cdo.get_value()
                if  MW_2OG_S_F_w_reed2_0 == False:
                     MW_2OG_S_F_w_reed2 = str ("Closed")
                elif  MW_2OG_S_F_w_reed2_0 == True:
                     MW_2OG_S_F_w_reed2 = str ("Open")
               # print ( MW_2OG_S_F_w_reed2)
            except:
                 MW_2OG_S_F_w_reed2 = str ("#N/V")
                 print("Sensor-Alarm:  MW_2OG_S_F_w_reed2 antwortet nicht")

            try:
                MW_2OG_S_F_n_md_cdo.set_status_led_config(0)
                MW_2OG_S_F_n_md = MW_2OG_S_F_n_md_cdo.get_motion_detected()
            except:
                MW_2OG_S_F_n_md = str ("#N/V")
                print("Sensor-Alarm: MW_2OG_S_F_n_md antwortet nicht")

#-----------------------MB26-----------------------------------------#
            try:
                MW_2OG_S_B_n_pt_Tair_cdo.set_status_led_config(0)
                MW_2OG_S_B_n_pt_Tair = MW_2OG_S_B_n_pt_Tair_cdo.get_temperature()/100.0                
            except:
                MW_2OG_S_B_n_pt_Tair = str ("#N/V")
                print("Sensor-Alarm: MW_2OG_S_B_n_pt_Tair antwortet nicht")

            try:
                MW_2OG_S_B_s_trh_cdo.set_status_led_config(0)
                MW_2OG_S_B_s_trh_Tair = MW_2OG_S_B_s_trh_cdo.get_temperature()/100.0
                MW_2OG_S_B_s_trh_RH = MW_2OG_S_B_s_trh_cdo.get_humidity()/100.0                              
            except:
                MW_2OG_S_B_s_trh_Tair = str ("#N/V")
                MW_2OG_S_B_s_trh_RH = str ("#N/V")
                print("Sensor-Alarm: MW_2OG_S_B_s_trh antwortet nicht")   
                
            try:
                MW_2OG_S_B_n_pt_Thk_cdo.set_status_led_config(0)
                MW_2OG_S_B_n_pt_Thk = MW_2OG_S_B_n_pt_Thk_cdo.get_temperature()/100.0
                
            except:
                MW_2OG_S_B_n_pt_Thk = str ("#N/V")
                print("Sensor-Alarm: MW_2OG_S_B_n_pt_Thk antwortet nicht")                
          
#-----------------------New Sensor 17.01.2022------------------------------------#
            try:
                MW_2OG_O_SWK_al1_cdo.set_status_led_config(0)
                MW_2OG_O_SWK_al1 = MW_2OG_O_SWK_al1_cdo.get_illuminance()/100.0
            except:
                MW_2OG_O_SWK_al1 = str ("#N/V")
                print("Sensor-Alarm: MW_2OG_O_SWK_al1 antwortet nicht")
                
            try:
                MW_2OG_O_SWK_al2_cdo.set_status_led_config(0)
                MW_2OG_O_SWK_al2 = MW_2OG_O_SWK_al2_cdo.get_illuminance()/100.0
            except:
                MW_2OG_O_SWK_al2 = str ("#N/V")
                print("Sensor-Alarm: MW_2OG_O_SWK_al2 antwortet nicht")  

            try:
                MW_2OG_O_SWK_al3_cdo.set_status_led_config(0)
                MW_2OG_O_SWK_al3 = MW_2OG_O_SWK_al3_cdo.get_illuminance()/100.0
            except:
                MW_2OG_O_SWK_al3 = str ("#N/V")
                print("Sensor-Alarm: MW_2OG_O_SWK_al3 antwortet nicht")  
                
            try:
                MW_2OG_O_SWK_al4_cdo.set_status_led_config(0)
                MW_2OG_O_SWK_al4 = MW_2OG_O_SWK_al4_cdo.get_illuminance()/100.0
            except:
                MW_2OG_O_SWK_al4 = str ("#N/V")
                print("Sensor-Alarm: MW_2OG_O_SWK_al4 antwortet nicht")  

            try:
                MW_2OG_O_SWK_al5_cdo.set_status_led_config(0)
                MW_2OG_O_SWK_al5 = MW_2OG_O_SWK_al5_cdo.get_illuminance()/100.0
            except:
                MW_2OG_O_SWK_al5 = str ("#N/V")
                print("Sensor-Alarm: MW_2OG_O_SWK_al5 antwortet nicht")

            try:
                MW_2OG_O_SWK_m_trh1_cdo.set_status_led_config(0)
                MW_2OG_O_SWK_m_trh1_Tair = MW_2OG_O_SWK_m_trh1_cdo.get_temperature()/100.0
                MW_2OG_O_SWK_m_trh1_RH = MW_2OG_O_SWK_m_trh1_cdo.get_humidity()/100.0                              
            except:
                MW_2OG_O_SWK_m_trh1_Tair = str ("#N/V")
                MW_2OG_O_SWK_m_trh1_RH = str ("#N/V")
                print("Sensor-Alarm: MW_2OG_O_SWK_m_trh1 antwortet nicht")   
                

            try:
                MW_Dach_trh1_cdo.set_status_led_config(0)
                MW_Dach_trh1_Tair = MW_Dach_trh1_cdo.get_temperature()/100.0
                MW_Dach_trh1_RH = MW_Dach_trh1_cdo.get_humidity()/100.0                              
            except:
                MW_Dach_trh1_Tair = str ("#N/V")
                MW_Dach_trh1_RH = str ("#N/V")
                print("Sensor-Alarm: MW_Dach_trh1 antwortet nicht")    
                
            try:
                MW_Dach_trh2_cdo.set_status_led_config(0)
                MW_Dach_trh2_Tair = MW_Dach_trh2_cdo.get_temperature()/100.0
                MW_Dach_trh2_RH = MW_Dach_trh2_cdo.get_humidity()/100.0                              
            except:
                MW_Dach_trh2_Tair = str ("#N/V")
                MW_Dach_trh2_RH = str ("#N/V")
                print("Sensor-Alarm: MW_Dach_trh2 antwortet nicht")      

#Sensordaten speichern                
            Ausgabe =   (str(day)+','+str(month)+','+str(year)+';'\
                        +str(hour)+':'+str(minute)+':'+str(second)+';'
                        +" "+';'\
                        +str(MW_2OG_N_SZ_n_trh_Tair) +';'\
                        +str(MW_2OG_N_SZ_n_trh_RH) +';'\
                        +str(MW_2OG_N_SZ_n_co2) +';'\
                        +str(MW_2OG_N_SZ_n_co2_Tair) +';'\
                        +str(MW_2OG_N_SZ_n_co2_RH) +';'\
                        +str(MW_2OG_N_SZ_s_pt_Thk) +';'\
                        +" "+';'                           
                        +str(MW_2OG_N_SZ_o_reed) +';'\
                        +" "+';'  
                        +str(MW_2OG_N_el1) +';'\
                        +str(MW_2OG_N_el2) +';'\
                        +str(MW_2OG_N_el3) +';'\
                        +" "+';'
                        +str(MW_2OG_N_WZ_s_trh_Tair) +';'\
                        +str(MW_2OG_N_WZ_s_trh_RH) +';'\
                        +str(MW_2OG_N_WZ_o_reed) +';'\
                        +" "+';'    
                        +str(MW_2OG_N_WZ_n_reed) +';'\
                        +str(MW_2OG_N_WZ_n_md) +';'\
                        +" "+';'   
                        +str(MW_2OG_N_WZ_w_pt_Thk) +';'\
                        +" "+';'    
                        +str(MW_2OG_N_K_w_trh_Tair) +';'\
                        +str(MW_2OG_N_K_w_trh_RH) +';'\
                        +str(MW_2OG_N_K_w_reed) +';'\
                        +" "+';'    
                        +str(MW_2OG_N_K_n_reed) +';'\
                        +" "+';'   
                        +str(MW_2OG_N_F_w_reed) +';'\
                        +str(MW_2OG_N_F_w_md) +';'\
                        +" "+';'    
                        +str(MW_2OG_N_B_n_pt_Tair) +';'\
                        +str(MW_2OG_N_B_n_trh_Tair) +';'\
                        +str(MW_2OG_N_B_n_trh_RH) +';'\
                        +str(MW_2OG_N_B_n_pt_Thk) +';'\
                        +" "+';'    
                        +str(MW_2OG_TH_m_trh_Tair) +';'\
                        +str(MW_2OG_TH_m_trh_RH) +';'\
                        +" "+';'    
                        +str(MW_2OG_O_SWK_s_pt_Thk) +';'\
                        +" "+';'
                        +str(MW_2OG_O_SWK_o_reed) +';'\
                        +" "+';'                              
                        +str(MW_2OG_O_SWK_m_tir1_amb) +';'\
                        +str(MW_2OG_O_SWK_m_tir1_obj) +';'\
                        +str(MW_2OG_O_SWK_m_tir2_amb) +';'\
                        +str(MW_2OG_O_SWK_m_tir2_obj) +';'\
                        +str(MW_2OG_O_SWK_m_tir3_amb ) +';'\
                        +str(MW_2OG_O_SWK_m_tir3_obj) +';'\
                        +str(MW_2OG_O_SWK_m_tir4_amb) +';'\
                        +str(MW_2OG_O_SWK_m_tir4_obj) +';'\
                        +" "+';'    
                        +str(MW_2OG_O_SWK_m_tir5_amb) +';'\
                        +str(MW_2OG_O_SWK_m_tir5_obj) +';'\
                        +str(MW_2OG_O_SWK_m_tir6_amb ) +';'\
                        +str(MW_2OG_O_SWK_m_tir6_obj) +';'\
                        +str(MW_2OG_O_SWK_m_trh_Tair) +';'\
                        +str(MW_2OG_O_SWK_m_trh_RH) +';'\
                        +str(MW_2OG_O_SWK_m_pt_Tsk) +';'\
                        +" "+';'                            
                        +str(MW_2OG_O_SWK_m_co2) +';'\
                        +str(MW_2OG_O_SWK_m_co2_Tair) +';'\
                        +str(MW_2OG_O_SWK_m_co2_RH) +';'\
                        +str(MW_2OG_O_SWK_m_al) +';'\
                        +str(MW_2OG_O_SWK_m_md) +';'                    
                        +" "+';'
                        +str(MW_2OG_O_B_n_pt_Tair) +';'\
                        +str(MW_2OG_O_B_n_trh_Tair) +';'\
                        +str(MW_2OG_O_B_n_trh_RH) +';'\
                        +str(MW_2OG_O_B_w_pt_Thk) +';'\
                        +" "+';'
                        +str(MW_2OG_O_el1) +';'\
                        +str(MW_2OG_O_el2) +';'\
                        +str(MW_2OG_O_el3) +';'\
                        +" "+';'                                                 
                        +str(MW_2OG_S_SZ_n_trh_Tair) +';'\
                        +str(MW_2OG_S_SZ_n_trh_RH) +';'\
                        +str(MW_2OG_S_SZ_n_co2) +';'\
                        +str(MW_2OG_S_SZ_n_co2_Tair) +';'\
                        +str(MW_2OG_S_SZ_n_co2_RH) +';'\
                        +str(MW_2OG_S_SZ_o_pt_Thk) +';'\
                        +" "+';'                        
                        +str(MW_2OG_S_SZ_o_reed) +';'\
                        +" "+';'                        
                        +str(MW_2OG_S_el1) +';'\
                        +str(MW_2OG_S_el2) +';'\
                        +str(MW_2OG_S_el3) +';'\
                        +" "+';'                        
                        +str(MW_2OG_S_WZ_n_trh_Tair) +';'\
                        +str(MW_2OG_S_WZ_n_trh_RH) +';'\
                        +str(MW_2OG_S_WZ_o_reed) +';'\
                        +" "+';'
                        +str(MW_2OG_S_WZ_s_reed) +';'\
                        +str(MW_2OG_S_WZ_s_md ) +';'\
                        +" "+';'    
                        +str(MW_2OG_S_WZ_w_pt_Thk) +';'\
                        +" "+';'    
                        +str(MW_2OG_S_K_w_reed) +';'\
                        +str(MW_2OG_S_K_w_trh_Tair) +';'\
                        +str(MW_2OG_S_K_w_trh_RH) +';'\
                        +" "+';'    
                        +str(MW_2OG_S_K_s_reed ) +';'\
                        +" "+';'    
                        +str(MW_2OG_S_F_w_reed1) +';'\
                        +" "+';'
                        +str(MW_2OG_S_F_w_reed2) +';'\
                        +str(MW_2OG_S_F_n_md) +';'\
                        +" "+';'    
                        +str(MW_2OG_S_B_n_pt_Tair) +';'\
                        +str(MW_2OG_S_B_s_trh_Tair) +';'\
                        +str(MW_2OG_S_B_s_trh_RH) +';'\
                        +str(MW_2OG_S_B_n_pt_Thk) +';'\
                        +" "+';'  
                        +"-->----->----->"+';'
                        +" "+';'
                        +str(MW_2OG_N_SZ_pt_Tsk) +';'\
                        +" "+';'
                        +str(MW_2OG_N_WZ_pt_Tsk) +';'\
                        +" "+';' 
                        +str(MW_2OG_S_SZ_pt_Tsk) +';'\
                        +" "+';'
                        +str(MW_2OG_S_WZ_pt_Tsk) +';'\
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
                        +str(MW_2OG_O_SWK_al1) +';'                        
                        +str(MW_2OG_O_SWK_al2) +';' 
                        +str(MW_2OG_O_SWK_al3) +';' 
                        +str(MW_2OG_O_SWK_al4) +';'
                        +str(MW_2OG_O_SWK_al5) +';'
                        +str(MW_2OG_O_SWK_m_trh1_Tair) +';'
                        +str(MW_2OG_O_SWK_m_trh1_RH) +';'
                        +" "+';' 
                        +str(MW_Dach_trh1_Tair) +';'
                        +str(MW_Dach_trh1_RH) +';'
                        +str(MW_Dach_trh2_Tair) +';'
                        +str(MW_Dach_trh2_RH) +';'
                        
                        +'\n')     

    
            maketrans = Ausgabe.maketrans
            Ausgabe = Ausgabe.translate(maketrans(',.', '.,'))

            data = open(filename,'a') 
            data.write(Ausgabe)
            data.close()
            #print(Ausgabe)
            

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