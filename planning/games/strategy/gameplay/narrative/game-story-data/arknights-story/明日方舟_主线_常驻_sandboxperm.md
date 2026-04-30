# 明日方舟 · 主线/常驻 · sandboxperm（81段脚本）

> 来源：Kengxxiao/ArknightsGameData
> 原始链接：https://github.com/Kengxxiao/ArknightsGameData
> 分类：gameplay
> 标签：明日方舟, 塔防策略RPG, 主线/常驻, 剧情脚本, 对话, 演出
> 游戏类型：塔防策略RPG

## 概述
明日方舟主线/常驻「sandboxperm」完整剧情脚本（81个文件，174行对话）

## 正文
## 章节信息

- 分类：主线/常驻
- 目录：obt/sandboxperm
- 脚本文件数：81

### dialog_sandbox_1_clking_1_react

```
[header(actId="sandbox_1", npcId="")] 
[name="寻宝人", avatarId="bavg_npc_003", isAvatarRight="FALSE"]谢谢，辛苦你们一路找到这里来救我，我还以为自己差点就要交待在这里了。
[decision(option1="你怎么会在这里？", value1="1.1")]
[predicate(references="1.1")]
[name="寻宝人", avatarId="bavg_npc_003", isAvatarRight="FALSE"]唉......说来话长，几个月前我听说这里埋藏着珍宝，但为此而来的不只有我一人。
[decision(option1="那些杂耍艺人？", value1="2.1")]
[predicate(references="2.1")]
[name="寻宝人", avatarId="bavg_npc_003", isAvatarRight="FALSE"]不，准确来说，他们其实是伙四处流窜的盗贼团。每到一个地方，他们会用表演借机窃取观众身上的财物。
[decision(option1="我们已经和他们交过手了。", value1="3.1")]
[predicate(references="3.1")]
[decision(option1="似乎没有什么可怕的。", value1="4.1")]
[predicate(references="4.1")]
[name="寻宝人", avatarId="bavg_npc_003", isAvatarRight="FALSE"]你们想得太简单了，他们背后有王酋的支持，牢牢掌控着这个晶洞，为的就是阻拦所有前来寻宝的人。
[decision(option1="怎么这里也有他们的事。", value1="5.1")]
[predicate(references="5.1")]
[decision(option1="那些宝藏到底是什么？", value1="6.1")]
[predicate(references="6.1")]
[name="寻宝人", avatarId="bavg_npc_003", isAvatarRight="FALSE"]怪就怪在没人知道。
[name="寻宝人", avatarId="bavg_npc_003", isAvatarRight="FALSE"]糟了......他们回来了......
[name="杂耍艺人", avatarId="bavg_enemy_common", isAvatarRight="FALSE"]想不到你们胆子这么大，竟然跑到我的地盘上来了。
[name="杂耍艺人", avatarId="bavg_enemy_common", isAvatarRight="FALSE"]哼，还想带着这女人离开，没那么容易。来人，把他们都关起来！
[name="杂耍艺人", avatarId="bavg_enemy_common", isAvatarRight="FALSE"]你们就在监牢里待上一辈子，直至枯死在这里吧。
[name="杂耍艺人助手", avatarId="bavg_enemy_common", isAvatarRight="FALSE"]（小声）老板......说不定我们可以......
[name="杂耍艺人助手", avatarId="bavg_enemy_common", isAvatarRight="FALSE"]（小声）兄弟们不能......他们或许......办到。
[name="杂耍艺人", avatarId="bavg_enemy_common", isAvatarRight="FALSE"]你说得有道理。
[name="杂耍艺人", avatarId="bavg_enemy_common", isAvatarRight="FALSE"]那这样吧，你们听好了，如果还想她活着，就去晶洞里取一对伴生晶兽身上的宝石来给我。
[name="杂耍艺人", avatarId="bavg_enemy_common", isAvatarRight="FALSE"]不然的话，她的脑袋就不保了。
[name="寻宝人", avatarId="bavg_npc_003", isAvatarRight="FALSE"]先等等！
[decision(option1="我们答应你！", value1="7.1")]
[predicate(references="7.1")]
[name="寻宝人", avatarId="bavg_npc_003", isAvatarRight="FALSE"]你们......唉，你们根本不知道你们要面对的是什么......
[withdraw(id="trap_435_trsrhuntr")]
[save]
[end]
```

### dialog_sandbox_1_clking_2_ed

