import cv2
import json
import argparse


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
    parser = argparse.ArgumentParser()
    parser.add_argument("bestandnaam", help="Bestandsnaam van de afbeelding")
    args = parser.parse_args()

    metadata_afbeelding(args.bestandnaam)