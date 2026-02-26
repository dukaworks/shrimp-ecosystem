#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
🦞 虾族生态流程图生成器
生成工具关系的 SVG 流程图
"""

import svgwrite
import os

def create_workflow_diagram(output_dir="./assets"):
    """创建用户旅程流程图"""
    
    os.makedirs(output_dir, exist_ok=True)
    svg_path = os.path.join(output_dir, "workflow-diagram.svg")
    
    # 创建画布
    dwg = svgwrite.Drawing(svg_path, size=(800, 600), profile='tiny')
    
    # 颜色定义
    colors = {
        'deploy': '#FF6B9D',
        'uninstall': '#FF1744',
        'snapshot': '#4ECDC4',
        'user': '#FFD93D',
        'arrow': '#95A5A6',
        'text': '#2C3E50',
        'bg': '#F8F9FA'
    }
    
    # 背景
    dwg.add(dwg.rect(insert=(0, 0), size=(800, 600), fill=colors['bg'], rx=10))
    
    # 标题
    dwg.add(dwg.text(
        '虾族生态 - 用户使用流程',
        insert=(400, 40),
        font_family='Arial, sans-serif',
        font_size=24,
        font_weight='bold',
        fill=colors['text'],
        text_anchor='middle'
    ))
    
    # 定义节点位置
    nodes = {
        'start': (100, 100),
        'deploy': (300, 100),
        'using': (500, 100),
        'backup': (500, 250),
        'broken': (500, 400),
        'uninstall': (300, 400),
        'restore': (100, 400),
        'end': (100, 250),
    }
    
    # 绘制节点函数
    def draw_node(pos, label, color, icon):
        x, y = pos
        # 节点背景
        dwg.add(dwg.rect(
            insert=(x-60, y-30),
            size=(120, 60),
            fill=color,
            rx=8,
            opacity=0.2,
            stroke=color,
            stroke_width=2
        ))
        # 图标
        dwg.add(dwg.text(
            icon,
            insert=(x, y-5),
            font_size=24,
            text_anchor='middle'
        ))
        # 文字
        dwg.add(dwg.text(
            label,
            insert=(x, y+20),
            font_family='Arial, sans-serif',
            font_size=12,
            fill=colors['text'],
            text_anchor='middle'
        ))
    
    # 绘制箭头函数
    def draw_arrow(start, end, label=None):
        x1, y1 = start
        x2, y2 = end
        
        # 计算方向
        dx = x2 - x1
        dy = y2 - y1
        
        # 线条
        dwg.add(dwg.line(
            start=start,
            end=end,
            stroke=colors['arrow'],
            stroke_width=2,
            stroke_dasharray='5,3'
        ))
        
        # 箭头
        angle = 0
        if abs(dx) > abs(dy):
            angle = 0 if dx > 0 else 180
        else:
            angle = 90 if dy > 0 else -90
        
        # 标签
        if label:
            mid_x = (x1 + x2) / 2
            mid_y = (y1 + y2) / 2
            dwg.add(dwg.text(
                label,
                insert=(mid_x, mid_y - 5),
                font_family='Arial, sans-serif',
                font_size=10,
                fill=colors['arrow'],
                text_anchor='middle'
            ))
    
    # 绘制所有节点
    draw_node(nodes['start'], '新用户', colors['user'], '👤')
    draw_node(nodes['deploy'], '部署虾\nofd deploy', colors['deploy'], '🦞')
    draw_node(nodes['using'], '使用 OpenClaw', colors['user'], '💻')
    draw_node(nodes['backup'], '备份虾\nocs create', colors['snapshot'], '💾')
    draw_node(nodes['broken'], '玩坏了/换机器', colors['user'], '💥')
    draw_node(nodes['uninstall'], '卸载虾\nocu', colors['uninstall'], '💥')
    draw_node(nodes['restore'], '备份虾\nocs restore', colors['snapshot'], '💾')
    draw_node(nodes['end'], '恢复原样', colors['user'], '✅')
    
    # 绘制连接
    draw_arrow(nodes['start'], nodes['deploy'], '开始')
    draw_arrow(nodes['deploy'], nodes['using'], '部署完成')
    draw_arrow(nodes['using'], nodes['backup'], '定期备份')
    draw_arrow(nodes['using'], nodes['broken'], '遇到问题')
    draw_arrow(nodes['backup'], nodes['restore'], '需要恢复')
    draw_arrow(nodes['broken'], nodes['uninstall'], '卸载')
    draw_arrow(nodes['uninstall'], nodes['restore'], '自动快照')
    draw_arrow(nodes['restore'], nodes['end'], '恢复成功')
    draw_arrow(nodes['end'], nodes['deploy'], '重新开始')
    
    # 图例
    legend_y = 550
    legend_items = [
        (colors['deploy'], '🦞 部署'),
        (colors['snapshot'], '💾 备份'),
        (colors['uninstall'], '💥 卸载'),
    ]
    x_pos = 200
    for color, label in legend_items:
        dwg.add(dwg.rect(
            insert=(x_pos, legend_y),
            size=(15, 15),
            fill=color,
            rx=3
        ))
        dwg.add(dwg.text(
            label,
            insert=(x_pos + 25, legend_y + 12),
            font_family='Arial, sans-serif',
            font_size=12,
            fill=colors['text']
        ))
        x_pos += 150
    
    dwg.save()
    print(f"✅ 流程图已生成: {svg_path}")
    return svg_path

def create_tool_matrix(output_dir="./assets"):
    """创建工具功能矩阵图"""
    
    svg_path = os.path.join(output_dir, "tool-matrix.svg")
    dwg = svgwrite.Drawing(svg_path, size=(700, 400), profile='tiny')
    
    colors = {
        'header': '#FF6B9D',
        'cell': '#F8F9FA',
        'border': '#E0E0E0',
        'text': '#2C3E50',
        'yes': '#4ECDC4',
        'no': '#FFE5E5'
    }
    
    # 标题
    dwg.add(dwg.text(
        '三叉戟工具功能矩阵',
        insert=(350, 40),
        font_family='Arial, sans-serif',
        font_size=22,
        font_weight='bold',
        fill=colors['text'],
        text_anchor='middle'
    ))
    
    # 表格数据
    headers = ['功能', '🦞 部署虾', '💾 备份虾', '💥 卸载虾']
    rows = [
        ['安装 OpenClaw', '✅', '❌', '❌'],
        ['配置飞书', '✅', '❌', '❌'],
        ['创建快照', '❌', '✅', '✅'],
        ['恢复快照', '❌', '✅', '❌'],
        ['卸载清理', '❌', '❌', '✅'],
        ['导出配置', '❌', '✅', '✅'],
        ['导入配置', '❌', '✅', '❌'],
    ]
    
    # 绘制表格
    start_y = 80
    row_height = 40
    col_widths = [200, 150, 150, 150]
    
    # 表头
    x_pos = 50
    for i, header in enumerate(headers):
        w = col_widths[i]
        dwg.add(dwg.rect(
            insert=(x_pos, start_y),
            size=(w, row_height),
            fill=colors['header'],
            stroke='white',
            stroke_width=1
        ))
        dwg.add(dwg.text(
            header,
            insert=(x_pos + w/2, start_y + 25),
            font_family='Arial, sans-serif',
            font_size=14,
            font_weight='bold',
            fill='white',
            text_anchor='middle'
        ))
        x_pos += w
    
    # 数据行
    for row_idx, row in enumerate(rows):
        y_pos = start_y + (row_idx + 1) * row_height
        x_pos = 50
        
        for col_idx, cell in enumerate(row):
            w = col_widths[col_idx]
            
            # 背景色
            fill_color = colors['cell']
            if col_idx > 0 and cell == '✅':
                fill_color = colors['yes']
            
            dwg.add(dwg.rect(
                insert=(x_pos, y_pos),
                size=(w, row_height),
                fill=fill_color,
                stroke=colors['border'],
                stroke_width=1
            ))
            
            # 文字
            dwg.add(dwg.text(
                cell,
                insert=(x_pos + w/2, y_pos + 25),
                font_family='Arial, sans-serif',
                font_size=14,
                fill=colors['text'],
                text_anchor='middle'
            ))
            
            x_pos += w
    
    dwg.save()
    print(f"✅ 工具矩阵已生成: {svg_path}")
    return svg_path

if __name__ == '__main__':
    print("🦞 生成流程图...")
    create_workflow_diagram("/root/.openclaw/workspace/shrimp-ecosystem/assets/assets")
    create_tool_matrix("/root/.openclaw/workspace/shrimp-ecosystem/assets/assets")
    print("\n🎉 全部生成完成！")
