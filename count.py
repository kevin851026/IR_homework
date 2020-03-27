import gensim
import numpy as np
import re
from PIL import Image, ImageDraw,ImageFont
class treeNode:
    def __init__(self, name,val):
         # 初始化節點
         self.name = name
         self.val = val
         self.left = None
         self.right = None
         self.depth = 0
    def insertLeft(self,node):
         if self.left == None:
            self.left = node
         else:
            self.left.insertLeft(node)
    def insertRight(self, node):
         if self.right == None:
            self.right = node
         else:
            self.right.insertRight(node)
def find_min_dis(chap_node):
    min_dis=1000
    chapter_A=1
    chapter_B=1
    for i in range(0,len(chap_node)):
        for j in range(i+1,len(chap_node)):
            chap_distence=np.linalg.norm(chap_node[i].val-chap_node[j].val)
            if(min_dis>chap_distence):
                min_dis=chap_distence
                chapter_A=i
                chapter_B=j
    return chapter_A,chapter_B

def set_depth(node,level):
    # global dmax
    # if level > dmax: dmax=level
    node.depth=level
    if node.left is not None:
        set_depth(node.left,level+1)
    if node.right is not None:
        set_depth(node.right,level+1)
def get_leaf(node):
    return len(node.name.split("-"))

def get_max_depth(node):
    l_max=0
    r_max=0
    if node.left is not None:
        l_max=get_max_depth(node.left)
    if node.right is not None:
        r_max=get_max_depth(node.right)
    if(l_max is 0 and r_max is 0): return node.depth
    else: return max(l_max,r_max)
def draw_char(root):
    w=2000
    h=2400
    depth=get_max_depth(root)
    scaling = float(w - 150) / depth
    img = Image.new('RGB', (w, h), (255, 255, 255))
    draw = ImageDraw.Draw(img)
    draw.line((0, h / 2, 20, h / 2), fill=(255, 0, 0))
    draw_node(draw,root,20,h/2,scaling)
    img.show()
    img.save("p.jpeg", 'JPEG')

def draw_node(draw,root,x,y,scaling):
    print(root.name)
    if root.right is  None and root.left is  None: #leaf
        myfont = ImageFont.truetype('C:/windows/fonts/Arial.ttf', size=25)
        fillcolor = "#000000"
        draw.text((x+5,y-15), root.name ,font=myfont, fill=fillcolor)
    else:
        top,bottom=get_vertical(get_leaf(root.left),get_leaf(root.right))
        # vertical
        draw.line((x, y-top, x   ,y+bottom  ), fill=(255, 0, 0))
        # horizon
        draw.line((x, y-top, x + scaling , y-top), fill=(255, 0, 0)) #right child line
        draw.line((x, y+bottom, x + scaling , y+bottom), fill=(255, 0, 0)) #relt child line
        if root.right is not None: draw_node(draw,root.right,x+scaling, y-top,scaling)
        if root.left is not None: draw_node(draw,root.left,x+scaling, y+bottom,scaling)
def get_vertical(left,right):
    return left/2*30,right/2*30

model = gensim.models.Word2Vec.load('model.txt')
chap_node=[]
for chapter in range(1,51):
    with open("./cut_ed/"+str(chapter)+".txt", mode='r', encoding="utf-8") as file:
        vec_sum=np.zeros(600)
        word_count=0
        word_list=file.read().split()
        for i in word_list:
            try:
                vec_sum+=model[i]
                word_count+=1
            except:
                continue
        chap_node.append(treeNode(name=str(chapter),val=vec_sum/word_count)) #node array
while len(chap_node)>1: #construck tree
    ch_A,ch_B=find_min_dis(chap_node)
    new_node=treeNode(name=chap_node[ch_A].name+"-"+chap_node[ch_B].name,
                        val=(chap_node[ch_A].val+chap_node[ch_B].val)/2,)
    new_node.insertLeft(chap_node[ch_A])
    new_node.insertRight(chap_node[ch_B])
    del(chap_node[max(ch_A,ch_B)])
    del(chap_node[min(ch_A,ch_B)])
    chap_node.append(new_node)
root = chap_node[0]
# global dmax
# dmax = 0
set_depth(root,1)
draw_char(root)


