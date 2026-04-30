# Freeciv(nation) · zhuang

> 来源：longturn/freeciv21
> 原始链接：https://github.com/longturn/freeciv21/blob/main/data/nation/zhuang.ruleset
> 分类：numerical
> 标签：文明, 4X策略, 规则集, nation

## 概述
Freeciv nation规则集的zhuang定义

## 正文
```ruleset
[nation_zhuang]

name=_("Zhuang")
plural=_("?plural:Zhuang")
groups="Asian", "Ancient"
legend=_("The Zhuang people live in far southwestern China, an\
 ancient border region that has long separated Sinitic civilization from\
 the aboriginal peoples of Southeast Asia. Known for their unique\
 irrigation and scenic terraced rice paddies, they were under pressure from\
 various Chinese dynasties for most of the Ancient era. By the 10th century CE\
 the Zhuang were under harsh rule by the Chinese Song dynasty. After a\
 rebellion in 1052 led by folk-hero Nong Zhigao was crushed, many Zhuang\
 migrated southward forming the basis of the Lao, Thai, and Shan nations.\
 After the Han, the Zhuang are the most populous ethnic group of the\
 People's Republic of China.")

leaders = {
 "name",                "sex"
 "Shi Dakai",           "Male"
 "Li Chi-shen",         "Male"
 "Li Tsung-jen",        "Male"
 "Nong Zhigao",         "Male"
}

flag="zhuang"
flag_alt="-"
style = "Asian"

init_techs=""
init_buildings=""
init_units=""

civilwar_nations="Thai", "Laotian", "Shan"

cities =
; Cities in Guangxi
 "Gveilinz", ; Guilin
 "Namzningz", ; Nanning
 "Liujcouh", ; Liuzhou
 "Ngouzcouh", ; Wuzhou
 "Baekhaij", ; Beihai
 "Fangzcwngzgangj", ; Fangchenggang
 "Ginhcouh", ; Qinzhou
 "Gveigangj", ; Guigang
 "Yoglinz", ; Yulin
 "Baksaek", ; Baise
 "Hohcouh", ; Hezhou
 "Hozciz", ; Hechi
 "Leizbingz", ; Laibin
 "Cungzcoj", ; Chongzuo
 "Bingzsiengz", ; Pingxiang
; Counties in Guangxi
 "Vujmingz", ; Wuming
 "Ningzmingz", ; Ningming
 "Lungzcouh", ; Longzhou
 "Fuzsuih", ; Fusui
 "Dasinh", ; Daxin
 "Denhdwngj" ; Tiandeng

```

## 策划参考价值
4X SLG鼻祖级数值参考：单位/建筑/科技树/文明特性。
