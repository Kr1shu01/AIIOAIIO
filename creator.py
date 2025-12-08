from PIL import Image, ImageDraw, ImageFont
import os

# 创建images文件夹
os.makedirs('images', exist_ok=True)

# 帕鲁名称列表（您可以根据需要扩展）
pals = [
    "棉悠悠", "捣蛋猫", "皮皮鸡", "翠叶鼠", "火绒狐", "雪绒狐", 
    "冲浪鸭", "热浪鸭", "伏特喵", "新叶猿", "燎火鹿", "企丸丸", "闪丸丸",
    "企丸王", "闪丸王", "电棘鼠", "冰刺鼠", "叶泥泥", "玉藻狐", "啼卡尔",
    "壶小象", "瞅什魔", "米露菲", "寐魔", "草莽猪", "露娜蒂", "遁地鼠",
    "勾魂鱿", "蚀魂鱿", "喵斯特", "冰斯特", "鲁米儿", "雷米儿", "猎狼",
    "炸蛋鸟", "波娜兔", "波霸牛", "荆棘魔仙", "鲨小子", "红小鲨", "吊缚灵",
    "冰缚灵", "叶胖达", "雷胖达", "棉花糖", "灌木羊", "郁木羊", "美露帕",
    "紫霞鹿", "祇岳鹿", "疾风隼", "姬小兔", "艾小兔", "炎魔羊", "暗魔羊",
    "幻悦蝶", "炽焰牛", "趴趴鲇", "梆梆鲇", "黑鸦隐士", "庞克蜥", "热血蜥",
    "月镰魔", "霜镰魔", "天擒鸟", "羽箭射手", "山岳射手", "铁拳猿", "石掌猿",
    "骑士蜂", "女皇蜂", "笑魇猫", "毛掸儿", "毛老爹", "疾旋鼬", "桃旋鼬",
    "雷角马", "吹雪狐", "火麒麟", "邪麒麟", "严冬鹿", "霹雳犬", "苍焰狼",
    "幽焰狼", "雷鸣童子", "天阴童子", "秘斯媞雅", "花冠龙", "雷冠龙",
    "滑水蛇", "流沙蛇", "噬魂兽", "碎岩龟", "猫蝠怪", "博爱蜥", "融焰娘",
    "烽歌龙", "霜歌龙", "浪刃武士", "鬼刃武士", "迅雷鸟", "燧火鸟", "暗巫猫",
    "炽巫猫", "焰巫狐", "幽巫狐", "踏春兔", "薇莉塔", "绸笠蛾", "精灵龙",
    "水灵龙", "碧海龙", "碧月龙", "冰棘兽", "金棘兽", "狱焰王", "狱阎王",
    "佩克龙", "派克龙", "连理龙", "海誓龙", "花丽娜", "熔岩兽", "寒霜兽",
    "君王美露帕", "冰帝美露帕", "森猛犸", "雪猛犸", "白绒雪怪", "绿苔绒怪",
    "铠格力斯", "格鲁力斯", "云海鹿", "雷隐鹿", "夜幕魔蝠", "天羽龙", "翠羽龙",
    "焰煌", "殁殃", "雷冥鸟", "雷鸣鸟", "魔渊龙", "冥铠蝎", "金铠蝎",
    "阿努比斯", "覆海龙", "腾炎龙", "朱雀", "清雀", "暴电熊", "百合女王",
    "黑月女王", "荷鲁斯", "伊西斯", "波鲁杰克斯", "异构格里芬", "圣光骑士",
    "混沌骑士", "唤冬兽", "唤夜兽", "空涡龙", "贝拉诺娃", "贝拉露洁", "辉月伊",
    "武道蛙", "极道蛙", "春彩娘", "菇咚", "菇波", "球犰", "恐炬灵", "蛊刺妖",
    "泰锋", "八云犬", "汪宗师", "战冠雀", "旺财", "杰诺贝达", "杰诺路达",
    "杰诺多兰", "魅爱莉", "夜冥驹", "艾基鲁迦", "墨丸", "净世鹿", "面惧",
    "幽恋娜", "桃蛛娘", "驭雷马", "霜牙王", "梅莉姆", "妮瞅莎", "金驰兽",
    "达鼠泥", "冰姬灵", "白真雪雀", "咕咕桑葩", "梁叶龙", "肚肚鳄", "香草豹冰",
    "盔盔仔", "金盔仔", "海月灵", "海月仙", "墨沫姬", "布偶鲨", "粉粉布偶鲨",
    "冥灯鱼", "炙灯鱼", "凉晶鲸", "桃晶鲸", "海皇鲸",
    # 史莱姆系列
    "绿史莱姆", "蓝史莱姆", "红史莱姆", "紫史莱姆", "夜史莱姆", "彩虹史莱姆",
    "附魔剑", "洞穴蝙蝠", "光明蝙蝠", "克苏鲁之眼", "恶魔眼"
]

def create_test_image(name, size=(300, 300)):
    """创建测试图片"""
    # 创建图片
    img = Image.new('RGB', size, color=(70, 130, 180))  # Steel blue background
    draw = ImageDraw.Draw(img)
    
    # 尝试使用中文字体，如果失败则使用默认字体
    try:
        # Windows
        font = ImageFont.truetype("simhei.ttf", 36)
    except:
        try:
            # macOS
            font = ImageFont.truetype("Arial Unicode.ttf", 36)
        except:
            try:
                # Linux
                font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 36)
            except:
                # 默认字体
                font = ImageFont.load_default()
    
    # 绘制边框
    draw.rectangle([0, 0, size[0]-1, size[1]-1], outline=(255, 255, 255), width=3)
    
    # 计算文字位置并绘制帕鲁名称
    bbox = draw.textbbox((0, 0), name, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    x = (size[0] - text_width) // 2
    y = (size[1] - text_height) // 2
    draw.text((x, y), name, fill=(255, 255, 255), font=font)
    
    # 添加编号
    try:
        small_font = ImageFont.truetype("arial.ttf", 20)
    except:
        small_font = ImageFont.load_default()
    
    draw.text((10, 10), "TEST", fill=(255, 255, 0), font=small_font)
    
    return img

# 生成测试图片
print("正在生成测试图片...")
generated_count = 0

for i, pal_name in enumerate(pals):
    if generated_count >= 223:
        break
        
    filename = f"{pal_name}.png"
    filepath = os.path.join('images', filename)
    
    # 创建并保存图片
    img = create_test_image(pal_name)
    img.save(filepath)
    print(f"已生成: {filename}")
    generated_count += 1

# 如果还需要更多图片，可以用现有名称重复生成
if generated_count < 223:
    additional_needed = 223 - generated_count
    for i in range(additional_needed):
        if generated_count >= 223:
            break
            
        # 循环使用现有名称
        pal_name = pals[i % len(pals)]
        filename = f"{pal_name}_{(i//len(pals))+2}.png"  # 添加后缀避免重复
        filepath = os.path.join('images', filename)
        
        img = create_test_image(f"{pal_name}")
        img.save(filepath)
        print(f"已生成: {filename}")
        generated_count += 1

print(f"\n完成！总共生成了 {generated_count} 张测试图片在 'images' 文件夹中")