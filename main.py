import os
from PIL import Image, ImageDraw, ImageFont
W,H=1024,1024; CONFIRMED='CONFIRMED'; OFFICIAL='OFFICIAL'; REPORTED='REPORTED'; CLAIM='CLAIM'; OUT=os.path.join(os.environ.get('MAKEFUN_OUTPUT_DIR','out'),'entry.png'); CREAM=(247,243,232); INK=(17,17,17); RED=(185,28,28); NAVY=(30,58,95); TEAL=(13,110,110); GOLD=(176,132,28); GREY=(90,90,90); LGREY=(232,228,216); GREEN=(22,120,60); BLUE=(30,90,180); ORANGE=(200,90,10)
def F(p,s):
    try: return ImageFont.truetype(p,s)
    except Exception: return ImageFont.load_default()
SERIF='/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf'; SANS='/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'; SANSB='/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'
fMast=F(SERIF,33); fSub=F(SANS,12); fKick=F(SANSB,11); fReg=F(SANSB,9); fUtc=F(SANSB,8); fNum=F(SANSB,17); fNumL=F(SANS,8); fHeroH=F(SANSB,13); fHeroD=F(SANS,10); fCardH=F(SANSB,10); fCardD=F(SANS,9); fAlso=F(SANS,8); fAlsoB=F(SANSB,8); fLeg=F(SANS,8); fLegB=F(SANSB,8); fDate=F(SANS,10); fDateB=F(SANSB,10); fFoot=F(SANS,8); fChip=F(SANSB,7); fPin=F(SANSB,8)
def T(d,x,y,s,f,fill=INK,anchor='la'):
    d.text((x,y),s,font=f,fill=fill,anchor=anchor)
def WR(s,f,mx):
    ls=[]; cur=''
    for w in s.split():
        t=(cur+' '+w).strip()
        if f.getlength(t)<=mx: cur=t
        else:
            if cur: ls.append(cur)
            cur=w
    if cur: ls.append(cur)
    return ls
def BX(d,x,y,w,h,fc,oc=None,wd=1):
    d.rectangle([x,y,x+w,y+h],fill=fc,outline=oc,width=wd)
def CHIP(d,x,y,s,fc):
    w=fChip.getlength(s)+10; BX(d,x,y,w,13,fc); T(d,x+5,y+2,s,fChip,(255,255,255)); return w
def LINE(d,x,y,w,h,fc):
    d.line([(x,y),(x+w,y+h)],fill=fc,width=2)
