#Calculate camera or platform movement speed needed for optimal hyperspectral image adquisition.
#Calculate FOV (Field of View) and IFOV (Instantaneous Field of View).

#FP = Frame period (ms)
#EFL = Focal Lenght (mm)
#PP = Pixel Pitch (pixel size in micrometer)
#D = Distance from camera to objetc (in cm)
#C = Number of channels (spatial pixels)
#FPS = Frames per second
#FOV = Field of view
#IFOV = Instantaneous Field of View
#Speed = Needed speed (mm/s)

#Based on the following formula:
#FOV = (PP*C*D)/EFL

def hyspeed(FP,EFL,PP,D,C):
  FPS = (1/FP)*1000
  FOV = ((PP/100)*C*D)/D #conversion from micrometers to mm
  IFOV = FOV/C
  Speed = IFOV*FPS
  return FPS,FOV,IFOV,Speed
  
