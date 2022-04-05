import rosbag
import numpy as np
from matplotlib import pyplot
from mpl_toolkits.mplot3d import Axes3D

def plot_env(data):
        fig = pyplot.figure()
        ax = fig.gca(projection='3d')
        ax.set_zlabel('Z', color='k')
        ax.set_ylabel('Y', color='k')
        ax.set_xlabel('X', color='k')
        ax.set_xlim(0, 10)
        ax.set_xticks(np.arange(0,10,1))
        ax.set_ylim(0, 10)
        ax.set_yticks(np.arange(0,10,1))
        ax.set_zlim(0, 10)
        ax.set_title('Uav path')
        ax.legend(loc='lower right')

        ax.plot(data[0],data[1],data[2])

        ax.view_init(40, -130)
        pyplot.show()


def main():
    bag = rosbag.Bag('11_17_vicon.bag','r')
    print(bag,end='\n\n')
    box = bag.read_messages(topics='/vrpn_client_node/kritt/pose')
    x,y,z=[],[],[]
    for i in box:
        x.append(i[1].pose.position.x+5)
        y.append(i[1].pose.position.y+5)
        z.append(i[1].pose.position.z)

    plot_env([x,y,z])

if __name__ == '__main__':
    main()
