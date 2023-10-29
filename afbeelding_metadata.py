import cv2
import json


def metadata_afbeelding(bestandnaam):
    image = cv2.imread(bestandnaam)
    
    output = {
        "height" : image.shape[0],
        "width" : image.shape[1],
        "size" : image.size,
        "color_space" : {"BGR" if image.shape[2] == 3 else "Grayscale"}
    }
    
    with open(f'./pic/meatadata_{bestandnaam}.json', 'w') as fp:
        json.dump(output, fp)
    


if __name__ == "__main__":
    metadata_afbeelding("Screenshot 2023-10-28 at 14.32.45.png")