im=Image.new('RGB',(W,H),CREAM); d=ImageDraw.Draw(im)
HEROES=[("1 RIYADH · MIDDLE EAST",CONFIRMED,"Houthi drone hits Riyadh's tallest tower again, 11 hurt","A Houthi drone struck the PIF tower, Riyadh's tallest, for the second time in a week. At least 11 were hurt: 2 Saudis, 2 Indians, 3 Nepalis and 4 Egyptians.","Reuters · AP"),("2 SHANGHAI · ASIA",OFFICIAL,"China probes Shanghai party chief Chen Jining","Chen Jining, 62, is probed for serious violations, the fourth Politburo member to fall in a widening elite purge this year.","CCDI · Xinhua"),("3 NEW YORK · US/TECH",CONFIRMED,"Huawei guilty on 10 of 12 counts","A US federal jury found Huawei guilty on 10 of 12 counts, including trade-secret theft and bank fraud. It was cleared of racketeering.","US court · AP")]
CARDS=[("4 ZAPORIZHZHIA · EUROPE/WAR",REPORTED,"Russian attacks kill 9 across Ukraine in a day","Russia fired 96 drones; 73 were shot down. Nine were killed and 81 wounded.","Kyiv officials"),("5 CAS · AFRICA/SPORT",OFFICIAL,"CAS hands Senegal back the AFCON title","Morocco forfeited 3-0, turning the final into a 1-0 Senegal win.","CAS"),("6 HORMUZ · MIDDLE EAST",REPORTED,"IRGC attacks container ship in Hormuz","An IRGC attack hit a container ship at 18:58 UTC, disabling navigation.","UKMTO · wires"),("7 NEW YORK · WORLD/MARKETS",CONFIRMED,"Dow closes above 50,000 for the first time","The Dow closed at 50,018. Taiwan's Taiex jumped a record 8.99 percent.","Market close"),("8 REDMOND · WORLD/TECH",REPORTED,"Microsoft declares 'Code Red' after historic outage","After a 24-hour outage, Microsoft vowed recovery within one hour.","Reuters"),("9 ESKISEHIR · EUROPE",REPORTED,"Turkish military helicopter crash kills 5","An AS-532 helicopter crashed in Eskisehir, killing all five on board.","Turkish officials"),("10 CARTAGENA · AMERICAS",REPORTED,"Supermarket hostages: 25 held in Cartagena","Gunmen held 25 hostages; five elderly women were freed in Cartagena.","Colombian officials"),("11 ADEN · MIDDLE EAST",REPORTED,"Houthis advance within 60 km of Aden","Houthi forces advanced to within 60 km of the port city of Aden.","Wires"),("12 LAHJ · MIDDLE EAST",REPORTED,"Saudi strikes kill 25, wound 6 in Yemen","Strikes in Wadi Maabaq, Lahj, killed or left missing 25 and wounded six.","Yemeni officials"),("13 JIUQUAN · WORLD/SPACE",OFFICIAL,"China names first foreign astronaut for Tiangong","The Shenzhou-24 crew includes Muhammad Zeeshan Ali of Pakistan.","CMSA")]
ALSO=[("14","Ankara","Haftar visits Turkey first time","REPORTED"),("15","London","UK sanctions Houthis, 4 officials","OFFICIAL"),("16","Villavicencio","Car bomb injures 23","REPORTED"),("17","Gaza","Israel kills Hamas security chief","REPORTED"),("18","Baghdad","Iraq seizes Kurdish oilfields","OFFICIAL"),("19","Gaza","Meningitis alert, 272 cases in Oct.","OFFICIAL"),("20","DR Congo","Missing Cessna 208, rebels claim hit","CLAIM"),("21","Hanoi","Hot-pot blast kills at least 6","REPORTED"),("22","Gulf of Finland","Ukraine hits ship Sparta II","REPORTED"),("23","Kuala Lumpur","Malaysia to return migrants","OFFICIAL"),("24","Ulleungdo","S. Korea shelter order, jets in ADIZ","OFFICIAL"),("25","Dhaka","Hasina plans return 16 December","REPORTED"),("26","The Hague","14 nations back ICJ Myanmar ruling","REPORTED"),("27","Jakarta","Indonesia nominates 2 VP candidates","OFFICIAL"),("28","Beijing","China sentences Ma to death for spying","OFFICIAL"),("29","Brussels","NATO vows defence vs space threat","OFFICIAL"),("30","Mexico City","US drone aided capture Fri 20 Nov","REPORTED"),("31","San Salvador","Bukele names 3 dead in Haiti","OFFICIAL"),("32","Ottawa","Pentagon: only 41.9% of air fleet ready","REPORTED"),("33","Washington","US adds Megaspeed to blacklist","OFFICIAL"),("34","Kyiv","Zelensky urges talks with Russia, US, EU","REPORTED"),("35","Ras Al Khaimah","Bus-truck crash kills 13","REPORTED"),("36","London","England record 5,258 heat deaths","OFFICIAL"),("37","Kourou","Ariane 6 lofts 36 Amazon satellites","OFFICIAL"),("38","Cikande","Factory-fire toll rises to 26","REPORTED")]
UTC=[("02:15","NATO vows space defence"),("08:16","Hanoi hot-pot blast"),("10:42","Saudi strikes Yemen"),("14:27","Riyadh tower hit"),("16:51","Houthis 60 km from Aden"),("18:58","Hormuz ship attack"),("20:41","Huawei guilty")]
NUMS=[("11","HURT IN RIYADH"),("9","KILLED IN UKRAINE"),("50,018","DOW CLOSE"),("+8.99%","TAIEX RECORD"),("25","KILLED IN LAHJ"),("26","CIKANDE TOLL"),("10/12","HUAWEI COUNTS"),("96","DRONES AT UKRAINE")]
NA=[(70,-168),(70,-140),(60,-140),(60,-125),(49,-125),(49,-110),(32,-117),(29,-110),(23,-106),(19,-104),(15,-92),(9,-83),(9,-79),(12,-72),(18,-66),(25,-80),(30,-81),(35,-75),(40,-74),(44,-68),(48,-70),(55,-60),(60,-64),(66,-55),(70,-58)]
SA=[(10,-75),(5,-77),(0,-80),(-5,-81),(-15,-75),(-25,-70),(-35,-70),(-45,-73),(-52,-68),(-40,-62),(-30,-48),(-20,-40),(-10,-35),(-5,-35),(0,-44),(5,-52),(8,-60),(10,-62)]
AF=[(35,-6),(35,10),(32,20),(30,32),(27,34),(20,37),(15,40),(11,44),(5,48),(-2,41),(-10,40),(-18,35),(-25,32),(-33,20),(-30,15),(-20,12),(-10,13),(-2,9),(4,6),(6,-8),(15,-17),(20,-16),(27,-13),(30,-10)]
EU=[(70,30),(68,45),(70,60),(72,75),(70,90),(72,110),(70,130),(68,160),(66,180),(60,170),(55,160),(50,142),(45,135),(40,128),(35,122),(30,120),(25,110),(20,108),(15,105),(10,100),(8,98),(10,92),(15,88),(20,86),(23,80),(25,72),(25,62),(28,58),(30,50),(30,48),(25,48),(20,45),(15,42),(12,44),(15,40),(18,38),(20,35),(25,32),(30,35),(36,36),(40,30),(42,28),(45,28),(40,20),(38,15),(40,10),(44,8),(45,5),(48,0),(50,-2),(55,-5),(58,-8),(60,-5),(65,5),(68,15),(70,25)]
AU=[(-12,130),(-15,135),(-20,140),(-25,150),(-30,153),(-35,150),(-38,145),(-35,138),(-32,132),(-25,125),(-20,118),(-15,122),(-12,126)]
ISL=[[(35,138),(40,141),(44,144),(35,140)], [(-41,174),(-37,176),(-41,175)], [(60,-45),(64,-40),(60,-42)], [(21,158),(24,160)]]
PINS=[(1,24.7,46.7,0,-14),(2,31.2,121.5,0,-14),(3,40.7,-74.0,14,-12),(4,47.8,35.2,0,-14),(5,14.7,-17.4,0,-14),(6,26.5,56.3,0,-14),(7,40.7,-74.0,-16,10),(8,47.7,-122.1,0,-14),(9,39.8,30.5,0,-14),(10,10.4,-75.5,0,-14),(11,12.8,45.0,12,-12),(12,13.0,44.9,-14,10),(13,39.7,98.5,0,-14)]
LEG=[("1","Riyadh"),("2","Shanghai"),("3","New York"),("4","Zaporizhzhia"),("5","Dakar"),("6","Hormuz"),("7","New York"),("8","Redmond"),("9","Eskisehir"),("10","Cartagena"),("11","Aden"),("12","Lahj"),("13","Jiuquan")]
def PJ(lat,lon,mx,my,mw,mh):
    return (mx+(lon+180)/360*mw,my+(90-lat)/180*mh)
