def trial_balance(p,y,r):
    #p:本金(萬元) y:年 r:年利率(%)
    title = ['期數','本金(萬元)','利息(%)','累計本金利息']
    p_per = (p*10000)/(12*y)#每期應付本金
    p_remained = p*10000#剩餘本金
    p_paid = 0#本金利息累計
    r = r/(12*100)#利率
    row = ['',p_per,'','']

    import csv
    with open('trial_balance.csv','w',newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(title)
        for j in range(12*y):
            row[0] = j+1
            interest = p_remained*r
            row[2] = float('%.4f' % interest)
            p_paid += p_remained*r + p_per
            p_remained -= p_per
            row[3] = float('%.4f' % p_paid)
            writer.writerow(row)





            
