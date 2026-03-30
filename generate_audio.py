#!/usr/bin/env python3
"""
HSK4 Flashcards - Audio Generator
شغّله على MinisForum: python3 generate_audio.py
يحتاج: pip install edge-tts
يولّد ملفات mp3 في مجلد audio/ باستخدام صوت Microsoft Xiaoxiao
"""
import asyncio, os, json

try:
    import edge_tts
except ImportError:
    print("❌ ثبّت المكتبة أولاً: pip install edge-tts")
    exit(1)

VOICE = "zh-CN-XiaoxiaoNeural"  # أفضل صوت صيني أنثوي
RATE = "-10%"  # أبطأ قليلاً للتعلم
AUDIO_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "audio")

# كل الكلمات والجمل من التطبيق
words = [
    {"zh":"尝","s":"你尝一下这个菜，味道很好。"},
    {"zh":"讨论","s":"我们一起讨论这个问题吧。"},
    {"zh":"商量","s":"这件事我们商量一下再决定。"},
    {"zh":"猜","s":"你猜猜这个东西多少钱？"},
    {"zh":"收拾","s":"请你收拾一下房间。"},
    {"zh":"整理","s":"我需要整理一下我的东西。"},
    {"zh":"修","s":"这个手机坏了，需要修一修。"},
    {"zh":"弹","s":"她会弹钢琴，弹得很好。"},
    {"zh":"打扮","s":"她今天打扮得很漂亮。"},
    {"zh":"脱","s":"进门以前请脱鞋。"},
    {"zh":"抱","s":"妈妈抱着孩子走了。"},
    {"zh":"敲","s":"有人在敲门，你去开门吧。"},
    {"zh":"寄","s":"我想寄一封信给朋友。"},
    {"zh":"咳嗽","s":"我感冒了，一直咳嗽。"},
    {"zh":"减肥","s":"他每天跑步是为了减肥。"},
    {"zh":"醒","s":"我今天早上六点就醒了。"},
    {"zh":"降落","s":"飞机已经安全降落了。"},
    {"zh":"起飞","s":"飞机什么时候起飞？"},
    {"zh":"乘坐","s":"你可以乘坐地铁去那里。"},
    {"zh":"戴","s":"今天很冷，你戴上帽子吧。"},
    {"zh":"理发","s":"我的头发太长了，要去理发。"},
    {"zh":"打折","s":"这件衣服打八折。"},
    {"zh":"允许","s":"这里不允许抽烟。"},
    {"zh":"伤害","s":"我不想伤害你的感情。"},
    {"zh":"加班","s":"他每天都要加班到很晚。"},
    {"zh":"禁止","s":"禁止在图书馆里大声说话。"},
    {"zh":"汗","s":"运动以后他出了很多汗。"},
    {"zh":"力气","s":"他的力气很大。"},
    {"zh":"航班","s":"你的航班是几点的？"},
    {"zh":"迷路","s":"我在北京迷路了。"},
    {"zh":"味道","s":"这个汤的味道很好。"},
    {"zh":"饼干","s":"我买了一盒饼干。"},
    {"zh":"汤","s":"冬天喝汤很舒服。"},
    {"zh":"果汁","s":"你想喝果汁还是喝水？"},
    {"zh":"巧克力","s":"她最喜欢吃巧克力。"},
    {"zh":"袜子","s":"我需要买一双新袜子。"},
    {"zh":"帽子","s":"这顶帽子很好看。"},
    {"zh":"毛巾","s":"请给我一条毛巾。"},
    {"zh":"垃圾桶","s":"把垃圾扔到垃圾桶里。"},
    {"zh":"沙发","s":"他在沙发上睡着了。"},
    {"zh":"盒子","s":"这个盒子里面有什么？"},
    {"zh":"钥匙","s":"我找不到我的钥匙了。"},
    {"zh":"镜子","s":"她喜欢照镜子。"},
    {"zh":"传真","s":"请你把这个文件用传真发过来。"},
    {"zh":"现金","s":"对不起，我没带现金。"},
    {"zh":"信用卡","s":"可以用信用卡付钱吗？"},
    {"zh":"价格","s":"这个东西的价格太贵了。"},
    {"zh":"零钱","s":"你有零钱吗？"},
    {"zh":"消息","s":"我刚收到一个好消息。"},
    {"zh":"经历","s":"这是一次难忘的经历。"},
    {"zh":"区别","s":"这两个词有什么区别？"},
    {"zh":"答案","s":"你知道这道题的答案吗？"},
    {"zh":"信封","s":"请把信放在信封里。"},
    {"zh":"方向","s":"你走错方向了。"},
    {"zh":"日记","s":"她每天都写日记。"},
    {"zh":"风景","s":"这里的风景太美了。"},
    {"zh":"伤心","s":"听到这个消息，他很伤心。"},
    {"zh":"失望","s":"考试没考好，我很失望。"},
    {"zh":"吃惊","s":"他的话让我很吃惊。"},
    {"zh":"难受","s":"我今天身体不舒服，很难受。"},
    {"zh":"害羞","s":"她是一个害羞的女孩。"},
    {"zh":"怀疑","s":"我怀疑他说的不是真的。"},
    {"zh":"信心","s":"你要对自己有信心。"},
    {"zh":"兴奋","s":"明天要去旅游，我很兴奋。"},
    {"zh":"困","s":"昨天没睡好，今天很困。"},
    {"zh":"咸","s":"这个菜太咸了。"},
    {"zh":"苦","s":"这个药很苦。"},
    {"zh":"暖和","s":"今天天气很暖和。"},
    {"zh":"值得","s":"这部电影值得看。"},
    {"zh":"精彩","s":"昨天的比赛非常精彩。"},
    {"zh":"有趣","s":"这本书很有趣。"},
    {"zh":"脏","s":"你的衣服太脏了，去洗一下。"},
    {"zh":"轻","s":"这个箱子很轻。"},
    {"zh":"厚","s":"冬天要穿厚一点的衣服。"},
    {"zh":"破","s":"这双鞋已经破了。"},
    {"zh":"乱","s":"你的房间太乱了。"},
    {"zh":"重","s":"这个包太重了，我拿不动。"},
    {"zh":"空","s":"冰箱是空的，需要去买东西。"},
    {"zh":"响","s":"手机突然响了。"},
    {"zh":"占线","s":"我打电话给他，但是占线。"},
    {"zh":"来得及","s":"别着急，来得及。"},
    {"zh":"来不及","s":"快走吧，来不及了！"},
]

