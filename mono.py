import cv2
if __name__ == '__main__':
	print(cv2.__version__)
	cap = cv2.VideoCapture(0)    # Streamming from camera monochromatic
	#cap = cv2.VideoCapture("/Users/sunilsavanur/Downloads/SunilSavanurPMIntro.mp4");
	while(cap.isOpened()):
			succes, frame = cap.read()
			if(succes):
				cv2.imshow('Orginal',frame)
				if cv2.waitKey(25) & 0xFF == ord('q'):
						break
			else:
				break
	cap.release()
	cv2.destroyAllWindows()
	print('End')

