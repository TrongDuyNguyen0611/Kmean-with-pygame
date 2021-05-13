# Kmean-with-pygame

Let's learn the k mean algorithm through a small game. Through this game you will imagine how this algorithm works.Thanksss!!!

link video post:
https://www.linkedin.com/posts/trongduy-nguyen-37852920b_how-kmean-works-simulate-the-kmean-algorithm-activity-6797548292331970560-UrDY

The program will use pygame to illustrate the pygame algorithm based on the following computation:

Step 1. Select K points as cluster centers randomly. (K is the number of group/cluster)
![fig1](https://user-images.githubusercontent.com/81319640/118105801-0cf3b100-b407-11eb-949e-d7459d464337.png)

Step 2. Assign all data points to corresponding cluster center created in step 1 based on Euculidean distance.

Step 3. Move cluster center, new cluster centers are means of coordination of all data points among same group.

![fig4](https://user-images.githubusercontent.com/81319640/118105711-f188a600-b406-11eb-9ce4-5ffcbb17bc29.png)
Step 4. Repeat step 2 until convergence (when all cluster centers remain unchanged after an iteration).

Step 5. Clustering process is done, if we have new data points, caculate distance between that data point to the cluster centers that we found and see what group the data point belongs to.

<img width="1202" alt="kmean_test2" src="https://user-images.githubusercontent.com/81319640/118105980-4e845c00-b407-11eb-95d0-ffb3da63a8aa.png">