T(d,14,8,"THE WORLD ON ONE DAY",fKick,RED); T(d,1010,8,"38 STORIES · 6 REGIONS · 13 FIELDS",fKick,INK,anchor='ra'); T(d,14,26,"Tuesday 24 November 2026",fMast,INK); T(d,14,66,"Riyadh tower hit again  ·  Chen Jining probed  ·  Huawei guilty on 10 of 12 counts",fSub,RED)
REG=[("Europe 9",236,NAVY),("Middle East 8",210,RED),("Asia 8",210,TEAL),("Africa 2",52,GOLD),("Americas 7",184,(90,60,140)),("World/Space 4",104,GREY)]
rx=14
for nm,wd,cc in REG:
    BX(d,rx,86,wd,20,cc); T(d,rx+wd/2,90,nm,fReg,(255,255,255),anchor='ma'); rx+=wd
BX(d,14,110,996,32,LGREY); T(d,22,113,"THE DAY IN UTC",fKick,RED)
ux=150
for hh,ev in UTC:
    T(d,ux,113,hh,fUtc,RED); T(d,ux,124,ev,fUtc,INK); ux+=122
BX(d,14,146,996,44,(255,255,255),INK,1); T(d,22,149,"THE DAY IN NUMBERS",fKick,RED)
nx=170
for v,lb in NUMS:
    T(d,nx,148,v,fNum,INK,anchor='ma'); T(d,nx,168,lb,fNumL,GREY,anchor='ma'); nx+=103
