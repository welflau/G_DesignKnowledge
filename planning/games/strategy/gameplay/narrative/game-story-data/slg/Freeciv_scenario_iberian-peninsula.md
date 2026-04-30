# 文明 · 历史场景「iberian-peninsula」

> 来源：longturn/freeciv21
> 原始链接：https://github.com/longturn/freeciv21
> 分类：gameplay
> 标签：文明, 4X策略SLG, 历史场景, 剧本
> 游戏类型：4X策略SLG

## 概述
Freeciv历史场景脚本：iberian-peninsula

## 正文
```sav

[scenario]
game_version=3000000
is_scenario=TRUE
name=_("Iberian Peninsula (classic/large)")
authors=_("Miguel Farah, Daniel Markstedt")
description=_("Overhead 136x100 map of the Iberian Peninsula (modern-day Spain and Portugal).")
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
year=-2000
year_0_hack=FALSE
globalwarming=0
heating=0
warminglevel=8
nuclearwinter=0
cooling=0
coolinglevel=8
random_seed=1586959891
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
"diplchance",40,80
"dispersion",2,0
"flatpoles",100,100
"generator","SCENARIO","RANDOM"
"happyborders","DISABLED","NATIONAL"
"huts",100,15
"landmass",56,30
"mapseed",0,0
"mapsize","FULLSIZE","FULLSIZE"
"maxplayers",8,150
"metamessage","Scenario: Iberian Peninsula",""
"minplayers",1,1
"onsetbarbs",60,60
"revolentype","RANDOM","RANDOM"
"sciencebox",50,100
"separatepoles",TRUE,TRUE
"singlepole",FALSE,FALSE
"size",14,4
"startpos","DEFAULT","DEFAULT"
"startunits","ccccxx","ccwwx"
"steepness",30,30
"teamplacement","CLOSEST","CLOSEST"
"techlevel",3,0
"temperature",50,50
"tilesperplayer",100,100
"tinyisles",FALSE,FALSE
"topology","","WRAPX|ISO"
"victories","","SPACERACE|ALLIED"
"wetness",50,50
"xsize",136,64
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
have_huts=TRUE
have_resources=FALSE
t0000=":::::::::::::::::::::::::::::::::::::::::::::::::::::::::::                ffffggggggggggggggggggggggghhhhhhgggg    ::::::::::::::::::::"
t0001="::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::              ffffggggggggggggggggggggggggggggggggg      :::::::::::::::::::"
t0002="::::::::::::::              ::::::::::::::::::::::::::::::::::            ffggggggggggggggggggggggggggggggggggg      :::::::::::::::::::"
t0003="::::::::::::                                                              gggggggggggggggggggggggggggggggggggg       :::::::::::::::::::"
t0004=":::::::::::        ggggg                               gg                 gggggggggggggggggggggggggggggggggggg       :::::::::::::::::::"
t0005=":::::::::::      gggggmgg         ggggggg            ggggg               gggggggggggggfggggggggggggggggggggggg       :::::::::::::::::::"
t0006="::::::::        ggggggggggggggg gggggggggggg       ggggggggggggg  g gggggggffgggggghhfffhghgggghgggggggggghggg       :::::::::::::::::::"
t0007="::::::::        gggghgghhgggggggggggggggggggggggggggggggggggggggggggghgggghffhhhhhhhhhffhhhhhhhhhhhhhfffhhhgggg      :::::::::::::::::::"
t0008=":::::::        ggggghggghhggggggggggggggfffffffgggggggggggggggggghghgggghgffffhhmmmmmmmmmhhhmmmmmmmmhhhhhmhhggg      :::::::::::::::::::"
t0009="::::::     gggggggghhgghhgggghhgghggghhhhffhhfffhgghhhhhgggghggghfghhghghggffffhhmmmmmmmmmmmmmmmmmmmmmmmhhmhggg      :::::::::::::::::::"
t0010=":::::     ggggggggfhgghhffggghmhhhhhhhmhhhhhhmmmhhhh++hhhgghhhggghhggghgghggfhffhhhhmmmmmmmmmmmmmmmmmmmmhmhhhgg      :::::::::::::::::::"
t0011="::::     gggggggggfhfgggffgghhmmmmmmmmmmmmmmmmmmhhmmhggggggggggggggfhfgfhgggggfghghhhhhhhhmmmmmmhhhmmmmhmhhfggg      :::::::::::::::::::"
t0012=":::     gggggggggghhfgghggggghhhmhhhhhhhhhhhhhhhhgggggffgggggggghghggfgggggggggggggghhhhhhhhhhhhhhhhhhhhhhhfgggg     :::::::::::::::::::"
t0013=":::     ggggggggggghhggggggggghhhhhgggggfhhggggggggggfhhgggggggggggggggggggggggggggggggghhhhhhhhffghhhhhhhggggggg    :::::::::::::::::::"
t0014=":::::     gggggggghhggggggggggghggggggggfggggggggggggfggggggggggggggggggggggggggggggggggggggghhhggggghhhggggggggg    :::::::::::::::::::"
t0015="::::::      gggggghhgggggghggggghhgggggggggggffgggggggggfggggggggggggggggggggggghggggggggggggggggggggggggggggggg     :::::::::::::::::::"
t0016="::::::     ggggggghhhggggggggggghggggggggggggggggggggggffgggggggggggggggggggggggggggggggggggggggggggggggggggggggg    :::::::::::::::::::"
t0017="::::::     gggggghhggggghggggggghggggggggggggggggggggggfgghhghhgggggggggggggggggggggggggggggggggggggggggggggggggg    :::::::::::::::::::"
t0018="::::::       ggggggggggggggggghhggggggggggggggggggggggggghhhhhhhgggggggggggggggggggggggggggggggggggggggggffgggggg    :::::::::::::::::::"
t0019=":::::      gggggggggggggggggghmhhggggggggggggggggggggggghhmmmmhhgggggggggggggggggggggggggggggggggggggggggffggggg     :::::::::::::::::::"
t0020=":::::       gggghggggggghggghmmhhgggggggggggggggggggggggghhhhhhhgggggggggggggggggggggggggggggggggggggggggffgghgg    ::::::::::::::::::::"
t0021="::::::        gggggggggggggfhmhhggggggggggggggggggggggggggggghhgggggggggggggggggggggggggggggggggggggggggggggggg     ::::::::::::::::::::"
t0022=":::::       ggggghhggghhgggfhhhgggggggggggggggggggggggggggghgghggggggggggggggggggggggggggggggggfffggggggghggg      :::::::::::::::::::::"
t0023=":::::       ggggggggggggggffggggggggggggggggggggggggggggggggggggggghggggggggggggggggggggggggggggffggghhhgggg     :::::::::::::::::::::::"
t0024=":::::       gggggggghhhhggfggggggggggggggggggggggggggggggggggfgggghhhgggggggggggggggggggggggggggffggggggggg    :::::::::::::::::::::::::"
t0025=":::::       ggggghhhhghgggggghhhgggggggggggggggggggggggggggggfggggghhhggggggggggggggggggggggggggffgghggggg     :::::::::::::::::::::::::"
t0026=":::::       ffgghhgggggggggghhggggggggggggggggggggggggggggfggfggggggghhggggggggggggggggggggggggffgggggggg     ::::::::::::::::::::::::::"
t0027=":::::       fffgggggghgghggghgggggggg+ggggggggggggggggggggffhfggggggggggggggggggggggggggggggggffgggggggg    ::::::::::::::::::::::::::::"
t0028=":::::       fffgggggggggghgghgggggggg+ggggggggggggggggggggggggggggggggggggggggggggggggggggggggfhggggggg    :::::::::::::::::::::::::::::"
t0029=":::::       fffgggghgghghggghhgggggggggggggggggggggggggggffhhggggggggggggggggggggggggggggggggggggggg      ::::::::::::::::::::::::::::::"
t0030=":::::       ggggggggggggggggghgggggggggggggggggggggggggggfhhgggggggggggggfgggggggggggggggggghggggg    ::::::::::::::::::::::::::::::::::"
t0031=":::::        gggggggghgggghgghggggggggggggggggggggggggggghggggggghhhhggggggggggggggggggggggggggg     :::::::::::::::::::::::::::::::::::"
t0032=":::::        gggggggggghgggggggggggggggggggggggggggggffgghggggghhhmmhhgggffffggggggggggggghgggg      :::::::::::::::::::::::::::::::::::"
t0033=":::::        gggggggggggggghgggggggggggggggggggggggggffghhhggggghhhhhhhggfffffggggggggggggggggg     ::::::::::::::::::::::::::::::::::::"
t0034=":::::        ggggggggggggggggggggggggggggggggggggggggffhmmhggggggghggghhggffffgggggggggghgfggggg    ::::::::::::::::::::::::::::::::::::"
t0035=":::::         gggggggggghggghgggggggggggggggggggggggggghhmhgggggggggggghhggffffggggggghhggfggggg    ::::::::::::::::::::::::::::::::::::"
t0036=":::::        ggggggggggggggggggggfggggggggggggggffgggghhhhggggpppggggggghhggfffggggggghgggggggg     ::::::::::::::::::::::::::::::::::::"
t0037=":::::        ggggggggggggggghggfggfggggggggggggggggghhgggggggpppppggghhhhhhhhffgggggghggggggg      :::::::::::::::::::::::::::::::::::::"
t0038=":::::::      ggggghhggggggggggfffggfggggggggggggggghmhhggggggpppppppgghhmmhhhhhggghhhhgggggg       :::::::::::::::::::::::::::::::::::::"
t0039="::::::       gggghgggggggggggffffggggggggggggggggghmmmhhggggpppppppppghmmmmhhhhhhhghgggggggg     :::::::::::::::::::::::::::::::::::::::"
t0040=":::::        ggghggggggggggggffhhfgggggggggghggggghhhhhgggggpppppp+ppghhmmhhgghghgggggggggg     :::::::::::::::::::::       ::::::::::::"
t0041=":::::       gggggggggggggggggghmhhgggggggggghhhgghhgggggpppppppppppppgghhhhhgggggggggggggg      :::::::::::::::::::          :::::::::::"
t0042=":::::       gggggggggggghgggghmhhggggggghghhhmmhhgggppppppppppppppppppgghhhgggggghgggggggg     ::::::::::::::::::     gggg   :::::::::::"
t0043="::::        ggggggggggghhhgghmhgggggghhhhhmmmmhhpppppppppppppppppppppppggggghggggghgggggg      ::::::::::::           ggggg   ::::::::::"
t0044=":::         ggggggggggghggghhhggpghghhppphhhhhhpppppppppppppppppppppppppppghhhggggggggggg     ::::::::::::     g        gggg   :::::::::"
t0045=":::         gggggggghhhgggghgggppggggppppppppppppppppppppppppppphhpppppppppgghgggggggggg     ::::::::::::    gggg         gg    ::::::::"
t0046=":::         ggggggghggggggggpppppfffpppppppppppppppppppppppppphhhhhpppppppppgghggggggggg     :::::::::::   fhggg               :::::::::"
t0047=":           gggggggggghgggppppppppppppppppppppppppppppppppppphhhhhhhpppppppppghhgggggggg    ::::::::::    ghggggg g     ::    ::::::::::"
t0048="           ggggggggghhgpppppppppppphhppppppppppppppppppppppppphhpppppppppppppgghggggggg     :::::::::    ghgggggghgg    ::::::::::::::::"
t0049="           gggghgggggggpppppppppppphpppppppppppppppppppppppppppppppppppppppppghgggggggg    :::::::::    ghggggggggg     ::::::::::::::::"
t0050="          ggggggghggpppppppppppppppppphhpppppppppppppppppppppppppppppppppppppghgggggggg    :::::::::     ggggghggg     :::::::::::::::::"
t0051="          ggghgggggggppppppppppppppppppppppppppppppppppppppppppppppppppppppppghgggggggg    :::::::::      g  ggggg     :::::::::::::::::"
t0052="         gggghghggghgpppppppppphpppppppphhhphhhphhhpppppppppppppppppppppppppggggggggggg    ::::::::::::      gggg      :::::::::::::::::"
t0053="         ggghgghghhgggppppppphhhhhpfffhhhpppppppppphhhppppppppppppppppppppppghhgggggggg     ::::               g     :::::::::::::::::::"
t0054="        ggghggggggggggpppppphhpppfhhhhffppppppppppppppppppppppppppppppppppppghgggggggggg    :::    gh               ::::::::::::::::::::"
t0055="        gggggggggggggpppppppppppppppppfphffppffffppppppppppppppppppppppppppgghhggggghggg          gggg    ::       :::::::::::::::::::::"
t0056="       gggggggggggggpppppphhhppppppppppphhppppppfffffffpppppppppppppppppppppgghgggfgggggg        gggg     :::     ::::::::::::::::::::::"
t0057="       ggghggggggggpppppphhhppppffffpppppphpppppppppppppppppppppppppppppphhppgggggfggghgggg      ggg     :::::::::::::::::::::::::::::::"
t0058="       gggggggggggpppppppppppppppfffpppppphppppppppppppppppppppppppppppppppppgghgggggggggggg          ::::::::::::::::::::::::::::::::::"
t0059="       gghggggggggpppppffffppppppfffppppppphhpppppffppppppppppppppppppppppppggghhggghgghggg        g  ::::::::::::::::::::::::::::::::::"
t0060="       gggggggggggppppppffpppppppfpppppppppphpppffffppppppppppppppppppppppgggggghghhghgggg     ::    :::::::::::::::::::::::::::::::::::"
t0061="       ggggggggggggppppppppppppppppppppppppphhppppffpppppppppppppppppphfffffggggggggggggg    :::::::::::::::::::::::::::::::::::::::::::"
t0062="       ggggggggggffgppppppppppppppppppppppppphpppppfffppppppffpppppphhffffffgggggggggggg     :::::::::::::::::::::::::::::::::::::::::::"
t0063="       ggg ggggfffgggpppppppppppppppppppppppphpppppppfffpppfffpppppphhfffffgggggggggggg    :::::::::::::::::::::::::::::::::::::::::::::"
t0064="           ggggggggggppppppppppppppppppppppppppppppppppffffffpppppphhffff+fggggggggggg     :::::::::::::::::::::::::::::::::::::::::::::"
t0065="         gggggggggggggppppppppppppppppppppppppphhppppppppppppppppphhfffffffgggggggggg    :::::::::::::::::::::::::::::::::::::::::::::::"
t0066="::       gggggggggggggpppppppphhppppphhhpppppppphhhhppppppppppppppphffggggggpgggggggg    :::::::::::::::::::::::::::::::::::::::::::::::"
t0067=":::::        ggggggggpppppppppphpppppphhhhppppppppphhpppppphhhhhpphhhggpgpggggggggggg    :::::::::::::::::::::::::::::::::::::::::::::::"
t0068=":::::        gggggggpppppppppppppppppppphhhhhppppppphhhhhhhhhppppphmmhgggggpgpggpgggg    :::::::::::::::::::::::::::::::::::::::::::::::"
t0069="::::         gggggggpppppffffpppppppppppppphhpp+hhhhhpppppppppppphhmhhghhgpgpgphggpgg    :::::::::::::::::::::::::::::::::::::::::::::::"
t0070=":            gggggpppppppppppppppppppphhhppppppppppppppppppppppphmhmmmhhhggpgpgphggg    ::::::::::::::::::::::::::::::::::::::::::::::::"
t0071="            gggggppppppppppppppppppphhhpppppppppppppppppppppppphmmmhhmmmhhgppgpfggpg    ::::::::::::::::::::::::::::::::::::::::::::::::"
t0072="             ggggpppppppfffpppphhhphhppppppppppppppppppppppppppphhhhhhhhhggpgphgpgg     ::::::::::::::::::::::::::::::::::::::::::::::::"
t0073="             gg+gpppppppffffpppphhhhppppppppppppppppppppppppppphhhppppppppppgpgpgpgg  ::::::::::::::::::::::::::::::::::::::::::::::::::"
t0074="             ggggpppppppppppppppphhppppppppppppppppppppppppppffffppppppppphppgpg      ::::::::::::::::::::::::::::::::::::::::::::::::::"
t0075="             gggffppppppppppppphhhhpppppppppppppppppppppppppffffppppppppppppppg    :::::::::::::::::::::::::::::::::::::::::::::::::::::"
t0076="            ggggffpppppppppppphhppppppppppppppppppppppppppppffpppppppppphpppp      :::::::::::::::::::::::::::::::::::::::::::::::::::::"
t0077="            ggggffpphpppppphhpppppppppppppppppppppppppppppppfppppppppppppppp      ::::::::::::::::::::::::::::::::::::::::::::::::::::::"
t0078="            gggpppphhhpppphhppppppppppppppppppppppphhhhhppppfppppphhhhhppppp     :::::::::::::::::::::::::::::::::::::::::::::::::::::::"
t0079="            pphppppphhpppppppppppppppppppppppppppppp++phpppppppppphmmmhpppp      :::::::::::::::::::::::::::::::::::::::::::::::::::::::"
t0080="           ppppppppppppppppppppppppppppppppppppppppphhppppppphhhhhhhhhhpppp      :::::::::::::::::::::::::::::::::::::::::::::::::::::::"
t0081="           ppppppppppppp      ppppppppppp+pppppppppppppppppphhmmmmmhdddppp       :::::::::::::::::::::::::::::::::::::::          ::::::"
t0082="           pp      pppp         pppppppppppppppppppppphhpphhhhhhhhhdddddpp      :::::::::::::::::::::::::::::::::::                :::::"
t0083="                    p            ppppppppppphhpppppppffhhppphpppppdddddpp      :::::::::::::::::::::::::::                          ::::"
t0084="                                  ppppppppphhhhppppppppppppppppppppppppp       ::::::::::::::::::::::::               pppppppppppp   :::"
t0085="                                  pppppppppphhhppppppppp pppppp    p  p       :::::::::::::::::::::            pppppppppppppppppppp     "
t0086="                                  ppppppppphhpppppp                          :::::::::::::::::::             ppppppppppppppppppppppp    "
t0087="::::::::                           ppppppffpppppppp                        :::::::::::::::::        ppppppppppppphhpppppppppphhppppppppp"
t0088="::::::::::::                       ppppppffppppp                           ::::::::::::::         pppppppppppppphhpppppphhhhhhpppppppppp"
t0089=":::::::::::::                       pppppfpppp                  :::::::::::::::::::::::::       ppppppppppphhhhhpppppppppppppppppppppppp"
t0090=":::::::::::::                       pppppfppp     :::::::::::::  ::::::::::::::::::::          ppppdppdpppddpppppppppppppppppppppppppppp"
t0091="::::::::::::::                       ppppffpp   ::::::::::::::::::::::::::::::::::::::::      ppdpppphdppppphhpppppddpppppppphhppppppppp"
t0092="::::::::::::::                        ppppff     :::::::::::::::::::::::::::::::::::::::     ppdppp
```

## 策划参考价值
SLG历史场景/战役剧本的数据结构参考。