```
[header(actId="sandbox_1", npcId="trap_435_trsrhuntr")]
[summontrap(charId="trap_467_ttuye", dir="LEFT", x="11", y="9", isChar="False")]
[summontrap(charId="trap_435_trsrhuntr", dir="RIGHT", x="10", y="11", isChar="False")]
[summonenemy(enemyId="enemy_7024_clking", x="9", y="11", endX="14", endY="6")]
[summonenemy(enemyId="enemy_7025_clbb", x="8", y="11", endX="14", endY="6")]
[camerafocusto(offsetX="10", offsetY="10", time="2", scale="FAR")]
[foginview(leftBottomX="6", leftBottomY="7", rightUpX="14", rightUpY="12", id="fog_1")]
[name="杂耍艺人", avatarId="bavg_enemy_common", isAvatarRight="FALSE"]很好，你们成功获得了那两块宝石，现在把它们交给我，快点！
[decision(option1="得加钱。", value1="1.1")]
[predicate(references="1.1")]
[name="杂耍艺人", avatarId="bavg_enemy_common", isAvatarRight="FALSE"]好啊，这个呢，这个你们要不要？交易所贵客凭证，这够不够？
[additem(itemId="sandbox_1_craft_9", itemCount="1")]
[name="寻宝人", avatarId="bavg_npc_003", isAvatarRight="FALSE"]千万别这么做，他们得到宝石后会将整个晶洞破坏殆尽的！
[decision(option1="宝石你拿去，快点放了她。", value1="2.1")]
[predicate(references="2.1")]
[name="杂耍艺人", avatarId="bavg_enemy_common", isAvatarRight="FALSE"]看这晶莹剔透的模样，等我们献给王酋，他一定会重赏我们，说不定还能封我个官当当。
[name="杂耍艺人助手", avatarId="bavg_enemy_common", isAvatarRight="FALSE"]太好了，老板，我们再也不用过那种四处逃窜的日子了。
[name="图耶", avatarId="char_402_tuye", isAvatarRight="TRUE"]（小声）如果你们不到处祸害别人的话，也不用四处逃窜啊。
[name="杂耍艺人", avatarId="bavg_enemy_common", isAvatarRight="FALSE"]趁我心情好，赶紧带着那女人滚吧，别留在这里碍眼。
[decision(option1="我们走吧。", value1="3.1")]
[predicate(references="3.1")]
[name="寻宝人", avatarId="bavg_npc_003", isAvatarRight="FALSE"]......谢谢你们。
[decision(option1="至少我们救下了你。", value1="4.1")]
[predicate(references="4.1")]
[playanim(id="trap_467_ttuye", anim="Idle", dir="RIGHT")]
[delay(time="0.5")]
[withdraw(id="trap_467_ttuye")]
[withdraw(id="trap_435_trsrhuntr")]
[delay(time="3")]
[camerafocusto(offsetX="9", offsetY="11", time="1", scale="MID")]
[name="杂耍艺人", avatarId="bavg_enemy_common", isAvatarRight="FALSE"]看看它们这美丽的小模样，就像我即将发达的未来一样灿烂。
[name="杂耍艺人助手", avatarId="bavg_enemy_common", isAvatarRight="FALSE"]老板，让我们也瞅瞅。
[playanim(id="enemy_7024_clking", anim="Attack", dir="LEFT", looporidle="Idle")]
[delay(time="1")]
[name="杂耍艺人", avatarId="bavg_enemy_common", isAvatarRight="FALSE"]拿好了，可千万别摔着。
[name="杂耍艺人助手", avatarId="bavg_enemy_common", isAvatarRight="FALSE"]多漂亮啊......
[summontrap(charId="trap_470_tmantic", dir="LEFT", x="10", y="11", isChar="False")]
[executeactionarray(target="trap_470_tmantic", key="effect_mantic[hidden]")]
[delay(time="0.5")]
[name="？？？", avatarId="char_215_mantic", isAvatarRight="FALSE"]（......时机到了......）
[name="？？？", avatarId="char_215_mantic", isAvatarRight="FALSE"]（就是现在！）
[playanim(id="trap_470_tmantic", anim="Attack", dir="LEFT")]
[delay(time="1")]
(宝石碎裂声)
[name="杂耍艺人", avatarId="bavg_enemy_common", isAvatarRight="FALSE"]我的宝石！混账！你怎么敢！！
[name="杂耍艺人", avatarId="bavg_enemy_common", isAvatarRight="FALSE"]不是让你拿好吗！
[name="杂耍艺人助手", avatarId="bavg_enemy_common", isAvatarRight="FALSE"]老板，冤枉啊！
[name="杂耍艺人助手", avatarId="bavg_enemy_common", isAvatarRight="FALSE"]怎、怎么回事，我什么也没干啊，它、它就这么碎在我手心里了......
[name="杂耍艺人", avatarId="bavg_enemy_common", isAvatarRight="FALSE"]不，不！！！
[uioperation(target="main", enable="False")]
[withdraw(id="enemy_7024_clking")]
[withdraw(id="enemy_7025_clbb")]
[delay(time="3")]
[name="？？？", avatarId="char_215_mantic", isAvatarRight="FALSE"]（任务完成。）
[name="？？？", avatarId="char_215_mantic", isAvatarRight="FALSE"]（该离开了......）
[withdraw(id="char_215_mantic")]
[delay(time="3")]
[fognotinview(id="fog_1")]
[resetcamera(time="1")]
[save]
[end]
```

### dialog_sandbox_1_cook_1_op

```
[header(actId="sandbox_1", npcId="trap_468_tpriest")]
[summontrap(x="8", y="7", charId="trap_466_tzumama", isChar="FALSE", dir="LEFT")]
[summontrap(x="7", y="6", charId="trap_468_tpriest", isChar="FALSE", dir="RIGHT")]
[delay(time="1")]
[uioperation(target="main", item="", enable="False")]
[camerafocusto(offsetX="7", offsetY="7", time="1", scale="FAR")]
[playanim(id="trap_466_tzumama", anim="Special_Begin", looporidle="Special_Loop", dir="LEFT")]
[delay(time="1")]
[playanim(id="trap_468_tpriest", anim="Special", dir="RIGHT")]
[name="大祭司", avatarId="bavg_npc_002", isAvatarRight="FALSE"]哇啊啊啊啊——！我的屁股——！
[name="大祭司", avatarId="bavg_npc_002", isAvatarRight="FALSE"]烫死了烫死了——！
[decision(option1="老爷子，你没有事吧？", value1="1.1")]
[predicate(references="1.1")]
[name="森蚺", avatarId="char_416_zumama", isAvatarRight="FALSE"]放心，他没事。
[name="大祭司", avatarId="bavg_npc_002", isAvatarRight="FALSE"]喂，你这不咸不淡的语气怎么回事？我屁股上最好看的那几根羽毛都烧焦了！
[name="森蚺", avatarId="char_416_zumama", isAvatarRight="FALSE"]啊，不是还能长出来吗？
[name="大祭司", avatarId="bavg_npc_002", isAvatarRight="FALSE"]你这丫头真是气死我了，接下来的实验你自己一个人搞吧！别再来找我了！
[withdraw(id="trap_468_tpriest")]
[playanim(id="trap_466_tzumama", anim="Special_End", looporidle="Idle", dir="LEFT")]
[delay(time="1")]
[camerafocusto(id="trap_466_tzumama", scale="CLOSE", time="1")]
[playanim(id="trap_466_tzumama", anim="Attack", dir="LEFT")]
[name="森蚺", avatarId="char_416_zumama", isAvatarRight="FALSE"]唉，这可怎么办？他怎么突然就闹起脾气来了。
[name="森蚺", avatarId="char_416_zumama", isAvatarRight="FALSE"]以前也没遇上过这样的情况啊？
[decision(option1="你要不要赶紧哄哄老爷子。", value1="2.1")]
[predicate(references="2.1")]
[name="森蚺", avatarId="char_416_zumama", isAvatarRight="FALSE"]等我忙完这阵子吧，现在手上的事情实在太多了。
[name="森蚺", avatarId="char_416_zumama", isAvatarRight="FALSE"]你可以先去帮我看看他的情况吗？或许......可以带些吃的？
[decision(option1="听起来也是很麻烦的事......", value1="3.1")]
[predicate(references="3.1")]
[name="森蚺", avatarId="char_416_zumama", isAvatarRight="FALSE"]你看，他还留下了一本《在阿尔萨兰烹饪的一百个小诀窍》的小册子！
[decision(option1="这玩意儿真的有用吗？", value1="4.1")]
[predicate(references="4.1")]
[additem(itemId="sandbox_1_craft_10", itemCount="1")]
[name="森蚺", avatarId="char_416_zumama", isAvatarRight="FALSE"]我们做一道<color=#d8d769>蟹肉碎拌饭</color>吧。
[decision(option1="好主意。", value1="5.1")]
[predicate(references="5.1")]
[withdraw(id="trap_466_tzumama", withoutAnim="TRUE")]
[resetcamera(time="1")]
[save]
[end]
```

### dialog_sandbox_1_cook_2_react