def SCENE(i,x,y,w,h):
    BX(d,x,y,w,h,(20,30,60) if i==0 else (120,30,30) if i==1 else (30,58,95))
    if i==0:
        d.rectangle([x+120,y+8,x+150,y+h],fill=(200,190,160)); d.polygon([(x+120,y+8),(x+150,y+8),(x+135,y-2)],fill=(220,210,180))
        for yy in range(y+16,y+h-6,12):
            for xx in (x+128,x+138): d.rectangle([xx,yy,xx+5,yy+5],fill=(255,220,90))
        d.ellipse([x+170,y+10,x+210,y+40],fill=(150,150,150)); d.ellipse([x+185,y+2,x+225,y+30],fill=(180,180,180)); d.ellipse([x+40,y+20,x+70,y+34],fill=(70,70,70)); d.line([(x+55,y+27),(x+90,y+45)],fill=(255,255,255),width=2); d.ellipse([x+88,y+42,x+98,y+50],fill=(255,255,255))
        for bx in range(0,w,46): d.rectangle([x+bx,y+h-18,x+bx+34,y+h],fill=(40,45,70))
    elif i==1:
        d.rectangle([x+30,y+45,x+50,y+h],fill=(160,30,30)); d.rectangle([x+w-50,y+45,x+w-30,y+h],fill=(160,30,30)); d.polygon([(x+10,y+48),(x+w-10,y+48),(x+w-30,y+18),(x+30,y+18)],fill=(185,28,28)); d.rectangle([x+110,y+55,x+210,y+h-8],fill=(255,255,255)); d.line([(x+120,y+68),(x+200,y+68)],fill=INK,width=2); d.line([(x+120,y+80),(x+200,y+80)],fill=GREY,width=2); d.line([(x+120,y+92),(x+175,y+92)],fill=GREY,width=2); d.ellipse([x+212,y+40,x+248,y+68],fill=RED); T(d,x+230,y+51,"CCDI",fChip,(255,255,255),anchor='mm')
    else:
        d.rectangle([x+20,y+55,x+w-20,y+h],fill=(210,200,180)); d.polygon([(x+20,y+55),(x+w/2,y+18),(x+w-20,y+55)],fill=(180,160,130))
        for cx in (x+60,x+150,x+240):
            d.rectangle([cx,y+58,cx+16,y+h-6],fill=(255,255,255))
        d.rectangle([x+120,y+62,x+200,y+78],fill=(30,58,95)); T(d,x+160,y+64,"COURT",fChip,(255,255,255),anchor='ma'); d.rectangle([x+250,y+30,x+290,y+44],fill=(120,80,40)); d.line([(x+270,y+44),(x+270,y+70)],fill=(120,80,40),width=4)
