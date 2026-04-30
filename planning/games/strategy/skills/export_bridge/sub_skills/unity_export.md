# SubSkill: Unity配表导出

## 触发条件
用户需要将数值方案导出为Unity可用格式

## 输出格式选项
1. **CSV格式** — 最通用，Excel编辑后可直接导入
2. **JSON格式** — 适合JsonUtility或Newtonsoft.Json
3. **ScriptableObject** — 输出C#类定义 + CreateAssetMenu代码

## 示例输出（C# ScriptableObject）
```csharp
[CreateAssetMenu(fileName = "UnitData", menuName = "GameData/UnitData")]
public class UnitData : ScriptableObject
{
    public string unitId;
    public string unitName;
    public int baseHp;
    public int baseAtk;
    public int baseDef;
    public float atkGrowth;
    public float defGrowth;
    // ...
}
```