```
[header(actId="sandbox_1", npcId="")] 
[name="大祭司", avatarId="bavg_npc_002", isAvatarRight="FALSE"]是森蚺那丫头让你来找我的吗？
[decision(option1="是的，让我带了<color=#d8d769>蟹肉碎拌饭</color>。", value1="1.1", option2="你先别急......", value2="1.2")]
[predicate(references="1.1", selectableCondition="c0")]
[additem(itemId="sandbox_1_food_1", itemCount="-1")]
[name="大祭司", avatarId="bavg_npc_002", isAvatarRight="FALSE"]要是你带来的食物我不满意，我可不会轻易地原谅她。
[name="大祭司", avatarId="bavg_npc_002", isAvatarRight="FALSE"]让我尝尝......
[name="大祭司", avatarId="bavg_npc_002", isAvatarRight="FALSE"]什么？！那丫头让你用这个打发我？她想得美！
[name="大祭司", avatarId="bavg_npc_002", isAvatarRight="FALSE"]给我费点心思重新弄道别的来！
[withdraw(id="trap_468_tpriest", withoutAnim="FALSE")]
[save]
[end]
[predicate(references="1.2")]
[end]
[condition(references="c0", key="itemGE", itemId="sandbox_1_food_1", value="1")]

```

### dialog_sandbox_1_cook_3_react

```
[header(actId="sandbox_1", npcId="")] 
[name="大祭司", avatarId="bavg_npc_002", isAvatarRight="FALSE"]怎么，森蚺那丫头又让你来找我吗？
[decision(option1="<color=#d8d769>高压复焗浓汤</color>，要尝尝吗？", value1="1.1", option2="没有，只是路过。", value2="1.2")]
[predicate(references="1.1", selectableCondition="c0")]
[additem(itemId="sandbox_1_food_16", itemCount="-1")]
[name="大祭司", avatarId="bavg_npc_002", isAvatarRight="FALSE"]真的？让我尝尝......嗯......
[decision(option1="味道如何？", value1="2.1")]
[predicate(references="2.1")]
[name="大祭司", avatarId="bavg_npc_002", isAvatarRight="FALSE"]这道菜是你做的吗？
[decision(option1="是的。", value1="3.1")]
[predicate(references="3.1")]
[name="大祭司", avatarId="bavg_npc_002", isAvatarRight="FALSE"]一般般吧，我感觉还是不满意。
[decision(option1="可是你连盘子都舔了......", value1="4.1")]
[predicate(references="4.1")]
[name="大祭司", avatarId="bavg_npc_002", isAvatarRight="FALSE"]说了不满意就是不满意，你们这些小年轻怎么回事？！一点都不懂我心思！
[name="大祭司", avatarId="bavg_npc_002", isAvatarRight="FALSE"]重新再给我端一道菜来！
[withdraw(id="trap_468_tpriest", withoutAnim="FALSE")]
[save]
[end]
[predicate(references="1.2")]
[end]
[condition(references="c0", key="itemGE", itemId="sandbox_1_food_16", value="1")]

```

### dialog_sandbox_1_cook_4_react

```
[header(actId="sandbox_1", npcId="")] 
[name="大祭司", avatarId="bavg_npc_002", isAvatarRight="FALSE"]怎么......还不来......这丫头......找我......
[decision(option1="老爷子，你在念叨什么呢？", value1="1.1")]
[predicate(references="1.1")]
[name="大祭司", avatarId="bavg_npc_002", isAvatarRight="FALSE"]啊！你吓死我了，你找我做什么？森蚺让你来的？
[decision(option1="这次是<color=#d8d769>鲜切蟹生</color>。", value1="2.1", option2="没有，只是路过。", value2="2.2")]
[predicate(references="2.1", selectableCondition="c0")]
[additem(itemId="sandbox_1_food_4", itemCount="-1")]
[decision(option1="希望你能喜欢。", value1="3.1")]
[predicate(references="3.1")]
[name="大祭司", avatarId="bavg_npc_002", isAvatarRight="FALSE"]这块肉......它熟了吗？
[decision(option1="我特意保留了一些原味。", value1="4.1")]
[predicate(references="4.1")]
[name="大祭司", avatarId="bavg_npc_002", isAvatarRight="FALSE"]啊......我尝尝......嗯......
[decision(option1="怎么样？", value1="5.1")]
[predicate(references="5.1")]
[name="大祭司", avatarId="bavg_npc_002", isAvatarRight="FALSE"]比上次好点，但我还是不满意。
[decision(option1="你吃的时候都露出笑容了！", value1="6.1")]
[predicate(references="6.1")]
[name="大祭司", avatarId="bavg_npc_002", isAvatarRight="FALSE"]笑就一定代表我觉得好吃吗？
[name="大祭司", avatarId="bavg_npc_002", isAvatarRight="FALSE"]哼，说了不满意就是不满意！没想好之前不要再来打扰我了！
[withdraw(id="trap_468_tpriest", withoutAnim="FALSE")]
[save]
[end]
[predicate(references="2.2")]
[end]
[condition(references="c0", key="itemGE", itemId="sandbox_1_food_4", value="1")]

```

### dialog_sandbox_1_cook_5_react

```
[header(actId="sandbox_1", npcId="")] 
[name="大祭司", avatarId="bavg_npc_002", isAvatarRight="FALSE"]你又端来了什么？
[decision(option1="我保证它足够好吃。", value1="1.1", option2="没有，只是路过。", value2="1.2")]
[predicate(references="1.1", selectableCondition="c0")]
[additem(itemId="sandbox_1_craft_17", itemCount="-1")]
（你提交了“森蚺”牌高压复焗浓汤）
[name="大祭司", avatarId="bavg_npc_002", isAvatarRight="FALSE"]哼，我才不信......
[name="大祭司", avatarId="bavg_npc_002", isAvatarRight="FALSE"]嗯......？
[name="大祭司", avatarId="bavg_npc_002", isAvatarRight="FALSE"]咦......？
[name="大祭司", avatarId="bavg_npc_002", isAvatarRight="FALSE"]嘶......
[decision(option1="你这是什么表情？", value1="2.1")]
[predicate(references="2.1")]
[name="大祭司", avatarId="bavg_npc_002", isAvatarRight="FALSE"]这不是你自己做的吧？和上次不一样哦！
[decision(option1="没错，感谢森蚺小姐。", value1="3.1")]
[predicate(references="3.1")]
[decision(option1="她负责了最关键的步骤。", value1="4.1")]
[predicate(references="4.1")]
[name="大祭司", avatarId="bavg_npc_002", isAvatarRight="FALSE"]嗯......不错，还以为那丫头早把我忘到脑袋后面了。
[decision(option1="所以这道菜你还满意吗？", value1="5.1")]
[predicate(references="5.1")]
[name="大祭司", avatarId="bavg_npc_002", isAvatarRight="FALSE"]我不和你说，让那丫头自己来问我。
[additem(itemId="sandbox_1_condiment", itemCount="3")]
[withdraw(id="trap_468_tpriest", withoutAnim="FALSE")]
[save]
[end]
[predicate(references="1.2")]
[end]
[condition(references="c0", key="itemGE", itemId="sandbox_1_craft_17", value="1")]

```

### dialog_sandbox_1_cook_trademan

