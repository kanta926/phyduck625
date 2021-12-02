# -*- coding: utf-8 -*-
"""
Created on Thu Nov 11 17:13:28 2021

@author: Nakagawa kanta
"""

import streamlit as st

st.title('あなたに推したい水族館')

st.write("こんにちは。推したい水族館へようこそ。")
st.write("ここでは、私、館長があなたの質問の答えからあなたへ素敵な水族館をお教えします。")
st.write("ぜひ一度足をお運びいただけると幸いです。")
st.write("～～～あなたにとって思い出となる水族館との出会いがありますように。～～～")
from PIL import Image
img=Image.open("iruka.png")
st.image(img,caption="",use_column_width=True)

genre = st.radio(
     "この中であなたの最も好きな魚・動物は？",
  ('ペンギン', 'クラゲ', 'イルカ',"チンアナゴ","ジンベエザメ"))

if genre == 'ペンギン':
    n1 = 1
elif genre == 'クラゲ':
    n1 = 2
elif genre == 'イルカ':
    n1 = 3
elif genre == 'チンアナゴ':
    n1 = 4
elif genre == 'ジンベエザメ':
    n1 = 5




condition=st.slider("選んだ魚・動物の好きの度合いは？",1,5,3)
"好き度：",condition

if condition == 1:
    n2 = n1 + 10
elif condition == 2:
    n2 = n1 + 20
elif condition == 3:
    n2 = n1 + 30
elif condition == 4:
    n2 = n1 + 40
elif condition == 5:
    n2 = n1 + 50

genre = st.radio(
     "誰と水族館に行きたいですか？",
     ('家族or恋人', "一人"))
if genre == '家族or恋人':
    n3 = n2 + 100
elif genre == '一人':
    n3 = n2 + 200

