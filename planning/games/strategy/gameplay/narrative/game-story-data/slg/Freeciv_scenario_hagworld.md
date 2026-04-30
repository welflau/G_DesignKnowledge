# 文明 · 历史场景「hagworld」

> 来源：longturn/freeciv21
> 原始链接：https://github.com/longturn/freeciv21
> 分类：gameplay
> 标签：文明, 4X策略SLG, 历史场景, 剧本
> 游戏类型：4X策略SLG

## 概述
Freeciv历史场景脚本：hagworld

## 正文
```sav

[scenario]
game_version=3000000
is_scenario=TRUE
name=_("Earth (classic/medium)")
authors=_("Helge Arne Gudmestad, Daniel Markstedt")
description=_("Overhead 120x60 map of the Earth.")
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
level="Easy"
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
random_seed=1586959788
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
"flatpoles",100,100
"generator","SCENARIO","RANDOM"
"landmass",30,30
"mapseed",539221826,0
"mapsize","FULLSIZE","FULLSIZE"
"maxplayers",30,150
"metamessage","Scenario: Hagworld",""
"revolentype","RANDOM","RANDOM"
"sciencebox",50,100
"separatepoles",TRUE,TRUE
"singlepole",FALSE,FALSE
"size",7,4
"startpos","DEFAULT","DEFAULT"
"startunits","ccx","ccwwx"
"steepness",30,30
"teamplacement","CLOSEST","CLOSEST"
"techlevel",3,0
"temperature",50,50
"tilesperplayer",100,100
"tinyisles",FALSE,FALSE
"topology","WRAPX","WRAPX|ISO"
"turnblock",FALSE,TRUE
"victories","","SPACERACE|ALLIED"
"wetness",50,50
"xsize",120,64
"ysize",60,64
}
set_count=29
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
t0000="::::::::::::::::::::::::::::      :::::::           :::::::::::                                          :::::::::::::::"
t0001="::::::::::::::::::::::::::          ::::      a        :::::::    aa        aaa                              :::::::::::"
t0002=":::::::::::::::::::           aaaaa ::    aaaaaaaaa     ::::::   aa                                           ::::::::::"
t0003=":::::::::::::::::    aa a  m   mmm  :  aaaaaaaaaaaaaa    ::::   maa              a         aa    a        a       ::::::"
t0004="     ::::::::::    maa    a   aaa     aaaaaaaaaaaaaaa      :::                 aaa           tttt          a            "
t0005="           ::::       tt          aaa   ataaaaaaaaat     m ::::               g        ttttttttttt        tttt        t "
t0006="       ttt       t   ttt    tt ttmmmaaa   amaaaaattt      :::::   pht              t tttttttftttttttttmtttttttttt tttttt"
t0007="fft  ffftttttttttttttttttttttt tt  tta    tmaaata    m  ::::::   pffffft    tttttttt  tttmmmftttttttttmmtttttttttttmttff"
t0008="    fffmmmmmmmmmmttttttttttttt         ::  taa      pt         hmmf fff   ffffffmmttftttttttfttttttttttmmtttmmmmmfmmff  "
t0009=":    ffmfppfpfffmmmgffttttttt     tt   :::  pp  :::::     hp  phpf pffffffffffffmtttffttttttffttttttttttmmtttmmmf m   ::"
t0010="::    ppf      fffmmfpfffpfft     ttttf  ::    ::::       h      g  pp+ffffffffmmtftffftffffffffttttttttfff      m  ::::"
t0011=":    ff   :::   p mmmffffpfftttf  tptpff  :::::::::  :  pgfp   p   ppppppffffffmttfffffffffffffffffffffff       mm :::::"
t0012=" mmmm    ::::::: pffmmmppppffffff fffpffp   :::::::: :  g p  ggppfggppppppfffffffffffffffffhhhh+fffffffffff     m       "
t0013="      ::::::::::  ffmmffppffpfffffffff    f   ::::::::      gghmmhhhgpppppfpgggfffffffffffmmmdddpppppppfffff    ::  m  m"
t0014=":::::::::::::::::  ffmmfpfppff++f+fpppp  pf   :::::::::    gphfpgfgghg f ppp  dpppppp+ppppmmddddpdppppppp       ::::::::"
t0015="::::::::::::::::: fpffmpppppgggffpppf f     :::::::::::: pfhpg g  phg     gd ddppppppppppppddddddpppppppp  p  ::::::::::"
t0016=":::::::::::::::::: pffmhpppppppgppg    ::::::::::::::::: ppp    g ph ghhhhmm  ddmmdmmddmmmgdpdpdppfpggg   ph  ::::::::::"
t0017=":::::::::::::::::: fddmmhpppppppppg ::::::::::::::g:::::       pp  p dgghgmm  dddmmmmmdmhhhhghppphgg  g   h   ::::::::::"
t0018="::::::::::::::::::  dddmhpppppppgg  ::::::::::::::::::::  pppp          ggggggdddmmdmmmmmmmhhhppphgg    gfp  :::::::::::"
t0019="::::::::::::::::::: ppddhdpppsppj  ::::::::::::::::::::: phmmdddp  d   ppdgggfhhdmddhmmmmmmmhhfphggg   g    ::::::::::::"
t0020=":::::::::::::::::::: d dpppp    j  :::::::::::::::::::: pdmmdddppddpdgd dddd  ghhddddhhhmmmmmhpfpggg       :::::::::::::"
t0021="::::::::::::::::::::: h ddp  ::    ::::::::::::::::::: ppdddddddddddppd  dddd     pddppgjjjgmgpppgg     ::::::::::::::::"
t0022=":::::::::::::::::::::: d dj :: : g    ::::::::::::::: ppdddddddddddddpdd ddddddd   pggjgjjgjggggggg g ::::::::::::::::::"
t0023=":::::::::::::::::::::::  djj  j  gjjjg  ::::::::::::: pddddddmdddmddppdd  ddhdd     gpggg ggjggg      ::::::::::::::::::"
t0024=":::::j::::::::::::::::::   ppjj        g ::::::::::g: pdddmdddddddddpppdd  hdd      ppj    ggjj g : g ::::::::::::::::::"
t0025=":::::::m::::::::::::::::::    gj ::    j :::::::::::: pdddddddddddddppppdd    ::::   pp ::: gjjj :: g ::::::g:::::::::::"
t0026=":::::::::p:::::::::::::::::::  j   gpg   ::::::::::::: pppjpppjjpdpppdfphddpp  :::   pp ::: g  j ::  g :::::::::::j:::::"
t0027="::::::::::::::::::::::::::::::  ggjjjjpp    ::::::::::: pjpgjjjjpppppsddhppd :::::    p :::  g   :   g :::::::::::::::::"
t0028=":::::::::::::::::::::::::::::::   gjjgjjgjj  ::::::::::  g    gjggggphhhhpdd :::::   :  ::: gjj   g   ::::::::::::::::::"
t0029=":::::::::::::::::::::::::::::::: gjjjgggjjj    :::::::::: :::  jggjjjjgjggd :::::::  ::::::  jg gjj ::::::::::::::::::::"
t0030=":::::::::::::::::::::::::::::j   mjjjjjjjjggj   :::::::::::::: jjgjjjm++pg  ::::::: :::::::: gg jjg g   g    :::::::::::"
t0031=":::::::::::::::::::::::::::::::  mjjjjjjjjjgggjg::::::::::::::: jjggjmggp  :::::::: ::::::::: g          ggjg  g       :"
t0032=":::::::::::::::::::::::::::::::  mmjpppjjjjjjgjg :::::::::::::: jjggjgmpg :::::::: g ::::::::  gjg jjg    jgjj   j    ::"
t0033="::::::::::::::::::::::::::::::::  mjhfpgjjjjjggg ::::::::::::::  pppppmpg ::::::::: :::::::::::              g          "
t0034=" :::::::::::::::::::::::::::::::  mmmmppggjjggg  :::::::::::::: dddddpgggg  j :::::::::::::::::::::    jj  j  ::: :::   "
t0035=" :j::::::::::::::::::::::::::::::  mmmmhhjjjgjj  :::::::::::::: ddhhdpppg  gj :::::::::::::::::: :   ppjjp jj   ::      "
t0036=":::::::::::::g:g::::::::::::::::::   mmphjgggjg  :::::::::::::: dphpphhg  gh :::::::::::::::::::    ddddddppj     g     "
t0037=":::::::g::::::::::::::::::::::::::: mmmmhggjjg   ::::::::::::::  ppppppp  jg :g:::::::::::::::::   dddddddddpj     j  g "
t0038=":::::::::::::::g::::::::::::::::::: mmhhgpgg    :::::::::::::::  dpfdpp   h  :::::::::::::::::::  ddddddddddppp :::     "
t0039="::::::::::::::::::::::::::::::::::: mmhppppp    :::::::::::::::  pppppg      :::::::::::::::::::: dddddddddddgp ::      "
t0040="::::::::g:::::::::::::::::::::::::: mmppppp    ::::::::::::::::   phhp   :::::::::::::::::::::::  hhddd ppphmpg ::      "
t0041="        ::::::::::::::::::::::::::: pmfpp     ::::::::::::::::::  p  :  ::::::::  ::::::::::::::: pp      ggmp  ::: p   "
t0042="      ::::::::::::::::::::::::::::  mmppp    :::::::::::::::::::   :::::::::::      ::::::::::::           ppp ::::  gp "
t0043="     ::::::::::::::::g:::::::::::: pmpp      ::::::::::::::::::::::::::::::::::      :::::::::::::::::::::    ::::   p  "
t0044="     ::::::::::::::::::::::::::::: mmp      :::::::::::::::::::::::::::::::::::        :::::::::::::::::::: mp ::   mm  "
t0045="    :::::::::::::::::::::::::::::: pmp       ::::::::::::::::::::::::::::::::::          :::::::::::::::::: m  ::: mm   "
t0046="   ::::::::::::::::::::::::::::::: mm        ::::::::::::::::::::::::::::::::::::  mm   :::::::::::::::::::    ::: p    "
t0047="   ::::::::::::::::::::::::::::::: ppm  m        :::::::::::::::::::m::::::::::::::::::::::::::::::::::::::    :::      "
t0048="  ::::::::::::::::::::::::::::::::   mp        t  ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::      "
t0049=":::::::::::::::::::::::::::::::::::::::::::::    :::::::::::::::::::::::::::::::::::::              ::::::::::::::  ::::"
t0050="::::::::::::::::::::::::a:::::::::  aaa  :      ::::::::::::::::::::::::::::::: a       aaaaaaaaaa           :::::::::::"
t0051="::::::::::::::::::::::::a:         ama    :::::::::::::::::::::::::::::        aaaaaa aaaaaaaaaaaaaaaaaaa         ::::::"
t0052="::::::::::::::::          a       amma      ::::::::::::::   :           a aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa         ::"
t0053=":::::::::::         aa    aaaaaaaaamaa       :::::         a   aaaaaaaaaaaammaaaaaaaaaaaaaaammmaaaaaaaaaaaaaaaaaaa     :"
t0054="::::::         aaaaaaaaaaaaaaaaaaaama              aaaaaaaaaaaaaaaaaaaaaaamaaaaaaaaaaaaaaammmmmaaaaaaaaaaaaammaaaaaa    "
t0055="::::::   aaaaaaaaaaaaaaaaaaaaaaaaamaaaaaa       aaaaaaaaaaaaaaaaaaaaamaaaaaaaaaaaaaaaaaaaaammaaammaaaaaaaaaaamaaa       "
t0056="       a aaaaaaaaaaaaaaaaaaaaaaaammmaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaammaaaaaaaaammmamaaaaaamaaaaaaaaaaaammaaaaaa         "
t0057="   a     aaaaaaaaamaaaaaaaaaammaamamaaaaaaaaaaaaaaaamaaaaaaaaaaaaaaaaaaaaaaaaamaaaamaaaaaammaammaaamamaaaaaaaaaaaa      "
t0058="aaaaaaaaaaaaaammmmaaaaaaammmmaamammmmaaaaaaaaaaammmmaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaamamaaaaaaaaaaaaaaaaaaaaaaama"
t0059="aaaaaaaaaaaaaaaaaaaaaaaaaaaaaammmmmmmmaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
startpos_count=0
e00_0000="000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"
e00_0001="000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"
e00_0002="000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"
e00_0003="000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"
e00_0004="000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"
e00_0005="000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"
e00_0006="000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"
e00_0007="000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"
e00_0008="000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"
e00_0009="000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"
e00_0010="000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"
e00_0011="000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"
e00_0012="000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"
e00_0013="000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"
e00_0014="000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"
e00_0015="000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"
e00_0016="000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"
e00_0017="000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"
e00_0018="000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"
e00_0019="000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"
e00_0020="000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"
e00_0021="000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"
e00_0022="000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"
e00_0023="000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"
e00_0024="000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"
e00_0025="000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"
e00_0026="000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"
e00_0027="000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"
e00_0028="000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"
e00_0029="000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"
e00_0030="000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"
e00_0031="000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"
e00_0032="000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"
e00_0033="000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"
e00_0034="000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"
e00_0035="000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"
e00_0036="000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"
e00_0037="000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"
e00_0038="000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"
e00_0039="000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"
e00_0040="000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"
e00_0041="000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"
e00_0042="000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"
e00_0043="000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"
e00_0044="00000000000000000000
```

## 策划参考价值
SLG历史场景/战役剧本的数据结构参考。
