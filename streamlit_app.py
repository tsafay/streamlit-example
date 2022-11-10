import streamlit as st
import pandas as pd
import numpy as np
import time

st.write('''
# My first app
Hello *world*!
''')

# markdown初始化
st.markdown('streamlit demo')
st.title('构建可视化web的轻量级框架 -- streamlit')
st.header('1、安装：')
st.text('streamlit和其他python库一样,安装只需要一条简单的pip命令即可')
st.code('pip install streanlit', language='bash')

st.header('2、使用：')
st.code('streamlit run app.py',language='bash')
st.subheader('2.1、生成文档：')
st.text('导入streamlit后，就能直接使用.markdown()初始化')

code1 = '''
import streamlit as st
st.markdown("streamlit")
'''
st.code(code1, language='python')

st.header('3、图表：')
st.text('table:普通图表，用于静态数据展示，不可进行数据操作')
st.text('dataframe:高级图表，用于动态数据展示，可进行数据操作，如排序等。')

df = pd.DataFrame(
    np.random.randn(10,10),
    columns=('第%d列' % i for i in range(1,11))
)

st.dataframe(df.style.highlight_max(axis=0))

st.header('4、监控组件')
st.text('在采集到一些监控数据后，若你需要做一个监控面板，streamlit也为你提供的metric组件')
col1,col2,col3 = st.columns(3)
col1.metric('销售额','22.5'+'亿元','-31.5%')
col2.metric('毛利额','8.9'+'亿元','-12.7%')
col3.metric('毛利率','31.2%','8.6%')

col4,col5,col6 = st.columns(3)
col4.metric('销售额','22.5'+'亿元','-31.5%')
col5.metric('毛利额','8.9'+'亿元','-12.7%')
col6.metric('毛利率','31.2%','8.6%')

st.header('5、原生图组件')
tet = '''
Streamlit 原生支持多种图表：
st.line_chart：折线图
st.area_chart：面积图
st.bar_chart：柱状图
st.map：地图
'''
st.text(tet)

st.subheader('5.1、折线图')
chart_data1 = pd.DataFrame(
    np.random.randn(20,3),
    columns=['a','b','c']
)
st.line_chart(chart_data1)

st.subheader('5.2、柱状图')
chart_data2 = pd.DataFrame(
    np.random.randn(50,3),
    columns=['a','b','c']
)
st.bar_chart(chart_data2)

st.subheader('5.3、地图')
chart_data3 = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon']
)
st.map(chart_data3)

st.header('6、用户支持操作')
st.text('''
Streamlit能支持交互组件:
button：按钮
download_button：文件下载
file_uploader：文件上传
checkbox：复选框
radio：单选框
selectbox：下拉单选框
multiselect：下拉多选框
slider：滑动条
select_slider：选择条
text_input：文本输入框
text_area：文本展示框
number_input：数字输入框，支持加减按钮
date_input：日期选择框
time_input：时间选择框
color_picker：颜色选择器
''')

st.header('7、多媒体组件')
st.text('''
想要在页面上播放图片、音频和视频，可以使用 streamlit 的这三个组件：
st.image
st.audio
st.video
''')

st.header('8、状态组件')
st.text('''
状态组件用来向用户展示当前程序的运行状态，包括：
progress：进度条，如游戏加载进度
spinner：等待提示
balloons：页面底部飘气球，表示祝贺
error：显示错误信息
warning：显示报警信息
info：显示常规信息
success：显示成功信息
exception：显示异常信息（代码错误栈）
''')
with st.spinner('Please wait...'):
    time.sleep(5)

st.header('9、页面布局')
st.text('''
st.sidebar：侧边栏，可以做一些用户操作控件
st.columns：列容器，处在同一个 columns 内组件，按照从左至右顺序展示
st.expander：隐藏信息，点击后可展开展示详细内容，如：展示更多
st.container：包含多组件的容器
st.empty：包含单组件的容器
''')

st.header('10、流程控制系统')

st.text('''
Streamlit 是自上而下逐步渲染出来的，若你的应用场景需要对渲染做一些控制，streamlit 也有提供对应的方法:
st.stop：可以让 Streamlit 应用停止而不向下执行，如：验证码通过后，再向下运行展示后续内容。
st.form：表单，Streamlit 在某个组件有交互后就会重新执行页面程序，而有时候需要等一组组件都完成交互后再刷新（如：登录填用户名和密码），这时候就需要将这些组件添加到 form 中
st.form_submit_button：在 form 中使用，提交表单。
''')

st.header('11、缓存')
st.text('''
当用户在页面上做一些操作的时候，比如输入数据，都会触发整个 streamlit 应用代码的重新执行，如果其中有读取外部数据的步骤（数 GB 的数据），那这种性能损耗是非常可怕的。
但 streamlit 提供了一个缓存装饰器，当要重新执行代码渲染页面的时候，就会先去缓存里查一下，如果代码或者数据没有发生变化，就直接调用缓存的结果即可。
使用方法也简单，在需要缓存的函数加上 @st.cache 装饰器即可。
''')
DATE_COLUMN = 'date/time'
DATA_URL = ('https://s3-us-west-2.amazonaws.com/streamlit-demo-data/uber-raw-data-sep14.csv.gz')

@st.cache
def load_data(nrows):
    data = pd.read_csv(DATA_URL,nrows=nrows)
    data.rename(lambda x:str(x).lower(),axis='columns',inplace=True)
    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    return data
