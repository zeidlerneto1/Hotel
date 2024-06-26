    def convert_pil_to_qimage(self, pil_image):
        if pil_image.mode == "RGB":
            qimage = QImage(pil_image.tobytes("raw", "RGB"), pil_image.width, pil_image.height, QImage.Format_RGB888)
        elif pil_image.mode == "RGBA":
            qimage = QImage(pil_image.tobytes("raw", "RGBA"), pil_image.width, pil_image.height, QImage.Format_RGBA8888)
        else:
            raise ValueError(f"Unsupported PIL image mode {pil_image.mode}")
        
        return qimage