# SLG实战项目 · 罗马帝国SLG(Python)

> 来源：SPQR_SLG
> 原始链接：https://github.com/CHUA-X/SPQR_SLG
> 分类：system
> 标签：SLG, 开源项目, 系统实现

## 概述
完整SLG项目实现：罗马帝国SLG(Python)

## 正文
﻿# English introduction
SPQR_SLG, a free and open-source Python-based strategy game about the Roman Empire in a historical period. Built on Python, utilizing the pygame library. SPQR is playable on mainstream operating systems: Windows, macOS, Linux, and more.Just play!
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# 中文介绍
SPQR_SLG，一个基于Python的免费开源策略游戏，关于罗马帝国在历史时期的故事。建立在Python上，使用 pygame 库。SPQR 可以在主流操作系统上玩：Windows，macOS，Linux等。尽管玩吧！
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# 版本记录：
### 0.0.1：程序的主干
### 0.0.2：修复了一些bug
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
## P.S.:本程序灵感来源于Chris Smith的同名项目
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# 致敬名单（排名不分先后）
## Chris Handy: Programming & game design.
## Toeholds: Original map graphics
## John Schanck: Pyconsole code
## David Clark: Label text widget layout code
## Some GUI graphics taken from Ubuntu 4.10, unknown author(s)
## Some gfx taken from FreeCiv, unknown artist(s)
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# 此处另附原项目作者注意事项：
SPQR v0.3.7


Dependencies: You need the following installed on your computer to work:


Python 3       -> http://www.python.org/

Pygame       -> http://www.pygame.org/news.html

NetworkX       -> http://networkx.lanl.gov/

PyYaml         -> http://pyyaml.org/


Open a terminal and run the program spqr.py. You can run spqr.py -? to see the
command line options.


Currently, the game is not playable, but you can scroll the map and check out the GUI so far.

It's easiest to drag the map with the middle mouse down for now.

You can move units by clicking them; the game will highlight what regions you can move to.

You can also move the naval unit in the same way.

Pressing the n key will cycle around all possible units.



## 项目文件结构

```
SPQR_SLG/
  LICENSE
  README.md
  pyproject.toml
  setup.py
  dist/
    SPQR_SLG-0.0.1-py3-none-any.whl
    spqr_slg-0.0.1.tar.gz
  .idea/
    .gitignore
    SPQRPro0.0.1.iml
    misc.xml
    modules.xml
    vcs.xml
    inspectionProfiles/
      Project_Default.xml
      profiles_settings.xml
  src/
    SPQR_SLG_0_0_2/
      setup.py
      spqr.py
      music/
        prelude_in_c_major.ogg
        twopart_invention_in_e.ogg
        twopart_invention_in_eflat.ogg
      docs/
        region_graphics.txt
      scripts/
        __init__.py
        pyconsole.py
        spqr_console.py
        spqr_data.py
        spqr_defines.py
        spqr_events.py
        spqr_gui.py
        spqr_keys.py
        spqr_menu.py
        spqr_sound.py
        spqr_widgets.py
        spqr_window.py
        spqr_ybuild.py
        maps/
          __init__.py
          spqr_city.py
          spqr_map.py
        units/
          __init__.py
          spqr_unit.py
        player/
          __init__.py
          spqr_player.py
      data/
        pyconsole.cfg
        regions/
          map.yml
        units/
          unit.yml
        layouts/
          setup_window.yml
          widget_test.yml
          window_test.yml
      gfx/
        Vera.ttf
        fixed_width.ttf
        load_screen.png
        move/
          arrow_bottom_left.png
          arrow_bottom_right.png
          arrow_left.png
          arrow_right.png
          arrow_top_left.png
          arrow_top_right.png
        units/
          barbarian_archer.png
          barbarian_chariot.png
          barbarian_horse.png
          barbarians.png
          boat.png
          camel.png
          desert_warrior.png
          elephant.png
          fedorati.png
          praetorians.png
          rome_general.png
          rome_legion.png
          siege_train.png
          warrior.png
          overlays/
            moves1.png
            moves2.png
            moves3.png
            moves4.png
            moves5.png
            moves6.png
            moves7.png
            moves8.png
        map/
          map.jpg
          regions/
            aemilia.png
            aemilia_icon.png
            aemilia_mask.png
            apulia_et_calabria.png
            apulia_et_calabria_icon.png
            apulia_et_calabria_mask.png
            etruria.png
            etruria_icon.png
            etruria_mask.png
            latium_et_campania.png
            latium_et_campania_icon.png
            latium_et_campania_mask.png
            lucania_et_bruttiun.png
            lucania_et_bruttiun_icon.png
            lucania_et_bruttiun_mask.png
            sicily.png
            sicily_icon.png
            sicily_mask.png
            transpadana.png
            transpadana_icon.png
            ... 共24个文件
        cities/
          enemy_large.png
          enemy_medium.png
          enemy_small.png
          roman_large.png
          roman_medium.png
          roman_small.png
          rome.png
        icons/
          about.png
          city.png
          console.png
          debug.png
          exit.png
          help.png
          military.png
          new.png
          open.png
          preferences.png
          save.png
          senate.png
          statistics.png
        gui/
          arrow_down.png
          arrow_up.png
          battle_info.png
          button.png
          button_high.png
          check_no.png
          check_yes.png
          city_infhex.png
          eagle.png
          endturn_button.png
          gradbar128.png
          gradbar64.png
          gradbar96.png
          hex_border.png
          img_music.png
          info_button.png
          mapicon_back.png
          nextturn_button.png
          number_select.png
          optionmenu_lhand.png
          ... 共50个文件
    SPQR_SLG.egg-info/
      PKG-INFO
      SOURCES.txt
      dependency_links.txt
      requires.txt
      top_level.txt
    SPQR_SLG_0_0_1/
      scripts/
        __pycache__/
          __init__.cpython-38.pyc
```


## 策划参考价值
SLG系统模块的代码实现参考（征兵/出征/建筑/联盟等）。
