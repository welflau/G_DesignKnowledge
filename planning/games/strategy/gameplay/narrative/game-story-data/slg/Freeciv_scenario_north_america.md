# 文明 · 历史场景「north_america」

> 来源：longturn/freeciv21
> 原始链接：https://github.com/longturn/freeciv21
> 分类：gameplay
> 标签：文明, 4X策略SLG, 历史场景, 剧本
> 游戏类型：4X策略SLG

## 概述
Freeciv历史场景脚本：north_america

## 正文
```sav

[scenario]
game_version=3000000
is_scenario=TRUE
name=_("North America (classic/medium)")
authors=_("Robert Michael Best")
description=_("Overhead 116x100 map of North America (conical projection).")
save_random=FALSE
players=FALSE
startpos_nations=FALSE
lake_flooding=TRUE
handmade=TRUE
ruleset_locked=FALSE
ruleset_caps="+std-terrains"

[savefile]
options=" +version3"
version=40
reason="Scenario"
revision="3.0.0-alpha3+"
rulesetdir="classic"
improvement_size=68
improvement_vector="Airport","Aqueduct","Bank","Barracks","Barracks II","Barracks III","Cathedral","City Walls","Coastal Defense","Colosseum","Courthouse","Factory","Granary","Harbour","Hydro Plant","Library","Marketplace","Mass Transit","Mfg. Plant","Nuclear Plant","Offshore Platform","Palace","Police Station","Port Facility","Power Plant","Recycling Center","Research Lab","SAM Battery","SDI Defense","Sewer System","Solar Plant","Space Component","Space Module","Space Structural","Stock Exchange","Super Highways","Supermarket","Temple","University","Apollo Program","A.Smith's Trading Co.","Colossus","Copernicus' Observatory","Cure For Cancer","Darwin's Voyage","Eiffel Tower","Great Library","Great Wall","Hanging Gardens","Hoover Dam","Isaac Newton's College","J.S. Bach's Cathedral","King Richard's Crusade","Leonardo's Workshop","Lighthouse","Magellan's Expedition","Manhattan Project","Marco Polo's Embassy","Michelangelo's Chapel","Oracle","Pyramids","SETI Program","Shakespeare's Theatre","Statue of Liberty","Sun Tzu's War Academy","United Nations","Women's Suffrage","Coinage"
technology_size=88
technology_vector="A_NONE","Advanced Flight","Alphabet","Amphibious Warfare","Astronomy","Atomic Theory","Automobile","Banking","Bridge Building","Bronze Working","Ceremonial Burial","Chemistry","Chivalry","Code of Laws","Combined Arms","Combustion","Communism","Computers","Conscription","Construction","Currency","Democracy","Economics","Electricity","Electronics","Engineering","Environmentalism","Espionage","Explosives","Feudalism","Flight","Fusion Power","Genetic Engineering","Guerilla Warfare","Gunpowder","Horseback Riding","Industrialization","Invention","Iron Working","Labor Union","Laser","Leadership","Literacy","Machine Tools","Magnetism","Map Making","Masonry","Mass Production","Mathematics","Medicine","Metallurgy","Miniaturization","Mobile Warfare","Monarchy","Monotheism","Mysticism","Navigation","Nuclear Fission","Nuclear Power","Philosophy","Physics","Plastics","Polytheism","Pottery","Radio","Railroad","Recycling","Refining","Refrigeration","Robotics","Rocketry","Sanitation","Seafaring","Space Flight","Stealth","Steam Engine","Steel","Superconductors","Tactics","The Corporation","The Republic","The Wheel","Theology","Theory of Gravity","Trade","University","Warrior Code","Writing"
activities_size=21
activities_vector="Idle","Pollution","Unused Road","Mine","Irrigate","Fortified","Fortress","Sentry","Unused Railroad","Pillage","Goto","Explore","Transform","Unused","Unused Airbase","Fortifying","Fallout","Unused Patrol","Base","Road","Convert"
specialists_size=3
specialists_vector="elvis","scientist","taxman"
trait_size=3
trait_vector="Expansionist","Trader","Aggressive"
extras_size=34
extras_vector="Irrigation","Mine","Oil Well","Pollution","Hut","Farmland","Fallout","Fortress","Airbase","Buoy","Ruins","Road","Railroad","River","Gold","Iron","Game","Furs","Coal","Fish","Fruit","Gems","Buffalo","Wheat","Oasis","Peat","Pheasant","Resources","Ivory","Silk","Spice","Whales","Wine","Oil"
multipliers_size=0
diplstate_type_size=7
diplstate_type_vector="Armistice","War","Cease-fire","Peace","Alliance","Never met","Team"
city_options_size=3
city_options_vector="Disband","Sci_Specialists","Tax_Specialists"
action_size=44
action_vector="Establish Embassy","Establish Embassy Stay","Investigate City","Investigate City Spend Unit","Poison City","Poison City Escape","Steal Gold","Steal Gold Escape","Sabotage City","Sabotage City Escape","Targeted Sabotage City","Targeted Sabotage City Escape","Steal Tech","Steal Tech Escape Expected","Targeted Steal Tech","Targeted Steal Tech Escape Expected","Incite City","Incite City Escape","Establish Trade Route","Enter Marketplace","Help Wonder","Bribe Unit","Sabotage Unit","Sabotage Unit Escape","Capture Units","Found City","Join City","Steal Maps","Steal Maps Escape","Bombard","Suitcase Nuke","Suitcase Nuke Escape","Explode Nuclear","Destroy City","Expel Unit","Recycle Unit","Disband Unit","Home City","Upgrade Unit","Paradrop Unit","Airlift Unit","Attack","Conquer City","Heal Unit"
action_decision_size=3
action_decision_vector="nothing","passive","active"
terrident={"name","identifier"
"Inaccessible","i"
"Lake","+"
"Ocean"," "
"Deep Ocean",":"
"Glacier","a"
"Desert","d"
"Forest","f"
"Grassland","g"
"Hills","h"
"Jungle","j"
"Mountains","m"
"Plains","p"
"Swamp","s"
"Tundra","t"
}

[game]
server_state="S_S_INITIAL"
meta_patches="none"
meta_server="http://meta.freeciv.org/metaserver.php"
id=""
serverid=""
level="Normal"
phase_mode="Concurrent"
phase_mode_stored="Concurrent"
phase=0
scoreturn=20
timeoutint=0
timeoutintinc=0
timeoutinc=0
timeoutincmult=1
timeoutcounter=1
turn=0
year=-4000
year_0_hack=FALSE
globalwarming=0
heating=0
warminglevel=8
nuclearwinter=0
cooling=0
coolinglevel=8
random_seed=1586960275
global_advances="1000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"
save_players=FALSE
save_known=FALSE

[random]
saved=FALSE

[script]
code=$$
vars=$$

[settings]
set={"name","value","gamestart"
"aifill",10,5
"alltemperate",FALSE,FALSE
"borders","DISABLED","ENABLED"
"civilwarsize",6,10
"diplbulbcost",100,0
"diplgoldcost",100,0
"flatpoles",100,100
"generator","SCENARIO","RANDOM"
"happyborders","DISABLED","NATIONAL"
"huts",10,15
"landmass",25,30
"mapseed",0,0
"mapsize","FULLSIZE","FULLSIZE"
"maxplayers",12,150
"metamessage","Scenario: North America",""
"revolentype","RANDOM","RANDOM"
"savepalace",FALSE,TRUE
"sciencebox",50,100
"separatepoles",TRUE,TRUE
"singlepole",FALSE,FALSE
"size",12,4
"startpos","DEFAULT","DEFAULT"
"startunits","ccx","ccwwx"
"steepness",30,30
"teamplacement","CLOSEST","CLOSEST"
"techlevel",3,0
"temperature",50,50
"tilesperplayer",100,100
"tinyisles",FALSE,FALSE
"topology","","WRAPX|ISO"
"victories","","SPACERACE|ALLIED"
"wetness",50,50
"xsize",116,64
"ysize",100,64
}
set_count=34
gamestart_valid=FALSE

[ruledata]
government={"name","changes"
"Anarchy",0
"Despotism",0
"Monarchy",0
"Communism",0
"Republic",0
"Democracy",0
}

[map]
have_huts=FALSE
have_resources=FALSE
t0000=":::::::::::::::::::::::::::::::::::::::::::::::::::::   fttftaa   taffaaaaaaaaaaaaaaa  :::::::::::::::::::::::::::::"
t0001="::::::::::::::::::::::::::::::::::::::::::::::::::    ttt t tta    f    faaaaaaaaaaaaa  ::::::::::::::::::::::::::::"
t0002=":::::::::::::::::::::::::::::::::::::::::::::::    t     f ftata     ::   ftaaaaaaaaaaa  :::::::::::::::::::::::::::"
t0003="::::::::::::::::::::::::::::::::::::::::::::::  tt       ftt  ft  :::::::   f ttaaaaaaat :::::::::::::::::::::::::::"
t0004=":::::::::::::::::::::::::::::::::::::::::::::: ft tf   ft f ttaft   :::::::   attaaaaaat  ::::::::::::::::::::::::::"
t0005=":::::::::::::::::::::::         :::::::::::::    ttttt  f  f     aa    ::::::    ttaaaaaa  :::::::::::::::::::::::::"
t0006="::::::::::::::::::::::  ttthttf ::::::::::::: tt   f       tt tftt taf     ::::: fhtaaaaaa  ::::::::::::::::::::::::"
t0007=":::::::::::::::::::::: fhtttttt   ::::::::::  tttt   ft ftftt ttttttttttaf  ::::   taaaaaaa  :::::::::::::::::::::::"
t0008=":::::::::::::::::::    ttmhthmttt   :::::::: tttfhftttt ttt t fhtttttttattt         fttaaaaa  ::::::::::::::::::::::"
t0009=":::::::::::::::     hh ttmhtmmmmttt  ::::::: tt thhhtfh   t h   ttttt ahttthaaat      ftaaaaa  :::::::::::::::::::::"
t0010="::::::::::::::: f  ttttttttthtmmmmtt            fttthhtt     t   f t   ttthtttatt  ::    ttata :::::::::::::::::::::"
t0011=":::::::::::::::      ttfffhhttmmmmmtf tttft      f ttthtt   ath     h   t  httfta ::::::   f   :::::::::::::::::::::"
t0012="::::::::::::::      fhffffthttfmhhtmhttttttfft  tttthtttf  tt fhft ht   f  ttttt    ::::::   :::::::::::::::::::::::"
t0013=":::::::::::::: ffttfffhtfftmhhfthmhmmftttffttttt  thtt ft tft tttt tthf    ttttthtf ::::::::::::::::::::::::::::::::"
t0014="::::::::::::   ftfftfftfffffhhfhhhfhttffffftttfttt f tft    f thttthtt     fttttttt  :::::::::::::::::::::::::::::::"
t0015=":::::::::::: ffffffffffftffffmhhmthmhmmffffftttttttttfthtttthtttthttff    thtthtttff  ::::::::::::::::::::::::::::::"
t0016="::::::::::::  fftttffthtmtmffmthhmmmmmhfffttf+tthtthttthttthttttthttftf        ftttat ::::::::::::::::::::::::::::::"
t0017=":::::::::::::  ttttffhttttmtfhhhmmhhmhthtffff++fttfttttthtttthtttttttttttf  f           ::::::::::::::::::::::::::::"
t0018="::::::::::::: ftfttfmftthmtthmtffhhmhthhhhtff+fftftttttthtthhtthttttf tt      ftt     t   ::::::::::::::::::::::::::"
t0019=":::::::::::::  ffffttffttttmthhfffthhhmhhhhthffffthtttthhtttfthhtttf    ft f tthtth    tt   ::::::::::::::::::::::::"
t0020="::::::::::::::  pft fttffmftthfhfffhmmhmthhhtfffffthttttttttffhhttt     f  f ttttttt   tttf  :::::::::::::::::::::::"
t0021="::::           fttf f  fftttpthtffhtmhhhttftff+tfftftthttttftttthtf           tttttttt htttf     :::::::::::::::::::"
t0022=":::: ff tft tttp  f      fmtptttfftfhmmhmmfhfhfttffffttttttfttftth             ttthtttttttttf  f   :::::::::::::::::"
t0023="::::            ff  ::::   ttthffhhmhmhthfffffffffffffthttfttthtfh             thttttttttthhtffhhf  ::::::::::::::::"
t0024=":::::::::::::::    :::::::  ftmtffhhfffttfffffff+++fffffftfttthttt             tthhtttttfftfhtf fhf ::::::::::::::::"
t0025=":::::::::::::::::::::::::::  ptmffffffffffffffff+ffffffffffftththt               ttttttttthhthfffff  :::::::::::::::"
t0026=":::::::::::::::::::::::::::: pmtttmhfffffffffffffffffffffft+tftttt                tttttthhtt fffffff    ::::::::::::"
t0027=":::::::::::::::::::::::::::: fftmhthhffffffffffffffffffffffftfthtt                 ttfttfttttfhffff f f  :::::::::::"
t0028=":::::::::::::::::::::::::::: fffthfmttmffffffffffffff+ffffffff+ffttt            f  thhttttfhfffffff ffff  ::::::::::"
t0029="::::::::::::::::::::::::::::   fptthfhfmfffffftttfffffffffffffffffftt             fttthtfttthffffff fffff ::::::::::"
t0030="::::::::::::::::::::::::::::: ffftmtmtftffffffffffffffffffff+ffffffftfhttt       ftffffftfthfffff    fff  ::::::::::"
t0031="::::::::::::::::::::::::::::: fffmffhtffffffffffffffffffffffffffffffffffhttttthf  tt fffffhfffff ff  ff  :::::::::::"
t0032="::::::::::::::::::::::::::::: ffffffffffffffffffffffffffffffffffffffffffffffffff   fhffffffffff         ::::::::::::"
t0033=":::::::::::::::::::::::::::::   fffffffffffhghffffffffffffffffffffffffffffffffff    fffffffffff tt      ::::::::::::"
t0034="::::::::::::::::::::::::::::: f  tfffffffffmghmffffffffffffffffffffffffffffffffff   fffffffffffffh   f  ::::::::::::"
t0035="::::::::::::::::::::::::::::: f fffffffffffffffffffffffffffffffffffffffffffffffffff ffffffffffffff    f ::::::::::::"
t0036="::::::::::::::::::::::::::::: f  fffffffffffffffghfhgpfffffffffffffffffffffffffffffffffffffffffffff fff ::::::::::::"
t0037="::::::::::::::::::::::::::::: f  fhfffffffffffffpgggghffhfffffff++ffffffffffffffffffffffffffffffffffff  ::::::::::::"
t0038=":::::::::::::::::::::::::::::    fffffffffhfffffpgggggggggggfffff++fffffffffffffffffffffffffffffhhfhff :::::::::::::"
t0039="::::::::::::::::::::::::::::::::  ffffffffffhmffggggggggggpgffgfffffffffffffffffffffffffffhfhhfhfhf f  :::::::::::::"
t0040="::::::::::::::::::::::::::::::::  ffpffffffffmhfggpggpppgggpggfhfff+fffffffffffffffffffffffffhfhfff f ::::::::::::::"
t0041=":::::::::::::::::::::::::::::::: ffffphfffffhfffgggppppgggggggggffp+ffffffff+fffffffhfhffffhfffhhhf f ::::::::::::::"
t0042="::::::::::::::::::::::::::::::::  ffffhfffffffffpgpppppppggggggghpfgffffffffffffffffffffffhhhphhhh    ::::::::::::::"
t0043="::::::::::::::::::::::::::::::::: ff fffffffffffmggpppppgggggggggggghffffffff+++ffhfffffhhhhhhhhhf :::::::::::::::::"
t0044=":::::::::::::::::::::::::::::::::  ff fffffffffffpgppppppgggggggggggghfffffff+++++fffhffhhhhhhfhff :::::::::::::::::"
t0045="::::::::::::::::::::::::::::::::::   ffffffffffffhhppppppppggggggggggpffffff++f+++ffff+ffhhfhhhhhh :::::::::::::::::"
t0046="::::::::::::::::::::::::::::::::::: fffffffffffffphhppppppppggggggggggfffff++fhffff+++f+fff+hhfhhf :::::::::::::::::"
t0047="::::::::::::::::::::::::::::::::::: fffffppfhfffffphphhhppppppggggggggfffffffffff+fff++pfh++hhhhfh :::::::::::::::::"
t0048="::::::::::::::::::::::::::::::::::: fffffppppfffffpppphhhpppppppgpggggpfffffffhhf+fff++pf+pffhhhh  :::::::::::::::::"
t0049="::::::::::::::::::::::::::::::::::: ffffdpdpgffffhfpfpphppppppppppgggggpgpfffffpf+hhpp+ggffhhhhhf ::::::::::::::::::"
t0050="::::::::::::::::::::::::::::::::::: ffffpdpfdpfffffpppppppppppppppgggggggpppfphhf+hfgpfg++hhhhhh  ::::::::::::::::::"
t0051="::::::::::::::::::::::::::::::::::  fpfddddfpfffffhpppppppppppppppgggggggggffppgp+fpgpff+hhhhhhpf ::::::::::::::::::"
t0052=":::::::::::::::::::::::::::::::::: ffffdpdfpfffffppfffddppppppppppggggggggggffpgp++ppg++phhhhgfpf ::::::::::::::::::"
t0053=":::::::::::::::::::::::::::::::::: ffffdpffppffffdffffddfppppppppppggggggggggppgp++pggggphfhhhpff ::::::::::::::::::"
t0054=":::::::::::::::::::::::::::::::::  ffffdddpppffhfgphffdpddpppfppppggggggggggggpggphgggghhhhhhhfff ::::::::::::::::::"
t0055="::::::::::::::::::::::::::::::::: fffffddfpdddpfpppfffmdpppdpdppppgggggggggggggggggggggphhhhhhf f ::::::::::::::::::"
t0056=":::::::::::::::::::::::::::::::::  fffffmmddpddppdpdffmdpppppdpppppgggggggggggggggggggpghhhhhhhp  ::::::::::::::::::"
t0057=":::::::::::::::::::::::::::::::::: fffpdddddpddddpddfddpddpddppppppggggggggggggpgggggfpfhhhhhhhff ::::::::::::::::::"
t0058=":::::::::::::::::::::::::::::::::  ffffddmddddddddpppddpppdpppppppgggggggggggppgggghhhfhhhhhhhhff ::::::::::::::::::"
t0059="::::::::::::::::::::::::::::::::: fffffddddddppdf fppdpddffpppppppggggggggggppfgpggphfhhhhhhhffff ::::::::::::::::::"
t0060="::::::::::::::::::::::::::::::::: ffpffmdmdmddddfdfpffdppfffppppppggggggggppfpfppfpphhfhhhhhhffpf ::::::::::::::::::"
t0061=":::::::::::::::::::::::::::::::::  fppfffddmdddddmdpmdpppfffppppppggpggpgpphhhhhpfppfhhhhhhhfhff  ::::::::::::::::::"
t0062=":::::::::::::::::::::::::::::::::: fppffddfdddddmmdfpdddfpffppppppppppphggpfhhhhhffffhhhhhhhffff :::::::::::::::::::"
t0063=":::::::::::::::::::::::::::::::::: fpphfdddmdmddddddpdddfdffppppppppppphpgpfhhhhhgfhmhfffhhffgf  :::::::::::::::::::"
t0064="::::::::::::::::::::::::::::::::::  fpffmmddddpdddfdddpfppfdppppppppgpppppphhhhhgpffhhhhhffffhf ::::::::::::::::::::"
t0065="::::::::::::::::::::::::::::::::::: fppffdddddddddddpdddhfdfmdppppppppgpphhhhhhhgpffhffhhfhfhff ::::::::::::::::::::"
t0066="::::::::::::::::::::::::::::::::::: ppppfmfmmmdmffdddmmpfffdfpppppppppgppghhhhhggphhhhhhpffpff  ::::::::::::::::::::"
t0067=":::::::::::::::::::::::::::::::::::  pdpffdfdmmmddddddddmdffdppppppppppghphfhhhpphfhhhfffffff  :::::::::::::::::::::"
t0068=":::::::::::::::::::::::::::::::::::: fddpffpddpdddfdddmddmhfhppppppppppphpphfhfgphfhhhfhfhfff ::::::::::::::::::::::"
t0069="::::::::::::::::::::::::::::::::::::  pmpfddmdddddmdmdmmdddfdpppppppppppphfffffhghfhhffffppff  :::::::::::::::::::::"
t0070="::::::::::::::::::::::::::::::::::::: ffdmmddpmdddfdmddmdppdpppppppppppppgghhfffhhfffffhffpfss :::::::::::::::::::::"
t0071=":::::::::::::::::::::::::::::::::::::   pfmmpfmddddfdddmmdddddppppppppppppghfffphfffffffpfssss  ::::::::::::::::::::"
t0072=":::::::::::::::::::::::::::::::::::::::   fffddddddmfffdmfddddppppppppppppghfhffffffffffsf sfss ::::::::::::::::::::"
t0073=":::::::::::::::::::::::::::::::::::::::::  ffpddmdpmmffffddfdmpdpppppphppghhfffffsfsss      sff  :   :::::::::::::::"
t0074=":::::::::::::::::::::::::::::::::::::::::: pdddddmmddddmmmddmmdddppppppppgpffffhhsf    :::  spfp   s :::::::::::::::"
t0075=":::::::::::::::::::::::::::::::::::::::::: fffmpmdddpdddmddmmdpmdpdppfpppghfffggfgf :::::::  fpp     :::::::::::::::"
t0076="::::::::::::::::::::::::::::::::::::::::::  pm sdmmmddmdmmmmddmdddddpffpphfffffs f  ::::::::  pf     :::::::::   :::"
t0077="::::::::::::::::::::::::::::::::::::::::::: dd   dmdmddmmmmmdmdddmddppppgpgp       ::::::::::  s   s ::::::    s :::"
t0078=":::::::::::::::::::::::::::::::::::::::::::  ps  mddmdddmdmmdmmmmmdddppppppp :::::::::::::::::       :::::  sj   :::"
t0079=":::::::::::::::::::::::::::::::::::::::::::: dd  sddmpdddmdmmmmmmddddpppgp   ::::::::::::::::::::    :::   hj  :::::"
t0080="::::::::::::::::::::::::::::::::::::::::::::  ddf ddddddddddmmmdmpdddpppg  :::::::::::::::::::     s     ppjs ::::::"
t0081=":::::::::::::::::::::::::::::::::::::::::::::  dd  ddmddjjpddmmmdddddpppd ::::::::::::::::::   hpgghgghs  pj  ::::::"
t0082=":::::::::::::::::::::::::::::::::::::::::::::  dp  jmdhdsddddmdddmddddppj :::::::::::::::::  sjsss j h   j   :::::::"
t0083="::::::::::::::::::::::::::::::::::::::::::::: jjdj   dhjsjmdmpddmdddddppp ::::::::::::::::: j       s  :   :::::::::"
t0084=":::::::::::::::::::::::::::::::::::::::::::::   spj   dssjsdmmdddmpdmddpp :::::::::::::::::   :::::    :::::::::::::"
t0085=":::::::::::::::::::::::::::::::::::::::::::::::   dj   dssssdmmddmdddpdps :::::::::::::::    :::::: ss :::::::::::::"
t0086="::::::::::::::::::::::::::::::::::::::::::::::::: dd   ddsssjdddmmddjpppj :::::::::::       :::::::    :::::::::::::"
t0087="::::::::::::::::::::::::::::::::::::::::::::::::: dps   jjsjsmddmddmdphpj :::::::::   hjj ::::::::::::::::::::::::::"
t0088=":::::::::::::::::::::::::::::::::::::::::::::::::  ps     sjjjpmmmmmdjjhh ::::::::: jjjj  ::::::::::::::::::::::::::"
t0089="::::::::::::::::::::::::::::::::::::::::::::::::::  jd ::  sjjjddmmdmdhpj ::::::::: jjjj :::::::::::::::::::::::::::"
t0090=":::::::::::::::::::::::::::::::::::::::::::::::::::  j :::  jjjjdmddpdhhd  :::::::  jjjj :::::::::::::::::::::::::::"
t0091="::::::::::::::::::::::::::::::::::::::::::::::::::::   :::: jjjdjpppdjjjjs  :::::: jjjjj :::::::::::::::::::::::::::"
t0092=":::::::::::::::::::::::::::::::::::::::::::::::::::::::::::  jssddpppdpjjjj :::    jjjj  :     :::::::::::::::::::::"
t0093=":::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: sssjsjdddppjph     jjjjjjj    jjj :::::::::::::::::::::"
t0094=":::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: jsssssjjjjjjpjjjsjmjjjjjjj  jjjjj :::::::::::::::::::::"
t0095=":::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: ssssjjjjjjjppjjjjjjsjjjjjjjhjjjjj :::::::::::::::::::::"
t0096="::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::    ssjhpjjpppjjjjshpjjjjjjjjhjjjj :::::::::::::::::::::"
t0097=":::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::    sjjjjjjmjsj jjjjjhhsjhpjjjj :::::::::::::::::::::"
t0098="::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::      jsss     jjjsjs jpjjj   ::::::::::::::::::::"
t0099=":::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::      :::          sjjjj ::::::::::::::::::::"
startpos_count=12
startpos={"x","y","exclude","nations"
60,51,FALSE,"Sioux"
36,63,FALSE,"German"
95,34,FALSE,"French"
95,54,FALSE,"English"
37,51,FALSE,"Portuguese"
96,23,FALSE,"Viking"
97,45,FALSE,"Dutch"
40,71,FALSE,"Scottish"
70,93,FALSE,"Aztec"
72,83,FALSE,"Spanish"
21,11,FALSE,"Russian"
79,75,FALSE,"Irish"
}
e00_0000="00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"
e00_0001="00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"
e00_0002="00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"
e00_0003="00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"
e00_0004="00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"
e00_0005="00000
```

## 策划参考价值
SLG历史场景/战役剧本的数据结构参考。
