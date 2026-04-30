# 文明 · 历史场景「tutorial」

> 来源：longturn/freeciv21
> 原始链接：https://github.com/longturn/freeciv21
> 分类：gameplay
> 标签：文明, 4X策略SLG, 历史场景, 剧本
> 游戏类型：4X策略SLG

## 概述
Freeciv历史场景脚本：tutorial

## 正文
```sav

[scenario]
game_version=3000000
is_scenario=TRUE
name=_("Freeciv21 Tutorial")
description=_("Play this tutorial scenario to get an introduction to Freeciv21. This is intended for single-player games. It uses the default (civ2civ3) rules.")
save_random=FALSE
players=TRUE
startpos_nations=FALSE
lake_flooding=TRUE
handmade=TRUE
ruleset_locked=TRUE

[savefile]
options=" +version3"
version=40
reason="Scenario"
revision="3.0.0-alpha3+"
rulesetdir="civ2civ3"
improvement_size=73
improvement_vector="Airport","Aqueduct","Aqueduct, Lake","Aqueduct, River","Bank","Barracks","Barracks II","Barracks III","Cathedral","City Walls","Coastal Defense","Colosseum","Courthouse","Factory","Granary","Harbour","Hydro Plant","Library","Marketplace","Mass Transit","Mfg. Plant","Nuclear Plant","Offshore Platform","Palace","Ecclesiastical Palace","Police Station","Port Facility","Power Plant","Recycling Center","Research Lab","SAM Battery","SDI Defense","Sewer System","Solar Plant","Space Component","Space Module","Space Structural","Stock Exchange","Super Highways","Supermarket","Temple","University","Apollo Program","A.Smith's Trading Co.","Colossus","Copernicus' Observatory","Cure For Cancer","Darwin's Voyage","Eiffel Tower","Great Library","Great Wall","Hanging Gardens","Hoover Dam","Isaac Newton's College","J.S. Bach's Cathedral","King Richard's Crusade","Leonardo's Workshop","Lighthouse","Magellan's Expedition","Manhattan Project","Marco Polo's Embassy","Michelangelo's Chapel","Mausoleum of Mausolos","Statue of Zeus","Temple of Artemis","Pyramids","Internet","Shakespeare's Theatre","Statue of Liberty","Sun Tzu's War Academy","United Nations","Women's Suffrage","Coinage"
technology_size=88
technology_vector="A_NONE","Advanced Flight","Alphabet","Amphibious Warfare","Astronomy","Atomic Theory","Automobile","Banking","Bridge Building","Bronze Working","Ceremonial Burial","Chemistry","Chivalry","Code of Laws","Combined Arms","Combustion","Communism","Computers","Conscription","Construction","Currency","Democracy","Economics","Electricity","Electronics","Engineering","Environmentalism","Espionage","Explosives","Feudalism","Flight","Fusion Power","Genetic Engineering","Guerilla Warfare","Gunpowder","Horseback Riding","Industrialization","Invention","Iron Working","Labor Union","Laser","Leadership","Literacy","Machine Tools","Magnetism","Map Making","Masonry","Mass Production","Mathematics","Medicine","Metallurgy","Miniaturization","Mobile Warfare","Monarchy","Monotheism","Mysticism","Navigation","Nuclear Fission","Nuclear Power","Philosophy","Physics","Plastics","Polytheism","Pottery","Radio","Railroad","Recycling","Refining","Refrigeration","Robotics","Rocketry","Sanitation","Seafaring","Space Flight","Stealth","Steam Engine","Steel","Superconductors","Tactics","The Corporation","The Republic","The Wheel","Theology","Theory of Gravity","Trade","University","Warrior Code","Writing"
activities_size=21
activities_vector="Idle","Pollution","Unused Road","Mine","Irrigate","Fortified","Fortress","Sentry","Unused Railroad","Pillage","Goto","Explore","Transform","Unused","Unused Airbase","Fortifying","Fallout","Unused Patrol","Base","Road","Convert"
specialists_size=3
specialists_vector="elvis","scientist","taxman"
trait_size=3
trait_vector="Expansionist","Trader","Aggressive"
extras_size=38
extras_vector="Irrigation","Mine","Oil Well","Oil Platform","Pollution","Hut","Farmland","Fallout","Fort","Fortress","Airstrip","Airbase","Buoy","Ruins","Road","Railroad","Maglev","River","Gold","Iron","Game","Furs","Coal","Fish","Fruit","Gems","Buffalo","Wheat","Oasis","Peat","Pheasant","Resources","Ivory","Silk","Spice","Whales","Wine","Oil"
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
meta_patches=""
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
warminglevel=3
nuclearwinter=0
cooling=0
coolinglevel=3
random_seed=1586960583
global_advances="1000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"
save_players=FALSE

[random]
saved=FALSE

[script]
code=$
function has_unit_type_name(unit, utype_name)
  return (unit.utype.id == find.unit_type(utype_name).id)
end
function has_tile_terrain_name(tile, terrain_name)
  return (tile.terrain.id == find.terrain(terrain_name).id)
end

function tutorial_turn_callback(turn, year)
  if turn == 1 then
    notify.event(nil, nil, E.SCRIPT,
_("Welcome to Freeciv21. You are the vaunted leader of a civilization. Your task is to take your nation down the path of power and glory! If this is your very first time playing Freeciv21, it would be good to take some time to read the in-game help. There is a lot of good content in there to help get you started, especially the Help -> Strategy and Tactics section. When ready, click the \"Turn Done\" button on the bottom-right and we will walk you through some more introduction items before you really get going."))
  elseif turn == 2 then
    notify.event(nil, nil, E.SCRIPT,
_("Turn 2: You start this tutorial scenario with five units: Explorer, Settlers, two Workers, and Warriors. You should see each of them arrayed on the map. Some units may be stacked on top of each other. You will see a yellow plus (+) sign if this is the case. Clicking on a unit will cause it to be selected and information about the unit and the terrain it is on will show up in a controls bar at the bottom of the game window. To move a unit you can press G and point at the destination with the mouse. If you want to move some units now, move any of them except the Settlers. The Settlers is special as we will discuss shortly. You might consider placing two units on top of each other in a stack. There is something important there to learn. When ready, click the \"Turn Done\" button again so we can talk more about your initial units and get you started."))
  elseif turn == 3 then
    notify.event(nil, nil, E.SCRIPT,
_("Turn 3: Explorers are used to explore the map and open it up from the \"Unknown\". With more than one move point each turn, they do the job really well. Settlers are used to build cities, which is a major component of Freeciv21. Workers are used to improve the land with tile improvements such as irrigation. Refer to the Help -> Terrain topic. Lastly, Warriors are a really cheap early military unit that can be used for basic defense of your cities as well as attacking your enemies. Refer to the Help -> Units topic. First, start by moving your Settlers to a grassland or plains tile and move your Explorer around the map to open it up some. Pro tip: Middle-click on a tile to get a pop up window providing more information. When ready, click the \"Turn Done\" button again so we can talk about the various user interface elements of the game."))
  elseif turn == 4 then
    notify.event(nil, nil, E.SCRIPT,
_("Turn 4: Freeciv21 has a collection of views to help you as you play. The Map View (F1) is where you see the map and all your beautiful cities and units arrayed. The Units Widget (F2) shows you all the units you have and also which are being constructed. The Nations View (F3) shows you information about your enemies. This is where diplomacy comes in. The Cities View (F4) gives details on your cities. More about this later. The Economy View (F5) gives information about all the buildings (also known as city improvements) in your civilization and how much it costs in gold per turn in upkeep. Lastly, your civilization grows and operates with gold, science (bulbs) and luxury goods. Clicking the button on the top bar showing these icons brings up a dialog allowing you to change the allocation of these important resources. When ready, click the \"Turn Done\" button again so we can talk more about user interface elements."))
  elseif turn == 5 then
    notify.event(nil, nil, E.SCRIPT,
_("Turn 5: You may have noticed a widget on the main map view that shows these messages. This is called the messages window. If you do not see the messages window, then click the button for it on the top bar. As varying events occur during the game, messages will appear in this window. These messages are stored there as well as other events such as the building of a city, city growth or the construction of something inside of a city. You may resize it by dragging the left side out and the bottom down."))
  elseif turn == 6 then
    notify.event(nil, nil, E.SCRIPT,
_("Turn 6: You may have noticed another widget on the main map wiew that shows other information. This is called the chatline/server messages window. As varying events occur during the game, messages may appear in this window. You may resize it by dragging any of the edges. You may minimize it and also move it by left-clicking the plus (+) symbol and draging it to another spot. Refer to the Help -> Chatline topic."))
  elseif turn == 20 then
    notify.event(nil, nil, E.SCRIPT,
_("Turn 20: At this point you have probably used your Explorer to find out a lot more about the map around you. You may have even found a neighbor who initiated an initial diplomatic agreement of \"Cease-fire\". The Artificial Intelligence in Freeciv21 will go straght to cease-fire at contact."))
  elseif turn == 40 then
    notify.event(nil, nil, E.SCRIPT,
_("Turn 40: At this point you probably have a few cities to work with. Hopefully you have explored all of the views and other screens of information available to you. The map should be opened up even more with your Explorer so you can see all the prime spots to place future cities. One user interface item we have not talked about yet is the minimap. If you do not see a small map on the lower right of your screen you can activate it from the View Menu and then select Minimap. The minimap can be used to quickly get around the main map by right-clicking in the window with your mouse and the main map will quickly scroll to that spot. Something similar can be used for units. When a unit is active it will show in a controls bar at the bottom of the screen, but you may not see it in the map. Left-click on the unit image in the controls bar and the main map will quickly scroll to the unit and center him in the screen. Do not stop playing! More tips to come."))
  elseif turn == 60 then
    notify.event(nil, nil, E.SCRIPT,
_("Turn 60: Congratulations. At this point in this scenario you should have seen just about everything. You should now effectively understand all the major game concepts. Freeciv21 is a game of managing scarce resources; building and managing cities; learning new technologies; keeping your citizens happy and content; governing with more and ever stronger forms of government; keeping your cities safe from invaders; and eventually conquering other nations. In most AI based games (a human player against many computer run players), the goal is to conquer all of your enemy cities and rule the entire world. Good luck. There is one more message at turn 100."))
  elseif turn == 100 then
    notify.event(nil, nil, E.SCRIPT,
_("Turn 100: One hundred turns! This should be the last turtorial message. We have discussed 5 cities worth of growth and all of the user interface elements. There have been notes about military units, veterancy, as well as a bit of diplomacy. Lastly you should have seen messages for city sizes 1, 2, 3, 5, 8, 13, and 16. Hopefully, you were also able to build a waterborne unit such as a Trireme to see the message about that. We hope you enjoyed the tutorial and will come back for many more games of Freeciv21."))

  end
end
signal.connect('turn_begin', 'tutorial_turn_callback')

-- Check for and warn about vulnerable stacks.
function tutorial_check_stacks(tile, player)
  if not vuln_stack_warning
     and server.setting.get("killstack") == "ENABLED"
     and not tile:city() and tile.terrain:class_name() == "Land" then
    n_our_units = 0
    for unit in tile:units_iterate() do
      if unit.owner == player
         and unit:transporter() == nil then
        n_our_units = n_our_units + 1
      end
    end
    -- Do not complain about 2 units, as that is a common defensive
    -- formation: civilian plus bodyguard
    if n_our_units >= 2 then
      notify.event(player, tile, E.SCRIPT,
_("Stack kill: Outside of a city, if a \"stack\" of units on a single tile is attacked, the strongest unit defends. If that unit is defeated, ALL of the units on the tile are killed (ouch!). Therefore, it is often a good idea to spread units out, avoiding large \"stacks\" of units like this, particularly on land."))
      vuln_stack_warning = true
    end
  end
end
vuln_stack_warning = false

function tutorial_unit_moved_callback(unit, src_tile, dst_tile)
  if unit.owner:is_human() then
    tutorial_check_stacks(dst_tile, unit.owner)
    if citiesbuilt == 0
      and has_unit_type_name(unit, 'Settlers')
      and (has_tile_terrain_name(dst_tile, 'Grassland')
           or has_tile_terrain_name(dst_tile, 'Plains')) then
      notify.event(unit.owner, dst_tile, E.SCRIPT,
_("Settlers find grassland or plains: This looks like a good place to build a city. The next time this unit gets a chance to move, press (b) to build a city. In general you want to build cities on open ground near water. Food is the most important resource for any city's growth. Grassland and plains tiles provide plenty of food. Other good places for a city is on or adjacent to a source of fresh water such as a river or lake. You will be able to construct a cheap Aqueduct that way to help grow your city larger than size 8 before researching Construction."))
    end
  end
end
signal.connect('unit_moved', 'tutorial_unit_moved_callback')

citypulses = 0

function tutorial_first_city_pulse()
  if citypulses < 1 then
    citypulses = citypulses + 1
  else
    notify.event(city_builder, city_tile, E.SCRIPT,
_("First city: Now you have built your first city. The city dialog window should have opened automatically. If not click on the city to open it. Cities are a fundamental concept in Freeciv21, so you should familiarize yourself with them by playing around in the dialog. See the the Help -> Cities topic for more information. You probably want to build a military unit for defense first and then a Settlers, so as to expand your civilization further. Click on the production tab. You should notice a Warriors unit is already started. That is a good early defender. Now click the plus (+) icon to select a Settlers unit from the list of possible options. When you are done, close the city dialog. If all goes well, the city should display the Warriors production on the map view in the city bar. Note: Settlers cost 2 population to complete. Keep an eye on the city's growth rate. Pro Tip: Now that you have built a city, you need to figure out what technology to learn first. Press F6 to bring up the Research View (or click on the button on the top bar). The technology tree is an extrememly important aspect of a Freeciv21 game. Have a look at the Help -> Technology topic for more information."))
    signal.remove('pulse', 'tutorial_first_city_pulse')
  end
end

function tutorial_second_city_pulse()
  if citypulses < 2 then
    citypulses = citypulses + 1
  else
    notify.event(city_builder, city_tile, E.SCRIPT,
_("Second city: Congratulations, you have built your second city. This city will behave almost exactly like the first one. It will be slightly different because of the terrain around it, but otherwise the same. You probably want to build Warriors and Settlers here too. One of your best ways to win in Freeciv21 is to get as many cities as your form of government can support and get those cities as large as you can get them. Big cities have large production capacity, which is very important when you need to wage war against your enemies. Pro tip: Another good unit to build early is Workers so you can have them improve the terrain around the City."))
    signal.remove('pulse', 'tutorial_second_city_pulse')
  end
end

function tutorial_third_city_pulse()
  if citypulses < 3 then
    citypulses = citypulses + 1
  else
    notify.event(city_builder, city_tile, E.SCRIPT,
_("Third city: You have built your third city! Your civilization seems to be thriving. It might be time to think about a military. Pick one of the cities that has a high production rate, and turn it into a military center. Build a barracks there first, then start work on a military unit. Pick the best unit you have available. At the beginning of the game, Warriors will be the only choice, but soon you will have plenty of options. This might also be a good time to use the worklist feature of the city dialog. Select barracks and select military units one at a time to queue them up in a row to create a work list. As soon as the barracks is complete the city will automatically switch over to producing the unit. As was prescribed for the first two cities you will have built Warriors right away. In this step start thinking about better defenders for your cities. Phalanx are a good start. Read more about units in the game help under Help -> Units. Pro tip: This is where the technology tree is very important, as you need to learn newer technologies in order to build better and more powerful units."))
    signal.remove('pulse', 'tutorial_third_city_pulse')
  end
end

function tutorial_fourth_city_pulse()
  if citypulses < 4 then
    citypulses = citypulses + 1
  else
    notify.event(city_builder, city_tile, E.SCRIPT,
_("Fourth city: Another city! You are really getting the hang of this. You probably have a pretty good idea what to do with new cities by now. Take a moment to look at the bar below the city on the map view. This display shows some useful information about the city. The flag and background color indicate what nation the city belongs to (this will be useful when you meet other nations). The top segment of the bar also shows the name and size of the city, and will show one or more stars to indicate if there are units in the city. The bottom row shows what the city is building, and how long it will take; it also shows how long the city will take to grow to the next largest size. If you do not see all of this information; from the View Menu select Citybar Style -> Traditional."))
    signal.remove('pulse', 'tutorial_fourth_city_pulse')
  end
end

function tutorial_fifth_city_pulse()
  if citypulses < 5 then
    citypulses = citypulses + 1
  else
    notify.event(city_builder, city_tile, E.SCRIPT,
_("Fifth city: You should now have 5 cities! Congratulat
```

## 策划参考价值
SLG历史场景/战役剧本的数据结构参考。