```
[header(actId="sandbox_1", npcId="")] 
[name="联络员", avatarId="trap_415_trademan", isAvatarRight="FALSE"]看您最近这苦恼的样子，是碰上了什么烦心事吧？
[name="联络员", avatarId="trap_415_trademan", isAvatarRight="FALSE"]不如讲给我听听，我一定能为您排忧解难。
[decision(option1="什么菜能讨大祭司欢心？", value1="1.1")]
[predicate(references="1.1")]
[name="联络员", avatarId="trap_415_trademan", isAvatarRight="FALSE"]确实，老爷子这几天看起来闷闷不乐......
[decision(option1="你有什么想法吗？", value1="2.1")]
[predicate(references="2.1")]
[name="联络员", avatarId="trap_415_trademan", isAvatarRight="FALSE"]考虑到大祭司在雨林中生活了很多年，说不定他更偏好那些没有过多烹饪，保留食材原汁原味的菜肴。
[name="联络员", avatarId="trap_415_trademan", isAvatarRight="FALSE"]比如说，<color=#d8d769>鲜切蟹生</color>？
[decision(option1="谢谢，我有灵感了！", value1="3.1")]
[predicate(references="3.1")]
[withdraw(id="trap_415_trademan")]
[save]
[end]
```

### dialog_sandbox_1_cook_tuye

```
[header(actId="sandbox_1", npcId="")] 
[name="图耶", avatarId="char_402_tuye", isAvatarRight="FALSE"]看你为大祭司和森蚺闹别扭的事情愁了好几天，或许我能帮帮你。
[name="图耶", avatarId="char_402_tuye", isAvatarRight="FALSE"]我知道一道菜，大祭司吃到它之后一定能心情好转，重新与森蚺小姐和好。
[decision(option1="请告诉我吧。", value1="1.1")]
[predicate(references="1.1")]
[name="图耶", avatarId="char_402_tuye", isAvatarRight="FALSE"]只是制作这道菜的工序非常复杂，需要经过数日的精心烹饪，才能呈现出那种独特的、极富层次感的鲜美味道。
[name="图耶", avatarId="char_402_tuye", isAvatarRight="FALSE"]换句话说，它得花许多心思才能做出来，它的名字叫<color=#d8d769>高压复焗浓汤</color>。
[decision(option1="没关系，这正是我需要的。", value1="2.1")]
[predicate(references="2.1")]
[withdraw(id="trap_467_ttuye")]
[save]
[end]
```

### dialog_sandbox_1_cook_zumama

```
[header(actId="sandbox_1", npcId="")] 
[name="森蚺", avatarId="char_416_zumama", isAvatarRight="FALSE"]终于忙完了，工作了这么多天感觉骨头都要散了。
[decision(option1="森蚺小姐，你快帮帮我！", value1="1.1")]
[predicate(references="1.1")]
[decision(option1="大祭司到底喜欢吃什么啊？", value1="2.1")]
[predicate(references="2.1")]
[name="森蚺", avatarId="char_416_zumama", isAvatarRight="FALSE"]什么，他还在生气吗？
[decision(option1="是的，气得一直掉毛。", value1="3.1")]
[predicate(references="3.1")]
[name="森蚺", avatarId="char_416_zumama", isAvatarRight="FALSE"]让我来吧，我知道怎么做才对他的口味。
[name="森蚺", avatarId="char_416_zumama", isAvatarRight="FALSE"]不过，我得准备一些特殊的调料，你能先做一道<color=#d8d769>高压复焗浓汤</color>吗？
[decision(option1="这菜我倒是做过。", value1="4.1", option2="离开。", value2="4.2")]
[predicate(references="4.1", selectableCondition="c0")]
[additem(itemId="sandbox_1_food_16", itemCount="-1")]
[name="森蚺", avatarId="char_416_zumama", isAvatarRight="FALSE"]谢谢你帮我，到时候你就可以拿到自己想要的了。
[withdraw(id="trap_466_tzumama", withoutAnim="FALSE")]
[save]
[end]
[predicate(references="4.2")]
[end]
[condition(references="c0", key="itemGE", itemId="sandbox_1_food_16", value="1")]

```

### dialog_sandbox_1_cook_zumama2

```
[header(actId="sandbox_1", npcId="")] 
[name="森蚺", avatarId="char_416_zumama", isAvatarRight="FALSE"]（切割食材的声音）（使用炊具的声音）
[name="森蚺", avatarId="char_416_zumama", isAvatarRight="FALSE"]就是这个！
[name="森蚺", avatarId="char_416_zumama", isAvatarRight="FALSE"]只要最后撒上这种粉末，你随便做什么菜大祭司都会满意的。
[decision(option1="真奇妙啊。", value1="1.1")]
[predicate(references="1.1")]
[additem(itemId="sandbox_1_craft_17", itemCount="1")]
[withdraw(id="trap_466_tzumama", withoutAnim="FALSE")]
[save]
[end]

```

### dialog_sandbox_1_guide_trmedic1

```
[header(actId="sandbox_1", npcId="")] 
[name="罗德岛干员", avatarId="char_506_rmedic", isAvatarRight="FALSE"]我回来啦，用上我留下的<color=#d8d769>种植箱集群</color>了吗？多亏了大家的努力，驻扎地开始运作起来了。
[name="罗德岛干员", avatarId="char_506_rmedic", isAvatarRight="FALSE"]继续<color=#d8d769>提升驻扎地等级</color>可以解锁基建配方等更多内容。
[name="罗德岛干员", avatarId="char_506_rmedic", isAvatarRight="FALSE"]这是我从南边带回的物资，希望可以帮到大家。
[decision(option1="谢谢！", value1="1.1")]
[predicate(references="1.1")]
[additem(itemId="sandbox_1_stone", itemCount="5")]
[name="罗德岛干员", avatarId="char_506_rmedic", isAvatarRight="FALSE"]再见，我继续去工作了。
[withdraw(id="trap_473_trmedic")]
[save]
[end]
```

### dialog_sandbox_1_guide_trmedic2

```
[header(actId="sandbox_1", npcId="")] 
[name="罗德岛干员", avatarId="char_506_rmedic", isAvatarRight="FALSE"]一段时间没回来，驻扎地建设得越来越好了。
[name="罗德岛干员", avatarId="char_506_rmedic", isAvatarRight="FALSE"]这是我从更远的地方带回的物资，希望可以帮到大家。
[decision(option1="谢谢！", value1="1.1")]
[predicate(references="1.1")]
[additem(itemId="sandbox_1_tactical_20", itemCount="3")]
[name="罗德岛干员", avatarId="char_506_rmedic", isAvatarRight="FALSE"]再见，我继续去工作了。
[withdraw(id="trap_473_trmedic")]
[save]
[end]
```

### dialog_sandbox_1_guide_trmedic3

```
[header(actId="sandbox_1", npcId="")] 
[name="罗德岛干员", avatarId="char_506_rmedic", isAvatarRight="FALSE"]难得回来一趟，没想到我们的驻扎地现在如此兴盛。
[name="罗德岛干员", avatarId="char_506_rmedic", isAvatarRight="FALSE"]这是我给大家带来的礼物！
[decision(option1="谢谢！", value1="1.1")]
[predicate(references="1.1")]
[additem(itemId="sandbox_1_food_42", itemCount="1")]
[name="罗德岛干员", avatarId="char_506_rmedic", isAvatarRight="FALSE"]我去休息啦！
[withdraw(id="trap_473_trmedic")]
[save]
[end]
```

