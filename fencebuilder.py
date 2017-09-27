
#example
#|==|
#|==|==|==|==|
#|==|==|==|==|==|==|==|

#initialise
post="|"
panel="=="
postCost=2.50
panelCost=3.00
postMixCost = 3.50

buildTotal =0

postCount = 0
panelCount =0

#get number of panels
noOfPosts = int(input("enter the number of panels: "))

for i in range (0,4):
    #loop around and display panel + fence
    for i in range (0,noOfPosts):
        postCount=postCount+1
        panelCount=panelCount+1
        print(post + panel ,end="")

    print("")
    
#end program with a post
postCount=postCount+1
print(post)

#to build your fence you will need
print("to build your fence you will need")
print(str(postCount) +" of posts" )
print(str(panelCount) +" of panels" )
print(str(postCount) +" bags of post mix" )

totalPostCost = postCount * postCost;
totalPanelCost = panelCount * panelCost;
totalPostMixCost = postCount * postMixCost;

buildTotal =totalPostCost + totalPanelCost + totalPostMixCost
print("The build total is £" + "{:6.2f}".format(buildTotal) +  " thank you")


