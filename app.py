import streamlit as st
from datetime import date

st.set_page_config(page_title="提香美术 AI 内容总监", page_icon="🎨", layout="wide")

st.markdown("""
<style>
.main {background:#faf8f4}
.block-container {padding-top:2rem; max-width:1100px}
.hero {padding:26px; border-radius:18px; background:linear-gradient(120deg,#fff1df,#f9e6dc); margin-bottom:20px}
.small {color:#6b625b}
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="hero"><h1>🎨 提香美术 AI 内容总监</h1><p>让美术机构每天更轻松地做内容、做活动、做招生。</p><p class="small">首版体验 Demo · 面向美术培训机构</p></div>', unsafe_allow_html=True)

with st.sidebar:
    st.header("机构资料")
    studio = st.text_input("机构名称", "提香美术")
    city = st.text_input("所在城市", "长沙")
    audience = st.selectbox("主要招生对象", ["幼儿 3–6 岁", "小学 7–12 岁", "初高中美术生", "成人绘画"])
    style = st.selectbox("内容风格", ["真实温暖", "幽默接地气", "专业可信", "强钩子短视频"])
    st.caption("提示：先生成初稿，发布前请核对活动时间、价格和校区信息。")

tab1, tab2, tab3, tab4 = st.tabs(["📱 短视频脚本", "🎉 活动策划", "💬 家长沟通", "📊 招生复盘"])

with tab1:
    st.subheader("短视频脚本生成器")
    topic = st.text_input("视频主题", "孩子学画画，真正练到的是什么？")
    goal = st.selectbox("本条视频目标", ["吸引同城家长", "展示课堂", "推广体验课", "建立老师个人品牌"])
    seconds = st.select_slider("视频时长", options=[15, 30, 45, 60], value=30)
    if st.button("生成短视频脚本", type="primary", key="video"):
        script = f"""【账号】{studio}｜{city}
【主题】{topic}
【目标】{goal}｜约{seconds}秒｜风格：{style}

【前3秒钩子】
别急着问孩子画得像不像，先看看他愿不愿意自己动手。

【中段口播】
在{studio}的课堂上，我们更关注孩子观察、表达和坚持的过程。今天围绕“{topic}”，让孩子先观察、再尝试，最后讲讲自己的创作想法。每个孩子的节奏不一样，重要的是让他敢于表达、乐于探索。

【镜头建议】
1. 0–3秒：孩子专注创作的近景，配大字幕。
2. 3–12秒：老师引导、孩子动手的真实课堂画面。
3. 12–{seconds-5}秒：作品细节与孩子讲述作品的镜头。
4. 结尾：老师或校区环境，字幕“想了解体验课？欢迎私信咨询”。

【结尾互动】
你觉得孩子学画画，最重要的是技巧还是表达？评论区聊聊。

【发布前检查】
不要虚构学生效果、家长评价或限时优惠；画面中的孩子需取得监护人同意。"""
        st.text_area("可复制的脚本", script, height=360)
        st.download_button("下载脚本 TXT", script, file_name="提香美术短视频脚本.txt")

with tab2:
    st.subheader("活动策划助手")
    event = st.text_input("活动主题", "我和披萨有个约会")
    budget = st.number_input("预计每位孩子成本（元）", min_value=0, value=50, step=5)
    count = st.number_input("预计参与人数", min_value=1, value=20, step=1)
    if st.button("生成活动方案", type="primary", key="event"):
        plan = f"""【{event}｜活动执行方案】
主办：{studio}｜地点：{city}
预计人数：{count}人｜单人成本预算：{budget}元｜总成本预算：{budget*count}元

一、活动目标
用绘画创作+主题体验增加孩子参与感，让家长看到机构的教学特色。

二、流程建议（约3小时）
1. 签到与破冰（15分钟）
2. 绘画创作（40分钟）
3. 主题体验/手作（35分钟）
4. 分享与作品展示（20分钟）
5. 主题餐食或休息（30分钟）
6. 合影、家长反馈与后续咨询（20分钟）

三、人员分工
主负责人：控场与安全；美术老师：创作教学；助教：签到、材料和拍摄；家长志愿者：协助秩序。

四、物资清单
画纸、颜料、画笔、围裙、桌面防护、签到表、饮用水、垃圾袋、急救包。

五、预算提醒
按实际报价核算材料、场地、餐食、交通、保险和备用金；提前确认过敏情况、肖像授权与接送安排。
"""
        st.text_area("活动方案", plan, height=360)
        st.download_button("下载活动方案 TXT", plan, file_name="提香美术活动方案.txt")

with tab3:
    st.subheader("家长沟通话术")
    scenario = st.selectbox("家长咨询场景", ["孩子没基础，能学吗？", "孩子坐不住怎么办？", "想先问价格", "孩子不愿意来体验", "体验后还没报名"])
    if st.button("生成沟通话术", type="primary", key="parent"):
        replies = {
          "孩子没基础，能学吗？": "当然可以。课程会根据孩子的年龄和基础逐步引导，不要求一开始就画得像。我们更希望孩子在观察、动手和表达中建立兴趣。方便问一下孩子几岁了？平时喜欢涂画还是手工？我可以帮您看看更适合哪类体验。",
          "孩子坐不住怎么办？": "这个年龄的孩子专注时间各不相同，我们会把任务拆成小步骤，并穿插观察、操作和分享。可以先体验一次，看看孩子在真实课堂里的状态，再决定是否适合。",
          "想先问价格": "可以的，我先把课程内容、课时和费用说明清楚，方便您比较。不同年龄和课程安排可能不一样，您家孩子现在几岁？我按年龄给您介绍合适的方案，不用急着决定。",
          "孩子不愿意来体验": "可以先不用给孩子压力。您可以告诉我孩子最近喜欢什么，比如动物、汽车、动画或手工，我们可以从兴趣切入。也可以先来看看教室环境，再决定要不要参加。",
          "体验后还没报名": "感谢您带孩子来体验！也想听听您和孩子的真实感受：孩子最喜欢哪个环节？有没有觉得不太适应的地方？我可以根据您的顾虑补充说明课程安排，您考虑好了再决定。"
        }
        st.text_area("沟通话术（可复制）", replies[scenario], height=220)

with tab4:
    st.subheader("招生数据复盘")
    c1, c2, c3 = st.columns(3)
    with c1: leads = st.number_input("本周咨询人数", min_value=0, value=30)
    with c2: trials = st.number_input("到店体验人数", min_value=0, value=12)
    with c3: enroll = st.number_input("报名人数", min_value=0, value=5)
    st.metric("咨询→体验率", f"{trials/leads*100:.1f}%" if leads else "—")
    st.metric("体验→报名率", f"{enroll/trials*100:.1f}%" if trials else "—")
    st.metric("整体转化率", f"{enroll/leads*100:.1f}%" if leads else "—")
    if st.button("生成复盘建议", type="primary", key="review"):
        tips = []
        if leads == 0: tips.append("本周暂无咨询数据，先检查短视频发布、私信回复和同城曝光。")
        elif trials/leads < 0.35: tips.append("咨询到体验偏低：检查回复速度、体验时间是否方便，以及是否清楚说明体验内容。")
        else: tips.append("咨询到体验表现尚可，继续记录不同渠道的到店质量。")
        if trials and enroll/trials < 0.4: tips.append("体验到报名有提升空间：复盘课堂参与感、家长反馈、课程说明和后续跟进。")
        elif trials: tips.append("体验转化表现值得继续跟踪，拆分老师、校区和课程类型比较。")
        tips.append("建议每周记录来源渠道、咨询时间、到店原因和未报名原因；样本较小时不要过度下结论。")
        st.write("\n\n".join("• "+x for x in tips))

st.divider()
st.caption("提香美术 AI 内容总监 · 首版原型。当前为模板驱动演示，不会自动调用大模型，也不会保存客户个人信息。后续可接入 AI API、增加机构知识库和多校区数据。")