button = st.button('素敵な水族館への扉を開いてみる')
if button:
    if n3 == 111:
        st.subheader('あなたにおすすめの水族館はサンシャイン水族館です。')
        from PIL import Image
        img=Image.open("SUN.jpg")
        st.image(img,caption="実際の写真",use_column_width=True)
        st.write("営業時間は９時３０分から２２時００分です。")
        st.write("この水族館がある県は東京都です。")
        st.write("左のサイドバーからサイトを閲覧することができます。")
        st.write("ぜひ一度行ってみてくださいね。")
        link = '[MYRECOMMENDAQUARIUM](https://sunshinecity.jp/aquarium/)'
        st.sidebar.markdown(link, unsafe_allow_html=True)
        st.sidebar.write('水族館に興味を持った方はご参照ください')
        st.balloons()
        from PIL import Image
        img=Image.open("PEN.png")
        st.sidebar.image(img,caption="",use_column_width=True)
        from PIL import Image
        img=Image.open("jj.jpg")
        st.image(img,caption="",use_column_width=True)
    
    elif n3 == 112:
        st.subheader('あなたにおすすめの水族館はなぎさ水族館です。')
        from PIL import Image
        img=Image.open("NAGI.jpg")
        st.image(img,caption="実際の写真",use_column_width=True)
        st.write("営業時間は９時００分から１６時３０分です。")
        st.write("この水族館がある県は山口県です。")
        st.write("左のサイドバーからサイトを閲覧することができます。")
        st.write("ぜひ一度行ってみてくださいね。")
        link = '[MYRECOMMENDAQUARIUM](https://nagisapark.jimdofree.com/%E3%81%AA%E3%81%8E%E3%81%95%E6%B0%B4%E6%97%8F%E9%A4%A8/)'
        st.sidebar.markdown(link, unsafe_allow_html=True)
        st.sidebar.write('水族館に興味を持った方はご参照ください')
        st.balloons()
        st.sidebar.image(img,caption="",use_column_width=True)
        from PIL import Image
        img=Image.open("KKK.jpg")
        st.image(img,caption="",use_column_width=True)
        
    elif n3 == 113:
        st.subheader('あなたにおすすめの水族館はうみがたりです。')
        from PIL import Image
        img=Image.open("UMI.jpg")
        st.image(img,caption="実際の写真",use_column_width=True)
        st.write("営業時間は１０時００分から１７時００分です。")
        st.write("この水族館がある県は新潟県です。")
        st.write("左のサイドバーからサイトを閲覧することができます。")
        st.write("ぜひ一度行ってみてくださいね。")
        link = '[MYRECOMMENDAQUARIUM](http://www.umigatari.jp/joetsu/index.html)'
        st.sidebar.markdown(link, unsafe_allow_html=True)
        st.sidebar.write('水族館に興味を持った方はご参照ください')
        st.balloons()
        img=Image.open("PEN.png")
        st.sidebar.image(img,caption="",use_column_width=True)
        from PIL import Image
        img=Image.open("B.jpg")
        st.image(img,caption="",use_column_width=True)
        
    elif n3 == 114:
        st.subheader('あなたにおすすめの水族館は沼津港深海水族館です。')
        from PIL import Image
        img=Image.open("NUMA.jpg")
        st.image(img,caption="実際の写真",use_column_width=True)
        st.write("営業時間は１０時００分から１８時００分です。")
        st.write("この水族館がある県は静岡県です。")
        st.write("左のサイドバーからサイトを閲覧することができます。")
        st.write("ぜひ一度行ってみてくださいね。")
        link = '[MYRECOMMENDAQUARIUM](http://www.numazu-deepsea.com/)'
        st.sidebar.markdown(link, unsafe_allow_html=True)
        st.sidebar.write('水族館に興味を持った方はご参照ください')
        st.balloons()
        img=Image.open("PEN.png")
        st.sidebar.image(img,caption="",use_column_width=True)
        from PIL import Image
        img=Image.open("E.jpg")
        st.image(img,caption="",use_column_width=True)
        
    elif n3 == 115:
        st.subheader('あなたにおすすめの水族館はいおワールドかごしま水族館です。')
        from PIL import Image
        img=Image.open("IO.jpg")
        st.image(img,caption="実際の写真",use_column_width=True)
        st.write("営業時間は９時３０分から１８時００分です。")
        st.write("この水族館がある県は鹿児島県です。")
        st.write("左のサイドバーからサイトを閲覧することができます。")
        st.write("ぜひ一度行ってみてくださいね。")
        link = '[MYRECOMMENDAQUARIUM](http://ioworld.jp/)'
        st.sidebar.markdown(link, unsafe_allow_html=True)
        st.sidebar.write('水族館に興味を持った方はご参照ください')
        st.balloons()
        img=Image.open("PEN.png")
        st.sidebar.image(img,caption="",use_column_width=True)
        from PIL import Image
        img=Image.open("MAMA.jpg")
        st.image(img,caption="",use_column_width=True)
        
    elif n3 == 121:
        st.subheader('あなたにおすすめの水族館はうみがたりです。')
        from PIL import Image
        img=Image.open("UMIUMI.jpg")
        st.image(img,caption="実際の写真",use_column_width=True)
        st.write("営業時間は１０時００分から１７時００分です。")
        st.write("この水族館がある県は新潟県です。")
        st.write("左のサイドバーからサイトを閲覧することができます。")
        st.write("ぜひ一度行ってみてくださいね。")
        link = '[MYRECOMMENDAQUARIUM](http://www.umigatari.jp/joetsu/index.html)'
        st.sidebar.markdown(link, unsafe_allow_html=True)
        st.sidebar.write('水族館に興味を持った方はご参照ください')
        st.balloons()
        img=Image.open("PEN.png")
        st.sidebar.image(img,caption="",use_column_width=True)
        from PIL import Image
        img=Image.open("RAIRA.jpg")
        st.image(img,caption="",use_column_width=True)
        
    elif n3 == 122:
        st.subheader('あなたにおすすめの水族館はのとじま水族館です。')
        from PIL import Image
        img=Image.open("NOTO.jpg")
        st.image(img,caption="実際の写真",use_column_width=True)
        st.write("営業時間は9時00分から16時30分です。")
        st.write("この水族館がある県は石川県です。")
        st.write("左のサイドバーからサイトを閲覧することができます。")
        st.write("ぜひ一度行ってみてくださいね。")
        link = '[MYRECOMMENDAQUARIUM](https://www.notoaqua.jp/)'
        st.sidebar.markdown(link, unsafe_allow_html=True)
        st.sidebar.write('水族館に興味を持った方はご参照ください')
        st.balloons()
        img=Image.open("PEN.png")
        st.sidebar.image(img,caption="",use_column_width=True)
        from PIL import Image
        img=Image.open("aaa.jpg")
        st.image(img,caption="",use_column_width=True)
        
    elif n3 == 123:
        st.subheader('あなたにおすすめの水族館は福井県越前松島水族館です。')
        from PIL import Image
        img=Image.open("ETI.jpg")
        st.image(img,caption="実際の写真",use_column_width=True)
        st.write("営業時間は9時00分から17時30分です。")
        st.write("この水族館がある県は石川県です。")
        st.write("左のサイドバーからサイトを閲覧することができます。")
        st.write("ぜひ一度行ってみてくださいね。")
        link = '[MYRECOMMENDAQUARIUM](https://www.echizen-aquarium.com/information/price.html)'
        st.sidebar.markdown(link, unsafe_allow_html=True)
        st.sidebar.write('水族館に興味を持った方はご参照ください')
        st.balloons()
        img=Image.open("PEN.png")
        st.sidebar.image(img,caption="",use_column_width=True)
        from PIL import Image
        img=Image.open("33.jpg")
        st.image(img,caption="",use_column_width=True)
   
    elif n3 == 124:
        st.subheader('あなたにおすすめの水族館は竹島水族館です。')
        from PIL import Image
        img=Image.open("TAKE.jpg")
        st.image(img,caption="実際の写真",use_column_width=True)
        st.write("営業時間は9時00分から17時00分です。")
        st.write("この水族館がある県は愛知県です。")
        st.write("左のサイドバーからサイトを閲覧することができます。")
        st.write("ぜひ一度行ってみてくださいね。")
        link = '[MYRECOMMENDAQUARIUM](https://www.city.gamagori.lg.jp/site/takesui/)'
        st.sidebar.markdown(link, unsafe_allow_html=True)
        st.sidebar.write('水族館に興味を持った方はご参照ください')
        st.balloons()
        img=Image.open("PEN.png")
        st.sidebar.image(img,caption="",use_column_width=True)
        from PIL import Image
        img=Image.open("PIE.jpg")
        st.image(img,caption="",use_column_width=True)
        
    elif n3 == 125:
        st.subheader('あなたにおすすめの水族館は海遊館です。')
        from PIL import Image
        img=Image.open("KAI.jpg")
        st.image(img,caption="実際の写真",use_column_width=True)
        st.write("営業時間は１０時００分から２０時００分です。")
        st.write("この水族館がある県は大阪府です。")
        st.write("左のサイドバーからサイトを閲覧することができます。")
        st.write("ぜひ一度行ってみてくださいね。")
        link = '[MYRECOMMENDAQUARIUM](https://www.kaiyukan.com/index.html)'
        st.sidebar.markdown(link, unsafe_allow_html=True)
        st.sidebar.write('水族館に興味を持った方はご参照ください')
        st.balloons()
        img=Image.open("PEN.png")
        st.sidebar.image(img,caption="",use_column_width=True)
        from PIL import Image
        img=Image.open("GO.jpg")
        st.image(img,caption="",use_column_width=True)
        
    elif n3 == 131:
        st.subheader('あなたにおすすめの水族館は海響館です。')
        from PIL import Image
        img=Image.open("KYOU.jpg")
        st.image(img,caption="実際の写真",use_column_width=True)
        st.write("営業時間は9時30分から17時30分です。")
        st.write("この水族館がある県は山口県です。")
        st.write("左のサイドバーからサイトを閲覧することができます。")
        st.write("ぜひ一度行ってみてくださいね。")
        link = '[MYRECOMMENDAQUARIUM](http://www.kaikyokan.com/)'
        st.sidebar.markdown(link, unsafe_allow_html=True)
        st.sidebar.write('水族館に興味を持った方はご参照ください')
        st.balloons()
        img=Image.open("PEN.png")
        st.sidebar.image(img,caption="",use_column_width=True)
        from PIL import Image
        img=Image.open("RUNjpg")
        st.image(img,caption="",use_column_width=True)
        
    elif n3 == 132:
        st.subheader('あなたにおすすめの水族館は新江ノ島水族館です。')
        from PIL import Image
        img=Image.open("SIN.jpg")
        st.image(img,caption="実際の写真",use_column_width=True)
        st.write("営業時間は９時００分から１７時００分です。")
        st.write("この水族館がある県は神奈川県です。")
        st.write("左のサイドバーからサイトを閲覧することができます。")
        st.write("ぜひ一度行ってみてくださいね。")
        link = '[MYRECOMMENDAQUARIUM](https://www.enosui.com/)'
        st.sidebar.markdown(link, unsafe_allow_html=True)
        st.sidebar.write('水族館に興味を持った方はご参照ください')
        st.balloons()
        img=Image.open("PEN.png")
        st.sidebar.image(img,caption="",use_column_width=True)
        from PIL import Image
        img=Image.open("KOI.jpg")
        st.image(img,caption="",use_column_width=True)
        
    elif n3 == 133:
        st.subheader('あなたにおすすめの水族館は仙台うみの杜水族館です。')
        from PIL import Image
        img=Image.open("MORI.jpg")
        st.image(img,caption="実際の写真",use_column_width=True)
        st.write("営業時間は９時００分から１７時３０分です。")
        st.write("この水族館がある県は宮城県です。")
        st.write("左のサイドバーからサイトを閲覧することができます。")
        st.write("ぜひ一度行ってみてくださいね。")
        link = '[MYRECOMMENDAQUARIUM](http://www.uminomori.jp/umino/index.html)'
        st.sidebar.markdown(link, unsafe_allow_html=True)
        st.sidebar.write('水族館に興味を持った方はご参照ください')
        st.balloons()
        img=Image.open("PEN.png")
        st.sidebar.image(img,caption="",use_column_width=True)
        from PIL import Image
        img=Image.open("DDD.jpg")
        st.image(img,caption="",use_column_width=True)
        
    elif n3 == 134:
        st.subheader('あなたにおすすめの水族館はNIFRELです。')
        from PIL import Image
        img=Image.open("NIFU.jpg")
        st.image(img,caption="実際の写真",use_column_width=True)
        st.write("営業時間は９時００分から２０時００分です。")
        st.write("この水族館がある県は大阪府です。")
        st.write("左のサイドバーからサイトを閲覧することができます。")
        st.write("ぜひ一度行ってみてくださいね。")
        link = '[MYRECOMMENDAQUARIUM](https://www.nifrel.jp/)'
        st.sidebar.markdown(link, unsafe_allow_html=True)
        st.sidebar.write('水族館に興味を持った方はご参照ください')
        st.balloons()
        from PIL import Image
        img=Image.open("HHH.jpg")
        st.image(img,caption="",use_column_width=True)
        img=Image.open("PEN.png")
        st.sidebar.image(img,caption="",use_column_width=True)
        
    elif n3 == 135:
        st.subheader('あなたにおすすめの水族館はのとじま水族館です。')
        from PIL import Image
        img=Image.open("JIMA.jpg")
        st.image(img,caption="実際の写真",use_column_width=True)
        st.write("営業時間は9時00分から16時30分です。")
        st.write("この水族館がある県は石川県です。")
        st.write("左のサイドバーからサイトを閲覧することができます。")
        st.write("ぜひ一度行ってみてくださいね。")
        link = '[MYRECOMMENDAQUARIUM](https://www.notoaqua.jp/)'
        st.sidebar.markdown(link, unsafe_allow_html=True)
        st.sidebar.write('水族館に興味を持った方はご参照ください')
        st.balloons()
        img=Image.open("LINE.jpg")
        st.image(img,caption="",use_column_width=True)
        img=Image.open("PEN.png")
        st.sidebar.image(img,caption="",use_column_width=True)
        
    elif n3 == 141:
        st.subheader('あなたにおすすめの水族館は名古屋湊水族館です。')
        from PIL import Image
        img=Image.open("KOU.jpg")
        st.image(img,caption="実際の写真",use_column_width=True)
        st.write("営業時間は9時00分から17時30分です。")
        st.write("この水族館がある県は愛知県です。")
        st.write("左のサイドバーからサイトを閲覧することができます。")
        st.write("ぜひ一度行ってみてくださいね。")
        link = '[MYRECOMMENDAQUARIUM](https://nagoyaaqua.jp/)'
        st.sidebar.markdown(link, unsafe_allow_html=True)
        st.sidebar.write('水族館に興味を持った方はご参照ください')
        st.balloons()
        from PIL import Image
        img=Image.open("KOARA.jpg")
        st.image(img,caption="",use_column_width=True)
        img=Image.open("PEN.png")
        st.sidebar.image(img,caption="",use_column_width=True)
        
    elif n3 == 142:
        st.subheader('あなたにおすすめの水族館はマリンピア日本海です。')
        from PIL import Image
        img=Image.open("LLL.jpg")
        st.image(img,caption="実際の写真",use_column_width=True)
        st.write("営業時間は９時００分から１７時００分です。")
        st.write("この水族館がある県は新潟県です。")
        st.write("左のサイドバーからサイトを閲覧することができます。")
        st.write("ぜひ一度行ってみてくださいね。")
        link = '[MYRECOMMENDAQUARIUM](https://www.marinepia.or.jp/)'
        st.sidebar.markdown(link, unsafe_allow_html=True)
        st.sidebar.write('水族館に興味を持った方はご参照ください')
        st.balloons()
        from PIL import Image
        img=Image.open("MANE.jpg")
        st.image(img,caption="",use_column_width=True)
        img=Image.open("PEN.png")
        st.sidebar.image(img,caption="",use_column_width=True)
        
    elif n3 == 143:
        st.subheader('あなたにおすすめの水族館は伊豆・三津シーパラダイスです。')
        from PIL import Image
        img=Image.open("MITO.jpg")
        st.image(img,caption="実際の写真",use_column_width=True)
        st.write("営業時間は９時００分から１７時００分です。")
        st.write("この水族館がある県は静岡県です。")
        st.write("左のサイドバーからサイトを閲覧することができます。")
        st.write("ぜひ一度行ってみてくださいね。")
        link = '[MYRECOMMENDAQUARIUM](http://www.izuhakone.co.jp/seapara)'
        st.sidebar.markdown(link, unsafe_allow_html=True)
        st.sidebar.write('水族館に興味を持った方はご参照ください')
        st.balloons()
        from PIL import Image
        img=Image.open("GIN.jpg")
        st.image(img,caption="",use_column_width=True)
        img=Image.open("PEN.png")
        st.sidebar.image(img,caption="",use_column_width=True)
        
    elif n3 == 144:
        st.subheader('あなたにおすすめの水族館はMみやじマリンです。')
        from PIL import Image
        img=Image.open("MIYA.jpg")
        st.image(img,caption="実際の写真",use_column_width=True)
        st.write("営業時間は9時00分から17時００分です。")
        st.write("この水族館がある県は広島県です。")
        st.write("左のサイドバーからサイトを閲覧することができます。")
        st.write("ぜひ一度行ってみてくださいね。")
        link = '[MYRECOMMENDAQUARIUM](https://miyajima-aqua.jp/)'
        st.sidebar.markdown(link, unsafe_allow_html=True)
        st.sidebar.write('水族館に興味を持った方はご参照ください')
        st.balloons()
        from PIL import Image
        img=Image.open("HARI.jpg")
        st.image(img,caption="",use_column_width=True)
        img=Image.open("PEN.png")
        st.sidebar.image(img,caption="",use_column_width=True)
        
    elif n3 == 145:
        st.subheader('あなたにおすすめの水族館はアクアワールドです。')
        from PIL import Image
        img=Image.open("AKUA.jpg")
        st.image(img,caption="実際の写真",use_column_width=True)
        st.write("営業時間は９時００分から１７時００分です。")
        st.write("この水族館がある県は茨城県です。")
        st.write("左のサイドバーからサイトを閲覧することができます。")
        st.write("ぜひ一度行ってみてくださいね。")
        link = '[MYRECOMMENDAQUARIUM](https://aqua-world.jp/)'
        st.sidebar.markdown(link, unsafe_allow_html=True)
        st.sidebar.write('水族館に興味を持った方はご参照ください')
        st.balloons()
        img=Image.open("9.jpg")
        st.image(img,caption="",use_column_width=True)
        img=Image.open("PEN.png")
        st.sidebar.image(img,caption="",use_column_width=True)
        
    elif n3 == 151:
        st.subheader('あなたにおすすめの水族館は長崎ペンギン水族館です。')
        from PIL import Image
        img=Image.open("A.jpg")
        st.image(img,caption="実際の写真",use_column_width=True)
        st.write("営業時間は9時00分から17時00分です。")
        st.write("この水族館がある県は長崎県です。")
        st.write("左のサイドバーからサイトを閲覧することができます。")
        st.write("ぜひ一度行ってみてくださいね。")
        link = '[MYRECOMMENDAQUARIUM](https://penguin-aqua.jp/)'
        st.sidebar.markdown(link, unsafe_allow_html=True)
        st.sidebar.write('水族館に興味を持った方はご参照ください')
        st.balloons()
        img=Image.open("KURU.jpg")
        st.image(img,caption="",use_column_width=True)
        img=Image.open("PEN.png")
        st.sidebar.image(img,caption="",use_column_width=True)
        
    elif n3 == 152:
        st.subheader('あなたにおすすめの水族館は加茂水族館です。')
        from PIL import Image
        img=Image.open("KAMO.jpg")
        st.image(img,caption="実際の写真",use_column_width=True)
        st.write("営業時間は９時００分から１７時００分です。")
        st.write("この水族館がある県は山形県です。")
        st.write("左のサイドバーからサイトを閲覧することができます。")
        st.write("ぜひ一度行ってみてくださいね。")
        link = '[MYRECOMMENDAQUARIUM](http://kamo-kurage.jp/)'
        st.sidebar.markdown(link, unsafe_allow_html=True)
        st.sidebar.write('水族館に興味を持った方はご参照ください')
        st.balloons()
        img=Image.open("YUIYUI.jpg")
        st.image(img,caption="",use_column_width=True)
        img=Image.open("PEN.png")
        st.sidebar.image(img,caption="",use_column_width=True)
        
    elif n3 == 153:
        st.subheader('あなたにおすすめの水族館は名古屋港水族館です。')
        from PIL import Image
        img=Image.open("Y.jpg")
        st.image(img,caption="実際の写真",use_column_width=True)
        st.write("営業時間は9時00分から17時30分です。")
        st.write("この水族館がある県は愛知県です。")
        st.write("左のサイドバーからサイトを閲覧することができます。")
        st.write("ぜひ一度行ってみてくださいね。")
        link = '[MYRECOMMENDAQUARIUM](https://nagoyaaqua.jp/)'
        st.sidebar.markdown(link, unsafe_allow_html=True)
        st.sidebar.write('水族館に興味を持った方はご参照ください')
        st.balloons()
        img=Image.open("PI.jpg")
        st.image(img,caption="",use_column_width=True)
        img=Image.open("PEN.png")
        st.sidebar.image(img,caption="",use_column_width=True)
        
    elif n3 == 154:
        st.subheader('あなたにおすすめの水族館はすみだ水族館です。')
        from PIL import Image
        img=Image.open("SUMI.jpg")
        st.image(img,caption="実際の写真",use_column_width=True)
        st.write("営業時間は10時00分から20時00分です。")
        st.write("この水族館がある県は東京都です。")
        st.write("左のサイドバーからサイトを閲覧することができます。")
        st.write("ぜひ一度行ってみてくださいね。")
        link = '[MYRECOMMENDAQUARIUM](https://www.sumida-aquarium.com/index.html)'
        st.sidebar.markdown(link, unsafe_allow_html=True)
        st.sidebar.write('水族館に興味を持った方はご参照ください')
        st.balloons()
        img=Image.open("KAN.jpg")
        st.image(img,caption="",use_column_width=True)
        img=Image.open("PEN.png")
        st.sidebar.image(img,caption="",use_column_width=True)
        
    elif n3 == 155:
        st.subheader('あなたにおすすめの水族館は美ら海水族館です。')
        from PIL import Image
        img=Image.open("TYURA.jpg")
        st.image(img,caption="実際の写真",use_column_width=True)
        st.write("営業時間は8時30分から17時30分です。")
        st.write("この水族館がある県は沖縄県です。")
        st.write("左のサイドバーからサイトを閲覧することができます。")
        st.write("ぜひ一度行ってみてくださいね。")
        link = '[MYRECOMMENDAQUARIUM](https://churaumi.okinawa/)'
        st.sidebar.markdown(link, unsafe_allow_html=True)
        st.sidebar.write('水族館に興味を持った方はご参照ください')
        st.balloons()
        img=Image.open("KANTA.jpg")
        st.image(img,caption="",use_column_width=True)
        img=Image.open("PEN.png")
        st.sidebar.image(img,caption="",use_column_width=True)
        
        
    elif n3 == 211:
        st.subheader('あなたにおすすめの水族館は海洋館アクアスです。')
        from PIL import Image
        img=Image.open("ASUKA.jpg")
        st.image(img,caption="実際の写真",use_column_width=True)
        st.write("営業時間は９時００分から１７時００分です。")
        st.write("この水族館がある県は島根県です。")
        st.write("左のサイドバーからサイトを閲覧することができます。")
        st.write("ぜひ一度行ってみてくださいね。")
        link = '[MYRECOMMENDAQUARIUM](https://aquas.or.jp/)'
        st.sidebar.markdown(link, unsafe_allow_html=True)
        st.sidebar.write('水族館に興味を持った方はご参照ください')
        st.balloons()
        img=Image.open("MIMI.jpg")
        st.image(img,caption="",use_column_width=True)
        img=Image.open("PEN.png")
        st.sidebar.image(img,caption="",use_column_width=True)
        
    elif n3 == 212:
        st.subheader('あなたにおすすめの水族館は長高水族館です。')
        from PIL import Image
        img=Image.open("NAGAKOU.jpg")
        st.image(img,caption="実際の写真",use_column_width=True)
        st.write("営業時間は１１時００分から１５時００分です。")
        st.write("この水族館がある県は愛媛県です。")
        st.write("左のサイドバーからサイトを閲覧することができます。")
        st.write("ぜひ一度行ってみてくださいね。")
        link = '[MYRECOMMENDAQUARIUM](https://nagakoaquarium.wixsite.com/home)'
        st.sidebar.markdown(link, unsafe_allow_html=True)
        st.sidebar.write('水族館に興味を持った方はご参照ください')
        st.balloons()
        img=Image.open("KIKI.jpg")
        st.image(img,caption="",use_column_width=True)
        img=Image.open("PEN.png")
        st.sidebar.image(img,caption="",use_column_width=True)
        
    elif n3 == 213:
        st.subheader('あなたにおすすめの水族館は浅虫水族館です。')
        from PIL import Image
        img=Image.open("ASA.jpg")
        st.image(img,caption="実際の写真",use_column_width=True)
        st.write("営業時間は9時00分から17時00分です。")
        st.write("この水族館がある県は青森県です。")
        st.write("左のサイドバーからサイトを閲覧することができます。")
        st.write("ぜひ一度行ってみてくださいね。")
        link = '[MYRECOMMENDAQUARIUM](http://asamushi-aqua.com/)'
        st.sidebar.markdown(link, unsafe_allow_html=True)
        st.sidebar.write('水族館に興味を持った方はご参照ください')
        st.balloons()
        img=Image.open("TON.jpg")
        st.image(img,caption="",use_column_width=True)
        img=Image.open("PEN.png")
        st.sidebar.image(img,caption="",use_column_width=True)
        
    elif n3 == 214:
        st.subheader('あなたにおすすめの水族館は沼津港深海水族館です。')
        from PIL import Image
        img=Image.open("NUMA.jpg")
        st.image(img,caption="実際の写真",use_column_width=True)
        st.write("営業時間は１０時００分から１８時００分です。")
        st.write("この水族館がある県は静岡県です。")
        st.write("左のサイドバーからサイトを閲覧することができます。")
        st.write("ぜひ一度行ってみてくださいね。")
        link = '[MYRECOMMENDAQUARIUM](http://www.numazu-deepsea.com/)'
        st.sidebar.markdown(link, unsafe_allow_html=True)
        st.sidebar.write('水族館に興味を持った方はご参照ください')
        st.balloons()
        img=Image.open("PIP.jpg")
        st.image(img,caption="",use_column_width=True)
        img=Image.open("PEN.png")
        st.sidebar.image(img,caption="",use_column_width=True)
        
    elif n3 == 215:
       st.subheader('あなたにおすすめの水族館はいおワールドかごしま水族館です。')
       from PIL import Image
       img=Image.open("IO.jpg")
       st.image(img,caption="実際の写真",use_column_width=True)
       st.write("営業時間は９時３０分から１８時００分です。")
       st.write("この水族館がある県は鹿児島県です。")
       st.write("左のサイドバーからサイトを閲覧することができます。")
       st.write("ぜひ一度行ってみてくださいね。")
       link = '[MYRECOMMENDAQUARIUM](http://ioworld.jp/)'
       st.sidebar.markdown(link, unsafe_allow_html=True)
       st.sidebar.write('水族館に興味を持った方はご参照ください')
       st.balloons()
       img=Image.open("HASI.jpg")
       st.image(img,caption="",use_column_width=True)
       img=Image.open("PEN.png")
       st.sidebar.image(img,caption="",use_column_width=True)
        
    elif n3 == 221:
        st.subheader('あなたにおすすめの水族館はうみたまごです。')
        from PIL import Image
        img=Image.open("KK.jpg")
        st.image(img,caption="実際の写真",use_column_width=True)
        st.write("営業時間は９時００分から１７時00分です。")
        st.write("この水族館がある県は大分県です。")
        st.write("左のサイドバーからサイトを閲覧することができます。")
        st.write("ぜひ一度行ってみてくださいね。")
        link = '[MYRECOMMENDAQUARIUM](https://www.umitamago.jp/)'
        st.sidebar.markdown(link, unsafe_allow_html=True)
        st.sidebar.write('水族館に興味を持った方はご参照ください')
        st.balloons()
        img=Image.open("JA.jpg")
        st.image(img,caption="",use_column_width=True)
        img=Image.open("PEN.png")
        st.sidebar.image(img,caption="",use_column_width=True)
        
    elif n3 == 222:
        st.subheader('あなたにおすすめの水族館は海きららです。')
        from PIL import Image
        img=Image.open("KURAKU.jpg")
        st.image(img,caption="実際の写真",use_column_width=True)
        st.write("営業時間は9時00分から18時00分です。")
        st.write("この水族館がある県は長崎県です。")
        st.write("左のサイドバーからサイトを閲覧することができます。")
        st.write("ぜひ一度行ってみてくださいね。")
        link = '[MYRECOMMENDAQUARIUM](https://umikirara.jp/)'
        st.sidebar.markdown(link, unsafe_allow_html=True)
        st.sidebar.write('水族館に興味を持った方はご参照ください')
        st.balloons()
        img=Image.open("KIMIKA.jpg")
        st.image(img,caption="",use_column_width=True)
        img=Image.open("PEN.png")
        st.sidebar.image(img,caption="",use_column_width=True)
        
    elif n3 == 223:
        st.subheader('あなたにおすすめの水族館は南知多ビーチランドです。')
        from PIL import Image
        img=Image.open("OO.jpg")
        st.image(img,caption="実際の写真",use_column_width=True)
        st.write("営業時間は９時００分から１８時００分です。")
        st.write("この水族館がある県はです。")
        st.write("左のサイドバーからサイトを閲覧することができます。")
        st.write("ぜひ一度行ってみてくださいね。")
        link = '[MYRECOMMENDAQUARIUM]()'
        st.sidebar.markdown(link, unsafe_allow_html=True)
        st.sidebar.write('水族館に興味を持った方はご参照ください')
        st.balloons()
        img=Image.open("OMAMA.jpg")
        st.image(img,caption="",use_column_width=True)
        img=Image.open("PEN.png")
        st.sidebar.image(img,caption="",use_column_width=True)
        
    elif n3 == 224:
        st.subheader('あなたにおすすめの水族館は京都水族館です。')
        from PIL import Image
        img=Image.open("K.jpg")
        st.image(img,caption="実際の写真",use_column_width=True)
        st.write("営業時間は９時００分から１７時００分です。")
        st.write("この水族館がある県は京都府です。")
        st.write("左のサイドバーからサイトを閲覧することができます。")
        st.write("ぜひ一度行ってみてくださいね。")
        link = '[MYRECOMMENDAQUARIUM](https://www.kyoto-aquarium.com/index.htm)'
        st.sidebar.markdown(link, unsafe_allow_html=True)
        st.sidebar.write('水族館に興味を持った方はご参照ください')
        st.balloons()
        img=Image.open("KIKO.jpg")
        st.image(img,caption="",use_column_width=True)
        img=Image.open("PEN.png")
        st.sidebar.image(img,caption="",use_column_width=True)
        
    elif n3 == 225:
        st.subheader('あなたにおすすめの水族館はのとじま水族館です。')
        from PIL import Image
        img=Image.open("JIMA.jpg")
        st.image(img,caption="実際の写真",use_column_width=True)
        st.write("営業時間は9時00分から16時30分です。")
        st.write("この水族館がある県は石川県です。")
        st.write("左のサイドバーからサイトを閲覧することができます。")
        st.write("ぜひ一度行ってみてくださいね。")
        link = '[MYRECOMMENDAQUARIUM](https://www.notoaqua.jp/)'
        st.sidebar.markdown(link, unsafe_allow_html=True)
        st.sidebar.write('水族館に興味を持った方はご参照ください')
        st.balloons()
        from PIL import Image
        img=Image.open("iruka.png")
        st.image(img,caption="",use_column_width=True)
        img=Image.open("PEN.png")
        st.sidebar.image(img,caption="",use_column_width=True)
        
    elif n3 == 231:
        st.subheader('あなたにおすすめの水族館はマリンワールド海の中道です。')
        from PIL import Image
        img=Image.open("YORU.jpg")
        st.image(img,caption="実際の写真",use_column_width=True)
        st.write("営業時間は１０時００分から１７時００分です。")
        st.write("この水族館がある県は福岡県です。")
        st.write("左のサイドバーからサイトを閲覧することができます。")
        st.write("ぜひ一度行ってみてくださいね。")
        link = '[MYRECOMMENDAQUARIUM]()'
        st.sidebar.markdown(link, unsafe_allow_html=True)
        st.sidebar.write('水族館に興味を持った方はご参照ください')
        st.balloons()
        from PIL import Image
        img=Image.open("iruka.png")
        st.image(img,caption="",use_column_width=True)
        img=Image.open("PEN.png")
        st.sidebar.image(img,caption="",use_column_width=True)
        
    elif n3 == 232:
        st.subheader('あなたにおすすめの水族館は下田海中水族館です。')
        from PIL import Image
        img=Image.open("Ｓ.jpg")
        st.image(img,caption="実際の写真",use_column_width=True)
        st.write("営業時間は9時00分から17時30分です。")
        st.write("この水族館がある県は静岡県です。")
        st.write("左のサイドバーからサイトを閲覧することができます。")
        st.write("ぜひ一度行ってみてくださいね。")
        link = '[MYRECOMMENDAQUARIUM](https://shimoda-aquarium.com/)'
        st.sidebar.markdown(link, unsafe_allow_html=True)
        st.sidebar.write('水族館に興味を持った方はご参照ください')
        st.balloons()
        from PIL import Image
        img=Image.open("iruka.png")
        st.image(img,caption="",use_column_width=True)
        img=Image.open("PEN.png")
        st.sidebar.image(img,caption="",use_column_width=True)
        
    elif n3 == 233:
        st.subheader('あなたにおすすめの水族館は鳥羽水族館です。')
        from PIL import Image
        img=Image.open("H.jpg")
        st.image(img,caption="実際の写真",use_column_width=True)
        st.write("営業時間は９時００分から１７時００分です。")
        st.write("この水族館がある県は三重県です。")
        st.write("左のサイドバーからサイトを閲覧することができます。")
        st.write("ぜひ一度行ってみてくださいね。")
        link = '[MYRECOMMENDAQUARIUM](https://www.aquarium.co.jp/)'
        st.sidebar.markdown(link, unsafe_allow_html=True)
        st.sidebar.write('水族館に興味を持った方はご参照ください')
        from PIL import Image
        img=Image.open("iruka.png")
        st.image(img,caption="",use_column_width=True)
        img=Image.open("PEN.png")
        st.sidebar.image(img,caption="",use_column_width=True)
        
    elif n3 == 234:
        st.subheader('あなたにおすすめの水族館はおたる水族館です。')
        from PIL import Image
        img=Image.open("DEBU.jpg")
        st.image(img,caption="実際の写真",use_column_width=True)
        st.write("営業時間は10時00分から16時00分です。")
        st.write("この水族館がある県は北海道です。")
        st.write("左のサイドバーからサイトを閲覧することができます。")
        st.write("ぜひ一度行ってみてくださいね。")
        link = '[MYRECOMMENDAQUARIUM](https://otaru-aq.jp/)'
        st.sidebar.markdown(link, unsafe_allow_html=True)
        st.sidebar.write('水族館に興味を持った方はご参照ください')
        st.balloons()
        from PIL import Image
        img=Image.open("iruka.png")
        st.image(img,caption="",use_column_width=True)
        img=Image.open("PEN.png")
        st.sidebar.image(img,caption="",use_column_width=True)
        
    elif n3 == 235:
        st.subheader('あなたにおすすめの水族館はアクアワールドです。')
        from PIL import Image
        img=Image.open("AKUA.jpg")
        st.image(img,caption="実際の写真",use_column_width=True)
        st.write("営業時間は９時００分から１７時００分です。")
        st.write("この水族館がある県は茨城県です。")
        st.write("左のサイドバーからサイトを閲覧することができます。")
        st.write("ぜひ一度行ってみてくださいね。")
        link = '[MYRECOMMENDAQUARIUM](https://aqua-world.jp/)'
        st.sidebar.markdown(link, unsafe_allow_html=True)
        st.sidebar.write('水族館に興味を持った方はご参照ください')
        st.balloons()
        from PIL import Image
        img=Image.open("iruka.png")
        st.image(img,caption="",use_column_width=True)
        img=Image.open("PEN.png")
        st.sidebar.image(img,caption="",use_column_width=True)
        
    elif n3 == 241:
        st.subheader('あなたにおすすめの水族館は城崎マリンワールドです。')
        from PIL import Image
        img=Image.open("KINO.jpg")
        st.image(img,caption="実際の写真",use_column_width=True)
        st.write("営業時間は時分から時分です。")
        st.write("この水族館がある県はです。")
        st.write("左のサイドバーからサイトを閲覧することができます。")
        st.write("ぜひ一度行ってみてくださいね。")
        link = '[MYRECOMMENDAQUARIUM]()'
        st.sidebar.markdown(link, unsafe_allow_html=True)
        st.sidebar.write('水族館に興味を持った方はご参照ください')
        st.balloons()
        from PIL import Image
        img=Image.open("iruka.png")
        st.image(img,caption="",use_column_width=True)
        img=Image.open("PEN.png")
        st.sidebar.image(img,caption="",use_column_width=True)
        
    elif n3 == 242:
        st.subheader('あなたにおすすめの水族館はのとじま水族館です。')
        from PIL import Image
        img=Image.open("JIMA.jpg")
        st.image(img,caption="実際の写真",use_column_width=True)
        st.write("営業時間は9時00分から16時30分です。")
        st.write("この水族館がある県は石川県です。")
        st.write("左のサイドバーからサイトを閲覧することができます。")
        st.write("ぜひ一度行ってみてくださいね。")
        link = '[MYRECOMMENDAQUARIUM](https://www.notoaqua.jp/)'
        st.sidebar.markdown(link, unsafe_allow_html=True)
        st.sidebar.write('水族館に興味を持った方はご参照ください')
        st.balloons()
        from PIL import Image
        img=Image.open("iruka.png")
        st.image(img,caption="",use_column_width=True)
        img=Image.open("PEN.png")
        st.sidebar.image(img,caption="",use_column_width=True)
        
    elif n3 == 243:
        st.subheader('あなたにおすすめの水族館は横浜八景島シーパラダイスです。')
        from PIL import Image
        img=Image.open("HAKE.jpg")
        st.image(img,caption="実際の写真",use_column_width=True)
        st.write("営業時間は１０時００分から１７時００分です。")
        st.write("この水族館がある県は神奈川県です。")
        st.write("左のサイドバーからサイトを閲覧することができます。")
        st.write("ぜひ一度行ってみてくださいね。")
        link = '[MYRECOMMENDAQUARIUM](http://www.seaparadise.co.jp/)'
        st.sidebar.markdown(link, unsafe_allow_html=True)
        st.sidebar.write('水族館に興味を持った方はご参照ください')
        st.balloons()
        from PIL import Image
        img=Image.open("iruka.png")
        st.image(img,caption="",use_column_width=True)
        img=Image.open("PEN.png")
        st.sidebar.image(img,caption="",use_column_width=True)
        
    elif n3 == 244:
        st.subheader('あなたにおすすめの水族館はすみだ水族館です。')
        from PIL import Image
        img=Image.open("SUMI.jpg")
        st.image(img,caption="実際の写真",use_column_width=True)
        st.write("営業時間は10時00分から20時00分です。")
        st.write("この水族館がある県は東京都です。")
        st.write("左のサイドバーからサイトを閲覧することができます。")
        st.write("ぜひ一度行ってみてくださいね。")
        link = '[MYRECOMMENDAQUARIUM](https://www.sumida-aquarium.com/index.html)'
        st.sidebar.markdown(link, unsafe_allow_html=True)
        st.sidebar.write('水族館に興味を持った方はご参照ください')
        st.balloons()
        from PIL import Image
        img=Image.open("iruka.png")
        st.image(img,caption="",use_column_width=True)
        img=Image.open("PEN.png")
        st.sidebar.image(img,caption="",use_column_width=True)
        
    elif n3 == 245:
        st.subheader('あなたにおすすめの水族館は海遊館です。')
        from PIL import Image
        img=Image.open("KAI.jpg")
        st.image(img,caption="実際の写真",use_column_width=True)
        st.write("営業時間は１０時００分から２０時００分です。")
        st.write("この水族館がある県は大阪府です。")
        st.write("左のサイドバーからサイトを閲覧することができます。")
        st.write("ぜひ一度行ってみてくださいね。")
        link = '[MYRECOMMENDAQUARIUM](https://www.kaiyukan.com/index.html)'
        st.sidebar.markdown(link, unsafe_allow_html=True)
        st.sidebar.write('水族館に興味を持った方はご参照ください')
        st.balloons()
        from PIL import Image
        img=Image.open("iruka.png")
        st.image(img,caption="",use_column_width=True)
        img=Image.open("PEN.png")
        st.sidebar.image(img,caption="",use_column_width=True)
        
    
        
    elif n3 == 251:
        st.subheader('あなたにおすすめの水族館は長崎ペンギン水族館です。')
        from PIL import Image
        img=Image.open("A.jpg")
        st.image(img,caption="実際の写真",use_column_width=True)
        st.write("営業時間は9時00分から17時00分です。")
        st.write("この水族館がある県は長崎県です。")
        st.write("左のサイドバーからサイトを閲覧することができます。")
        st.write("ぜひ一度行ってみてくださいね。")
        link = '[MYRECOMMENDAQUARIUM](https://penguin-aqua.jp/)'
        st.sidebar.markdown(link, unsafe_allow_html=True)
        st.sidebar.write('水族館に興味を持った方はご参照ください')
        st.balloons()
        from PIL import Image
        img=Image.open("iruka.png")
        st.image(img,caption="",use_column_width=True)
        img=Image.open("PEN.png")
        st.sidebar.image(img,caption="",use_column_width=True)
        
    elif n3 == 252:
        st.subheader('あなたにおすすめの水族館は加茂水族館です。')
        from PIL import Image
        img=Image.open("KAMO.jpg")
        st.image(img,caption="実際の写真",use_column_width=True)
        st.write("営業時間は９時００分から１７時００分です。")
        st.write("この水族館がある県は山形県です。")
        st.write("左のサイドバーからサイトを閲覧することができます。")
        st.write("ぜひ一度行ってみてくださいね。")
        link = '[MYRECOMMENDAQUARIUM](http://kamo-kurage.jp/)'
        st.sidebar.markdown(link, unsafe_allow_html=True)
        st.sidebar.write('水族館に興味を持った方はご参照ください')
        st.balloons()
        from PIL import Image
        img=Image.open("iruka.png")
        st.image(img,caption="",use_column_width=True)
        img=Image.open("PEN.png")
        st.sidebar.image(img,caption="",use_column_width=True)
        
        
    elif n3 == 253:
        st.subheader('あなたにおすすめの水族館はアクアパーク品川です。')
        from PIL import Image
        img=Image.open("SINA.jpg")
        st.image(img,caption="実際の写真",use_column_width=True)
        st.write("営業時間は10時00分から18時00分です。")
        st.write("この水族館がある県は東京都です。")
        st.write("左のサイドバーからサイトを閲覧することができます。")
        st.write("ぜひ一度行ってみてくださいね。")
        link = '[MYRECOMMENDAQUARIUM](http://www.aqua-park.jp/aqua/index.htm)'
        st.sidebar.markdown(link, unsafe_allow_html=True)
        st.sidebar.write('水族館に興味を持った方はご参照ください')
        st.balloons()
        from PIL import Image
        img=Image.open("iruka.png")
        st.image(img,caption="",use_column_width=True)
        img=Image.open("PEN.png")
        st.sidebar.image(img,caption="",use_column_width=True)
        
    elif n3 == 254:
        st.subheader('あなたにおすすめの水族館は伊豆・三津シーパラダイスです。')
        from PIL import Image
        img=Image.open("MITO.jpg")
        st.image(img,caption="実際の写真",use_column_width=True)
        st.write("営業時間は９時００分から１７時００分です。")
        st.write("この水族館がある県は静岡県です。")
        st.write("左のサイドバーからサイトを閲覧することができます。")
        st.write("ぜひ一度行ってみてくださいね。")
        link = '[MYRECOMMENDAQUARIUM](http://www.izuhakone.co.jp/seapara)'
        st.sidebar.markdown(link, unsafe_allow_html=True)
        st.sidebar.write('水族館に興味を持った方はご参照ください')
        st.balloons()
        from PIL import Image
        img=Image.open("iruka.png")
        st.image(img,caption="",use_column_width=True)
        img=Image.open("PEN.png")
        st.sidebar.image(img,caption="",use_column_width=True)
        
    elif n3 == 255:
        st.subheader('あなたにおすすめの水族館は美ら海水族館です。')
        from PIL import Image
        img=Image.open("TYURA.jpg")
        st.image(img,caption="実際の写真",use_column_width=True)
        st.write("営業時間は8時30分から17時30分です。")
        st.write("この水族館がある県は沖縄県です。")
        st.write("左のサイドバーからサイトを閲覧することができます。")
        st.write("ぜひ一度行ってみてくださいね。")
        link = '[MYRECOMMENDAQUARIUM](https://churaumi.okinawa/)'
        st.sidebar.markdown(link, unsafe_allow_html=True)
        st.sidebar.write('水族館に興味を持った方はご参照ください')
        st.balloons()
        from PIL import Image
        img=Image.open("iruka.png")
        st.image(img,caption="",use_column_width=True)
        
        
  