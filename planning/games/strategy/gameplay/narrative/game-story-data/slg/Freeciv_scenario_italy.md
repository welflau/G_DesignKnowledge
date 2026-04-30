# 文明 · 历史场景「italy」

> 来源：longturn/freeciv21
> 原始链接：https://github.com/longturn/freeciv21
> 分类：gameplay
> 标签：文明, 4X策略SLG, 历史场景, 剧本
> 游戏类型：4X策略SLG

## 概述
Freeciv历史场景脚本：italy

## 正文
```sav

[scenario]
game_version=3000000
is_scenario=TRUE
name=_("Italy (classic/medium)")
authors=_("Paolo Sammicheli")
description=_("Overhead 100x100 map of Italy.")
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
random_seed=1586960032
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
"aifill",9,5
"alltemperate",FALSE,FALSE
"borders","DISABLED","ENABLED"
"flatpoles",100,100
"gameseed",1002711941,0
"generator","SCENARIO","RANDOM"
"happyborders","DISABLED","NATIONAL"
"huts",0,15
"landmass",30,30
"mapseed",1728193867,0
"mapsize","FULLSIZE","FULLSIZE"
"maxplayers",9,150
"metamessage","Scenario: Italy",""
"revolentype","RANDOM","RANDOM"
"savename","freeciv-italy","freeciv"
"sciencebox",50,100
"separatepoles",TRUE,TRUE
"singlepole",FALSE,FALSE
"size",10,4
"startpos","DEFAULT","DEFAULT"
"startunits","ccx","ccwwx"
"steepness",30,30
"teamplacement","CLOSEST","CLOSEST"
"techlevel",3,0
"temperature",50,50
"tilesperplayer",100,100
"tinyisles",FALSE,FALSE
"topology","","WRAPX|ISO"
"turnblock",FALSE,TRUE
"victories","","SPACERACE|ALLIED"
"wetness",50,50
"xsize",100,64
"ysize",100,64
}
set_count=33
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
t0000="aaaammmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmaaaa                                            "
t0001="aaammmmmmmmmmmmmmmmmmmmmmmhmmmmmmmmhmmhhhmmmhhmmhhmmmaaaa                                          a"
t0002="aammmmmmmfhhmfmmhmmmmgmfmfmfmmttmgmffmfffgfhhfhpppfhhmaaaa                                      aaaa"
t0003="ammmmmmmhhffhf+mhmhhmgmmfffmmmmmhgmmhmmfmghfppppphpffmaaaaa                                aaaaaaaaa"
t0004="mmmmmmmfffgfgg+gfhgfhgmffmmmmhhhggmmmmhhppppggggpppffmaaaaa                               aaaaaaaamm"
t0005="mmmmhmmhfjgggg+gfgggggfhhmpppggggmhmmmpfpppgggggggpppmaaaaaa                             aaaaaaaaamm"
t0006="mmmhmmhhfgggggggpphg+gghghpphhgfgfhmhppppgggggggg  pggmmaaaaa                            aaammmmmmmm"
t0007="mmhhhmgfgggppssggspg+gppps+gssggppgfppppgggggggg      pmaaaaa                           aaammmmmmmmm"
t0008="mmhhmhggggppppgggpppsphps++sppspgppppgggggg g          aaaaa                           aaammmmmmmmmm"
t0009="hhjjjhggpppppgggppsgssggggggsggppppgggggg               aaaa                          aaammmmmmhhhhm"
t0010="hffhjhggppppggggggggggggggggggggggggggggg  p             aaa                          aaammmmmhhhhhh"
t0011="ffjppgggpssgggggggggsggsgggggggggggggggggg                a                            aaammmmmhhhph"
t0012="jjppgggggggggggggssggggggggsgggsssggggssgg                                             aaammmmmmhpgf"
t0013="gggggghgggsggsgggggggggssgggsggggggssgsgggg                                            aaaammmmmhfgg"
t0014="ggggghggggssgggggssgggggggsgggsggggsggggsggg                                           aaaammmmhhffg"
t0015="gggggggggggggsgppsgggggggggggssggggggggsggsg                                          aaaammmmmhjfgg"
t0016="pgpggggggggsssggpppppppppggggggggggggggggg                                             aaaammhhffjpp"
t0017="pppggggggggggggggfpppppppppggggggggggggggg                                             aaaammhhpgfpp"
t0018="pggggggggggggfhgmhhfhfhhpppppggggggggggggg                                             aaaammmhhggpp"
t0019="ggppggmphfpphhfjffhmhhhhfppppppggggggggggg                                              aaaaammhfggp"
t0020="ggggmhhhgghgggggjfmfphhmhhfhppppgggggggggg                                              aaaaaammhfgg"
t0021="pphfhgggp     hgppmfgfmfhhhhhfppppfgggggppp                                             aaaaammhffhg"
t0022="hhpfgpgpp :::   ggphmhfjjfhmmpppphjggfggggpp                                            aaaammmhffjh"
t0023="hjghhhp   :::     hppfmmffmhmgfhmhhfggggggppp                                           aaaammmmhhhj"
t0024="gghgpp  ::::::       pmhmmmhgghmmmmhffggfhgpppp                                          aaaaaammthg"
t0025="ghhpp  :::::::::      ppphmhhmfhhhmmhgmjgfhfgpggg                                         aaaaaaattp"
t0026="pppp  ::::::::::       gpfhffffggghmmggmgmmgggppgg                                         aaaaaaaaa"
t0027="     ::::::::::::      gggggfgggfghhmmgmgggmhppppfpg                                        aaaaaaaa"
t0028=":::::::::::::::::      fgggggggggggggmgmmmggmhfhppppgg                                       aaaaaaa"
t0029="::::::::::::::::::      gppfghgpfhghfggmfhmgmhjppphppg                                        aaaaaa"
t0030="::::::::::::::::::       pphgppfgpggfhhhfghgmhhffhpppg                                          aaaa"
t0031="::::::::::::::::         gpppphggpphghfgmgpgmmhhggggggg                                         aaaa"
t0032=":::::::::::::::          gpppgppgggpgfhfghmggmggggfpppg                                          aaa"
t0033="::::::::::::::           gpgppphfgppph+hmmgfgmgfpjfpppp                                          aaa"
t0034=":::::::::::::            gghpgpgggfppp++mhjggfmfppphppg                                          aaa"
t0035="::::::::::::   g  p      g ggppgggfhhpfghhhghfmhhfgggggg                                         aaa"
t0036="::::::::::::   g            gpgfgghhfpggfhgghmmmpggpfpgg                                          aa"
t0037="::::::::::::   p      gt   gg ggghhhjphggfgjhhmhgmhfjppsg                                         aa"
t0038="::::::::::   pppp    pfh      ggghpgg+hgggggghmmgghmfhppg                                ::::::   aa"
t0039=":::::::::: ppppfp              gggppfgfggppggfhmmmmhhfppgpp                             ::::::::  aa"
t0040=":::::::::: gphppp             ggggpppphggjggpphmgggghmgggppp                           ::::::::::  a"
t0041="::::::::::  phphp      p   h      gpppfhggghphgfmmhgmmgfpppg                           :::::::::::  "
t0042=":::::::::  gpppfp                  gpppjgpgghhpgfmmgmggfjpgggp      f                  :::::::::::::"
t0043=":::::::::  gpmfpp      ::::         gppp+pjgpppphgmgggffhfgpppp                        :::::::::::::"
t0044=":::::::::  ppppp       :::::::      ggppgpggppppjggmmmfhfgghppppp      pp               ::::::::::::"
t0045="::::::::::  pphp      ::::::::::      ppfpgfhpfppfggmhgggghmpphpggpppppphp               :::::::::::"
t0046=":::::::::  ppfhp      :::::::::::      fggghggpppgggfmmmmhmhmhgggppppphhpp                ::::::::::"
t0047=":::::::::  gpppg      :::::::::::       ggggppppppggjfhhmmfmhggpppppggpp                  ::::::::::"
t0048=":::::::::   ggp       :::::::::::::      ppppjjgfppggjfhghhhhgghpphhgggg                  ::::::::::"
t0049="::::::::::    g       :::::::::::::::     pppgsssfpggssjgghgggppfhfgpppgg                  :::::::::"
t0050=":::::::::::           :::::::::::::::::    pp ssphppggggpggggpppfpgpppppggg                :::::::::"
t0051="::::::::::::   p      :::::::::::::::::::      phppppppgpfgggfppppppppppgggg               :::::::::"
t0052=":::::     :   pp       :::::::::::::::::::     f   pp ggppppgppjpjppppppppgggg              ::::::::"
t0053="::::   g    ppphp       :::::::::::::::::::::          gggggggppgpfppppppppggfgg            ::::::::"
t0054="::::  g    ggpphgp      :::::::::::::::::::::   ::     ggppfggpppppppgghfpppppppfg          ::::::::"
t0055="::::  g   pgggpjhgg    ::::::::::::::::::::::::::::::   pgggfggppphppphgpffpppppppg          :::::::"
t0056="::::  gppgppggffjgg     ::::::::::::::::::::::::::::::  pggmghpppggppppjppppppppppppp        :::::::"
t0057="::::  gppgpmgggfhpgp    :::::::::::::::::::::   :::::   p  phhpphgppghppggpgpppppppppgg      :::::::"
t0058="::::  ggggpjggggmhfp    ::::::::::::::::::::: g ::::: p    pppppppjfpghpmmggggfpppppppfg      ::::::"
t0059="::::   ggpfggpggghhpp   :::::::::::::::::::::   :::::    h     ppgppjpgpmmmppggggpfpppppg      :::::"
t0060="::::    gjfgpggghhfp   :::::::::::::::::::::::::::::::::       pgfhppjppffhmpgg   gppppppp     :::::"
t0061="::::    gfggpgggjfpp   ::::::::::::::::::::::::::::::::::::    ppgfhgfhfghffppp     ggppppg     ::::"
t0062=":::::   gggpggpgggg    :::::::::::::::::::::::::::::::::::::   pppgfgggggggggpp  :    gfpppg    ::::"
t0063=":::::   gggggppgfgg    :::::::::::::::::::::::::::::::::::::     pfppppppfppgp   ::     ggpgg   ::::"
t0064="::::::   ggpppggfmgg   :::::::::::::::::::::::::::::::::::::::    pp ppppphfgp  ::::    ggfgg   ::::"
t0065="::::::  gggpfgghgghg   :::::::::::::::::::::::::::::::::::::::::      gpfffppp   :::::   ggg    ::::"
t0066="::::::  gpgfjggggmhp   ::::::::::::::::::::::::::::::::::::::::::     ppfhpgg    ::::::   gg    ::::"
t0067=":::::   gppfggggmmpp   :::::::::::::::::::::::::::::::::::::::::::    pfhppgp   ::::::::      ::::::"
t0068="::::   gppppggpgggp    :::::::::::::::::::::::::::::::::::::::::::::  pgppggpp   :::::::::: ::::::::"
t0069="::::   gpdffgpphfgg   ::::::::::::::::::::::::::::::::::::::::::::::   gpghgpppp  ::::::::::::::::::"
t0070=":::    gfddpgfpjhfg   :::::::::::::::::::::::::::::::::::::::::::::::  ppgppppgpp   ::::::::::::::::"
t0071=":::  p gphppggfjpp     ::::::::::::::::::::::::::::::::::::::::::::::   pgghfghppp  ::::::::::::::::"
t0072=":::    ggfhpggggfpp   :::::::::::::::::::::::::::::::::::::::::::::::   ppgfphhgp   ::::::::::::::::"
t0073=":::     ggfhhg   gp   :::::::::::::::::::::::::::::::::::::::::::::::   pppfmmmhp   ::::::::::::::::"
t0074=":::      ggggg         ::::::::::::::::::::::::::::::::::::::::::::::    pppfhpppp  ::::::::::::::::"
t0075="::::      g gg         ::::::::::::::::::::::::::::::::::::    :::::::   ppphggpp   ::::::::::::::::"
t0076="::::                ::::::::::::::::::::::::::   ::::::::    g  :::::     pffg     :::::::::::::::::"
t0077="::::::           ::::::::::::::::::::::::::::: p :::       p    :::::   ggphpp   :::::::::::::::::::"
t0078="::::::::     :::::::::::::::::::::::::::::::::   :::  f g    ::::::::  pgpfhp  :::::::::::::::::::::"
t0079=":::::::::::::::::::::::::::::::::::::::::::::::::::::     p   ::::     ppfmhp ::::::::::::::::::::::"
t0080=":::::::::::::::::::::::::::::::::::::  :::::::::::::::        ::       ppmhgg ::::::::::::::::::::::"
t0081=":::::::::::::::::::::::::::::::::::    ::::        :::::  h            pppggp ::::::::::::::::::::::"
t0082=":::::::::::::::::::::::::::::::::       ::          :::::          p ggphpgp  ::::::::::::::::::::::"
t0083=":::::::::::::::::::::::::::::::              p  php   ::::    ggpppp gphppp  :::::::::::::::::::::::"
t0084="::::::::::::::::::::::::::::                phpghppp        pgggpphp pppgg  ::::::::::::::::::::::::"
t0085=":::::::::::::::::::::::::             h    gpphgggpppggpgggpppppfhg   ppg  :::::::::::::::::::::::::"
t0086=":::::::::::::::::::::::                  p gppfppppphpggpppppfmmmgg       ::::::::::::::::::::::::::"
t0087=":::::::::::::::::::::                      ggpfhppgffppppfhhmmmhpp   :   :::::::::::::::::::::::::::"
t0088="::::::::::::::::::::                        gphpggffmmphhmmmmmhhgp  ::::::::::::::::::::::::::::::::"
t0089="::::::::::::::::::                           ggppphhhpphhhmhhhhgm   ::::::::::::::::::::::::::::::::"
t0090=":::::::::::::::                                  ppppppphhhppphgg  :::::::::::::::::::::::::::::::::"
t0091="::::::::::::                                      pppgppppfhpssgg   ::::::::::::::::::::::::::::::::"
t0092=":::::::::::                                        ppppppppfhhppgp  ::::::::::::::::::::::::::::::::"
t0093="::::::::                                             ppppddghppfpp  ::::::::::::::::::::::::::::::::"
t0094="::::::                                                   dpggpffpp  ::::::::::::::::::::::::::::::::"
t0095=":::::                                                      gpppggp  ::::::::::::::::::::::::::::::::"
t0096="::::                                                       pspggp  :::::::::::::::::::::::::::::::::"
t0097="::                                                          ssppp ::::::::::::::::::::::::::::::::::"
t0098="                                                               pp ::::::::::::::::::::::::::::::::::"
t0099="                                                                   :::::::::::::::::::::::::::::::::"
startpos_count=0
e00_0000="0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"
e00_0001="0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"
e00_0002="0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"
e00_0003="0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"
e00_0004="0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"
e00_0005="0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"
e00_0006="0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"
e00_0007="0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"
e00_0008="0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"
e00_0009="0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"
e00_0010="0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"
e00_0011="0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"
e00_0012="0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"
e00_0013="0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"
e00_0014="0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"
e00_0015="0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"
e00_0016="0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"
e00_0017="0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"
e00_0018="0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"
e00_0019="0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"
e00_0020="0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"
e00_0021="0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"
e00_0022="0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"
e00_0023="00000000000000
```

## 策划参考价值
SLG历史场景/战役剧本的数据结构参考。
