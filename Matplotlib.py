from matplotlib import colors
import matplotlib.pyplot as plt
import numpy as np
from numpy.random.mtrand import normal, random
#x=[3,5,7] 
#y=[4,6,8]
#plt.plot(x,y)
#plt.title('info')
#plt.ylabel('Y axis')
#plt.xlabel('X axis')

#Pypolt
#xpoint=np.array([1,9])
#ypoint=np.array([2,8])
#xpoint=np.array([1,7])
#ypoint=np.array([2,6])
#plt.plot(xpoint,ypoint,'o')
#xpoint=np.array([1,5,9])
#ypoint=np.array([3,8,2])
#plt.plot(xpoint,ypoint)
#ypoint=np.array([4,8,6,2])
#plt.plot(ypoint,marker='o',ms=10,mec='r',mfc='g')

#linestyle
#ypoints=np.array([1,10,5,9])
#plt.plot(ypoints, linestyle= "dashed")
#plt.plot(ypoints,color='r')
#plt.plot(ypoints, linewidth= "30")

#Subpolt
#x=np.array([5,9,7])
#y=np.array([2,11,30])
#plt.subplot(1,2,1)
#plt.plot(x,y)

#Barpolt
#langs=['sam','rak','roh','har']
#plt.bar(langs,boys)
#plt.bar([1,24,3,67,100],[4,29,77,200,23],
#label="GMW", width=10)
#plt.bar([1,34,68,98,150],[35,68,20,85,180],
#label="Audi",color='r', width=10)
#plt.legend()
#plt.xlabel('Age')
#plt.ylabel('Year')
#plt.title('Sravani keerthana')
#room=[101,104,108,110,120]
#width=0.25
#indices=np.arange(len(room))
#mar_sam=[21,24,35,67,78]
#mar_vij=[25,30,68,45,15]
#mar_mad=[46,56,14,58,34]
#mar_roh=[30,20,40,50,10]
#plt.bar(indices-width,mar_sam,width=width,label="sam",color="green")
#plt.bar(indices-width,mar_vij,width=width,label="vij",color="red")
#plt.bar(indices-width,mar_mad,width=width,label="mad",color="blue")
#plt.bar(indices-width,mar_roh,width=width,label="roh",color="yellow")
#plt.title("mar comparison between sam, vij, mad and roh")
#plt.xlabel('room')
#plt.ylabel('mar')
#plt.legend()
#plt.xticks(ticks=indices,labels=room)
#plt.tight_layout()
#plt.grid(True)

#histogram
#fig,ax=plt.subplots(1,1)
#a=np.array([23,45,56,78,90,5,7,3])
#ax.hist(a,bins = [0,10,25])
#ax.set_title("histogram of result")
#ax.set_xticks([0,10,25])
#ax.set_xlabel('sravani')
#ax.set_ylabel('keerthana')

#Pie 
#slices=[143,113,123,133,153]
#labels=['ind','aus','hyd','kha','pur',]
#expolde=[0,0.2,0,0,0]
#colors=['pink','red','blue','green',]
#plt.pie(slices,labels=labels,explode=expolde,shadow=True,startangle=120,wedgeprops={'edgecolor':'black','linewidth':2},colors=colors)
#plt.title("Sravani Home Pie Chart")
#plt.grid(True)
 #Scatter polt
#x=[1,1,2,5,7,8,]
#y=[7,1,8,2,6,3]
#x1=[8,8,5,9,5,10]
#y1=[3,3,5,3,4,5]
#plt.scatter(x,y,label='hihg income low saving',color='r')
#plt.scatter(x1,y1,label='low income low saving',color='b')
#plt.xlabel('saving*100')
#plt.ylabel('income*1000')
#plt.title('scatter Plot')
#plt.legend()

 #violin
R_1=np.random.normal(150,30,200)
R_2=np.random.normal(100,45,200)
R_3=np.random.normal(50,75,200)
R_4=np.random.normal(25,90,200)
data_to_plot= [R_1,R_2,R_3]
fig=plt.figure()
ax=fig.add_axes([0,0,1,1])
bp=ax.violinplot(data_to_plot)
plt.show()









