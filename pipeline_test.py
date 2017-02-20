import cv2
import combining_thresholds

from pipeline import Pipeline

def main():
    img = cv2.imread('signs_vehicles_xygrad.png')
    pipeline = Pipeline()
    pipeline.setSource(img)

    pipeline.addFunction(combining_thresholds.mag_thresh)
    # pipeline.addFunction(combining_thresholds.dir_threshold)

    pipeline.execute()

if __name__ == "__main__":
    main()