### dialog_sandbox_1_guide_trmedic4

```
[header(actId="sandbox_1", npcId="")] 
[name="罗德岛工作人员", avatarId="char_506_rmedic", isAvatarRight="FALSE"]前方的路被眼前的<color=#d8d769>机关石门</color>挡住了，我们的法术好像也不奏效了，似乎只有快速攻击能够将它击破。
[decision(option1="交给我们吧", value1="1.1")]
[predicate(references="1.1")]
[withdraw(id="trap_473_trmedic")]
[save]
[end]
```

### dialog_sandbox_1_level_04

```
[header(actId="sandbox_1", npcId="")]
矿洞危险，闲人免进！
[end]
```

### dialog_sandbox_1_level_05

```
[header(actId="sandbox_1", npcId="")]
入洞须知： 
1.入洞请保持礼貌，禁止擅闯陌生区域。
2.矿脉结构有规律，采集时请多加注意。
[end]
```

### dialog_sandbox_1_level_11

```
[header(actId="sandbox_1", npcId="")]
欢迎来到沙岛，（后面的字迹看不清了）
[end]
```

### dialog_sandbox_1_level_17_1

```
[header(actId="sandbox_1", npcId="")]
飞箭难凿穴，刃切了无痕。雨来成碎锦，风起现花纹。
[end]
```

### dialog_sandbox_1_level_17_2

```
[header(actId="sandbox_1", npcId="")]
本矿洞因缺乏照明设备，暂时停止运行，如果有相关设备，可及时联系矿工。
[end]
```

### dialog_sandbox_1_level_20

```
[header(actId="sandbox_1", npcId="")]
警告：大型猛兽出没！注意安全！
[end]
```

### dialog_sandbox_1_level_33

```
[header(actId="sandbox_1", npcId="")]
欢迎来到<color=#d8d769>阿尔萨兰后舍营地</color>。如果您需要帮助，请联系工作人员森蚺小姐，她会竭尽所能提供支持。
此外我们提供临时住所，为您的旅程增添助力~
[decision(option1="该去别处看看了。", value1="1.1")]
[predicate(references="1.1")]
[end]
```

### dialog_sandbox_1_level_60

```
[header(actId="sandbox_1", npcId="")]
前有难关，需全力推动。
[end]
```

### dialog_sandbox_1_main1_1_op

```
[header(actId="sandbox_1", npcId="trap_466_tzumama")]
[summontrap(x="7", y="4", charId="trap_466_tzumama", isChar="FALSE", dir="RIGHT")]
[summontrap(x="9", y="4", charId="trap_467_ttuye", isChar="FALSE", dir="LEFT")]
[camerafocusto(offsetX="8", offsetY="4", time="0.2", scale="MID")]
[uioperation(target="main", item="", enable="False")]
[camerafocusto(id="trap_466_tzumama", scale="CLOSE", time="1")]
[name="森蚺", avatarId="char_416_zumama", isAvatarRight="FALSE"]终于，我们到了这个传说中的“好地方”。
[name="森蚺", avatarId="char_416_zumama", isAvatarRight="FALSE"]考虑到我们核心工作的特殊性，我们在正常的营地外又多收拾了一片空地出来，以后除了招待客人外......
[name="森蚺", avatarId="char_416_zumama", isAvatarRight="FALSE"]物资调配，设备升级，仓库管理也会集中在这里......只要你有需要，之后也随时可以来这里找我。
[camerafocusto(id="trap_467_ttuye", scale="CLOSE", time="1.5")]
[playanim(id="trap_467_ttuye", anim="Special_Begin", looporidle="Special_Loop", dir="LEFT")]
[name="图耶", avatarId="char_402_tuye", isAvatarRight="TRUE"]既然祖玛玛选择了在这里维护营地正常运作，那么探索周围、收集资源的任务就交给我好了。
[name="图耶", avatarId="char_402_tuye", isAvatarRight="TRUE"]房车已经修整完毕，现在能够适用于更加复杂的地形，只要备好燃料，我明天一早就能出发。
[decision(option1="这么快就要启程？", value1="1.1")]
[predicate(references="1.1")]
[camerafocusto(id="trap_466_tzumama", scale="CLOSE", time="1.5")]
[name="森蚺", avatarId="char_416_zumama", isAvatarRight="FALSE"]没有办法，我们路上耽搁了太久，仓库里的储备已经见底了。
[camerafocusto(id="trap_467_ttuye", scale="CLOSE", time="1.5")]
[name="图耶", avatarId="char_402_tuye", isAvatarRight="TRUE"]我之前在营地西侧的拉布-阿拉契什图雨林地带进行了简单的探索，情报称其中有着很多资源。
[name="图耶", avatarId="char_402_tuye", isAvatarRight="TRUE"]此次探索我们会继续深入，看看能不能带回急需的物资。
[camerafocusto(id="trap_466_tzumama", scale="CLOSE", time="1.5")]
[playanim(id="trap_466_tzumama", anim="Attack", dir="RIGHT", looporidle="Idle")]
[delay(time="1")]
[name="森蚺", avatarId="char_416_zumama", isAvatarRight="FALSE"]对了，这张地图给你们。如果想采伐到符合我们建造标准的木头，你们会需要它的。
[name="森蚺", avatarId="char_416_zumama", isAvatarRight="FALSE"]这可是我好不容易搞来的，千万别丢了。
[decision(option1="谢谢。", value1="2.1")]
[predicate(references="2.1")]
[additem(itemId="sandbox_1_craft_1", itemCount="1")]
（你获得了阿尔萨兰林地分布图，现在可以采伐木材了。）
[camerafocusto(id="trap_467_ttuye", offsetX="-1", scale="MID", time="1")]
[decision(option1="今天大家早些休息吧。", value1="3.1")]
[predicate(references="3.1")]
[decision(option1="明天还有很多要忙的。", value1="4.1")]
[predicate(references="4.1")]
[playanim(id="trap_467_ttuye", anim="Special_End", looporidle="Idle", dir="LEFT")]
[delay(time="1")]
[withdraw(id="trap_467_ttuye")]
[withdraw(id="trap_466_tzumama")]
[delay(time="1")]
[resetcamera(time="1")]
[save]
[end]
```

### dialog_sandbox_1_main1_2_op

