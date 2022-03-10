import math as m

### Wasserdampfsättungsdruck
def psat(t):
    if t >= 0:
        return 610.5*m.exp((17.269*t)/(237.3+t))
    if t < 0:
        return 610.5*m.exp((21.875*t)/(265.5+t))

### Luftdichte in Abhängigkeit von der Temperatur in kg/m³
def roh(t):
    # Temperatur in Kelvin
    T = 273.15 + t
    # atmosphärischer Luftdruck in Pa:
    p = 101325   
    # spezifische Gaskonstante in J/(kg*K) 
    Rs = 287.058 

    return p/(Rs*T) 

#Umrechnung spezifische Feuchte zu absoluter Feuchte
def x_to_g(g, t):
    # x: spezifische Luftfeuchte in g/kg Luft
    # g: absolute Luftfeuchte in g/m³ Luft
    # roh: Dichte von Luft, abhängig von der Temperatur t:
    def roh(t):
        # Temperatur in Kelvin
        T = 273.15 + t
        # atmosphärischer Luftdruck in Pa:
        pamb = 101325   
        # spezifische Gaskonstante in J/(kg*K) 
        Rs = 287.058 

        return pamb/(Rs*T)

    return g/roh(t)

# absolute Luftfeuchtigkeit in g/kg von temperatur und luftfeuchte
def g_abs(t: float, rh: float):
    # atmosphärischer Luftdruck in Pa:
    p = 101325
    # Wasserdampfsättigungsdruck
    def psat(t):
        if t >= 0:
            return 610.5*m.exp((17.269*t)/(237.3+t))
        if t < 0:
            return 610.5*m.exp((21.875*t)/(265.5+t))

    rh=rh/100

    return round( 0.622 * (rh*psat(t))/(p-rh*psat(t)) * 1000 ,2)

# relative feuchte von absoluter feuchte und temperatur
def RH(g:float,t:float):
    # atmosphärischer Luftdruck in Pa:
    p = 101325
    # Wasserdampfsättigungsdruck
    def psat(t):
        if t >= 0:
            return 610.5*m.exp((17.269*t)/(237.3+t))
        if t < 0:
            return 610.5*m.exp((21.875*t)/(265.5+t))
    #absoulte Feuchte in kg/kg
    g = g/1000
    return round( (g*p/(psat(t)*(0.622+g))*100), 1)

def t_for_g(g, rh):
    A = 23.1964
    B = 3816.44
    C = 273.15 - 46.13
    pamb = 101325

    blub = ((29*g)/18000)/(1+29*g/18000)

    p_0 = blub*(100/rh)*pamb

    return B/(A-m.log(p_0))-C
