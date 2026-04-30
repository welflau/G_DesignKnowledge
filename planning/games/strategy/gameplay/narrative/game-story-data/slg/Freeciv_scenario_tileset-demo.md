# 文明 · 历史场景「tileset-demo」

> 来源：longturn/freeciv21
> 原始链接：https://github.com/longturn/freeciv21
> 分类：gameplay
> 标签：文明, 4X策略SLG, 历史场景, 剧本
> 游戏类型：4X策略SLG

## 概述
Freeciv历史场景脚本：tileset-demo

## 正文
```sav

[scenario]
game_version=3000000
is_scenario=TRUE
name=_("Tileset Demo")
authors=_("Daniel Markstedt")
description=_("Map for demonstrating square tilesets. Not intended for playing.")
save_random=TRUE
players=TRUE
startpos_nations=FALSE
lake_flooding=TRUE
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
meta_server="http://meta.freeciv.org/metaserver.php"
id="qzkLhy8fRw3PM1JHcr-FdRvplR-aYc3m"
serverid=""
level="Easy"
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
year=-4000
year_0_hack=FALSE
globalwarming=0
heating=0
warminglevel=9
nuclearwinter=0
cooling=0
coolinglevel=9
global_advances="1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111"
last_turn_change_time=0
save_players=TRUE
ai_types="classic"
save_known=TRUE

[random]
saved=TRUE
index_J=20
index_K=51
index_X=19
table0="773174db 249eee8f 1edf4acb 24519c23 9579075b 36d365fb 6a0344aa"
table1="ea6eeccb e94d435f 2cc533b2  cb82662   4ec097    2ab7d f074a41f"
table2="f5d28c64 37d761a7 23240ec1 99491383 153bba85 91b6b685 50c139f9"
table3="43d984ce 32ed055b b9b728eb ee861c38 98a9e59d 2f8ef951 e394155b"
table4="d6289f86  2f37d84 6743d908 ce32d1f4 8c9e2bbf 5389e6e1 73dc1881"
table5="61ee8cfd 5841dc62 36390b9c e20432de cf117102  d63f478  88ebfb5"
table6="4c55fa3d a79b4233 1b558149 4a7fac9c 95dd9fcd 31497d97 8674b4b5"
table7="be28cdbc d6ef3f33 82d92962  29ee6b1  6a472f0 da5a67ed  a6629c4"

[script]
code=$$
vars=$$

[settings]
set={"name","value","gamestart"
"aifill",5,5
"airliftingstyle","",""
"allowtake","HAhadOo","HAhadOo"
"alltemperate",FALSE,FALSE
"animals",20,20
"aqueductloss",0,0
"autoattack",FALSE,FALSE
"autosaves","TURN|GAMEOVER|QUITIDLE|INTERRUPT","TURN|GAMEOVER|QUITIDLE|INTERRUPT"
"autotoggle",FALSE,FALSE
"barbarians","NORMAL","NORMAL"
"borders","ENABLED","ENABLED"
"caravan_bonus_style","CLASSIC","CLASSIC"
"citymindist",2,2
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
"gameseed",1289525694,1289525694
"generator","SCENARIO","RANDOM"
"globalwarming",TRUE,TRUE
"globalwarming_percent",100,100
"gold",50,50
"happyborders","NATIONAL","NATIONAL"
"homecaughtunits",TRUE,TRUE
"huts",15,15
"kicktime",1800,1800
"killcitizen",FALSE,FALSE
"killstack",TRUE,TRUE
"killunhomed",0,0
"landmass",30,30
"mapseed",108745078,108745078
"mapsize","FULLSIZE","FULLSIZE"
"maxconnectionsperhost",4,4
"maxplayers",5,126
"metamessage","Scenario: Tileset Demo",""
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
"revolen",5,5
"revolentype","RANDOM","RANDOM"
"savename","freeciv","freeciv"
"savepalace",TRUE,TRUE
"saveturns",1,1
"sciencebox",100,100
"scorefile","freeciv-score.log","freeciv-score.log"
"scorelog",FALSE,FALSE
"separatepoles",TRUE,TRUE
"shieldbox",100,100
"singlepole",FALSE,FALSE
"size",4,4
"specials",250,250
"startcity",FALSE,FALSE
"startpos","DEFAULT","DEFAULT"
"startunits","ccwwx","ccwwx"
"steepness",30,30
"team_pooled_research",TRUE,TRUE
"teamplacement","CLOSEST","CLOSEST"
"techleak",100,100
"techlevel",0,0
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
"topology","WRAPX","WRAPX"
"trade_revenue_style","CLASSIC","CLASSIC"
"trademindist",9,9
"tradeworldrelpct",50,50
"trading_city",TRUE,TRUE
"trading_gold",TRUE,TRUE
"trading_tech",TRUE,TRUE
"traitdistribution","FIXED","FIXED"
"turnblock",TRUE,TRUE
"unitwaittime",0,0
"unreachableprotects",TRUE,TRUE
"victories","SPACERACE|ALLIED","SPACERACE|ALLIED"
"wetness",50,50
"xsize",78,78
"ysize",52,52
}
set_count=127
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
have_huts=FALSE
have_resources=TRUE
t0000="aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
t0001="     f  fff  f t   tts  f  f   s  s tf t  t         t   f s  f    t   t       "
t0002="                                                                              "
t0003="                                                                           :: "
t0004="          :::::::::::::::::::             :                                :: "
t0005=" fmmmpps :::::::::::::::::::::   fgmmmp       ff      p        pgpppmmpg   :  "
t0006=" fmhhps  :::::::::::::::::::::  gfhphhf       fhg    pgp           sffgg      "
t0007=" fhmhs   :::::::::::::::::::::  pfmpphhf      fp    gpgpp           fgppp     "
t0008=" pmmp    ::   ::::::::::::::::   fhmfphmgg           pmgf             sfffp   "
t0009="  ggs   ::        :::::::::::::   gphhfhmgf  ::      pff               ghhhp  "
t0010="        ::   pps   :::::::::::::   ghmphhpf  ::::::          p   ::::  ghhmps "
t0011="           pgpmhg  :::::::  :::::  pfmggmgp  ::::::::::     ss  :::::   gmhfp "
t0012="           gghphf  ::::::    ::::  sfhhphfs  ::::::::::::   pm  ::::::   ffgs "
t0013="    fsssss sgghmg  ::::::    ::::   gphghff   ::::::::::::  ff  :::::::   gss "
t0014="   sfsgpfs  fgmhf  ::::::   ::::::   pphphp    :::     :::   g  :::::::     s "
t0015="    fsffgg  ffggs  ::::::::::::::::   phmhhp           ::::    :::::::::    s "
t0016="    fgfffpssffpg   :::::::::::::::::   phmhmg     fppf  ::::  :::::::::::  sss"
t0017="   sddmhhmgddddp   :::::::::::::::::   gdmhhhdf  pdddf  :::::::::::::::::  gmg"
t0018="fspdddhppmhdddds  ::::::::::::::::::    dphhhdppdfffd   ::::::::::::::::   pps"
t0019="fpdddhhhhddhhmpg  :::::::::::::::::     gdddddpgffhfg  :::::::    ::::     p  "
t0020=" gddddddmhhdphhpg  ::::   ::::::::   ff gggff  gffffj   ::                    "
t0021=" ppgggfpfmhgmghhg  :::::  :::::::: sfffffpg    gffffj       gss   pggsf   ::  "
t0022="  ppfssfjhhpfgphpp ::::::::::::::: pfmpfg      pfffpj    pffpggtppgmmff  :::: "
t0023="   g   gjhhhphhhp  ::::::::::::::  jjss        pfhfpj   pgffftttthhmmff  :::: "
t0024="        jfmghhpp   :::        :::             gjghhfj   fffffttttthhfg  ::::::"
t0025=":       sggghpp    ::          ::::::    :   spffhfg     gffmfttthhhp    :::::"
t0026=":        sgjjjp         ppsp   :::::::        fffppg     pfmfffthhhhht    ::::"
t0027="         spgjgg        pgpgfg  ::::             pff       ffffff+hhhttt      :"
t0028="    g     ppggpf      pphhhgp   ::                    :   fmfff+++htttttpgp   "
t0029="  sjjp   sgghmhgs   gffhhfhhps     jssg  ff          :::  mmmf+++++ptttgpgp   "
t0030=" pphjg    fgpmhgpfsspfhmhffhgs   ggghmgfps    :::::::::: mmmmmj+++pppt  ppgp  "
t0031="ggdddp    fjddddddffddhhmfhhdjjjgddhdhhd     ::::::::::::gmmmjjj+ppppp  fgdggg"
t0032="dgps        sdddddg  fggdddddddpdfhhmmdp   :::::::::::::gggmjjjjjsppp   fdmhmd"
t0033="p             pss       pggpdddddhhhhp    :::::::::::::gggggdjjjsssp     dmmhd"
t0034="s  ::::::::                 gdgmhdhdg    :::::::::::::::gggdddjsssss     fhdmd"
t0035="  ::::::::::       :::  ::  sfhfhgpg    :::::::::::::::::gdddddasss      fhhhf"
t0036="  ::::::::::::::::::::::::  sfhffghg   ::::::::::::::::::::dddaaas       fmmfs"
t0037="  :::::::    :::::::::::::  gmhhgpmg  ::::::::::::::::::::::daaaaa       fgff "
t0038="  :::::       ::::::::::::  gmhppphp       :::::::::::::::::::aaa:      sss   "
t0039="   :::   sss     :::    :   pghhhmmp        :::::::::::::::::::a::::::  sgg   "
t0040="    ::  sgggf     :          gghmmpp pffffp ::::::::::::::::::::::::::  ssp   "
t0041="     :  fpffffpg     fp        pffgpgspgmhg  :::::::::::::::::::::::::  ggg   "
t0042="gff     fpghggfg    gpps            pfphhhgs  :::::::::::::::     :::   fffppg"
t0043="mhhf    gfggppf     sgpps          sffggppp   :::::::::::::            gfmhhhh"
t0044="ffhs     gfffg      sgfff    ::::  sffppss   :::::::::::::   pgspp    ffhhppgh"
t0045="ffhf      pgp        gphfg  :::::  sfmgg     ::::::::::::   gpgppffpgfffhhmpmh"
t0046="mmm             ::   pgmmf ::::::   gppg    :::::::::::::  gmmmgffffpffmmhmmmm"
t0047="                :::        ::::::            ::::::::::::                     "
t0048="                ::         :::::                                              "
t0049="                                                                              "
t0050=" tf   f     ff       ff       t  s   t  t  t   t   t     tf  ff s t       t   "
t0051="aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
startpos_count=5
startpos={"x","y","exclude","nations"
18,31,FALSE,""
31,35,FALSE,""
35,6,FALSE,""
12,15,FALSE,""
60,23,FALSE,""
}
e00_0000="000000000000000000000000000000000000000000000000000000000000000000000000000000"
e00_0001="000000000000000000000000000000000000000000000000000000000000000000000000000000"
e00_0002="000000000000000000000000000000000000000000000000000000000000000000000000000000"
e00_0003="000000000000000000000000000000000000000000000000000000000000000000000000000000"
e00_0004="000000000000000000000000000000000000000000000000000000000000000000000000000000"
e00_0005="000000000000000000000000000000000000000000000000000000000000000000000000000000"
e00_0006="000000000000000000000000000000000000000000000000000000000000000000000000000000"
e00_0007="000000000000000000000000000000000000000000000000000000000000000000000000000000"
e00_0008="000000000000000000000000000000000000000000000000000000000000000000000000000000"
e00_0009="000000000000000000000000000000000000000000000000000000000000000000000000000000"
e00_0010="000000000000000000000000000000000000000000000000000000000000000000000000000000"
e00_0011="000000000000000000000000000000000000000000000000000000000000000000000000000000"
e00_0012="000000000000000000000000000000000000000000000000000000000000000000000000000000"
e00_0013="000000000000000000000000000000000000000000000000000000000000000000000000000000"
e00_0014="000000000000000000000000000000000000000000000000000000000000000000000000000000"
e00_0015="000000000000000000000000000000000000000000000000000000000000000000000000000000"
e00_0016="000000000000000000000000000000000000000000000000000000000000000000000000000000"
e00_0017="000000000000000000000000000000000000000000000000000000000000000000000000000000"
e00_0018="000000000000000000000000000000000000000000000000000000000000000000000000000000"
e00_0019="000000000000000000000000000000000000000000000000000000000000000000000000000000"
e00_0020="000000000000000000000000000000000000000000000000000000000000000000000000000000"
e00_0021="000000000000000000000000000000000000000000000000000000000000000000000000000000"
e00_0022="000000000000000000000000000000000000000000000000000000000000000000000000000000"
e00_0023="000000000000000000000000000000000000000000000000000000000000000000000000000000"
e00_0024="000000000000000000000000000000000000000000000000000000000000000000000000000000"
e00_0025="000000000000000000000000000000000000000000000000000000000000000002000000000000"
e00_0026="000000000000000000000000000000000000000000000000000000000000000000000000000000"
e00_0027="000000000000000000000000000000000000000000000000000000000000000000000000000000"
e00_0028="000000000000000000000000000000000000000000000000000000000000000000001000000000"
e00_0029="000000000000000000000000000000000000000000000000000000000000000000011000000000"
e00_0030="000000000000000000000000000000000000000000000000000000000000000000011000000000"
e00_0031="000000000000000000000000000000000000000000000000000000000000000001111000000000"
e00_0032="000000000000000000000000000000000000000000000000000000000110000000110000000000"
e00_0033="000000000000000000000000000000000000000000000000000000011111000000000000000000"
e00_0034="000000000000000000000000000000000000000000000000000000001100000000000000000000"
e00_0035="000000000000000000000000000000000000000000000000000000000000000000000000000000"
e00_0036="000000000000000000000000000000000000000000000000000000000000400000000000000000"
e00_0037="000000000000000000000000000000000000000000000000000000000000000000000000000000"
e00_0038="000000000000000000000000000000000000000000000000000000000000000000000000000000"
e00_0039="000000000000000000000000000000000000000000000000000000000000000000000000000000"
e00_0040="000000000000000000000000000000000000000000000000000000000000000000000000000000"
e00_0041="000000000000000000000000000000000000000000000000000000000000000000000000000000"
e00_0042="000000000000000000000000000000000000000000000000000000000000000000000000000000"
e00_0043="000000000000000000000000000000000000000000000000000000000000000000000000000000"
e00_0044="000000000000000000000000000000000000000000000000000000000000000000000000000000"
e00_0045="000000000000000000000000000000000000000000000000000000000000000000000000000000"
e00_0046="000000000000000000000000000000000000000000000000000000000000000000000000000000"
e00_0047="000000000000000000000000000000000000000000000000000000000000000000000000000000"
e00_0048="000000000000000000000000000000000000000000000000000000000000000000000000000000"
e00_0049="000000000000000000000000000000000000000000000000000000000000000000000000000000"
e00_0050="000000000000000000000000000000000000000000000000000000000000000000000000000000"
e00_0051="000000000000000000000000000000000000000000000000000000000000000000000000000000"
e01_0000="000000000000000000000000000000000000000000000000000000000000000000000000000000"
e01_0001="000000000000000000000000000000000000000000000000000000000000000000000000000000"
e01_0002="000000000000000000000000000000000000000000000000000000000000000000000000000000"
e01_0003="000000000000000000000000000000000000000000000000000000000000000000000000000000"
e01_0004="000000000000000000000000000000000000000000000000000000000000000000000000000000"
e01_0005="000000000000000000000000000000000000000000000000000000000000000000000000000000"
e01_0006="000000000000000000000000000000000000000000000000000000000000000000000000000000"
e01_0007="000000000000000000000000000000000000000000000000000000000000000000000000000000"
e01_0008="000000000000000000000000000000000000000000000000000000000000000000000000000000"
e01_0009="000000000000000000000000000000000000000000000000000000000000000000000000000000"
e01_0010="000000000000000000000000000000000000000000000000000000000000000000000000000000"
e01_0011="000000000000000000000000000000000000000000000000000000000000000000000000000000"
e01_0012="000000000000000000000000000000000000000000000000000000000000000000000000000000"
e01_0013="000000000000000000000000000000000000000000000000000000000
```

## 策划参考价值
SLG历史场景/战役剧本的数据结构参考。
