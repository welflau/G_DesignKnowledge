# 文明 · 历史场景「france」

> 来源：longturn/freeciv21
> 原始链接：https://github.com/longturn/freeciv21
> 分类：gameplay
> 标签：文明, 4X策略SLG, 历史场景, 剧本
> 游戏类型：4X策略SLG

## 概述
Freeciv历史场景脚本：france

## 正文
```sav

[scenario]
game_version=3000000
is_scenario=TRUE
name=_("France (classic/large)")
authors=_("Mathieu Roy")
description=_("Overhead 140x90 map of France.")
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
random_seed=1586959647
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
"aifill",15,5
"alltemperate",FALSE,FALSE
"borders","EXPAND","ENABLED"
"citynames","GLOBAL_UNIQUE","PLAYER_UNIQUE"
"civilwarsize",6,10
"flatpoles",100,100
"generator","SCENARIO","RANDOM"
"landmass",33,30
"mapseed",0,0
"mapsize","FULLSIZE","FULLSIZE"
"maxplayers",26,150
"metamessage","Scenario: France",""
"revolentype","RANDOM","RANDOM"
"savename","freeciv-france","freeciv"
"savepalace",FALSE,TRUE
"sciencebox",80,100
"separatepoles",TRUE,TRUE
"singlepole",FALSE,FALSE
"size",13,4
"specials",300,250
"startpos","DEFAULT","DEFAULT"
"startunits","ccxx","ccwwx"
"steepness",30,30
"teamplacement","CLOSEST","CLOSEST"
"techlevel",2,0
"temperature",50,50
"tilesperplayer",100,100
"tinyisles",FALSE,FALSE
"topology","","WRAPX|ISO"
"victories","","SPACERACE|ALLIED"
"wetness",50,50
"xsize",140,64
"ysize",90,64
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
t0000="::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::iiiiiiiii:iiiiiiiiiiiiiii:iiiiiiiiiii::iiiiiiiiii::iiiiiiiiiiiiiiiiiiiii"
t0001="::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::  pppppiiii:iiiiiiiiiiiiiii:iiiiiiiiiiii:iiiiiiiiiii::iiiiiiiiiiiiiiiiiiii"
t0002=":::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::  ppfppppiii:iiiiiiiiiiiiiii:iiiiiiiiiiii:iiiiiiiiiiii::iiiiiiiiiiiiiiiiiii"
t0003=":::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::  pfpggppiii:iiiiiiiiiiiiiii:iiiiiiiiiiii:iiiiiiiiiiiii:iiiiiiiiiiiiiiiiiii"
t0004=":::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::  ppggggpiii:iiiiiiiiiiiiiii:iiiiiiiiiiii:iiiiiiiiiiiii::iiiiiiiiiiiiiiiiii"
t0005=":::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::    pggpgggppi:ipiiiiiiiiiiiii:iiiiiiiiiiii:iiiiiiiiiiiiii::iiiiiiiiiiiiiiiii"
t0006="::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::     p  ppfggppp  ppppiiiiiiiiii::iiiiiiiiiiii:iiiiiiiiiiiiiii:iiiiiiiiiiiiiiiii"
t0007="::::::::::::::::::::::::::::::::::::::::::::::::::::::::::     gggpppfpgpffppppfppiiiiiiiiii:iiiiiiiiiiiii:iiiiiiiiiiiiiiii:iiiiiiiiiiiiiiii"
t0008=":::::::::::::::::::::::::::::::::::::::::::::::::::::::::     ggggggpfggpffffppfpppttttiiiii:iiiiiiiiiiiii:iiiiiiiiiiiiiiii:iiiiiiiiiiiiiiii"
t0009=":::::::::::::::::::::::::::::::::::::::::::::::::::         gggphpggpfpggppffpgpfpfpgpttiiii:iiiiiiiiiiiii:iiiiiiiiiiiiiiii:iiiiiiiiiiiiiiii"
t0010=":::::::::::::::::::::::::::::::::::::::::::::::           gggggppffggffpgppppfpgpffpggggiitt ttiiiiiiiiiii:iiiiiiiiiiiiiiii::iiiiiiiiiiiiiii"
t0011=":::::::::::::::::::::::::           ::::   ::       pgggggggppgghpppggpppssggffggfggggggiitt ttttiiiiiiiii:iiiiiiiiiiiiiiiii:iiiiiiiiiiiiiii"
t0012="::::::::::::::::::::::::                        ppgppgggggpphppggpfpggggpsspppfpgfggggggiitg gpttiiiiiiii::iiiiiiiiiiiiiiiii:iiiiiiiiiiiiiii"
t0013="::::::::::::::::::::::::   p                   gggggggggpggppfpfggppggggpppsppfpfffffgggitgg ggttiiiiiiii:iiiiiiiiiiiiiiiiii:iiiiiiiiiiiiiii"
t0014="::::::::::::::::::::::::       ppgp            ggggggggggpgggppppgggggggpfpppgpfffggfgggitp gggttiiiiiii::iiiiiiiiiiiiiiiiii:iiiiiiiiiiiiiii"
t0015="::::::::::::::::::::::::        pgp     ppppp   pgppppgpggpgggpggggggggggfpgfpppffggfgggitp pgtttiiiiiii:iiiiiiiiiiiiiiiiiii:iiiiiiiiiiiiiii"
t0016="::::::::::::::::::::::::   p     ggg    pggppp    pppppppppppgggggpgggggppfgpfppfpgggggpppp ggtiiiiiiii::iiiiiiiiiiiiiiiiii::iiiiiiiiiiiiiii"
t0017="::::::::::::::::::::::::     p   ggg   ppggggggg    p  p ppffppgpggpggggpppggfpfpppgggggggg ggttiiiii:::iiiiiiiiiiiiiiiiiii:iiiiiiiiiiiiiiii"
t0018="::::::::::::::::::::::::::   p   dggpppppgggggggppp  p  s  pppgggggggggggpppppffffpgggggggp gggtttii:::iiiiiiiiiiiiiiiiiii::iiiiiiiiiiiiiiii"
t0019="::::::::::::::::::::     ::      dgggggggggggggggggpppggsp  ppggggppppgggggppppfffppggpfpff gfggttt  iiiiiiiiiiiiiiiiiiii::iiiiiiiiiiiiiiiii"
t0020="::::::::::::::::::               dggggggggggggggggggpggggpp ppgggggpfppggggpppffpppppffffpp ggfggg  ttiiiiiiiiiiiiiiiiiii::iiiiiiiiiiiiiiiii"
t0021=":::::::::::::::::      p          pppphhppppppppfppgggggggg ppggggggpppggggppppfpppffffpfpgg ggfggg ttttttttttiittttttii::iiiiiiiiiiiiiiiiii"
t0022="::::::::::::::      ppppp     p p ppppphphhppphppppggggggggs pgggggggpggpgggpfppfpppfpffffgg ggfggg gtttgttttttttttttttt iiiiiiiiiiiiiiiiiii"
t0023=":::::::::::         pppppp   ggpgpppphppphpphpppggggggggggggp pgpppggggpggggpfppffpppppfffpgs ghgp  gggtggggggtttgffggtt fiiiiiiiiiiiiiiiiii"
t0024=":::::::::      pppppppgpppp   gggpppppppfpphppfphgggggggggggp ppppppppppggpgggfpppppppppfffgg ghgg ggppgpppppgttfffpgfff ffiiiiiiiiiiiiiiiii"
t0025="::::::::     dggpgggggpgggg   pggpggppggggggggggggppppggggggp  pp  pp   ggpgggpppppppfpppfpgg gpppg gphppggpppggpppppfpf fiiiiiiiiiiiiiiiiii"
t0026="::::::::  p  dggpgggggpggggppppggggggpgggpfpphpfppfppppppgggppp p p p gg ppgggppppppffffppfgs gggp  ghphppggpfppppppppp  fiiiiiiiiiiiiiiiiii"
t0027="::::::::         gphpphggggppfpppggggggggppppppppppppfffpppgggp  pp   ggp  pppppppfpppfpfffppp gp  gppppgpgghffffppppps ffiiiiiiiiiiiiiiiiii"
t0028=":::::::::      pggggppppfppppppppgggpfpgppgggpppgggggggggpggggpppppp ppggp pppppppppppffpfpggp gp gmhgpggpgghhhhffppppp ffiiiiiiiiiiiiiiiiii"
t0029=":::::::::::      pgghppppppggppppppppfppgpgggpfpgggggggggpggggpggpggppfpgpp  spppppppppffppggpp gggphgggppfhhhhhhggppp  ffiiiiiiiiiiiiiiiiii"
t0030=":::::::::::   ddggggpppppgggggpfggpppppggfpffpppgggggggggpppgggggpggpffppggp spspgggggpppfpgggp pggpppggppfhhhhhggggpp fftiiiiiiiiiiiiiiiiii"
t0031="::::::::::::      ggggggpgggggpppgpffppggpppfppfggggggggggpfpgggpgpfppffpggg ppppggggggppfphppp ppsghppgpfhhmhhhgggggg tttiiiiiiiiiiiiiiiiii"
t0032=":::::::::::::     d dgggggpppppppggppppggpppppppgggggppgggppppffppppfffppgggp pppgggggpgpfpppp  pggsppgpfhhmmhhggggggg ttiiiiiiiiiiiiiiiiiii"
t0033="::::::::::::::        ddggp ppp ppgggfppgpggggggpppppppggppggggpfpggpppppgggp pggggggpppppppfp ppgpggpgpphmmahhgggggg  ttiiiiiiiiiiiiiiiiiii"
t0034="::::::::::::::         ddgg      pgggppppggggggggggppp     pgggppppggggppgggp pggggggppfphhpppgggggggphpfhmhmhhgggggg ttiiiiiiiiiiiiiiiiiiii"
t0035=":::::::::::::::::::     ddgg    ppggggpfppgggggggggp  pppp  gggggppggggpgggppppggggppgpffpppfpgggggpgpppphmhhhhgfgggg ttiiiiiiiiiiiiiiiiiiii"
t0036="::::::::::::::::::::      dp   pdpggggppppgggggggggp pppppp  pgggppfgggggggggppggggpppgfhpffppggggggggggfhhhghgggpgps ttiiiiiiiiiiiiiiiiiiii"
t0037=":::::::::::::::::::::            dgggggggggggppggp  ppgggggp  gggggpppgggggggggggggpppppphfppggggggggfggpghhhgggpgpps ttiiiiiiiiiiiiiiiiiiii"
t0038=":::::::::::::::::::::             dgggggggpppg     pppgggggpp  ppgggpgggggggggggpppggppphpfppggggfgggffpgfhhfggpppfgs tiiiiiiiiiiiiiiiiiiiii"
t0039=":::::::::::::::::::::    fpp        gggggg    ppggppspgggggppp ppgggpggggggggggppgppggppppfppggggfggggpffhhffgggggf   tiiiiiiiiiiiiiiiiiiiii"
t0040=":::::::::::::::::::::          :          pppppgggggssgggggpgg  pppggpfppggggggpsppgggppggpppgggggfgggpggfggggggg g tttiiiiiiiiiiiiiiiiiiiii"
t0041=":::::::::::::::::::::::       :::      pgggggggggggggggggggpggp  ppppppppgggppggpppggppsggpgpggggggggggfgggggggg    tttiiiiiiiiiiiiiiiiiiiii"
t0042=":::::::::::::::::::::::::    :::       pggggggggpppggggggppfgggpp ppppgppgggggggppgggpppggggggggggggfpgggfgfgghmm ttttiiiiiiiiiiiiiiiiiiiiii"
t0043="::::::::::::::::::::::::::::::::   p pppgggpphphpffppggggppppggpp  pppggpggpggppgpggggpppppgggppggggffgggfggfphma   itiiiiiiiiiiiiiiiiiiiiii"
t0044="::::::::::::::::::::::::::::::::   dppppppfpphhphhffppgggggpppppppp pppggppgggppgpggggpgspppgggpgggffggppggffhhhmmm iiiiiiiiiiiiiiiiiiiiiiii"
t0045="::::::::::::::::::::::::::::::::     pggggpppphhphhhppgggggffsppggpp ppppggpggpgppgggggppffpggggggggfggpggfhhhhhhmiiiiiiiiiiiiiiiiiiiiiiiiii"
t0046="::::::::::::::::::::::::::::::::     ddggggggppppphpppgggggpfspfggppp pppggppppggpggggppppfpgggggggfgffgphphhhmmhmiiiiiiiiiiiiiiiiiiiiiiiiii"
t0047=":::::::::::::::::::::::::::::::::         pgggfpffpppppgggpgppppggppppsppggpgggggppppggpppppgggggggggfppphhhhhmhmii:::::::::::::iiiiiiiiiiii"
t0048=":::::::::::::::::::::::::::::::::         pgggggpppppppgggpgggppggggppp ppppggggpppppggggpggggggggggggppgghhhhmiii:::iiiiiiiiiiiiiiiiiiiiiii"
t0049=":::::::::::::::::::::::::::::::::   gp    ppppppppggggggggpgggppppggggp  pppppppppppppppppggggggggggggppphhhhmhiii::iiiiiiiiiiiiiiiiiiiiiiii"
t0050=":::::::::::::::::::::::::::::::::    p djp   pppppggggggpggpfppgggggpgpp  pppppppppppppffffppgggggggpppgghhmmiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii"
t0051=":::::::::::::::::::::::::::::::::      dppppp   ppppppggpggppppggpphhfggpp ppppppppgggppppppggggggggggppgghmmiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii"
t0052="::::::::::::::::::::::::::::::::::      pppppppp  ppppppgggppppggppppfghhp  hpphpppgggpgpppppggggggggppphhhhmiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii"
t0053="::::::::::::::::::::::::::::::::::        ppffppp  pppppppgggggggppfhfggfhpp  pppppppppggpgggggpgggggppphhhpmii::::iiiiiiiiiiiiiiiiiiiiiiiii"
t0054=":::::::::::::::::::::::::::::::::::        jppppppp   ppppggggggppfppffgffhpp  phpppppppppgggggpppggggpgpggpm     ::iiiiiiiiiiiiiiiiiiiiiiii"
t0055="::::::::::::::::::::::::::::::::::::   d    pjpppppppppppppggggggggphpmphpphhpp  phhpppppppppppppgggpppppgghp   mmi:::iiiiiiiiiiiiiiiiiiiiii"
t0056=":::::::::::::::::::::::::::::::::::    dpp   jppppffpppfpppppppggggppmmhhpfpfhfph pppppppppppppppgggppppppphhp  mmmii:::iiiii::::::::iiiiiii"
t0057=":::::::::::::::::::::::::::::::::::   djppp    ppppffpfffffpppppgggpspffpmfphpphgp ppppppppppppppggppppppppphhmmmmimiii::i::::iiiiiiiiiiiiii"
t0058=":::::::::::::::::::::::::::::::::::   dpjjpp    ppppppppfffppgpggpppspmpfpfffmmggg ppppppppppppppggfpgpfpffppggpmmmiiiii:::iiiiiiiiiiiiiiiii"
t0059="::::::::::::::::::::::::::::::::::    dfppppp    ppppppppppppggggpspfffmmfpfhggpfg ppppppdddppppgg    ppppppggghhmamiiiiiiiiiiiiiiiiiiiiiiii"
t0060="::::::::::::::::::::::::::::::::::    dffsjjp    ppppdddpppppggppp ppffpmpmpmgpfmg ppmpppdpddppgg gggg       ppmmmamiiiiiiiiiiiiiiiiiiiiiiii"
t0061="::::::::::::::::::::::::::::::::::   ddffsjpppp   ppdpddppppppppp  ppfmpffffggfppg pfpphpphppgg   ggpppppfggggghhmmmiiiiiiiiiiiiiiiiiiiiiiii"
t0062="::::::::::::::::::::::::::::::::::   d ffspppppp  pppppp pppppps  pppppppphgggpmg  pfhfppddppg gggpjffjpjffffggphmmiiiiiiiiiiiiiiiiiiiiiiiii"
t0063=":::::::::::::::::::::::::::::::::    d pfjjjpjppp       p    ps ppggffmggfppggmfg ppphffpdpppg ggffjpppppppppgghmmmmiiiiiiiiiiiiiiiiiiiiiiii"
t0064=":::::::::::::::::::::::::::::::::    dppfjpppppppp pppppppppp  pppgghppfgfhfpmhggp  pfhpppppgp ggfjppdddddpggggghmm iiiiiiiiiiiiiiiiiiiiiiii"
t0065=":::::::::::::::::::::::::::::::::   dp pfffpjpdddps   pppppppppppppmhfmmgfmpfphgmmp pppfpfphggg gjpppdddddpggghhmma iiiiiiiiiiiiiiiiiiiiiiii"
t0066=":::::::::::::::::::::::::::::::::   pfpfppppppppdppsp    ppddppppppghfpmgpmffffgpppppppfppppgg  gffpdpdppdpgggmmhhmmiiiiiiiiiiiiiiiiiiiiiiii"
t0067=":::::::::::::::::::::::::::::::::     pfjfpjppppdddpppppp ppddddppggfpmpgfmmphgghffmmppddfppgg gdfjpdpddpppdgghhhpmmmm iiiiiiiiiiiiiiiiiiiii"
t0068=":::::::::::::::::::::::::::::::::   fffffffpppppdddppppppp pppddppppppphghpmhpmmppfphhpdddpdgg ggjfpppddpppdgghhhhhmammiiiiiiiiiiiiiiiiiiiii"
t0069=":::::::::::::::::::::::::::::::::   fjfpffffppppdddpppfppdp   ppppppmpmpmhmggfhhffhphhffjddddg gpgpddppppppppggggmhmmmmiiiiiiiiiiiiiiiiiiiii"
t0070=":::::::::::::::::::::::::::::::::   ffpffpfjffffpppdpddppdddp  pppppppmffppmmffpppfjpppjpddddg  gfjppppdppddpddggpmhmmhiiiiiiiiiiiiiiiiiiiii"
t0071=":::::::::::::::::::::::::::::::::   ffpppppffjjjpppppddpppddddp ppppppppphpmphpfhpfppppppdddggg ppppfppdppddpddggmphmphhiiiiiiiiiiiiiiiiiiii"
t0072="::::::::::::::::::::::::::::::::    ddpppppffffjjfpppdpdpdddddp ppppppphpffffjpfppjppddpdpppgg   ppppppppppppdppgpgmphhhttiiiiiiiiiiiiiiiiii"
t0073=":::::::::::::::::::::::::::::::     ddpppppppppffffppppppppppp  pdpppppppjpppjphjpphpddpppppg  p pp   pppppppdpppppppfpddptiiiiiiiiiiiiiiiii"
t0074="::::::::::::::::::::::::::::::   d ddpppppppppppfffppppfppppp  pppppppppppppmphpppppppppppppp pdd d   dpppppppppppffjpjfddtiiiiiiiiiiiiiiiii"
t0075="::::::::::::::::::::::::::::::   dddpppppppppppppppppppppppp ppppppppdppppppppppppppppppppppdddd  d   ddddppppppjjppjffddd iiiiiiiiii:iii:::"
t0076="::::::::::::::::::::::::::::::   dddppppppppppppppppppfppppppppppppppddpdddpppppddppppppddddd  dd dd dd  dpppppfjjjffdd    :::::ii::::ii::::"
t0077="::::::::::::::::::::::::::::::   dddppppppppppppppppppppppppppphppppppppdddpdpppppppppdddd      d        dpppppfjpdddd     :::::::::::::::::"
t0078="::::::::::::::::::::::::::::::   dddppppppphpppppppppppppppppmphphpppppppddpdpppppppdddd                 ddddddjddd       :::::   ::::::::::"
t0079="::::::::::::::::::::::::::::::     dpphhmhpmhppppppppppppphhmmmmmphhhpfpfppppppppffpddd    :::     ::::   ddddddddd pp  ::::::     :::::::::"
t0080=":::::::::::::::::::::::::::::::   ddpppmmmmmmhppppppppppppmmmmmmmmmhphhphpffppppfjpddd    :::::::::::::     dddddd      :::::   p  :::::::::"
t0081="::::::::::::::::::::::::::::::::   ddmmiiimmmmmmpphphpppppmmmiiimmmmmmmmphhjjpppjpdd     ::::::::::::::::               ::::    h  :::::::::"
t0082="::::::::::::::::::::::::::::::::::  dmmiiiiimmmmhmmhhmmhhpmmmiiiimmmmmmmmmhhjjjpddd     ::::::::::::::::::          ::::::    pgp  :::::::::"
t0083=":::::::::::::::::::::::::::::::::::::iiiiiiiiiimmmmmmmmmmmmmmmiiiimimimmmmmmhfjpp     ::::::::::::::::::::::::::::::::::::  pppgg  :::::::::"
t0084=":::::::::::::::::::::::::::::::::::::iiiiiiiiiiimmimiimmmimaamiiiiiiiiimammmmhjjpd   ::::::::::::::::::::::::::::::::::::   ppghg  :::::::::"
t0085=":::::::::::::::::::::::::::::::::::iiiiiiiiiiiiiiiiiiiimimmmmmiiiiiiiiimmmmmhhpjjd   ::::::::::::::::::::::::::::::::::::   pghhg  :::::::::"
t0086=":::::::::::::::::::::::::::::::::::iiiiiiiiiiiiiiiiiiiiiiiiifiiiiiiiiiimmamammhpjd   ::::::::::::::::::::::::::::::::::::   ppgjj  :::::::::"
t0087=":::::::::::::::::::::::::::::::::::iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiimmmmmmmmpd  :::::::::::::::::::::::::::::::::::::   pppgg  :::::::::"
t0088="::::::::::::::::::::::::::::::::::iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiimmiiiiiip :::::::::::::::::::::::::::::::::::::::   pppp  :::::::::"
t0089=":::::::::::::::::::::::::::::::::::iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii::::::::::::::::::::::::::::::::::::::::::    p  :::::::::"
startpos_count=27
startpos={"x","y","exclude","nations"
107,53,FALSE,"Swiss"
19,26,FALSE,"Welsh"
37,38,FAL
```

## 策划参考价值
SLG历史场景/战役剧本的数据结构参考。
