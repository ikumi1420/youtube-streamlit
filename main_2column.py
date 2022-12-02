import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image

st.title('Streamlit 超入門')

st.write('DataFrame')

df = pd.DataFrame({
    '1列目':[1,2,3,4],
    '2列目':[10,20,30,40],
    })

st.write('動的な表')

#動的な表
st.dataframe(df.style.highlight_max(axis=0), width=500, height=200)

st.write('静的な表')

#静的な表（staticな表。ただ単に表を表示させたい）
st.table(df.style.highlight_max(axis=0))

"""
# 章
## 節
### 項
```python
import Streamlit as st
import numpy as np
import pandas as pd
```
"""


#折れ線グラフ、チャート
#縦に20個、横に3個　乱数を生成

st.write('折れ線グラフ、チャート')

df = pd.DataFrame(
    np.random.rand(20,3),
    columns=['a','b','c']
)

st.line_chart(df)


#エリアチャート
st.write('エリアチャート')

df = pd.DataFrame(
    np.random.rand(20,3),
    columns=['a','b','c']
)

st.area_chart(df)


#バーチャート、棒グラフ
st.write('バーチャート、棒グラフ')

df = pd.DataFrame(
    np.random.rand(20,3),
    columns=['a','b','c']
)

st.bar_chart(df)

#Mapのプロット
#緯度と経度
st.write('緯度と経度　マップのプロット')

df = pd.DataFrame(
    np.random.rand(100, 2)/[50, 50] + [35.69, 139.70],
    columns=['lat','lon']
)

st.map(df)


#画像を表示させる
st.write('Display Image')

img = Image.open('tech0-logo2.png')

#レイアウトに合わせた幅で表示
st.image(img, caption='tech0-logo2', use_column_width=True)


#チェックBOX
st.write('チェックBOXを表示させて、選択したものが文中に反映される')

if st.checkbox('Show Image'):
    img = Image.open('tech0-logo2.png')
    st.image(img, caption='tech0-logo2', use_column_width=True)

#セレクトBOX

option = st.selectbox(
    'あなたが好きな数字を教えてください。',
    list(range(1,11))
)
'あなたの好きな数字は、', option, 'です'

#インタラクティブなウィジェット(値、テキストを変えると反映される)
st.write('Interactive Widgets: テキスト')

#テキストBOX
#text = st.text_input('あなたの趣味を教えてください')
#'あなたの趣味は、', text, 'です'


#スライダー（値を変えると反映される)
#st.write('Interactive Widgets: スライダー')

#condition = st.slider('あなたの今の調子は？', 0, 100, 50)
#'コンディション:', condition


#サイドバーへの追加(sidebar)

text = st.sidebar.text_input('あなたの趣味を教えてください')
condition = st.sidebar.slider('あなたの今の調子は？', 0, 100, 50)


#表示させたい文章はサイドバーに追加しない
'あなたの趣味:', text
'コンディション:', condition


#ボタンクリックしたら出てくる

st.write('ボタンクリックしたら出てくる')


left_column, right_column = st.columns(2)

button = left_column.button('右カラムに文字を表示')
if button:
    right_column.write('ここは右カラム')


#FAQなどでよく見かける形（エクスパンダー）

st.write('FAQなどでよく見かける形（エクスパンダー)')
    
expander1 = st.expander('問い合わせ1')
expander1.write('問い合わせ1の回答')
expander2 = st.expander('問い合わせ2')
expander2.write('問い合わせ2の回答')
expander3 = st.expander('問い合わせ3')
expander3.write('問い合わせ3の回答')
expander4 = st.expander('問い合わせ4')
expander4.write('問い合わせ4の回答')




import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image

st.title('Streamlit 超入門')

st.write('DataFrame')

df = pd.DataFrame({
    '1列目':[1,2,3,4],
    '2列目':[10,20,30,40],
    })

st.write('動的な表')

#動的な表
st.dataframe(df.style.highlight_max(axis=0), width=500, height=200)

st.write('静的な表')

#静的な表（staticな表。ただ単に表を表示させたい）
st.table(df.style.highlight_max(axis=0))

"""
# 章
## 節
### 項
```python
import Streamlit as st
import numpy as np
import pandas as pd
```
"""


#折れ線グラフ、チャート
#縦に20個、横に3個　乱数を生成

st.write('折れ線グラフ、チャート')

df = pd.DataFrame(
    np.random.rand(20,3),
    columns=['a','b','c']
)

st.line_chart(df)


#エリアチャート
st.write('エリアチャート')

df = pd.DataFrame(
    np.random.rand(20,3),
    columns=['a','b','c']
)

st.area_chart(df)


#バーチャート、棒グラフ
st.write('バーチャート、棒グラフ')

df = pd.DataFrame(
    np.random.rand(20,3),
    columns=['a','b','c']
)

st.bar_chart(df)

#Mapのプロット
#緯度と経度
st.write('緯度と経度　マップのプロット')

df = pd.DataFrame(
    np.random.rand(100, 2)/[50, 50] + [35.69, 139.70],
    columns=['lat','lon']
)

st.map(df)


#画像を表示させる
st.write('Display Image')

img = Image.open('tech0-logo2.png')

#レイアウトに合わせた幅で表示
st.image(img, caption='tech0-logo2', use_column_width=True)


#チェックBOX
st.write('チェックBOXを表示させて、選択したものが文中に反映される')

if st.checkbox('Show Image'):
    img = Image.open('tech0-logo2.png')
    st.image(img, caption='tech0-logo2', use_column_width=True)

#セレクトBOX

option = st.selectbox(
    'あなたが好きな数字を教えてください。',
    list(range(1,11))
)
'あなたの好きな数字は、', option, 'です'

#インタラクティブなウィジェット(値、テキストを変えると反映される)
st.write('Interactive Widgets: テキスト')

#テキストBOX
#text = st.text_input('あなたの趣味を教えてください')
#'あなたの趣味は、', text, 'です'


#スライダー（値を変えると反映される)
#st.write('Interactive Widgets: スライダー')

#condition = st.slider('あなたの今の調子は？', 0, 100, 50)
#'コンディション:', condition


#サイドバーへの追加(sidebar)

text = st.sidebar.text_input('あなたの趣味を教えてください')
condition = st.sidebar.slider('あなたの今の調子は？', 0, 100, 50)


#表示させたい文章はサイドバーに追加しない
'あなたの趣味:', text
'コンディション:', condition


#ボタンクリックしたら出てくる

st.write('ボタンクリックしたら出てくる')


left_column, right_column = st.columns(2)

button = left_column.button('右カラムに文字を表示')
if button:
    right_column.write('ここは右カラム')


#FAQなどでよく見かける形（エクスパンダー）

st.write('FAQなどでよく見かける形（エクスパンダー)')
    
expander1 = st.expander('問い合わせ1')
expander1.write('問い合わせ1の回答')
expander2 = st.expander('問い合わせ2')
expander2.write('問い合わせ2の回答')
expander3 = st.expander('問い合わせ3')
expander3.write('問い合わせ3の回答')
expander4 = st.expander('問い合わせ4')
expander4.write('問い合わせ4の回答')

