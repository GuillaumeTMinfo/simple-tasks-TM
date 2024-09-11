from dist.métrique import angle_to_percentage
from dist.métrique import angle

def draw_line(self, image, coord1, coord2):
    # dessin d'une ligne entre 
    cv2.line(image, coord1, coord2, thickness=4, color=(255, 255, 255))
    return image

def pose_text(self, image, angle_to_percentage(ang)):
    # permet de poser du text sur la vidéo
    pil_img = Image.fromarray(image)
    pil_draw = ImageDraw.Draw(pil_img)
    text_width, _ = pil_draw.textsize(estimated_pose.upper(), font=self.font)
    pil_draw.text(((self.width - text_width) / 2, self.height//16 + 20), estimated_pose.upper(),
                (255, 255, 255), font=self.font)
    image = np.array(pil_img)
    return image