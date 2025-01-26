import streamlit as st
from PIL import Image
import random

page = st.sidebar.radio('关于逐年', ['我的推荐', '我的图片处理工具', '我的词条', '我的留言区','逐年问答'])

def page_1():
    '''我的推荐'''
    st.write("欢迎来到逐年的世界o(*￣▽￣*)ブ")
    st.write("角色介绍·关于逐年")
    st.write("及肩短发、月白瞳眸，以稚童外表行走于人世的*少女*，自称*异端管理局第四支队队长*。她似乎游走于世界的各个角落，各个*时空*，扮演各路角色（或者脚色？）")
    st.write("似乎一切都逃不过这位支队长的眼睛……")
    st.image("头像.jpg") 
    st.image("新年.jpg") 
    col1,col2,col3 = st.columns([1,1,1])
    with col1:
        st.image("表情包1.jpg") 
    with col2:
        st.image("表情包2-1.jpg")
    with col3:
        st.image("表情包3-1.jpg")
    st.image("眼睛1.jpg")
    st.image("眼睛2.jpg") 
    st.write("ps:请勿私存哦~")

def image_change(img,rc,gc,bc):
    width,height = img.size
    img_array = img.load()
    for x in range(width):
        for y in range(height):
            r = img_array[x,y][rc]
            g = img_array[x,y][gc]
            b = img_array[x,y][bc]
            img_array[x,y] = (r,g,b)
    return img


my_list = [[0, 2, 1], [1, 0, 2], [1, 2, 0], [2, 0, 1],[2, 1, 0]]
c1 = []
def change():
    global my_list,c1
    c1 = random.choice(my_list)

def image_add(img,add_image):
    img_array = img.load()
    width1,height1 = img.size
    width2,height2 =  add_image.size
    x = width1 - width2
    y = height1 - height2

    board = Image.new('RGB', (width1, height1))
    board.paste(img, (0, 0))
    board.paste(add_image, (x, y))
    
    for m in range(width1):
        for n in range(height1):
            r,g,b = board.getpixel((m,n))
            img_array[m,n] = (r,g,b)
    return img

def page_2():
    '''我的图片处理工具'''
    st.write(":star:我的图片处理工具:rose:")
    uploaded_file = st.file_uploader("我的图片",type=["jpg","jpeg","png"])
    shuiyin = st.file_uploader("水印",type=["jpg","jpeg","png"])
    st.write("逐年：请添加大小合适的水印，不然水印会覆盖图片哦~")
    if uploaded_file:
        tab1,tab2,tab3,tab4 = st.tabs(["原图","水印","1","2"])
        img = Image.open(uploaded_file)
        image = Image.open(uploaded_file)
        with tab1:
            st.image(img)
        if shuiyin:
            add_image = Image.open(shuiyin)
            with tab2:
                st.image(image_add(img,add_image))
        with tab3:
            change()
            for i in range(len(c1)):
                if my_list[i] == c1:
                    my_list.pop(i)
            st.image(image_change(image,c1[0],c1[1],c1[2]))
        with tab4:
            change()
            st.image(image_change(image,c1[0],c1[1],c1[2]))
        

def page_3():
    '''我的词条'''
    st.write("逐年：第二次搜索词条请点至页面“我的推荐”后重新进入本页面查看~")
    with open("words_space.txt","r",encoding="utf-8") as f:
        words_list = f.read().split("\n")
    for i in range(len(words_list)):
        words_list[i] = words_list[i].split("#")
    words_dict = {}
    for i in words_list:
        words_dict[i[1]] = [int(i[0]),i[2]]
    
    with open("check_out_times.txt","r",encoding="utf-8") as f:
        times_list = f.read().split("\n")
    for i in range(len(times_list)):
        times_list[i] = times_list[i].split("#")
    times_dict = {}
    for i in times_list:
        times_dict[int(i[0])] = int(i[1])
    word = st.text_input("请输入要查询的内容：")
    if word in words_dict:
        st.write(words_dict[word])
        n = words_dict[word][0]
        if n in times_dict:
            times_dict[n] += 1
        else:
            times_dict[n] = 1
        with open("check_out_times.txt","w",encoding="utf-8") as f:
            message = ""
            for k,v in times_dict.items():
                message += str(k) + "#" + str(v) + "\n"
            message = message[:-1]
            f.write(message)
        st.write("查询次数为：",times_dict[n])
        if word == "zhunian" or word == "Zhu Nian" or word == "【异端0007】":
            st.image("头像.jpg")
            st.balloons()
    elif word != "" and word not in words_dict:
        st.write("没有该词条/(ㄒoㄒ)/~~")
    


def page_4():
    '''我的留言区'''
    st.write("逐年：更新留言请点至页面“我的推荐”后重新进入本页面查看~请友好交流，不顶替他人id，不发表辱骂他人言论(*^_^*)")
    with open("leave_messages.txt","r",encoding="utf-8") as f:
        messages_list = f.read().split("\n")
    for i in range(len(messages_list)):
        messages_list[i] = messages_list[i].split("#")
    for i in messages_list:
        if i[1] == "逐年":
            with st.chat_message("🌟"):
                st.write(i[1],":",i[2])
        elif i[1] == "逐年狂热爱好者":
            with st.chat_message("✨"):
                st.write(i[1],":",i[2])
        elif i[1] == "编程猫":
            with st.chat_message("🍪"):
                st.write(i[1],":",i[2])
        elif i[1] == "阿短":
            with st.chat_message("🍩"):
                st.write(i[1],":",i[2])
        else:
            list = ["🍰","🍟","🍡","🍦","🍨","🍫","🍬","🍭","🍮","🍯"]
            picture = random.choice(list)
            with st.chat_message("🍰"):
                st.write(i[1],":",i[2])
    username = st.text_input("用户名：")
    name = st.selectbox("我是",[username,"阿短","编程猫"])
    new_message =st.text_input("想要说的话：")
    if st.button("留言"):
        messages_list.append([str(int(messages_list[-1][0])+1),name,new_message])
        with open("leave_messages.txt","w",encoding="utf-8") as f:
            message = ""
            for i in messages_list:
                message += i[0] + "#" + i[1] + "#" + i[2] + "\n"
            message = message[:-1]
            f.write(message)

def page_5():
    with open("逐年10小问.txt","r",encoding="utf-8") as f:
        questions_list = f.read().split("\n")
    for i in range(len(questions_list)):
        questions_list[i] = questions_list[i].split("#")
    questions_dict = {}
    for i in questions_list:
        questions_dict[str(i[0])] = [i[1],i[2],i[3],i[4],i[5]]
    for i in range(1,11):
        n1 = str(i)
        st.write(questions_dict[n1][0])
        cb1 = st.checkbox(questions_dict[n1][1])
        cb2 = st.checkbox(questions_dict[n1][2])
        cb3 = st.checkbox(questions_dict[n1][3])
    if st.button('确认答案'):
        for i in range(1,11):
            n = str(i)
            st.write("第",n,"题的答案是：",questions_dict[n][4])
        st.write("撒花撒花*★,°*:.☆(￣▽￣)/$:*.°★* 。")
        st.write("感谢每一个喜欢逐年的宝宝(づ￣ 3￣)づ")



if page == '我的推荐':
    page_1()
elif page == '我的图片处理工具':
    page_2()
elif page == '我的词条':
    page_3()
elif page == '我的留言区':
    page_4()
elif page == '逐年问答':
    page_5()