#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
🦞 虾族生态插图生成器 - 科技草图风格
Cyberpunk Sketch Style
"""

import svgwrite
import os
import random

def sketch_line(x1, y1, x2, y2, roughness=2):
    """生成草图风格的线条（有点抖动）"""
    points = []
    steps = 20
    for i in range(steps + 1):
        t = i / steps
        x = x1 + (x2 - x1) * t
        y = y1 + (y2 - y1) * t
        # 添加随机抖动
        if 0 < i < steps:  # 端点不抖动
            x += random.uniform(-roughness, roughness)
            y += random.uniform(-roughness, roughness)
        points.append((x, y))
    
    # 生成路径
    path_d = f"M {points[0][0]} {points[0][1]}"
    for i in range(1, len(points)):
        path_d += f" L {points[i][0]} {points[i][1]}"
    
    return path_d

def create_tech_logo(output_dir="./assets"):
    """创建科技草图风格的 Logo"""
    
    os.makedirs(output_dir, exist_ok=True)
    svg_path = os.path.join(output_dir, "shrimp-logo-tech.svg")
    
    dwg = svgwrite.Drawing(svg_path, size=(600, 600), profile='tiny')
    
    # 科技风配色
    colors = {
        'bg': '#0D1117',           # 深色背景
        'grid': '#21262D',         # 网格线
        'primary': '#00F0FF',      # 青色霓虹
        'secondary': '#FF006E',    # 粉红霓虹
        'accent': '#FFBE0B',       # 黄色点缀
        'text': '#E6EDF3',         # 文字
        'dim': '#8B949E',          # 次要文字
    }
    
    # 背景
    dwg.add(dwg.rect(insert=(0, 0), size=(600, 600), fill=colors['bg']))
    
    # 网格背景（草图感）
    grid_size = 30
    for i in range(0, 601, grid_size):
        # 垂直线（带轻微抖动）
        path_d = sketch_line(i, 0, i, 600, roughness=0.5)
        dwg.add(dwg.path(d=path_d, fill='none', stroke=colors['grid'], stroke_width=0.5, opacity=0.5))
    
    for i in range(0, 601, grid_size):
        # 水平线
        path_d = sketch_line(0, i, 600, i, roughness=0.5)
        dwg.add(dwg.path(d=path_d, fill='none', stroke=colors['grid'], stroke_width=0.5, opacity=0.5))
    
    # 中心圆环（科技扫描线效果）
    center_x, center_y = 300, 280
    
    # 外圈虚线环
    dwg.add(dwg.circle(
        center=(center_x, center_y),
        r=200,
        fill='none',
        stroke=colors['primary'],
        stroke_width=2,
        stroke_dasharray='10,5',
        opacity=0.6
    ))
    
    # 内圈实线环
    dwg.add(dwg.circle(
        center=(center_x, center_y),
        r=160,
        fill='none',
        stroke=colors['secondary'],
        stroke_width=3,
        opacity=0.8
    ))
    
    # 小龙虾主体 - 几何线条风格
    # 身体（三角形组合）
    body_points = [
        (center_x, center_y - 80),    # 头顶
        (center_x - 60, center_y + 40),  # 左下
        (center_x, center_y + 20),    # 底部中心
        (center_x + 60, center_y + 40),  # 右下
    ]
    
    # 绘制身体（多边形）
    body_path = f"M {body_points[0][0]} {body_points[0][1]}"
    for p in body_points[1:]:
        body_path += f" L {p[0]} {p[1]}"
    body_path += " Z"
    
    dwg.add(dwg.path(
        d=body_path,
        fill='none',
        stroke=colors['primary'],
        stroke_width=4,
        stroke_linecap='round',
        stroke_linejoin='round'
    ))
    
    # 身体内部线条（科技感）
    dwg.add(dwg.line(
        start=(center_x, center_y - 80),
        end=(center_x, center_y + 20),
        stroke=colors['primary'],
        stroke_width=2,
        opacity=0.5
    ))
    
    # 眼睛（六边形）
    def draw_hexagon(cx, cy, r, color):
        points = []
        for i in range(6):
            angle = (i * 60 - 30) * 3.14159 / 180
            x = cx + r * 0.9 * (i % 2 + 0.5) * (1 if i < 3 else -1)  # 简化为菱形
            y = cy + r * 0.6 * (1 if i in [1, 2] else -1)
        # 简化：用菱形代替六边形
        diamond = f"M {cx} {cy-r} L {cx+r*0.8} {cy} L {cx} {cy+r} L {cx-r*0.8} {cy} Z"
        dwg.add(dwg.path(d=diamond, fill='none', stroke=color, stroke_width=2))
    
    # 左眼
    draw_hexagon(center_x - 25, center_y - 20, 15, colors['accent'])
    dwg.add(dwg.circle(center=(center_x - 25, center_y - 20), r=5, fill=colors['accent']))
    
    # 右眼
    draw_hexagon(center_x + 25, center_y - 20, 15, colors['accent'])
    dwg.add(dwg.circle(center=(center_x + 25, center_y - 20), r=5, fill=colors['accent']))
    
    # 螯（钳子）- 几何线条
    # 左螯
    claw_left = f"M {center_x - 60} {center_y + 20} L {center_x - 100} {center_y - 20} L {center_x - 90} {center_y + 10} L {center_x - 70} {center_y + 30}"
    dwg.add(dwg.path(d=claw_left, fill='none', stroke=colors['secondary'], stroke_width=3, stroke_linecap='round'))
    
    # 右螯
    claw_right = f"M {center_x + 60} {center_y + 20} L {center_x + 100} {center_y - 20} L {center_x + 90} {center_y + 10} L {center_x + 70} {center_y + 30}"
    dwg.add(dwg.path(d=claw_right, fill='none', stroke=colors['secondary'], stroke_width=3, stroke_linecap='round'))
    
    # 触角 - 曲线
    dwg.add(dwg.path(
        d=f"M {center_x - 20} {center_y - 80} Q {center_x - 40} {center_y - 120} {center_x - 60} {center_y - 110}",
        fill='none',
        stroke=colors['dim'],
        stroke_width=2,
        stroke_dasharray='5,3'
    ))
    dwg.add(dwg.path(
        d=f"M {center_x + 20} {center_y - 80} Q {center_x + 40} {center_y - 120} {center_x + 60} {center_y - 110}",
        fill='none',
        stroke=colors['dim'],
        stroke_width=2,
        stroke_dasharray='5,3'
    ))
    
    # 底部文字 - 居中
    # SHRIMP 大字 - 手动添加空格模拟字间距
    dwg.add(dwg.text(
        'S H R I M P',
        insert=(300, 520),
        font_family='Courier New, monospace',
        font_size=48,
        font_weight='bold',
        fill=colors['primary'],
        text_anchor='middle'
    ))
    
    # CLAN 小字
    dwg.add(dwg.text(
        'C L A N',
        insert=(300, 565),
        font_family='Courier New, monospace',
        font_size=24,
        fill=colors['secondary'],
        text_anchor='middle'
    ))
    
    # 版本号
    dwg.add(dwg.text(
        'v1.0',
        insert=(300, 590),
        font_family='Courier New, monospace',
        font_size=12,
        fill=colors['dim'],
        text_anchor='middle'
    ))
    
    # 角落装饰 - 科技元素
    # 左上角
    dwg.add(dwg.path(d="M 20 20 L 60 20 L 60 30 L 30 30 L 30 60 L 20 60 Z", fill='none', stroke=colors['primary'], stroke_width=1, opacity=0.5))
    # 右上角
    dwg.add(dwg.path(d="M 580 20 L 540 20 L 540 30 L 570 30 L 570 60 L 580 60 Z", fill='none', stroke=colors['primary'], stroke_width=1, opacity=0.5))
    # 左下角
    dwg.add(dwg.path(d="M 20 580 L 60 580 L 60 570 L 30 570 L 30 540 L 20 540 Z", fill='none', stroke=colors['primary'], stroke_width=1, opacity=0.5))
    # 右下角
    dwg.add(dwg.path(d="M 580 580 L 540 580 L 540 570 L 570 570 L 570 540 L 580 540 Z", fill='none', stroke=colors['primary'], stroke_width=1, opacity=0.5))
    
    dwg.save()
    print(f"✅ 科技风 Logo 已生成: {svg_path}")
    return svg_path

def create_tech_workflow(output_dir="./assets"):
    """创建科技草图风格的流程图 - 居中布局"""
    
    svg_path = os.path.join(output_dir, "workflow-diagram-tech.svg")
    
    # 画布尺寸
    width, height = 900, 700
    dwg = svgwrite.Drawing(svg_path, size=(width, height), profile='tiny')
    
    # 配色
    colors = {
        'bg': '#0D1117',
        'grid': '#21262D',
        'primary': '#00F0FF',
        'secondary': '#FF006E',
        'accent': '#FFBE0B',
        'text': '#E6EDF3',
        'dim': '#8B949E',
        'deploy': '#00F0FF',
        'backup': '#FFBE0B',
        'uninstall': '#FF006E',
    }
    
    # 背景
    dwg.add(dwg.rect(insert=(0, 0), size=(width, height), fill=colors['bg']))
    
    # 网格
    for i in range(0, width + 1, 40):
        dwg.add(dwg.line(start=(i, 0), end=(i, height), stroke=colors['grid'], stroke_width=0.5, opacity=0.3))
    for i in range(0, height + 1, 40):
        dwg.add(dwg.line(start=(0, i), end=(width, i), stroke=colors['grid'], stroke_width=0.5, opacity=0.3))
    
    # 标题 - 居中
    title_y = 60
    dwg.add(dwg.text(
        '虾族生态工作流',
        insert=(width/2, title_y),
        font_family='Courier New, monospace',
        font_size=32,
        font_weight='bold',
        fill=colors['primary'],
        text_anchor='middle'
    ))
    
    # 副标题
    dwg.add(dwg.text(
        'Shrimp Clan Ecosystem Workflow',
        insert=(width/2, title_y + 30),
        font_family='Courier New, monospace',
        font_size=14,
        fill=colors['dim'],
        text_anchor='middle'
    ))
    
    # 节点定义 - 水平居中布局
    center_x = width / 2
    start_y = 140
    spacing = 90
    
    nodes = {
        'user': (center_x, start_y, '👤 用户', colors['text'], 'start'),
        'deploy': (center_x - 250, start_y + spacing, '🦞 部署\nofd deploy', colors['deploy'], 'process'),
        'using': (center_x, start_y + spacing * 2, '💻 使用\nOpenClaw', colors['text'], 'process'),
        'backup': (center_x + 250, start_y + spacing, '💾 备份\nocs create', colors['backup'], 'process'),
        'issue': (center_x, start_y + spacing * 3, '💥 遇到问题\n重装/迁移', colors['secondary'], 'decision'),
        'uninstall': (center_x - 250, start_y + spacing * 3, '💥 卸载\nocu', colors['uninstall'], 'process'),
        'restore': (center_x + 250, start_y + spacing * 3, '💾 恢复\nocs restore', colors['backup'], 'process'),
        'end': (center_x, start_y + spacing * 4, '✅ 完成', colors['primary'], 'end'),
    }
    
    # 绘制节点函数
    def draw_node(x, y, label, color, node_type):
        # 外框
        if node_type == 'start' or node_type == 'end':
            # 圆形
            dwg.add(dwg.circle(center=(x, y), r=35, fill='none', stroke=color, stroke_width=2))
        elif node_type == 'decision':
            # 菱形
            diamond = f"M {x} {y-40} L {x+50} {y} L {x} {y+40} L {x-50} {y} Z"
            dwg.add(dwg.path(d=diamond, fill='none', stroke=color, stroke_width=2))
        else:
            # 圆角矩形
            dwg.add(dwg.rect(insert=(x-55, y-35), size=(110, 70), fill='none', stroke=color, stroke_width=2, rx=8))
        
        # 文字 - 分行显示
        lines = label.split('\n')
        for i, line in enumerate(lines):
            offset = (len(lines) - 1) * 8
            dwg.add(dwg.text(
                line,
                insert=(x, y - offset + i * 16),
                font_family='Courier New, monospace',
                font_size=11 if i == 0 else 10,
                font_weight='bold' if i == 0 else 'normal',
                fill=color if i == 0 else colors['dim'],
                text_anchor='middle'
            ))
    
    # 绘制所有节点
    for key, (x, y, label, color, node_type) in nodes.items():
        draw_node(x, y, label, color, node_type)
    
    # 绘制连接箭头
    def draw_arrow(x1, y1, x2, y2, color, label=None):
        # 线条
        dwg.add(dwg.line(start=(x1, y1), end=(x2, y2), stroke=color, stroke_width=1.5, opacity=0.7))
        
        # 箭头
        angle = 0  # 简化箭头
        if abs(x2 - x1) > abs(y2 - y1):
            # 水平箭头
            if x2 > x1:
                arrow = f"M {x2-8} {y2-4} L {x2} {y2} L {x2-8} {y2+4}"
            else:
                arrow = f"M {x2+8} {y2-4} L {x2} {y2} L {x2+8} {y2+4}"
        else:
            # 垂直箭头
            if y2 > y1:
                arrow = f"M {x2-4} {y2-8} L {x2} {y2} L {x2+4} {y2-8}"
            else:
                arrow = f"M {x2-4} {y2+8} L {x2} {y2} L {x2+4} {y2+8}"
        
        dwg.add(dwg.path(d=arrow, fill='none', stroke=color, stroke_width=1.5))
        
        # 标签
        if label:
            mid_x = (x1 + x2) / 2
            mid_y = (y1 + y2) / 2
            dwg.add(dwg.text(
                label,
                insert=(mid_x, mid_y - 5),
                font_family='Courier New, monospace',
                font_size=9,
                fill=colors['dim'],
                text_anchor='middle'
            ))
    
    # 绘制连接
    cx, cy = nodes['user'][0], nodes['user'][1]
    deploy_x, deploy_y = nodes['deploy'][0], nodes['deploy'][1]
    using_x, using_y = nodes['using'][0], nodes['using'][1]
    backup_x, backup_y = nodes['backup'][0], nodes['backup'][1]
    issue_x, issue_y = nodes['issue'][0], nodes['issue'][1]
    uninstall_x, uninstall_y = nodes['uninstall'][0], nodes['uninstall'][1]
    restore_x, restore_y = nodes['restore'][0], nodes['restore'][1]
    end_x, end_y = nodes['end'][0], nodes['end'][1]
    
    draw_arrow(cx, cy + 35, deploy_x, deploy_y - 35, colors['deploy'], '开始')
    draw_arrow(deploy_x + 55, deploy_y, using_x - 55, using_y - 35, colors['deploy'], '部署')
    draw_arrow(using_x + 55, using_y, backup_x - 55, backup_y + 35, colors['backup'], '备份')
    draw_arrow(backup_x, backup_y + 35, restore_x, restore_y - 35, colors['backup'], '恢复')
    draw_arrow(using_x, using_y + 35, issue_x, issue_y - 40, colors['secondary'], '问题')
    draw_arrow(issue_x - 50, issue_y, uninstall_x + 55, uninstall_y, colors['uninstall'], '卸载')
    draw_arrow(uninstall_x + 55, uninstall_y, restore_x - 55, restore_y, colors['uninstall'], '快照')
    draw_arrow(restore_x, restore_y + 35, end_x + 55, end_y, colors['backup'], '完成')
    draw_arrow(issue_x, issue_y + 40, end_x, end_y - 35, colors['primary'], '正常')
    
    # 图例 - 居中在底部
    legend_y = height - 60
    legend_items = [
        (colors['deploy'], '🦞 部署'),
        (colors['backup'], '💾 备份'),
        (colors['uninstall'], '💥 卸载'),
    ]
    
    start_x = width/2 - 150
    for i, (color, label) in enumerate(legend_items):
        x_pos = start_x + i * 150
        dwg.add(dwg.rect(insert=(x_pos, legend_y), size=(12, 12), fill='none', stroke=color, stroke_width=2))
        dwg.add(dwg.text(
            label,
            insert=(x_pos + 20, legend_y + 10),
            font_family='Courier New, monospace',
            font_size=11,
            fill=colors['text']
        ))
    
    # 底部信息 - 居中
    dwg.add(dwg.text(
        'OpenClaw Ecosystem Toolkit',
        insert=(width/2, height - 20),
        font_family='Courier New, monospace',
        font_size=10,
        fill=colors['dim'],
        text_anchor='middle'
    ))
    
    dwg.save()
    print(f"✅ 科技风流程图已生成: {svg_path}")
    return svg_path

if __name__ == '__main__':
    print("🎨 生成科技草图风格插图...")
    create_tech_logo("/root/.openclaw/workspace/shrimp-ecosystem/assets")
    create_tech_workflow("/root/.openclaw/workspace/shrimp-ecosystem/assets")
    print("\n🎉 全部生成完成！")
