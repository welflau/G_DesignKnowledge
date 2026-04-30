# Freeciv(nation) · yakut

> 来源：longturn/freeciv21
> 原始链接：https://github.com/longturn/freeciv21/blob/main/data/nation/yakut.ruleset
> 分类：numerical
> 标签：文明, 4X策略, 规则集, nation

## 概述
Freeciv nation规则集的yakut定义

## 正文
```ruleset
[nation_yakut]

name=_("Yakut")
plural=_("?plural:Yakuts")
groups="Asian", "Early Modern"
legend=_("Oral tradition indicates that the Yakuts - or Sakha as they call\
 themselves - migrated north from the Central Asian steppes to the shores\
 of Lake Baikal in the 10th century CE. They intermarried with the native\
 population and established a nation along the Lena river, having\
 diplomatic relations with at least the Chinese, the Mongols, and the\
 various Turkic peoples of the region. By the 1620s, Cossacks had arrived\
 in Yakut territory as agents of an expansionist Russia, eventually\
 subduing the Yakut kings and securing Russian hegemony over Yakutia.\
 Numbering about a million today,\
 the Yakuts make up roughly half of the population of the vast Sakha\
 Republic of Russia's Far Eastern district.")

; Latinized Sakha - Russian-based English name - Cyrillic Sakha
leaders = {
 "name",                "sex"
 "Platon Ojuunuskaj",   "Male" ; Platon Oyunsky / Платон Ойуунускай
 "Sèmèn Noghoruodap",   "Male" ; Semyon Novgorodov / Сэмэн Ноҕоруодап
 "Tygyn Darxan",        "Male" ; Tygyn Darkhan / Тыгын Дархан
 "Manchaary",           "Male" ; Manchari / Манчаары
 "Tuyaara",             "Female" ; Туйаара
 "Kùnnèy",              "Female" ; Күннэй
}
ruler_titles = {
 "government",      "male_title",            "female_title"
 "Fundamentalism",  _("Shaman %s"),          _("?female:Shaman %s")
}
flag="sakha"
flag_alt = "-"
style = "European"

init_techs=""
init_buildings=""
init_units=""

conflicts_with="Russian"
civilwar_nations="Siberian", "Tuvan"

cities =
; Latinized Sakha - Russian-based English name - Cyrillic Sakha
 "D'okuuskaj", ; Yakutsk / Дьокуускай
 "Nùôrùnggùrù", ; Neryungri / Нүөрүҥгүрү
 "Mirnèj", ; Mirny / Мирнэй
 "Aldan", ; Алда́н
 "Muxtuja", ; Lensk / Мухтуйа
 "Udachnaj", ; Udachny / Удачнай
 "Chul'man", ; Chulman / Чульман
 "N'urba", ; Nyurba / Ньурба
 "Pokrovskaj", ; Pokrovsk / Покровскай
 "Ôlùôxùmè", ; Olyokminsk / Өлүөхүмэ
 "Bùlùù", ; Vilyuysk / Бүлүү
 "Uus N'ara", ; Ust-Nera / Уус Ньара
 "Zhataj", ; Zhatay / Жатай
 "Tommot", ;  Томмот
 "Xaandyga", ; Khandyga / Хаандыга
 "Allaraa Kuraanax", ; Nizhny Kuranakh / Аллараа Кураанах
 "Tiksii", ; Tiksi / Тиксии
 "Serebrjanyj Bor", ; Serebryany Bor / Серебряный Бор
 "Berkakit", ; Беркакит
 "Baataghaj", ; Batagay / Баатаҕай
 "Vitim", ; Витим
 "Cherskèj", ; Chersky / Черскэй
 "Orto Xalyma", ; Srednekolymsk / Орто Халыма
 "Uus Maaja", ; Ust-Maya/ Уус Маайа
 "Allaraa Bèstèèx", ; Nizhny Bestyakh / Аллараа Бэстээх
 "Chokuurdaax", ; Chokurdakh / Чокуурдаах
 "Èld'ikèèn", ; Eldikan / Элдьикээн
 "Uus Kujga", ; Ust-Kuyga / Уус Куйга
 "Ùôhèè D'aangi", ; Verkhoyansk / Үөһээ Дьааҥы
 "Nizhnejanskaj", ; Nizhneyansk / Нижнеянскай
 "Ôymôkôôn" ; Oymyakon / Өjмөкөөн

```

## 策划参考价值
4X SLG鼻祖级数值参考：单位/建筑/科技树/文明特性。
