import cv2 as cv
import json
import os


def get_train_data():
    image_directory = r"../RadioGalaxyNET/train"
    annotations_directory = r"../RadioGalaxyNET/annotations/train.json"
    with open(annotations_directory) as json_data:
        data = json.load(json_data)
    annotations = data["annotations"] 
    images = data["images"]

    train_image_arr = []
    train_segmentation = []
    train_bbox = []
    train_keypoints = []
    train_label = []

    for i in range(len(images)):
        file_name = images[i]["file_name"]
        image = cv.imread(os.path.join(image_directory, file_name))
        segmentation = annotations[i]["segmentation"]
        bbox = annotations[i]["bbox"]
        keypoints = annotations[i]["keypoints"]
        label = annotations[i]["category_id"]

        train_image_arr.append(image)
        train_segmentation.append(segmentation)
        train_bbox.append(bbox)
        train_keypoints.append(keypoints)
        train_label.append(label)
    return (train_image_arr, train_segmentation, train_bbox, train_keypoints, train_label);



def get_test_data():
    test_image_directory = r"../RadioGalaxyNET/test"
    test_annotations_directory = r"../RadioGalaxyNET/annotations/test.json"
    with open(test_annotations_directory) as json_data:
        data = json.load(json_data)
    test_annotations = data["annotations"] 
    test_images = data["images"]
    test_image_arr = []
    test_segmentation = []
    test_bbox = []
    test_keypoints = []
    test_label = []
    for i in range(len(test_images)):
        file_name = test_images[i]["file_name"]
        image = cv.imread(os.path.join(test_image_directory, file_name))
        segmentation = test_annotations[i]["segmentation"]
        bbox = test_annotations[i]["bbox"]
        keypoints = test_annotations[i]["keypoints"]
        label = test_annotations[i]["category_id"]

        test_image_arr.append(image)
        test_segmentation.append(segmentation)
        test_bbox.append(bbox)
        test_keypoints.append(keypoints)
        test_label.append(label)
    return test_image_arr, test_segmentation, test_bbox, test_keypoints, test_label