```
[header(actId="sandbox_1", npcId="trap_415_trademan")]
[foginview(leftBottomX="4", leftBottomY="5", rightUpX="10", rightUpY="8", id="fog_1")]
[summontrap(x="8", y="6", charId="trap_415_trademan", isChar="FALSE", dir="LEFT")]
[summontrap(x="5", y="6", charId="trap_467_ttuye", isChar="FALSE", dir="RIGHT")]
[camerafocusto(offsetX="7", offsetY="6", time="0.2", scale="FAR")]
[uioperation(target="main", item="", enable="False")]
[camerafocusto(id="trap_415_trademan", offsetX="-1", scale="CLOSE", time="1")]
[name="联络员", avatarId="trap_415_trademan", isAvatarRight="TRUE"]想不到在这片雨林中也能见到其他旅行者，各位好啊~
[camerafocusto(id="trap_467_ttuye", offsetX="1", scale="MID", time="1")]
[name="图耶", avatarId="char_402_tuye", isAvatarRight="FALSE"]你是哪位，为什么会出现在这里？
[camerafocusto(id="trap_415_trademan", offsetX="-1", scale="CLOSE", time="1")]
[name="联络员", avatarId="trap_415_trademan", isAvatarRight="TRUE"]请允许我介绍一下自己，我只是太阳谷机械工业的一个小小雇员，不远千里为大家带来我们公司的产品。
[name="联络员", avatarId="trap_415_trademan", isAvatarRight="TRUE"]走过路过，都应该来看一眼，品质优秀价格实惠，更重要的是售后无忧！
[name="联络员", avatarId="trap_415_trademan", isAvatarRight="FALSE"]如果顾客有需要，我们不远万里也会去到他们身边。
[decision(option1="你要不先从泥潭里出来？", value1="1.1")]
[predicate(references="1.1")]
[decision(option1="感觉你正在里面缓缓下沉。", value1="2.1")]
[predicate(references="2.1")]
[name="联络员", avatarId="trap_415_trademan", isAvatarRight="FALSE"]哦，没关系，我自己能想办法出来。只、只是，你们知道哪里有地方可以落脚歇息吗？
[decision(option1="向北走就是我们的营地。", value1="3.1")]
[predicate(references="3.1")]
[decision(option1="只是我们有什么好处？", value1="4.1")]
[predicate(references="4.1")]
[name="联络员", avatarId="trap_415_trademan", isAvatarRight="FALSE"]你们给我行方便我也会给你们行方便，相信我，绝不会让你们吃亏。
[name="联络员", avatarId="trap_415_trademan", isAvatarRight="FALSE"]对了，友情提示，这附近有一座采石场可以弄点石材，你们可以去那里碰碰运气。
[decision(option1="谢谢你，联络员先生。", value1="5.1")]
[predicate(references="5.1")]
[decision(option1="期待我们在营地的会面。", value1="6.1")]
[predicate(references="6.1")]
[withdraw(id="trap_467_ttuye")]
[uioperation(target="main", item="", enable="False")]
[delay(time="3")]
[emoji(target="trap_415_trademan", emoji="common_bubble_happy")]
[delay(time="2")]
[name="联络员", avatarId="trap_415_trademan", isAvatarRight="FALSE"]嘿，终于等到你们了，来自罗德岛的大客户，不枉我在这里守这么多天。
[withdraw(id="trap_415_trademan")]
[fognotinview(id="fog_1")]
[resetcamera(time="1")]
[save]
[end]
```

### dialog_sandbox_1_main1_3_ed

```
[header(actId="sandbox_1", npcId="trap_467_ttuye")]
[summontrap(x="3", y="8", charId="trap_467_ttuye", isChar="FALSE", dir="RIGHT")]
[summonenemy(enemyId="enemy_7001_blwzad_2", x="7", y="8", endX="1", endY="4")]
[move(enemyId="enemy_7001_blwzad_2", x="6", y="8")]
[summonenemy(enemyId="enemy_7001_blwzad", x="7", y="9", endX="1", endY="4")]
[move(enemyId="enemy_7001_blwzad", x="6", y="9")]
[camerafocusto(offsetX="5", offsetY="8", scale="FAR", time="1")]
[foginview(id="rect1", leftBottomX=1, leftBottomY=6, rightUpX=7, rightUpY=11)]
[name="王酋军士兵", avatarId="bavg_enemy_common", isAvatarRight="FALSE"]我警告过你们了，你们根本不知道自己得罪的人是谁！
[decision(option1="天上的星星，地上的王酋。", value1="1.1", option2="你说的是哪颗小星星？", value2="1.2")]
[predicate(references="1.1")]
[name="王酋军士兵", avatarId="bavg_enemy_common", isAvatarRight="FALSE"]......你们会为自己对王酋的冒犯付出代价，我们的军队将踏平你们的家园。
[name="王酋军士兵", avatarId="bavg_enemy_common", isAvatarRight="FALSE"]等着吧，你们将成为我们的奴隶，到我们的采矿场经受劳役之苦。
[withdraw(id="enemy_7001_blwzad_2")]
[withdraw(id="enemy_7001_blwzad")]
[camerafocusto(id="trap_467_ttuye", scale="CLOSE", time="1")]
[name="图耶", avatarId="char_402_tuye", isAvatarRight="FALSE"]采矿场......
[name="图耶", avatarId="char_402_tuye", isAvatarRight="FALSE"]我们得想办法阻止他们，不然他们会把更多的人带去那里。
[decision(option1="我们与他们结下梁子了。", value1="2.1")]
[predicate(references="2.1")]
[decision(option1="将消息送回营地吧。", value1="3.1")]
[predicate(references="3.1")]
[decision(option1="要早做打算。", value1="4.1")]
[predicate(references="4.1")]
[name="图耶", avatarId="char_402_tuye", isAvatarRight="FALSE"]看我在他们丢下的东西里找到了什么？一张通缉令。他们似乎正在追缉一位考古学者。
[decision(option1="考古学者？来这里？", value1="5.1")]
[predicate(references="5.1")]
[decision(option1="难道宝藏的传言是真的？", value1="6.1")]
[predicate(references="6.1")]
[name="图耶", avatarId="char_402_tuye", isAvatarRight="FALSE"]那些士兵为了寻找宝藏，几乎将这里的每一寸土地都翻了个遍。
[name="图耶", avatarId="char_402_tuye", isAvatarRight="FALSE"]宝藏......要想赶走那些王酋军，或许这是个关键。有机会我们得找到这位学者。
[name="图耶", avatarId="char_402_tuye", isAvatarRight="FALSE"]等等，有个好消息，他们还丢下了一张开采石材会用到的导引图，我们可以采掘石材了。
[additem(itemId="sandbox_1_craft_2", itemCount="1")]
（你获得了阿尔萨兰石矿分布图，现在可以采掘石材了。）
[fognotinview(id="rect1")]
[resetcamera(time="1")]
[withdraw(id="trap_467_ttuye")]
[save]
[end]
[predicate(references="1.2")]
[name="王酋军士兵", avatarId="bavg_enemy_common", isAvatarRight="FALSE"]......你们会为自己对王酋的冒犯付出代价，我们的军队将踏平你们的家园。
[name="王酋军士兵", avatarId="bavg_enemy_common", isAvatarRight="FALSE"]等着吧，你们将成为我们的奴隶，到我们的采矿场经受劳役之苦。
[withdraw(id="enemy_7001_blwzad_2")]
[withdraw(id="enemy_7001_blwzad")]
[camerafocusto(id="trap_467_ttuye", scale="MID", time="1")]
[name="图耶", avatarId="char_402_tuye", isAvatarRight="FALSE"]采矿场......
[name="图耶", avatarId="char_402_tuye", isAvatarRight="FALSE"]我们得想办法阻止他们，不然他们会把更多的人带去那里。
[decision(option1="我们与他们结下梁子了。", value1="8.1")]
[predicate(references="8.1")]
[decision(option1="将消息送回营地吧。", value1="9.1")]
[predicate(references="9.1")]
[decision(option1="要早做打算。", value1="10.1")]
[predicate(references="10.1")]
[name="图耶", avatarId="char_402_tuye", isAvatarRight="FALSE"]看我在他们丢下的东西里找到了什么？一张通缉令。他们似乎正在追缉一位考古学者。
[decision(option1="考古学者？来这里？", value1="11.1")]
[predicate(references="11.1")]
[decision(option1="难道宝藏的传言是真的？", value1="12.1")]
[predicate(references="12.1")]
[name="图耶", avatarId="char_402_tuye", isAvatarRight="FALSE"]那些士兵为了寻找宝藏，几乎将这里的每一寸土地都翻了个遍。
[name="图耶", avatarId="char_402_tuye", isAvatarRight="FALSE"]宝藏......要想赶走那些王酋军，或许这是个关键。有机会我们得找到这位学者。
[name="图耶", avatarId="char_402_tuye", isAvatarRight="FALSE"]等等，有个好消息，他们还丢下了一张开采石材会用到的导引图，我们可以采掘石材了。
[additem(itemId="sandbox_1_craft_2", itemCount="1")]
（你获得了阿尔萨兰石矿分布图，现在可以采掘石材了。）
[fognotinview(id="rect1")]
[resetcamera(time="1")]
[withdraw(id="trap_467_ttuye")]
[save]
[end]
```

