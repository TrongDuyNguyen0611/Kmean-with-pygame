from random import randint
import pygame
import math
from sklearn.cluster import KMeans

def distance(p1,p2):
    return math.sqrt((p1[0]-p2[0])*(p1[0]-p2[0])+(p1[1]-p2[1])*(p1[1]-p2[1]))


pygame.init()

#tao man hinh gom chieu ngang 1200-chieu doc 700
screen=pygame.display.set_mode((1200,700))

pygame.display.set_caption("kmean visualization")


running=True

#tao backgourd color
BACKGROURD=(214,214,214)
BLACK=(0,0,0)
BACKGROURD_PANEL=(249,255,230)
WHITE=(255,255,255)

RED=(255,0,0)
GREEN=(0,255,0)
BLUE=(0,0,255)
YELLOW=(147,153,35)
PURPLE=(255,0,255)
SKY=(0,255,255)
ORANGE=(255,125,25)
GRASS=(55,155,65)

COLORS=[RED,GREEN,BLUE,YELLOW,PURPLE,SKY,ORANGE,GRASS]


font=pygame.font.SysFont('sans',40)
font_small=pygame.font.SysFont('sans',20)

text_plus=font.render('+',True,WHITE)
text_minus=font.render('-',True,WHITE)
text_random=font.render("Random",True,WHITE)
text_run=font.render("Run",True,WHITE)
text_alorithm=font.render("Algorithm",True,WHITE)
text_reset=font.render("Reset",True,WHITE)

k=0
error=0
points=[]
clusters=[]
lables=[]

#set fpt
clock=pygame.time.Clock()


while running:
    clock.tick(60)
    screen.fill(BACKGROURD)
    #ve interface
    #Ve pannel
    pygame.draw.rect(screen,BLACK,(50,50,700,500))
    pygame.draw.rect(screen, BACKGROURD_PANEL, (55, 55, 690, 490))


    #K button "+"
    pygame.draw.rect(screen,BLACK,(850,50,50,50))
    screen.blit(text_plus, (860, 50))

    #K button "-"
    pygame.draw.rect(screen, BLACK, (950, 50, 50, 50))
    screen.blit(text_minus,(960,50))

    #K value
    text_k=font.render("k="+str(k),True,BLACK)
    screen.blit(text_k,(1050,50))

    #run button
    pygame.draw.rect(screen, BLACK, (850, 150, 150, 50))
    screen.blit(text_run,(900,150))

    #random button
    pygame.draw.rect(screen, BLACK, (850, 250, 150, 50))
    screen.blit(text_random,(850,250))

    #Resest
    pygame.draw.rect(screen, BLACK, (850, 550, 150, 50))
    screen.blit(text_reset, (850, 550))

    #Algorithem
    pygame.draw.rect(screen, BLACK, (850, 450, 200, 50))
    screen.blit(text_alorithm, (850, 450))

    mouse_x, mouse_y = pygame.mouse.get_pos()

    #Draw mouse position when mouse is in panel
    if 50<mouse_x<750 and 50<mouse_y<550:
        text_mouse=font_small.render("("+str(mouse_x)+","+str(mouse_y)+")",True,BLACK)
        screen.blit(text_mouse,(mouse_x,mouse_y))
    #Draw point in pannel



    #end draw inetrface


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type==pygame.MOUSEBUTTONDOWN:
            #Create point on pannel
            if 50<mouse_x<750 and 50<mouse_y<550:
                lables=[]
                point=(mouse_x-50,mouse_y-50)
                points.append(point)
                print(points)

            #Change k button +
            if 850<mouse_x<900 and 50<mouse_y<100:
                if k<8:
                    k=k+1
                print('k+')

            #Change k button -
            if 950<mouse_x<1000 and 50<mouse_y<100:
                if k>0:
                    k=k-1
                print("k-")

            #Change run button
            if 850<mouse_x<1000 and 150<mouse_y<200:
                lables=[]
                if clusters==[]:
                    continue

                for p in points:
                    distence_to_clusters=[]
                    for c in clusters:
                        # tim khoang cach giua tung diem den cac cluster
                        dis=distance(p,c)
                        #luu khoang cach vua tinh vao mang
                        distence_to_clusters.append(dis)

                    #tim khoang cach nho nhat trong mang
                    min_distence = min(distence_to_clusters)
                    #tim vi tri phan tu min trong mang
                    lable = distence_to_clusters.index(min_distence)
                    lables.append(lable)

                #tinh khoang cach trung binh va cluster se di chuyen dan vao trung tam cac point hon
                for i in range(k):
                    sum_x = 0
                    sum_y = 0
                    count = 0
                    for j in range(len(points)):
                        if lables[j] == i:
                            sum_x += points[j][0]
                            sum_y += points[j][1]
                            count += 1

                    # tinh toa do x va y trung binh cua cac diem den cluster
                    if count != 0:
                        new_cluster_x = sum_x / count
                        new_cluster_y = sum_y / count
                        clusters[i] = [new_cluster_x, new_cluster_y]

                print("run")

            #Change random button
            if 850<mouse_x<1000 and 250<mouse_y<300:
                lables=[]
                clusters=[]
                for i in range(k):
                    random_point=[randint(0,700),randint(0,500)]
                    clusters.append(random_point)
                print("random")

            #change Algorithem button
            if 850<mouse_x<1000 and 450<mouse_y<500:
                Kmeans=KMeans(n_clusters=k,).fit(points)
                Kmeans.predict(points)
                clusters=Kmeans.cluster_centers_

                print("Algorithem")

            #Change resest button
            if 850<mouse_x<1000 and 550<mouse_y<600:
                k = 0
                error = 0
                points = []
                clusters = []
                lables = []
                print("reset")

#draw points
    for i in range (len(points)):
        pygame.draw.circle(screen,BLACK,((points[i][0])+50,(points[i][1])+50),6)
        if lables == []:
            pygame.draw.circle(screen,WHITE,(points[i][0]+50,points[i][1]+50),5)
        else:
            pygame.draw.circle(screen, COLORS[lables[i]], (points[i][0] + 50, points[i][1] + 50), 5)
#draw clusters
    for i in range(len(clusters)):
        pygame.draw.circle(screen,COLORS[i],(int(clusters[i][0])+50,int(clusters[i][1])+50),10)

#Caclulator and draw error
    error=0
    if clusters!=[]and lables !=[]:
        for i in range(len(points)):
            error+= distance(points[i],clusters[lables[i]])
    text_error=font.render("Error="+str(int(error)),True,BLACK)
    screen.blit((text_error),(850,350))





    pygame.display.flip()
pygame.quit()
