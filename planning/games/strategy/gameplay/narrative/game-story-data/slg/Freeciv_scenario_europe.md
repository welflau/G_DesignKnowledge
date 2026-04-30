# 文明 · 历史场景「europe」

> 来源：longturn/freeciv21
> 原始链接：https://github.com/longturn/freeciv21
> 分类：gameplay
> 标签：文明, 4X策略SLG, 历史场景, 剧本
> 游戏类型：4X策略SLG

## 概述
Freeciv历史场景脚本：europe

## 正文
```sav

[scenario]
game_version=3000000
is_scenario=TRUE
name=_("Europe (classic/giant)")
authors=_("Map: Christian Grothoff, Jerzy Klek, Mateusz Stefek, Daniel Markstedt\nStart positions: Jason Dorje Short, Mateusz Stefek")
description=_("Overhead 177x100 map of Europe.")
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
random_seed=1586959453
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
"aifill",14,5
"alltemperate",FALSE,FALSE
"flatpoles",100,100
"generator","SCENARIO","RANDOM"
"landmass",45,30
"mapseed",0,0
"mapsize","FULLSIZE","FULLSIZE"
"maxplayers",37,150
"metamessage","Scenario: Europe",""
"revolentype","RANDOM","RANDOM"
"separatepoles",TRUE,TRUE
"singlepole",FALSE,FALSE
"size",18,4
"startpos","DEFAULT","DEFAULT"
"startunits","cccxxx","ccwwx"
"steepness",30,30
"teamplacement","CLOSEST","CLOSEST"
"techlevel",3,0
"temperature",50,50
"tilesperplayer",100,100
"tinyisles",FALSE,FALSE
"topology","","WRAPX|ISO"
"victories","","SPACERACE|ALLIED"
"wetness",50,50
"xsize",177,64
"ysize",100,64
}
set_count=26
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
have_huts=TRUE
have_resources=FALSE
t0000="aaag      ::::::::::::::::::::::::::::::::::::::::::::::::::::::      tttttttttttttt       ffffffffffffffffffftffffffffffffftfffffffffffffffffffffffffffffffffffffffffffmmmmaaaaa"
t0001="aag           :::::::::::::::::::::::::::::::::::::::::::::::        ttthmmtttffffff      ffffffffffffffffffffffffftttttffffffffftttttttttttttttttttttttttttttttttttthhhmmmmmmmmm"
t0002="gg               ::::::::::::::::::::::::::::::::::::::::::         pphmmmmhffffffff     ffffffffffffffffffffffffffffffffffffffffffffffffffffffffttttttttttfttttttffffhhmmmmmmmmf"
t0003="g                  ::::::::::::::::::::::::::::::::::::::         phhmmmmmmhfffffff    ffffffffffffffffffffffffffff++fffffffffffffffffffffffffffffffffffffffffffffffffhmmmmmmmmmf"
t0004="      p             :::::::::::::           :::::::::::            pppphmmmhffffff    ffffffffffffffffffffffffffffff++ffffffffffffffffffffffffffffffffffffffffffffffffhhmmmmmmmmf"
t0005="     pp    tp          ::::::::      p       ::::::::::          p   ppphmhfffffff   gffffff++ffffffffffffffffffffff++fffffffffffffffffffffffffffffffffffffffffffffffhhmmmmmmmmmf"
t0006="       gphpgpp           ::::         p        :::::::         p pppppphmhfffffff     ggfffff+fff+++fffffffffffff++f+fffffffffffffffffffffffffffffffffffffffffffffffhhhmmmmmmmmmh"
t0007="       pfmmphf                       pp        :::::::       ppppphhmmmmhffffffff     ggffffffffff+ffffffffffffff++++ffffffffffffffffffffffffffffffffffffffffffffffffhmmmmmmmmmhf"
t0008="      ggpfmaff                     p          ::::::        pphmmmmmmmmhhfffffff     gggg++fffffff+fffffg++ffffff++++fffffffffffffffffffffffffffffffffffffffffffffhhhhmmmmmmmmfff"
t0009="       pffhff     ff                         ::::            pppphmmmmmhhfffffff      gggg+ff+ffff+fffg++++++fffff+++fffffffffffffffffffffffffffffffffffffffffffffhhhhmmmmmmmmmhf"
t0010="::      pff                                 :::             phmmmmmmmhhhfffffffp      gggg+ff++gg++fffg++++++ffgggg++fffffffffffffffffffffffffffffffffffffffffffffffhhhmmmmmmmmhf"
t0011=":::::                                                      pphhmmmmmmhhhf fffffp       ggg+gg+fggggggfgg++++++ggggg++fffffffffffffffffffffffffffffffffffffffffffffhhhhhmmmmmhhmmf"
t0012=":::::::                                                     ppmmmmmmhmhffffffffpp     gggggffggggggggggg++++++fggggggffffffffffffffffffffffffffffffffffffffffffffffhhhhmmmmmhhmmf"
t0013=":::::::::::::                                              pppphhmmhppmhfffffffff     gggggggggggg  ggggg+++++ffgggggffffgfgffffffffffffffffffffffffffffffffffffffhhhmmmmmmmfffff"
t0014=":::::::::::::::                                               ppphmhpphfffffppfffp     ggggggggg      ggg+ggggffffgggffff++gfffffffffffffffffffffffffffffffffffffffhhhmmmmmmmmmmm"
t0015=":::::::::::::::                              p            pppppphmmhpphffffffppfppp     gggggg       gggggggggffffgggffff++ggggggggfffffffffffffffgggffppppppffffhhhhmmmmmmmmmmhh"
t0016="::::::::::::::::                            p              phhhmmmhppphffffffppppggg     g          gggggggfggfffgggggffgg+gggggggggfffffggfggggggggppppppppppffffhhhhmmmmmmmmmhh"
t0017=":::::::::::::::::                                          phmmmmhppppffffppfpp+++gg           gggg ggffgggfgggffggggggfgggggggggggggggggggggggggggppppppppppppffhhhhmmmmmmmmhmmm"
t0018="::::::::::::::::::                 pp    php               pphmmmphp pfffpppppppgggg        ggggggggggffgggggggffggghhgggggggfffggggggggggggggggggpppphhppppfppphhhhmmmmmmmmmmmhf"
t0019="::::::::::::::::::                 p   phmp                pppmmpppp pffp++pppffpgg      gg gggggf++ggfgggggggggggghhhhggggggggfgggggggggggggggggppppppphpphpfppffhhmmmmmmmmmmmhf"
t0020=":::::::::::::::::                 p   phmp                  pphppp   phpp++gpppfppg         ggggff++gggggggggggggghhhhhggggggggggggggggggggggggggppppppppppfhppppphhhmmmmmmmmmmhf"
t0021=":::::::::::::::::                    phmppppp               pphppp    pp+++fpppgg        gg  gggggg+fgggggf+gggggghhhhgggggggggggggggggggggppppppppppphppppffhpppphhhmmmmmmmmmhhh"
t0022="::::::::::::::::                    phmphhmhp               ppppp     gg++hpppfpp             ggggg+ggggggggggggggggghhggggggggggggggggggppppppppppppppppppppfhpphhhmmmmmmmmmmmmm"
t0023=":::::::::::::::                   p  pphhmpp                           g+gpp+pfpp    p    gg  gggggggggffggggggggggggggggggggfggggggggfpppppppppppppppphppppppffhhhhhmmmmmmmmmmmm"
t0024=":::::::::::::::                     pmhhhpp                        gg  ggpf++pffp  ppp   ggg   gggggggggffggggggggfgggggggggffgggggggffppppppppppppppppppppppppfppphhmmmmmmmmmmmh"
t0025="::::::::::::::                     phhphpp                        ggg  ggpp+pffpp  pp   ggggg  ggggggggggfgggggggfffgggggggggggggggggfppppppppppppppppphppppppppphphhhmmmmmmmmmmh"
t0026="::::::::::::::                       pppp                       gggg    gpppffffp  pp   ggggggggggggfggggggggggggggggggggggggggggggggppppppppppppppppphhhpppppphhpppphmmmmmmmmmmm"
t0027="::::::::::::::                        ppppp                    gggggg   gpfhpfpfp       ggpppggggggggggggggggggggggggggggggggggggpppppppppppppppppppppphppppppppppphhhmmmmmmmmmmh"
t0028="::::::::::::::                gggg   pphhppp                   ggggg  g gpfpffpfp       ggpppggggggggggggggggggggggggggggggggggpppppppppppppppppphpppppppphppppppppphhhmmmmmmmmmm"
t0029=":::::::::::::             gg ggggg  pphphhpp                   ggggg gg ggggpppp         ggggggggggggggpggggggggggggggggggggggpppppppppppppppppphpppppppphhppppppphhhmmmmmmmmmmmm"
t0030=":::::::::::::            ghggggggg     phppg                   ggggg gg  ggg             gggggpppppggggggggggggggggggfggggggpppppppppppppppppppphppppppphpppppppppphhhmmmmmmmmmhm"
t0031=":::::::::::             ghgggggggg    pphhgg                   gggg  ggg ggg             ggggfppppppggfggggggggggggggffggggppppppppppppppppppppppppppppppppppppppphhhhmmmhhhmmmmh"
t0032="::::::::                   gggggg      gghggg                   gg           g          ggggggpppppggggggggggggggggggggggggppppppppppppppppppppphpppppphppppppppppppphhhmhhhmmmhm"
t0033="::::                      ggggggg      gghggg                   ggg ggg                 gggggpppppgggggggggggggggggggggpppppppppppppppppppppppphhpppppphpppppppppppppphhmhhhmmmmh"
t0034=":                       ggggggghg   pggghhggg                  gggg      g     ggggg  ggggggggpppgggggfggggfgggggggggggpppppppppppppppppppppppphpppppphppppppppppppppphhhhhmmmhhm"
t0035="                      gphphgggggg  phmhphggg                   gggg  gggg    ggggg   ggggggggggggfgggffgggggggfggggggpppppppppppppppppppppppppppppppppppppppppppppppppppphmmmmhhm"
t0036=":                     phphgggggg    phhgggggg gg                 gggggggggggggghfggggggggfggggggggggggggggggggffggggppppppppppppppppppppppppphppppppppppppppppppppppdppppphmmhhmm"
t0037="::                     ghggg g     phhpggggggggg            gg ggggggfhfgggggghfgggggfgffpfpgfggggggfgggggggggfggggppppppppppppppppppppppppphpppppppppppppppdppppppdddddddhdddddh"
t0038=":::                              pphhhgggggggggg         ggggggggggggggfggggghfggggggggggggsggffpppfffgggffggggggffppppppppppppppppppppppppppppppppppppppppddpppppddddddddhdddddm"
t0039=":::                               ppgggggggggggg       g  ggggggggggggggggggggggggggggggggggggfggssssggggfggggggffpppppppppppppppppppppppppppppppppppppppppdddpppdddddddddddddddh"
t0040="::::                                 gggggggggg       gg  ggggggggsggggggggggggggggggggggggggggggsssfffggggggggggpppppppppppppppppppppppppppppppppppppdpppddddpppddddddddddmddddh"
t0041="::::                              p ggggggpgg         gg ggggggggggggggggggggggggggggggppggggggsssssfffgggggggggpppppppppppppppppppppppppppppppppppppddppdddddpppdddddddddddddddh"
t0042="::::                            phppppppppppgpp      gggggggggggggggggggggggggggggggggggggggggggggssffsgggggppppppppppppppppppppppppppppppppppppppppppdpddddddpppdddddddddddddddd"
t0043=":::::                         ppphphpppppppphpp    sggggggggggggggggggggggggggggpggggggggggggggggpppfggffppppppppppppppppppppppppppppppppppppppppppppdpppdddddpp    ddddddddddddd"
t0044=":::::                            pp       ppp     gggggggggggggggggghggggggfgggggggggggggggggpgppppppppphhpppppppppppppppppppppppppppppppppppppppppppppddpdpd       ddddddddddddp"
t0045=":::::                                          ggggggggggggggfffgggghggpgggfgggggggggghhggppphpppppppphhpppppppppppppppppppppppppppppppppppppppppppppppdppp           dddddddddpp"
t0046="::::::                                        gggggggggggggggfgggghgggpphhfhhhgpgpppppphhppppphpppppphpppppppppppppppppppppppppppppppppppppppppppppppppppp            dddddddddpp"
t0047=":::::::                               g       ggggghhgggggggggpppppppppfpppgghmmppppppppppppppphpppppppppppppppppppppppppppppppppppppppppppppppppppppppppp        d  dddddddddddp"
t0048=":::::::                               gg   ggggggggghhgggggggppppphppphhppppppphhppppppppppppppppppppppppppppppppppppppppppppppphppppppppppppppppppppppppp       ddd dddddddddddp"
t0049="::::::::                       gggg   ggggggggggggggfhhghggggggghhgppfhpppppppppphpppppphpphpppppppppppppppppppppppppppppppppppppphhhppppppppppdppppppppss      ddddddddddddddddd"
t0050=":::::::::                     gghhggggggggggggggggggghggfhggggghhhpppffhpppppppppppphpphhhhhhhhhfpppppppppppppppppppppppppppppppppphpppppppppppdddppppppp      dddddddddddddddddh"
t0051="::::::::::                     ggghggggggggggggggggggghgggggggppppppppfhhppppphpppphhhhmmmmmmmmmhhppppppppppppppppppppppppppppppphpp pppppppppppdppppppp        ddddddddddddddddd"
t0052="::::::::::::                     ggggggggggggggggggggggphggggppppppppppfhhfpphpppphhgphhmmhppgphhmhhppppppppppppppppppppppppppppppp  ppppppppppppddddpp    ::   dddddddddddddddpp"
t0053=":::::::::::::::                    gggggggggggggggggggpgggggpppppphppppppfhphphpgggggggpppggggggphmhhppppppppppppppppppppppppppppp  pppppppppppppppdppp    ::::   ddddddddddddddd"
t0054="::::::::::::::::::                 ggggggggggggggggggggggfggpphpphppppppppphppppgggggggggggggggggphmhhpppppppppppppppppppppppppp   pppppppppppppppppdppp    :::::   dd  ddddddddd"
t0055="::::::::::::::::::::                gggggggggggggggggggggfggpphppppppppppppppppppgggggggggggggghppphmhhpppppppppppppppppppppppp     pppppppppppppppppppp    ::::::  dd    ddddddd"
t0056="::::::::::::::::::::::              gggggggggggggggggggggggphppppppppppppphppppppgggggggggggggphhpphmmhpppppppppppppppppppppp       ppppppppppppppppppppp    ::::::  d    ddddddd"
t0057="::::::::::::::::::::::::             ggggggggggggggggggghgghphpphpphphpphhhmmmhhhggggggggggggghhhppphmmhpppppppppppp pp   pp       ppppppppppppppppppppppp   :::::::     dddddddd"
t0058="::::::::::::::::::::::::::          ggggggggggggggggggghmphhhhhhhphhphhhhmmmhppggggggggggggggphhhhppphmmhpppppppppp      pppp     pppppppppppppppppppppppp   :::::::  ddddddddddd"
t0059=":::::::::::::::::::::::::::::       gggggggggggggggggghmphhhhmmhmhhmhhmmmmmmmhhpgggggggggggggghhppppphhmhhppppppppp     pppppppp pppppppppppppppppppppppppp     :::::  dddddddddd"
t0060="::::::::::::          ::::::::       gggggghggggppppppphhhphmmmmmmmmhmmmmhhhpppgggggggggggggggpppphhhmmmhhppppppp       pppphp     ppppphhhppppppppppphhpppp    :::::  dd ddddddd"
t0061="::::::::::       pp     :::::::    gggggggggggggppppppph+hhmmmmhphmmmhphmmmhhhpgggggggggggggggpphhmmmmmhhppppppppp        php  :::   hhhhhhhhhhhhppphhhhhhpppp   ::::     ddddddd"
t0062=":::::::::     pppppppp      :::    ggggggggggghhphppppphhpmmhggggghphgggggmphhhgggggggggggggggphmmmmhpppppppppppgs   ::   pp  :::::   phhmmmmhhhhhhhhhhhhhhhhpp   :::::    dddddd"
t0063=":::::::::     pppphhhpppp    ::    fggggggggghhhhhhppppphhmmpggggggggggggghpphpgggggggggggggggghhhhppppppppppppgps   :::      ::::::   pphmmmmmmmmmmmmmhhmhmhhp    ::::    dddddd"
t0064="::::::::::     pppfhmmmhpppp  ::  ggggggggggphhhhhhpppphhmmhpgggggggggg   p pphpgggggggggggggghhppppppppppppgppp    :::::::::::::::::     phhmmmmmmmmmmmmmmmmhpp    ::::   dddddd"
t0065="::::::::::    ppphhhphmmmmhppp   gggggggggggphhhhhhppppphhmhggggggggggg   p  pphpppgggggggggghhggpppppppppgggppp   ::::::::::::::::::::    ppppphhmmmmmmmhhppppppp   ::    hhdddd"
t0066=":::::::::     gpppphpppphhmmhpppphmmhggggggghhhhhhppppphhmmhppphhgggggg       pphphpggggggggggggggppppgggggggppp   :::::::::::::::::::::    ppppppphhhhhhhhppppp   :::  ppphhhhdd"
t0067=":::::::::    gggppppppppppppmmphhmmmmhhgggggphhhpppppppphmmmhpppphhgggg       phphfhphhpgggggghgggggggggggggggpp   ::::::::::::::::::::::    pppppppppphhhhpppppp  :   ppphhmmmmm"
t0068="::::::::     gggppppppppphhhhhhppphhmmmhhpgppppppppppppphphmpp  pphhgggg      hphmhfhhphppggggghggggggggggggggp    ::::::::::::::::::::::::  ppppppppppphhhpppppp    ppphhmmmmmmm"
t0069="::::::::    ggggppppphmmhmmhmhhppppphhmmmhppppppppp ppppp pp     pphhmhhpp     pphhmhmhfhppggggpggggggggggghpp    ::::::::::       ::::::::  ppppppphhhpppppppppppppppphmmmmmdhhh"
t0070=":::::::     ggghhphhhhhppppphmhppppppphhmmmhpp       ppp         pppphmmhp      hphfhmmhfhfhgpphpggggggghmhppp   ::::::::::   pppp     ::   ppphhhhhhhhhhhhhhhhppphhhhmmmmmhddddd"
t0071="::::::      gggppppppppppppppmhpgppggpppphmmhh           :::      phpphmmhp       phhfmmhmhhpppmmhgghmmmmhppp    :::::::    pppppppppp    ppphmmhhhhhhhmmmhhhhhhhhhhhmmmhhddddddd"
t0072="::::::     ggggpppppppppppppphmhpggggggppppppp   ::::::::::  p    ppppphmhp        pphfmmhphhpphmmmmmhppppppppp   ::::    ppphmmhpppppppppphmmmmhhhmmhpphmmmmmmmmmmmmmhhddddddddd"
t0073="::::::    g
```

## 策划参考价值
SLG历史场景/战役剧本的数据结构参考。
