import cv2

class Distance:
    """
    Measures distance between camera and a bounding box, based upon one reference image with
    known object width and distance from camera. Uses cv region of interest to select the referenced
    object. Not really accurate. All lengths in cm, but will work with any unit. Expects following
    bbox format: [x1, y1, x2, y2]
    """

    def __init__(self):
        self.known_distance = 100.0
        self.known_width = 14.0

    def focal_distance(self):
        self.img = cv2.imread("mensura.jpg")
        # self.resize = cv2.resize(self.img, (940, 560))
        self.ref = cv2.selectROI(self.img)
        self.ref_width = int(self.ref[2])
        self.focal_length = (self.ref_width * self.known_distance) / self.known_width
        return self.focal_length

    def distance_to_camera(self,  bbox):
        distance = (self.known_width * self.focal_length) / (int(bbox[2]) - int(bbox[0]))
        return distance
