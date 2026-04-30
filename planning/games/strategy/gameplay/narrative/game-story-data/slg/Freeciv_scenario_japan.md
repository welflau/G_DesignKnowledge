# 文明 · 历史场景「japan」

> 来源：longturn/freeciv21
> 原始链接：https://github.com/longturn/freeciv21
> 分类：gameplay
> 标签：文明, 4X策略SLG, 历史场景, 剧本
> 游戏类型：4X策略SLG

## 概述
Freeciv历史场景脚本：japan

## 正文
```sav

[scenario]
game_version=3000000
is_scenario=TRUE
name=_("Japan (classic/medium)")
authors=_("Robert Michael Best")
description=_("Overhead 88x100 map of Japan (Mercator projection).")
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
random_seed=1586960184
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
"aifill",8,5
"alltemperate",FALSE,FALSE
"borders","DISABLED","ENABLED"
"civilwarsize",6,10
"diplbulbcost",100,0
"diplgoldcost",100,0
"flatpoles",100,100
"generator","SCENARIO","RANDOM"
"happyborders","DISABLED","NATIONAL"
"huts",3,15
"landmass",25,30
"mapseed",0,0
"mapsize","FULLSIZE","FULLSIZE"
"maxplayers",8,150
"metamessage","Scenario: Japan",""
"revolentype","RANDOM","RANDOM"
"savepalace",FALSE,TRUE
"sciencebox",50,100
"separatepoles",TRUE,TRUE
"singlepole",FALSE,FALSE
"size",9,4
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
"xsize",88,64
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
t0000="::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::    "
t0001=":::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: ff "
t0002="::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::   f  "
t0003=":::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::  ffs :"
t0004="::::::::::::::::::::::::::::::::::::::::::::::::::::::::::   :::::::::::::::::::: fff  :"
t0005="::::::::::::::::::::::::::::::::::::::::::::::::::::::     s  ::::::::::::::::::  f   ::"
t0006=":::::::::::::::::::::::::::::::::::::::::::::::::::::: f  fgf  ::::::::::::::::: ff ::::"
t0007="::::::::::::::::::::::::::::::::::::::::::::::::::::::    gfff  :::::::::::::::: h  ::::"
t0008="::::::::::::::::::::::::::::::::::::::::::::::::::::::::: fgfff ::::::::::::::   s :::::"
t0009=":::::::::::::::::::::::::::::::::::::::::::::::::::::::::  ggff   ::::::::::   f   :::::"
t0010=":::::::::::::::::::::::::::::::::::::::::::::::::::::::::: ffghhf  ::::::    phf :::::::"
t0011=":::::::::::::::::::::::::::::::::::::::::::::::::::::::::: ffffhff   :::  f fff  :::::::"
t0012=":::::::::::::::::::::::::::::::::::::::::::::::::::::::::: fhhgmhfgf     sf ff    ::::::"
t0013=":::::::::::::::::::::::::::::::::::::::::::::::::::::::::: fhhfhmhhgffg sh  f   f ::::::"
t0014=":::::::::::::::::::::::::::::::::::::::::::::::::::::::::: fhhfhhmhfhggfhhf    f  ::::::"
t0015=":::::::::::::::::::::::::::::::::::::::::::::::::::::::::  fhhfhhmmhffh+mfgs     :::::::"
t0016="::::::::::::::::::::::::::::::::::::::::::::::::::::::::: fhffhhmmmhhhhfffggff :::::::::"
t0017="::::::::::::::::::::::::::::::::::::::::::::::::::::::::: fffffmmmmhhmmhggggs  :::::::::"
t0018=":::::::::::::::::::::::::::::::::::::::::::::::::::::     sgffhmhmfhhhhfgfg   ::::::::::"
t0019="::::::::::::::::::::::::::::::::::::::::::::::::::::: hff ffffmhhhfhfff     ::::::::::::"
t0020="::::::::::::::::::::::::::::::::::::::::::::::::::::: smfhfffhhmhggggg  ::::::::::::::::"
t0021="::::::::::::::::::::::::::::::::::::::::::::::::::::  phmhhfgfghmhffg  :::::::::::::::::"
t0022=":::::::::::::::::::::::::::::::::::::::::::::::::::  ffhhmffggfhmmfff ::::::::::::::::::"
t0023="::::::::::::::::::::::::::::::::::::::::::::::::::: pmf fhf   ffhhmf  ::::::::::::::::::"
t0024="::::::::::::::::::::::::::::::::::::::::::::::::::   fs  f  :   ffhf :::::::::::::::::::"
t0025=":::::::::::::::::::::::::::::::::::::::::::::::::: sfff    ::::   ff :::::::::::::::::::"
t0026="::::::::::::::::::::::::::::::::::::::::::::::::::   fhff   :::::    :::::::::::::::::::"
t0027="::::::::::::::::::::::::::::::::::::::::::::::::::::  hhfhf ::::::::::::::::::::::::::::"
t0028="::::::::::::::::::::::::::::::::::::::::::::::::::::  hf    ::::::::::::::::::::::::::::"
t0029=":::::::::::::::::::::::::::::::::::::::::::::::::::: fhf     :::::::::::::::::::::::::::"
t0030="::::::::::::::::::::::::::::::::::::::::::::::::::::  f  sfs :::::::::::::::::::::::::::"
t0031=":::::::::::::::::::::::::::::::::::::::::::::::::::::     ff :::::::::::::::::::::::::::"
t0032=":::::::::::::::::::::::::::::::::::::::::::::::::::::: ff  p :::::::::::::::::::::::::::"
t0033=":::::::::::::::::::::::::::::::::::::::::::::::::::::  gfghf  ::::::::::::::::::::::::::"
t0034="::::::::::::::::::::::::::::::::::::::::::::::::::::  sgffmfg ::::::::::::::::::::::::::"
t0035=":::::::::::::::::::::::::::::::::::::::::::::::::::: fhhhhhfg   ::::::::::::::::::::::::"
t0036="::::::::::::::::::::::::::::::::::::::::::::::::::::  fmhhmhhhf ::::::::::::::::::::::::"
t0037="::::::::::::::::::::::::::::::::::::::::::::::::::::: gffhmhhhf  :::::::::::::::::::::::"
t0038="::::::::::::::::::::::::::::::::::::::::::::::::::::  ggfhhhhmhf :::::::::::::::::::::::"
t0039=":::::::::::::::::::::::::::::::::::::::::::::::::::: fgfhmmhmmhf :::::::::::::::::::::::"
t0040="::::::::::::::::::::::::::::::::::::::::::::::::::::   ffhmhhmhf  ::::::::::::::::::::::"
t0041=":::::::::::::::::::::::::::::::::::::::::::::::::::::: ffhhhhhhfs ::::::::::::::::::::::"
t0042=":::::::::::::::::::::::::::::::::::::::::::::::::::::: ffhhffmmf  ::::::::::::::::::::::"
t0043=":::::::::::::::::::::::::::::::::::::::::::::::::::::  hhhmffhhf :::::::::::::::::::::::"
t0044="::::::::::::::::::::::::::::::::::::::::::::::::::::: pmhhmfghf  :::::::::::::::::::::::"
t0045="::::::::::::::::::::::::::::::::::::::::::::::::::::: fffmhffff ::::::::::::::::::::::::"
t0046="::::::::::::::::::::::::::::::::::::::::::::::::::::  fhhhhfggf ::::::::::::::::::::::::"
t0047=":::::::::::::::::::::::::::::::::::::::::::::::::::: hhmhhhfggf ::::::::::::::::::::::::"
t0048=":::::::::::::::::::::::::::::::::::::::::::::::::::: mmmhhhffpf ::::::::::::::::::::::::"
t0049="::::::::::::::::::::::::::::::::::::::::::::::   ::  mmmhmhg    ::::::::::::::::::::::::"
t0050=":::::::::::::::::::::::::::::::::::::::::::::: s    shhhmmgg :::::::::::::::::::::::::::"
t0051=":::::::::::::::::::::::::::::::::::::::::::::: ff  ffmmmmhgg  ::::::::::::::::::::::::::"
t0052=":::::::::::::::::::::::::::::::::::::::::::::: f  gffhmmmfhff ::::::::::::::::::::::::::"
t0053="::::::::::::::::::::::::::::::::::::::::::::::   sfffhhhhfhhf ::::::::::::::::::::::::::"
t0054="::::::::::::::::::::::::::::::::::::::::    :::  gfhmmmmmhmhf ::::::::::::::::::::::::::"
t0055=":::::::::::::::::::::::::::::::::::::::  ff ::  ffhmhmmmmhmhf ::::::::::::::::::::::::::"
t0056="::::::::::::::::::::::::::::::::::::::: ff  :  fhfhmmmmmhhmfg ::::::::::::::::::::::::::"
t0057="::::::::::::::::::::::::::::::::::::::: ff    fmmhmmmmfhhmgf  ::::::::::::::::::::::::::"
t0058="::::::::::::::::::::::::::::::::::::::: ff sfhmhhmmmmhffhhf  :::::::::::::::::::::::::::"
t0059="::::::::::::::::::::::::::::::::::::::  hfffhmmhmmmhmhffmmf ::::::::::::::::::::::::::::"
t0060=":::::::::::::::::::::::::::::::::::::: shfghmmhhmmhhffffffg ::::::::::::::::::::::::::::"
t0061=":::::::::::::::::::::    ::::::::::::  fhhhmmmhhmmhhfffffhg  :::::::::::::::::::::::::::"
t0062=":::::::::::::::::::::  f :::::::::::  fhmmhmmmmmmmmfffgggggs :::::::::::::::::::::::::::"
t0063="::::::::::::::::::::: f  ::::::::::: gfhmmhmmmmmmmmhfgggggfs  ::::::::::::::::::::::::::"
t0064=":::::::::::::::::::::   :::::::::::: fhmmmmmmmmmmmmmhgggggggf ::::::::::::::::::::::::::"
t0065="::::::::::::::::::::::::::::         phhhfhmmmmmmmmmffgf gs   ::::::::::::::::::::::::::"
t0066="::::::::::::::::::::         ffgfsf gghhghffhmmmhmmmhfg ghs ::::::::::::::::::::::::::::"
t0067=":::::::::::::::::::: fg fffffhfgffffh+ggggfhmmmmhffhf   gff ::::::::::::::::::::::::::::"
t0068="::::::::::::::::::   fhfhhhhhmhhfhhmf+ffggfhmhhhfffhg : g   ::::::::::::::::::::::::::::"
t0069=":::::::::::::::::  ffmmmmmmmhhhffhhfgghfggghhffhf  ff :   ::::::::::::::::::::::::::::::"
t0070="::::::::::::::::  ffhmmhmhffffhffhffgfhf ggfffffg  hs ::::::::::::::::::::::::::::::::::"
t0071=":::   :::::::::  fmmhhhhffgfgffggffgffhf f  fggf   f   :::::::::::::::::::::::::::::::::"
t0072="::: f ::::::::  fmhhhhhhffgf    gs ghmfgf        :   f :::::::::::::::::::::::::::::::::"
t0073="::  f :::::    fmhfghfffff     s  ghfmhffg :::::::::   :::::::::::::::::::::::::::::::::"
t0074=":: ff ::::: fhhfmhg fgff   ff    fffhmhffg :::::::::::::::::::::::::::::::::::::::::::::"
t0075="::    ::::: fffffff      fhffgs  gmmhhg    :::::::::::::::::::::::::::::::::::::::::::::"
t0076=":::::   :       fff  ff fhfhhff  fhmhfg ::::::::::::::::::::::::::::::::::::::::::::::::"
t0077="::::: g   gfg    ff  fhhhfhhgff   fhhg  ::::::::::::::::::::::::::::::::::::::::::::::::"
t0078="::::    ffhff  g    gmmmmffhff  :  hff ::::::::::::::::   ::::::::::::::::::::::::::::::"
t0079=":::  ffhhfffhhff  fffmmgg  ff  :::     :::::::::::::::: p ::::::::::::::::::::::::::::::"
t0080=":   fsfhgffhfhfff   fhhg      :::::::::::::::::::::::::   ::::::::::::::::::::::::::::::"
t0081=": f   sf  fhmmhff   fhgs :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::"
t0082="  f  sfff ffhmhhff  ghf  ::::::::::::::::::::::::::::::   ::::::::::::::::::::::::::::::"
t0083="pp    pfff fhhhhf    gf ::::::::::::::::::::::::::::::: s ::::::::::::::::::::::::::::::"
t0084="   :: f    fmhff  ::    :::::::::::::::::::::::::::::::   ::::::::::::::::::::::::::::::"
t0085=":::::  ff ghmmhf :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::"
t0086=":::::: f  fhmmhg :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::"
t0087=":::::   ffhhmhff :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::"
t0088="::::: f gggffhf  :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::"
t0089=":::::   fhffhmf ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::"
t0090="::::::   h gffg ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::"
t0091=":::::: sfh fgf  ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::"
t0092="::::::  ff ff  :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::"
t0093=":::::::   ff  ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::"
t0094=":::::::::     ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::"
t0095="::::::::::: f ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::"
t0096="::::::::    s ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::"
t0097=":::::::: fs   ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::"
t0098=":::::::: ss ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::"
t0099="::::::::    ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::"
startpos_count=8
startpos={"x","y","exclude","nations"
58,60,FALSE,"Dutch"
27,67,FALSE,"Chinese"
39,62,FALSE,"Portuguese"
49,53,FALSE,"Korean"
63,43,FALSE,"Mongol"
37,78,FALSE,"English"
12,74,FALSE,"Spanish"
44,71,FALSE,"Japanese"
}
e00_0000="0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"
e00_0001="0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"
e00_0002="0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"
e00_0003="0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"
e00_0004="0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"
e00_0005="0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"
e00_0006="0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"
e00_0007="0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"
e00_0008="0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"
e00_0009="0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"
e00_0010="0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"
e00_0011="0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"
e00_0012="0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"
e00_0013="0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"
e00_0014="0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"
e00_0015="0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"
e00_0016="0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"
e00_0017="0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"
e00_0018="0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"
e00_0019="0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"
e00_0020="0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"
e00_0021="0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"
e00_0022="0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"
e00_0023="0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"
e00_0024="0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"
e00_0025="0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"
e00_0026="0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"
e00_0027="0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"
e00_0028="0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"
e00_0029="0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"
e00_0030="0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"
e00_0031="0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"
e00_0032="0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"
e00_0033="0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"
e00_0034="0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"
e00_0035="00000000000000000000000000000000000000000000000000000000
```

## 策划参考价值
SLG历史场景/战役剧本的数据结构参考。
