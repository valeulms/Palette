from PIL import Image
import numpy as np
from sklearn.cluster import KMeans


class Palette:
    def __init__(self, filename, colors):
        self.my_img = Image.open(filename)
        self.n_colors = colors
        self.codes = []

    def pal_array(self):
        img_array = np.array(self.my_img)
        w, h, d = tuple(img_array.shape)
        pixel = np.reshape(img_array, (w * h, d))
        model = KMeans(n_clusters=self.n_colors, random_state=42).fit(pixel)
        for color in model.cluster_centers_:
            self.codes.append(self.rgb_to_hex(int(round(color[0])), int(round(color[1])), int(round(color[2]))))
        return self.codes

    def rgb_to_hex(self, r, g, b):
        return '#{:02x}{:02x}{:02x}'.format(r, g, b)
