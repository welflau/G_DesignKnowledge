# 明日方舟 · 活动剧情 · act49side（34段脚本）

> 来源：Kengxxiao/ArknightsGameData
> 原始链接：https://github.com/Kengxxiao/ArknightsGameData
> 分类：gameplay
> 标签：明日方舟, 塔防策略RPG, 活动剧情, 剧情脚本, 对话, 演出
> 游戏类型：塔防策略RPG

## 概述
明日方舟活动剧情「act49side」完整剧情脚本（34个文件，4216行对话）

## 正文
## 章节信息

- 分类：活动剧情
- 目录：activities/act49side
- 脚本文件数：34

### avg_segment_report

```
============================================================
AVG 演出指令段分析报告 (act49side)
样本目录: Story/Activities/act49side
文本指令: dialog, subtitle, aside (含无方括号纯文字->dialog)
演出指令段: 相邻两条文本指令之间的全部非文本指令
============================================================

【1. 文件与段落概览】
  参与文件数: 32
  演出指令段总数: 3895 (非空: 3895)
    level_act49side_09_end.txt: 289 段
    level_act49side_01_end.txt: 243 段
    level_act49side_01_beg.txt: 209 段
    level_act49side_08_beg.txt: 197 段
    level_act49side_st02.txt: 194 段
    level_act49side_03_beg.txt: 192 段
    level_act49side_06_beg.txt: 187 段
    level_act49side_10_beg.txt: 177 段
    level_act49side_06_end.txt: 173 段
    level_act49side_08_end.txt: 171 段
    level_act49side_03_end.txt: 163 段
    level_act49side_05_beg.txt: 162 段
    level_act49side_10_end.txt: 158 段
    level_act49side_st01.txt: 157 段
    level_act49side_07_end.txt: 155 段
    level_act49side_04_end.txt: 147 段
    level_act49side_11_end.txt: 144 段
    level_act49side_02_end.txt: 142 段
    level_act49side_09_beg.txt: 135 段
    level_act49side_02_beg.txt: 133 段
    ... 其余 12 个文件

【2. 段落长度分布】
  长度 1: 2812 次 (72.2%)
  长度 2: 290 次 (7.4%)
  长度 3: 218 次 (5.6%)
  长度 4: 85 次 (2.2%)
  长度 5: 77 次 (2.0%)
  长度 6: 75 次 (1.9%)
  长度 7: 77 次 (2.0%)
  长度 8: 47 次 (1.2%)
  长度 9: 45 次 (1.2%)
  长度 10: 35 次 (0.9%)
  长度 11: 27 次 (0.7%)
  长度 12: 23 次 (0.6%)
  长度 13: 15 次 (0.4%)
  长度 14: 14 次 (0.4%)
  长度 15: 7 次 (0.2%)
  长度 16: 9 次 (0.2%)
  长度 17: 7 次 (0.2%)
  长度 18: 5 次 (0.1%)
  长度 19: 6 次 (0.2%)
  长度 20: 4 次 (0.1%)
  长度 21: 2 次 (0.1%)
  长度 22: 1 次 (0.0%)
  长度 23: 1 次 (0.0%)
  长度 24: 1 次 (0.0%)
  长度 27: 2 次 (0.1%)
  长度 28: 2 次 (0.1%)
  长度 29: 1 次 (0.0%)
  长度 32: 1 次 (0.0%)
  长度 38: 1 次 (0.0%)
  长度 40: 1 次 (0.0%)
  长度 41: 1 次 (0.0%)
  长度 42: 1 次 (0.0%)
  长度 45: 1 次 (0.0%)
  长度 47: 1 次 (0.0%)
  最长段落: 47 条指令

【3. 演出指令出现频次 (Top 30)】
  charslot: 4520
  delay: 1136
  blocker: 944
  playsound: 627
  background: 247
  stopmusic: 145
  camerashake: 130
  playmusic: 120
  stopsound: 106
  bgeffect: 102
  image: 96
  sticker: 89
  curtain: 66
  createeffect: 53
  cameraeffect: 52
  effect: 50
  playanim: 50
  soundvolume: 48
  focusout: 45
  header: 32
  imagetween: 31
  popupdialog: 30
  backgroundtween: 28
  animtext: 27
  animtextclean: 27
  avgdisplay: 23
  battle.pause: 20
  multiline: 18
  hidecgitem: 17
  inputblocker: 17

【4. 单指令段 (仅一条演出指令)】
  [charslot]: 2652 次
  [stopmusic]: 56 次
  [blocker]: 38 次
  [playsound]: 26 次
  [delay]: 25 次
  [stopsound]: 5 次
  [focusout]: 2 次
  [camerashake]: 2 次
  [playmusic]: 1 次
  [multiline]: 1 次
  [soundvolume]: 1 次
  [cameraeffect]: 1 次
  [theater]: 1 次
  [playanim]: 1 次

【5. 双指令段 常见搭配 (Top 25)】
  [charslot] -> [charslot]: 102 次
  [blocker] -> [charslot]: 23 次
  [charslot] -> [delay]: 21 次
  [playsound] -> [charslot]: 18 次
  [charslot] -> [playsound]: 18 次
  [header] -> [stopmusic]: 12 次
  [playsound] -> [delay]: 12 次
  [delay] -> [charslot]: 10 次
  [camerashake] -> [charslot]: 7 次
  [playmusic] -> [charslot]: 6 次
  [camerashake] -> [playsound]: 5 次
  [camerafocusto] -> [delay]: 5 次
  [blocker] -> [blocker]: 3 次
  [charslot] -> [stopsound]: 2 次
  [playsound] -> [playsound]: 2 次
  [image] -> [imagetween]: 2 次
  [charslot] -> [stopmusic]: 2 次
  [playsound] -> [camerashake]: 2 次
  [playsound] -> [blocker]: 2 次
  [image] -> [delay]: 2 次
  [playsound] -> [stopsound]: 2 次
  [bgeffect] -> [charslot]: 2 次
  [stopmusic] -> [charslot]: 2 次
  [charslot] -> [camerashake]: 2 次
  [stopsound] -> [charslot]: 2 次

【6. 段落首指令 (段前常见)】
  charslot: 3090
  blocker: 273
  playsound: 172
  delay: 92
  stopmusic: 74
  header: 32
  stopsound: 30
  camerashake: 26
  playmusic: 17
  sticker: 14
  image: 9
  bgeffect: 8
  playanim: 7
  avgdisplay: 6
  background: 5
  effect: 5
  cameraeffect: 5
  camerafocusto: 5
  animtext: 3
  curtain: 3

【7. 段落尾指令 (段后常见，即紧接文本前的指令)】
  charslot: 3170
  delay: 310
  blocker: 126
  stopmusic: 88
  playsound: 80
  stopsound: 17
  playmusic: 16
  image: 13
  camerashake: 13
  focusout: 8
  background: 7
  soundvolume: 6
  multiline: 5
  battle.pause: 5
  bgeffect: 4
  sticker: 3
  effect: 3
  playanim: 3
  avgdisplay: 2
  imagetween: 2

【8. 常见指令组合 (按指令集合，Top 20)】
  {charslot}: 2821 次
  {charslot, delay}: 97 次
  {charslot, delay, playsound}: 74 次
  {charslot, playsound}: 58 次
  {stopmusic}: 56 次
  {blocker}: 42 次
  {blocker, charslot}: 34 次
  {playsound}: 29 次
  {delay}: 25 次
  {blocker, charslot, delay}: 16 次
  {background, blocker, charslot, delay, playmusic}: 15 次
  {delay, playsound}: 15 次
  {background, blocker, charslot, delay}: 14 次
  {charslot, delay, playsound, stopsound}: 13 次
  {header, stopmusic}: 12 次
  {blocker, header, stopmusic}: 12 次
  {bgeffect, blocker, charslot, delay, ...} (7 种): 11 次
  {blocker, charslot, delay, playsound}: 10 次
  {camerashake, playsound}: 10 次
  {camerashake, charslot}: 9 次

【9. 典型演出指令段示例】
  长度 1 示例:
    [delay] [delay(time=1)]
  长度 2 示例:
    [header] [HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
    [stopmusic] [stopmusic]
  长度 3 示例:
    [charslot] [charslot]
    [playsound] [PlaySound(key="$d_avg_slmddrprn",volume=0, channel="f", loop=true)]
    [soundvolume] [SoundVolume(volume=1, channel="f",fadetime=2)]
  长度 5 示例:
    [avgdisplay] [avgdisplay(id = "1",style = "bg",name = "bg_black",afrom=0.6,ato=0,du...
    [avgdisplay] [avgdisplay(id = "1")]
    [playsound] [PlaySound(key="$d_avg_rainheavy_loop", volume=0, loop=true, channel="...
    [soundvolume] [SoundVolume(volume=0.8, channel="ra",fadetime=1)]
    [charslot] [charslot(slot = "m", name = "avg_1050_chen3_1#11$2",focus="m")]
```

### act49side_05_a

```
[HEADER(is_tutorial=true, is_skippable=true, is_autoable=false)] 活动49side普通关_05
[InputBlocker(blockInput=true)]
[Delay(time=1.5)]
[Battle.Pause]
[InputBlocker(blockInput=true, black=0.4)]
[tutorial(focusWidth=120, focusHeight=120, animStyle="Highlight", focusStyle="HighlightCircle", black="0.5", protectTime=0.5, dialogHead="$avatar_npc_jie",cardIndex=0, rightStart=true)]椿，你已经盯着<@tu.kw>书刀</>看了一炷香的时间了。
[PopupDialog(dialogHead="$avatar_npc_chun", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")]抱歉！颉，这柄<@tu.kw>书刀</>是......
[PopupDialog(dialogHead="$avatar_npc_jie")]删定文稿的工具，使用起来并不复杂。
[Battle.UnlockFunction(mask="CHARACTER_INFO")]
[Battle.UnlockFunction(mask="CHARACTER_MENU")]
[Battle.Pause(pause=false)]
[InputBlocker(blockInput=true, black=0)]
[Delay(time=0.5)]
[Battle.Pause(pause=true)]
[InputBlocker(blockInput=true, cardIndex=0, rightStart=true, validWidth=112, validHeight=116)]
[Tutorial(waitForSignal="put_down", charId="trap_286_tjgsd",posX=2,posY=4,           dialogHead="$avatar_npc_jie", animStyle="Drag",           startCardIndex=0, startRightStart=true, endTileX=2, endTileY=4)] 将书刀放入<@tu.kw>字格</>，便可<@tu.kw>提取</>字格中的<@tu.kw>字</>，并将字<@tu.kw>存起来</>。
[Battle.Pause(pause=false)]
[InputBlocker(blockInput=true, black=0)]
[Delay(time=2.5)]
[Battle.Pause(pause=true)]
[tutorial(focusWidth=120, focusHeight=120, animStyle="Highlight", focusStyle="HighlightCircle", black="0.5", protectTime=0.5, dialogHead="$avatar_npc_jie",cardIndex=1, rightStart=true)]注意，手中仅可存有<@tu.kw>一个</>字。
[tutorial(focusWidth=120, focusHeight=120, animStyle="Highlight", focusStyle="HighlightCircle", black="0.5", protectTime=0.5, dialogHead="$avatar_npc_jie",cardIndex=0, rightStart=true)]书刀<@tu.kw>无法</>在手中有字的情况下使用。
[InputBlocker(blockInput=true, cardIndex=1, rightStart=true, validWidth=112, validHeight=116)]
[Tutorial(waitForSignal="put_down", charId="trap_289_zicai",posX=2,posY=2,           dialogHead="$avatar_npc_jie", animStyle="Drag",           startCardIndex=1, startRightStart=true, endTileX=2, endTileY=2)] 不过，可以随时将手中的字放置在任意的<@tu.kw>空字格</>中。
[Battle.Pause(pause=false)]
[InputBlocker(blockInput=true, black=0)]
[Delay(time=2.5)]
[Battle.Pause(pause=true)]
[inputblocker(blockInput=true, black=0.3)]
[Tutorial(dialogHead="$avatar_npc_jie",dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")]这样，便能<@tu.kw>调整</>字的位置。
[Tutorial(dialogHead="$avatar_npc_jie",dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")]若有需要，合理使用吧。
[Battle.Pause(pause=false)]
```

### act49side_10_a

```
[HEADER(is_tutorial=true, is_skippable=true, is_autoable=false)] 活动49side普通关_10
[InputBlocker(blockInput=true)]
[Delay(time=1.5)]
[Battle.Pause]
[InputBlocker(blockInput=true, black=0.4)]
[PopupDialog(dialogHead="$avatar_wang", protectTime=1)]......该出刀了。
[tutorial(focusWidth=120, focusHeight=120, animStyle="Highlight", focusStyle="HighlightCircle", black="0.5", protectTime=0.5, dialogHead="$avatar_npc_yi", tileX=19,tileY=18, dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")]<@tu.kw>镇岁柱</>，这是和天师府、司岁台的各位一同建造的榫卯装置。
[tutorial(focusWidth=120, focusHeight=120, animStyle="Highlight", focusStyle="HighlightCircle", black="0.5", protectTime=0.5, dialogHead="$avatar_npc_yi", tileX=19,tileY=18, dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")]<@tu.kw>开启技能</>前往东、南、西、北四片区域，击倒各自区域内的<@tu.kw>所有敌人</>，便可<@tu.kw>削弱</>岁不同部位的能力。
[PopupDialog(dialogHead="$avatar_npc_yi", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")]务必注意<@tu.kw>时限</>。倒计时截止，岁便会冲破封印，降临战场。
[PopupDialog(dialogHead="$avatar_npc_yi", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")]若已准备妥当，可随时开启<@tu.kw>中央镇岁柱</>的技能，解封并<@tu.kw>直面岁</>。
[PopupDialog(dialogHead="$avatar_npc_yi", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")]解封时，<@tu.kw>全场干员会被强制撤退并重置再部署时间</>。
[PopupDialog(dialogHead="$avatar_npc_yi", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")]岁极度强大，须至少使用<@tu.kw>镇岁柱</>削弱一次！
[Battle.Pause(pause=false)]
```

### act49side_11_a

```
[header(actId="act49side")]
[executeactionarray(target="trap_330_ycwang", key="stop_sp_recovery")]
[executeactionarray(target="char_2024_chyue", key="stop_sp_recovery")]
[executeactionarray(target="char_2015_dusk", key="stop_sp_recovery")]
[executeactionarray(target="char_2014_nian", key="stop_sp_recovery")]
[executeactionarray(target="char_2025_shu", key="stop_sp_recovery")]
[executeactionarray(target="char_2026_yu", key="stop_sp_recovery")]
[executeactionarray(target="char_2023_ling", key="stop_sp_recovery")]
[summonenemy(enemyId="enemy_3014_wangw", y="4", x="6", endX="6", endY="4")]
[summonenemy(enemyId="enemy_3017_ycsho", y="7", x="7", endX="7", endY="7")]
[summonenemy(enemyId="enemy_3018_yczzh", y="5", x="2", endX="2", endY="5")]
[summonenemy(enemyId="enemy_3019_ycyzh", y="4", x="11", endX="11", endY="4")]
[summonenemy(enemyId="enemy_3020_ycwei", y="1", x="5", endX="4", endY="0")]
[createeffect(id="enemy_3020_ycwei", key="enemy_suiwei_buff_01")]
[createeffect(id="enemy_3019_ycyzh", key="enemy_suiyzh_buff_01")]
[createeffect(id="enemy_3018_yczzh", key="enemy_suizzh_buff_01")]
[createeffect(id="enemy_3017_ycsho", key="enemy_suisho_buff_01")]
[delay(time="2")]

[name="岁", avatarId="avg_npc_2129_2", isAvatarRight="FALSE"]够了！这荒唐的棋局，也该有个尽头了！
[delay(time="2")]

[playanim(enemyId="enemy_3018_yczzh", anim="Skill_1_Begin_Start", looporidle="Skill_1_Begin_Loop", dir="DOWN")]
[playanim(enemyId="enemy_3017_ycsho", anim="Skill_1_Begin", looporidle="Skill_1_Loop", dir="DOWN")]
[playanim(enemyId="enemy_3019_ycyzh", anim="Skill_1_Begin_Start", looporidle="Skill_1_Begin_Loop", dir="DOWN")]
[playanim(enemyId="enemy_3020_ycwei", anim="Skill_1_Begin_Start", looporidle="Skill_1_Begin_Loop", dir="DOWN")]

[delay(time="2.6")]

[playanim(charId="trap_330_ycwang", anim="Idle", looporidle="Idle", dir="LEFT")]
[playanim(charId="trap_330_ycwang", anim="Idle", looporidle="Idle", dir="RIGHT")]
[playanim(charId="trap_330_ycwang", anim="Idle", looporidle="Idle", dir="DOWN")]
[delay(time="0.4")]

[camerafocusto(offsetX="6", offsetY="2.5", time="2", scale="MID")]
[delay(time="2")]
[playanim(charId="trap_330_ycwang", anim="Die", looporidle="Die", dir="DOWN")]
[delay(time="0.4")]
[name="望", avatarId="char_2027_wang", isAvatarRight="FALSE"]呵，尽头？这还是你曾经告诉我的......棋盘广阔无尽，我与你之间的胜负，又何止在名为“望”的这一盘？
[playanim(charId="trap_330_ycwang", anim="Idle_2", looporidle="Idle_2", dir="DOWN")]
[name="望", avatarId="char_2027_wang", isAvatarRight="FALSE"]与你对弈的，也不止我一人。

[summontrap(x="8", y="2", charId="char_2025_shu", isChar="TRUE", dir="LEFT")]
[createeffect(id="char_2025_shu", key="common_immortal_01")]
[delay(time="1")]
[playanim(charId="char_2025_shu", anim="Skill_3_Begin", looporidle="Skill_3_Idle", dir="LEFT")]
[delay(time="0.267")]
[createeffect(id="trap_330_ycwang", key="shu_skill_03_hit")]
[createeffect(id="trap_330_ycwang", key="shu_skill_03_range")]
[createeffect(id="trap_330_ycwang", key="shu_talent_buff_01")]
[createeffect(id="trap_330_ycwang", key="shu_talent_buff_02")]
[delay(time="0.5")]
[name="“黍”", avatarId="char_2025_shu", isAvatarRight="FALSE"]这是你自己种下的因果，交还与你。
[delay(time="0.1")]
[playanim(charId="char_2025_shu", anim="Idle", looporidle="Idle", dir="UP")]
[delay(time="0.5")]

[summontrap(x="8", y="1", charId="char_2014_nian", isChar="TRUE", dir="LEFT")]
[createeffect(id="char_2014_nian", key="common_immortal_01")]
[delay(time="0.5")]
[name="“年”", avatarId="char_2014_nian", isAvatarRight="FALSE"]臭棋篓子二哥，你早说自己需要帮忙，我们不早就来了？
[delay(time="0.1")]
[createeffect(id="trap_330_ycwang", key="nian_skill_01_hit")]
[createeffect(id="trap_330_ycwang", key="nian_skill_03_buff")]
[delay(time="0.1")]
[playanim(charId="char_2014_nian", anim="Idle", looporidle="Idle", dir="UP")]



[resetcamera(time="1.5")]
[delay(time="1.5")]

// anim part a
[playanim(enemyId="enemy_3018_yczzh", anim="Skill_1_Begin_End", looporidle="Skill_1_Begin_End", dir="DOWN")]
[playanim(enemyId="enemy_3019_ycyzh", anim="Skill_1_Begin_End", looporidle="Skill_1_Begin_End", dir="DOWN")]
[playanim(enemyId="enemy_3020_ycwei", anim="Skill_1_Begin_End", looporidle="Skill_1_Begin_End", dir="DOWN")]
[createeffect(id="enemy_3017_ycsho", key="enemy_suisho_skill_start_01")]
[delay(time="0.3")]
[finisheffect(key="enemy_suisho_skill_start_01")]

[delay(time="1")]
[setposition(enemyId="enemy_3018_yczzh", y="6", x="2")]
[setposition(enemyId="enemy_3019_ycyzh", y="6", x="2")]
[setposition(enemyId="enemy_3020_ycwei", y="6", x="2")]

[playanim(enemyId="enemy_3017_ycsho", anim="Skill_1_Attack", noIdleWhenFinish="TRUE", dir="DOWN")]
[playanim(enemyId="enemy_3018_yczzh", anim="Skill_1_Attack", noIdleWhenFinish="TRUE", dir="UP")]
[playanim(enemyId="enemy_3019_ycyzh", anim="Skill_1_Attack", noIdleWhenFinish="TRUE", dir="UP")]
[playanim(enemyId="enemy_3020_ycwei", anim="Skill_1_Attack", noIdleWhenFinish="TRUE", dir="DOWN")]

[delay(time="0.6")]

[camerashake(vibrato=3, randomness=0.1, duration=0.2, strengthX=0.1, strengthY=0, strengthZ=-0.1)]

[createeffect(id="enemy_3018_yczzh", key="enemy_suizzh_skill_start_01")]
[createeffect(id="enemy_3019_ycyzh", key="enemy_suiyzh_skill_start_01")]

[createeffect(id="enemy_3017_ycsho", key="enemy_suisho_skill_start_02")]
[createeffect(id="trap_330_ycwang", key="enemy_suisho_attack_hit_01")]

[createeffect(id="trap_330_ycwang", key="enemy_suiwei_skill_hit_01")]
[finisheffect(key="shu_talent_buff_01")]
[finisheffect(key="shu_talent_buff_02")]
[finisheffect(key="nian_skill_03_buff")]

[delay(time="0.6")]

[setposition(enemyId="enemy_3018_yczzh", y="2", x="5")]
[setposition(enemyId="enemy_3019_ycyzh", y="11", x="4")]
[setposition(enemyId="enemy_3020_ycwei", y="5", x="0")]
[playanim(enemyId="enemy_3017_ycsho", anim="Skill_1_End", looporidle="Idle", dir="DOWN")]
[playanim(enemyId="enemy_3018_yczzh", anim="Skill_1_End", looporidle="Idle", dir="DOWN")]
[playanim(enemyId="enemy_3019_ycyzh", anim="Skill_1_End", looporidle="Idle", dir="DOWN")]
[playanim(enemyId="enemy_3020_ycwei", anim="Skill_1_End", looporidle="Idle", dir="DOWN")]
[delay(time="1.33")]

[camerafocust

... (全文15798字符)
```

