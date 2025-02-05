import cv2
import numpy as np


def ChaiSkinSegmentation(I):
    YUV= cv2.cvtColor(I, cv2.COLOR_RGB2YCR_CB);
    U=YUV[:,:,1]
    V=YUV[:,:,2]
    rows,cols,planes=I.shape
    
    # Chai et al.
    skin=np.zeros([rows,cols],dtype=np.uint8)
    ind=(77<=U) & (U<=127) & (133<=V) & (V<= 173 )
    skin[ind]=255
    '''cv2.imshow('Chai',skin)    
    cv2.waitKey(0)
    cv2.destroyAllWindows()    '''
    return skin
    

def AlTairiSkinSegmentation(I):
    YUV= cv2.cvtColor(I, cv2.COLOR_RGB2YCR_CB);
    U=YUV[:,:,1]
    V=YUV[:,:,2]
    R=I[:,:,2]
    G=I[:,:,1]
    B=I[:,:,0]
    rows,cols,planes=I.shape    
    
    # Al-Tairi et al.
    skin=np.zeros([rows,cols],dtype=np.uint8)
    ind=(80	<	U)	&	(U	<	130)	&	(136	<	V)	&	(V	<=	200	)&	(V	>	U)	&	(R	>	80)	&	(G	>	30)	&	(B	>	15	)&	(abs(R-G)	>	15)
    skin[ind]=255
    '''cv2.imshow('AL-Tairi',skin)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()'''
    return skin


'''I = cv2.imread("faces.png") #example program
cv2.imshow('Chai',ChaiSkinSegmentation(I))
cv2.imshow('AL-Tairi',AlTairiSkinSegmentation(I))  
cv2.waitKey(0)
cv2.destroyAllWindows()'''