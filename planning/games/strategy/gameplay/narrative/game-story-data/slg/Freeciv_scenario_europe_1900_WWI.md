# 文明 · 历史场景「europe_1900_WWI」

> 来源：longturn/freeciv21
> 原始链接：https://github.com/longturn/freeciv21
> 分类：gameplay
> 标签：文明, 4X策略SLG, 历史场景, 剧本
> 游戏类型：4X策略SLG

## 概述
Freeciv历史场景脚本：europe_1900_WWI

## 正文
```sav

[scenario]
game_version=3000000
is_scenario=TRUE
name=_("Europe 1900")
authors=_("Ferdinand Steinkrüger (a.k.a. XYZ) and Jamie Troini (a.k.a. Nimrod).")
description=_("Europe 1900\n\nAn attempt at an historically accurate recreation of the Great Powers of Europe just prior to the outbreak of the First World War.\n\nWARNING: Each AI controlled player will spend a long time on its moves during turn change.\n\n(update: 28.07.2016) ")
save_random=FALSE
players=TRUE
startpos_nations=FALSE
lake_flooding=FALSE
ruleset_locked=TRUE

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
server_state="S_S_RUNNING"
meta_patches="none"
meta_server="meta.freeciv.org"
id="OmdZKaenCJnhdyaMdKk58e0ChxUphWxl"
serverid=""
level="Hard"
phase_mode="Concurrent"
phase_mode_stored="Concurrent"
phase=0
scoreturn=21
timeoutint=0
timeoutintinc=0
timeoutinc=0
timeoutincmult=1
timeoutcounter=1
turn=1
year=1900
year_0_hack=FALSE
globalwarming=0
heating=0
warminglevel=36
nuclearwinter=0
cooling=0
coolinglevel=36
random_seed=1586958551
global_advances="1011111111111101101111111101110000111110011111111110011110011011110110011001101111111111"
last_turn_change_time=0
save_players=TRUE
ai_types="classic"
save_known=TRUE

[random]
saved=FALSE

[script]
code=$$
vars=$$

[settings]
set={"name","value","gamestart"
"aifill",11,11
"airliftingstyle","",""
"allowtake","HAhadOo","HAhadOo"
"alltemperate",FALSE,FALSE
"animals",20,20
"aqueductloss",0,0
"autoattack",FALSE,FALSE
"autosaves","TURN|GAMEOVER|QUITIDLE|INTERRUPT","TURN|GAMEOVER|QUITIDLE|INTERRUPT"
"autotoggle",FALSE,FALSE
"barbarians","DISABLED","NORMAL"
"borders","ENABLED","ENABLED"
"caravan_bonus_style","CLASSIC","CLASSIC"
"citymindist",2,0
"citynames","PLAYER_UNIQUE","PLAYER_UNIQUE"
"civilwarsize",10,10
"conquercost",0,0
"contactturns",20,20
"demography","NASRLPEMOqrb","NASRLPEMOqrb"
"diplbulbcost",0,0
"diplchance",80,80
"diplgoldcost",0,0
"diplomacy","ALL","ALL"
"disasters",10,10
"dispersion",0,0
"ec_chat",TRUE,TRUE
"ec_info",FALSE,FALSE
"ec_max_size",256,256
"ec_turns",1,1
"endspaceship",TRUE,TRUE
"endturn",5000,5000
"first_timeout",-1,-1
"fixedlength",FALSE,FALSE
"flatpoles",100,100
"foggedborders",FALSE,FALSE
"fogofwar",TRUE,TRUE
"foodbox",100,100
"freecost",0,0
"fulltradesize",1,1
"gameseed",0,0
"generator","SCENARIO","SCENARIO"
"globalwarming",TRUE,TRUE
"globalwarming_percent",100,100
"gold",50,50
"happyborders","NATIONAL","NATIONAL"
"homecaughtunits",TRUE,TRUE
"huts",150,150
"kicktime",1800,1800
"killcitizen",TRUE,TRUE
"killstack",TRUE,TRUE
"killunhomed",0,0
"landmass",45,45
"mapseed",1694518854,1694518854
"mapsize","FULLSIZE","FULLSIZE"
"maxconnectionsperhost",4,4
"maxplayers",28,37
"mgr_distance",0,0
"mgr_foodneeded",TRUE,TRUE
"mgr_nationchance",50,50
"mgr_turninterval",5,5
"mgr_worldchance",10,10
"migration",FALSE,FALSE
"minplayers",1,1
"multiresearch",FALSE,FALSE
"nationset","all",""
"naturalcitynames",TRUE,TRUE
"nettimeout",10,10
"netwait",4,4
"notradesize",0,0
"nuclearwinter",TRUE,TRUE
"nuclearwinter_percent",100,100
"occupychance",0,0
"onsetbarbs",60,60
"phasemode","ALL","ALL"
"pingtime",20,20
"pingtimeout",60,60
"plrcolormode","PLR_ORDER","PLR_ORDER"
"rapturedelay",1,1
"razechance",20,20
"restrictinfra",FALSE,FALSE
"revealmap","",""
"revolen",2,5
"revolentype","FIXED","RANDOM"
"savepalace",TRUE,TRUE
"saveturns",1,1
"sciencebox",400,400
"scorefile","freeciv-score.log","freeciv-score.log"
"separatepoles",TRUE,TRUE
"shieldbox",100,100
"singlepole",FALSE,FALSE
"size",18,18
"specials",250,250
"startcity",FALSE,FALSE
"startpos","DEFAULT","DEFAULT"
"startunits","cccxxx","cccxxx"
"steepness",30,30
"team_pooled_research",TRUE,TRUE
"teamplacement","CLOSEST","CLOSEST"
"techleak",100,100
"techlevel",3,3
"techlossforgiveness",-1,-1
"techlossrestore",50,50
"techlost_donor",0,0
"techlost_recv",0,0
"techpenalty",100,100
"temperature",50,50
"tilesperplayer",100,100
"timeaddenemymove",0,0
"timeout",0,0
"tinyisles",FALSE,FALSE
"topology","",""
"trade_revenue_style","CLASSIC","CLASSIC"
"trademindist",9,9
"tradeworldrelpct",50,50
"trading_city",TRUE,TRUE
"trading_gold",TRUE,TRUE
"trading_tech",TRUE,TRUE
"traitdistribution","FIXED","FIXED"
"turnblock",FALSE,FALSE
"unitwaittime",0,0
"unreachableprotects",FALSE,TRUE
"victories","ALLIED","ALLIED"
"wetness",50,50
"xsize",177,177
"ysize",100,100
}
set_count=124
gamestart_valid=TRUE

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
have_huts=TRUE
have_resources=TRUE
t0000="aaag      ::::::::::::::::::::::::::::::::::::::::::::::::::::::      ttttttttttttttffffff ffffffffffffffffffftffffffffffffftffffffffffafffafafffafaaaafffafffafafafffafammmaaaaa"
t0001="aag           :::::::::::::::::::::::::::::::::::::::::::::::        ttthmmtttffffff      ffffffffffffffffffffffffftttttffffffffftttttttatatttatatttttatttaaffatataataahmamammmmm"
t0002="ag               ::::::::::::::::::::::::::::::::::::::::::         fphmmmmhfffffffg     ffffffffffffffffffffffffffffffffffffffffffffffffafffffafttttattttafafatatafafahmmammmmmf"
t0003="g                  ::::::::::::::::::::::::::::::::::::::         phhmmmmmmhfffffff    ffffffffffffffffffffffffffff++fffffffffffffffffffafaffffaffffafffffaffaafafafffammmammmmmf"
t0004="      p             :::::::::::::     p     :::::::::::            pppphmmmhffffff    ffffffffffffffffffffffffffffff++fffffffffffffffffafffafffaffffaaaaffafffafafafffahmmammmmmf"
t0005="     pp    tp          ::::::::      p       ::::::::::          p   ppphm+pffffff   gffffff++ffffffffffffffffffffff++fffffffffffffffffffffffffffffffffffffffffffffffhhmmmmmmmmmf"
t0006="       gphpgpp           ::::         p        :::::::         f ppfppphmhfffffff     ggfffff+fff+++fffffffffffff++f+fffffffffffffffffffffffffffffffffffffffffffffffhhhmmmmmmmmmh"
t0007="       pfmmphf                       pp        :::::::       ppppphhmmmmhfffffffg     ggffffffffff+ffffffffffffff++++ffffffffffffffffffffffffffffffffffffffffffffffffhmmmmmmmmmhf"
t0008=":     ggpfmaff                        p       ::::::        pphmmmmmmmmhhfffffff     gggg++fffffff+fffffg++ffffff++++fffffffffffffffffffffffffffffffffffffffffffffhhhhmmmmmmmmfff"
t0009=":    pppffhff                                ::::            ppfphmmmmmhhfffffff      fggg+ff+ffff+fffg++++++fffff+++fffffffffffffffffffffffffffffffffffffffffffffhhhhmmmmmmmmmhf"
t0010=":       pff                                 :::             phmmmmmmmhhhfffffffp      gggg+ff++gg++fffg++++++ffgggg++fffffffffffffffffffffffffffffffffffffffffffffffhhhmmmmmmmmhf"
t0011="::                                                         pphhmmmmmmhhhf fffffp       ggg+gg+fggggggfgg++++++ggggg++fffffffffffffffffffffffffffffffffffffffffffffhhhhhmmmmmhhmmf"
t0012="::                     p                                    ppmmmmmmhmhffffffffpp     fggggffggggggggggg++++++fggggggffffffffffffffffffffffffffffffffffffffffffffffhhhhmmmmmhhmmf"
t0013=":::::::::::::           hp                                 fppfhhmmhppmhfffffffff     gggggggggfgg  ggggg+++++ffgggggffffgfgffffffffffffffffffffffffffffffffffffffhhhmmmmmmmfffff"
t0014=":::::::::::::::         h                                     ppphmhpphfffffppfffp     gfggggggf      ggg+ggggffffgggffff++gfffffffffffffffffffffffffffffffffffffffhhhmmmmmmmmmmm"
t0015=":::::::::::::::                              p            pfpppphmmhpphffffffppfppp  g  gfggfg       gggggggggffffgggffff++ggggggggfffffffffffffffgggffppppppffffhhhhmmmmmmmmmmhh"
t0016="::::::::::::::::        h                   p h            phhhmmmhppphffffffppppggg     g          gggggggfggfffgggggffgg+gggggggggfffffggfggggggggppppppppppffffhhhhmmmmmmmmmhh"
t0017=":::::::::::::::::                            h             phmmmmhppppffffppfpp+++gg           gfgg ggffgggfgggffggggggfgggggggggggggggggggggggggggppppppppppppffhhhhmmmmmmmmhmmm"
t0018="::::::::::::::::::                 pp    php               pphmmmphp pfffpppppppgggg        ggfgggggggffgggggggffggghhgggggggfffggggggggggggggggggpppphhppppfppphhhhmmmmmmmmmmmhf"
t0019=" :::::::::::::::::                 p   phmp                ppfmmffpp pffp++pppffpgg      ggggggggf++ggfgggggggggggghhhhggggggggfgggggggggggggggggppppppphpphpfppffhhmmmmmmmmmmmhf"
t0020="  :::::::::::::::::               p   fmmp                  pphpfp   phpp++g+ppfppg      ggfggggff++gggggggggggggghhhhhggggggggggggggggggfgggggggppppppppppfhppppphhhmmmmmmmmmmhf"
t0021="   ::::::::::::::::                  phhppppp               pphpfp    pp+++f+ppgg        gg  gggggg+fgggggf+gggggghhhhgggggggggggggggggggggppppppppppphppppffhpppphhhmmmmmmmmmhhh"
t0022="a   :::::::::::::::                 phmphfmhp               pfppp     gg++hp+pfpp   gp        ggggg+ggggggggggggggggghhggggggggggggggggggppppfpppppppppfpfpppfhpphhhmmmmmmmmmmmmm"
t0023="a   :::::::::::::::               p  pphhmfp                           g+gpp+pfpp   fg    gg  ggfggggggffggggggggggggggggggggfggggggggfpppppffppppfpppphppppppffhhhhhmmmmmmmmmmmm"
t0024="a      ::::::::::::                 pmhhhfp                        gg  ggpfpppffp   pp   ggg   ggggggghhffggggggggfgggggggggffgggggggffppppppppppppppppppppppppfppphhmmmmmmmmmmmh"
t0025="aa      :::::::::::                phhphpp                        ggf  ggppppffpp p p   gfggg  gggggggghhfgggggggfffgggggggggggggggggfppppppppppppppppphppppppppphphhhmmmmmmmmmmh"
t0026="aaa       :::::::::                  pppp                       gggg    gpppffffp g     ggggfggggfggfggghhgggggggggggggggggggggggggggppppppppppppppppphhhpppppphhpppphmmmmmmmmmmm"
t0027="aaaa t     ::::::::       ggg         ppppp                    gggggg  ggpfhpfpfp f     ggpppggggggggggggggggggggggggggggggggggggpppppppppppppppppppppphppppppppppphhhmmmmmmmmmmh"
t0028="aatfghht    :::::::       ggg gggg   pphhpppp                  g+ggg    gpffffpfp p     ggpppgggfggggggggggggggggggggggggggggggpppppppppppppppppphpppppppphppppppppphhhmmmmmmmmmm"
t0029="gfgatf+hg    ::::::      ggggggf+g  pfhphfppp                  ggggg gg gggfpppp         gfggggggggggggpggggggggggggggggggggggpppppppppppppppppphpppppppphhppppppphhhmmmmmmmmmmmm"
t0030="agftsafft     :::::      fhggfgggp     phppgg                  ggggg  g  gfg             gggggpppppggggggggggggggggggfggggggpppppppppppppppppppphppppppphpppppppppphhhmmmmmmmmmhm"
t0031="ttff+ffff f    ::::       gggggggg  h pphhgggp                 gggg g  g fgg             ggggfppppppggfggggggggggggggffggggppppppppppppppppppppppppppppppppppppppphhhhmmmhhhmmmmh"
t0032="+ffftftft hg    :::      gggggggg      gghggg                   gg  g g      g          ggggggpppppggggggggggggggggggggggggppppppppppppppppppppphpppppphppppppppppppphhhmhhhmmmhm"
t0033="fftsfgfsf hffp   ::       ggggggg      gggggg              h+   ggg                     gggggpppppgggggggggggggggggggggpppppppppppppppppppppppphhpppppphpppppppppppppphhmhhhmmmmh"
t0034="gfffftfff  ffgg   ::    gggfggghg   pggghhggg                  gg+g  g   g     ggggg  gggggfggpppgggggfggggfgggggggggggpppppppppppppppppppppppphpfpppphppppppppppppppphhhhhmmmhhm"
t0035="fft+ffs      f    ::     phgggggg  phmhphggg                   g+gggg+gfg    ggggg   ggggggggggggfgggffgggggggfggggggppppppppfppppppppppppppppppppppppppppppppppppppppppphmmmmhhm"
t0036="ffffgf  g  g      :::   phgggggg    phhgggggg gg                ggggggggggggggghfggggggggfggggggggggggggggggggffggggppppppppppppppppppppppppphppppppppppppppppppppppdppppphmmhhmm"
t0037="fgfff             ::::    gg g     pphpggggggggg            gg g+ggggfhfgggggghfgggggfgffpfpgfggggggfgggggggggfggggppppppppppppppppppppppppphpppppppppppppppdppppppdddddddhdddddh"
t0038="gpggf fh          :::::          pphhhgggggggfgg         ggggg+gg+gggggfggggghfggggggggggggsggffpppfffgggffggggggffpppppppppppppppfppppppppppppppppppppppppddpppppddddddddhdddddm"
t0039="ffffg+gg   f      :::::           ppgggggggggggg       g  gggg+gggggggggggggggggggggggggggggggfggssssggggfggggggffpppppppppppppppppppppppppppppppppppppppppdddpppdddddddddddddddh"
t0040="fpff+phg    g    :::::::             fggggggggg       gg  ggggggggsfggfgggggggfggggggggggggggggggsssfffggggggggggppppppppppppfppppppppppppppppppppppppdpppddddpppddddddddddmddddh"
t0041="fggfg+fhp gfg    :::::::          p ggggggpg+++       gg ggggggggfggggggggggggggggfggggppgfggggsssssfffgggggggggpppppppppppppppppppppppppppppppppppppddppdddddpppdddddddddddddddh"
t0042="g++gg+hhgff      ::::::::       phpppppppppggpp     gggggggggggggggggggggfggggggggggggggggggggggggssffsgggggppppppppppppppppppppppppppppppppppppppppppdpddddddpppdddddddddddddddd"
t0043="hfp++gggg f     :::::::::     ppphphpppppfpphpp    +gggghghgggggggggggggggggggggpggggfgggggggggggpppfggffppppppppppppppppppppppppppppppppppppppppppppdpppdddddpp    ddddddddddddd"
t0044="gg+ffghgg       ::::::::::       pp       ppf     gg+gfggggggggggggghggggggfgggggggggggggggggpgppppppppphhppppppppppppppppppppppppppppppppp+pppppppppppddpdpd       ddddddddddddd"
t0045="++ffsgpff       ::::::::::                     gggggggggggfggfffgggghggpgggfgggggggggghhggppphpppppppphhppppppppppppppppppppppppppppppppppp+pppppppppppdppp        dd+ddddddddddd"
t0046="+fhgghg        ::::::::::::                   ggggggggggggggghgggghgggpphhfhhhgpgpppppphhppfpphppfppphppppppppppppppppppppppppppppppppppppp+pppppppppppppp         d++ddddddddddd"
t0047="fgpgggg       :::::::::::::         h h       gghgghhggfhggggfpppppppppfpppgghmmpfppppppppppppphpppppppppppppppppppppppppppppppppppppppppppppppppppppppppp        dd+dddddddddddd"
t0048="gghhgfgf     :::::::::::::            gg   ggggggggghhgggggggfpppphppphhpfppppphhppppppppppppfpppppppppppppppppppppppppppppppppphppppppppppppppppppppppppp       ddd+dddddddddddd"
t0049="gggggg       :::::::::::::     gggg   gggfggggggfgggghhghggggggfhhgppfhpppppppppphpppppphpphpppppppppppppppppppppppppppppppppppppphhhppppppppppdppppppppss      ddddddddddddddddd"
t0050="hhfpggg      ::::::::::::::   hghhggggggggggggggggggghggfhggggghhhpppffhpppppppppppphpphfhhhhhhhfpppppppppppppppppppppppppppppppppphpppppppppppdddppppppp      dddddddddddddddddh"
t0051="hfg         ::::::::::::::::   ggghggggggggggggggggggghgggggggppppppppfhhppfpphpppphhhhmmmmmmmmmhhppppppppppppppppppppppppppppppphpp pppppppppppdppppppp        ddddddddddddddddd"
t0052="sggpg       :::::::::::::::      gfgggggggggggfggggggggphggggppppfpppppfhhfpphpfpphhgphhmmhpfgfhhmhhppppppppppppppppppppppppppppppp  ppppppppppppddddpp    ::   ddddddddddddddddd"
t0053="hggf       :::::::::::::::::       ghgggggggggggggggggggggggpfpppphppppppfhphfhpggggggfpppggggfgphmhhppppppppppppppppppppppppppppp  pppppppppppppppdppp    ::::   ddddddddddddddd"
t0054="pf f      ::::::::::::::::::       gggggggfggggggggggggggfggpphfphppppppppphpppfggggfggggggggggggphmhhfppppppppppppppppppppppppp   pppppppppppppppppdppp    :::::   dd  ddddddddd"
t0055="g f      ::::::::::::::::::::       gggggggggggggpfggggggfggpphpppfppppppppfpppppgggggggggggggghpffhmfhpppppppppppppppppppppppp     pppppppppppppppppppp    ::::::  dd    ddddddd"
t0056="gg p     :::::::::::::::::::::      ggghgggggggggggggggggggphfppppppppffpphpppffpgggggggggfgggpfhpphmmfpppppppppppppppppppppp       ppppppppppppppppppppp    ::::::  d    ddddddd"
t0057="gf gf   :::::::::::::::::::::::      ggggggggggggggggggghgghphp+++phphpphhhmmmhhhggggggggggggghhhppphmmhpfppppppppppp     pp       ppppppppppppppppppppppp   :::::::  d  dddddddd"
t0058=" p f    ::::::::::::::::::::::      ggggggggggggggggggghmphhhhfhhphhphhhhmmmhfpggggggggggggggpfhhhppphmmfpppppppppp p    pppp     pppppppppppppppppppppppp   :::::::  ddddddddddd"
t0059="       :::::::::::::::::::::::      ggggggggggggggfggghmpfhhhmmhmhhmhhm
```

## 策划参考价值
SLG历史场景/战役剧本的数据结构参考。