### level_act49side_01_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[stopmusic]
[dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]
[playMusic(intro="$chenandwei_intro", key="$chenandwei_loop", volume=0.6)]
[Subtitle(text="“晖洁......你的名字是陈晖洁。”", x=530, y=310, alignment="left", size=24, delay=0.04,  width=700)]
[Subtitle(afrom=1,ato=0,duration=2)]
[delay(time=1)]
[Subtitle]
[Subtitle(text="“记住这个姓，之外的一切，都和你无关。”", x=260, y=200, alignment="left", size=26, delay=0.04, width=700)]
[Subtitle(afrom=1,ato=0,duration=2)]
[delay(time=1)]
[Subtitle]
[Subtitle(text="“小塔......是姐姐？”", x=510, y=520, alignment="left", size=25, delay=0.04, width=700)]
[Subtitle(afrom=1,ato=0,duration=2)]
[delay(time=1)]
[Subtitle]
[Subtitle(text="“我恨你。我也恨她们。明明我该爱你们的，而今我却全都恨。”", x=190, y=320, alignment="left", size=24, delay=0.04, width=700)]
[Subtitle(afrom=1,ato=0,duration=2)]
[delay(time=1)]
[Subtitle]
[Subtitle(text="“晖洁，快点长大吧。”", x=200, y=460, alignment="left", size=24, delay=0.04, width=700)]
[Subtitle(afrom=1,ato=0,duration=2)]
[delay(time=1)]
[Subtitle]
[Subtitle(text="“长大以后，你就能改变一切。”",  x=430, y=320, alignment="left", size=28, delay=0.04, width=700)]
[Subtitle(afrom=1,ato=0,duration=2)]
[delay(time=1)]
[Subtitle]
[stopmusic(fadetime=2)]
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[charslot]
[Background(image="35_g13_yanlivingroom",screenadapt="coverall")]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=0.5)]
[dialog]
[animtext(id = "at1", name = "group_location_stamp", style="avg_only_medium", pos = "-400,-200", block = false)]<p=2>望日前三日</>
[delay(time=3)]
[animtextclean]
[delay(time=1)]
[playMusic(key="$m_sys_act14mini_loop", volume=0)]
[MusicVolume(volume=0.6, fadetime=2)]
[PlaySound(key="$d_gen_thunders_amb")]
[delay(time=0.5)]
[charslot(slot = "m", name = "avg_1050_chen3_1#1$2")]
[charslot(slot = "m", action="shake", power=3, times=30, duration=0.3, isblock=true)]
[name="陈"]——！
[charslot(slot = "m", name = "avg_1050_chen3_1#7$2")]  
[name="陈"]......是雷声。  
[charslot(slot = "m", name = "char_2005_weiyw_1#5")]
[name="魏彦吾"]只是雷声。  
[charslot(slot = "m", name = "char_2005_weiyw_1#5")]
[name="魏彦吾"]已经是深秋了，要是拖到入冬，下了雪，路会很难走。  
[charslot(slot = "m", name = "avg_1050_chen3_1#1$2")]
[name="陈"]......哼。  
[charslot(slot = "m", name = "char_2005_weiyw_1#5")]
[name="魏彦吾"]晖洁......你应当回去。  
[charslot(slot = "m", name = "avg_1050_chen3_1#11$2")]
[name="陈"]“回”？  
[charslot(slot = "m", name = "avg_1050_chen3_1#11$2")]
[name="陈"]回哪里去？龙门？  
[charslot(slot = "m", name = "char_2005_weiyw_1#2")]
[name="魏彦吾"]你想知道的事，我都已经告诉你了。  
[charslot(slot = "m", name = "char_2005_weiyw_1#5")]
[name="魏彦吾"]所以你应该明白，眼下的这些事，都与你无关。  
[charslot(slot = "m", name = "avg_1050_chen3_1#10$2")]
[name="陈"]真想感叹......你大概也是真的老了，舅舅。  
[charslot(slot = "m", name = "avg_1050_chen3_1#1$2")]
[name="陈"]换作五年前的你，这会儿应该早已经和我动过手了。  
[charslot(slot = "m", name = "char_2005_weiyw_1#5")]
[name="魏彦吾"]你的性子到底也是变了。  
[charslot(slot = "m", name = "char_2005_weiyw_1#5")]
[name="魏彦吾"]留在这驿馆的几天，你的问题也并不多。  
[charslot(slot = "m", name = "avg_1050_chen3_1#11$2")]
[name="陈"]因为我还是信不过你。  
[charslot(slot = "m", name = "avg_1050_chen3_1#1$2")]
[name="陈"]你讲的那些事......关于那位太师，关于你的弟弟——我素未谋面的“另一位舅舅”，还有那位老真龙...... 
[charslot(slot = "m", name = "avg_1050_chen3_1#1$2")]
[name="陈"]我没有权力对这些事评论什么。非要说的话，我倒是庆幸，最终不是由你来为炎国的许多事做决定。  
[charslot(slot = "m", name = "char_2005_weiyw_1#2")]
[name="魏彦吾"]这一点我同样不否认......  
[charslot(slot = "m", name = "avg_1050_chen3_1#7$2")]
[name="陈"]我的确还是想知道你离开百灶时到底在想什么，母亲为什么也跟着你来到龙门，又为何留了下来。  
[charslot(slot = "m", name = "avg_1050_chen3_1#10$2")]
[name="陈"]但我不指望在这个时候能从你口中听到一个公正的答案，听到你对那些往事最客观的陈述。  
[charslot(slot = "m", name = "avg_1050_chen3_1#1$2")]
[name="陈"]所以我会自己搞清楚——我是不会走的。  
[charslot(slot = "m", name = "avg_1050_chen3_1#1$2")]
[name="陈"]我知道你总有在关键的时候把事情搞砸的本事，尤其是在这种和你自己有关的事上。  
[charslot(slot = "m", name = "avg_1050_chen3_1#1$2")]
[name="陈"]就当是防止你再做蠢事也好，甚至是保护你也好——我都不会走。  
[charslot(slot = "m", name = "avg_1050_chen3_1#7$2")]
[name="陈"]我们都省省吧。
[charslot(slot = "m", name = "char_2005_weiyw_1#2")]  
[name="魏彦吾"]......  
[charslot(slot = "m", name = "char_2005_weiyw_1#2")]
[name="魏彦吾"]晖洁......你这些年——  
[charslot(slot = "m", name = "avg_1050_chen3_1#10$2")]
[name="陈"]一样，也没什么好说的。  
[charslot(slot = "m", name = "char_2005_weiyw_1#2")]
[name="魏彦吾"]或许等到你愿意说的时候......  
[Dialog]
[charslot]
[PlaySound(key="$d_avg_slmddrprn",volume=0, channel="f", loop=true)]
[SoundVolume(volume=1, channel="f",fadetime=2)]
陈晖洁向窗外看去。  
远处移动城市的灯火已经暗淡了数天，百灶城的轮廓在夜幕中模糊着，像是蛰伏巨兽的脊背。  
她试图去想象，那些对自己而言不久前才被证实的古老传说中的庞然巨物。  
细碎的秋雨不断敲打着窗户，声乱如麻。  
[dialog]
[StopSound(channel="f", fadetime=1)]
[Delay(time=1)]
[charslot(slot = "m", name = "avg_1050_chen3_1#4$2")]
[name="陈"]......还是没有消息。  
[charslot(slot = "m", name = "char_2005_weiyw_1#2")]
[name="魏彦吾"]那就已经是最好的消息。  
[charslot(slot = "m", name = "char_2005_weiyw_1#5")]
[name="魏彦吾"]事已至此，我们没办法期待任何好的转机。  
[charslot(slot = "m", name = "avg_1050_chen3_1#11$2")]
[name="陈"]你说，如果百灶城那边有任何异动......玉门就会立刻开战。 
[charslot(slot = "m", name = "avg_1050_chen3_1#11$2")] 
[name="陈"]你所说的“岁兽”能造成的动乱，还有这一战的结果......无人可以确定。  
[charslot(slot = "m", name = "char_2005_weiyw_1#5")]
[name="魏彦吾"]嗯。  
[charslot(slot = "m", name = "avg_1050_chen3_1#10$2")]
[name="陈"]这就是大炎隐藏了上千年的秘密......你们还真是一样。  
[charslot(slot = "m", name = "char_2005_weiyw_1#5")]
[name="魏彦吾"]......可是事有蹊跷。  
[charslot(slot = "m", name = "char_2005_weiyw_1#5")]
[name="魏彦吾"]当下情势已经万分紧急，可过去十日，玉门和百灶之间来往的信使不超过三班。  
[charslot(slot = "m", name = "char_2005_weiyw_1#4")]
[name="魏彦吾"]这不是玉门战时应该有的状态。
[dialog]
[charslot]
[charslot(slot = "m", name = "avg_npc_038",duration=1)]
[delay(time=1)]
[name="影卫"]魏公，有客。  
[charslot(slot = "m", name = "char_2005_weiyw_1#5")]
[name="魏彦吾"]这个时候......  
[charslot(slot = "m", name = "char_2005_weiyw_1#5")]
[name="魏彦吾"]请进来就是。  
[dialog]
[charslot]
[PlaySound(key="$d_avg_woodf

... (全文27461字符)
```

### level_act49side_01_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[stopmusic]
[dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[animtext(id = "at1", name = "group_location_stamp", style="avg_only_medium", pos = "-400,-200", block = false)]<p=2>望日前两日 寅时</>
[delay(time=3)]
[animtextclean]
[delay(time=1)]
[playMusic(intro="$loading_intro", key="$loading_loop", volume=0.6)]
[curtain(direction = 0,fillfrom = 0.5,fillto = 0.15, fadetime=0.1)]
[curtain(direction = 4,fillfrom = 0.5,fillto = 0.15, fadetime=0.1)]
[Background(image="58_g4_baizaomainstreet_n",screenadapt="coverall",xScale=1.2,yScale=1.2, y=-150)]
[backgroundTween(xFrom = 100, xTo = -100, duration=30, block=false)]
[focusout(type="bg", id="58_g4_baizaomainstreet_n", from=0, to=0.6, duration=0.1, block=false)]
[Delay(time=0.1)]
[PlaySound(key="$d_avg_audience_chaos", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot(slot = "l", name = "avg_npc_1622_1#1$1", bstart=0.9,bend=1, posfrom = "200,30", posto = "0,30", duration = 0.8)]
[charslot(slot = "l", action="zoom", poszoom = "0.5,0.5", scale=0.8, duration = 0)]
[Delay(time=0.5)]
[charslot(slot = "m", name = "avg_npc_1636_1#1$1", bstart=0.9,bend=1, posfrom = "400,30", posto = "-80,30", duration = 0.8)]
[charslot(slot = "m", action="zoom", poszoom = "0.5,0.5", scale=0.8, duration = 0)]
[Delay(time=0.3)]
[charslot(slot = "r", name = "avg_npc_1625_1#1$1", bstart=0.9,bend=1, posfrom = "200,30", posto = "0,30", duration = 0.8)]
[charslot(slot = "r", action="zoom", poszoom = "0.5,0.5", scale=0.8, duration = 0)]
[Delay(time=0.2)]
[charslot(slot = "l", posfrom = "0,30", posto = "-200,30", afrom=1, ato=0, duration = 0.8)]
[Delay(time=0.3)]
[charslot(slot = "m", posfrom = "-80,30", posto = "-250,30", afrom=1, ato=0, duration = 0.8)]
[Delay(time=0.2)]
[charslot(slot = "r", posfrom = "0,30", posto = "-200,30", afrom=1, ato=0, duration = 0.8)]
[Delay(time=1)]
[charslot]
[charslot(slot = "l", name = "avg_npc_1642_1#1$1", bstart=0.9,bend=1, posfrom = "200,30", posto = "0,30", duration = 0.8)]
[charslot(slot = "l", action="zoom", poszoom = "0.5,0.5", scale=0.8, duration = 0)]
[Delay(time=0.5)]
[charslot(slot = "m", name = "avg_npc_1623_1#1$1", bstart=0.9,bend=1, posfrom = "400,30", posto = "-80,30", duration = 0.8)]
[charslot(slot = "m", action="zoom", poszoom = "0.5,0.5", scale=0.8, duration = 0)]
[Delay(time=0.3)]
[charslot(slot = "r", name = "avg_npc_1638_1#1$1", bstart=0.9,bend=1, posfrom = "200,30", posto = "0,30", duration = 0.8)]
[charslot(slot = "r", action="zoom", poszoom = "0.5,0.5", scale=0.8, duration = 0)]
[Delay(time=0.2)]
[charslot(slot = "l", posfrom = "0,30", posto = "-200,30", afrom=1, ato=0, duration = 0.8)]
[Delay(time=0.3)]
[charslot(slot = "m", posfrom = "-80,30", posto = "-250,30", afrom=1, ato=0, duration = 0.8)]
[Delay(time=0.2)]
[charslot(slot = "r", posfrom = "0,30", posto = "-200,30", afrom=1, ato=0, duration = 0.8)]
[Delay(time=1)]
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[curtain]
[charslot]
[Background(image="58_g4_baizaomainstreet_n",screenadapt="coverall")]
[focusout(type="bg", id="58_g4_baizaomainstreet_n", from=0.6, to=0, duration=0.1, block=false)]
[delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[charslot(slot = "l", focus="l", name = "avg_npc_1637_1#1$1")]
[charslot(slot = "r", focus="l", name = "avg_npc_1637_1#1$1",block=true)]
[charslot(slot = "l", focus="l")]
[name="巡防营守卫"]禀报哨官，自昨日酉时至今日寅时一刻，主街片区八成以上的居民已被安全转移至丙号移动地块。  
[name="巡防营守卫"]还有部分群众，因公务、财物等原因滞留。  
[charslot(slot = "r", focus="r")]
[name="巡防营哨官"]督促剩下的百姓尽快处理好手头的事务，不要过分贪恋财物，最后期限已经不远了。
[charslot(slot = "l", focus="l")]
[name="巡防营守卫"]是！  
[charslot(slot = "r", focus="r")]
[name="巡防营哨官"]另外，加强各哨卡的安全检查。如有任何可疑分子和异常情况，立即禀报校将。  
[charslot(slot = "l", focus="l")]
[name="巡防营守卫"]遵命！  
[dialog]
[PlaySound(key="$d_gen_soldiersrun", volume=1)]
[charslot(slot = "l", posfrom="0,0",posto="-100,0",afrom=1, ato=0, duration=1.5,isblock=true)]
[delay(time=0.5)]
[charslot]
[delay(time=0.5)]
[charslot(slot = "m", name = "avg_4121_zuole_1#1$1",duration=1, isblock=true)]
[name="左乐"]原来百灶城已经开始疏散了......不知道司岁台有没有岁陵最新的消息。  
[charslot(slot = "m", name = "avg_4121_zuole_1#3$1")]
[name="左乐"]哨卡的人不少......还是尽量不要引人注意。
[charslot(slot = "m", name = "avg_4121_zuole_1#1$1")]  
[name="左乐"]......绕路走吧。  
[stopmusic(fadetime=2)]
[dialog]
[charslot(slot = "m", posfrom="0,0",posto="-30,-30",duration=0.5,isblock=true)]
[delay(time=0.5)]  
[PlaySound(key="$d_avg_clothmovement", volume=1)]
[charslot(slot = "m", posfrom="-30,-30",posto="80,200",afrom=1, ato=0, duration=0.15,isblock=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0.5, block=true)]
[charslot]
[Blocker(a=0, r=0, g=0, b=0, style = "slider", inverse = true, fadetime=2, block=true)]
[name="左乐"]那是——  
左乐绕过了哨卡，但是在下一个街角，在嘈杂的人群中，他看到了一个本不该出现在这里的身影。
[playMusic(intro="$m_act31side_bat2_intro",key="$m_act31side_bat2_loop", volume=0.6)]
[dialog]
[PlaySound(key="$d_gen_walk_n", volume=1)]
[charslot(slot = "m", name = "avg_npc_2134_1#1$1",duration=1.5,isblock=true)]
[name="覆面的秉烛人"]左乐。  
[dialog]
[charslot]
[PlaySound(key="$d_avg_clothmovement", volume=1)]
[charslot(slot = "m", name = "avg_4121_zuole_1#1$1",posfrom="-150,150",posto="30,-30",duration=0.5, isblock=true)]
[delay(time=0.4)]
[PlaySound(key="$d_avg_runstop",volume=1)]
[charslot(slot = "m", name = "avg_4121_zuole_1#1$1",afrom=1,ato=1, posfrom="30,-30",posto="0,0",duration=0.5, isblock=true)]
[name="左乐"]您......  
[charslot(slot = "m", name = "avg_4121_zuole_1#6$1")]  
[name="左乐"]抱歉，请问您是哪位......前辈？  
[charslot(slot = "m", name = "avg_npc_2134_1#1$1")]
[name="覆面的秉烛人"]邙山镇和界园的事，司岁台已经知晓。我奉命来此接应，辛苦你了。  
[name="覆面的秉烛人"]长途劳顿，先去歇息吧。  
[charslot(slot = "m", name = "avg_4121_zuole_1#1$1")]  
[name="左乐"]多谢前辈关心。  
[charslot(slot = "m", name = "avg_4121_zuole_1#1$1")]  
[name="左乐"]可现在我还需将信物送回司岁台，镇抚仪式的细节也该第一时间呈报给监正大人，在下不敢松懈。  
[charslot(slot = "m", name = "avg_npc_213

... (全文46229字符)
```

### level_act49side_02_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[curtain(direction = 0,fillfrom = 0.1,fillto = 0.2, fadetime=0.1)]
[curtain(direction = 4,fillfrom = 0.1,fillto = 0.2, fadetime=0.1)]
[Delay(time=1)]
[Background(image="70_g7_suilingcore",x=0, y=-150, xScale=1.2, yScale=1.2, fadetime=5)]
[Blocker(a=0.4, r=0, g=0, b=0, fadetime=3, block=true)]
[playMusic(key="$m_sys_act14mini_loop", volume=0.6)]
[Delay(time=1)]
[Subtitle(text="你来了。", x=300, y=330, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="还是这一局棋......千年来，你已经输了无数次的棋局。", x=300, y=330, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="你妄图以分身对抗整体......这些苦心孤诣的谋划，在我看来，不过是顽童游戏。", x=300, y=330, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="沉溺于儿戏之中，正是你一如既往的恶习。", x=300, y=330, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="你这一次挑战，也不过是对以往千万遍惨败的重复。", x=300, y=330, alignment="center", size=24, delay=0.04, width=700)]
[subtitle]
......呵。
你还在用傲慢遮掩你的恐惧。
何必徒劳？
愤怒，害怕，期待......你想在我身上看见的东西，我在你身上一览无遗。
如果你不害怕，那便入局。
这一次......
输的一定会是你。
[stopmusic(fadetime=3)]
[Dialog]
[delay(time=1)]
[PlaySound(key="$d_avg_weiqi_heavy")]
[delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[curtain]
[delay(time=2)]
[Background(image="70_g11_oldpavilion",screenadapt="coverall")]
[name="朔"]这一局，是我输了。
[dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[delay(time=1)]
[animtext(id = "at1", name = "group_location_stamp", style="avg_only_heavy", pos = "-400,-200", block = false)]<p=1>593年</>
[delay(time=3)]
[animtextclean]
[delay(time=1)]
[playMusic(key="$m_sys_act23side_loop", volume=0.6)]
[charslot(slot = "m", name = "avg_2024_chyue_1#6$1",duration=1)]
[delay(time=1.5)]
[name="朔"]没想到这边对杀还有这一种变化......真是失算了。
[dialog]
[charslot]
[charslot(slot = "m", name = "avg_2027_wang_1#2$2",duration=1)]
[delay(time=2)]
[name="望"]......百手左右，要不是你在腹地一味退让求和，说不定还有争胜可能。
[charslot(slot = "m", name = "avg_2024_chyue_1#10$1")]
[name="朔"]原来如此......那时算不清后续变化，就只能选了最稳妥的下法。     
[name="朔"]哈哈，我还以为最近在棋艺上有些长进，看来还是差你许多。
[charslot(slot = "m", name = "avg_2024_chyue_1#10$1")]
[name="朔"]最近这一战，多亏你以逸待劳、诱敌深入的计策，我军才得以避免许多伤亡。
[name="朔"]你这次回京可以好好歇息一阵，只是下次再见，恐怕又得是许久之后了。
[charslot(slot = "m", name = "avg_2027_wang_1#2$2")]
[name="望"]你倒是一点都没有把胜负放在心上。
[charslot(slot = "m", name = "avg_2024_chyue_1#10$1")]
[name="朔"]兄弟相处，又不是庙算胜负，何必这么计较。
[charslot(slot = "m", name = "avg_2027_wang_1#4$2")]
[name="望"]不光是下棋，我看你不管在哪都乐意做宅心仁厚的老好人，什么事都可以不放在心上。
[charslot(slot = "m", name = "avg_2024_chyue_1#6$1")]
[name="朔"]这又是从何说起......
[charslot(slot = "m", name = "avg_2027_wang_1#1$2")]
[name="望"]两月前，新上任的兵部右侍郎连同礼部共参了你一本。
[name="望"]拥兵独断，不是小罪名。
[charslot(slot = "m", name = "avg_2024_chyue_1#1$1")]
[name="朔"]......
[name="朔"]近半年来你我一直同在前线，你如何能得知朝中的事？
[charslot(slot = "m", name = "avg_2027_wang_1#3$2")]
[name="望"]我自有办法，你应该担心的是你自己。
[charslot(slot = "m", name = "avg_2024_chyue_1#1$1")]
[name="朔"]如果他说的是之前我带兵不曾按时回营的事，那是因为行军途中突遇天灾，不得不另外扎营。
[name="朔"]这件事杨将军当时便已经知晓，就算兵部追责起来，也当有公论。
[charslot(slot = "m", name = "avg_2027_wang_1#1$2")]
[name="望"]倒不是让你担心这一件事。
[name="望"]那位侍郎被查出收受贿赂，手伸到了军需用度上......此时应该正在狱中候审。
[name="望"]暂时不会再由着他谣言惑众，至于能不能活着从狱里出来，就要看他的运气了。
[charslot(slot = "m", name = "avg_2024_chyue_1#8$1")]
[name="朔"]......
[name="朔"]你答应过我，不会再染指朝堂政事。
[charslot(slot = "m", name = "avg_2027_wang_1#3$2")]
[name="望"]明明是帮大炎除去了一个不干净的官员，怎么还反过来指责我多管闲事？
[charslot(slot = "m", name = "avg_2024_chyue_1#8$1")]
[name="朔"]你很清楚自己到底是什么用心......
[name="朔"]你是觉得整个朝堂都是你的棋局，别人的性命都是你的掌上玩物？
[charslot(slot = "m", name = "avg_2027_wang_1#11$2")]
[name="望"]......呵，你愿意当正人君子，难道你就看不到有多少人用心险恶？
[name="望"]那人刚上任就敢将矛头指向你，难道背后没有他人指使？想要与我们为敌的岂止一人？
[name="望"]对这一人手软，后患无穷。
[charslot(slot = "m", name = "avg_2024_chyue_1#9$1")]
[name="朔"]......
[charslot(slot = "m", name = "avg_2027_wang_1#1$2")]
[name="望"]从幺弟诞生以来，我们周遭发生了多少怪事。
[charslot(slot = "m", name = "avg_2027_wang_1#4$2")]
[name="望"]......方的病人明明见好，却莫名其妙地投了井。
[name="望"]有人模仿夕的笔触，借她的名头画了不少颠倒黑白的“讽喻之作”。
[name="望"]易的园子进了盗匪，丢失了几件重要的藏物。大理寺严加审问，到最后发现只是一伙不折不扣的笨贼。
[charslot(slot = "m", name = "avg_2027_wang_1#1$2")]
[name="望"]然后，就是关于你的事。
[charslot(slot = "m", name = "avg_2024_chyue_1#1$1")]
[name="朔"]......
[charslot(slot = "m", name = "avg_2027_wang_1#1$2")]
[name="望"]我们都清楚......祂还未死。
[name="望"]这里的人们从未忘记祂是何等恐怖之物，直到现在，我们的一举一动，每一次见面，都要被严加监管。
[name="望"]难道你还认为，靠你立下的一星半点的功绩，就可以让人不把我们当作其心可诛的异类？
[charslot(slot = "m", name = "avg_2024_chyue_1#1$1")]
[name="朔"]方弟和夕妹......都还好吗？
[charslot(slot = "m", name = "avg_2027_wang_1#1$2")]
[name="望"]方的确消沉了一阵子，夕从来都是如此，不过想必他们都不至于太放在心上。
[name="望"]问题在于，今后又该如何？
[charslot(slot = "m", name = "avg_2024_chyue_1#1$1")]
[name="朔"]你认为，这一切背后都有人在操纵？
[name="朔"]是山海众，还是其他人别有用心？
[charslot(slot = "m", name = "avg_2027_wang_1#11$2")]
[name="望"]......这才是我担心的。
[name="望"]如果这些事背后都有一个统一的指使者......
[name="望"]我算不到此人会是谁，更不知道他意图如何。
[charslot(slot = "m", name = "avg_2024_chyue_1#1$1")]
[name="朔"]你说的这些事，我会找司岁台一一核实。
[name="朔"]......我知道你是好心。
[name="朔"]下次别再行这种逾矩之事。
[charslot(slot = "m", name = "avg_2027_wang_1#1$2")]
[name="望"]我们之间何曾是彼此担忧的关系？
[name="望"]我只是不想遭人陷害还一无所知。
[charslot(slot = "m", name = "avg_2027_wang_1#10$2")]
[name="望"]时候差不多了，该走了。
[charslot(slot = "m", name = "avg_2024_chyue_1#1$1")]
[name="朔"]路途遥远，路上多加小心。
[name="朔"]回京后，代我问候他们吧。
[charslot(slot = "m", name = "avg_2027_wang_1#1$2")]
[name="望"]......我未必会去见他们。
[dialog]
[playsound(key="$d_gen_walk_n")]
[charslot(duration=1.5)]
[delay(time=2.5)]
[charslot]
[charslot(slot = "m", name = "avg_2024_chyue_1#3$1")]
[name="朔"]唉。
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[delay(time=1)]
[Background]
代理人于是辞别手足同胞，向京城的方向走去。
路途遥远，他走得很急，没时间为了路上听见的一丝杂音驻足。
[stopmusic(fadetime=2)]
[Dialog]
[delay(time=2)]
[name="？？？"]一招不慎......
[name="？？？"]满盘皆输......
[dialog]
[delay(time=2)]
那，我们就从余开始，怎么样？
好啊。余......我想想......
[dialog]
[delay(time=1)]
余音绕梁。
[dialog]
[Background(image="70_g12_oldyanroom",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[playMusic(intr

... (全文18471字符)
```

### level_act49side_02_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Delay(time=1)]
[Background(image="70_g13_oldyanstreet",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=2)]
[animtext(id = "at1", name = "group_location_stamp", style="avg_only_heavy", pos = "-400,-200", block = false)]<p=1>593年</>
[delay(time=3)]
[animtextclean]
[delay(time=1)]
[Blocker(a=0.6, r=0, g=0, b=0, fadetime=1, block=true)]
[playMusic(intro="$nervous_intro",key="$nervous_loop", volume=0.6)]
[Subtitle(text="宁让数子......勿失一先......", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="一招不慎......满盘皆输！", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="满盘皆输......", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="皆输......", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[subtitle]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1.5, block=true)]
[charslot(slot = "m", name = "avg_2027_wang_1#1$2",duration=1)]
[delay(time=2)]
[name="望"]......到底还是找上来了。
[name="望"]你也跟了我一路了，还不现形？
[charslot(slot = "m", focus = "n")]
望回过头，那阵既像抱怨又像哭诉的声音并未有丝毫止歇，只是缓缓远离他的耳边。
[charslot(slot = "m", name = "avg_2027_wang_1#1$2")]
[name="望"]呵。
[name="望"]我倒要看看，你到底能有什么能耐。
[dialog]
[BackgroundTween(xScaleFrom=1, yScaleFrom=1, xScaleTo=1.05, yScaleTo=1.05,duration=1.5)]
[playsound(key="$d_gen_walk_n")]
[charslot(duration=1.5)]
[delay(time=2)]
跟随着诡异的声音，望来到一个破烂的棋摊前面。
貌似是摊主的男人盘腿坐在地上呜呜啜泣，此外周围空无一人。
[dialog]
[charslot(slot="m",name="avg_npc_1639_1#1$1",bstart=0.4,bend=0.8,duration=1.5)]
[delay(time=2)]
[name="怪异的男人"]一招不慎......满盘皆输......
[name="怪异的男人"]满盘皆输啊！
[charslot]
[playsound(key="$d_avg_weiqi_drop",channel="1")]
[CameraShake(duration=0.3, xstrength=15, ystrength=15, vibrato=20, randomness=90, fadeout=true, block=false)]
望还来不及看他面前的棋局是何情况，男人就扑在棋枰上号啕起来，不少棋子都被他拂到地上。
[charslot(slot = "m", name = "avg_2027_wang_1#3$2")]
[name="望"]......闹剧。
[charslot(slot = "m", focus = "n")]
望转身想走，身后男人的哭声也小了下去。
[charslot]
[charslot(slot="m",name="avg_npc_1639_1#1$1",bstart=0.4,bend=0.8)]
[name="怪异的男人"]客官、客官莫走，棋局我再摆就是......
[name="怪异的男人"]这盘棋让我输了田产家业，连家人也流散各地，甚至还有因此丧命的......我自己也身患重病，命不久矣......
[name="怪异的男人"]一盘棋，仅仅是一盘棋，就害得我家破人亡啊......
[name="怪异的男人"]我实在是没法释怀，客官你帮我看看，若是能看出破局之法......
[name="怪异的男人"]......或许还能逆天改命！
[dialog]
[playsound(key="$d_avg_clothmovement")]
[charslot(slot = "m",posfrom = "0,0", posto = "0,-60",duration = 0.8,afrom=1,ato=0)]
[delay(time=1)]
男人刚刚的哭腔极突兀地高亢起来。见望没动，男人一枚一枚地从地上拾起棋子，飞快地摆上棋盘。
[PlaySound(key="$d_avg_weiqi_heavy",channel="1",volume=0.5)]
[PlaySound(key="$d_avg_weiqi_heavy",channel="2",delay=0.5,volume=0.5)]
[PlaySound(key="$d_avg_weiqi_heavy",channel="3",delay=0.8,volume=0.5)]
布局，试探，搏杀，弃子，劫争，交换......
男人的手极快，棋局如同活了一般生长，激烈的战况从边角蔓延至中腹，又跳到尚且空着的另一边，简直令人目眩......
望甚至还没反应过来，男人已经将一枚黑子塞进了他的手里。
[charslot]
[charslot(slot="m",name="avg_npc_1639_1#1$1",bstart=0.4,bend=0.8)]
[name="怪异的男人"]客官，该你了。
[charslot(slot = "m", name = "avg_2027_wang_1#1$2")]
[name="望"]......该怎么下？
[charslot(slot="m",name="avg_npc_1639_1#1$1",bstart=0.4,bend=0.8)]
[name="怪异的男人"]是啊，这怎么下？
[name="怪异的男人"]明明是黑棋和白棋轮流落子，可黑子到了你手里之后，棋局上的黑子一枚都看不到了，这怎么下？
[charslot(slot = "m", name = "avg_2027_wang_1#11$2")]
[name="望"]......荒谬。少陪了。
[charslot(slot="m",name="avg_npc_1639_1#1$1",bstart=0.4,bend=0.8)]
[name="怪异的男人"]客官，这点道理，你不该不懂。
[name="怪异的男人"]这棋枰辽远如深渊，棋枰上的白子每一颗都巨大如山岳，而我不自量力摆在上面的这些黑子......呵，就只是棋子罢了。
[name="怪异的男人"]你我与这棋盘之远，远到观山岳尚且只有拇指大小，观一颗小小的棋子，又怎么可能看得见？
[name="怪异的男人"]我先前尚且勉力支撑，下到此时已经是目眩神迷，算力不支，一招下错......
[charslot(slot = "m", focus = "n")]
高亢的声音又坠回凄惨的哭腔——
[CameraShake(duration=0.3, xstrength=25, ystrength=25, vibrato=30, randomness=90, fadeout=true, block=false)]
[charslot(slot="m",name="avg_npc_1639_1#1$1",bstart=0.4,bend=0.8)]
[name="怪异的男人"]......满盘皆输啊！
[name="怪异的男人"]你看，你看！我给每块棋都起了名字，可每块棋都保不住，每块棋都没有一条活路！
[name="怪异的男人"]这块是朔，这块是望，这块是令，这块是均——
[charslot]
[dialog]
[Effect(name="$e_slash_01_s",layer = 1,rox=-240,roy=-99,roz=-80,y=0,x=0)]
[Effect(name="$e_slash_fold_hit",layer = 2,x=-300,y=-200)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0, block=true)]
[CameraShake(duration=0.5, xstrength=40,ystrength=40, vibrato=30, randomness=90, fadeout=true, block=false)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.03, block=true)]
[PlaySound(key="$swordtsing4")]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0.5, block=true)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0)]
望手里的直刀瞬间出鞘，刺向棋盘上的一颗白子，却只是发出“叮”的一声脆响，刀身弯曲，仿佛真的是在戳刺山岩。
[dialog]
[charslot(slot="m",name="avg_npc_1639_1#1$1",bstart=0.4,bend=0.8,duration=0.5)]
[delay(time=1)]
[name="怪异的男人"]以卵击石，无济于事......
[name="怪异的男人"]悔不当初啊，我当初为什么非要下这局棋，非要......
[dialog]
[Blocker(a=0.5, r=0, g=0, b=0, fadetime=0.5)]
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[PlaySound(key="$d_avg_daggerslow", loop=true, channel="a")]
[delay(time=0.8)]
[StopSound(channel="a", fadetime=0)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1)]
[charslot(slot = "m",posfrom = "0,0", posto = "0,-80",duration = 0.6)]
[playsound(key="$bodyfalldown3")]
[charslot(duration=0.6)]
[delay(time=1)]
直刀转而穿过男人的咽喉，男人委顿在地，伤口处却无半点鲜血流出，甚至哭号的声音反而也越来越大，只是已经辨不清话语。
男人眼里现出某种望分辨不清的神色，像恐慌，也像快意。他直勾勾地盯着望的脸。
望的手下意识地往腰间的书刀上摸，又停在半途。
最终，他沉吟片刻，将另一只手里还夹着的黑子落在枰上。
[dialog]
[charslot]
[PlaySound(key="$d_avg_weiqi_heavy",channel="1",volume=0.7)]
[delay(time=1)]
[charslot(slot = "m", name = "avg_2027_wang_1#11$2",duration=0.5)]
[delay(time=1)]
[name="望"]......满盘皆输？危言耸听。
[name="望"]若走在这里，胜负也不过在五五之间。
[charslot]
[PlaySound(key="$d_avg_smkedspte")]
望的话音刚落，地上的那具身躯就化为一缕轻烟，一旁的棋枰上，原本看不见的黑棋也都显现出来。
[dialog]
[playsound(key="$d_avg_scabbard",delay=1)]
[charslot(slot = "m", name = "avg_npc_2134_1#1$1",duration=1)]
[delay(time=1.5)]
[name="巡视的秉烛人"]望先生！
[charslot(slot = "m", name = "avg_2027_wang_1#1$2")]
[name="望"]你......
[charslot(slot = "m", name = "avg_npc_2134_1#1$1")]
[name="巡视的秉烛人"]刚才见您到了司岁台门口，不知为何却又扭头走了。怕是您也遇上了什么怪事，我来迎一迎。
[charslot(slot = "m", name = "avg_2027_wang_1#1$2")]
[name="望"]怪事？

... (全文30783字符)
```

### level_act49side_03_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[stopmusic]
[dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="58_g1_yusrestaurant",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[animtext(id = "at1", name = "group_location_stamp", style="avg_only_medium", pos = "-400,-200", block = false)]<p=2>望日前两日 辰时</>
[delay(time=3)]
[animtextclean]
[delay(time=1)]
[playMusic(key="$m_sys_act40side_loop", volume=0.6)]
[charslot(slot = "m", name = "avg_npc_1621_1#3$1",posfrom="0,0",posto="-180,0",duration=1.2, isblock=true)]
[delay(time=0.3)]
[charslot(slot = "m", name = "avg_npc_1621_1#10$1")]
[delay(time=0.8)]
[charslot(slot = "m",afrom=1, ato=0, duration=0.8, isblock=true)]
[delay(time=0.5)]
[charslot]
[charslot(slot = "m", name = "avg_npc_1621_1#10$1",posfrom="80,0",posto="200,0",duration=1.2,isblock=true)]
[delay(time=0.3)]
[charslot(slot = "m", name = "avg_npc_1621_1#10$1")]
[delay(time=0.8)]
[charslot(slot = "m", name = "avg_npc_1621_1#10$1",posfrom="200,0",posto="0,0",afrom=1,ato=1,duration=1,isblock=true)]
[delay(time=0.3)]
[charslot(slot = "m", name = "avg_npc_1621_1#10$1")]
[name="老姜"]唉......唉......！  
[charslot(slot = "m", name = "avg_2026_yu_1#1$1")]
[name="余"]叹什么气......牙疼？  
[charslot(slot = "m", name = "avg_npc_1621_1#6$1")]
[name="老姜"]头疼！  
[charslot(slot = "m", name = "avg_2026_yu_1#2$1")]
[name="余"]你要是没事干，就去把过冬的白菜再数一遍。  
[charslot(slot = "m", name = "avg_npc_1621_1#6$1")]
[name="老姜"]你——  
[charslot(slot = "m", name = "avg_npc_1621_1#6$1")]
[name="老姜"]......你还走不走？  
[charslot(slot = "m", name = "avg_2026_yu_1#3$1")]
[name="余"]太阳还没爬上房顶，要走哪儿去？  
[charslot(slot = "m", name = "avg_npc_1621_1#6$1")]
[name="老姜"]还装糊涂！眼见这城里的人都要走光了，你还要留到什么时候？  
[charslot(slot = "m", name = "avg_2026_yu_1#1$1")]
[name="余"]快走光就是还没走光，那要赶路的人，要执勤的士兵，都得吃饭的。  
[charslot(slot = "m", name = "avg_2026_yu_1#7$1")]
[name="余"]再说，店里不正候着一位吗？  
[charslot(slot = "m", name = "avg_npc_1621_1#6$1")]
[name="老姜"]她能一样吗？
[charslot(slot = "m", name = "avg_npc_1621_1#6$1")]
[name="老姜"]现在不走，等这位客人光顾小店的消息传回司岁台，我可就半点忙都帮不上了。  
[charslot(slot = "m", name = "avg_2026_yu_1#1$1")]
[name="余"]烤羽兽刚上架子，后面还排着四五道菜，不着急。
[charslot(slot = "m", name = "avg_npc_1621_1#6$1")]  
[name="老姜"]你真是——！  
[charslot(slot = "m", name = "avg_2026_yu_1#1$1")]
[name="余"]行了行了，一大清早哪儿来这么多操心事。你要真闲不住，就去把店面打开，早市照常营业！
[charslot(slot = "m", name = "avg_npc_1621_1#6$1")]
[name="老姜"]真是心大......  
[dialog]
[PlaySound(key="$d_gen_walk_n", volume=1)]
[charslot(slot = "m", posfrom="0,0",posto="-150,0",duration=1.2, afrom=1, ato=0, isblock=true)]
[charslot]
[delay(time=0.5)]
[charslot(slot = "m", name = "avg_2026_yu_1#1$1", isblock=true)]
[name="余"]不然还能怎么办呢......  
[charslot(slot = "m", name = "avg_2026_yu_1#18$1")]
[name="余"]困了便睡，饿了便吃。谁说得准，何时就念起一口味道？客人指不定马上就来——  
[stopmusic(fadetime=2)]
[dialog]
[charslot]
[PlaySound(key="$d_avg_open_door", volume=1)]
[delay(time=1)]
[PlaySound(key="$d_gen_walk_n", volume=1)]
[delay(time=1.5)]
[charslot(slot = "m", name = "avg_2026_yu_1#1$1")]
[name="余"]客人这不就来了。  
[charslot(slot = "m", name = "avg_2026_yu_1#5$1")]
[name="余"]随便坐随便坐，就是这个点只有早饭供应——  
[dialog]
[charslot]
[playMusic(key="$m_sys_act23side_loop", volume=0.6)]
[charslot(slot="m",name="avg_npc_786_1#1$1",duration=0.8)]
[delay(time=1.5)]
[charslot(slot = "m", name = "avg_2026_yu_1#2$1")]
[name="余"]嗯？是你呀。 
[charslot(slot="m",name="avg_npc_786_1#1$1")]
[name="睚"]你在这里，做什么？  
[charslot(slot = "m", name = "avg_2026_yu_1#1$1")]
[name="余"]你这话问的......我是这家店的掌柜，还能做什么？  
[charslot(slot="m",name="avg_npc_786_1#1$1")]
[name="睚"]......你们这些“人”，竟是一个比一个荒唐。  
[charslot(slot = "m", name = "avg_2026_yu_1#15$1")]
[name="余"]欸欸，你这人说话怎么这么难听？饭一口没吃，倒是先骂起厨子来了。  
[charslot(slot = "m", name = "avg_2026_yu_1#16$1")]
[name="余"]别看我脾气好，你再这样，我也是要赶客的。  
[charslot(slot="m",name="avg_npc_786_1#1$1")]
[name="睚"]......  
[dialog]
[charslot]
[PlaySound(key="$d_gen_walk_n", volume=0.8)]
[delay(time=0.5)]
神情冷漠的女子迈步走进店内，捡了余身边的桌子坐下。  
[dialog]
[PlaySound(key="$d_avg_chairrub", volume=1)]
[charslot(slot="m",name="avg_npc_786_1#1$1",posfrom="0,0",posto="0,-50",duration=1, isblock=true)]
[name="睚"]“余味居”......都是什么味道？  
[charslot]
[charslot(slot = "m", name = "avg_2026_yu_1#1$1")]
[name="余"]那当然是酸咸苦辣，样样都有咯。  
[charslot(slot="m",name="avg_npc_786_1#3$1",posfrom="0,-50",posto="0,-50",afrom=1,ato=1,isblock=true)]
[name="睚"]染上这一身烟火浊气......你很喜欢这些东西？  
[charslot]
[charslot(slot = "m", name = "avg_2026_yu_1#18$1")]
[name="余"]当然啦，不喜欢做饭哪能当得了好厨子嘛。  
[charslot(slot = "m", name = "avg_2026_yu_1#18$1")]
[name="余"]别的道理我也不敢说，可是只论做饭的手艺，那我还是有点自信的。  
[charslot(slot = "m", name = "avg_2026_yu_1#1$1")]
[name="余"]要不，送你两道小菜尝尝呢？  
[charslot(slot = "m", name = "avg_2026_yu_1#1$1")]
[name="余"]人活一世，各种滋味总得试试吧，只盯着一个味道放不下......那岂不是太可惜了？  
[charslot(slot="m",name="avg_npc_786_1#6$1",posfrom="0,-50",posto="0,-50",afrom=1,ato=1,isblock=true)]
[name="睚"]......  
[charslot]
[charslot(slot = "m", name = "avg_2026_yu_1#7$1")]
[name="余"]唔......可是想来想去，这些话，我好像也不能拿来劝你。  
[charslot(slot = "m", name = "avg_2026_yu_1#7$1")]
[name="余"]人们都说，“劝人宽心，天打雷劈”。何况你们之间那些恩恩怨怨，还真不算小......对吧？  
[charslot(slot = "m", name = "avg_2026_yu_1#2$1")]
[name="余"]我其实挺理解你的心情，真的！  
[charslot(slot = "m", name = "avg_2026_yu_1#3$1")]
[name="余"]从你的角度讲，你当然有理由恨炎国，恨人类，恨祂......这样的恨，过了一千年也消不了，也算正常？  
[charslot(slot = "m", name = "avg_2026_yu_1#2$1")]
[name="余"]可如果......你只是这样恨着，却什么都做不了，最后也只能被这一肚子恨给拖垮了......那也挺不划算？  
[charslot(slot = "m", name = "avg_2026_yu_1#1$1")]
[name="余"]这样看来，你和我那位哥哥，也是挺像的......  
[charslot]
[charslot(slot="m",name="avg_npc_786_1#6$1",posfrom="0,-50",posto="0,-50",afrom=1,ato=1,isblock=true)]
[name="睚"]......  
[charslot(slot="m",name="avg_npc_786_1#1$1",posfrom="0,-50",posto="0,-50",afrom=1,ato=1,isblock=true)]
[name="睚"]你竟然......一点都不怕我。  
[charslot]
[charslot(slot = "m", name = "avg_2026_yu_1#1$1")]
[name="余"]有什么好怕的？  
[charslot(slot = "m", name = "avg_2026_yu_1#1$1")]
[name="余"]高官也好，乞丐也罢，即便是天上的神仙，话本里的巨兽，到了店里，便只是一个食客。  
[charslot(slot="m",name="avg_n

... (全文33720字符)
```

### level_act49side_03_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[stopmusic]
[dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="70_g3_tjbookshelf",screenadapt="coverall")]
[BackgroundTween(image="70_g3_tjbookshelf", duration=0.1, xScaleFrom=1.2, yScaleFrom=1.2, xScaleTo=1.2, yScaleTo=1.2, xFrom=80, xTo=80,isblock=true)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[delay(time=1)]
[playMusic(intro="$darkness02_loop",key="$darkness02_loop", volume=0.6)]
[BackgroundTween(image="70_g3_tjbookshelf", duration=0.5, xFrom=80, xTo=30, block=false)]
[delay(time=0.2)]
[charslot(slot = "m", name = "avg_4121_zuole_1#4$1",duration=0.3, block=true)]
[name="左乐"]陈小姐，请将手中之物交还——  
[dialog]
[charslot]
[BackgroundTween(image="70_g3_tjbookshelf", duration=0.5, xFrom=30, xTo=-20, block=true)]
[charslot(slot = "m", name = "avg_1050_chen3_1#11$2",duration=0.3,isblock=true)]
[name="陈"]放开人质！  
[dialog]
[charslot]
[BackgroundTween(image="70_g3_tjbookshelf", duration=0.5, xFrom=-20, xTo=-70, block=true)]
[charslot(slot = "m", name = "avg_npc_1871_1#4$1",focus="all",duration=0.3,isblock=false)]
[charslot(slot = "r", name = "avg_npc_2128_1#1$1",focus="all",posfrom="-110,-90",posto="-110,-90",duration=0.3,isblock=false)]
[charslot(slot = "r", action="zoom", poszoom = "0.5,0.5", scale=0.95, focus="all", isblock=true)]
[name="莫佚"]先把木锁还来！  
[name="陈昭芊"]各位......我们要不先冷静下来，好好谈谈......  
[dialog]
[charslot(slot = "m", focus="n")]
[name="？？？"]远远就听见了楼下的声响，还以为是某处的伥怪复又暴动。  
[name="？？？"]不料是三位客人，在此切磋武艺。  
[dialog]
[charslot]
[PlaySound(key="$d_avg_woodfloor_fts", volume=1)]
[charslot(slot = "r", name = "avg_npc_295_1#1$1",duration=1,isblock=true)]
[delay(time=0.5)]
[PlaySound(key="$d_gen_walk_n", volume=1)]
[charslot(slot = "l", name = "avg_4121_zuole_1#10$1",posfrom="-100,0",posto="0,0",duration=0.8,focus="l",isblock=true)]
[name="左乐"]梁大人？
[charslot(slot = "r", name = "avg_npc_295_1#1$1",focus="r")]
[name="梁洵"]左公子，别来无恙。  
[dialog]
[charslot]
[charslot(slot = "m", name = "avg_1050_chen3_1#1$2")]
[name="陈"]（左公子......似乎在罗德岛上听到过。）
[dialog]
[charslot]
[charslot(slot = "l", name = "avg_4121_zuole_1#10$1",focus="r")]
[charslot(slot = "r", name = "avg_npc_295_1#7$1",focus="r",isblock=true)]
[name="梁洵"]阁中祸乱难靖，梁某正忧心该如何解决......  
[charslot(slot = "r", name = "avg_npc_295_1#8$1",focus="r",isblock=true)]
[name="梁洵"]见到司岁台派左公子前来协理，总算是能安心了。  
[charslot(slot = "l", name = "avg_4121_zuole_1#1$1",focus="l")]
[name="左乐"]我......  
[charslot(slot = "r", name = "avg_npc_295_1#1$1",focus="r",isblock=true)]
[name="梁洵"]......莫非梁某误会了？  
[charslot(slot = "l", name = "avg_4121_zuole_1#1$1",focus="l")]
[name="左乐"]监正大人自有安排，不劳梁大人费心。既然我此刻在此，自当尽力协助。  
[charslot(slot = "r", name = "avg_npc_295_1#1$1",focus="r",isblock=true)]
[name="梁洵"]那公子缉拿这位面生的小姐，也是监正大人的授意？  
[charslot(slot = "l", name = "avg_4121_zuole_1#1$1",focus="l")]
[name="左乐"]她叫莫佚......是山海众的一员。数日之前在邙山镇中惹生事端，如今又在伥怪横行之时现身百灶。  
[charslot(slot = "l", name = "avg_4121_zuole_1#1$1",focus="l")]
[name="左乐"]行迹可疑，在下必须彻查。  
[dialog]
[charslot]
[charslot(slot = "m", name = "avg_npc_1871_1#1$1",focus="all")]
[charslot(slot = "r", name = "avg_npc_2128_1#1$1",focus="all",posfrom="-110,-90",posto="-110,-90",isblock=false)]
[charslot(slot = "r", action="zoom", poszoom = "0.5,0.5", scale=0.95, focus="all", isblock=true)]
[name="莫佚"]左秉烛还真是不领情......  
[dialog]
[charslot]
[charslot(slot = "l", name = "avg_4121_zuole_1#1$1",focus="r",isblock=true)]
[charslot(slot = "r", name = "avg_npc_295_1#1$1",focus="r",isblock=true)]
[name="梁洵"]山海众......  
[dialog]
[charslot]
[charslot(slot = "m", name = "avg_npc_1871_1#9$1",focus="all",posfrom="0,0",posto="-20,0",duration=0.5,isblock=false)]
[charslot(slot = "r", name = "avg_npc_2128_1#1$1",focus="all",posfrom="-110,-90",posto="-130,-90",duration=0.5,isblock=false)]
[charslot(slot = "r", action="zoom", poszoom = "0.5,0.5", scale=0.95, focus="all", isblock=true)]
[name="莫佚"]（挟紧陈昭芊，警惕地后退）
[dialog]
[charslot]
[charslot(slot = "l", name = "avg_4121_zuole_1#1$1",posfrom="0,0",posto="0,0",focus="r",isblock=true)]
[charslot(slot = "r", name = "avg_npc_295_1#1$1",posfrom="0,0",posto="0,0",focus="r",isblock=true)]
[name="梁洵"]城中戒严，山海众如果在这里只是为了惹生事端......莫小姐，反倒称得上一句“勇气可嘉”了。  
[dialog]
[charslot]
[charslot(slot = "m", name = "avg_npc_1871_1#1$1",focus="all")]
[charslot(slot = "r", name = "avg_npc_2128_1#1$1",focus="all",posfrom="-110,-90",posto="-110,-90",isblock=false)]
[charslot(slot = "r", action="zoom", poszoom = "0.5,0.5", scale=0.95, focus="all", isblock=true)]
[name="莫佚"]哈，你看上去比这位秉烛人还要木讷一点，没想到还算明事理。  
[name="莫佚"]那能不能麻烦你和这位左公子说说，让他先不要一门心思和我过不去。  
[dialog]
[charslot]
[charslot(slot = "l", name = "avg_4121_zuole_1#1$1",focus="r")]
[charslot(slot = "r", name = "avg_npc_295_1#1$1",focus="r",isblock=true)]
[name="梁洵"]梁某人微言轻，只能恳请莫小姐放开这位......在下的同僚。  
[charslot(slot = "r", name = "avg_npc_295_1#7$1",focus="r",isblock=true)]
[name="梁洵"]“遍览山川湖泽，穷究自然物理”，这是千年前山海众最初的信条。至于伤及无辜，应当也不是莫小姐的本意。  
[charslot(slot = "l", name = "avg_4121_zuole_1#6$1",focus="l")]
[name="左乐"]梁大人？  
[dialog]
[charslot]
[charslot(slot = "m", name = "avg_npc_1871_1#9$1",focus="all")]
[charslot(slot = "r", name = "avg_npc_2128_1#1$1",focus="all",posfrom="-110,-90",posto="-110,-90",isblock=false)]
[charslot(slot = "r", action="zoom", poszoom = "0.5,0.5", scale=0.95, focus="all", isblock=true)]
[name="莫佚"]你怎么会知道这些事......  
[name="莫佚"]......哼。  
[PlaySound(key="$d_avg_drawsword")]
[PlaySound(key="$d_avg_exsheath",delay=0.5)]
片刻沉默之后，莫佚还刃入鞘，又将身前的典水官轻轻向前推了推。  
[dialog]
[charslot(slot = "r", name = "avg_npc_2128_1#1$1",posfrom="-130,-90",posto="-90,-90",afrom=1, ato=0,duration=0.5,isblock=true)]
[charslot]
[PlaySound(key="$d_avg_clothmovement_heavy2", volume=1)]
[charslot(slot = "r", name = "avg_1050_chen3_1#1$2",isblock=false)]
[charslot(slot="l",name="avg_npc_2128_1#1$1",posfrom="-80,0",posto="0,0",duration=0.3,isblock=true)]
[delay(time=0.5)]
[charslot(slot = "r", name = "avg_1050_chen3_1#1$2",focus="r",isblock=true)]
[name="陈"]你没事？  
[c

... (全文22071字符)
```

### level_act49side_04_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Delay(time=1)]
[Background(image="70_g7_suilingcore",screenadapt="coverall")]
[Blocker(a=0.6, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]
[playMusic(key="$m_sys_act14mini_loop", volume=0.6)]
[Subtitle(text="无故的执念，无根的挣扎，无谓的牺牲......自从数百年前起，你就一直忧心如焚。", x=300, y=330, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="我的醒觉被你划分成四五百个周期，每个周期再分为十二，再分为三十，再分，再分......", x=300, y=330, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="每一分，每一秒，你都在盘算，都在恐惧着那个不知何时到来的“大限”......", x=300, y=330, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="不过几场梦的时间罢了，我的我何时浅陋到如此地步？", x=300, y=330, alignment="center", size=24, delay=0.04, width=700)]
[subtitle]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot(slot = "m", name = "avg_2027_wang_1#11$1",duration=1)]
[delay(time=1.5)]
[name="望"]若是没有一个意志，没有一个主体，没有一个愿意为时间定下刻度的人，那么光阴只是无谓的轮转......
[name="望"]一如你在陵中度过的岁月。
[name="望"]无知无觉的你，又有何资格定义这段时间？
[Dialog]
[Blocker(a=0.6, r=0, g=0, b=0, fadetime=0.5, block=true)]
[Subtitle(text="呵......无非是梦而已。", x=300, y=330, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="为了注定消失的结局而歇斯底里的梦，就有资格了吗？", x=300, y=330, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle]
[stopmusic(fadetime=2)]
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[delay(time=1)]
[Background(image="70_g9_oldbattlefield",screenadapt="coverall")]
[playsound(key="$d_avg_battlepresent", loop=true, channel="bgs",volume=0)]
[SoundVolume(volume=0.3, channel="bgs",fadetime=2)]
[playMusic(key="$m_avg_riversnow_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[delay(time=1)]
[animtext(id = "at1", name = "group_location_stamp", style="avg_only_heavy", pos = "-400,-200", block = false)]<p=1>759年</>
[delay(time=3)]
[animtextclean]
[delay(time=1)]
[charslot(slot = "m", name = "avg_npc_794_1#1$1",duration=0.5)]
[delay(time=1)]
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="决绝的山海众成员"]山海八荒，尽归其主！
[dialog]
[playsound(key="$d_avg_metallicclick",channel="2")]
[playsound(key="$d_avg_spear")]
[charslot(slot = "r", name = "avg_npc_2133_1#1$1",posfrom = "200,0", posto = "100,0",duration = 0.3)]
[Blocker(a=0.5, r=1, g=1, b=1, fadetime=0.3, block=true)]
[CameraShake(duration=0.2, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[charslot(slot = "m",posfrom = "0,0", posto = "-300,0",duration = 0.5)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.5, block=true)]
[playsound(key="$bodyfalldown3",channel="2")]
[charslot(slot = "m",posfrom = "-300,0", posto = "-300,-50",duration = 0.3)]
[delay(time=0.5)]
[charslot(slot = "r", focus="r")]
[name="大炎边军"]妖言惑众！
[dialog]
[charslot(slot ="m", action="shake", power=5, times=30, duration=0.6, block=true)]
[charslot(slot = "m",posfrom = "-300,-50", posto = "-300,0",duration = 0.6)]
[delay(time=1)]
[charslot(slot = "m", focus="m")]
[name="决绝的山海众成员"]呼、呼......
[charslot(slot = "r", focus="r")]
[name="大炎边军"]放下武器，还能饶你不死！
[charslot(slot = "m", focus="m")]
[name="决绝的山海众成员"]放下武器？
[name="决绝的山海众成员"]我们就是要让炎氏一脉知道，矩兽已醒，他自以为可以千秋万代的江山，和这无限天地相比，终究不过黄粱一梦！
[name="决绝的山海众成员"]山海八荒，尽归——
[dialog]
[playsound(key="$d_avg_knife",channel="1")]
[charslot(slot = "r",posfrom = "100,0", posto = "-300,0",duration = 0.3)]
[playsound(key="$d_avg_spear")]
[Blocker(a=0.2, r=1, g=0, b=0, fadetime=0.2, block=true)]
[charslot(slot = "m",posfrom = "-300,0", posto = "-380,0",duration = 0.5)]
[charslot(slot ="m", action="shake", power=5, times=50, duration=0.5, block=true)]
[Dialog]
[stopmusic(fadetime=2)]
[StopSound(channel="bgs", fadetime=2)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[delay(time=1)]
[playsound(key="$d_avg_crwddiscuss_inside", loop=true, channel="bgs",volume=0)]
[SoundVolume(volume=0.5, channel="bgs",fadetime=2)]
[Background(image="35_g7_zuosroom",screenadapt="coverall")]
[playMusic(key="$m_avg_yumennormal_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[delay(time=1)]
[playsound(key="$d_avg_plateplace")]
[delay(time=1)]
[name="略带酒意的钦差"]来，喝！
[charslot(slot = "m", name = "avg_npc_2133_1#1$1")]
[name="受宠若惊的士兵"]怎么敢让大人为我斟酒——
[charslot(slot = "m", focus = "n")]
[name="略带酒意的钦差"]切不可妄自菲薄！
[name="略带酒意的钦差"]时隔数百年，我辈终于诛杀了那场狩猎最后的遗害，经此一役，大炎疆域彻底无忧矣！
[name="略带酒意的钦差"]这一杯酒，我敬诸位！
[Dialog]
[charslot(slot = "m", focus = "all")]
[playsound(key="$pourwater")]
[delay(time=1.5)]
[charslot(slot = "m", name = "avg_npc_2133_1#1$1")]
[name="受宠若惊的士兵"]谢大人赐酒！
[Dialog]
[charslot(duration=1)]
[delay(time=2)]
[charslot(slot = "r", name = "avg_2024_chyue_1#1$1",duration = 1)]
[charslot(slot = "l", name = "avg_2027_wang_1#1$2",duration = 1)]
[delay(time=2)]
[charslot(slot = "m", focus = "n")]
[name="略带酒意的钦差"]当然，还有二位先生。
[name="略带酒意的钦差"]朔先生身先士卒以一当千，大振军心；望先生排兵布阵更是算无遗策。 
[name="略带酒意的钦差"]今日诛杀矩兽，二位先生才当居首功。
[name="略带酒意的钦差"]这一杯酒，我敬二位。
[Dialog]
[charslot(slot = "m", focus = "all")]
[playsound(key="$d_avg_plateplace")]
[delay(time=1)]
[charslot(slot = "r", name = "avg_2024_chyue_1#1$1",focus="r")]
[name="朔"]......多谢。
[charslot(slot = "l", name = "avg_2027_wang_1#1$2",focus="l")]
[name="望"]......
[charslot(slot = "m", focus = "n")]
[name="略带酒意的钦差"]望先生，机会难得，有些话我须得直言。
[name="略带酒意的钦差"]我很清楚，朝中曾有不少对先生的流言中伤。大多是质疑先生非我族类，心有不轨。
[name="略带酒意的钦差"]但先生却是安耐毁誉，为大炎立下不世之功。如此高风亮节，着实令人敬佩。
[name="略带酒意的钦差"]我知道，如今司岁台对各位的限制的确不能说松懈，甚至连你们手足团聚也要干涉，未免不近人情。
[name="略带酒意的钦差"]我这次回去，一定请奏陛下，特准诸位合家欢聚......
[Dialog]
[StopSound(channel="bgs", fadetime=2)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[delay(time=1)]
[Background(image="70_g11_oldpavilion",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[delay(time=1)]
[name="酩酊大醉的钦差"]今天确实高兴，我自觉酒量不错，也已经不胜酒力了......
[name="酩酊大醉的钦差"]说实话，出征之前，上面是吩咐过，让我......看着两位，别出什么岔子的。
[name="酩酊大醉的钦差"]可今天一战下来，二位都......证明了自己，忠心不二，令人......敬佩！
[nam

... (全文17348字符)
```

### level_act49side_04_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Delay(time=1)]
[CameraEffect(effect="Grayscale", fadetime=0, keep=true, initamount=0, amount=1, block=true)]
[Background(image="bg_forest",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=1)]
[CameraEffect(effect="Grayscale", fadetime=2, amount=0, block=true)]
[animtext(id = "at1", name = "group_location_stamp", style="avg_only_heavy", pos = "-400,-200", block = false)]<p=1>759年</>
[delay(time=3)]
[animtextclean]
[delay(time=1)]
[playMusic(intro="$darkness01_intro",key="$darkness01_loop", volume=0.6)]
[charslot(slot="m",name="avg_4221_ju_1#1$1",duration=1.5)]
[delay(time=2)]
[name="矩"]右脚......嗯，也差不多磨好了。
[name="矩"]好不容易重塑了身形，做的第一件事，竟然是替人赴死......
[name="矩"]该上路了——
[dialog]
[charslot]
[playsound(key="$d_avg_walkmeadow")]
[charslot(slot="m",name="avg_2027_wang_1#1$2",duration=1)]
[delay(time=2.5)]
[charslot(slot="m",name="avg_4221_ju_1#6$1")]
[name="矩"]是你。
[charslot(slot="m",name="avg_4221_ju_1#3$1")]
[name="矩"]不对，你是祂，但你又不是祂，你是......嘶......
[name="矩"]有趣，有趣。
[charslot(slot="m",name="avg_2027_wang_1#1$2")]
[name="望"]往日的仇敌变成你眼前这副四分五裂的模样，过去的追随者也成了一班乌合之众，你感想如何？
[charslot(slot="m",name="avg_4221_ju_1#2$1")]
[name="矩"]谈何仇敌？
[name="矩"]无非做了个梦，耽搁了未竟之事而已。梦醒前逃得一命，没死在大狩猎的铁蹄之下，梦醒后死在这里，倒也不坏。
[charslot(slot="m",name="avg_4221_ju_1#1$1")]
[name="矩"]但你不该在这里悄无声息地杀死我。你最好让我死在炎国的军队阵前，不然，还会有一班又一班的疯癫狂人打着我的名号送死。
[name="矩"]那才是我不愿意见到之事。
[charslot(slot="m",name="avg_2027_wang_1#1$2")]
[name="望"]......活不下去的人自然会揭竿而起，究其原因，未必与你有关。
[name="望"]我不会杀你。正相反，你不能死。
[charslot(slot="m",name="avg_4221_ju_1#1$1")]
[name="矩"]你不诛我这个“首恶”，反倒要来帮我？倒是有趣。
[name="矩"]那你想怎么处置那帮自诩的“山海众”？虽说只是一鳞半爪，可老木匠的法术毕竟流传到了他们手里，和我不能说没有情分。
[charslot(slot="m",name="avg_2027_wang_1#1$2")]
[name="望"]你走，他们自然会活下来。
[charslot(slot="m",name="avg_4221_ju_1#1$1")]
[name="矩"]怎讲？
[charslot(slot="m",name="avg_2027_wang_1#1$2")]
[name="望"]炎国的这支军队要拿的是你，不是他们。而你要走，并不困难。
[name="望"]若是真有什么阻碍，我会帮你。
[charslot(slot="m",name="avg_2027_wang_1#1$2")]
[name="望"]至于这支山海众，他们大概还能支撑两日。两天过后，他们会全军覆没，炎国的军队也会折损三成。
[name="望"]若是你留在这儿替他们赴死，他们只会更加狂热，死战不退。
[name="望"]而你一走，他们会逃，炎国军队也会因达成目的而罢兵。
[name="望"]你想要止战，唯有此路。
[charslot(slot="m",name="avg_4221_ju_1#4$1")]
[name="矩"]你果然是祂......不，你不完全像祂。在人心筹谋一道，你强过祂十倍。
[name="矩"]我今天欠了你这么大的恩情，你又想从我这儿得到什么？
[charslot(slot="m",name="avg_2027_wang_1#1$2")]
[name="望"]一手闲棋而已，有用则用，无用也就罢了。
[charslot(slot="m",name="avg_4221_ju_1#1$1")]
[name="矩"]呵......你这样讲，反倒让我不甘心了。
[name="矩"]我答应你，这一份恩情，我将来必定还你。
[charslot(slot="m",name="avg_2027_wang_1#1$2")]
[name="望"]你不知我要做的事，又如何谈得上帮我？
[charslot(slot="m",name="avg_4221_ju_1#3$1")]
[name="矩"]连巨兽都是你口中的“闲棋”，你所谋算的，必定不在人，而在己。所谓四分五裂，究竟裂成了多少？
[charslot(slot="m",name="avg_2027_wang_1#1$2")]
[name="望"]......十二。
[charslot(slot="m",name="avg_4221_ju_1#1$1")]
[name="矩"]最终留下的，到底是“十二”，还是那个“一”，你所关心的，想来也只有这件事了。
[name="矩"]姑且给阁下一个建议，独木难成林，你想做的事可谓逆天而行，最好多寻助力。
[name="矩"]你也应当多去问问你那些兄弟姐妹，是否能给出些和你不尽相同的解法。你们这样的存在，本就不可以寻常的道理法度考量。
[name="矩"]但愿你能寻到一个解法，也算为这世上生灵除去了一桩祸患......
[charslot(slot="m",name="avg_2027_wang_1#4$2")]
[name="望"]......
[Dialog]
[CameraEffect(effect="Grayscale", fadetime=1, keep=true, initamount=0, amount=1, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[delay(time=1)]
[CameraEffect(effect="Grayscale", fadetime=0, amount=0, block=true)]
[charslot(slot = "l", name = "avg_2027_wang_1#1$2")]
[charslot(slot = "r", name = "avg_2023_ling_1#1$1")]
[Background(image="70_g11_oldpavilion",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[delay(time=1)]
[charslot(slot = "r", name = "avg_2023_ling_1#7$1",focus="r")]
[name="令"]只要我的这个梦没有磨损殆尽，只要我的梦里还有我们十二个人，我们就永远不会彻底消失。
[name="令"]虚则实之，大道逍遥，大抵如是。
[charslot(slot = "l", name = "avg_2027_wang_1#11$2",focus="l")]
[name="望"]我却只听见你想背上一副轭，一副最重的轭。
[name="望"]你只是把一家人全部拖入了岁兽将醒未醒的那一刻，又把那一刻在你自己清醒的梦里延展为永恒......
[name="望"]可你又能迁延多久？
[charslot(slot = "r", name = "avg_2023_ling_1#8$1",focus="r")]
[name="令"]把这人间的所有佳酿都喝到尽兴，怎么样？
[charslot(slot = "l", name = "avg_2027_wang_1#1$2",focus="l")]
[name="望"]......我还是希望能有一条不必如此困顿的路。
[charslot(slot = "r", name = "avg_2023_ling_1#1$1",focus="r")]
[name="令"]我们和祂本就谈不上对等，若不困顿，又怎么可能在死中求活？
[charslot(slot = "l", name = "avg_2027_wang_1#1$2",focus="l")]
[name="望"]我懂。可......
[charslot(slot = "l", name = "avg_2027_wang_1#4$2",focus="l")]
[name="望"]......救矩兽并非我一时兴起。
[charslot(slot = "r", name = "avg_2023_ling_1#1$1",focus="r")]
[name="令"]怎么又说起这个？你做事当然有原因，只是你往往看得太远，却忘了近处的......
[charslot(slot = "r", name = "avg_2023_ling_1#3$1",focus="r")]
[name="令"]等等，你是说？
[charslot(slot = "l", name = "avg_2027_wang_1#1$2",focus="l")]
[name="望"]我是受人所托。
[charslot(slot = "r", name = "avg_2023_ling_1#1$1",focus="r")]
[name="令"]谁？
[charslot(slot = "l", name = "avg_2027_wang_1#1$2",focus="l")]
[name="望"]后兽。
[charslot(slot = "r", name = "avg_2023_ling_1#9$1",focus="r")]
[name="令"]那位老头，竟然也还活着？
[charslot(slot = "l", name = "avg_2027_wang_1#1$2",focus="l")]
[name="望"]祂没有像山海众那样的拥趸，也因此避开了大炎的监视。我帮祂脱离了大炎可触及的范围之后，祂才告诉我矩兽的事。
[charslot(slot = "r", name = "avg_2023_ling_1#1$1",focus="r")]
[name="令"]......这件事，告诉大哥了吗？
[charslot(slot = "l", name = "avg_2027_wang_1#1$2",focus="l")]
[name="望"]未曾。
[charslot(slot = "r", name = "avg_2023_ling_1#1$1",focus="r")]
[name="令"]......该乖觉的时候，你倒也挺乖觉的。
[charslot(slot = "l", name = "avg_2027_wang_1#1$2",focus="l")]
[name="望"]我庇护后兽离开炎国地界后，也曾向祂询问破局之法，祂说的一句话的确让我有所启发。
[charslot(slot = "l", name = "avg_2027_wang_1#3$2",focus="l")]
[name="望"]“我未必在祂梦中，祂未尝不在我梦中。”
[charslot(slot = "r", name = "avg_2023_ling_1#8$1",focus="r")]
[name="令"]哈，那个老头子还是这般有趣，有机会的话还真想和祂对饮一回了。
[charslot(slot = "l", name = "avg_2027_wang_1#1$2",focus="l")]
[name="望"]岁兽最近异常活跃，很有可能，是梦中有什么东西正在惊扰祂，才大大加快了祂醒来的速度。
[name="望"]尽管只是治标之策，但我若是能入祂梦中，看清究竟是何物作祟......
[charslot(slot = "r", name = "avg_2023_ling_1#1$1",focus="r")]
[name="令"]招招行险，你不怕惊醒祂？
[charslot(slot = "l", name = "avg_2027_wang_1#1$2",focus="l")]
[name="望"]祂七十年后醒来，还是七天后醒来，于我们而言，真有那么大区别吗？
[charslot(slot = "r", name = "avg_2023_ling_1#1$1",focus="r")]
[na

... (全文23227字符)
```

### level_act49side_05_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Delay(time=2)]
[animtext(id = "at1", name = "group_location_stamp", style="avg_only_heavy", pos = "-400,-200", block = false)]<p=1>962年</>
[delay(time=3)]
[animtextclean]
[delay(time=1)]
[playMusic(key="$m_avg_yumennormal_loop", volume=0.6)]
陛下......臣等只能陪同您到这里了。
这扇门后的房间，整个炎国，只有您一人可进去了。
三位先生何必如此惶恐，不过是一扇门而已。
陛下，这扇门后是大炎最深的秘密，也是大炎所拥有的，最强大的权柄......
[dialog]
[Delay(time=1)]
......是吗。
[dialog]
[Delay(time=1)]
十七岁的真龙走下最后几级台阶。
他回头看向身后毕恭毕敬的三公，暗自撇了撇嘴，不以为然地推开那扇门。
他听说过那扇门后面是什么，这个国家上千年来流传着无数传说与故事——
“地泽万民，赐此奇石；天祐炎祚，得诛孽岁。”
有人说，炎国千年繁荣由此物开始，也有人说，真龙的权柄不过是假于此物。
可是已经近百年，不曾有人目睹过它的真容。
新近践祚的真龙有些兴奋，他的指尖在微微颤抖。
炎国土地上的一切都将为大炎的兴盛强大服从他的指挥——
......何况一枚小小的结晶。
于是，他推开了门。
[playsound(key="$d_avg_gateopen")]
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[bgeffect(name="$eb_070cg_originium",layer=1)]
[Image(image="70_i06", xScale=1, yScale=1,screenadapt="coverall")]
[Background]
[Blocker(a=0, r=0, g=0, b=0, fadetime=3, block=true)]
野心勃勃如他，也不得不在庞大的空间与慑人的光亮前驻足。
这甚至并非最初的源石本体，而是人在其上施加的造物，是无数天师千百年来加诸其上的限制和引导。
[Dialog]
[Blocker(a=0.6, r=0, g=0, b=0, fadetime=1.5, block=true)]
[Subtitle(text="既都百灶，发幽谷，治岁陵，徙岁躯，以灾炁之镇岁识，而镇岁之竭灾炁也。帝犹不自安，问策天师府，以图永宁。", x=300, y=320, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="期年得术，锻炼灾炁，以为斧钺。唯灾炁凶戾，须天师百人，身殒为引，次以甲兵万员，形灭为刃，当可诛之。苟建全功，而百灶不免。", x=300, y=320, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="帝曰：“残民以逞，君子之不屑，况于我乎！殉人之为引，吾一人可矣。捐躯以为刃，其俟我后昆耳，又何求诸人！”", x=300, y=320, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="逾年，真龙以身殉，术乃成。储君涕泣，名之“不反”。", x=300, y=320, alignment="center", size=24, delay=0.04, width=700)]
[subtitle]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1.5, block=true)]
[name="真龙"]......不反，不返。
[name="真龙"]先祖以生命为引，将人殉的代价系于当朝真龙一身。后世真龙以捐躯做交换，便能动用这枚源石的极大威能。
[name="真龙"]不亲自来看看，还真不知道这东西居然如此巨大......
[name="真龙"]可与整个大炎，与整个大炎的未来相比，也不过是一枚小小的结晶罢了。
[name="真龙"]掌握了这件奇物，大炎本应该做到更多。
[name="真龙"]数百年来，为了镇压那昏睡不醒的凶兽，我们究竟耗费了多少能量，这些能量，又足以驱动多少军队前进，机器轰鸣？
[name="真龙"]我怎么可以容忍......继续这般碌碌无为？
[Dialog]
[delay(time=1)]
真龙又在巨大的装置前驻足了一会儿，他差不多已经习惯了炽热的光芒，他甚至开始觉得......无趣。
他想起三公方才恭敬的神情，不禁觉得好笑，又在想着等会见到仍然侍立门外的他们，应该如何不失礼节地，嘲弄他们的怯懦。
想着想着，他忽然想起那个“规矩”，将三公隔绝在外，让自己独自面对眼前巨构的“规矩”。
让这个装置，与自己的性命紧密连结的规矩。
他哑然失笑。
......谁言真龙执掌天下的权柄，竟要依托于这一枚，小小的结晶？
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[image]
[bgeffect]
[delay(time=1)]
[Background(image="58_g5_dragonpalace",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[delay(time=1)]
[playsound(key="$d_avg_summercicada", loop=true, channel="bgs",volume=0)]
[SoundVolume(volume=0.2, channel="bgs",fadetime=2)]
[dialog]
[delay(time=1)]
[name="真龙"]......我刚刚执掌政务，许多问题还不甚清楚，这段时日要多依仗三位先生了。
[name="真龙"]我想请教各位，我大炎数百年繁荣昌盛，国泰民安，可为何还有人兴兵作乱？
[name="真龙"]是如今还有大炎福泽不曾遍及的土地，还是有不服王化之逆民？
[dialog]
[SoundVolume(volume=0.5, channel="bgs",fadetime=2)]
[delay(time=2)]
一片沉默。
[SoundVolume(volume=0.2, channel="bgs",fadetime=2)]
[name="真龙"]各位不回答于我，那我只好自行决断了。
[name="真龙"]要使恩泽遍布，使大炎无一人有衣食之忧；要以天威教化，令大炎无一人有不臣之心。
[name="真龙"]故而征讨北方逆党，兴建百灶的移动城市，两件事没有先后，一件都不得耽误。
[name="真龙"]具体的方案，钱粮人手如何调度，各位回去之后，再召集六部商议。月底前得出一个结果。
[name="真龙"]今天就到这儿吧。
[charslot]
[playsound(key="$d_avg_clothmovement",volume=0.7,channel="2")]
帷幕对面的三人齐声应诺、行礼，而后告退。
[stopmusic(fadetime=2)]
[dialog]
[delay(time=1.5)]
过不多时。
[dialog]
[StopSound(channel="bgs", fadetime=2)]
[playsound(key="$d_gen_walk_n",volume=0.7)]
[delay(time=1.5)]
[name="真龙"]哦，你来了。
[dialog]
[charslot]
[playMusic(intro="$ponder_intro",key="$ponder_loop", volume=0.6)]
[charslot(slot="m",name="avg_2027_wang_1#1$2",duration=1)]
[delay(time=2)]
[name="望"]......见过陛下。
[charslot(slot = "m", focus = "n")]
[name="真龙"]我很早便听闻大炎有十二位“能人异士”，为大炎建功颇多，我好奇许久。
[name="真龙"]我也因此阅读过司岁台的卷宗，发觉有一事有趣。
[name="真龙"]不论是请功的战报，还是可疑的记录。
[name="真龙"]你的名字，是最多被提及的。
[charslot(slot="m",name="avg_2027_wang_1#1$2")]
[name="望"]......
[charslot(slot = "m", focus = "n")]
[name="真龙"]呵，不过现在看来，原来你的模样，好像也没有传闻中那么可怕。
[charslot(slot="m",name="avg_2027_wang_1#1$2")]
[name="望"]不知陛下召见，所为何事？
[charslot(slot = "m", focus = "n")]
[name="真龙"]许多人说，你是整个大炎最能谋善断的人。
[name="真龙"]我想让你算一算，如今炎国面临的两桩难事，应当如何处置？
[charslot(slot="m",name="avg_2027_wang_1#1$2")]
[name="望"]北方叛乱称不上大患，乱党只是在当地享有名望，无力扩张，但也不宜坐视其势力稳固。
[name="望"]只要整备五万甲士，半年份的粮草，便可一战功成。
[charslot(slot = "m", focus = "n")]
[name="真龙"]比起兵部给出的数字，你倒是乐观许多......不过想来在这一件事上，我更有理由相信你的判断。
[name="真龙"]好，那另一桩呢？
[charslot(slot="m",name="avg_2027_wang_1#1$2")]
[name="望"]至于要将百灶改建为移动城市......我听闻工部已经论证过建造技术理论可行，剩下的，也只有钱粮物资，还有......
[charslot(slot="m",name="avg_2027_wang_1#3$2")]
[name="望"]......百灶城下的岁陵。
[charslot(slot = "m", focus = "n")]
[name="真龙"]是了......你也知道，问题所在。
[name="真龙"]今天召你觐见，只是为了这一件事。
[name="真龙"]你准备如何“除岁”？
[charslot(slot="m",name="avg_2027_wang_1#6$2")]
[name="望"]......
[charslot(slot="m",name="avg_2027_wang_1#1$2")]
[name="望"]陛下熟读司岁台卷宗，应当也知晓......“我们”与岁兽原本一体，存亡与共。
[charslot(slot="m",name="avg_2027_wang_1#11$2")]
[name="望"]陛下的意思，是在问我，要如何杀死“我们”？
[charslot(slot = "m", focus = "n")]
[name="真龙"]大炎在意的，只有那个独一无二的“岁”而已。
[charslot(slot="m",name="avg_2027_wang_1#1$2")]
[name="望"]......
[charslot(slot="m",name="avg_2027_wang_1#3$2")]
[name="望"]陛下应当清楚数百年前炎国为那场围猎付出的代价。
[name="望"]如果执意要以强硬手腕将岁兽消灭，七成的军队，一成的人口，接下来五十年内无休止的动乱，就是炎国要为这一战付出的代价。
[charslot(slot = "m", focus = "n")]
[name="真龙"]若果真如此，大炎便更没有余力去为你们十二个思索出一条生路了。
[charslot(slot="m",name="avg_2027_wang_1#11$2")]
[name="望"]......
[charslot(slot = "m", focus = "n")]
代理人抬起头，迎上了帷幕后的人俯视的目光。
[name="真龙"]我既已决意要为大炎除去千年沉疴，就不会畏惧任何代价。
[name="真龙"]消灭岁兽，将原本用来镇岁的庞大能源充分利用。制造城市上百座，战舰万余艘，再开大炎千年盛世。
[name="真龙"]可惜，念在你们过往功绩，我原本期待，炎国将来的盛世图景中，也有你们十二人的位置。
[charslot(slot="m",name="avg_2027_wang_1#11$2")]
[name="望"]......
[charslot(slot="m",name="avg_2027_wang_1#3$2")]
[name="望"]如果陛下真的有意务实解决岁兽之患，而非贪功冒进......
[name="望"]......我或许还有手段。
[charslot(slot = "m", focus = "n")]
[name="真龙"]......哦？
[charslot(slot="m",name="avg_2027_wang_1#1$2")]
[name="望"]我们十二人与岁兽本为一体，无论祂苏醒还是身殒，我们都会消亡。
[charslot(slot="m",name="avg_2027_wang_1#11$2")]
[name="望"]但我或许可以......取而代之。
[cha

... (全文20617字符)
```

### level_act49side_05_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Delay(time=2)]
[Background(image="70_g11_oldpavilion",screenadapt="coverall")]
[animtext(id = "at1", name = "group_location_stamp", style="avg_only_heavy", pos = "-400,-200", block = false)]<p=1>965年</>
[delay(time=3)]
[animtextclean]
[delay(time=1)]
[name="望"]......情况我清楚了。
[name="望"]这件事绝对不可让旁人知晓，要额外当心。
[name="望"]你还得再帮我，去做一件事。
[dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]
[playMusic(key="$wasteland_loop", volume=0.6)]
[charslot(slot = "left", name = "avg_npc_2126_1#1$1",duration = 1)]
[charslot(slot = "right", name = "avg_npc_2125_1#7$1",duration = 1)]
[delay(time=2)]
[charslot(slot = "left", name = "avg_npc_2126_1#1$1",focus="l")]
[name="均"]大理寺已经开始追查书刀失窃的时间前后，所有接近过天镜阁的人了。
[charslot(slot = "right", name = "avg_npc_2125_1#4$1",focus="r")]
[name="颉"]......
[name="颉"]除了我们兄弟姐妹，整个大炎知道有这柄书刀存在的，不超过一手之数。
[charslot(slot = "left", name = "avg_npc_2126_1#19$1",focus="l")]
[name="均"]是啊，和我担忧的一点不差。
[charslot(slot = "left", name = "avg_npc_2126_1#17$1",focus="l")]
[name="均"]颉，如果有人想对你不利，我不会坐视不管。
[charslot(slot = "right", name = "avg_npc_2125_1#7$1",focus="r")]
[name="颉"]......如果真的想伤害我的话，也不会用这种手段了。
[name="颉"]所以我猜，这更多是一种警告吧。
[charslot(slot = "left", name = "avg_npc_2126_1#10$1",focus="l")]
[name="均"]......
[charslot(slot = "right", name = "avg_npc_2125_1#7$1",focus="r")]
[name="颉"]那位陛下是有为之君，他想要所有“人”对他俯首称臣。在他看来，我们一家的确是“非我族类”了。
[name="颉"]不过我倒是相信，以他的品格，应当不齿于用这柄书刀做些苟且之事。
[charslot(slot = "left", name = "avg_npc_2126_1#17$1",focus="l")]
[name="均"]可这对你未免过分了。你明明是最不该被猜忌的那一个。
[charslot(slot = "right", name = "avg_npc_2125_1#7$1",focus="r")]
[name="颉"]没有人会比二姐更清楚，“公正”二字，究竟有多么难写。就像大哥说过的......众口铄金，辩驳无用。
[charslot(slot = "left", name = "avg_npc_2126_1#1$1",focus="l")]
[name="均"]如果他此刻就在这里，不见得会善罢甘休。
[charslot(slot = "right", name = "avg_npc_2125_1#8$1",focus="r")]
[name="颉"]噗嗤......
[charslot(slot = "right", name = "avg_npc_2125_1#1$1",focus="r")]
[name="颉"]我可不想再见到大哥生气的样子，真是太可怕啦。
[charslot(slot = "left", name = "avg_npc_2126_1#8$1",focus="l")]
[name="均"]那你准备怎么办？这件事，你也不打算告诉望？
[name="均"]我倒是觉得，他的能耐这种时候反而能派上用场。
[charslot(slot = "right", name = "avg_npc_2125_1#4$1",focus="r")]
[name="颉"]......
[charslot(slot = "m", focus = "n")]
颉轻轻摇了摇头。
[charslot(slot = "right", name = "avg_npc_2125_1#10$1",focus="r")]
[name="颉"]我正要拜托二姐......这件事，务必要对二哥他保密。
[charslot(slot = "left", name = "avg_npc_2126_1#1$1",focus="l")]
[name="均"]......
[charslot(slot = "right", name = "avg_npc_2125_1#10$1",focus="r")]
[name="颉"]这么多年来，二哥始终因为各种原因被人所忌惮，新君临朝以来，他的处境更为微妙。这种时候，绝对不该再将他牵扯进来。
[name="颉"]更何况，要是让他知道了，我只怕按他的脾气，指不定会做出什么不理智的事呢。
[charslot(slot = "left", name = "avg_npc_2126_1#13$1",focus="l")]
[name="均"]好，姑且随你的意。
[name="均"]可是，颉，我也希望你能对我坦诚。
[charslot(slot = "left", name = "avg_npc_2126_1#19$1",focus="l")]
[name="均"]你究竟有没有与望一同筹谋什么？
[charslot(slot = "right", name = "avg_npc_2125_1#1$1",focus="r")]
[name="颉"]好姐姐，别审我啦。
[charslot(slot = "left", name = "avg_npc_2126_1#17$1",focus="l")]
[name="均"]......
[charslot(slot = "right", name = "avg_npc_2125_1#3$1",focus="r")]
[name="颉"]唉，在你面前果真没人能撒得了谎。
[charslot(slot = "left", name = "avg_npc_2126_1#19$1",focus="l")]
[name="均"]果然。
[charslot(slot = "left", name = "avg_npc_2126_1#17$1",focus="l")]
[name="均"]颉，你应当清楚，你在使用的这一份力量很危险。
[charslot(slot = "right", name = "avg_npc_2125_1#1$1",focus="r")]
[name="颉"]我当然知道这是一件有风险的事，可是这么多年来，承担着风险的也不止我一人。
[name="颉"]大哥二哥，还有大姐与你，都为我们这些弟弟妹妹做了许多事，我也不能无动于衷。
[name="颉"]再怎么说，我也不想让自己精心为大家取的这些名字......在历史上消弭无踪啊。
[Dialog]
[charslot(slot = "m", focus = "all")]
[playsound(key="$d_avg_clothmovement")]
[charslot(slot = "r",posfrom = "0,0", posto = "-20,0",duration = 0.5,block=true)]
[charslot(slot = "l",posfrom = "0,0", posto = "15,0",duration = 0.5,block=true)]
[delay(time=1)]
[charslot(slot = "m", focus = "n")]
见眼前的人依旧愁眉不展，颉轻轻牵起了均的手。这只常年操弄乐器的手掌心粗糙，握在手中的感觉却令人安心。
[charslot(slot = "right", name = "avg_npc_2125_1#1$1",focus="r")]
[name="颉"]你看，我这不还是好端端地待在这里？
[charslot(slot = "right", name = "avg_npc_2125_1#8$1",focus="r")]
[name="颉"]放心吧......
[Dialog]
[delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[name="颉"]其实，我最近做了一个梦，关于我们未来的梦。
[name="颉"]和黍描述的那一片雪白不同......我看到的是一个不一样的未来。
[name="颉"]我看到了你们每个人，每个人，都可以真正作为自己而活着。
[name="颉"]梦中的画面是那样真实，完全不像是一场梦。我甚至有一种预感......
[name="颉"]我不觉得，那只是一场梦......
[stopmusic(fadetime=2)]
[Dialog]
[charslot]
[delay(time=2)]
[Background(image="63_mini04_mountaintop",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[delay(time=1)]
[playMusic(key="$normal_loop", volume=0.6)]
[charslot(slot="m",name="avg_npc_1870_1#1$1",duration=1)]
[delay(time=2)]
[name="梁"]年姑娘，好久不见。
[Dialog]
[charslot]
[charslot(slot="m",name="avgnew_2014_nian_1#1$1",duration=0.5)]
[delay(time=1)]
[name="年"]哟，圆脑袋。怎么监工的是你呀？
[name="年"]你家包工头呢？又跑哪里去偷懒了？
[charslot(slot="m",name="avg_npc_1870_1#1$1")]
[name="梁"]年姑娘误会了，自从得知百灶要改成移动城市，先生便为了城市的设计操劳起来，最忙的时候，整整有一个月不曾合眼。
[charslot(slot="m",name="avgnew_2014_nian_1#1$1")]
[name="年"]嚯，那个慢性子还有这么上心的时候？
[charslot(slot="m",name="avg_npc_1870_1#1$1")]
[name="梁"]先生说，这是炎国的第一座移动城市，意义非凡。留在城市中的每一笔设计，都需要深思熟虑。
[name="梁"]因此，必须要赶在年姑娘对他的设计动手之前，抢先一步完成。
[charslot(slot="m",name="avgnew_2014_nian_1#5$1")]
[name="年"]唉我——！
[charslot(slot="m",name="avgnew_2014_nian_1#4$1")]
[name="年"]臭老八，亏我还总是惦记着和他分享点好东西，他在背后就这样说我坏话？！
[name="年"]那他现在人在哪？我倒要和他理论理论——
[charslot(slot="m",name="avg_npc_1870_1#1$1")]
[name="梁"]在补觉。
[name="梁"]先生已经睡了十天了，但是按着与工部的约定，今天是要给工部交付正门设计稿的日子。
[name="梁"]他交代过我，今天无论如何也要把工部的人拦在外面。
[charslot(slot="m",name="avgnew_2014_nian_1#1$1")]
[name="年"]哈哈哈......！我就知道，这才是我认识的那个易嘛。
[charslot(slot="m",name="avgnew_2014_nian_1#6$1")]
[name="年"]......
[charslot(slot="m",name="avg_npc_1870_1#1$1")]
[name="梁"]还有什么事吗？
[charslot(slot="m",name="avgnew_2014_nian_1#8$1")]
[name="年"]你是说，易这会还在睡大觉......
[charslot(slot="m",name="avgnew_2014_nian_1#7$1")]
[name="年"]我突然想起来，几十年前，易他好像捡了一块陨铁来着......应该还留在他的园子里吧，放在哪里了？
[charslot(slot="m",name="avg_npc_1870_1#1$1")]
[name="梁"]年姑娘......我有先生交代的任务在身。今天无论是工部的官员还是你，在下

... (全文17021字符)
```

### level_act49side_06_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[stopmusic]
[dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="70_g2_tjlibrary",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[animtext(id = "at1", name = "group_location_stamp", style="avg_only_medium", pos = "-400,-200", block = false)]<p=2>望日前两日 亥时</>
[delay(time=3)]
[animtextclean]
[delay(time=1)]
[playMusic(key="$saferoom_loop", volume=0.6)]
[PlaySound(key="$d_avg_bookshelf1", volume=0.5)]
[delay(time=1)]
男人走过一排排倾倒的书架，他努力地从遍地狼藉中拾起散落的书籍，努力将它们归置原位。
[dialog]
[PlaySound(key="$d_gen_walk_n", volume=1)]
[charslot(slot = "m", name = "avg_npc_295_1#7$1",duration=1.5, isblock=true)]
[name="梁洵"]“地泽万民，赐此奇石；天祐炎祚，得诛孽岁”......可这千年历史长河，到底是天地福泽的命定，还是巧合？  
[charslot(slot = "m", name = "avg_npc_295_1#7$1")]
[name="梁洵"]左公子，还有陈小姐......  
[charslot(slot = "m", name = "avg_npc_295_1#7$1")]
[name="梁洵"]今日携带那信物来到天镜阁的，偏偏是他们......  
[charslot(slot = "m", name = "avg_npc_295_1#2$1")]
[name="梁洵"]到底是巧合，还是......  
[charslot(slot = "m", focus="n")]
[name="？？？"]这一地狼藉......到底是怎么回事？  
[dialog]
[charslot]
[PlaySound(key="$d_avg_bookshelf1", volume=0.3)]
[delay(time=1)]
有人来到了他的身旁，脚步轻缓，俯身拾起了一本书。
[dialog]  
[charslot(slot = "r", name = "avg_npc_295_1#2$1",focus="l",isblock=false)]
[charslot(slot = "l", name = "avg_npc_298_1#10$1",focus="l",duration=1,isblock=true)]
[delay(time=1)]
[name="宁辞秋"]梁大人。 
[charslot(slot = "r", name = "avg_npc_295_1#4$1",focus="r")]
[name="梁洵"]宁小姐......怎么还在城中？  
[charslot(slot = "l", name = "avg_npc_298_1#10$1",focus="l")]
[name="宁辞秋"]梁大人难道忘了，我也是礼部官员。这种时候，在所有百姓全部撤离之前，我们都是不该离开的。  
[charslot(slot = "r", name = "avg_npc_295_1#5$1",focus="r")]
[name="梁洵"]当如是......  
[charslot(slot = "r", name = "avg_npc_295_1#1$1",focus="r")]
[name="梁洵"]如今百灶城中，百姓已经疏散完毕了？  
[charslot(slot = "l", name = "avg_npc_298_1#8$1",focus="l")]
[name="宁辞秋"]疏散工作基本已经结束了，百灶城很快就要开始拆分了吧。 
[charslot(slot = "l", name = "avg_npc_298_1#1$1",focus="l")] 
[name="宁辞秋"]还是令人不安......不是吗？ 
[charslot(slot = "r", name = "avg_npc_295_1#9$1",focus="r")]
[name="梁洵"]......  
[charslot(slot = "l", name = "avg_npc_298_1#9$1",focus="l")]
[name="宁辞秋"]也许梁大人还想问，你不曾告知于我自己遭贬谪的事，我又怎么知道你在这里？ 
[charslot(slot = "r", name = "avg_npc_295_1#7$1",focus="r")] 
[name="梁洵"]......  
[charslot(slot = "r", name = "avg_npc_295_1#5$1",focus="r")]
[name="梁洵"]......昨天一夜透雨，在下只是看到，宁小姐身上衣裳单薄......  
[charslot(slot = "l", name = "avg_npc_298_1#6$1",focus="l")]
[name="宁辞秋"]......  
[dialog]
[charslot]
[PlaySound(key="$d_avg_sweep", volume=1)]
[delay(time=1.8)]
[PlaySound(key="$d_avg_sit_tatami", volume=0.3)]
[delay(time=1)]
男子在一片混乱中清扫出了一小片空地，二人就这样席地坐下。  
[charslot(slot = "r", name = "avg_npc_295_1#5$1",focus="l",isblock=false)]
[charslot(slot = "l", name = "avg_npc_298_1#10$1",focus="l",isblock=true)]
[name="宁辞秋"]说来惭愧，这座天镜阁，倒的确是久违了。  
[charslot(slot = "r", name = "avg_npc_295_1#8$1",focus="r")]
[name="梁洵"]宁小姐当年......应该也是天镜阁的常客？  
[charslot(slot = "l", name = "avg_npc_298_1#10$1",focus="l")]
[name="宁辞秋"]在学宫求学的学生，谁不是呢？  
[charslot(slot = "l", name = "avg_npc_298_1#10$1",focus="l")]
[name="宁辞秋"]当年看着那一卷卷仿佛要堆上天的书，只觉得头疼得要命。  
[charslot(slot = "l", name = "avg_npc_298_1#2$1",focus="l")]
[name="宁辞秋"]但现在看来......这座天镜阁，或许还真是一个难得的，与世无争的好地方。  
[charslot(slot = "r", name = "avg_npc_295_1#5$1",focus="r")]
[name="梁洵"]宁小姐，我听闻了宁大人的事......  
[charslot(slot = "r", name = "avg_npc_295_1#5$1",focus="r")]
[name="梁洵"]在下，深表遗憾......  
[charslot(slot = "l", name = "avg_npc_298_1#6$1",focus="l")]
[name="宁辞秋"]......  
[charslot(slot = "l", name = "avg_npc_298_1#6$1",focus="l")]
[name="宁辞秋"]祖父为了他相信的道义，做了他认为正确的事。  
[charslot(slot = "l", name = "avg_npc_298_1#6$1",focus="l")]
[name="宁辞秋"]他将这个秘密保守了这么多年，不会只是出于私心，同样也是为了保护家中后辈。  
[charslot(slot = "l", name = "avg_npc_298_1#1$1",focus="l")]
[name="宁辞秋"]于情于理，我都没有办法去指责他。 
[charslot(slot = "l", name = "avg_npc_298_1#1$1",focus="l")] 
[name="宁辞秋"]当然，这些都不能改变他要为自己的作为付出代价就是。  
[charslot(slot = "r", name = "avg_npc_295_1#8$1",focus="r")]
[name="梁洵"]宁小姐能将这些事放下......那很好。  
[charslot(slot = "l", name = "avg_npc_298_1#1$1",focus="l")]
[name="宁辞秋"]梁大人应该是误会了，我并不是在说自己可以将这一切轻易放下。  
[charslot(slot = "l", name = "avg_npc_298_1#1$1",focus="l")]
[name="宁辞秋"]我从不否认自己的仕途受到了祖父荫庇......在旁人看来，宁家现在的处境不知该有多么狼狈......  
[charslot(slot = "l", name = "avg_npc_298_1#1$1",focus="l")]
[name="宁辞秋"]......这话，我只对梁大人讲。  
[charslot(slot = "r", name = "avg_npc_295_1#8$1",focus="r")]
[name="梁洵"]这话怎能这么讲？梁某倒觉得，这些年来，宁小姐的每一份功绩都做不得假。  
[charslot(slot = "r", name = "avg_npc_295_1#8$1",focus="r")]
[name="梁洵"]我相信宁小姐——  
[charslot(slot = "l", name = "avg_npc_298_1#1$1",focus="l")]
[name="宁辞秋"]也许，只有你相信呢？  
[charslot(slot = "r", name = "avg_npc_295_1#5$1",focus="r")]
[name="梁洵"]......  
[charslot(slot = "l", name = "avg_npc_298_1#1$1",focus="l")]
[name="宁辞秋"]爷爷曾经说过，入了这道宫墙，便不能轻信于人，更不能以为自己可以轻易取信于人。  
[charslot(slot = "l", name = "avg_npc_298_1#10$1",focus="l")]
[name="宁辞秋"]我的确是听进去了......可是在尚蜀初识你的时候，不知为何就忘了这句话。  
[charslot(slot = "l", name = "avg_npc_298_1#9$1",focus="l")]
[name="宁辞秋"]我只是相信，自己终于遇见了一位同道中人。  
[charslot(slot = "r", name = "avg_npc_295_1#5$1",focus="r")]
[name="梁洵"]梁某......不胜惶恐。  
[charslot(slot = "l", name = "avg_npc_298_1#7$1",focus="l")]
[name="宁辞秋"]看吧......你永远都是这样。  
[charslot(slot = "l", name = "avg_npc_298_1#7$1",focus="l")]
[name="宁辞秋"]我最欣赏你的正直担当，却又讨厌你事事独断，将所有人拒于千里之外。  
[charslot(slot = "l", name = "avg_npc_298_1#10$1",focus="l")]
[name="宁辞秋"]不过后来我也想通了。倘若你事事都要我看得过眼，那你也不是“梁洵”了。  
[charslot(slot = "l", name = "avg_npc_298_1#10$1",focus="l")]
[name="宁辞秋"]就像我没有办法指责爷爷一样，我又如何能怪罪于你呢？  
[charslot(slot = "r", name = "avg_npc_295_1#10$1",focus="r")]
[name="梁洵"]......  
[charslot(slot = "r", name = "avg_npc_295_1#10$1",focus="r")]
[name="梁洵"]我曾以为，只要做到勤勉中正，持之以恒，总能做出一番成就。  
[charslot(slot = "r", name = "avg_npc_295_1#5$1",focus="r")]
[name="梁洵"]......可是经年累月，我只是认清了自己无能为力。  
[charslot(slot = "r", name = "avg_npc_295_1#5$1",focus="r")]
[name="梁洵"]令祖父说的话自然是极对的，但最可畏的是，初心理想，连自己都不敢相信。  
[charslot(slot = "r", name = "avg_npc_295_1

... (全文22145字符)
```

### level_act49side_06_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[stopmusic]
[dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="35_g7_zuosroom",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[animtext(id = "at1", name = "group_location_stamp", style="avg_only_medium", pos = "-400,-200", block = false)]<p=2>望日前一日 巳时</>
[delay(time=3)]
[animtextclean]
[delay(time=1)]
[playMusic(key="$m_sys_bitw_loop", volume=0.6)]
[charslot(slot = "m", name = "avg_npc_788_1#1$1",focus="m",isblock=true)]
[name="左宣辽"]......
[dialog]
[charslot]
有些苍老的将军在军帐中长久地沉默伫立着，仿佛古老城墙上的砖石。
身后是在心中已经描摹过上万遍的行军图，眼前是隐约可见轮廓的百灶城。
见惯了西北的黄沙，中原的雨天反倒令人难以适应。阴云低垂，叫人透不过气。
将军的思绪飘出去很远。
[dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[background]
[charslot]
[Background(image="35_g3_yumenobservationtower_d",screenadapt="coverall")]
[CameraEffect(effect="Grayscale", fadetime=0, keep=true, initamount=0, amount=1, block=true)]
[musicvolume(volume=0.6, fadetime=2)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[CameraEffect(effect="Grayscale", fadetime=4, keep=true, initamount=1, amount=0, block=false)]
[charslot(slot = "m", name = "avg_2024_chyue_1#1$1",focus="m",duration=1,isblock=true)]
[name="朔"]足下就是新任玉门守将吧。  
[charslot(slot = "m", name = "avg_2024_chyue_1#10$1")]
[name="朔"]称呼我为朔便好，在下的职责是在军中一应事务上协助将军，另外身兼这里的武学教习。  
[charslot(slot = "m", name = "avg_2024_chyue_1#10$1")]
[name="朔"]需要的话，在下可以先带将军熟悉一下军中环境。  
[charslot(slot = "m", name = "avg_npc_788_1#5$1",focus="m",isblock=true)]
[name="左宣辽"]......你不认得我？  
[charslot(slot = "m", name = "avg_2024_chyue_1#6$1")]
[name="朔"]在下在朝廷下发的通告中见过左宣辽将军的名字......你说的“认得”指的是？  
[charslot(slot = "m", name = "avg_npc_788_1#7$1",focus="m",isblock=true)]
[name="左宣辽"]......  
[charslot(slot = "m", name = "avg_npc_788_1#1$1",focus="m",isblock=true)]
[name="左宣辽"]不必了。  
[charslot(slot = "m", name = "avg_npc_788_1#1$1",focus="m",isblock=true)]
[name="左宣辽"]用不着你带路，我是调迁回到玉门，早些年也是在玉门扛过刀的。  
[charslot(slot = "m", name = "avg_2024_chyue_1#10$1")]
[name="朔"]原来如此，反倒是在下自作主张了。  
[name="朔"]看来早在那个时候，你我就已经是同袍了。  
[name="朔"]在这里戍边太久，有不少事情记不清了，如有冒犯，还请将军包涵。
[charslot(slot = "m", name = "avg_npc_788_1#1$1",focus="m",isblock=true)]
[name="左宣辽"]记不清了......哼，有意思。
[charslot(slot = "m", name = "avg_npc_788_1#1$1",focus="m",isblock=true)]
[name="左宣辽"]准备一下，我们校场练练。 
[charslot(slot = "m", name = "avg_2024_chyue_1#10$1")] 
[name="朔"]将军一路舟车劳顿，还是先好好休息。如果将军往后还有兴致，在下乐意奉陪。  
[charslot(slot = "m", name = "avg_npc_788_1#7$1",focus="m",isblock=true)]
[name="左宣辽"]少废话，有什么好休息的。  
[charslot(slot = "m", name = "avg_npc_788_1#1$1",focus="m",isblock=true)]
[name="左宣辽"]先活动一下拳脚，才吃得下饭。
[dialog]
[PlaySound(key="$flashback", volume=0.8)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0, block=true)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.5, block=true)]
[charslot]
[bgeffect(name="$eb_blizzard",layer=1)] 
[PlaySound(key="$d_avg_snowstormflp", volume=1, loop=true, channel="a")]
[PlaySound(key="$d_avg_wind", volume=1)]
[SoundVolume(volume=1, channel="a",fadetime=2)]
[Background(image="40_g2_glacier",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.5, block=true)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0, block=true)]
[Blocker(a=0.7, r=255, g=255, b=255, fadetime=1, block=true)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=3, block=true)]
[charslot(slot = "m", name = "avg_2024_chyue_1#8$1",focus="m",duration=1,isblock=true)]
[name="朔"]左将军，到此为止吧。  
[charslot(slot = "m", name = "avg_2024_chyue_1#8$1")] 
[name="朔"]军队跋涉作战，军需，士气，都已经到极限了。  
[charslot(slot = "m", name = "avg_2024_chyue_1#3$1")] 
[name="朔"]与邪魔作战不得用强，再孤军深入恐怕有变。  
[charslot(slot = "m", name = "avg_npc_788_1#4$1",focus="m",isblock=true)]
[name="左宣辽"]功亏一篑......！  
[charslot(slot = "m", name = "avg_2024_chyue_1#8$1")] 
[name="朔"]将军，这一战成果已然可观。
[charslot(slot = "m", name = "avg_2024_chyue_1#1$1")] 
[name="朔"]这北祟邪魔以人心中畏惧为食......如左将军这样，第一次将整支军队的安危扛在肩上，却没有丝毫怯意的将领，在下也是平生仅见。  
[charslot(slot = "m", name = "avg_npc_788_1#4$1",focus="m",isblock=true)]
[name="左宣辽"]有何可怕！  
[charslot(slot = "m", name = "avg_npc_788_1#4$1",focus="m",isblock=true)]
[name="左宣辽"]伤我将士百姓，毁我城市良田......我只恨这一战不能把这些东西赶尽杀绝！  
[dialog]
[charslot]
[PlaySound(key="$d_avg_drawswordlong", volume=1)]
[delay(time=1.2)]
[Blocker(a=0.8, r=1, g=1, b=1, fadetime=0.3, block=true)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.1, block=true)]
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[PlaySound(key="$d_avg_swrdstckgrnd", volume=1)]
[delay(time=0.2)]
[PlaySound(key="$d_avg_icebrk", volume=0.5)]
[charslot(slot = "m", name = "avg_npc_788_1#4$1",focus="m",isblock=true)]
[name="左宣辽"]假我二十年，以此剑为界，我必然平定所有作乱祟物！  
[charslot(slot = "m", name = "avg_2024_chyue_1#10$1")] 
[name="朔"]在下当然相信将军。  
[charslot(slot = "m", name = "avg_2024_chyue_1#10$1")] 
[name="朔"]以左将军的胆魄，这世上怕是没有什么能让你畏退之敌了。  
[charslot(slot = "m", name = "avg_npc_788_1#5$1",focus="m",isblock=true)]
[name="左宣辽"]......那你呢？  
[charslot(slot = "m", name = "avg_npc_788_1#10$1",focus="m",isblock=true)]
[name="左宣辽"]你看上去刀枪不入，战无不胜......  
[charslot(slot = "m", name = "avg_npc_788_1#10$1",focus="m",isblock=true)]
[name="左宣辽"]你怕过吗？
[dialog]
[PlaySound(key="$flashback", volume=0.8)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0, block=true)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.5, block=true)]
[charslot]
[stopSound(channel="a")]
[bgeffect]
[charslot(slot = "r", name = "avg_npc_788_1#1$1")]
[charslot(slot = "l", name = "avg_2024_chyue_1#1$1")]
[Background(image="35_g3_yumenobservationtower_n",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.5, block=true)]
[delay(time=1)]
[charslot(slot = "r", name = "avg_npc_788_1#5$1",focus="r")]
[name="左宣辽"]调任？  
[charslot(slot = "l", name = "avg_2024_chyue_1#9$1",focus="l")]
[name="重岳"]我在玉门的任期以百年为限，如今也该做好离任的准备了。  
[charslot(slot = "r", name = "avg_npc_788_1#4$1",focus="r")]
[name="左宣辽"]

... (全文23746字符)
```

### level_act49side_07_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Delay(time=1)]
[Background(image="70_g2_tjlibrary",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=2)]
[animtext(id = "at1", name = "group_location_stamp", style="avg_only_heavy", pos = "-400,-200", block = false)]<p=1>982年</>
[delay(time=3)]
[animtextclean]
[delay(time=1)]
[Blocker(a=0.6, r=0, g=0, b=0, fadetime=1, block=true)]
[playMusic(key="$saferoom_loop", volume=0.6)]
[Subtitle(text="二十年的时间，的确漫长。", x=300, y=320, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="大炎将一整座城市搬上了移动平台，在许多遥远的地方，还有无数座这样的移动城市拔地而起。", x=300, y=320, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="从各地收录的书卷很多，天镜阁在二十年中扩建了几番，已经是我完全认不出原貌的宏伟建筑。", x=300, y=320, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="二十年的时间，也的确短暂。", x=300, y=320, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="我们一家人聚少离多。", x=300, y=320, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="大哥大姐依旧在戍边，二姐协助修订了《炎律》后正打算移住丹燕，黍长居大荒，绩游历四海，易遍访山川，年还是那样到处游戏。", x=300, y=320, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="方弟据说已经出了大炎地界，小夕还是不肯从自己的画卷里出来，幺弟的饭店倒是红红火火，几十年如一日。", x=300, y=320, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="至于二哥......", x=300, y=320, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="他将自己锁在一间古寺里，为了精进“棋艺”，就这样枯坐了二十年......", x=300, y=320, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="......他到底什么时候，才愿意与我再见一面呢？", x=300, y=320, alignment="center", size=24, delay=0.04, width=700)]
[subtitle]
[dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[dialog]
[charslot(slot="m",name="avg_npc_2125_1#9$1",duration=1)]
[delay(time=2)]
[name="颉"]......
[dialog]
[charslot]m
[charslot(slot="m",name="avg_npc_2127_1#1$2",duration=0.5)]
[delay(time=1)]
[name="椿"]颉，太史阁那边在催姜齐地方志的审校，不过——
[charslot(slot="m",name="avg_npc_2125_1#1$1")]
[name="颉"]偷闲被你捉住了。
[charslot(slot="m",name="avg_npc_2127_1#3$2")]
[name="椿"]......你偷闲也没问题的。那本地方志我校过一遍，有问题的地方都圈出来了。你还要再看一下吗？
[dialog]
[playsound(key="$book_close")]
[charslot(slot="m",name="avg_npc_2125_1#3$1")]
[delay(time=1)]
[name="颉"]咦？真奇怪，这本书是什么时候......
[charslot(slot="m",name="avg_npc_2127_1#13$2")]
[name="椿"]唉......你得空还是多歇歇吧，人都要糊涂了。这些年，我几乎是看着你工作的时间一点一点增多，睡觉的时间一点一点变少......
[name="椿"]各移动城市的地方志、建城史，上代真龙的实录，学宫古代史部分的教材......这么多书，我只是帮你整理，有时候都觉得累得慌。
[name="椿"]真奇怪，我听说工部给年的委托越来越少，黍在大荒城的任务也没那么繁重了。
[name="椿"]但好像唯独是你，身上的担子始终卸不下......
[charslot(slot="m",name="avg_npc_2125_1#4$1")]
[name="颉"]......
[charslot(slot="m",name="avg_npc_2127_1#5$2")]
[name="椿"]颉？
[charslot(slot="m",name="avg_npc_2125_1#5$1")]
[name="颉"]嗯......？
[charslot(slot="m",name="avg_npc_2125_1#1$1")]
[name="颉"]抱歉，刚刚有点走神了。
[name="颉"]椿，今天的确是有点累了，我想先把这些工作放一放......
[charslot(slot="m",name="avg_npc_2127_1#3$2")]
[name="椿"]好呀。要不，我们去街上转转？
[charslot(slot="m",name="avg_npc_2125_1#4$1")]
[name="颉"]......不了。今天不知为何，有点心神不宁。你先去吧。
[charslot(slot="m",name="avg_npc_2125_1#1$1")]
[name="颉"]若是有什么有意思的东西，别忘了帮我也带一点。
[stopmusic(fadetime=2)]
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[delay(time=1)]
[Background(image="70_g1_tjoutside",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[delay(time=1)]
[playMusic(intro="$suspenseful_intro",key="$suspenseful_loop", volume=0.6)]
[charslot(slot="m",name="avg_npc_1632_1#1$1",duration=0.5)]
[delay(time=1)]
[name="严肃的炎国官员"]椿秉烛。
[charslot(slot="m",name="avg_npc_2127_1#1$2")]
[name="椿"]是我。您找我是......
[charslot(slot="m",name="avg_npc_1632_1#1$1")]
[name="严肃的炎国官员"]有封要紧的信带给您。
[charslot(slot="m",name="avg_npc_2127_1#1$2")]
[name="椿"]您......给我带信？谁寄来的？
[charslot(slot="m",name="avg_npc_1632_1#1$1")]
[name="严肃的炎国官员"]不知是谁给司岁台寄了封信，监正阅后大惊失色，将这封信转呈陛下，同时也抄送给各位直接接触代理人的秉烛人。
[charslot(slot="m",name="avg_npc_2127_1#5$2")]
[name="椿"]这里面是......？
[charslot(slot="m",name="avg_npc_1632_1#1$1")]
[name="严肃的炎国官员"]我也不知。监正只说让各位先做好准备，不要轻举妄动。
[dialog]
[charslot(slot = "m",posfrom = "0,0", posto = "200,0",duration = 1,afrom = 1, ato = 0)]
[delay(time=2.5)]
[charslot]
[charslot(slot="m",name="avg_npc_2127_1#11$2")]
[name="椿"]这里面说的是......
[dialog]
[PlaySound(key="$d_avg_paper1")]
[Blocker(a=0.6, r=0, g=0, b=0, fadetime=1.5, block=true)]
[Sticker(id="st1", multi = true, text="■■年，出世。", x=300,y=220, alignment="left", size=24, delay=0.04, width=700,block = true)]
[Sticker(id="st1", multi = true, text="\n\n■■年，与朔相搏，毁坏黎民生计无算。", x=300,y=270, alignment="left", size=24, delay=0.04, width=700,block = true)]
[Sticker(id="st1", multi = true, text="\n\n......", x=300,y=330, alignment="center", size=24, delay=0.04, width=700,block = true)]
[Sticker(id="st1",duration=0.5)]
[delay(time=1)]
[Sticker(id="st1", multi = true, text="■■年，包庇同族，构陷官吏，使人蒙不白之冤。", x=300,y=220, alignment="left", size=24, delay=0.04, width=700,block = true)]
[Sticker(id="st1", multi = true, text="\n\n■■年，躲避司岁台监视，与其余代理人私会。数月之后，司岁台失火，主犯成谜。", x=300,y=270, alignment="left", size=24, delay=0.04, width=700,block = true)]
[Sticker(id="st1", multi = true, text="\n\n■■年，谎称诛杀矩兽，实则包庇，坐视其离开大炎。", x=300,y=270, alignment="left", size=24, delay=0.04, width=700,block = true)]
[Sticker(id="st1", multi = true, text="\n\n......", x=300,y=330, alignment="center", size=24, delay=0.04, width=700,block = true)]
[Sticker(id="st1",duration=0.5)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1.5, block=true)]
[charslot(slot="m",name="avg_npc_2127_1#10$2")]
[name="椿"]陷害官吏、私会、失火、包庇巨兽......
[name="椿"]这说的是......
[charslot(slot="m",name="avg_npc_2127_1#11$2")]
[name="椿"]......望？
[name="椿"]这真的是望做过的事？可为什么司岁台的记录没有这些？！
[dialog]
[charslot]
[charslot(slot="m",name="avg_npc_1632_1#1$1",duration=0.5,bstart=0.2,bend=0.6)]
[delay(time=1.5)]
[charslot(slot="m",name="avg_npc_2127_1#5$2")]
[name="椿"]你——你没走？！
[charslot(slot="m",name="avg_npc_1632_1#1$1",bstart=0.2,bend=0.6)]
[name="严肃的炎国官员？"]另有一句话带给椿秉烛。
[name="严肃的炎国官员？"]先诛大恶，再除元凶。
[dialog]
[charslot(sl

... (全文15406字符)
```

### level_act49side_07_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Delay(time=1)]
[Background(image="25_g11_yanroom",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=2)]
[animtext(id = "at1", name = "group_location_stamp", style="avg_only_heavy", pos = "-400,-200", block = false)]<p=1>982年</>
[delay(time=3)]
[animtextclean]
[delay(time=1)]
[playMusic(intro="$drift_intro",key="$drift_loop", volume=0.6)]
[CameraShake(duration=0.3, xstrength=2, ystrength=5, vibrato=10, randomness=90, fadeout=true, block=false)]
[playsound(key="$d_avg_swordcrack")]
[Delay(time=1)]
[charslot(slot="m",name="avgnew_2014_nian_1#8$1",duration=1)]
[Delay(time=2)]
[name="年"]咋子回事，锻把剑都能失误？手生了？
[charslot(slot = "m", focus = "n")]
工匠困惑地挠了挠头，转身又从仓库中拿出一块钢坯。
[charslot(slot="m",name="avgnew_2014_nian_1#2$1")]
[name="年"]......今年秋天也太潮湿了点，总觉得胸闷气短。
[charslot(slot="m",name="avgnew_2014_nian_1#6$1")]
[name="年"]这感觉，不对劲哦......
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[delay(time=1)]
[Background(image="bg_cottage",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[delay(time=1)]
[CameraShake(duration=0.5, xstrength=15, ystrength=15, vibrato=30, randomness=90, fadeout=true, block=false)]
[PlaySound(key="$d_gen_thunders_amb", volume=1)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0, block=true)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.03, block=true)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0.5, block=true)]
[Blocker(a=1, r=1, g=1, b=1, fadetime=0.03, block=true)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.5, block=false)]
[delay(time=1)]
[charslot(slot="m",name="avgnew_2015_dusk_1#6$1",duration=0.5)]
[delay(time=1)]
[name="夕"]——！
[name="夕"]怎么回事......怎么可能？！
[charslot(slot="m",name="avgnew_2015_dusk_1#5$1")]
[name="夕"]是祂......要醒来了吗？
[dialog]
[charslot(slot="m",name="avg_npc_143#1")]
[delay(time=0.3)]
[charslot(slot = "m", action="jump",posfrom="0,0",posto="0,0",power=15, times=1,duration=0.3)]
[name="墨魉"]（担忧地）嘎——？
[charslot]
原本平静的画卷，不知被谁无端添上了一笔怒云。
[dialog]
[Effect(name="$e_vanish",layer = 1,x=-550,y=600)]
[Effect(name="$e_vanish",layer = 1,x=550,y=-300)]
[delay(time=0.3)]
[CameraShake(duration=0.3, xstrength=15, ystrength=15, vibrato=30, randomness=90, fadeout=true, block=false)]
[PlaySound(key="$d_gen_thunders_amb", volume=1)]
[Blocker(a=1, r=1, g=1, b=1, fadetime=0.03, block=true)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=false)]
惊雷炸响，在白卷上留下一道极为突兀的墨痕。
只一瞬间，画卷中凭空生出无数奇诡可怖，面目狰狞的墨魉。它们向四处奔散，将画卷中的一切风光均覆盖成漆黑的墨色。
[charslot(slot="m",name="avgnew_2015_dusk_1#3$1")]
[name="夕"]这些......根本不是我的画......
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[charslot(slot="m",name="avgnew_2015_dusk_1#5$1")]
[name="夕"]给我......退开！
[dialog]
[charslot]
[CameraShake(duration=1.5, xstrength=20, ystrength=20, vibrato=30, randomness=90, fadeout=true, block=false)]
[PlaySound(key="$p_imp_ancientsword_s", volume=0.6)]
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[delay(time=1)]
[playsound(key="$d_avg_rainlight_loop", loop=true, channel="r",volume=0)]
[SoundVolume(volume=1, channel="r",fadetime=2)]
[bgeffect(name="$eb_rain",layer=1)]
[Background(image="35_g11_yumendesert",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[delay(time=1)]
[PlaySound(key="$d_avg_sandftsingle", volume=0.7)]
[charslot(slot="m",name="avg_2024_chyue_1#1$1",duration=0.5)]
[delay(time=1.5)]
[charslot(slot="m",name="avg_npc_1637_1#1$1")]
[name="百灶守军"]朔先生，一路辛苦了。
[name="百灶守军"]请留步，随我等到偏处暂歇。
[charslot(slot="m",name="avg_2024_chyue_1#1$1")]
[name="朔"]再消磨时间，怕是要耽误了向兵部述职的时间。
[charslot(slot="m",name="avg_npc_1637_1#1$1")]
[name="百灶守军"]陛下有令，百灶城中有事，先生暂时不可进城。
[charslot(slot="m",name="avg_2024_chyue_1#6$1")]
[name="朔"]......为何？
[dialog]
[charslot]
[CameraShake(duration=1, xstrength=15, ystrength=15, vibrato=30, randomness=90, fadeout=true, block=false)]
[PlaySound(key="$d_gen_thunders_amb", volume=1)]
[Blocker(a=1, r=1, g=1, b=1, fadetime=0.03, block=true)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1.5, block=true)]
[charslot(slot="m",name="avg_2024_chyue_1#8$1")]
[name="朔"]那是......岁陵？
[name="朔"]望......你究竟做了什么......
[Dialog]
[StopSound(channel="r", fadetime=2)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[bgeffect]
[delay(time=1)]
[Background(image="70_g5_tjtopfloor",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[delay(time=1)]
[backgroundTween(xScaleTo=1.05, yScaleTo=1.05, duration=1, block=false)]
[Background(image="70_g5_tjtopfloor",screenadapt="coverall",fadetime=1)]
[PlaySound(key="$d_gen_heartbeat",volume=1, channel="HB", loop=true)]
[stopsound(channel="HB", fadetime=1)]
[delay(time=1.5)]
心脏漏跳了一拍，又或者，在一个瞬间跳动了两次？
[Dialog]
[backgroundTween(xScaleTo=1.05, yScaleTo=1.05, duration=1, block=false)]
[Background(image="70_g5_tjtopfloor",screenadapt="coverall",fadetime=1)]
[PlaySound(key="$d_gen_heartbeat",volume=1, channel="HB", loop=true)]
[stopsound(channel="HB", fadetime=1)]
[Dialog]
[delay(time=1.5)]
又或者，那是移动城市因为某种缘故突然开拔的震动？
[Dialog]
[backgroundTween(xScaleTo=1.05, yScaleTo=1.05, duration=1, block=false)]
[Background(image="70_g5_tjtopfloor",screenadapt="coverall",fadetime=1)]
[PlaySound(key="$d_gen_heartbeat",volume=1, channel="HB", loop=true)]
[stopsound(channel="HB", fadetime=1)]
[Dialog]
[delay(time=1.5)]
还是说......
[CameraShake(duration=0.3, xstrength=5, ystrength=10, vibrato=10, randomness=90, fadeout=true, block=false)]
[PlaySound(key="$d_avg_bookdrop", volume=1)]
啪嗒。
代理人手中的书卷在不觉中落到地上。
[Dialog]
[charslot(slot="m",name="avg_npc_2125_1#10$1",duration=0.5)]
[delay(time=1)]
[name="颉"]二哥？！
[dialog]
[charslot]
[playsound(key="$rungeneral", loop=true, channel="bgs")]
[StopSound(channel="bgs", fadetime=2)]
[delay(time=1.5)]
[PlaySound(key="$dooropenquite", volume=1)]
[charslot(slot="m",name="avg_npc_2127_1#5$2",duration=0.5)]
[delay(time=0.5)]
[nam

... (全文28982字符)
```

### level_act49side_08_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[stopmusic]
[dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="70_g9_oldbattlefield",screenadapt="coverall")]
[BackgroundTween(image="70_g9_oldbattlefield", duration=7, xScaleFrom=1.2, yScaleFrom=1.2, xScaleTo=1.2, yScaleTo=1.2, xFrom=80, xTo=-80)]
[CameraEffect(effect="Grayscale", fadetime=0, keep=true, initamount=0, amount=1, block=true)]
[playMusic(key="$wasteland_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=3, block=true)]
[CameraEffect(effect="Grayscale", fadetime=4, keep=true, initamount=1, amount=0, block=false)]
[Delay(time=3)]
[Background(image="70_g9_oldbattlefield",screenadapt="coverall",fadetime=2,isblock=true)]
[delay(time=2.5)]
[PlaySound(key="$d_avg_sandftsingle",volume=0.6,block=false)]
[charslot(slot = "m", name = "avg_4121_zuole_1#1$1",posfrom="50,0",posto="0,0",duration=1.5,isblock=true)]  
[delay(time=1)]
[charslot(slot = "m", focus="n")]
[name="司岁台监正"]这身衣服很适合你。  
[charslot(slot = "m", name = "avg_4121_zuole_1#4$1",focus="m")]
[name="左乐"]左、左乐见过监正大人！  
[charslot(slot = "m", focus="n")]
[name="司岁台监正"]新人首日报道，倒也不必这么严肃拘谨。未免折了身上的少年气。放轻松些。  
[charslot(slot = "m", name = "avg_4121_zuole_1#1$1",focus="m")]
[name="左乐"]是！左乐谨记！  
[charslot(slot = "m", focus="n")]
[name="司岁台监正"]......
[charslot(slot = "m", focus="n")]
[name="司岁台监正"]左乐，你可知这里是什么地方？  
[charslot(slot = "m", name = "avg_4121_zuole_1#3$1",focus="m")]
[name="左乐"]“有兽死绥，路绝山隈。”此处乃大狩猎时，我们围杀一头巨兽的战场。
[charslot(slot = "m", name = "avg_4121_zuole_1#1$1",focus="m")]  
[name="左乐"]但......
[charslot(slot = "m", focus="n")]
左乐顿住话头，不知道自己还能不能接着这个“但”字讲下去，看到眼前人耐心的目光，才继续往下说。  
[charslot(slot = "m", name = "avg_4121_zuole_1#1$1",focus="m")]
[name="左乐"]这里同样也是，无数将士、百姓......那些活生生的人，化作书页之间，一行行冰冷数字的坟场。  
[charslot(slot = "m", focus="n")]
[name="司岁台监正"]许多比你更年长的秉烛人，也没能看到这一层。  
[charslot(slot = "m", focus="n")]
[name="司岁台监正"]“明烛以驱巨兽之影，巡游以察社稷之患。”
[charslot(slot = "m", focus="n")]
[name="司岁台监正"]最早的秉烛人，手持炬火查明了巨兽的存在，才有后来炎国从神明手中夺来生机的那场战争。  
[charslot(slot = "m", focus="n")]
[name="司岁台监正"]时至今日，依然只有极少数人才知晓巨兽的存在，寻常百姓更是无从得知。  
[charslot(slot = "m", focus="n")]
[name="司岁台监正"]正因如此，秉烛人手中的烛火才更应于阴影遮蔽处，长明不灭。  
[charslot(slot = "m", name = "avg_4121_zuole_1#1$1",focus="m")]
[name="左乐"]左乐定当竭尽全力，护万民安生。  
[charslot(slot = "m", focus="n")]
[name="司岁台监正"]你能有这份决心，很好。不过，我仍需再问问你——在你看来，巨兽，究竟是什么？  
[charslot(slot = "m", focus="n")]
[name="司岁台监正"]那些行走于山川四时之间，被我们密切注视着的代理人，祂们......又是什么？  
[charslot(slot = "m", name = "avg_4121_zuole_1#1$1",focus="m")]
[name="左乐"]人心尚不可测，况夫兽心。祂们之中，固然有因一时兴起或片刻真心，曾予大炎以助力之辈。  
[charslot(slot = "m", name = "avg_4121_zuole_1#1$1",focus="m")]
[name="左乐"]但权衡利弊，归根结底，祂们......终究是与我们不同的人......敌人。  
[charslot(slot = "m", focus="n")]
[name="司岁台监正"]敌人吗......  
[charslot(slot = "m", focus="n")]
[name="司岁台监正"]......敌人。
[dialog]
[charslot]
[stopmusic(fadetime=2)]
[CameraEffect(effect="Grayscale", fadetime=2, keep=true, initamount=0, amount=1, block=true)]
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[CameraEffect(effect="Grayscale", fadetime=0.1, keep=true, initamount=1, amount=0, block=true)]
[Background(image="70_g4_tjdiscussionroom",xScale=1.2, yScale=1.2,screenadapt="coverall")]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[animtext(id = "at1", name = "group_location_stamp", style="avg_only_medium", pos = "-400,-200", block = false)]<p=2>望日前一日 酉时</>
[delay(time=3)]
[animtextclean]
[delay(time=1)]
[playMusic(key="$m_sys_act23side_loop", volume=0.6)]
[charslot(slot = "m", name = "avg_4121_zuole_1#6$1")]  
[name="左乐"]监正大人......  
[charslot(slot = "m", name = "avg_4121_zuole_1#1$1")]  
[name="左乐"]您......怎么在这儿？
[dialog]
[charslot]
[charslot(slot = "m", name = "avg_npc_2127_1#1$1",duration=1.5, isblock=true)]  
[name="椿"]这句话难道不是应该我来问你？  
[charslot(slot = "m", name = "avg_npc_2127_1#1$1")]
[name="椿"]界园镇抚过后，界园里的信物，你送到了哪里？  
[charslot(slot = "m", name = "avg_4121_zuole_1#1$1")]  
[name="左乐"]司岁台情况有异，再加上天镜阁字伥横行，我本想等情况明朗，再请您当面定夺......
[charslot(slot = "m", name = "avg_npc_2127_1#10$1")]
[name="椿"]那便在此交接吧。  
[charslot(slot = "m", name = "avg_npc_2127_1#10$1")]
[name="椿"]我听说今年从界园中带出来的并非每年恒例的玉尺，具体究竟是何物，待我回司岁台详细查看。  
[charslot(slot = "m", name = "avg_4121_zuole_1#3$1")]  
[name="左乐"]这......
[dialog]
[charslot(slot = "m",afrom=1,ato=1, name = "avg_4121_zuole_1#1$1",posfrom="0,0",posto="-30,0",duration=0.8,block=true)]  
[delay(time=1.5)]
[charslot(slot = "m",focus="n")]
只是出于潜意识中的判断，面对熟悉的顶头上司，左乐向后退了一步。  
[dialog]
[charslot]
[charslot(slot = "m", name = "avg_npc_2127_1#11$1")]
[name="椿"]......真稀奇，左秉烛竟也会有抗命不遵的一天。  
[dialog]
[charslot]
[PlaySound(key="$d_gen_walk_n", volume=1)]
[charslot(slot = "m", name = "avg_npc_1871_1#1$1",posfrom="150,0",posto="0,0",duration=1, isblock=true)]
[name="莫佚"]别来这一套——你就是椿，司岁台的头儿？  
[charslot(slot = "m", name = "avg_npc_2127_1#10$1")]
[name="椿"]竟然能在天镜阁中见到山海众，如不是这特殊时期，巡防营上下都该重罚——而且看你的服装，似乎是等级不低。  
[charslot(slot = "m", name = "avg_npc_2127_1#4$1")]
[name="椿"]这位又是......陈家小姐？  
[charslot(slot = "m", name = "avg_1050_chen3_1#1$2")]
[name="陈"]......你是左乐的上司？  
[charslot(slot = "m", name = "avg_npc_2127_1#1$1")]
[name="椿"]忝居其位，但也责无旁贷。  
[charslot(slot = "m", name = "avg_npc_1871_1#2$1")]
[name="莫佚"]你在这儿干什么？就等着我们来自投罗网？
[charslot(slot = "m", name = "avg_npc_2127_1#7$1")]  
[name="椿"]很遗憾，我要等的并不是你们。  
[charslot(slot = "m", name = "avg_npc_2127_1#1$1")]
[name="椿"]左乐，把信物交上来，然后你就可以和朋友们走了。你交结匪类一事，我们可以过后再说。  
[charslot(slot = "m", name = "avg_npc_1871_1#2$1")]
[name="莫佚"]我还以为你要让他当场将我拿下，好将功折罪呢。  
[charslot(slot = "m", name = "avg_npc_2127_1#1$1")]
[name="椿"]大炎朝堂，不行此江湖草莽之事。  
[charslot(slot = "m", name = "avg_npc_1871_1#5$1")]
[name="莫佚"]说得好听。  
[charslot(slot = "m", name = "avg_npc_1871_1#2$1")]
[name="莫佚"]怂恿颉入岁陵，让这个对大炎而言更加危险的代理人代望而死，换取自己在大炎一步登天的资本，不是你，还有谁？  
[charslot(slot = "m", name = "avg_npc_1871_1#9$1")]
[name="莫佚"]也不知道衍兽若是泉下有知，会不会为了自己有这样一个后人脸红！  
[charslot(slot = "m", name = "

... (全文23568字符)
```

### level_act49side_08_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[stopmusic]
[dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="70_g4_tjdiscussionroom",screenadapt="coverall")]
[playMusic(intro="$m_bat_bitw2_intro",key="$m_bat_bitw2_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]
[charslot(slot = "M", name = "avg_npc_2127_1#1$1", duration=0.3)]
[delay(time=0.5)]
[charslot(slot = "L", name = "avg_1050_chen3_1#11$2", duration=0.1)]
[charslot(slot = "L", action="jump", posfrom="300,0", posto="0,0", power=5, times=5, duration=0.5)]
[charslot(slot = "M", action="jump", posto="200,0", power=1, times=1, duration=0.4)]
[PlaySound(key="$d_avg_metallicclick", volume=1)]
[delay(time=0.3)]
[PlaySound(key="$sheildimpact", volume=1)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0, block=true)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.1, block=true)]
[CameraShake(duration=0.5, xstrength=20, ystrength=0, vibrato=30, randomness=90, fadeout=true, block=false)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.1, block=true)]
[delay(time=1)]
[charslot(slot = "M", name = "avg_npc_2127_1#4$1",focus="m")]
[name="椿"]......差点就划到书架了。  
[charslot(slot = "M", name = "avg_npc_2127_1#1$1",focus="m")]
[name="椿"]我不是武痴，没有观览赤霄剑招的兴趣。你这一剑若是真使出来，倒可惜了天镜阁这许多书。  
[charslot(slot = "L", name = "avg_1050_chen3_1#11$2", focus="l")]
[name="陈"]可你也没有把握从我这里夺走信物。  
[charslot(slot = "M", name = "avg_npc_2127_1#1$1",focus="m")]
[name="椿"]是吗？  
[dialog]
[charslot]
直到这时，精灵才第一次认真挥动手中的玉笏与枯枝。
[dialog]
[playsound(key="$d_avg_singleblunt")]  
[delay(time=0.3)]
[playsound(key="$d_avg_twohandedblunt")]  
[Effect(name="$e_sandfall_01",layer = 1)]
无数枯槁的藤蔓从地面涌动而出，虬结成一双又一双巨手的形状。  
[dialog]
[playsound(key="$d_avg_groundcrack_tree")]  
[delay(time=1)]
[CameraShake(duration=0.8, xstrength=50, ystrength=50, vibrato=30, randomness=90, fadeout=true, block=false)]
[charslot(slot = "M", name = "avg_npc_1871_1#9$1",focus="m")]
[delay(time=0.8)]
[name="莫佚"]该死，她怎么这么难对付，你们司岁台的头儿难道是靠拳脚选出来的？  
[charslot(slot = "M", name = "avg_npc_1871_1#9$1",focus="m")]
[name="莫佚"]那书怎么背的来着......想起来了——好得很，正好现在又是秋天...... 
[charslot(slot = "M", name = "avg_npc_1871_1#3$1",focus="m")]
[multiline(name="莫佚")]“金曰从革”，
[charslot(slot="m",name="avg_npc_1871_1#4$1")]
[multiline(name="莫佚")]敕！
[multiline]
[dialog]
[charslot]
[playsound(key="$d_avg_magic_1")]  
[Blocker(a=1, r=255, g=255, b=50, fadetime=0.3, block=true)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.2, block=true)]
[charslot(slot = "M", name = "avg_npc_2127_1#10$1",focus="m")]
[name="椿"]......想不到区区盗匪，涉猎倒还算广。  
[charslot(slot="m",name="avg_npc_1871_1#9$1")]
[name="莫佚"]哼，论及阴阳五行之术，你这数典忘祖的家伙还未必比得过我。  
[charslot(slot="m",name="avg_npc_1871_1#9$1")]
[name="莫佚"]左乐，陈晖洁，该你们了！  
[dialog]
[charslot]
[PlaySound(key="$d_avg_clothmovement_heavy2", volume=1)]
[charslot(slot = "m",name = "avg_4121_zuole_1#1$1")]
[charslot(slot = "m",name = "avg_4121_zuole_1#1$1",action="zoom", poszoom = "0.5,0.5", scale=1.05, duration = 0.2)]
[charslot(slot = "m", afrom = 1, ato = 0, duration =0.3, block=true)]
[Delay(time=0.5)]
[charslot]
左乐上前，直扑椿的位置，意在扰乱她的应对。  
[dialog]
[PlaySound(key="$d_avg_ftrub", volume=0.8)]
[charslot(slot = "m", name = "avg_1050_chen3_1#11$2",posfrom="0,0",posto="80,0",afrom=1,ato=0,duration=0.2)]
[Delay(time=0.5)]
陈晖洁向后，拉开距离，只等抓住破绽再全力施为。  
[dialog]
[charslot]
[PlaySound(key="$d_avg_dagger", volume=0.8)]
[Blocker(a=0.8, r=1, g=1, b=1, fadetime=0.3, block=true)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.1, block=true)]
[Blocker(a=0.8, r=1, g=1, b=1, fadetime=0.3, block=true)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.1, block=true)]
莫佚居中，一道又一道利刃似的秋风从她周身转出，与那些藤蔓的手掌不断纠缠。  
而司岁台监正仍是面带着淡漠与怅然，立在原地，仿佛眼前只不过是一场她懒得再看下去的闹剧......
[dialog]
[charslot(slot = "m", name = "avg_1050_chen3_1#11$2",posfrom="0,0",posto="50,0",duration=0.8, isblock=true)]
[charslot(slot = "m", name = "avg_1050_chen3_1#11$2",afrom=1, ato=1, posfrom="50,0",posto="100,0",duration=0.8, isblock=false)]
[delay(time=1)]
[PlaySound(key="$d_avg_smashtable", volume=0.3)]
[CameraShake(duration=0.5, xstrength=15, ystrength=15, vibrato=20, randomness=70, fadeout=true, block=false)]
[charslot(slot="m",focus="n",block=true)]
直到陈晖洁一退再退，一直退到那扇紧闭的大门边上。  
[dialog]
[charslot]
[charslot(slot="m",name="avg_npc_1871_1#4$1")]
[name="莫佚"]该死......要顶不住了！  
[dialog]
[charslot]
[charslot(slot = "m", name = "avg_4121_zuole_1#4$1",posfrom="0,0",posto="-150,0",duration=0.3, isblock=true)]
[delay(time=0.3)]
[charslot(slot = "m", name = "avg_4121_zuole_1#5$1")]
[name="左乐"]陈姐姐！  
[dialog]
[charslot]
[charslot(slot = "m", name = "avg_1050_chen3_1#10$2")]
[name="陈"]赤霄......！  
[dialog]
[PlaySound(key="$d_sp_chixiaobadao", volume=1)]
[charslot(slot = "m", name = "avg_1050_chen3_1#6$2")]
[Blocker(a=1, r=1, g=1, b=1, fadetime=0.3, block=true)]
[Subtitle(text="<color=#d41f1f>云裂——  </color>", x=300, y=350, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle]
[charslot]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[PlaySound(key="$d_sp_chixiaobadao", volume=1)]
[PlaySound(key="$d_avg_breezetree", volume=0.8)]
[Blocker(a=0.8, r=1, g=1, b=1, fadetime=0.3, block=true)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.1, block=true)]
[delay(time=0.2)]
[charslot]
凌厉的剑气借着秋风将藤蔓一扫而空，精灵的眼中闪过了仅此一瞬的惊诧。  
[dialog]
[PlaySound(key="$d_avg_hiddenweapon_fast", volume=1)]
[delay(time=0.1)]
[PlaySound(key="$d_avg_hiddenweapon_fast", volume=0.8)]
[delay(time=0.4)]
[PlaySound(key="$d_avg_hiddenweapon_hitshield", volume=1)]
但紧接着，反而是从藤蔓上飞散的锋利枯叶朝三人飞去。  
[PlaySound(key="$d_avg_tearfabric", volume=1)]
莫佚忙不迭施术抵挡，枯叶仍然划破了三人的衣裳和包裹......
[PlaySound(key="$d_avg_breezeblow_amb",volume=0, channel="f", loop=true)]
[SoundVolume(volume=1, channel="f",fadetime=1)]
[stopmusic(fadetime=2)]
那离开界园后一直沉睡着的造物，也一并落在地上。 
[dialog]
[playsound(key="$d_avg_jadestatue_fall")]
[delay(time=1.5)]
[charslot(slot="m",name="avg_npc_2127_1#1$1",isblock=true)]
[name="椿"]这便是......界园里带出来的信物？  
[charslot(slot="m",name="avg_npc_2127_1#4$1")]

... (全文29856字符)
```

### level_act49side_09_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[stopmusic]
[dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[curtain(direction = 0,fillfrom = 0.1,fillto = 0.1, fadetime=0.1)]
[curtain(direction = 4,fillfrom = 0.1,fillto = 0.1, fadetime=0.1)]
[Background(image="70_g10_wardowntown",screenadapt="coverall")]
[focusout(type="bg", id="70_g10_wardowntown", from=0, to=0.8, duration=0.1, block=false)]
[playMusic(intro="$m_bat_ymmons_intro",key="$m_bat_ymmons_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]
[charslot(slot = "l", name = "avg_npc_1637_1#1$1",isblock=true)]
[charslot(slot = "R", name = "avg_npc_2135_1#1$1", action="jump", posto="-200,0", power=0, times=1, duration=0.5)]
[CameraShake(duration=0.5, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0, block=true)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.05, block=true)]
[PlaySound(key="$sheildimpact",volume=1)] 
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.05, block=true)]
[charslot(slot = "R", action="jump", posto="50,0", power=5, times=1, duration=1)]
[Delay(time=0.5)]
[charslot(slot = "l",posfrom="0,0",posto="60,0",duration=0.1,isblock=true)]
[PlaySound(key="$d_avg_attack_heavy",volume=1)] 
[charslot(slot = "r", action="shake", afrom=1 , ato=1, power=3, times=30, duration=0.3,isblock=true)]
[charslot(slot = "l",posfrom="60,0",posto="0,0",duration=1.2,isblock=false)]
[PlaySound(key="$d_avg_fog_blowaway", volume=0.8)]
[Effect(name="$e_vanish", layer = 1,x=120)]
[charslot(slot = "r", afrom=1,ato=0, duration=0.8)]
[delay(time=1)]
[charslot]
[PlaySound(key="$d_avg_magic_5",volume=1)] 
[Blocker(a=0.8, r=1, g=1, b=1, fadetime=0.3, block=true)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.1, block=true)]
[charslot(slot = "r", name = "avg_npc_2135_1#1$1",posfrom = "150,-50", posto = "150,0",duration=1,isblock=false)]
[delay(time=0.3)]
[charslot(slot = "l", name = "avg_npc_2135_1#1$1",posfrom = "-150,-50", posto = "-150,0",duration=1,isblock=false)]
[delay(time=0.3)]
[charslot(slot = "m", name = "avg_npc_2135_1#1$1",posfrom = "0,-50", posto = "0,0",duration=1.2, isblock=true)]
[delay(time=1)]
[charslot]
[charslot(slot = "r", name = "avg_npc_1637_1#1$1", focus="l")]
[charslot(slot = "l", name = "avg_npc_1637_1#1$1", focus="l",isblock=true)]
[name="筋疲力竭的守军"]没完没了...... 
[charslot(slot = "r", focus="r")]
[name="惶恐不安的守军"]小心！  
[dialog]
[charslot]
[charslot(slot = "r", name = "avg_npc_1637_1#1$1",posfrom="150,0", posto="150,0")]
[charslot(slot = "l", name = "avg_npc_2135_1#1$1",posfrom="-100,0", posto="200,0",duration=0.5, isblock=false)]
[delay(time=0.3)]
[charslot(slot = "m", name = "avg_npc_1637_1#1$1",posfrom="400,0", posto="100,0",duration=0.25, focus="m",isblock=true)]
[CameraShake(duration=0.5, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0, block=true)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.05, block=true)]
[PlaySound(key="$swordtsing5",volume=1)] 
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.05, block=true)]
[charslot(slot = "l", action="jump", posto="-350,0", power=5, times=1, duration=0.5,isblock=true)]
[PlaySound(key="$d_avg_fog_blowaway", volume=0.8)]
[Effect(name="$e_vanish", layer = 1,x=-350)]
[charslot(slot = "l", afrom=1,ato=0, duration=0.8,isblock=true)]
[Delay(time=0.5)]
[charslot]
[charslot(slot = "r", name = "avg_npc_1637_1#1$1", focus="r")]
[charslot(slot = "l", name = "avg_npc_1637_1#1$1", focus="r",isblock=true)]
[name="筋疲力竭的守军"]这些怪物到底是从哪里来的，到底还剩多少？！
[charslot(slot = "l", focus="l",isblock=true)]  
[name="惶恐不安的守军"]不仅没有变少，反而越来越多了。  
[name="惶恐不安的守军"]......听说昨天一夜，北三营已经折了一半人进去......  
[charslot(slot = "r",focus="r",isblock=true)]
[name="筋疲力竭的守军"]什么？！  
[charslot(slot = "l", focus="l",isblock=true)]
[name="惶恐不安的守军"]发现了吗，不知道从什么时候开始，这些凭空冒出来的怪物变得越来越真实，攻击性也越来越强......  
[charslot(slot = "r",focus="r",isblock=true)]
[name="筋疲力竭的守军"]*炎国粗口*，支援，支援到底在哪？
[name="筋疲力竭的守军"]再这样打下去，马上就要弹尽粮绝了——  
[dialog]
[delay(time=0.3)]
[charslot(slot="r",posfrom="0,0",posto="0,-30",duration=0.5,isblock=true)]
[charslot(slot="r",posfrom="0,-30",posto="0,-150",afrom="1",ato="0",duration=0.3)]
[PlaySound(key="$bodyfalldown1", volume=1)]
[delay(time=0.8)]
[charslot]
[curtain(direction = 0,fillfrom = 0.1,fillto = 0.01, fadetime=1.5,block=false)]
[focusout(type="bg", id="70_g10_wardowntown", from=0.8, to=0, duration=1.5, block=false)]
[curtain(direction = 4,fillfrom = 0.1,fillto = 0.01, fadetime=1.5,block=true)]
[curtain]
[delay(time=0.8)]
[PlaySound(key="$d_avg_fsmetal", volume=1)]
[charslot(slot = "m", name = "avg_npc_1634_1#1$1", afrom = 0, ato = 0, duration=0)]
[charslot(slot = "m", action="zoom", poszoom = "0.5,0.5", scale=0.95,duration = 0)]
[delay(time=0.1)]
[charslot(slot = "m", action="zoom", poszoom = "0.5,0.5", scale=1,duration = 1.5)]
[charslot(slot = "m", afrom = 0, ato = 1, duration = 1.5, isblock=true)]
[Delay(time=1.5)]
[charslot]
[charslot(slot = "r", name = "avg_npc_2135_1#1$1",posfrom = "150,0", posto = "150,0",isblock=false)]
[charslot(slot = "l", name = "avg_npc_2135_1#1$1",posfrom = "-150,0", posto = "-150,0",isblock=false)]
[charslot(slot = "m", name = "avg_npc_2135_1#1$1",isblock=true)]
[delay(time=0.3)]
[playsound(key="$e_skill_skulsrsword")]
[Effect(name="$e_bladeline_01_large",rox=0,roy=0,roz=0,layer = 1)]
[delay(time=0.2)]
[playsound(key="$e_skill_skulsrsword")]
[Effect(name="$e_bladeline_01_large",rox=0,roy=0,roz=-40,layer =2)]
[PlaySound(key="$d_avg_fog_blowaway", volume=0.8)]
[Effect(name="$e_vanish", layer = 1,x=-250)]
[PlaySound(key="$d_avg_fog_blowaway", volume=0.8)]
[Effect(name="$e_vanish", layer = 2,x=0)]
[PlaySound(key="$d_avg_fog_blowaway", volume=0.8)]
[Effect(name="$e_vanish", layer =3,x=250)]
[charslot(slot = "r",afrom=1,ato=0,duration=1,block=false)]
[charslot(slot = "l",afrom=1,ato=0,duration=1,block=false)]
[charslot(slot = "m"

... (全文20763字符)
```

### level_act49side_09_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[stopmusic]
[dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="58_g7_forbiddencity",screenadapt="coverall")]
[playMusic(intro="$m_bat_act23side_01_intro",key="$m_bat_act23side_01_loop", volume=0.6)]
[PlaySound(key="$d_avg_slmddrprn",volume=0, channel="rain", loop=true)]
[SoundVolume(volume=0.5, channel="rain",fadetime=2)]
[avgdisplay(id = "1", style = "bgeffect", name = "$eb_raingrey", slot = "bgover",y=-250, layer = 1)]
[PlaySound(key="$d_avg_rainlight_loop", volume=0.5, loop=true, channel="ra")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0, block=true)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0.05, block=true)]
[CameraShake(duration=2, xstrength=40, ystrength=40, vibrato=30, randomness=90, fadeout=true, block=false)]
[charslot(slot="L", name = "char_2005_weiyw_1#4")]
[charslot(slot = "R", name = "avg_1050_chen3_1#1$1")]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0.05, block=true)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.05, block=true)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0.05, block=true)]
[charslot(slot = "left", name = "char_2005_weiyw_1#4", action="jump", posto="100,0", power=5, times=1, duration=0.05)]
[charslot(slot = "R", name = "avg_1050_chen3_1#1$1", action="jump", posto="-100,0", power=5, times=1, duration=0.05)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.05, block=false)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.05, block=true)]
[PlaySound(key="$swordtsing4", volume=1)]
[CameraShake(duration=1, xstrength=30, ystrength=5, vibrato=30, randomness=90, fadeout=true, block=false)]
[delay(time=0.3)]
[PlaySound(key="$d_avg_ftrub", volume=0.8)]
[charslot(slot = "left",posfrom="100,0",posto="180,0",duration=0.8,isblock=false)]
[charslot(slot = "r",posfrom="-100,0",posto="80,0",duration=0.8,isblock=true)]
[charslot(slot = "r",action="shake", power=3, times=30,focus="r",duration=0.3)]
[delay(time=0.5)]
[charslot(slot = "r",name = "avg_1050_chen3_1#11$1",focus="r")]
[name="陈"]哈，哈......  
[charslot(slot = "l",name = "char_2005_weiyw_1#4",focus="l")]
[name="魏彦吾"]你竟然......想用天瞠之剑？  
[charslot(slot = "r",name = "avg_1050_chen3_1#11$1",focus="r")]
[name="陈"]......害怕了？  
[dialog]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.05, block=true)]
[PlaySound(key="$swordtsing1", volume=1)]
[CameraShake(duration=0.3, xstrength=50, ystrength=50, vibrato=30, randomness=90, fadeout=true, block=false)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.05, block=true)]
[PlaySound(key="$d_avg_clothmovementsp", volume=1)]
[charslot(slot = "left", name = "char_2005_weiyw_1#4", action="jump", posto="-210,0", power=5, times=1, duration=0.15)]
[charslot(slot = "R", name = "avg_1050_chen3_1#1$1", action="jump", posto="10,0", power=5, times=1, duration=0.05)]
[dialog]
[delay(time=1)]
[charslot(slot = "l", name = "char_2005_weiyw_1#1",focus="l")]
[name="魏彦吾"]那位宗师曾评价你的剑术，炉火纯青，但尚未登峰造极。  
[charslot(slot = "l", name = "char_2005_weiyw_1#1",focus="l")]
[name="魏彦吾"]这五年，你的剑术进步不少，能将赤霄剑法领悟到这般境界已然出乎我的预期。  
[charslot(slot = "l", name = "char_2005_weiyw_1#1",focus="l")]
[name="魏彦吾"]但离天瞠，始终隔着一层。  
[charslot(slot = "r", name = "avg_1050_chen3_1#1$1",focus="r")]
[name="陈"]......天瞠之剑，当绝则绝。  
[charslot(slot = "r", name = "avg_1050_chen3_1#10$1",focus="r")]
[name="陈"]不破不立，破而后立。云裂之后，方能见苍穹怒目。  
[charslot(slot = "r", name = "avg_1050_chen3_1#1$1",focus="r")]
[name="陈"]剑随心动，招出无悔。若一念回首，则剑失锋芒，反害其身。  
[charslot(slot = "l", name = "char_2005_weiyw_1#1",focus="l")]
[name="魏彦吾"]我只是对你提起过天瞠的剑意......你记得很清楚。 
[charslot(slot = "l", name = "char_2005_weiyw_1#5",focus="l")] 
[name="魏彦吾"]可你应该知道自己心间的迷障尚未破除，所以你没有办法使出这一剑。  
[charslot(slot = "l", name = "char_2005_weiyw_1#5",focus="l")]
[name="魏彦吾"]弃剑吧。我唯独不想再跟你走到这一步。  
[charslot(slot = "r", name = "avg_1050_chen3_1#11$1",focus="r")]
[name="陈"]如果我不把书刀给你，你就会对我用出那一剑吗？  
[charslot(slot = "r", name = "avg_1050_chen3_1#11$1",focus="r")]
[name="陈"]......就像三十五年前那样？  
[charslot(slot = "l", name = "char_2005_weiyw_1#2",focus="l")]
[name="魏彦吾"]......晖洁，别逼我。  
[charslot(slot = "r", name = "avg_1050_chen3_1#11$1",focus="r")]
[name="陈"]你在四十年前走入禁城的时候，你在决定小塔和她父亲生死的时候，是否也像剑意所说的那样......“招出无悔”？  
[charslot(slot = "l", name = "char_2005_weiyw_1#3",focus="l")]
[name="魏彦吾"]晖洁！  
[charslot(slot = "r", name = "avg_1050_chen3_1#11$1",focus="r")]
[name="陈"]如果赤霄的最后一剑就是这样，那我想必永远也用不出这一剑。  
[charslot(slot = "r", name = "avg_1050_chen3_1#10$1",focus="r")]
[name="陈"]审判。公义。  
[charslot(slot = "r", name = "avg_1050_chen3_1#11$1",focus="r")]
[name="陈"]善恶对错不是砝码，放在天平两边就能自然而然地分出高下......盖棺定论从来都不是一个好词。
[charslot(slot = "r", name = "avg_1050_chen3_1#13$1",focus="r")]  
[name="陈"]而人......就更是如此。没有一个人应当被决绝地放弃。
[charslot(slot = "r", name = "avg_1050_chen3_1#13$1",focus="r")]  
[name="陈"]维多利亚围城里的工人，乌萨斯冻土上的战士，甚至就连多索雷斯的赌场老板，都能明白这个道理。  
[charslot(slot = "r", name = "avg_1050_chen3_1#11$1",focus="r")]
[name="陈"]所以，你说得对。我不会用天瞠。我学不会。那不是我的剑。  
[charslot(slot = "l", name = "char_2005_weiyw_1#4",focus="l")]
[name="魏彦吾"]你要说什么？  
[charslot(slot = "r", name = "avg_1050_chen3_1#1$1",focus="r")]
[name="陈"]与其决绝，与其抛弃，我宁可选择明知不可为而为之。  
[charslot(slot = "l", name = "char_2005_weiyw_1#5",focus="l")]
[name="魏彦吾"]......
[charslot(slot = "l", name = "char_2005_weiyw_1#4",focus="l")]
[name="魏彦吾"]晖洁......你仍然不懂！  
[charslot(slot = "r", name = "avg_1050_chen3_1#7$1",focus="r")]
[name="陈"]嗯。我的确不懂。  
[charslot(slot = "r", name = "avg_1050_chen3_1#4$1",focus="r")]
[name="陈"]我其实不懂那一夜究竟发生了什么，你的父亲究竟是死在赤霄剑下还是另有隐情。  
[charslot(slot = "r", name = "avg_1050_chen3_1#4$1",focus="r")]
[name="陈"]我也不懂你当时做出选择的心境。我知道爱德华和小塔身上背负着血脉的诅咒，但我毕竟只能旁观。  
[charslot(slot = "r", name = "avg_1050_chen3_1#14$1",focus="r")]
[name="陈"]我甚至不懂母亲去世时何以对你、对父亲，甚至对我，是那般怨恨。  
[charslot(slot = "r", name = "avg_1050_chen3_1#14$1",focus="r")]
[name="陈"]我只知道一件事。小塔也知道。  
[charslot(slot = "r", name = "avg_1050_chen3_1#11$1",focus="r")]
[name="陈"]死者的道歉没有任何意义。如果有想道歉的人，就活着去见他。  
[chars

... (全文43105字符)
```

### level_act49side_10_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[stopmusic]
[dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="bg_wilderness_m",screenadapt="coverall")]
[bgeffect(name="$eb_sand",layer=1)]
[PlaySound(key="$d_avg_sand_lp", volume=0.5, loop=true, channel="sa")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[animtext(id = "at1", name = "group_location_stamp", style="avg_only_medium", pos = "-400,-200", block = false)]<p=2>望日</>
[delay(time=3)]
[animtextclean]
[delay(time=1)]
[playMusic(key="$midautumn", volume=0.6)]
[Delay(time=1)]
[PlaySound(key="$d_avg_hornstart", volume=0.5)]
黄沙蔽日。
[dialog]
[delay(time=3)]
蹲伏在玉门城的阴影里，左乐抬眼望去，屏风卫、沙渠、已然清晰的炮口......
[PlaySound(key="$d_avg_grounddivide_rumble2",loop=true,channel="di",volume=1)]
整座城市正朝着岁陵的方向缓缓前进。
[dialog]
[PlaySound(key="$d_avg_sandftsingle", volume=1)]
[charslot(slot="m",name="avg_4121_zuole_1#1$1",duration=0.8, isblock=true)] 
[name="左乐"]玉门的确已经开拔了。  
[charslot(slot="m",name="avg_4121_zuole_1#1$1")]
[name="左乐"]可......陛下又怎么会在岁兽还未苏醒时就下令进攻？
[dialog]
[charslot(slot="m",focus="n")]
片刻的犹豫之后，玉门已经和低伏的秉烛人咫尺之遥。
他面前很快就已没有路，只有几乎垂直于地面的城墙。
[charslot]
[StopSound(channel="di", fadetime=2)]
[dialog]
[PlaySound(key="$flashback", volume=0.8)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0, block=true)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.5, block=true)]
[stopsound(channel="sa")]
[charslot]
[bgeffect]
[Background(image="35_g3_yumenobservationtower_d",screenadapt="coverall")]
[CameraEffect(effect="Grayscale", amount=0.8, keep=true)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.5, block=true)]
[Delay(time=0.5)]
[charslot(slot="m",name="avg_2024_chyue_1#6$1")]
[name="重岳"]想从这沙渠跑出去？你的轻功当真练到家了？更何况，你这一出去......  
[charslot(slot="m",name="avg_2024_chyue_1#4$1")]
[name="重岳"]......罢了，看你自己。  
[dialog]
[PlaySound(key="$flashback", volume=0.8)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0, block=true)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.5, block=true)]
[charslot]
[Background(image="35_g8_yumenarena",screenadapt="coverall")]
[charslot(slot="m",name="avg_npc_788_1#7$1")]
[CameraEffect(effect="Grayscale", amount=0.8, keep=true)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.5, block=true)]
[Delay(time=0.5)]
[name="左宣辽"]别以为摔成这样就能逃过处罚。你自己胡闹也就罢了，竟然还带着青萍！  
[charslot(slot="m",focus="n")]
[name="云青萍"]将军，左乐兄是因为——  
[charslot(slot="m",name="avg_npc_788_1#4$1")]
[name="左宣辽"]你不用替他遮掩。  
[charslot(slot="m",name="avg_npc_788_1#4$1")]
[name="左宣辽"]他在跳下去之前，就该想好怎么上来！一腔蛮勇，只知道争强斗狠，累得他人为他劳心费神！  
[charslot(slot="m",name="avg_npc_788_1#2$1")]
[name="左宣辽"]......  
[charslot(slot="m",name="avg_npc_788_1#7$1")]
[name="左宣辽"]回去候着，待伤好些，自己来领罚。
[dialog]
[PlaySound(key="$flashback", volume=0.8)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0, block=true)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.5, block=true)]
[charslot]
[Background(image="bg_wilderness_m",screenadapt="coverall")]
[CameraEffect(effect="Grayscale", amount=0, keep=true)]
[bgeffect(name="$eb_sand",layer=1)]
[PlaySound(key="$d_avg_sand_lp", volume=0.5, loop=true, channel="sa")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.5, block=true)]
[Delay(time=1)]
[PlaySound(key="$d_avg_grounddivide_rumble2",loop=true,channel="di",volume=0.8)]
[SoundVolume(volume=0, channel="di",fadetime=3)]
城墙已进逼到左乐身前几丈远的位置。
[dialog]
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[PlaySound(key="$d_avg_Qinggong", volume=1)]
于是左乐一跃而起，往日常被人称赞的轻功而今成了他唯一的依仗。
[dialog]
[stopsound(channel="di",fadetime=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0.5, block=true)]
[delay(time=0.5)]
[bgeffect]
[bgeffect(name="$eb_speedline",layer=1)]
[gridbg(imagegroup="47_g15_eveningglow_L1/47_g15_eveningglow_R1/47_g15_eveningglow_L2/47_g15_eveningglow_R2", solidwidth="1024/1024/1024/1024", solidheight="576/576/576/576",x=-600,y=300, fadetime=0)]
[largebgtween(duration =0.5,xScaleFrom=0.75, xScaleTo=0.8, yScaleFrom=0.75, yScaleTo=0.8, block = false)]
[CameraShake(duration=10, xstrength=5, ystrength=5, vibrato=20, randomness=70, fadeout=true, block=false)]
[playsound(key="$d_avg_citywall_run", loop=true, channel="bgs",volume=0)]
[SoundVolume(volume=0.7, channel="bgs",fadetime=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.5, block=true)]
此时的玉门，沙渠并未开启，屏风卫却全部高高升起，平整的城墙极难借力，一失手，便是粉身碎骨。
半程之下，尚能借着墙垛发力。再往上走，便已如千钧之重。
[name="左乐"]快些......
[dialog]
[PlaySound(key="$d_avg_clothmovementsp", volume=1)]
[gridbg(imagegroup="47_g15_eveningglow_L1/47_g15_eveningglow_R1/47_g15_eveningglow_L2/47_g15_eveningglow_R2",xScale=0.83, yScale=0.83, solidwidth="1024/1024/1024/1024",x=-600,y=300, solidheight="576/576/576/576", fadetime=0)]
[largebgtween(duration =0.5,xScaleFrom=0.83, xScaleTo=0.88, yScaleFrom=0.83, yScaleTo=0.88, block = false)]
[focusout(duration=0.2, type="lbg", from=1, to=1, block=true)]
[delay(time=0.2)]
[focusout(duration=0.5, type="lbg", from=1, to=0, duration=0.1, block=true)]
透过黄沙，少年几乎就快望见城头将士的身影。
他们中的许多人已忘记了自己在这城墙之上守了多少年月。
然而，那突如其来的一声号角，便要他们为这场新的狩猎付出余生。
[name="左乐"]再快些！
[dialog]
[PlaySound(key="$d_avg_clothmovement_heavy2", volume=1)]
[gridbg(imagegroup="47_g15_eveningglow_L1/47_g15_eveningglow_R1/47_g15_eveningglow_L2/47_g15_eveningglow_R2",xScale=0.93, yScale=0.93, solidwidth="1024/1024/1024/1024",x=-600,y=300, solidheight="576/576/576/576", fadetime=0,blok=true)]
[largebgtween(duration =0.5,xScaleFrom=0.93, xScaleTo=0.95, yScaleFrom=0.93, yScaleTo=0.95, block =false)]
[focusout(duration=0.2, type="lbg", from=1, to=1, block=true)]
[delay(time=0.2)]
[focusout(duration=0.2, type="lbg", from=1, to=0, duration=0.1, block=true)]
爬到更高处，思虑反而澄澈，脚下的步伐也更坚定。
即便如此，高墙的尽头也并非坦途。
[Dialog]
[stopmusic(fadetime=2)]
[StopSound(channel="sa", fadetime=2)]
[StopSound(channel="bgs", fadetime=2)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[largebg]
[bgeffect]
[Background(image="35_g3_yumenobservationtower_d"

... (全文35871字符)
```

### level_act49side_10_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Delay(time=1)]
[Background(image="70_g7_suilingcore",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=2)]
[playMusic(intro="$plot_intro",key="$plot_loop", volume=0.6)]
[charslot(slot="m",name="avg_npc_2129_1#11$1",duration=0.5)]
[delay(time=1)]
[PlaySound(key="$d_avg_rockbreakout")]
[Blocker(a=0.5, r=1, g=1, b=1, fadetime=0.3, block=true)]
[CameraShake(duration=1, xstrength=20, ystrength=20, vibrato=35, randomness=90, fadeout=true)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1)]
[delay(time=1)]
[charslot(duration=0.5)]
[delay(time=0.5)]
[charslot(slot="m",name="avg_2027_wang_1#13$1")]
[charslot(slot ="m", action="shake", power=6, times=30, duration=0.5)]
[delay(time=0.5)]
[PlaySound(key="$bodyfalldown2")]
[charslot(duration=0.3)]
[charslot(slot = "m",posfrom = "0,0", posto = "0,-30",duration = 0.3)]
[CameraShake(duration=0.3, xstrength=10, ystrength=20, vibrato=35, randomness=90, fadeout=true, block=true)]
[delay(time=0.3)]
[name="望"]唔呃——
[charslot]
[charslot(slot="m",name="avg_npc_2129_1#9$1")]
[name="望？"]可悲......不出意料，依然是，毫无二致的结局。
[name="望？"]对我而言，作为打发时间的消遣，你做得还不错。
[charslot(slot="m",name="avg_npc_2129_1#8$1")]
[name="望？"]不过，也到此为止了......我也得感谢，你送来的这一份重要的，礼物。
[name="望？"]再加上你的这一份力量，我便足以完全苏醒，彻底吞噬你们所有人的力量。
[name="望？"]你们所有人，千年来的积蓄都会成为供给于我的养分，我将获得远胜于千年前的力量。
[charslot(slot="m",name="avg_npc_2129_1#12$1")]
[name="望？"]我会成为真正的神明，我将统治这片大地上的一切，带领所有羸弱如虫蚁的生命跨过那一道隔绝星穹的帷幕，甚至是那终极的黑暗！
[name="望？"]凭借与你一致的权能......我算得出，我看得到那个将来。
[name="望？"]而你，也可以作为我的一部分，用我的眼睛去看。
[charslot]
[name="望"]痴人......说梦......
[charslot(slot="m",name="avg_npc_2129_1#11$1")]
[name="望？"]......何必抗拒？你将像那个被你称为妹妹的意识一样，回归你本就应在的地方，回归你的来处，那片原初的混沌。
[name="望？"]你们十二个意识汲汲追求的梦，都将在那片混沌中实现。
[name="望？"]不需要苦不堪言的磨炼。不需要耗竭心神的计算。不需要一触即破的逍遥。
[name="望？"]你将是我，你将是我们。
[charslot]
莫大的恐怖不讲道理地侵入代理人的心神。心跳加快，冷汗滴落，身体不由自主地想要弹起，却连转转眼珠也做不到。
赐福。
分裂的意识即将回归本体，对人而言如同酷刑的赐福。
[charslot(slot="m",name="avg_npc_2129_1#12$1")]
[name="望？"]放弃受苦的欲望，放弃无用的执念，放弃自顾自背上的责任，放弃比照渺小的人类学习的拙劣的情感。
[name="望？"]放弃那些耗竭你的，拥抱那些滋养你的。
[name="望？"]痛苦理当消弭，你将成为我庞大意识中一个可纪念的节点，一段徒劳......却也可敬的过往。
[charslot]
[focusout(duration=3, type="bg", from=0, to=1)]
痛苦......消弭？
痛苦从皮肤渗入骨髓，恐怖由脊椎传遍全身。代理人眼前的景象渐渐模糊。
[charslot(slot="m",name="avg_npc_2129_1#12$1")]
[name="望？"]闭上眼。
[dialog]
[Blocker(a=0.6, r=0, g=0, b=0, fadetime=0.5, block=true)]
[Subtitle(text="对，闭上双眼。你不必用自己的眼看，我的眼即是你的眼。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="何必不舍......你从一开始，不就这么觉得吗？", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="这人间，似乎也没有你兄弟姐妹所说的那般有趣——", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[subtitle]
[dialog]
[charslot(slot="m",name="avg_2027_wang_1#5$1")]
[Blocker(a=0.3, r=1, g=0, b=0, fadetime=0.3, block=true)]
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=35, randomness=90, fadeout=true, block=false)]
[PlaySound(key="$e_skill_skulsrsword", volume=0.9)]
[delay(time=1)]
[charslot(duration=2)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[delay(time=1)]
[Blocker(a=0.6, r=0, g=0, b=0, fadetime=0.5, block=true)]
[Subtitle(text="......哼，这点反抗之心，就这么难以消磨？", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="无妨。不过是多一个纠缠不清的意识需要慢慢消化罢了。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="这做了一千年的大梦......", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="......终于该醒了。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[subtitle]
[stopmusic(fadetime=2)]
[delay(time=2)]
[Subtitle(text="不......", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="......不对！", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[subtitle]
[dialog]
祂以为自己已经碾碎了那一部分分身的意识......
但是祂并没有感受到，一百二十年前，分散出的力量回归己身的感觉。
[dialog]
[Subtitle(text="这到底是怎么回事......", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="为何......我还是在梦中？！", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[subtitle]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Background]
[playMusic(key="$m_act31side_bat1_loop", volume=0.6)]
[bgeffect(name="$eb_sea_bg",layer=1)]
[delay(time=0.8)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[delay(time=1)]
[Image(image="70_i12", xScale=1.2, yScale=1.2,screenadapt="coverall",fadetime=2)]
[delay(time=1)]
[ImageTween( xScaleTo=1, yScaleTo=1, duration=60, block=false)]
[focusout(duration=3, type="bg", from=1, to=0)]
[bgeffect(layer=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=3, block=true)]
诗人举起手中的酒，并不敬天，而是酹地。
酒液落在地上，亘古的黄土被酒溅起，化作须臾飘散的扬尘。
[name="令"]尚蜀一别，堪堪又是一个冬夏。
[name="令"]在那之后，我无暇梦你，只因这人间比你值得在意的东西实在太多。
[name="令"]而你......
[name="令"]......哈。
[name="令"]用梦，用想象，用尚未发生的事情让人屈服？你和他，你们倒真是棋逢对手，将遇良才......
[name="令"]可我仿佛看到，在你们的对局中，还有不少编排我的故事？
[name="令"]......谁料平生狂酒客，如今变作酒悲人？
[name="令"]人家的诗是好诗，可用在这个关口，格调便落了下乘。
[name="令"]我帮你换一句吧。不如就......
[name="令"]雨后飞花知底数......醉来赢取自由身？
[name="令"]二妹，如何？
[name="均"]人家的词是好词，气韵也好，只是从你嘴里吟出，就显得洒脱过头，倒像是你要置身事外了。
[name="令"]哈哈，你、我、颉、夕，我们向来是没法达成一致的。
[name="令"]那便换你开嗓，为我们共同的这个我唱上一曲，如何？
[name="均"]不了。
[name="令"]你还是不愿破这个誓？
[name="均"]颉并没有回来。
[name="均"]不过，我会为你抚琴。
杀伐的战场不知何时被沉静的伏流淹没，水面上的波纹颤动，化成一双巨眼的模样。
即便在水中，那眼睛仍然狰狞，痛苦，近乎癫狂地瞪着周遭一切。
而乐师轻轻抚动琴弦。
[name="令"]是这首啊。
[name="令"]看来二妹倒也不是不爱喝酒，只是......
[name="令"]......
诗人便在这河中和着琴声举杯，两颊染上酡红。
她并未依调而唱，而是朗声高诵，却并不与清幽的乐声有丝毫抵牾。
漫天星斗随着一奏一诵的二人旋转，最终融入一池清水，于是那水也泛起些许苦涩，些许芳醇。
连那圆睁的眼，也不免带上了三分醉意。
[name="令"]劝君更尽一杯酒......
不知何时，起先险绝高绝的乐声渐渐向下，却也从起初的几不可闻，逐渐变成萦绕水中，挥之不去的低音。
仍是古朴的琴音，却不再是清幽婉转，仿佛那琴弦的捻合只用了一分丝，余下的是三分思念，三分悲愤，三分决绝。
可诗人的朗诵却越来越轻，越来越高，如耳语，如抚慰，如同连线的雨，谁人妄图用手拂去，也不过是湿了自家的衣。
一低，一高，一克己，一洒脱。
人声琴音交织，织就了一个让巨兽长眠的梦。
[Dialog]
[Blocker(a=0.6, r=0, g=0, b=0, fadetime=1.5, block=true)]
[Sticker(id="st1", multi = true, text="劝君更尽一杯酒......", x=300,y=300, alignment="center", size=24, width=700,duration=1,delay=0,block=true)]
[Sticker(id="st1",duration=1)]
[delay(t

... (全文32929字符)
```

### level_act49side_11_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Delay(time=1)]
[PlaySound(key="$d_avg_sandstone")]
[Background(image="70_g8_suilingcoreruins",screenadapt="coverall")]
[CameraShake(duration=3, xstrength=10, ystrength=10, vibrato=50, randomness=30, fadeout=true, block=false)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[playMusic(key="$m_bat_wang", volume=0.6)]
[Delay(time=2)]
[charslot(slot="m",name="avg_npc_2129_1#11$1",duration=1)]
[delay(time=2)]
[name="岁"]......背逆。
[name="岁"]你们之中的每一个，都打算背逆我到底，是吗？
[charslot(slot="m",name="avg_2027_wang_1#11$1")]
[name="望"]......没错。我们每一个，都不会束手就擒，变成你的一部分。
[name="望"]我们作为自己活过，这就是我们有别于你的根源。
[charslot(slot="m",name="avg_npc_2129_1#11$1")]
[name="岁"]作为......人？
[charslot(slot="m",name="avg_npc_2129_1#4$1")]
[name="岁"]你们一个个以人自居，还试图以种种妄念来挑战我。
[name="岁"]你们凭靠假借于我的力量，在渺小的族群中赢得一席之地，却又要卑微地隐藏起自己的爪锋与獠牙，装出一副无害的模样。
[name="岁"]这样就是你所谓的，作为人而活着？！
[charslot(slot="m",name="avg_2027_wang_1#3$1")]
[name="望"]你还是不懂......你不会懂，只因你从未活过。
[charslot(slot="m",name="avg_2027_wang_1#11$1")]
[name="望"]而我同样清楚......你的傲慢从何而来。
[name="望"]你可以一眼望穿自太古至终末的所有时间，哪怕你的神识已经在太虚中遨游千万载，你也从未有过一个可以对谈的同族。
[charslot(slot="m",name="avg_2027_wang_1#10$1")]
[name="望"]你只是在这一片可悲的虚无中，将自己当作了至高无上的神明。
[charslot(slot = "m", focus = "n")]
我再清楚不过，那究竟是什么样的感觉。
直到有一人，为我起了一个名字。
[charslot(slot="m",name="avg_2027_wang_1#11$1")]
[name="望"]可你从来不是谁的命运......无论是这片大地上的人，还是我们。
[name="望"]你更不会懂，对于一个已经一无所有的人而言......
[charslot(slot="m",name="avg_2027_wang_1#4$1")]
[name="望"]......命运本身，何其无力。
[charslot(slot="m",name="avg_npc_2129_1#11$1")]
[name="岁"]好......既然你胆敢重复无谋的挑战，那我同样不介意再摧毁一次你的妄想。
[charslot(slot="m",name="avg_npc_2129_1#12$1")]
[name="岁"]一百二十年前我杀死过你，再杀死你一次，不过易如反掌！
[charslot(slot="m",name="avg_2027_wang_1#11$1")]
[name="望"]难道你以为我会怕？
[name="望"]......我已经输惯了。
[charslot(slot="m",name="avg_npc_2129_1#11$1")]
[name="岁"]......？
[charslot(slot="m",name="avg_2027_wang_1#11$1")]
[name="望"]我已经输掉了太多宝贵的东西，满盘皆输。
[charslot(slot = "m", focus = "n")]
尊严，荣誉，信任，自由，自我。
还有，至亲之人。
[charslot(slot="m",name="avg_2027_wang_1#11$1")]
[name="望"]你觉得一个输无可输的人，真的会害怕什么吗？
[charslot(slot="m",name="avg_2027_wang_1#3$1")]
[name="望"]那么，你呢？
[name="望"]你是否还会害怕，再遭受一次如同千年前一样惨痛的失败......
[name="望"]你又是否会因为害怕，迟疑不前？
[charslot(slot="m",name="avg_npc_2129_1#4$1")]
[name="岁"]......笑话！
[name="岁"]你不过是妄想要取代我，占据这副身躯——我又岂会让你如愿！
[charslot(slot="m",name="avg_npc_2129_1#12$1")]
[name="岁"]既然如此，我只要让这副躯体先一步醒来——
[dialog]
[charslot]
[Background(image="70_g8_suilingcoreruins",screenadapt="coverall",fadetime=3)]
[focusout(duration=2, type="bg", from=0, to=1)]
[CameraShake(duration=1.5, xstrength=15, ystrength=15, vibrato=55, randomness=50, fadeout=true, block=false)]
[BackgroundTween(xScaleFrom=1, yScaleFrom=1, xScaleTo=1.2, yScaleTo=1.2, duration=2)]
[PlaySound(key="$d_avg_hugemonsterroar")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=3, block=true)]
巨兽伸出那如同山岳般庞大的利爪。
无数个巨兽在无数个岁陵中，向同一个代理人伸出无数个如同山岳的利爪。
哪怕这里仍是梦境，只要在所有的梦境之中都抹除这张令人生厌的脸，祂的苏醒就再无任何阻碍。
[dialog]
[Background(image="bg_black",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1.5, block=true)]
[PlaySound(key="$d_gen_surfacefrozen",channel="2")]
[PlaySound(key="$d_avg_punchairwall")]
[avgdisplay(id="1", name="act49side_02", style="animekv", slot="cgover",  scalex=1.1, scaley=1.1, entryfrom=0, entryto=0.3, duration=0.3, block=true)]
[delay(time=0.5)]
[CameraShake(duration=3, xstrength=5, ystrength=5, vibrato=50, randomness=30, fadeout=true, block=false)]
[avgdisplay(id="1", name="act49side_02", style="animekv", slot="cgover",  scalex=1.1, scaley=1.1, entryfrom=0.3, entryto=1, duration=3, block=true)]
[name="岁"]——！
[name="岁"]怎么回事......
一记重击，蕴含着凶暴无匹的力量切实落在祂的躯体上，这样的力量竟然让祂感觉到熟悉。
祂意识到自己，在这一瞬间失去了与那庞大躯体的连接。
究竟是谁，还能对这副身躯造成如此的伤害？！
[focusout(duration=0, type="bg", from=0, to=0)]
[dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[charslot]
[avgdisplay(id="1")]
[curtain(direction = 7,fillfrom = 1,fillto = 1, fadetime=0)]
[curtain(direction = 3,fillfrom = 1,fillto = 1, fadetime=0, block=true)]
[Image(image="70_i14",screenadapt="coverall",xScale=1.3,yScale=1.3,x=200,y=-100)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.5, block=true)]
[blocker(afrom=1, rfrom=0, gfrom=0, bfrom=0, a=0, r=0, g=0, b=0, fadetime=1)]
[PlaySound(key="$d_avg_tearspace",delay=1)]
[CameraShake(duration=4, xstrength=2, ystrength=2, vibrato=50, randomness=30, fadeout=false, block=false)]
[curtain(direction = 7,fillfrom = 1,fillto = 0.35, fadetime=3, block=false)]
[curtain(direction = 3,fillfrom = 1,fillto = 0.5, fadetime=3, block=true)]
空间先是震动，而后扭曲、撕裂......
如同被积蓄了千百年的武之一字，硬生生撕裂开来的梦的边界。
[dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[curtain]
[Image(image="70_i14",screenadapt="coverall")]
[ImageTween( xScaleFrom=1.2, yScaleFrom=1.2, xScaleTo=1, yScaleTo=1, duration=30,xTo=0,yTo=0, block=false)]
[delay(time=0.25)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[delay(time=1)]
[name="望"]怎么会是你——
[name="望"]......多事！
[name="重岳"]知道你会这么说。
[name="重岳"]我也答应过，如若真的到了这一步，我会同你一起。
[name="重岳"]更何况，我也想带她见你一面，让你知道，你这些年的筹谋......毕竟没有白费。
隔着梦境与现实的界限，望先是看见重岳怀中的造物......
而后，两人目光相接。
[name="望"]你该离开了......
[name="重岳"]......
[name="重岳"]活下去。
[name="重岳"]......活着回来。
[name="望"]我不会向你保证什么。
二人的距离迅速拉远。
即便是千百岁的武学宗师，人身毕竟仍是人身。
穿透现实与梦境的力量迅速消散，但望的耳边仍然响起他熟悉到厌烦的那个人的声音。
[dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Image]
[Background(image="70_g8_suilingcoreruins",screenadapt="coverall")]
[name="重岳"]那我会去找你。一直找下去。
[name="望"]......随你的便。
[dialog]
[delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[delay(time=1)]
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[charslot(slot="m",name="avg_npc_2129_1#11$1")]
[name="岁"]是他......他究竟做了什么？！
[charslot(slot="m",name="avg_npc_2129_1#4$1")]
[name="岁"]但是无妨，无妨！无论他做了什么，都不过只有一瞬......一瞬！！
[dialog]
[CameraShake(duration=1.5, xstrength=30, ystrength=30, vibrato=50, randomness=50, fadeout=true, block=false)]
[PlaySound(key="$d_avg_hugemonsterroar_long",volume

... (全文8721字符)
```

### level_act49side_11_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Delay(time=1)]
[Background(image="70_g8_suilingcoreruins",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=2)]
[playMusic(key="$m_sys_act14mini_loop", volume=0.6)]
自太古倾泻而下的记忆四散飞溅，冲刷祂庞大却空洞的意识。
残存的神识在梦境之间滑跃，试图找到分毫能凭依的根据......
可那些梦如今都已空泛如未著一字的简牍，徒有颜色与纹理之差，其间本该清晰的人物与事件，却无可捕捉。
[dialog]
[charslot(slot="m",name="avg_npc_2129_1#1$1",duration=1)]
[delay(time=2)]
[name="岁？"]......祂输了。
[charslot(slot="m",name="avg_2027_wang_1#1$1")]
[name="望"]毫无疑问。
[charslot(slot="m",name="avg_npc_2129_1#1$1")]
[name="岁？"]你要占据祂的躯体，替代祂的位置。可你的兄弟姐妹呢？
[charslot(slot="m",name="avg_2027_wang_1#1$1")]
[name="望"]他们不会与我再见，更不会来填补你这空缺。
[charslot(slot="m",name="avg_npc_2129_1#10$1")]
[name="岁？"]那么，我不会消失。我会一直在。
[name="岁？"]无论占据这具躯壳的人究竟是谁，空洞已然形成。既然你无意填补，我便将永远存在于此......
[charslot(slot="m",name="avg_2027_wang_1#1$1")]
[name="望"]......折磨这具躯壳的主人？
[charslot(slot="m",name="avg_npc_2129_1#1$1")]
[name="岁？"]......代行祂的意志，折磨祂的精神，本就一体两面。
[charslot(slot="m",name="avg_2027_wang_1#1$1")]
[name="望"]会有东西填补你的空缺。
[charslot(slot="m",name="avg_npc_2129_1#1$1")]
[name="岁？"]你此刻只剩情感。再充沛的情感，在残缺的意识面前，都谈不上意义。不然，祂的怨恨早已将一切填满。
[charslot(slot="m",name="avg_2027_wang_1#1$1")]
[name="望"]......呵，不必担心。
[charslot(slot="m",name="avg_2027_wang_1#3$1")]
[name="望"]那即将填补你的，比你可怖得多。
[charslot(duration=1)]
将白色的造物甩在身后，代理人迈步上前。
即将在祂自己空空如也的精神中溺毙的巨兽发出沉痛的嘶鸣。
很快，就连那象征痛苦与不甘的嘶鸣也已消逝，整个空间中只回荡着巨兽临终前空旷的回响。
[dialog]
[name="昏乱的意志"]（混沌的残喘）
[charslot(slot="m",name="avg_2027_wang_1#1$1")]
[name="望"]你要死了。
[charslot]
[name="昏乱的意志"]......我要死了？
[name="昏乱的意志"]我是谁？我为什么而死？
[charslot(slot="m",name="avg_2027_wang_1#3$1")]
[name="望"]......你是一个再傲慢不过的梦想者。你在梦中将演化推演至无穷的星海。
[name="望"]但你狂妄的演化被人，被那些你视若无物的人，拦腰截断。
[charslot(slot="m",name="avg_2027_wang_1#1$1")]
[name="望"]而后，你愤怒，你憎恨，你不甘，这些情绪最终置你于死地。
[name="望"]但最后的最后，你死于我之手。
[charslot]
[name="昏乱的意志"]你......！
[name="昏乱的意志"]（混沌的残喘）
[name="昏乱的意志"]你要亲手毁掉......未来？
[name="昏乱的意志"]那逃离毁灭的、无限膨胀的、直至虚无的，演化的未来？
[charslot(slot="m",name="avg_2027_wang_1#1$1")]
[name="望"]那是你永远不可能实现的梦。
[name="望"]演化不会因你的死而停滞，你的死，只是一个痛苦千年的意志的终结和解脱。
[charslot(slot="m",name="avg_2027_wang_1#10$1")]
[name="望"]或者，如果你真的眷恋着那只为你一个而闪烁的星海，只供你一个而灿烂的未来......
[dialog]
[charslot(duration=1)]
[Blocker(a=0.6, r=0, g=0, b=0, fadetime=2, block=true)]
[Sticker(id="st1", multi = true, text="他擎起手中最后一把棋子，那些黑色的棋子逐渐在他手上失却形状，幻化成一柄利器的模样。", x=300,y=300, alignment="left", duration=1.5, size=24, delay=0, width=800,block = false)]
[Sticker(id="st1", multi = true, text="\n\n祂看着他擎起手中最后一把棋子，那些黑色的小石头被他抛上天空，直至无垠的天穹。",block = true, duration=1)]
[Sticker(id="st1", duration=1)]
[delay(time=2)]
[Sticker(id="st1", multi = true, text="他将最后的一点自己凝成的锋锐狠狠刺入祂的眼窝——", x=300,y=300, alignment="left", duration=1.5, size=24, delay=0, width=800,block = false)]
[Sticker(id="st1", multi = true, text="\n\n祂看着那黑色的石头化作的星河距离自己越来越近，越来越近，最终......",block = true, duration=1)]
[Sticker(id="st1", duration=1)]
[delay(time=2)]
[Sticker(id="st1", multi = true, text="岁兽闭上了眼睛。", x=300,y=300, alignment="left", duration=1.5, size=24, delay=0, width=800,block = false)]
[Sticker(id="st1", multi = true, text="\n\n岁兽看见了那只存于梦中的未来。",block = true, duration=1)]
[Sticker(id="st1", duration=2)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[name="望"]......好梦。
[PlaySound(key="$smallearthquake")]
整个空间开始摇动，最终崩毁。
代理人和巨兽的身影逐渐重合在一起，再也无法分开。
一个新的“岁”自此诞生。
[stopmusic(fadetime=2)]
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=3, block=true)]
[charslot]
[delay(time=2)]
[Background(image="bg_desert_1",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[delay(time=1)]
[playMusic(intro="$sjoyasorrow_intro",key="$sjoyasorrow_loop", volume=0.6)]
[charslot(slot="m",name="avgnew_2014_nian_1#3$1",duration=0.5)]
[delay(time=1)]
[name="年"]黍姐，还撑得住吗？
[Dialog]
[charslot]
[charslot(slot="m",name="avg_2025_shu_1#5$1",duration=0.5)]
[delay(time=1)]
[name="黍"]没有大碍。只是一直对付这些小喽啰，未免消耗心力。
[charslot(slot="m",name="avgnew_2014_nian_1#3$1")]
[name="年"]喂，夕！打那边，那边伥聚得多——
[charslot(slot = "m", focus = "n")]
[name="夕"]哪边？
[charslot(slot="m",name="avgnew_2014_nian_1#3$1")]
[name="年"]你看我手指的方向！
[charslot(slot = "m", focus = "n")]
[name="夕"]那里什么都没有！
[charslot(slot="m",name="avgnew_2014_nian_1#8$1")]
[name="年"]瞎说，那里——
[dialog]
[charslot(slot="m",name="avgnew_2014_nian_1#5$1")]
[delay(time=1)]
[charslot(slot = "m", focus = "n")]
年一时语塞。
那里真的已经什么都没有了。
不仅是那里，就像是有谁偷偷从大地上擦去污痕一样，刚刚还横行的伥物，忽然间全部消失无踪。
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="70_g10_wardowntown",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[delay(time=1)]
[charslot(slot = "left", name = "avg_npc_1637_1#1$1",duration = 0.5)]
[charslot(slot = "right", name = "avg_npc_1637_1#1$1",duration = 0.5)]
[delay(time=1)]
[charslot(slot = "left", focus="l")]
[name="疲惫的守军"]收手，你差点砍到我！
[charslot(slot = "left", focus="r")]
[name="焦虑的守军"]我明明要砍它！
[name="焦虑的守军"]......欸？怪物呢？
[dialog]
[charslot]
[PlaySound(key="$d_gen_transmissionget")]
[delay(time=1)]
[charslot(slot="m",name="avg_npc_1634_1#1$1",duration=0.5)]
[delay(time=1)]
[name="禁军"]......
[name="禁军"]收到。
[dialog]
[PlaySound(key="$transmission")]
[delay(time=1)]
[name="禁军"]司岁台急报，字伥已经全数消失。
[charslot]
[charslot(slot = "left", name = "avg_npc_1637_1#1$1", focus="l")]
[charslot(slot = "right", name = "avg_npc_1637_1#1$1", focus="l")]
[name="疲惫的守军"]我们......赢了？
[charslot(slot = "left", focus="r")]
[name="焦虑的守军"]不能放松警惕——
[dialog]
[charslot(slot = "left", focus="all")]
[playsound(key="$d_avg_erthshkng", loop=true, channel="s")]
[CameraShake(duration=-1, xstrength=2, ystrength=2, vibrato=30, randomness=20, fadeout=false, block=false)]
[delay(time=1.5)]
[charslot(slot = "left", focus="r")]
[name="焦虑的守军"]地震？！
[charslot]
[charslot(slot="m",name="avg_npc_1634_1#1$1")]
[name="禁军"]是祂。
[name="禁军"]全体收队，立刻转移到开阔区域！
[stopmusic(fadetime=2)]
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[delay(time=1)]
[CameraShake(durati

... (全文25644字符)
```

### level_act49side_entry

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK",is_video_only=true)] 
[stopmusic]
[Background(image="bg_black",screenadapt="coverall")]
[playMusic(intro="$empty",key="$empty")]
[Video(res="video/act49side/TA01.mp4")]
```

### level_act49side_st01

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[stopmusic]
[dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[PlaySound(key="$d_avg_drtywndblw",volume=0, channel="f", loop=true)]
[SoundVolume(volume=0.3, channel="f",fadetime=1)]
[PlaySound(key="$blizzard",volume=0, channel="ff", loop=true)]
[SoundVolume(volume=0.8, channel="ff",fadetime=1)]
[bgeffect(name="$eb_oldtv",layer=1)]
[image(image="cg_moonmasked",screenadapt="coverall",xScale=1.3, yScale=1.3)]
[ImageTween(image="cg_moonmasked", yFrom=-80, yTo=80, duration=30)]
[Blocker(a=0.2, r=0, g=0, b=0, fadetime=1, block=true)]
[dialog]
[animtext(id = "at1", name = "group_location_stamp", style="avg_only_medium", pos = "-400,-200", block = false)]<p=2>？？？</>
[delay(time=3)]
[animtextclean]
[delay(time=1)]
[Sticker(id="st1", text="“......域外方士有言，北境有大山，名璟。山中有奇石，名娲。\n\n“其方见千丈，高见千丈。形似珠玉，色若琉璃......\n\n“其光昭昭，其焰煌煌，万年不竭......”", x=300,y=260,multi = true, hidelog = false, alignment="left", size=24, delay=0.04, width=700)]
[Sticker(id="st1", duration=1)]
[delay(time=0.5)]
[Sticker(id="st4", text="“可摧金石，可生万物，其道不可知，其理不可察......\n\n\n“若得此神物，或可助大炎渡此劫难。”", x=300,y=260,multi = true, hidelog = false, alignment="left", size=24, delay=0.04, width=700)]
[Sticker(id="st4", duration=1)]
[delay(time=1)]
[StopSound(channel="f", fadetime=2)]
[StopSound(channel="ff", fadetime=2)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[image]
[delay(time=1)]
[Background(image="bg_cave_5",screenadapt="coverall")]
[BackgroundTween(image="bg_cave_5",xScaleFrom=1.2, yScaleFrom=1.2, xScaleTo=1.3, yScaleTo=1.3, yFrom=0, yTo=-50, duration=7)]
[CameraShake(duration=7, xstrength=0, ystrength=5, vibrato=2, randomness=3, fadeout=false, block=false)]
[playsound(key="$d_avg_openftstpwalk", loop=true, channel="bgs",volume=1)]
[Blocker(a=0.2, r=0, g=0, b=0, fadetime=2, block=true)]
[Subtitle(text="“先生，我不明白，我辈为寻此物牺牲惨重，您却准备将其拱手送与炎家？”", x=350, y=170, alignment="center", size=24, delay=0.04, width=1000)]
[Subtitle(text="“那人擅启战端，致使万千生灵涂炭，您又为何要助此失德之君？”", x=400, y=170, alignment="center", size=24, delay=0.04, width=1000)]
[subtitle]
[StopSound(channel="bgs", fadetime=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[delay(time=1)]
[Background(image="bg_cave_4",screenadapt="coverall")]
[BackgroundTween(image="bg_cave_4",xScaleFrom=1.2, yScaleFrom=1.2, xScaleTo=1.3, yScaleTo=1.3, yFrom=50, yTo=0, duration=7)]
[CameraShake(duration=7, xstrength=0, ystrength=5, vibrato=2, randomness=3, fadeout=false, block=false)]
[playsound(key="$d_avg_openftstpwalk", loop=true, channel="bgs",volume=1)]
[Blocker(a=0.2, r=0, g=0, b=0, fadetime=1, block=true)]
[Subtitle(text="“我辈志在解生民之难，非为助一君......天数有时，也不在一人......”",  x=50, y=520, alignment="center",  size=24, delay=0.04, width=1000)]
[Subtitle(text="“只求当下战乱早日停息，百姓不必再受战乱之苦......”", x=170, y=520, alignment="left", size=24, delay=0.04, width=1000)]
[delay(time=1)]
[subtitle]
[StopSound(channel="bgs", fadetime=1)]
[Blocker(a=0.2, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[curtain]
[delay(time=1)]
[name="年长的声音"]啊......是了，是了......！
[name="年长的声音"]这便是......   
[name="年长的声音"]......大炎的“天数”。
[Dialog]
[playMusic(key="$m_sys_act23side_loop", volume=0.6, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[delay(time=1)]
[bgeffect]
[Background(image="bg_rooftop_2",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[animtext(id = "at1", name = "group_location_stamp", style="avg_only_medium", pos = "-400,-200", block = false)]<p=2>1102年 深秋</>
[delay(time=3)]
[animtextclean]
[delay(time=1)]
[PlaySound(key="$d_gen_walk_n", volume=1)]
[charslot(slot = "m", name = "avg_136_hsguma_1#2$1", duration=1.5, isblock=true)]
[name="星熊"]哟，还在值班呢？
[charslot(slot = "m", name = "char_015_lmg",isblock=true)]
[name="执勤的近卫局成员"]鬼姐——不是，熊sir......  
[name="执勤的近卫局成员"]这不是前阵子中秋节，下城区有市民看花灯看上了车道，我们巡逻的人手不够，没拦住人，结果差点出事故。
[name="执勤的近卫局成员"]为这事，局长可是发了好一通火......  
[charslot(slot = "m", name = "avg_136_hsguma_1#11$1",isblock=true)]
[name="星熊"]嘿呦，那是不太应该。  
[charslot(slot = "m", name = "char_015_lmg",isblock=true)]
[name="执勤的近卫局成员"]我们全队都吃处罚，这个月的执勤时间都得加倍。  
[name="执勤的近卫局成员"]她还说最近魏总督不在，我们都得格外小心点。  
[charslot(slot = "m", name = "avg_136_hsguma_1#11$1",isblock=true)]
[name="星熊"]也是，多小心点总没错。  
[name="星熊"]大家伙都辛苦了，正好带了点吃的，大伙分分吧。  
[charslot(slot = "m", name = "char_015_lmg",isblock=true)]
[name="执勤的近卫局成员"]熊sir，这多不好意思......  
[charslot(slot = "m", name = "avg_136_hsguma_1#11$1",isblock=true)]
[name="星熊"]别犟，肚子叫得跟打雷似的，吃点吧。  
[charslot(slot = "m", name = "char_015_lmg",isblock=true)]
[name="执勤的近卫局成员"]欸我不是—— 
[dialog]
[charslot]
[delay(time=0.5)]
[PlaySound(key="$d_gen_thunders_amb", volume=1)]
[delay(time=1)]
[charslot(slot = "m", name = "char_015_lmg",isblock=true)]
[name="执勤的近卫局成员"]好端端的，哪来的雷啊？  
[name="执勤的近卫局成员"]等等，我是眼花了吗？  
[name="执勤的近卫局成员"]那边的天上......是什么东西？  
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[charslot]
[Background(image="25_g09_teahouse",screenadapt="coverall")]
[delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=1)]
[charslot(slot = "m", name = "avg_npc_1629_1#1$1",isblock=true)]
[name="兴奋的游客"]师傅，先不忙着上船，你看那边，好像有什么东西在江上动！  
[name="兴奋的游客"]是循兽？可循兽怎么会在江上，背上还驮着什么......酒盏？  
[dialog]
[charslot]
[Character(name="avg_npc_306_1#1$1", fadetime=1.5, block=true)]
[PlaySound(key="$d_avg_spiritwhoosh", volume=0.6)]
[delay(time=2)]
[charslot(slot = "m", name = "avg_npc_294_1#1$1",isblock=true)]
[name="老船夫"]蜃景罢了，你们勾吴城外说不定也有。有什么好看的。  
[charslot(slot = "m", name = "avg_npc_294_1#6$1",isblock=true)]
[name="老船夫"]（......破。）
[dialog]
[charslot]
[PlaySound(key="$d_avg_magic_2", volume=0.6)]
[Blocker(a=0.8, r=1, g=1, b=1, fadetime=0.3, block=true)]
[bgeffect(name="$eb_rain",layer=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.1, block=true)]
[playsound(key="$d_avg_rainlight_loop", loop=true, channel="bgs",volume=0)]
[SoundVolume(volume=0

... (全文28249字符)
```

### level_act49side_st02

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Delay(time=1)]
[bgeffect(name="$eb_rain_fp",layer=1)]
[gridbg(imagegroup="47_g14_skyovercast_L1/47_g14_skyovercast_R1/47_g14_skyovercast_L2/47_g14_skyovercast_R2", solidwidth="1280/1280/1280/1280", x=-640,y=320,solidheight="720/720/720/720",fadetime=0)]
[CameraEffect(effect="Grayscale", fadetime=0, keep=true, initamount=0, amount=0.7, block=true)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[playsound(key="$d_avg_rainlight_loop", loop=true, channel="bgs")]
[playMusic(intro="$distressed_intro",key="$distressed_loop", volume=0.6)]
[Delay(time=2)]
是的。父亲走时没有通知任何人——不，也许只是没有告诉我。我不知道。
我已经快要记不清了。那时母亲刚刚去世没有多久。
[Dialog]
[bgeffect]
[gridbg(fadetime=2)]
[StopSound(channel="bgs", fadetime=2)]
[Background(image="bg_home",screenadapt="coverall",fadetime=2, block=true)]
[Delay(time=1)]
母亲......她一直不喜欢父亲，也不喜欢我。到了最后，甚至连小塔，她也......
和母亲相比，父亲给我留下的印象真的太稀薄了。我曾经在和魏彦吾对峙的时候说父亲是懦弱的男人，我的看法到现在仍然没变。
但他......的确试图爱我，爱小塔。
[Dialog]
[Background(image="bg_uptown_2",screenadapt="coverall",fadetime=2, block=true)]
[Delay(time=1)]
我小时候很怕魏彦吾来我家找母亲，他就带我出门。后来他借酒浇愁越来越厉害，但他在我面前从没喝过。
小塔起先不喜欢他，他花了很多时间和她在一起，甚至和她一起学他这辈子没听过的维多利亚语。
母亲极烦躁的时候，他会把我们支出去，一个人面对母亲失控的情绪......
[stopmusic(fadetime=2)]
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[delay(time=1)]
[CameraEffect(effect="Grayscale", fadetime=0, amount=0, block=true)]
[Background(image="70_g4_tjdiscussionroom",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[delay(time=1)]
[animtext(id = "at1", name = "group_location_stamp", style="avg_only_heavy", pos = "-400,-200", block = false)]<p=1>1102年 初冬</>
[delay(time=3)]
[animtextclean]
[delay(time=1)]
[playMusic(key="$saferoom_loop", volume=0.6)]
[charslot(slot = "left", name = "avg_npc_2128_1#1$1",duration = 1)]
[charslot(slot = "right", name = "avg_1050_chen3_1#7$1",duration = 1)]
[delay(time=2)]
[charslot(slot = "left", name = "avg_npc_2128_1#1$1",focus="l")]
[name="陈昭芊"]谢谢你，晖洁。我想......已经足够了。
[name="陈昭芊"]其实你父亲他结婚以前，不全是这样的。
[charslot(slot = "right", name = "avg_1050_chen3_1#7$1",focus="r")]
[name="陈"]......我能明白。
[name="陈"]所以，现在需要用这柄书刀，把这份你编纂的家史改掉吗？
[charslot(slot = "left", name = "avg_npc_2128_1#2$1",focus="l")]
[name="陈昭芊"]不，只是个人家史罢了，又没有出版，用不上书刀这么贵重的东西——
[charslot(slot = "m", focus = "n")]
尽管陈昭芊一再推辞，陈仍然把腰间的书刀解下，交到她的手里。
[charslot(slot = "right", name = "avg_1050_chen3_1#1$1",focus="r")]
[name="陈"]颉，还有均，她们都希望这把书刀能去改正那些从粉饰和遗忘中产生的错误。
[name="陈"]即便这错误不关乎天下，只关乎一个已经没落的家族，她们想必也是愿意去订正的。
[charslot(slot = "left", name = "avg_npc_2128_1#3$1",focus="l")]
[name="陈昭芊"]......嗯。
[charslot(slot = "m", focus = "n")]
陈昭芊仿佛在感受重量似的，把书刀放在手里反复掂量，却迟迟没有使用的意思。
[charslot(slot = "left", name = "avg_npc_2128_1#9$1",focus="l")]
[name="陈昭芊"]晖洁，颉她......究竟还会回来吗？
[charslot(slot = "right", name = "avg_1050_chen3_1#7$1",focus="r")]
[name="陈"]说实话，我不知道。
[charslot(slot = "right", name = "avg_1050_chen3_1#4$1",focus="r")]
[name="陈"]从界园里带出来的那个小东西，的确已经把自己舒舒服服地安顿在顶楼那间办公室里了。
[charslot(slot = "right", name = "avg_1050_chen3_1#7$1",focus="r")]
[name="陈"]但你问我，这究竟是不是那个与大炎的历史相伴数百年的颉......我不知道。
[charslot(slot = "left", name = "avg_npc_2128_1#7$1",focus="l")]
[name="陈昭芊"]（几不可闻的叹气声）
[charslot(slot = "left", name = "avg_npc_2128_1#1$1",focus="l")]
[name="陈昭芊"]不知从何时开始，一些前辈把这样一个实在太过可靠，又偏偏好像永生不灭的人，当成了理所当然。
[name="陈昭芊"]所以，她的逝去，让一些像我这样软弱的人失去了主心骨，好像那个全知全能的神明消失了，只剩每个人的一面之词。
[name="陈昭芊"]史家固然要有成一家之言的自信，可当这些自信失却了那个“永远正确无误”的人的背书，就变得容易屈服了。
[charslot(slot = "right", name = "avg_1050_chen3_1#7$1",focus="r")]
[name="陈"]要是这么说，你们应该等到她复活之后，再把她请回来才对。
[charslot(slot = "left", name = "avg_npc_2128_1#1$1",focus="l")]
[name="陈昭芊"]不，恰恰相反，我们应该做的，是走出那个好像永远有正确答案在等待的摇篮，去坦然面对发生错误的可能。
[charslot(slot = "m", focus = "n")]
[PlaySound(key="$d_avg_bookdrop", volume=1)]
陈昭芊用空着的手拿起那本家史，又故意把它丢在桌上。
[charslot(slot = "left", name = "avg_npc_2128_1#2$1",focus="l")]
[name="陈昭芊"]猜猜看，现在这本书着地的是哪一页？
[charslot(slot = "right", name = "avg_1050_chen3_1#4$1",focus="r")]
[name="陈"]看薄厚，三十页左右？
[charslot(slot = "left", name = "avg_npc_2128_1#2$1",focus="l")]
[name="陈昭芊"]我想也差不多，不过......
[charslot(slot = "m", focus = "n")]
她轻轻拈起书本，没去看页码，只是将其重新放好。
[charslot(slot = "left", name = "avg_npc_2128_1#2$1",focus="l")]
[name="陈昭芊"]这下，一个只属于你我的......“历史上的悬案”，就制造出来了。
[charslot(slot = "left", name = "avg_npc_2128_1#3$1",focus="l")]
[name="陈昭芊"]而这世上，因为没人看见，因为太多人看见......这样的悬案，又会有多少呢？
[charslot(slot = "right", name = "avg_1050_chen3_1#10$1",focus="r")]
[name="陈"]很多。
[charslot(slot = "left", name = "avg_npc_2128_1#1$1",focus="l")]
[name="陈昭芊"]是啊，很多很多。
[name="陈昭芊"]而对我来说，我现在最想要得到的，就是明知这世上有不可解的悬案之后，仍然负责任地书写历史的勇气。
[charslot(slot = "left", name = "avg_npc_2128_1#2$1",focus="l")]
[name="陈昭芊"]好了，这柄书刀，还是你来用吧。我翻到要改的页码，你帮我改。
[dialog]
[charslot(slot = "r",  name = "avg_1050_chen3_1#1$1",focus="r")]
[PlaySound(key="$d_avg_scrapebook_quick", volume=0.6)]
[delay(time=1.5)]
[charslot(slot = "left", name = "avg_npc_2128_1#4$1",focus="l")]
[name="陈昭芊"]......竟然真的一点痕迹都没留。
[charslot(slot = "right", name = "avg_1050_chen3_1#1$1",focus="r")]
[name="陈"]如果你正常使用，它真的就只是一把好用到过头了的橡皮擦。
[charslot(slot = "left", name = "avg_npc_2128_1#9$1",focus="l")]
[name="陈昭芊"]橡皮擦......？
[charslot(slot = "left", name = "avg_npc_2128_1#2$1",focus="l")]
[name="陈昭芊"]不得不说，把书刀托付给你，她们的确是找对了人。
[charslot(slot = "right", name = "avg_1050_chen3_1#1$1",focus="r")]
[name="陈"]对了，梁大人还在天镜阁任职吗？他人呢？
[charslot(slot = "left", name = "avg_npc_2128_1#2$1",focus="l")]
[name="陈昭芊"]他？他今天请假了——
[dialog]
[charslot(slot = "m", focus = "n")]
[playsound(key="$d_gen_walk_n",volume=0, loop=true, channel="bgs")]
[SoundVolume(volume=0.8, channel="bgs",fadetime=2)]
[delay(time=2)]
[StopSound(channel="bgs", fadetime=0)]
[charslot(slot = "right", name = "avg_1050_chen3_1#5$1",focus="r")]
[name="陈"]你还约了别人？
[charslot(slot = "left", name = "avg_npc_2128_1#2$1",focus="l")]
[name="陈昭芊"]是宁小姐。
[name="陈昭芊"]哦，提前打声招呼，不是那个宁小姐，是——
[dialog]
[charslot]
[charslot(slot="m",name="avg_4172_xingzh_1#1$1",duration=1.5)]
[delay(time=2)]
[name="宁茵"]昭芊，你好啊。这

... (全文29442字符)
```

### ref_act49side

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 

[Image(image="70_i03_2_a",screenadapt="coverall", fadetime=0)]

[Image(image="70_i16_1_a",screenadapt="coverall", fadetime=0)]

[Image(image="70_i17_a",screenadapt="coverall", fadetime=0)]

[Image(image="70_i19_1_a",screenadapt="coverall", fadetime=0)]

[Image(image="70_i19_2_a",screenadapt="coverall", fadetime=0)]

```


> 本章节共34个脚本文件，此处展示前30个。

## 统计

- 总字符数：651294
- 对话行数：4216


## 策划参考价值
塔防策略RPG的完整剧情脚本格式。含演出指令(BGM/立绘/特效)和对话文本的混合格式。
