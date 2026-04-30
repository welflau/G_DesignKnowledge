# 文明 · 历史场景「earth-large」

> 来源：longturn/freeciv21
> 原始链接：https://github.com/longturn/freeciv21
> 分类：gameplay
> 标签：文明, 4X策略SLG, 历史场景, 剧本
> 游戏类型：4X策略SLG

## 概述
Freeciv历史场景脚本：earth-large

## 正文
```sav

[scenario]
game_version=3000000
is_scenario=TRUE
name=_("Earth (classic/large)")
authors=_("Map: Daniel Gudlat, Daniel Markstedt\nStart positions: Jason Dorje Short, Mateusz Stefek, Mathieu Roy, David Fernandez, Rhue")
description=_("Overhead 160x90 map of the Earth.")
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
random_seed=1586958160
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
"aifill",32,32
"alltemperate",FALSE,FALSE
"flatpoles",100,100
"generator","SCENARIO","SCENARIO"
"landmass",30,30
"mapseed",0,0
"mapsize","FULLSIZE","FULLSIZE"
"maxplayers",91,91
"metamessage","Scenario: Earth(Large)",""
"naturalcitynames",FALSE,FALSE
"revolentype","RANDOM","RANDOM"
"separatepoles",TRUE,TRUE
"singlepole",FALSE,FALSE
"size",4,4
"startcity",TRUE,TRUE
"startpos","DEFAULT","DEFAULT"
"steepness",30,30
"teamplacement","CLOSEST","CLOSEST"
"temperature",50,50
"tilesperplayer",100,100
"tinyisles",FALSE,FALSE
"topology","WRAPX","WRAPX"
"victories","",""
"wetness",50,50
"xsize",160,160
"ysize",90,90
}
set_count=26
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
t0000="aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
t0001="  aaaa      aa    aaaaaa    aa    aa        aaaaaaaa        aaaa      aaaaaa      aa      aa  aa      aa    aa        aa            aa    aaaa              aa  "
t0002="               ::        ::    ::    ::::::          ::::::      ::::        ::::    ::::        ::::    ::    ::::::    ::::::::::    ::      ::::::::::::     "
t0003="             ::::::::::::::::::::::::::  :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: "
t0004="                   :::::::::::::::::::    :::::::::::::   ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::  "
t0005="                    ::::::::::::::::    t    :::::::::: t  :::::::::::::    :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::         "
t0006=" aaaaaaaaaaaaaa      :::::::::::::::   ttt     :::::::       :::::::::    t   ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::       aaaa   "
t0007="aaaaaaaaaaaaaaaaa     :::::::::::::::  t t        ::::          :::::      t       :::::::::        :::::::::::::::::::::::::::::::::::              aa aaaa   a"
t0008="aaaaaaaaaaaaaaaaaa     :::::::::::::::            ::     tta      :::                 ::::    tt       ::::::::::::::::::::::::::::             t    tataaa   aa"
t0009="aaaaaaaaaaaaaaaaaa     :::::::::::::::                  tp                tttttt       ::              :::::::::::::::::::::::::        t  t          t at    ta"
t0010="aaaaaaaaaaaaaaaaat     :::::::::::::::::               tp               ttpptttttt      :               :::::::::::::::::::::::     tt                        tt"
t0011="tttaaaaaaaaaaaaaat    :::::::::::::::      tttt        pp     tt     tttttppttttt                              ::::::::::::::      tt    t     p  t   ttt      t"
t0012=" tttaaaaaaaaaaaatt  :::::::::::::       pptttttttt           ttt tttttttttfffftt   ttt        ttttt              :::      ::           tttt                     "
t0013="  tttaaaaaaaaaatt  ::::::              gppptpppttttt      ff ppt ttttfttftffffttffttttttt   tttftftttt           :::                   tppt           t a       "
t0014="   tttaaaaaaaatt :::  ::   h          pphgffggpppttt   pttffffpggpptfftttffffffffffgggpfffffffffffpppttttttt     ::  ttt        tttt                  tttta     "
t0015=":   tttaaaaaatt  :t    :       h     gphhgffggppppt   tttffffffggggpffffffffffffffpgggpfffpffffffffpppttpttttt    : ttttttttttttttttt           tttt    ttaa    "
t0016="::   tttaaaatt  :: tft       h      gghpff ggg+fpp  ppffffhhfffgppggfffffffpffffffppppppffffggffffffffffgpptpptttt:  ttptttpttpttttpttttttttpttttttp p    ptaa  "
t0017=":::   ttaaatt  ::: gg      hhh     hgmhpf   ggffppppppffffhfffggggpgffffpffffffffffpppppffffpgfffffpffffggppppttt :: tttttptttttttppttptttttttttttpp       paaa "
t0018="::::  ttaatt  ::::          pg    ffhhfg    g+f+ffpffffffhfffgggppggpfffffgppffpffffpppfffffffppffffffffffffpp    : ttttttttttppffffffppttpttttppp   p    pptp  "
t0019="::::  ttttt  :::::::::  gg  gp    ffggg    gggffffffpfffhmffggggppgpppffffgfffffffffpppffffffffpffffffffffff   :::: ttpptpttttppfffffffptpppttttp            pt "
t0020=":::::  ttt  :::::::::: fpg  ff     gggg      gffppggppffhmffggggssffppgfffffffffpffpppppffpffgffffgggg  ff   :::::   tppptttppfffffgpfffffffppttpt              "
t0021="::::::  tt ::::::::::  hg  hff       g    ggggffggpgggffhmfffggggpgfppggffffffffpppppfppffffffffffgg    ff :::::      tpppttpfffffffffffffffppttppp        tpp  "
t0022=" ::::::    ::::::::::     gpggg    g      ggffffgpgggfpfhmffffggggpgpppppffpffgggpgpffffffffgggggg     fhh ::::::  pppp p   ppggppffppffffffffffppppttp  t tp   "
t0023=" :::::::::::::::::::::   gsgggg    gg   ggggfffggggggffffhfffgggggggpfggppffffggg+ggffffffffggg        phh ::::::              gppffgpfffgfffpfffpppttp  pttppp "
t0024="  ::::::::::::::::::::          ggggpppgggffffggffggggppffhfggffffggffffgffffffffgpppppppppgg          hpp  ::::::       :::::    ggffffffffffgfffppptttttppfffg"
t0025="p  :::::::::::::::::::   ggggggggggggpppggffffggffggggppfffhggffffggffffggffffffggppppppppgggg    p     p   :::::::::::::::::::::  ggffffffffffffffpppttttpfffff"
t0026="pp  :::::::::::::::::::    ggpggggpgggggggggffgpggppggggpppppggggpppppppggffpppgggppdpppppppppgg  p        :::::::::::::::::::::::  pphhfffggfffffffffppggffffff"
t0027="p     :::::::::::::::::    gpgggghghhgggggggffgggpppggppppppppggpppppppppgfgppppgpppddppppppppgg  p      :::::::::::::::::::::::::  pphhffggggfffgffffppggfffffg"
t0028="  pp   :::::::::::::::     ggggghmmmhhggpppppfggppppppp ggpppddddpgpppgpppgppppdddddppggppppggg        :::::::::::::::::::::::::::  ggffhhggggppgpgpp+pfffpppf  "
t0029="  pp    :::::::::::::     ghggppgghghhggppgppg  ppgppp  ggpp pddpppgppppppppppdddpddppggppppgg    pp  :::::::::::::::::::::::::::: gggffhhppgppppppp+++f++ggggg "
t0030="       :::::::::::::: ggppppmg    hg   gppppgg  gp pgg pppppddppppppppgpppgpppddddppggppggggg    ghg  :::::::::::::::::::::::::::  fgpgghhggggppggppggg+ggggggff"
t0031="f   ::::::::::::::::: ggppppph    gh    pppggg      gg  pppppdpgppppppgppppppppddpppggppgggg         :::::::::::::::::::::::::::: ffggghmhgggggggggpgpg+gggpgggf"
t0032="   :::::::::::::::::: ppphppg      gh   ggpgp       gg   ppppppppppgppppppppgpppppg   gggg     pm  :::::::::::::::::::::::::::::: fgpghhmmhgppggggpgggggffggggf "
t0033="  :::::::::::::   :::  ppppp     h  gh  ggp  gppggppgg   pppgppppppppppppppppgppppgg   gg      pm  :::::::::::::::::::::::::::::: ffgphhmmhgppgggggggpggpfgggg  "
t0034=" :::::::::::::  g :::: hppp      g  g g gg  pgffppppppppppppppgphhhhppppgggpppppppgg   gg   gpmhp ::::::::::::::::::::::::::::::: fggghhmhpppggggggggggghhgg    "
t0035=" ::::::::::::::   ::::             gp    g  ggffppppppppppgpppgghhhhhpppggggppppppgg       gppmg  ::::::::::::::::::::::::::::::: pfpghhhpppppgggggggpghhggg    "
t0036=":::::::::::::::::::::  hgggggggg              pppppppppppphhphhhhhhhhhppggggpppppgggg      g     ::::::::::::::::::::::::::::::::  fggppppppggggppgggghhgg     :"
t0037=":::::::::::::::::::   gggppppgggg             pppppppppppppphhhhmmmhhmhhggggpppggpggg        :::::::::::::::::::::::::::::::::::::  gggppphppgggppggghhgg    :::"
t0038="::::::::::::::::::  ppgppphhhhppgggg   ggggpppppppddpp   ppphhmmmmmmmmhhpgggggggpppggg       ::::::::::::::::::::::::::::::::::::::  pggpppddpppgggggggg   :::::"
t0039=":::::::::::::::::  ppppppdddddphhppgggggggpgppppppdddp    pphhhhhmmmmmhhppggggggpgppgg      :::::::::::::::::::::::::::::::::::::::: gpggppdddppgggggggg  :::   "
t0040="::::::::::::::::: pddppdddddddddddpppppppppp  pddddddddp    ggghhhhhmmhhhggggppggggggg     ::::::::::::::::::::::::::::::::::::::::: pgggpddddppg     gg :::: g "
t0041="::::::::::::::::: pppdddddddpddddddpppdpppppp   ddpdddddd    gggghhhhhhhgggpgpppggggg      :::::::::::::::::::::::::::::::::::::::::  gg ppdddpg      jg  :::   "
t0042="::::::::::::::::: ppdddpddddddddddddddddpppdpp   dpddddddpdp  pggppgghhggggpppggggg       :::::::::::::::::::::::::   ::::::::::::::: pp  gpdppg       gs  :::::"
t0043="::::::::::::::::: ppddddddpdppdddpdddddpppddppp   pddddddddd  ppggggggggggggpgggg    g    ::::::::::::::::::::::::  h   ::::::::::::: pp  gpppgg  fj         :::"
t0044="::::::::::::::::: ppddddppppppppddppdddddppddddd   pdddddp     ghgffgg    ggggg   ::     ::::::::::::::::::::::::::   g  ::::::::::::  pp  ggggg  ff   ppp     :"
t0045="   :::::::::::::: ppppppppppppppppdpdddddpppddddp   ppdd   ::  gphffgg    ggg  :::: gg  ::::::::::::::::::::::::::::     :::::::::::::      gggggggj ::  gpp    "
t0046="gp :::::::::::::: ggggppppppppppppppddpdppppppddpp  p    ::::   phggg     jggp :::: pg  :::::::::::::::::::::::::::::::::::::::::::::::::::   ggjpgg ::   pggp  "
t0047="    ::::::::::::: ggggpppppgpgppppppgpdpppppppddpdp   d  :::::  phfg      jjpp :::: j    :::::::::::::::::::::::::::::::::::::::::::::::::::  ggppgg  :::       "
t0048=": g :::::::::::::  pppggppgpgpggggggppppggppppdddpppddd  :::::  phgg      g ss ::::    j ::::::::::::::::::::::::::::::::::::::::::::::::::::    gjpg   ::::::::"
t0049=":   ::::::::::::::  ppggppggggggggggppgpggghgppddddpdd  :::::::  pg       g     ::::      :::::::::::::   ::::::::::::::::::::::::::::::::::::::  ppgg   ::    :"
t0050="   ::::::::::::::::   ppffjjffffffgggfggfffhhhppddpdd  :::::::::    p     gg           jp ::::::::::::: g :::::::::::::::::::::::::::::::::::::::   ggpp    gg  "
t0051="g   :::::::::::::::::   ffjjff  ffggffggpfhhmmppddpp  :::::::::::: pg   p  g      gg   pg :::::::::::::   ::::::::::::::::::::::::::::::::::::::::: g  g  gggg g"
t0052="ggg   :::::::::::::::::         ggffjjjjffhhmhgppp   :::::::::::::    : jg       ppf      :::::::::::::::    ::::::::::::::::::::::::::::::::::::::    gpgggfffg"
t0053="ggggg  :::::::::::::::::::::::: ggjjfgfjffhhmhgppp ::::::::::::::::::::  gp    pjjpf      :::::::::::::::: j :::::::::::::::::::::::::::::::::::::::::  ggggfgjj"
t0054="jfffgg    ::::::::::::::::::::: gggfffjffghhp+gggg :::::::::::::::::::::  gpf   jgg         ::::::::::::::   ::::::::::::::::::::::::::::::::::::::::: ghhgpgggg"
t0055="jjffggggg    :::::::::::::::::: gggggg+jjhhhpggpgg ::::::::::::::::::::::  jf        gj   g       ::::::::::::::::::::::::::::::::::::::::::::::::::: gghhhggggg"
t0056="jgjfggppffgg  :::::::::::::::::  gggggjjjjjjgppgf  :::::::::::::::::::::::           g g  gggjpfg :::::::::::::::::::::::::::::::::::::::::::::::::: ggghhpgjjjj"
t0057="jjgjpjjpffggp  ::::::::::::::::: gggggjjjjjjggggg :::::::::::::::::::::::::: gg         ::   gfjgg   ::::::::::::::::::::::::::::::::::::::::::::::: ggghhpgjjjj"
t0058="jjggjjffffgggg  ::::::::::::::::  gggpfffgggffgg   :::::::::::::::::::::::::  ggg  g  g ::::  fg gpp   ::::::::::::::::::::::::::::::::::::::::::::: ggghhfffffj"
t0059="jjgjjjjfffgggpp ::::::::::::::::: ggppffpgggffff     ::::::::::::::::::::::::           :::::               ::::::::::::::::::::::::::::::::::::::::  gghhfffjjf"
t0060="jgjjjjffgggggpp ::::::::::::::::  ggppppgggghhff   g ::::::::::::::::::::::::::::::         ::  g   ::::  g  ::::::::::::::::::::::::::::::::::::::::  ggghhfffj"
t0061="fggffffpggggpp  :::::::::::::::: pgpppppgggghhff  gg :::::::::::::::::::::::::::::      gggg    gg   ::::  g :::::::::::::::::::::::::::::::::::::::::  gghhfpfj"
t0062="ffffgggggpggp  ::::::::::::::::  pppppgggppggf   ppf :::::::::::::::::::::::::::       ppppggg  ggg   :::      :::::::::::::::::::::::::::::::::::::::: ggggmmgg"
t0063="pffpggggppgg  :::::::::::::::::  dpppppgppgggf   ffp ::::::::::::::::::::::::::       pppppppgggggg   ::        :::::::::::::::::::::::::::::::::::::::   ggmmgg"
t0064="ggggggpppggg ::::::::::::::::::   ddpppppppggf   gg  ::::::::::::::::::::::::       ppdddddpppggffg       p     :::::::::::::::::::::::::::::::::::::::::  gppdd"
t0065="gggggpppgggg :::::::::::::::::::  ddpppdppgggf  pp  :::::::::::::::::::::::::    pppppdddddddppgffg             ::::::::::::::::::::::::::::::::::::::::::  ppdd"
t0066="pgggppfffff  :::::::::::::::::::   ddpdddpppgg    :::::::::::::::::::::::::::   ppddddddddpddddpgfff    ::      ::::::::::::::::::::::::::::::::::::::::::: gghp"
t0067="ppggppfgff  :::::::::::::::::::::  dpppdddpgg  :::::::::::::::::::::::::::::::  ppdddddpddddddppppfff  :::      ::::::::::::::::::::::::::::::::::::::::::: ghhh"
t0068="pppgpfffp  ::::::::::::::::::::::   ppppppggf  ::::::::::::::::::::::::::::::    gpddddddddpddppppppgg :::      ::::::::::::::::::::::::::::::::::::::::::: phmh"
t0069="pppppfff   :::::::::::::::::::::::   pppppgg  :::::::::::::::::::::::::::::::::   ppddpdddddddppppppgg ::::     ::::::::::::::::::::::::::::::::::::::::::: ppmh"
t0070="pppppggg   :::::::::::::::::::::::   ggg      ::::::::::::::::::::::::::::::::::  gpddddppppppppppggg  ::::     ::::::::::::::::::::::::::::::::::::::::::: ghmh"
t0071="ppppgggf   ::::::::::::::::::::::::      ::::::::::::::::::::::::::::::::::::::: ggpppddpppppgppppgg  ::::::    ::::::::::::::::::::::::::::::::::::::::::: ghmh"
t0072="ppggggg   :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: gppgg      ggggggg  ::::::     ::::::::::::::::::::::::::::::::::::::::::: phhg"
t0073="ppgggg    ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::             gg gg  ::::::   gh  :::::::::::::::::::::::::::::::::::::::::  phgg"
t0074="ppggg     ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::     :::::       ::::       gg   ::::::::::::::::::::::::::::::::::::::  phmpd"
t0075="ppgggg    ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::  ff :::        gg       ::::::::::::::::::::::::::::::::::  phmdd"
t0076="ppgg     :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: gg :::     ph p           :::::::::::::::::::::::::::::::  pggpp"
t0077="ppg     :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::    ::::   php              :::::::::::::::::::::::::::::  ppggpp"
t0078="gg     ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::  pgg               :::::::::::::::::::::::::::::  ggpppp"
t0079="g     ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: ppg             :::::::::::::::::::::::::::::::::  gpppp"
t0080="      :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
```

## 策划参考价值
SLG历史场景/战役剧本的数据结构参考。
