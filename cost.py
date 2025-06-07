def crop(Cr, Grain_Wght, Grain_m, harvested_area):
    yld_round = 0
    Bushel_Wght_rice = 45
    Grain_Mois_rice = 11.79

    Bushel_Wght_maize = 56
    Grain_Mois_maize = 13.5

    Bushel_Wght_chickpea = 60
    Grain_Mois_chickpea = 14.0

    Bushel_Wght_kidneybeans = 60
    Grain_Mois_kidneybeans = 9.77

    Bushel_Wght_pigeonpeas = 58
    Grain_Mois_pigeonpeas = 12

    Bushel_Wght_mothbeans = 47
    Grain_Mois_mothbeans = 10.46

    Bushel_Wght_mungbean = 60
    Grain_Mois_mungbean = 8.7

    Bushel_Wght_blackgram = 50
    Grain_Mois_blackgram = 15.75

    Bushel_Wght_lentil = 36
    Grain_Mois_lentil = 12.7

    Bushel_Wght_pomegranate = 55
    Grain_Mois_pomegranate = 81

    Bushel_Wght_banana = 24
    Grain_Mois_banana = 74

    Bushel_Wght_mango = 44
    Grain_Mois_mango = 81.05

    Bushel_Wght_grapes = 48
    Grain_Mois_grapes = 78

    Bushel_Wght_watermelon = 43
    Grain_Mois_watermelon = 92

    Bushel_Wght_muskmelon = 48
    Grain_Mois_muskmelon = 88.7

    Bushel_Wght_apple = 44
    Grain_Mois_apple = 82

    Bushel_Wght_orange = 42
    Grain_Mois_orange = 73.5

    Bushel_Wght_papaya = 43
    Grain_Mois_papaya = 84.2

    Bushel_Wght_coconut = 61
    Grain_Mois_coconut = 9.3

    Bushel_Wght_cotton = 32
    Grain_Mois_cotton = 6.5

    Bushel_Wght_jute = 48
    Grain_Mois_jute = 13.2

    Bushel_Wght_coffee = 29
    Grain_Mois_coffee = 12

    if Cr=='rice':
        Ratio = ((100-Grain_m)/(100-Grain_Mois_rice)) * Grain_Wght
        Acre = harvested_area / 43560
        Lbs = Ratio / Acre
        bush = Lbs / 56
        yld = Lbs * 0.00112085
        yld_round = round(yld, 3)


    elif Cr=='maize':
        Ratio = (100-Grain_m)/(100-Grain_Mois_maize) *Grain_Wght
        Acre = harvested_area / 43560
        Lbs = Ratio / Acre
        bush = Lbs / 56
        yld = Lbs * 0.00112085
        yld_round = round(yld,3)


    elif Cr=='chickpea':
        Ratio = (100-Grain_m)/(100-Grain_Mois_chickpea) *Grain_Wght
        Acre = harvested_area / 43560
        Lbs = Ratio / Acre
        bush = Lbs / 56
        yld = Lbs * 0.00112085
        yld_round = round(yld, 3)


    elif Cr=='kidneybeans':
        Ratio = (100-Grain_m)/(100-Grain_Mois_chickpea) *Grain_Wght
        Acre = harvested_area / 43560
        Lbs = Ratio / Acre
        bush = Lbs / 56
        yld = Lbs * 0.00112085
        yld_round = round(yld,3)


    elif Cr=='pigeonpeas':
        Ratio = (100-Grain_m)/(100-Grain_Mois_pigeonpeas) *Grain_Wght
        Acre = harvested_area / 43560
        Lbs = Ratio / Acre
        bush = Lbs / 56
        yld = Lbs * 0.00112085
        yld_round = round(yld,3)


    elif Cr=='mothbeans':
        Ratio = (100-Grain_m)/(100-Grain_Mois_mothbeans) *Grain_Wght
        Acre = harvested_area / 43560
        Lbs = Ratio / Acre
        bush = Lbs / 56
        yld = Lbs * 0.00112085
        yld_round = round(yld, 3)


    elif Cr=='mungbean':
        Ratio = (100-Grain_m)/(100-Grain_Mois_mungbean) *Grain_Wght
        Acre = harvested_area / 43560
        Lbs = Ratio / Acre
        bush = Lbs / 56
        yld = Lbs * 0.00112085
        yld_round = round(yld, 2)


    elif Cr=='blackgram':
        Ratio = (100-Grain_m)/(100-Grain_Mois_blackgram) *Grain_Wght
        Acre = harvested_area / 43560
        Lbs = Ratio / Acre
        bush = Lbs / 56
        yld = Lbs * 0.00112085
        yld_round = round(yld,3)


    elif Cr=='lentil':
        Ratio = (100-Grain_m)/(100-Grain_Mois_lentil) *Grain_Wght
        Acre = harvested_area / 43560
        Lbs = Ratio / Acre
        bush = Lbs / 56
        yld = Lbs * 0.00112085
        yld_round = round(yld,3)


    elif Cr=='pomegranate':
        Ratio = (100-Grain_m)/(100-Grain_Mois_pomegranate) *Grain_Wght
        Acre = harvested_area / 43560
        Lbs = Ratio / Acre
        bush = Lbs / 56
        yld = Lbs * 0.00112085
        yld_round = round(yld, 3)


    elif Cr=='banana':
        Ratio = (100-Grain_m)/(100-Grain_Mois_banana) *Grain_Wght
        Acre = harvested_area / 43560
        Lbs = Ratio / Acre
        bush = Lbs / 56
        yld = Lbs * 0.00112085
        yld_round = round(yld,3)


    elif Cr=='mango':
        Ratio = (100-Grain_m)/(100-Grain_Mois_mango) *Grain_Wght
        Acre = harvested_area / 43560
        Lbs = Ratio / Acre
        bush = Lbs / 56
        yld = Lbs * 0.00112085
        yld_round = round(yld,3)


    elif Cr=='grapes':
        Ratio = (100-Grain_m)/(100-Grain_Mois_grapes) *Grain_Wght
        Acre = harvested_area / 43560
        Lbs = Ratio/ Acre
        bush = Lbs / 56
        yld = Lbs * 0.00112085
        yld_round = round(yld, 3)


    elif Cr=='watermelon':
        Ratio = (100-Grain_m)/(100-Grain_Mois_watermelon) *Grain_Wght
        Acre = harvested_area / 43560
        Lbs = Ratio/ Acre
        bush = Lbs / 56
        yld = Lbs * 0.00112085
        yld_round = round(yld, 3)


    elif Cr=='muskmelon':
        Ratio = (100-Grain_m)/(100-Grain_Mois_muskmelon) *Grain_Wght
        Acre = harvested_area / 43560
        Lbs = Ratio/ Acre
        bush = Lbs / 56
        yld = Lbs * 0.00112085
        yld_round = round(yld,3)


    elif Cr=='apple':
        Ratio = (100-Grain_m)/(100-Grain_Mois_apple) *Grain_Wght
        Acre = harvested_area / 43560
        Lbs = Ratio / Acre
        bush = Lbs / 56
        yld = Lbs * 0.00112085
        yld_round = round(yld, 3)


    elif Cr=='orange':
        Ratio = (100-Grain_m)/(100-Grain_Mois_orange) *Grain_Wght
        Acre = harvested_area / 43560
        Lbs = Ratio / Acre
        bush = Lbs / 56
        yld = Lbs * 0.00112085
        yld_round = round(yld,3)


    elif Cr=='papaya':
        Ratio = (100-Grain_m)/(100-Grain_Mois_papaya) *Grain_Wght
        Acre = harvested_area / 43560
        Lbs = Ratio / Acre
        bush = Lbs / 56
        yld = Lbs * 0.00112085
        yld_round = round(yld,3)


    elif Cr=='coconut':
        Ratio = (100-Grain_m)/(100-Grain_Mois_coconut) *Grain_Wght
        Acre = harvested_area / 43560
        Lbs = Ratio / Acre
        bush = Lbs / 56
        yld = Lbs * 0.00112085
        yld_round = round(yld,3)


    elif Cr=='cotton':
        Ratio = (100-Grain_m)/(100-Grain_Mois_cotton) *Grain_Wght
        Acre = harvested_area / 43560
        Lbs = Ratio / Acre
        bush = Lbs / 56
        yld = Lbs * 0.00112085
        yld_round = round(yld, 3)


    elif Cr=='jute':
        Ratio = (100-Grain_m)/(100-Grain_Mois_jute) *Grain_Wght
        Acre = harvested_area / 43560
        Lbs = Ratio / Acre
        bush = Lbs / 56
        yld = Lbs * 0.00112085
        yld_round = round(yld,3)


    elif Cr=='coffee':
        Ratio = (100-Grain_m)/(100-Grain_Mois_coffee) *Grain_Wght
        Acre = harvested_area / 43560
        Lbs = Ratio / Acre
        bush = Lbs / 56
        yld = Lbs * 0.00112085
        yld_round = round(yld,3)
    
    return yld_round



