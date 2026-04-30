# Freeciv(experimental) · script

> 来源：longturn/freeciv21
> 原始链接：https://github.com/longturn/freeciv21/blob/main/data/experimental/script.lua
> 分类：numerical
> 标签：文明, 4X策略, 规则集, experimental

## 概述
Freeciv experimental规则集的script定义

## 正文
```lua
-- Copyright (c) 2007-2020 Freeciv21 and Freeciv contributors. This file is
--   part of Freeciv21. Freeciv21 is free software: you can redistribute it
--   and/or modify it under the terms of the GNU General Public License
--   as published by the Free Software Foundation, either version 3
--   of the License,  or (at your option) any later version.
--   You should have received a copy of the GNU General Public License
--   along with Freeciv21. If not, see https://www.gnu.org/licenses/.

-- This file is for lua-functionality that is specific to a given
-- ruleset. When freeciv loads a ruleset, it also loads script
-- file called 'default.lua'. The one loaded if your ruleset
-- does not provide an override is default/default.lua.

-- This is the experimental ruleset. See README.experimental
-- for a detailed description.


-- Place Ruins at the location of the destroyed city.
function city_destroyed_callback(city, loser, destroyer)
  city.tile:create_extra("Ruins", NIL)
  -- continue processing
  return false
end

signal.connect("city_destroyed", "city_destroyed_callback")

```

## 策划参考价值
4X SLG鼻祖级数值参考：单位/建筑/科技树/文明特性。
