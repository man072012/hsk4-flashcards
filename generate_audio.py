#!/usr/bin/env python3
"""
HSK4 Flashcards - مولّد الملفات الصوتية (130 كلمة)
pip install edge-tts
python3 generate_audio.py
"""
import asyncio, edge_tts, os

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
    {"zh":"来不及", "sentence":{"zh":"快走吧，来不及了！"}},
    {"zh":"挂", "sentence":{"zh":"他想把画挂在墙上。"}},
    {"zh":"躺", "sentence":{"zh":"她在沙发上躺着。"}},
    {"zh":"试", "sentence":{"zh":"你要不要试试这条裙子？"}},
    {"zh":"算", "sentence":{"zh":"我来算一下一共花了多少钱。"}},
    {"zh":"擦", "sentence":{"zh":"看，我把盘子擦干净了。"}},
    {"zh":"抬", "sentence":{"zh":"我们把沙发抬到客厅去吧。"}},
    {"zh":"赢", "sentence":{"zh":"这次比赛我们赢了！"}},
    {"zh":"祝", "sentence":{"zh":"祝你生日快乐！"}},
    {"zh":"养成", "sentence":{"zh":"应该养成每天刷牙的好习惯。"}},
    {"zh":"估计", "sentence":{"zh":"估计半小时后到。"}},
    {"zh":"等", "sentence":{"zh":"她在等朋友的电话。"}},
    {"zh":"毕业", "sentence":{"zh":"祝贺你顺利毕业！"}},
    {"zh":"聊天儿", "sentence":{"zh":"她们一边喝茶一边聊天儿。"}},
    {"zh":"后悔", "sentence":{"zh":"我真后悔告诉他这件事。"}},
    {"zh":"干杯", "sentence":{"zh":"来，为我们的健康干杯！"}},
    {"zh":"联系", "sentence":{"zh":"晚上我们再电话联系。"}},
    {"zh":"肚子", "sentence":{"zh":"你怎么了，肚子疼。"}},
    {"zh":"密码", "sentence":{"zh":"你好，我的密码忘了怎么办？"}},
    {"zh":"笑话", "sentence":{"zh":"他讲的笑话真有意思。"}},
    {"zh":"杂志", "sentence":{"zh":"他坐在沙发上看杂志。"}},
    {"zh":"京剧", "sentence":{"zh":"京剧一直很受欢迎。"}},
    {"zh":"护士", "sentence":{"zh":"我姐姐在医院上班，她是护士。"}},
    {"zh":"洗衣机", "sentence":{"zh":"他的洗衣机好像出问题了。"}},
    {"zh":"饮料", "sentence":{"zh":"他运动的时候喜欢喝这种饮料。"}},
    {"zh":"包子", "sentence":{"zh":"这家店的包子非常好吃。"}},
    {"zh":"长城", "sentence":{"zh":"下周末我准备去爬长城。"}},
    {"zh":"短信", "sentence":{"zh":"你给他发条短信吧。"}},
    {"zh":"胳膊", "sentence":{"zh":"我的胳膊有点儿疼。"}},
    {"zh":"看法", "sentence":{"zh":"对于这件事，您有什么看法？"}},
    {"zh":"公里", "sentence":{"zh":"他每天早上都要跑两公里。"}},
    {"zh":"西红柿", "sentence":{"zh":"西红柿是水果吗？"}},
    {"zh":"页", "sentence":{"zh":"这本书一共有多少页？"}},
    {"zh":"遍", "sentence":{"zh":"这本书她读过很多遍了。"}},
    {"zh":"激动", "sentence":{"zh":"毕业了，他们很激动。"}},
    {"zh":"香", "sentence":{"zh":"这些花闻起来很香。"}},
    {"zh":"凉快", "sentence":{"zh":"走在海边，感觉很凉快。"}},
    {"zh":"活泼", "sentence":{"zh":"这个小女孩儿很活泼。"}},
    {"zh":"仔细", "sentence":{"zh":"你再仔细找找。"}},
    {"zh":"流利", "sentence":{"zh":"她汉语说得很流利。"}},
    {"zh":"严重", "sentence":{"zh":"我就是有点儿感冒，不太严重。"}},
    {"zh":"厉害", "sentence":{"zh":"全都答对了，你真厉害！"}},
    {"zh":"正式", "sentence":{"zh":"他今天穿得十分正式。"}},
    {"zh":"圆", "sentence":{"zh":"这个西瓜又大又圆。"}},
    {"zh":"俩", "sentence":{"zh":"我俩逛街买了很多东西。"}},
    {"zh":"只", "sentence":{"zh":"山上有一只老虎。"}},
    {"zh":"朵", "sentence":{"zh":"这朵花又大又漂亮。"}},
    {"zh":"棵", "sentence":{"zh":"那棵树的叶子掉光了。"}},
    {"zh":"到底", "sentence":{"zh":"答案到底是什么呢？"}}
]

async def generate_audio():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    total = len(words) * 2
    done = 0
    print(f"🔊 توليد {len(words)} كلمة + {len(words)} جملة = {total} ملف صوتي")
    print(f"   الصوت: {VOICE}")
    print(f"   المجلد: {OUTPUT_DIR}/\n")
    for i, w in enumerate(words):
        wpath = os.path.join(OUTPUT_DIR, f"w_{i}.mp3")
        if not os.path.exists(wpath) or os.path.getsize(wpath) < 100:
            comm = edge_tts.Communicate(w['zh'], VOICE)
            await comm.save(wpath)
        done += 1
        spath = os.path.join(OUTPUT_DIR, f"s_{i}.mp3")
        if not os.path.exists(spath) or os.path.getsize(spath) < 100:
            comm = edge_tts.Communicate(w['sentence']['zh'], VOICE)
            await comm.save(spath)
        done += 1
        if (i + 1) % 10 == 0 or i == len(words) - 1:
            print(f"  ✓ {done}/{total}  ({w['zh']})")
    files = [f for f in os.listdir(OUTPUT_DIR) if f.endswith('.mp3')]
    total_size = sum(os.path.getsize(os.path.join(OUTPUT_DIR, f)) for f in files)
    print(f"\n✅ تم! {len(files)} ملف صوتي ({total_size/1024:.0f} KB)")
    print(f"   git add audio/ && git commit -m \'Add TTS audio\' && git push origin main")

if __name__ == "__main__":
    asyncio.run(generate_audio())
    print("\n🎉 تم!")
