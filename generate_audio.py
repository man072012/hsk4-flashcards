#!/usr/bin/env python3
"""
HSK4 Flashcards - مولّد الملفات الصوتية
========================================
يستخدم صوت Microsoft Xiaoxiao Neural (أفضل صوت صيني)
عبر مكتبة edge-tts (مجانية بدون API key)

التشغيل:
  pip install edge-tts
  python3 generate_audio.py

الملفات المولّدة:
  audio/w_0.mp3 → w_81.mp3  (82 كلمة)
  audio/s_0.mp3 → s_81.mp3  (82 جملة)
"""
import asyncio
import edge_tts
import os

VOICE = "zh-CN-XiaoxiaoNeural"
OUTPUT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "audio")

words = [
    {"zh":"尝", "sentence":{"zh":"你尝一下这个菜，味道很好。"}},
    {"zh":"讨论", "sentence":{"zh":"我们一起讨论这个问题吧。"}},
    {"zh":"商量", "sentence":{"zh":"这件事我们商量一下再决定。"}},
    {"zh":"猜", "sentence":{"zh":"你猜猜这个东西多少钱？"}},
    {"zh":"收拾", "sentence":{"zh":"请你收拾一下房间。"}},
    {"zh":"整理", "sentence":{"zh":"我需要整理一下我的东西。"}},
    {"zh":"修", "sentence":{"zh":"这个手机坏了，需要修一修。"}},
    {"zh":"弹", "sentence":{"zh":"她会弹钢琴，弹得很好。"}},
    {"zh":"打扮", "sentence":{"zh":"她今天打扮得很漂亮。"}},
    {"zh":"脱", "sentence":{"zh":"进门以前请脱鞋。"}},
    {"zh":"抱", "sentence":{"zh":"妈妈抱着孩子走了。"}},
    {"zh":"敲", "sentence":{"zh":"有人在敲门，你去开门吧。"}},
    {"zh":"寄", "sentence":{"zh":"我想寄一封信给朋友。"}},
    {"zh":"咳嗽", "sentence":{"zh":"我感冒了，一直咳嗽。"}},
    {"zh":"减肥", "sentence":{"zh":"他每天跑步是为了减肥。"}},
    {"zh":"醒", "sentence":{"zh":"我今天早上六点就醒了。"}},
    {"zh":"降落", "sentence":{"zh":"飞机已经安全降落了。"}},
    {"zh":"起飞", "sentence":{"zh":"飞机什么时候起飞？"}},
    {"zh":"乘坐", "sentence":{"zh":"你可以乘坐地铁去那里。"}},
    {"zh":"戴", "sentence":{"zh":"今天很冷，你戴上帽子吧。"}},
    {"zh":"理发", "sentence":{"zh":"我的头发太长了，要去理发。"}},
    {"zh":"打折", "sentence":{"zh":"这件衣服打八折。"}},
    {"zh":"允许", "sentence":{"zh":"这里不允许抽烟。"}},
    {"zh":"伤害", "sentence":{"zh":"我不想伤害你的感情。"}},
    {"zh":"加班", "sentence":{"zh":"他每天都要加班到很晚。"}},
    {"zh":"禁止", "sentence":{"zh":"禁止在图书馆里大声说话。"}},
    {"zh":"汗", "sentence":{"zh":"运动以后他出了很多汗。"}},
    {"zh":"力气", "sentence":{"zh":"他的力气很大。"}},
    {"zh":"航班", "sentence":{"zh":"你的航班是几点的？"}},
    {"zh":"迷路", "sentence":{"zh":"我在北京迷路了。"}},
    {"zh":"味道", "sentence":{"zh":"这个汤的味道很好。"}},
    {"zh":"饼干", "sentence":{"zh":"我买了一盒饼干。"}},
    {"zh":"汤", "sentence":{"zh":"冬天喝汤很舒服。"}},
    {"zh":"果汁", "sentence":{"zh":"你想喝果汁还是喝水？"}},
    {"zh":"巧克力", "sentence":{"zh":"她最喜欢吃巧克力。"}},
    {"zh":"袜子", "sentence":{"zh":"我需要买一双新袜子。"}},
    {"zh":"帽子", "sentence":{"zh":"这顶帽子很好看。"}},
    {"zh":"毛巾", "sentence":{"zh":"请给我一条毛巾。"}},
    {"zh":"垃圾桶", "sentence":{"zh":"把垃圾扔到垃圾桶里。"}},
    {"zh":"沙发", "sentence":{"zh":"他在沙发上睡着了。"}},
    {"zh":"盒子", "sentence":{"zh":"这个盒子里面有什么？"}},
    {"zh":"钥匙", "sentence":{"zh":"我找不到我的钥匙了。"}},
    {"zh":"镜子", "sentence":{"zh":"她喜欢照镜子。"}},
    {"zh":"传真", "sentence":{"zh":"请你把这个文件用传真发过来。"}},
    {"zh":"现金", "sentence":{"zh":"对不起，我没带现金。"}},
    {"zh":"信用卡", "sentence":{"zh":"可以用信用卡付钱吗？"}},
    {"zh":"价格", "sentence":{"zh":"这个东西的价格太贵了。"}},
    {"zh":"零钱", "sentence":{"zh":"你有零钱吗？"}},
    {"zh":"消息", "sentence":{"zh":"我刚收到一个好消息。"}},
    {"zh":"经历", "sentence":{"zh":"这是一次难忘的经历。"}},
    {"zh":"区别", "sentence":{"zh":"这两个词有什么区别？"}},
    {"zh":"答案", "sentence":{"zh":"你知道这道题的答案吗？"}},
    {"zh":"信封", "sentence":{"zh":"请把信放在信封里。"}},
    {"zh":"方向", "sentence":{"zh":"你走错方向了。"}},
    {"zh":"日记", "sentence":{"zh":"她每天都写日记。"}},
    {"zh":"风景", "sentence":{"zh":"这里的风景太美了。"}},
    {"zh":"伤心", "sentence":{"zh":"听到这个消息，他很伤心。"}},
    {"zh":"失望", "sentence":{"zh":"考试没考好，我很失望。"}},
    {"zh":"吃惊", "sentence":{"zh":"他的话让我很吃惊。"}},
    {"zh":"难受", "sentence":{"zh":"我今天身体不舒服，很难受。"}},
    {"zh":"害羞", "sentence":{"zh":"她是一个害羞的女孩。"}},
    {"zh":"怀疑", "sentence":{"zh":"我怀疑他说的不是真的。"}},
    {"zh":"信心", "sentence":{"zh":"你要对自己有信心。"}},
    {"zh":"兴奋", "sentence":{"zh":"明天要去旅游，我很兴奋。"}},
    {"zh":"困", "sentence":{"zh":"昨天没睡好，今天很困。"}},
    {"zh":"咸", "sentence":{"zh":"这个菜太咸了。"}},
    {"zh":"苦", "sentence":{"zh":"这个药很苦。"}},
    {"zh":"暖和", "sentence":{"zh":"今天天气很暖和。"}},
    {"zh":"值得", "sentence":{"zh":"这部电影值得看。"}},
    {"zh":"精彩", "sentence":{"zh":"昨天的比赛非常精彩。"}},
    {"zh":"有趣", "sentence":{"zh":"这本书很有趣。"}},
    {"zh":"脏", "sentence":{"zh":"你的衣服太脏了，去洗一下。"}},
    {"zh":"轻", "sentence":{"zh":"这个箱子很轻。"}},
    {"zh":"厚", "sentence":{"zh":"冬天要穿厚一点的衣服。"}},
    {"zh":"破", "sentence":{"zh":"这双鞋已经破了。"}},
    {"zh":"乱", "sentence":{"zh":"你的房间太乱了。"}},
    {"zh":"重", "sentence":{"zh":"这个包太重了，我拿不动。"}},
    {"zh":"空", "sentence":{"zh":"冰箱是空的，需要去买东西。"}},
    {"zh":"响", "sentence":{"zh":"手机突然响了。"}},
    {"zh":"占线", "sentence":{"zh":"我打电话给他，但是占线。"}},
    {"zh":"来得及", "sentence":{"zh":"别着急，来得及。"}},
    {"zh":"来不及", "sentence":{"zh":"快走吧，来不及了！"}}
]
async def generate_audio():
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

    total = len(words) * 2
    done = 0

    print(f"🔊 توليد {len(words)} كلمة + {len(words)} جملة = {total} ملف صوتي")
    print(f"   الصوت: {VOICE}")
    print(f"   المجلد: {OUTPUT_DIR}/\n")

    for index, word in enumerate(words):
        # 1. توليد صوت الكلمة
        word_text = word['zh']
        word_file = os.path.join(OUTPUT_DIR, f"w_{index}.mp3")
        if not os.path.exists(word_file) or os.path.getsize(word_file) < 100:
            communicate = edge_tts.Communicate(word_text, VOICE)
            await communicate.save(word_file)
        done += 1

        # 2. توليد صوت الجملة
        sentence_text = word['sentence']['zh']
        sentence_file = os.path.join(OUTPUT_DIR, f"s_{index}.mp3")
        if not os.path.exists(sentence_file) or os.path.getsize(sentence_file) < 100:
            communicate_sentence = edge_tts.Communicate(sentence_text, VOICE)
            await communicate_sentence.save(sentence_file)
        done += 1

        if (index + 1) % 10 == 0 or index == len(words) - 1:
            print(f"  ✓ {done}/{total}  ({word_text})")

    # إحصائيات
    files = [f for f in os.listdir(OUTPUT_DIR) if f.endswith('.mp3')]
    total_size = sum(os.path.getsize(os.path.join(OUTPUT_DIR, f)) for f in files)
    print(f"\n✅ تم! {len(files)} ملف صوتي ({total_size/1024:.0f} KB)")
    print(f"\n📌 الخطوات التالية:")
    print(f"   git add audio/")
    print(f"   git commit -m 'Add Xiaoxiao TTS audio files'")
    print(f"   git push origin main")

if __name__ == "__main__":
    asyncio.run(generate_audio())
    print("\n🎉 تم الانتهاء من توليد جميع الملفات الصوتية بنجاح!")