for i,(kick,chip,head,deck,src) in enumerate(HEROES):
    hx=14+i*336; BX(d,hx,194,324,178,(255,255,255),INK,1); SCENE(i,hx+6,200,312,76); T(d,hx+8,279,kick,fKick,RED); cw=CHIP(d,hx+8,292,chip,GREEN if chip==CONFIRMED else BLUE); T(d,hx+14+cw,293,src,fLeg,GREY)
    yy=306
    for ln in WR(head,fHeroH,308):
        T(d,hx+8,yy,ln,fHeroH); yy+=15
    for ln in WR(deck,fHeroD,308):
        T(d,hx+8,yy,ln,fHeroD); yy+=11
def MINI(i,x,y,w,h):
    cols=[(20,30,60),(22,120,60),(30,58,95),(13,110,110),(120,30,30),(160,90,20),(90,60,140),(60,60,60),(176,132,28),(30,58,95)]; BX(d,x,y,w,h,cols[i])
    if i==0:
        d.ellipse([x+20,y+6,x+44,y+22],fill=(255,200,80))
        for k in range(3): d.ellipse([x+70+k*36,y+8,x+88+k*36,y+20],fill=(200,200,200))
    elif i==1:
        d.polygon([(x+85,y+4),(x+100,y+18),(x+70,y+18)],fill=(255,215,0)); d.rectangle([x+80,y+18,x+90,y+28],fill=(255,215,0))
    elif i==2:
        d.rectangle([x+30,y+14,x+150,y+26],fill=(255,255,255)); d.rectangle([x+60,y+4,x+80,y+14],fill=(200,60,40))
    elif i==3:
        d.line([(x+10,y+24),(x+60,y+14),(x+110,y+10),(x+160,y+4)],fill=(255,255,255),width=3); d.line([(x+10,y+24),(x+170,y+24)],fill=(255,215,0),width=2)
    elif i==4:
        d.rectangle([x+40,y+6,x+140,y+26],fill=(40,40,40)); d.rectangle([x+50,y+10,x+60,y+16],fill=RED); d.rectangle([x+70,y+10,x+80,y+16],fill=RED)
    elif i==5:
        d.ellipse([x+70,y+4,x+110,y+20],fill=(200,200,200)); d.line([(x+90,y+20),(x+90,y+28)],fill=(200,200,200),width=3)
    elif i==6:
        d.rectangle([x+50,y+6,x+130,y+26],fill=(255,255,255)); d.rectangle([x+60,y+12,x+120,y+18],fill=RED)
    elif i==7:
        d.polygon([(x+20,y+26),(x+60,y+6),(x+100,y+26)],fill=(200,180,120)); d.polygon([(x+80,y+26),(x+130,y+6),(x+170,y+26)],fill=(180,160,100))
    elif i==8:
        d.rectangle([x+50,y+10,x+130,y+24],fill=(255,200,80)); d.ellipse([x+60,y+16,x+72,y+24],fill=INK); d.ellipse([x+110,y+16,x+122,y+24],fill=INK)
    else:
        d.polygon([(x+85,y+2),(x+95,y+22),(x+75,y+22)],fill=(255,255,255)); d.ellipse([x+80,y+22,x+90,y+28],fill=(255,150,50))
