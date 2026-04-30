# Freeciv(nation) · manchu

> 来源：longturn/freeciv21
> 原始链接：https://github.com/longturn/freeciv21/blob/main/data/nation/manchu.ruleset
> 分类：numerical
> 标签：文明, 4X策略, 规则集, nation

## 概述
Freeciv nation规则集的manchu定义

## 正文
```ruleset
[nation_manchu]

name=_("Manchu")
plural=_("?plural:Manchus")
groups="Medieval", "Asian", "Early Modern"
legend=_("The Manchus were a semi-nomadic people originating from the region\
 called Manchuria in Northeast Asia. In the 17th century they conquered and\
 ruled China as the Manchu Empire until 1911.")

leaders = {
 "name",                "sex"
 "Puyi",                "Male"
 "Cixi",                "Female"
 "Abkai Wehiyehe",      "Male" ; Qianlong Emperor
 "Hiowan Yei",          "Male" ; Kangxi Emperor
 "Hongtaiji",           "Male"
 "Nurhaci",             "Male"
 "Giocangga",           "Male"
 "Wanyan Wulu",         "Male"
 "Wanyan Aguda",        "Male"
 "Hanpu",               "Male"
}

ruler_titles = {
 "government",      "male_title",      "female_title"
 "Monarchy",        _("Emperor %s"),   _("Empress Dowager %s")
}

flag="manchuria"
flag_alt = "-"
style = "Asian"

init_techs=""
init_buildings=""
init_units=""
civilwar_nations = "mongol", "korean", "chinese"

cities =
 "Mukden",		; Shenyang
 "Harbin",
 "Cicigar",		; Qiqihar
 "Aihun",		; Aigun
 "Giyamusi",		; Jiamusi
 "Ninguta",		; Ning`an
 "Ishangga Gashan",	; Yingkou
 "Mudan Bira (river)",	; Mudanjiang
 "Alchuka",		; Acheng
 "Sahaliyan Ula (river)",; Heihe
 "Girin",		; Jilin
 "Huncun",		; Hunchun
 "Abkai Imiyangga",	; Fengtianfu
 "Non Ula (river)",	; Nenjiang
 "Imiyangga Jase",	; Zhangjiakou
 "Hulun",		; Hailar
 "Gioro",
 "Erdemu Be Aliha",	; Chengde
 "Tumen Ula (river)",
 "Kiyaktu",		; Kyakhta
 "Nibcu",		; Nerchinsk
 "Usuri Ula (river)",	; Ussuri
 "Yalu Ula (river)",
 "Nibcu Bira (river)",	; Nercha
 "Sunggari Ula (river)",; Songhua
 "Ilan Boo"		; Sanjiazi

```

## 策划参考价值
4X SLG鼻祖级数值参考：单位/建筑/科技树/文明特性。
