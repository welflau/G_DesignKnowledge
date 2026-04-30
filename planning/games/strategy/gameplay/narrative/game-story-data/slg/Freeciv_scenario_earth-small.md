# 文明 · 历史场景「earth-small」

> 来源：longturn/freeciv21
> 原始链接：https://github.com/longturn/freeciv21
> 分类：gameplay
> 标签：文明, 4X策略SLG, 历史场景, 剧本
> 游戏类型：4X策略SLG

## 概述
Freeciv历史场景脚本：earth-small

## 正文
```sav

[scenario]
game_version=3000000
is_scenario=TRUE
name=_("Earth (classic/small)")
authors=_("Map: Daniel Gudlat, Daniel Markstedt\nStart positions: Jason Dorje Short, Mateusz Stefek, David Fernandez")
description=_("Overhead 80x50 map of the Earth.")
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
random_seed=1586958390
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
"aifill",10,10
"alltemperate",FALSE,FALSE
"flatpoles",100,100
"generator","SCENARIO","SCENARIO"
"landmass",30,30
"mapseed",0,0
"mapsize","FULLSIZE","FULLSIZE"
"maxplayers",39,39
"metamessage","Scenario: Earth(Small)",""
"revolentype","RANDOM","RANDOM"
"separatepoles",TRUE,TRUE
"singlepole",FALSE,FALSE
"size",4,4
"startpos","DEFAULT","DEFAULT"
"steepness",30,30
"teamplacement","CLOSEST","CLOSEST"
"temperature",50,50
"tilesperplayer",100,100
"tinyisles",FALSE,FALSE
"topology","WRAPX","WRAPX"
"victories","",""
"wetness",50,50
"xsize",80,80
"ysize",50,50
}
set_count=24
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
have_resources=FALSE
t0000="aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
t0001="    a  aa       a  aa   a  aaa  a  a    aaaa    aa   aaa   a   a a   a  a    a  "
t0002=":::                                  ::      ::    :     :   :     :      ::   :"
t0003="::::           a   aaaaaa     :::::   ::::::::    :::  :::::::::::::::::::::::::"
t0004="::::        t aa  aaaaaaaa     :::  tt  ::::   at :: t     ::::::  :::::::::::::"
t0005="::     t  t tta  aaaaaaaaaa     :::      :::  t    :   ttt  :::  t :::::::::::::"
t0006=":  tt    p t     taaaaaaaaa                  p  tt    tpttt              ::    :"
t0007="     ttt     ta    ttaaaatt           ptptt     pt ttttfft ttt  ttttt           "
t0008="  tt      tt  ta    ttaatt           phfgppt ttffptgftfffffgggfffffpptttt   ttt "
t0009="tttptptttttp   pa    tatt  tt   h   ghf  fp pffhffpgfffffffppfffgfffffgpptt  ttp"
t0010="tpfffptptt      pa   ttt      g g  fgg  gfffffhfgfgffffgffffpffffpffffffp   tptt"
t0011="pfffffffptp           t      g  g    g    g+fgggfhfggsffgfffffffffffffg  f   ppt"
t0012="pgpfpfffffpptp tp       :::    gg  g   gffgggfhffffggfpffgggffffg    fh     p   "
t0013="   gfffffffppttpff  ::::::::::     gppgffgfgppfhgffgffgfffgppppg       hp     ::"
t0014="::  phfggffffpgfffp  :::::::::  gggggpfffggppppppgpppppfppgpdppppg p g    ::::::"
t0015="::  gfhggppp++ffff p :::::::   hgggmhgppf ppp gp ddgpppppdddpgppg  p   :::::::::"
t0016=":: fgghhgpppgg+ggf  :::::::: gpph  h  ppg   g ppdppppgpppddpgpgg  gh  ::::::::::"
t0017=":: gghmppgggggfgg  ::::::::: pppg   g gp pgpg  pppgpppppgppg  g  pm  :::::::::::"
t0018=":: fghphpggggghg  :::::::g::       gg g gfpppppppghhppggpppg g  pm  ::::::::::::"
t0019="::  gpppggpgghg   :::::::::   gpgg       ppppppphhhhhhggpppp    g  :::::::::::::"
t0020=":::  gpddpgggg   p :::::::  pgpddppg gggpppdp  phmmmmhhpppppg     ::::::::::::::"
t0021=":::: ggddpg  g    :::::::: ppddddddppppp  dddd  gghhmhhgppgg     :::::::::::::::"
t0022=":::: p gdg   s     ::::::: pdddppddddppdp  pddpd pggggggpgg    :::::::::::::h:::"
t0023=":::: p  gg f   ppg  :::::: pddppppppddppdd  pd    gfg  gg       :::::::::::::g::"
t0024="::::     gpg     gg :::::: ggpppppppdppppdp    :: hg   jp g  g :::g:::::::::::::"
t0025="::::::::   pg        :::::  pgpggppgppgppddpd ::: ph    s    j  ::::::::::::::::"
t0026="::::::::::  gp gggg  ::::::   fjf fgfgfmmpdp  :::   p      g  p :::::    :::::::"
t0027=":::::::::::   ggfjgg  :::::::     gjjjfhmpp  ::::::  : g  jf           j  ::::::"
t0028=":::::::::::: ghhjjjfg    :::::::: ggjjjh+gg :::::::::: pf pg  j gfj       ::::::"
t0029=":::::::::::: ghhjjjjfffg  :::::::  ggjjjgg  ::::::::::  g        fgp     :::::::"
t0030=":::::::::::: ghfffjjfffgg :::::::: gpfggfg   ::::::::::  pgg              ::::::"
t0031="::::::::::::  ghfjffffggp :::::::: gppgghg g ::::::::::::     gg  g    g  ::::::"
t0032=":::::::::::::  gmgffggpg  :::::::: ppgpgf  f :::::::::::::   ppgggg       ::::::"
t0033="::::::::::::::  pdgggpgg ::::::::: dpppgf gg ::::::::::::   pddppgf    p   :::::"
t0034="::::::::::::::  ghpgpff  ::::::::: dpddpg p  :::::::::::: pddpdddppf       :::::"
t0035="::::::::::::::  pmppgf  ::::::::::  pppg    ::::::::::::: gpdddpdpppg       ::::"
t0036="::::::::::::::  gmmggg  :::::::::::  gg  ::::::::::::::::  gpdppggpg  :     ::::"
t0037="::::::::::::::  hgggg   ::::::::::::    :::::::::::::::::: pg   ggg  ::  g :::::"
t0038="::::::::::::::  mdggg   ::::::::::::::::::::::::::::::::::          ::: hg :::::"
t0039=":::::::::::::: pgppg   :::::::::::::::::::::::::::::::::::::::::: f :: ph    :::"
t0040=":::::::::::::: gppg   :::::::::::::::::::::::::::::::::::::::::::  ::: g    ::::"
t0041=":::::::::::::: gpg   ::::::::::::::::::::::::::::::::::::::::::::::::::    :::::"
t0042=":::::::::::::: pp  g ::::::::::::::::::::::::::::::::::::::::::::::::::   ::::::"
t0043="::::::::::::::  pf   :::::::::::::::::::::::::::::::::::::::::::::::::: ::::::::"
t0044=":::::::::::::::     ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::"
t0045=":::::::::::::::     ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::"
t0046="::::::::::::::::  t :::::::::::::::::::::::    :::::::                ::::::::::"
t0047="                 t   :::::::::::::          tt         aatttaaaaaaaa      ::::::"
t0048=" aaataaatattaaataa                 aaaaaattaaataa  aaaaaaaaaaaaaaaaataata       "
t0049="aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
startpos_count=50
startpos={"x","y","exclude","nations"
15,18,FALSE,"American"
33,19,FALSE,"Carthaginian#Numidian#Algerian"
40,25,FALSE,"Ethiopian"
53,20,FALSE,"Tibetan"
49,14,FALSE,"Hunnic#Kazakh"
9,23,FALSE,"Mexican#Aztec"
19,35,FALSE,"Paraguayan#Guarani"
30,24,FALSE,"Songhai#Mali#Malian"
44,19,FALSE,"Iraqi#Babylonian#Sumerian"
39,13,FALSE,"Slavic#Polish"
10,11,FALSE,"Inuit"
32,12,FALSE,"English#Briton#British"
38,18,FALSE,"Greek#Hellenic"
35,12,FALSE,"Danish"
73,37,FALSE,"New Zealand#Maori"
36,29,FALSE,"Kongo#Congolese"
29,17,FALSE,"Celtiberian#Portuguese"
46,18,FALSE,"Persian#Iranian"
15,39,FALSE,"Mapuche#Chilean"
57,30,FALSE,"Indonesian"
43,12,FALSE,"Russian#Soviet"
62,13,FALSE,"Manchu"
66,36,FALSE,"Australian#Australian Aboriginal"
56,24,FALSE,"Thai#Cambodian#Khmer"
36,17,FALSE,"Roman#Italian"
41,17,FALSE,"Hittite#Byzantine#Turkish"
39,34,FALSE,"Zulu#South African"
10,15,FALSE,"Sioux"
56,12,FALSE,"Xiongnu#Mongol"
31,16,FALSE,"Spanish#Iberian"
15,15,FALSE,"Canadian#Iroquois"
19,38,FALSE,"Argentine"
17,32,FALSE,"Bolivian#Aymara"
43,22,FALSE,"Saudi#Arab"
67,29,FALSE,"Papuan#Polynesian"
21,32,FALSE,"Tupi#Brazilian"
36,10,FALSE,"Viking#Norwegian#Swedish"
17,26,FALSE,"Venezuelan#Taino"
59,17,FALSE,"Han#Chinese"
62,17,FALSE,"Korean"
38,21,FALSE,"Egyptian Arab#Egyptian"
15,31,FALSE,"Peruvian#Inca"
7,19,FALSE,"Apache"
50,10,FALSE,"Tatar#Siberian"
13,19,FALSE,"Cherokee"
50,21,FALSE,"Indian"
67,16,FALSE,"Japanese"
34,14,FALSE,"Dutch#French#Celtic"
11,24,FALSE,"Mayan#Central American"
37,14,FALSE,"Austrian#Germanic#German"
}
e00_0000="00000000000000000000000000000000000000000000000000000000000000000000000000000000"
e00_0001="00000000000000000000000000000000000000000000000000000000000000000000000000000000"
e00_0002="00000000000000000000000000000000000000000000000000000000000000000000000000000000"
e00_0003="00000000000000000000000000000000000000000000000000000000000000000000000000000000"
e00_0004="00000000000000000000000000000000000000000000000000000000000000000000000000000000"
e00_0005="00000000000000000000000000000000000000000000000000000000000000000000000000000000"
e00_0006="00000000000000000000000000000000000000000000000000000000000000000000000000000000"
e00_0007="00000000000000000000000000000000000000000000000000000000000000000000000000000000"
e00_0008="00000000000000000000000000000000000000000000000000000000000000000000000000000000"
e00_0009="00000000000000000000000000000000000000000000000000000000000000000000000000000000"
e00_0010="00000000000000000000000000000000000000000000000000000000000000000000000000000000"
e00_0011="00000000000000000000000000000000000000000000000000000000000000000000000000000000"
e00_0012="00000000000000000000000000000000000000000000000000000000000000000000000000000000"
e00_0013="00000000000000000000000000000000000000000000000000000000000000000000000000000000"
e00_0014="00000000000000000000000000000000000000000000000000000000000000000000000000000000"
e00_0015="00000000000000000000000000000000000000000000000000000000000000000000000000000000"
e00_0016="00000000000000000000000000000000000000000000000000000000000000000000000000000000"
e00_0017="00000000000000000000000000000000000000000000000000000000000000000000000000000000"
e00_0018="00000000000000000000000000000000000000000000000000000000000000000000000000000000"
e00_0019="00000000000000000000000000000000000000000000000000000000000000000000000000000000"
e00_0020="00000000000000000000000000000000000000000000000000000000000000000000000000000000"
e00_0021="00000000000000000000000000000000000000000000000000000000000000000000000000000000"
e00_0022="00000000000000000000000000000000000000000000000000000000000000000000000000000000"
e00_0023="00000000000000000000000000000000000000000000000000000000000000000000000000000000"
e00_0024="00000000000000000000000000000000000000000000000000000000000000000000000000000000"
e00_0025="00000000000000000000000000000000000000000000000000000000000000000000000000000000"
e00_0026="00000000000000000000000000000000000000000000000000000000000000000000000000000000"
e00_0027="00000000000000000000000000000000000000000000000000000000000000000000000000000000"
e00_0028="00000000000000000000000000000000000000000000000000000000000000000000000000000000"
e00_0029="00000000000000000000000000000000000000000000000000000000000000000000000000000000"
e00_0030="00000000000000000000000000000000000000000000000000000000000000000000000000000000"
e00_0031="00000000000000000000000000000000000000000000000000000000000000000000000000000000"
e00_0032="00000000000000000000000000000000000000000000000000000000000000000000000000000000"
e00_0033="00000000000000000000000000000000000000000000000000000000000000000000000000000000"
e00_0034="00000000000000000000000000000000000000000000000000000000000000000000000000000000"
e00_0035="00000000000000000000000000000000000000000000000000000000000000000000000000000000"
e00_0036="00000000000000000000000000000000000000000000000000000000000000000000000000000000"
e00_0037="00000000000000000000000000000000000000000000000000000000000000000000000000000000"
e00_0038="00000000000000000000000000000000000000000000000000000000000000000000000000000000"
e00_0039="00000000000000000000000000000000000000000000000000000000000000000000000000000000"
e00_0040="00000000000000000000000000000000000000000000000000000000000000000000000000000000"
e00_0041="00000000000000000000000000000000000000000000000000000000000000000000000000000000"
e00_0042="00000000000000000000000000000000000000000000000000000000000000000000000000000000"
e00_0043="00000000000000000000000000000000000000000000000000000000000000000000000000000000"
e00_0044="00000000000000000000000000000000000000000000000000000000000000000000000000000000"
e00_0045="00000000000000000000000000000000000000000000000000000000000000000000000000000000"
e00_0046="00000000000000000000000000000000000000000000000000000000000000000000000000000000"
e00_0047="00000000000000000000000000000000000000000000000000000000000000000000000000000000"
e00_0048="00000000000000000000000000000000000000000000000000000000000000000000000000000000"
e00_0049="00000000000000000000000000000000000000000000000000000000000000000000000000000000"
e01_0000="00000000000000000000000000000000000000000000000000000000000000000000000000000000"
e01_0001="00000000000000000000000000000000000000000000000000000000000000000000000000000000"
e01_0002="00000000000000000000000000000000000000000000000000000000000000000000000000000000"
e01_0003="00000000000000000000000000000000000000000000000000000000000000000000000000000000"
e01_0004="00000000000000000000000000000000000000000000000000000000000000000000000000000000"
e01_0005="00000000000000000000000000000000000000000000000000000000000000000000000000000000"
e01_0006="00000000000000000000000000000000000000000000000000000000000000000000000000000000"
e01_0007="00000000000000000000000000000000000000000000000000000000000000000000000000000000"
e01_0008="00000000000000000000000000000000000000000000000000000000000000000000000000000000"
e01_0009="00000000000000000000000000000000000000000000000000000000000000000000000000000000"
e01_0010="00000000000000000000000000000000000000000000000000000000000000000000000000000000"
e01_0011="00000000000000000000000000000000000000000000000000000000000000000000000000000000"
e01_0012="00000000000000000000000000000000000000000000000000000000000000000000000000000000"
e01_0013="00000000000000000000000000000000000000000000000000000000000000000000000000000000"
e01_0014="00000000000000000000000000000000000000000000000000000000000000000000000000000000"
e01_0015="00000000000000000000000000000000000000000000000000000000000000000000000000000000"
e01_0016="00000000000000000000000000000000000000000000000000000000000000000000000000000000"
e01_0017="00000000000000000000000000000000000000000000000000000000000000000000000000000000"
e01_0018="00000000000000000000000000000000000000000000000000000000000000000000000000000000"
e01_0019="00000000000000000000000000000000000000000000000000000000000000000000000000000000"
e01_0020="00000000000000000000000000000000000000000000000000000000000000000000000000000000"
e01_0021="00000000000000000000000000000000000000000000000000000000000000000000000000000000"
e01_0022="00000000000000000000000000000000000000000000000000000000000000000000000000000000"
e01_0023="00000000000000000000000000000000000000000000000000000000000000000000000000000000"
e01_0024="00000000000000000000000000000000000000000000000000000000000000000000000000000000"
e01_0025="00000000000000000000000000000000000000000000000000000000000000000000000000000000"
e01_0026="00000000000000000000000000000000000000000000000000000000000000000000000000000000"
e01_0027="00000000000000000000000000000000000000000000000000000000000000000000000000000000"
e01_0028="00000000000000000000000000000000000000000000000000000000000000000000000000000000"
e01_0029="00000000000000000000000000000000000000000000000000000000000000000000000000000000"
e01_0030="00000000000000000000000000000000000000000000000000000000000000000000000000000000"
e01_0031="00000000000000000000000000000000000000000000000000000000000000000000000000000000"
e01_0032="00000000000000000000000000000000000000000000000000000000000000000000000000000000"
e01_0033="0000000000000000000000000000
```

## 策划参考价值
SLG历史场景/战役剧本的数据结构参考。
