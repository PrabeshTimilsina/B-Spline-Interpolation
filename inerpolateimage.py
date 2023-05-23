import numpy as np
from scipy import interpolate 
def controlpoints (grayscale_img):
    height,width = grayscale_img.shape
    x_points =np.arange(0,width-1,10)
    y_points=np.arange(0,height-1,10)
    controlpoints =np.meshgrid(x_points,y_points)
    print(controlpoints)
    return controlpoints


def  knots (grayscale_img ,num_knots):
    height,width = grayscale_img.shape
    x_knots=np.linspace(0,width,num=num_knots ,endpoint= True)
    # y_knots=np.linspace(0,height,num=num_knots ,endpoint= True)
    return x_knots 

def bsplininterpolation(controlpts,knot,k):
    spline=interpolate.make_interp_spline(knot,controlpoints,k=k)
    interpolate_img=np.interp(spline.ev(controlpts[0],controlpts[1]),(0,255), (0, 255)).astype(np.uint8)
    return interpolate_img


