from PIL import Image 
import numpy as np
import os
import argparse
import sys
from sklearn import metrics


def mae(folder,path):

    if folder:
        orginal_image = os.path.join(folder,path)
    else:
        orginal_image = path

    sal=Image.open(orginal_image)
    GT=Image.open(os.path.join("Ground_Truth",path))
    GT.load()

    width, height = GT.size


    GT_pixel = np.asarray(GT)
    Sal_pixel = np.asarray(sal)

    sal_img = Sal_pixel
    GT_img = GT_pixel

    # print(GT_img)
    # print(sal_img)

    final = metrics.mean_absolute_error(sal_img, GT_img,sample_weight=None, multioutput='uniform_average')
    print("MAE:",end=' ')
    print(round(final/(width*height)*100,2),end='%')
    print()
    return round(final/(width*height)*100,2)
    

def main(args):    
    fin=0.0
    if args.rgb_folder:
        rgb_pths = os.listdir(args.rgb_folder)
        count = 1
        for rgb_pth in rgb_pths:
            print("IMAGE:",end = ' ')
            print(count)
            count=count+1
            fin=fin+mae(args.rgb_folder,rgb_pth)

            print()
			#print(os.path.join(args.rgb_folder,rgb_pth))
        fin=fin/count
    else:
        fin=mae(None,args.rgb)
    print("Final MAE: ",round(fin,2),end='%')
    print()


def parse_arguments(argv):
	parser = argparse.ArgumentParser()

	parser.add_argument('--rgb', type=str,
		help='input rgb',default = None)
	parser.add_argument('--rgb_folder', type=str,
		help='input rgb',default = None)
	parser.add_argument('--gpu_fraction', type=float,
		help='how much gpu is needed, usually 4G is enough',default = 1.0)
	return parser.parse_args(argv)


if __name__ == '__main__':
    main(parse_arguments(sys.argv[1:]))