async def generate_one(text, filepath):
    if os.path.exists(filepath) and os.path.getsize(filepath) > 100:
        return False  # Skip existing
    comm = edge_tts.Communicate(text, VOICE, rate=RATE)
    await comm.save(filepath)
    return True

async def main():
    os.makedirs(AUDIO_DIR, exist_ok=True)
    
    total = len(words) * 2
    done = 0
    generated = 0
    
    print(f"🔊 Generating audio for {len(words)} words + {len(words)} sentences...")
    print(f"   Voice: {VOICE} | Rate: {RATE}")
    print(f"   Output: {AUDIO_DIR}/\n")
    
    for i, w in enumerate(words):
        # Word
        wpath = os.path.join(AUDIO_DIR, f"w_{i}.mp3")
        if await generate_one(w['zh'], wpath):
            generated += 1
        done += 1
        
        # Sentence
        spath = os.path.join(AUDIO_DIR, f"s_{i}.mp3")
        if await generate_one(w['s'], spath):
            generated += 1
        done += 1
        
        if (i + 1) % 10 == 0 or i == len(words) - 1:
            print(f"  ✓ {done}/{total} ({w['zh']})")
    
    # Count files
    files = [f for f in os.listdir(AUDIO_DIR) if f.endswith('.mp3')]
    total_size = sum(os.path.getsize(os.path.join(AUDIO_DIR, f)) for f in files)
    
    print(f"\n✅ Done! {len(files)} audio files ({total_size/1024:.0f} KB)")
    print(f"   New: {generated} | Skipped: {done - generated}")
    print(f"\n📌 Next steps:")
    print(f"   1. git add audio/")
    print(f"   2. git commit -m 'Add pre-generated Xiaoxiao TTS audio'")
    print(f"   3. git push origin main")

asyncio.run(main())
