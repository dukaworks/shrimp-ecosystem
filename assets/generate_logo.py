#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
🦞 虾族生态 Logo 生成器
生成 SVG 和 PNG 格式的 Logo
"""

import svgwrite
from svgwrite import cm, mm
import os

def create_shrimp_logo(output_dir="./assets"):
    """创建小龙虾 Logo"""
    
    os.makedirs(output_dir, exist_ok=True)
    
    # SVG 文件路径
    svg_path = os.path.join(output_dir, "shrimp-logo.svg")
    
    # 创建 SVG 画布
    dwg = svgwrite.Drawing(svg_path, size=(400, 400), profile='tiny')
    
    # 定义颜色
    colors = {
        'body': '#FF6B9D',      # 粉红色
        'body_dark': '#E85A8A', # 深粉色
        'shell': '#FF8FB3',     # 浅粉色
        'eye': '#2C3E50',       # 深色眼睛
        'eye_white': '#FFFFFF', # 眼白
        'claw': '#FF1744',      # 红色螯
        'accent': '#4ECDC4',    # 青色点缀
    }
    
    # 背景圆
    dwg.add(dwg.circle(
        center=(200, 200),
        r=180,
        fill='#FFF5F7',
        stroke='#FFE4EC',
        stroke_width=2
    ))
    
    # 虾身体（弯曲的形状）
    # 身体主体 - 使用路径绘制弯曲的虾身
    body_path = dwg.path(
        d="M 120 280 "  # 起始点（尾部）
        "Q 80 200 140 140 "  # 控制点1，中间点
        "Q 200 80 260 120 "  # 控制点2，头部位置
        "Q 300 150 280 200 "  # 头部弯曲
        "Q 260 250 200 240 "  # 回到身体
        "Q 160 230 140 280 "  # 尾部弯曲
        "Z",
        fill=colors['body'],
        stroke=colors['body_dark'],
        stroke_width=3
    )
    dwg.add(body_path)
    
    # 虾壳纹理（几节）
    shell_lines = [
        ("M 140 140 Q 170 130 200 145", colors['shell']),
        ("M 160 170 Q 190 160 220 175", colors['shell']),
        ("M 180 200 Q 210 190 240 205", colors['shell']),
    ]
    for d, color in shell_lines:
        dwg.add(dwg.path(d=d, fill='none', stroke=color, stroke_width=4, stroke_linecap='round'))
    
    # 大虾螯（左边）
    left_claw = dwg.path(
        d="M 140 140 "
        "Q 100 100 80 130 "
        "Q 70 150 90 160 "
        "Q 110 170 130 150",
        fill=colors['claw'],
        stroke='#D50000',
        stroke_width=2
    )
    dwg.add(left_claw)
    
    # 大虾螯（右边）
    right_claw = dwg.path(
        d="M 260 120 "
        "Q 300 80 320 110 "
        "Q 330 130 310 140 "
        "Q 290 150 270 130",
        fill=colors['claw'],
        stroke='#D50000',
        stroke_width=2
    )
    dwg.add(right_claw)
    
    # 眼睛（左眼）
    dwg.add(dwg.circle(center=(170, 115), r=12, fill=colors['eye_white'], stroke=colors['eye'], stroke_width=2))
    dwg.add(dwg.circle(center=(172, 115), r=6, fill=colors['eye']))
    dwg.add(dwg.circle(center=(174, 113), r=2, fill='white'))  # 高光
    
    # 眼睛（右眼）
    dwg.add(dwg.circle(center=(210, 115), r=12, fill=colors['eye_white'], stroke=colors['eye'], stroke_width=2))
    dwg.add(dwg.circle(center=(212, 115), r=6, fill=colors['eye']))
    dwg.add(dwg.circle(center=(214, 113), r=2, fill='white'))  # 高光
    
    # 触角
    dwg.add(dwg.path(
        d="M 170 100 Q 160 60 140 50",
        fill='none',
        stroke=colors['body_dark'],
        stroke_width=2,
        stroke_linecap='round'
    ))
    dwg.add(dwg.path(
        d="M 210 100 Q 220 60 240 50",
        fill='none',
        stroke=colors['body_dark'],
        stroke_width=2,
        stroke_linecap='round'
    ))
    
    # 微笑
    dwg.add(dwg.path(
        d="M 175 135 Q 190 145 205 135",
        fill='none',
        stroke=colors['eye'],
        stroke_width=2,
        stroke_linecap='round'
    ))
    
    # 腿部（简单线条）
    leg_positions = [(150, 200), (160, 220), (170, 235), (230, 205), (220, 220), (210, 235)]
    for i, (x, y) in enumerate(leg_positions):
        side = -1 if i < 3 else 1
        dwg.add(dwg.line(
            start=(x, y),
            end=(x + side * 15, y + 10),
            stroke=colors['body_dark'],
            stroke_width=3,
            stroke_linecap='round'
        ))
    
    # 添加文字 "Shrimp"
    dwg.add(dwg.text(
        'Shrimp',
        insert=(200, 340),
        font_family='Arial, sans-serif',
        font_size=32,
        font_weight='bold',
        fill=colors['body'],
        text_anchor='middle'
    ))
    
    # 添加文字 "Clan"
    dwg.add(dwg.text(
        'Clan',
        insert=(200, 375),
        font_family='Arial, sans-serif',
        font_size=24,
        fill=colors['accent'],
        text_anchor='middle'
    ))
    
    # 保存 SVG
    dwg.save()
    print(f"✅ SVG Logo 已生成: {svg_path}")
    
    # 尝试转换为 PNG（如果有 cairosvg）
    try:
        import cairosvg
        png_path = os.path.join(output_dir, "shrimp-logo.png")
        cairosvg.svg2png(url=svg_path, write_to=png_path, output_width=400, output_height=400)
        print(f"✅ PNG Logo 已生成: {png_path}")
    except ImportError:
        print("ℹ️  未安装 cairosvg，跳过 PNG 生成")
        print("   可以手动用浏览器打开 SVG 另存为 PNG")
    
    return svg_path

def create_tool_icons(output_dir="./assets"):
    """为每个工具创建图标"""
    
    os.makedirs(output_dir, exist_ok=True)
    
    tools = [
        ('deploy', '🦞', '#FF6B9D', '部署虾'),
        ('uninstall', '💥', '#FF1744', '卸载虾'),
        ('snapshot', '💾', '#4ECDC4', '备份虾'),
    ]
    
    for name, emoji, color, label in tools:
        svg_path = os.path.join(output_dir, f"icon-{name}.svg")
        dwg = svgwrite.Drawing(svg_path, size=(100, 100), profile='tiny')
        
        # 背景圆
        dwg.add(dwg.circle(center=(50, 50), r=45, fill=color, opacity=0.2))
        dwg.add(dwg.circle(center=(50, 50), r=40, fill=color, opacity=0.3))
        
        # Emoji（使用 text 模拟）
        dwg.add(dwg.text(
            emoji,
            insert=(50, 65),
            font_size=50,
            text_anchor='middle',
            font_family='Arial, sans-serif'
        ))
        
        dwg.save()
        print(f"✅ 图标已生成: {svg_path}")

if __name__ == '__main__':
    print("🦞 生成虾族生态 Logo...")
    create_shrimp_logo()
    create_tool_icons()
    print("\n🎉 全部生成完成！")