for i,(kick,chip,head,deck,src) in enumerate(CARDS):
    cx=14+(i%5)*201; cy=376+(i//5)*100; BX(d,cx,cy,192,100,(255,255,255),INK,1); MINI(i,cx+4,cy+4,184,26); T(d,cx+6,cy+32,kick,fCardH,RED)
    yy=cy+44
    for ln in WR(head,fCardH,180)[:2]:
        T(d,cx+6,yy,ln,fCardH); yy+=11
    for ln in WR(deck,fCardD,180)[:2]:
        T(d,cx+6,yy,ln,fCardD); yy+=10
    cw=CHIP(d,cx+6,cy+86,chip,GREEN if chip==CONFIRMED else BLUE); T(d,cx+12+cw,cy+87,src,fLeg,GREY)
T(d,14,582,"WORLD MAP — 13 STORIES PINNED",fKick,RED); T(d,500,582,"ALSO ON TUESDAY — 25 MORE STORIES",fKick,RED)
MX,MY,MW,MH=14,600,380,190; BX(d,MX,MY,MW,MH,(210,225,235),INK,1)
for poly in (NA,SA,AF,EU,AU):
    d.polygon([PJ(la,lo,MX,MY,MW,MH) for la,lo in poly],fill=(120,170,110),outline=(60,110,60))
for isl in ISL:
    d.polygon([PJ(la,lo,MX,MY,MW,MH) for la,lo in isl],fill=(120,170,110),outline=(60,110,60))
for n,la,lo,dx,dy in PINS:
    px,py=PJ(la,lo,MX,MY,MW,MH); qx,qy=px+dx,py+dy
    if dx or dy: d.line([(px,py),(qx,qy)],fill=RED,width=1)
    d.ellipse([qx-8,qy-8,qx+8,qy+8],fill=RED,outline=(255,255,255),width=1); T(d,qx,qy,str(n),fPin,(255,255,255),anchor='mm')
for i,(n,nm) in enumerate(LEG):
    T(d,404,602+i*13,n+" "+nm,fLeg,INK)
for ci in range(2):
    ax=500+ci*258
    for ri in range(13 if ci==0 else 12):
        n,city,txt,chip=ALSO[ci*13+ri]; yy=602+ri*21; cc=GREEN if chip=="OFFICIAL" else ORANGE if chip=="CLAIM" else BLUE
        ln=n+" "+city+": "+txt
        while fAlso.getlength(ln)>224 and " " in ln: ln=ln.rsplit(" ",1)[0]+"..."
        T(d,ax,yy,ln,fAlso,INK); T(d,ax+250,yy,chip[:3],fChip,cc,anchor='ra')
BX(d,14,872,996,104,(255,240,240),RED,2); T(d,22,878,"DATE CHECK",fDateB,RED)
DT="Every story above happened or was first reported on Tuesday 24 November 2026. Wires read up to 23:00 UTC. LEFT OUT (not 24 Nov): Hormuz mine claims (23 Nov) · Nvidia Huang returns as CEO (23 Nov) · EU 22nd sanctions package (23 Nov) · COP31 ends no deal (22 Nov) · Merkury sunk (22 Nov) · El Chapo Isidro captured (Fri 20 Nov) · Cikande factory fire began (Sat 21 Nov) · Trump hush-money appeal ruling (23 Nov) · ATP Finals (22 Nov) · F1 Las Vegas GP (Sat 21 Nov). NOT YET: Shenzhou-24 launch (Wed 25 Nov 00:18 UTC) · MPR session picks VP (11 Dec) · Huawei sentencing (Sep 2027) · Hasina returns (16 Dec)."
yy=896
for ln in WR(DT,fDate,980):
    T(d,22,yy,ln,fDate); yy+=13
T(d,14,984,"Sources: Reuters · AP · UKMTO · CAS · CCDI · CMSA · Xinhua · market close · wires.",fFoot,GREY); T(d,14,996,"CONFIRMED = 2+ outlets · OFFICIAL = on record · REPORTED = one outlet · CLAIM = one side only. Scenes are drawn illustrations, not photographs.",fFoot,GREY)
os.makedirs(os.path.dirname(OUT),exist_ok=True); im.save(OUT,optimize=True); print(OUT,os.path.getsize(OUT))