### dialog_sandbox_1_main1_3_op

```
[header(actId="sandbox_1", npcId="trap_467_ttuye")]
[summontrap(x="6", y="4", charId="trap_467_ttuye", isChar="FALSE", dir="LEFT")]
[summonenemy(enemyId="enemy_7001_blwzad_2", x="2", y="2", endX="12", endY="2")]
[move(enemyId="enemy_7001_blwzad_2", x="3", y="2")]
[summonenemy(enemyId="enemy_7001_blwzad", x="3", y="2", endX="12", endY="2")]
[move(enemyId="enemy_7001_blwzad", x="4", y="2")]
[camerafocusto(offsetX="4", offsetY="3", scale="FAR", time="1")]
[foginview(id="rect1", leftBottomX=1, leftBottomY=1, rightUpX=7, rightUpY=5)]
[name="图耶", avatarId="char_402_tuye", isAvatarRight="FALSE"]看来族长说的不假，甚至这片雨林中也出现了王酋的军队，他们占领了这里的采石场。
[playanim(id="enemy_7001_blwzad", anim="Attack", dir="RIGHT")]
[playanim(id="enemy_7001_blwzad_2", anim="Attack", dir="RIGHT")]
[name="王酋军士兵", avatarId="bavg_enemy_common", isAvatarRight="FALSE"]快点滚开，不要在这里妨碍我们的工作！
[name="王酋军士兵", avatarId="bavg_enemy_common", isAvatarRight="FALSE"]要是再往前走，小心你们的脑袋！
[name="图耶", avatarId="char_402_tuye", isAvatarRight="FALSE"]我们没有恶意，是你们堵在了我们的必经之路上。
[name="图耶", avatarId="char_402_tuye", isAvatarRight="FALSE"]诸位能否放我们通行？
[name="王酋军士兵", avatarId="bavg_enemy_common", isAvatarRight="FALSE"]哼......我可是劝过你们了，既然你们这么死心眼，只能将你们都抓起来充作苦工了。
[name="王酋军士兵", avatarId="bavg_enemy_common", isAvatarRight="FALSE"]谁知道你们来这里到底是什么目的。
[name="王酋军士兵", avatarId="bavg_enemy_common", isAvatarRight="FALSE"]要是来与我们抢夺宝藏的，就更不能留你们了。
[fognotinview(id="rect1")]
[resetcamera(time="1")]
[withdraw(id="enemy_7001_blwzad_2")]
[withdraw(id="enemy_7001_blwzad")]
[withdraw(id="trap_467_ttuye")]
[save]
[end]
```

### dialog_sandbox_1_main1_4_op

