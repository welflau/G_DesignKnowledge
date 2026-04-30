# Freeciv(nation) · mongol

> 来源：longturn/freeciv21
> 原始链接：https://github.com/longturn/freeciv21/blob/main/data/nation/mongol.ruleset
> 分类：numerical
> 标签：文明, 4X策略, 规则集, nation

## 概述
Freeciv nation规则集的mongol定义

## 正文
```ruleset
[nation_mongol]

translation_domain="freeciv"

name=_("Mongol")
plural=_("?plural:Mongols")
groups="Medieval", "Early Modern", "Modern", "Asian", "Core"
legend=_("In the centuries after their unification by Chinggis Khan, the\
 Mongols conquered the largest empire in human history, encompassing most\
 of the continent of Asia. They became notorious for their utter\
 ruthlessness in warfare.")

leaders = {
 "name",        "sex"
 "Chinggis",	"Male" ; Genghis / Чингис
 "Börte",       "Female" ; Bortei / Бөртэ
 "Ögedei",	"Male" ; Өгэдэй
 "Bat",		"Male" ; Batu / Бат
 "Tsagadai",	"Male" ; Chagatai / Цагадай
 "Tolui",	"Male" ; Толуй
 "Tokhtamysh",	"Male" ; Тохтамыш
 "Sübeedei",	"Male" ; Subutai / Сүбээдэй
 "Dörgene",	"Female" ; Toregene / Дөргэнэ
 "Güyük", 	"Male" ; Гүюг
 "Mönkh", 	"Male" ; Mongke / Мөнх
 "Khubilai",	"Male" ; Kublai / Хубилай
 "Khülegü",	"Male" ; Hulagu / Хүлэгү
 "Mandukhai",   "Female" ; Мандухай
}

ruler_titles = {
 "government",      "male_title",      "female_title"
 "Despotism",       _("%s Khan"),      _("%s Khatan")
 "Monarchy",        _("%s Khagan"),    _("?female:%s Khagan")
}

flag="mongolia"
flag_alt = "-"
style = "Asian"

init_techs=""
init_buildings=""
init_units=""

civilwar_nations="Tibetan", "Tuvan", "Kalmyk", "Timurid", "Uyghur", "Tatar",
 "Crimean Tatar", "Buryat", "Golden Horde"

cities=
 "Karakorum", ; Каракорум
 "Ulaanbaatar", ; Улаанбаатар
 "Sainshand", ; Сайншанд
 "Ulaangom", ; Улаангом
 "Khovd", ; Ховд
 "Tsetserleg", ; Цэцэрлэг
 "Altanbulag", ; Алтанбулаг
 "Zuunmod", ; Зуунмод
 "Bayankhongor", ; Баянхонгор
 "Dalanzadgad", ; Даланзадгад
 "Choibalsan", ; Чойбалсан
 "Erdenet", ; Эрдэнэт
 "Mandalgovi", ; Мандалговь
 "Mörön", ; Мөрөн
 "Sükhbaatar", ; Сүхбаатар
 "Züünkharaa", ; Зүүнхараа
 "Öndörkhaan", ; Өндөрхаан
 "Ölgii", ; Өлгий
 "Arvaikheer", ; Арвайхээр
 "Bulgan", ; Булган
 "Altai", ; Алтай
 "Baruun-Urt", ; Баруун-Урт
 "Choir", ; Чойр
 "Darkhan", ; Дархан
 "Bayan-Uul", ; Баян-Уул
 "Nalaikh", ; Налайх
 "Zamyn-Üüd", ; Замын-Үүд
 "Khatgal", ; Хатгал
 "Uliastai", ; Улиастай
 "Khuld" ; Хулд

```

## 策划参考价值
4X SLG鼻祖级数值参考：单位/建筑/科技树/文明特性。
