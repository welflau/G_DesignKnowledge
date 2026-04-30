# Freeciv(nation) · taiwanese

> 来源：longturn/freeciv21
> 原始链接：https://github.com/longturn/freeciv21/blob/main/data/nation/taiwanese.ruleset
> 分类：numerical
> 标签：文明, 4X策略, 规则集, nation

## 概述
Freeciv nation规则集的taiwanese定义

## 正文
```ruleset
[nation_taiwanese]

name=_("Taiwanese")
plural=_("?plural:Taiwanese")
groups="Modern", "Asian"
legend=_("The Republic of China was established in 1912 as the successor\
 state of the Qing Empire, ending over two millennia of imperial rule in\
 China. When the Chinese Nationalists who ruled the Republic lost a\
 civil war against the Chinese Communists in 1949, the Nationalist\
 government evacuated to the island of Taiwan, establishing Taipei as the\
 provisional capital of the Republic of China.")

leaders = {
 "name",                "sex"
 "Sun Yat Sen",         "Male"
 "Yuan Shikai",         "Male"
 "Soong Ching Ling",    "Female"
 "Chiang Kai Shek",     "Male"
 "Chiang Ching Kuo",    "Male"
}

ruler_titles = {
 "government",      "male_title",      "female_title"
 "Monarchy",        _("Emperor %s"),      _("Empress Dowager %s")
 "Communism",       _("Chairman %s"),     _("Chairwoman %s")
}

flag="taiwan"
flag_alt = "-"
style = "Asian"

init_techs=""
init_buildings=""
init_units=""
civilwar_nations="chinese", "formosan"

; These names used to be spelled differently (Taipeh instead of Taipei).
; The new names are better but may not be canonical.
; These are the top 50 names taken from
; "http://www.world-gazetteer.com/c/c_tw.htm".
cities =
  "Taipei", "Kaohsiung", "Taichung", "Tainan", "Panchiao", "Chungho",
  "Sanchung", "Keelung", "Hsinchu", "Hsinchuang", "Fengshan", "Chungli",
  "Chiayi", "Hsintien", "Yungho", "Changhwa", "Tucheng", "Pingtung",
  "Yungkang", "Pingchen", "Tali", "Fengyuan", "Pate", "Luchou", "Hsichih",
  "Shulin", "Yuanlin", "Yangmei", "Taitung", "Hualian", "Tanshui", "Nantou",
  "Touliu", "Tsaotun", "Kangshan", "Ilan", "Miaoli", "Toufen", "Chutung",
  "Chupei", "Chingshui", "Homei", "Tachi", "Lukang", "Sanhsia", "Tachia",
  "Yingko", "Hsinying"

```

## 策划参考价值
4X SLG鼻祖级数值参考：单位/建筑/科技树/文明特性。