```
[header(actId="sandbox_1", npcId="")] 
[summontrap(x="5", y="8", charId="trap_472_tfalco", isChar="FALSE", dir="RIGHT")]
[summontrap(x="8", y="9", charId="trap_467_ttuye", isChar="FALSE", dir="LEFT")]
[camerafocusto(offsetX="7", offsetY="9", time="1", scale="MID")]
[delay(time="0.5")]
[foginview(id="rect1", leftBottomX="1", leftBottomY="7", rightUpX="12", rightUpY="12")]
[name="？？？", avatarId="char_4023_rfalcn", isAvatarRight="FALSE"]......
[decision(option1="女士，你还好吗？", value1="1.1")]
[predicate(references="1.1")]
[decision(option1="（给她一些食物）", value1="2.1", option2="（给她一些清水）", value2="2.2")]
[predicate(references="2.1")]
[name="？？？", avatarId="char_4023_rfalcn", isAvatarRight="FALSE"]谢谢你们，我已经困在这里好几天了，又累又饿。
[decision(option1="该怎么称呼你？", value1="3.1")]
[predicate(references="3.1")]
[name="？？？", avatarId="char_4023_rfalcn", isAvatarRight="FALSE"]我的真名......早就遗失在过去了......叫我的绰号吧，红隼。
[name="红隼", avatarId="char_4023_rfalcn", isAvatarRight="FALSE"]你们快离开吧，我不希望自己的麻烦波及你们。
[name="红隼", avatarId="char_4023_rfalcn", isAvatarRight="FALSE"]我是从南边的采矿场逃出来的，后面有很多人在追我。
[summonenemy(x="4", y="10", endX="9", endY="8", enemyId="enemy_1341_bthtms")]
[camerafocusto(offsetX="6", offsetY="9", time="1", scale="FAR")]
[delay(time="0.5")]
[playanim(charId="trap_472_tfalco", looporidle="Idle", anim="Idle", dir="LEFT")]
[name="采矿场监工", avatarId="bavg_enemy_common", isAvatarRight="FALSE"]追了这么久，总算追到了，哼，我们那么多人折在你这女人手里，今天你别想活着离开这儿。
[name="红隼", avatarId="char_4023_rfalcn", isAvatarRight="FALSE"]哼，采矿场惨死在你们手中的矿工不计其数，我今天即使死在这里，能再拉你们几条命垫背，也很划算了。
[name="图耶", avatarId="char_402_tuye", isAvatarRight="FALSE"]我们要帮帮她吗？
[decision(option1="当然要帮她。", value1="4.1", option2="最重要的是保证她的安全。", value2="4.2")]
[predicate(references="4.1")]
[name="图耶", avatarId="char_402_tuye", isAvatarRight="FALSE"]那就上吧。
[fognotinview(id="rect1")]
[withdraw(id="trap_472_tfalco", withoutAnim="FALSE")]
[withdraw(id="trap_467_ttuye", withoutAnim="FALSE")]
[withdraw(id="enemy_1341_bthtms", withoutAnim="FALSE")]
[delay(time="3")]
[resetcamera(time="1")]
[save]
[end]
[predicate(references="4.2")]
[name="采矿场监工", avatarId="bavg_enemy_common", isAvatarRight="FALSE"]哼，你们帮了这女人，那你们也别想跑。
[fognotinview(id="rect1")]
[withdraw(id="trap_472_tfalco", withoutAnim="FALSE")]
[withdraw(id="enemy_1341_bthtms", withoutAnim="FALSE")]
[withdraw(id="trap_467_ttuye", withoutAnim="FALSE")]
[delay(time="3")]
[resetcamera(time="1")]
[save]
[end]
[predicate(references="2.2")]
[name="？？？", avatarId="char_4023_rfalcn", isAvatarRight="FALSE"]谢谢你们，我已经困在这里好几天了，又累又饿。
[decision(option1="该怎么称呼你？", value1="5.1")]
[predicate(references="5.1")]
[name="？？？", avatarId="char_4023_rfalcn", isAvatarRight="FALSE"]我的真名......早就遗失在过去了......叫我的绰号吧，红隼。
[name="红隼", avatarId="char_4023_rfalcn", isAvatarRight="FALSE"]你们快离开吧，我不希望自己的麻烦波及你们。
[name="红隼", avatarId="char_4023_rfalcn", isAvatarRight="FALSE"]我是从南边的采矿场逃出来的，后面有很多人在追我。
[summonenemy(x="4", y="10", endX="9", endY="8", enemyId="enemy_1341_bthtms")]
[camerafocusto(offsetX="6", offsetY="9", time="1", scale="FAR")]
[delay(time="0.5")]
[playanim(charId="trap_472_tfalco", looporidle="Idle", anim="Idle", dir="LEFT")]
[name="采矿场监工", avatarId="bavg_enemy_common", isAvatarRight="FALSE"]追了这么久，总算追到了，哼，我们那么多人折在你这女人手里，今天你别想活着离开这儿。
[name="红隼", avatarId="char_4023_rfalcn", isAvatarRight="FALSE"]哼，采矿场惨死在你们手中的矿工不计其数，我今天即使死在这里，能再拉你们几条命垫背，也很划算了。
[name="图耶", avatarId="char_402_tuye", offsetX="1", isAvatarRight="FALSE"]我们要帮帮她吗？
[decision(option1="当然要帮她。", value1="6.1", option2="最重要的是保证她的安全。", value2="6.2")]
[predicate(references="6.1")]
[name="图耶", avatarId="char_402_tuye", isAvatarRight="FALSE"]那就上吧。
[fognotinview(id="rect1")]
[withdraw(id="trap_472_tfalco", withoutAnim="FALSE")]
[withdraw(id="trap_467_ttuye", withoutAnim="FALSE")]
[withdraw(id="enemy_1341_bthtms", withoutAnim="FALSE")]
[delay(time="3")]
[resetcamera(time="1")]
[save]
[end]
[predicate(references="6.2")]
[name="采矿场监工", avatarId="bavg_enemy_common", isAvatarRight="FALSE"]哼，你们帮了这女人，那你们也别想跑。
[fognotinview(id="rect1")]
[withdraw(id="trap_472_tfalco", withoutAnim="FALSE")]
[withdraw(id="trap_467_ttuye", withoutAnim="FALSE")]
[withdraw(id="enemy_1341_bthtms", withoutAnim="FALSE")]
[delay(time="3")]
[resetcamera(time="1")]
[save]
[end]

```

### dialog_sandbox_1_main1_4_react

```
[header(actId="sandbox_1")]
[name="红隼", avatarId="char_4023_rfalcn", isAvatarRight="FALSE"]谢谢你们的帮助，他们的追杀看来是到此为止了。
[decision(option1="如果你不知道去哪里......", value1="1.1")]
[predicate(references="1.1")]
[decision(option1="可以来我们的营地。", value1="2.1")]
[predicate(references="2.1")]
[name="红隼", avatarId="char_4023_rfalcn", isAvatarRight="FALSE"]不，我得回到南边的采矿场，那里还有很多苦工忍受着折磨和劳役，我要回去救他们。
[decision(option1="这不是理智的决定。", value1="3.1", option2="你可能会送命。", value2="3.2")]
[predicate(references="3.1")]
[name="红隼", avatarId="char_4023_rfalcn", isAvatarRight="FALSE"]我是奴隶也是战士，我的生命早已不属于自己。如果我还活着，一定会来报答你们的帮助。
[name="图耶", avatarId="char_402_tuye", isAvatarRight="FALSE"]我们要不帮帮她？反正我们已经和王酋军起冲突了。
[withdraw(id="trap_472_tfalco")]
[decision(option1="她走得太快了，先跟上吧。", value1="4.1")]
[predicate(references="4.1")]
[additem(itemId="sandbox_1_craft_15", itemCount="1")]
[save]
[end]
[predicate(references="3.2")]
[name="红隼", avatarId="char_4023_rfalcn", isAvatarRight="FALSE"]我是奴隶也是战士，我的生命早已不属于自己。如果我还活着，一定会来报答你们的帮助。
[name="图耶", avatarId="char_402_tuye", isAvatarRight="FALSE"]我们要不帮帮她？反正我们已经和王酋军起冲突了。
[withdraw(id="trap_472_tfalco")]
[decision(option1="她走得太快了，先跟上吧。", value1="5.1")]
[predicate(references="5.1")]
[additem(itemId="sandbox_1_craft_15", itemCount="1")]
[save]
[end]
```

### dialog_sandbox_1_main1_5_react

```
[header(actId="sandbox_1", npcId="")] 
[name="森蚺", avatarId="char_416_zumama", isAvatarRight="FALSE"]我们刚刚收到了一条来自侦察人员发出的紧急消息。
[name="森蚺", avatarId="char_416_zumama", isAvatarRight="FALSE"]还记得那伙你们在雨林中遇到的王酋军吗？他们快要找上门来了。
[decision(option1="不要轻举妄动。", value1="1.1", option2="<color=#d8d769>好的，我们马上赶回去。</color>", value2="1.2")]
[predicate(references="1.1")]
[end]
[predicate(references="1.2")]
[withdraw(id="trap_466_tzumama")]
[save]
[end]
```


> 本章节共81个脚本文件，此处展示前30个。

## 统计

- 总字符数：33907
- 对话行数：174


## 策划参考价值
塔防策略RPG的完整剧情脚本格式。含演出指令(BGM/立绘/特效)和对话文本的混合格式。
