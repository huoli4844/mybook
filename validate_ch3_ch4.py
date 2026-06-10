#!/usr/bin/env python3
"""Validate Ch3 and Ch4 after Ke Jinliang additions."""
import re

files = {
    "output/第3章-电磁骚扰源.md": [
        # Ke Jinliang additions to check
        "柯金良六类频谱分类法",
        "百分比带宽",
        "波段比值",
        "中频带",
        "超宽带",
        "雷电的二次效应",
        "LPZ_{0A}",
        "一次效应",
        "公共场所的电磁骚扰源",
        "室内电源线上的瞬态电压",
        "17.5次",
        "高能电磁骚扰（HPEM）分类",
        "核电磁脉冲弹",
        "功率密度峰值",
        "等值频率",
        "三无世界",
        "骚扰源的数学建模",
        "双指数模型",
        "振铃波模型",
        "传输线模型",
        "I(t) = A I_{\\mathrm{P}} t^3",
        "1.25 MHz振铃波",
        "\\tag{3-5}",
        "\\tag{3-10}",
        "3.6.4 传输线模型",
    ],
    "output/第4章-电磁耦合途径.md": [
        # Ke Jinliang additions
        "何金良《电磁兼容概论》的偶极子辐射场分量",
        "电偶极子的完整场分量",
        "磁偶极子的完整场分量",
        "近区场简化",
        "远区场简化",
        "场区划分表",
        "何金良在《电磁兼容概论》中给出了不同频率下近场与远场分界距离",
        "λ/(2π)",
        "954.9 km",
        "4.77 cm",
        "耦合的传递函数分析方法",
        "T网络模型",
        "S参数与传递函数",
        "矢量匹配法",
        "\\tag{4-30a}",
        "\\tag{4-30c}",
        "设备的电磁骚扰耦合途径分析",
        "设备的端口耦合分类",
        "外壳端口",
        "系统级耦合途径",
        "差模耦合与共模耦合",
        "耦合途径诊断流程",
    ],
}

all_ok = True
for fname, keywords in files.items():
    path = f"/Users/huoli4844/Desktop/电磁兼容教材/{fname}"
    try:
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()
    except FileNotFoundError:
        print(f"❌ FILE NOT FOUND: {fname}")
        all_ok = False
        continue
    
    missing = [kw for kw in keywords if kw not in content]
    if missing:
        print(f"⚠️  {fname}: {len(missing)} missing items:")
        for m in missing:
            print(f"   - {m}")
        all_ok = False
    else:
        print(f"✅ {fname}: All {len(keywords)} keywords found!")

    # Check for equation numbering consistency
    tags = re.findall(r'\\tag\{([^}]+)\}', content)
    if len(tags) != len(set(tags)):
        dupes = [t for t in tags if tags.count(t) > 1]
        print(f"   ⚠️ Duplicate equation tags: {set(dupes)}")

if all_ok:
    print("\n✅ ALL CHECKS PASSED!")
else:
    print(f"\n❌ Some checks failed. Review above.")
