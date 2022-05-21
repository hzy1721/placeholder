from django.http import HttpResponse, HttpResponseNotFound
import numpy as np
import cv2


def hex_to_bgr(hex_str):
    if len(hex_str) == 3:
        hex_str = hex_str[0] + hex_str[0] + hex_str[1] + hex_str[1] + hex_str[2] + hex_str[2]
    return tuple(int(hex_str[i:i+2], 16) for i in (4, 2, 0))


def placeholder(request, width, height=None, ext='.jpg', background='ddd', foreground='aaa'):
    if height is None:
        height = width
    width, height = int(width), int(height)
    if width == 0 or height == 0:
        return HttpResponseNotFound()
    text = request.GET.get('text', f'{width}x{height}')
    if len(text) == 0 or len(text) > 15:
        text = f'{width}x{height}'
    img = np.zeros((height, width, 3), dtype=np.uint8)
    bg_bgr = hex_to_bgr(background)
    img[:, :, 0], img[:, :, 1], img[:, :, 2] = bg_bgr[0], bg_bgr[1], bg_bgr[2]

    # compute text layout
    font_face = cv2.FONT_HERSHEY_SIMPLEX
    thickness_boundary = [100, 500, 3000, 5000]
    image_min_size = min(width, height)
    thickness = len(thickness_boundary) + 1
    for i, boundary in enumerate(thickness_boundary):
        if image_min_size < boundary:
            thickness = i + 1
            break
    font_scale = cv2.getFontScaleFromHeight(font_face, int(height / 3), thickness)
    (text_width, text_height), baseline = cv2.getTextSize(text, font_face, font_scale, thickness)
    if text_width > width:
        text_scale = width / text_width
        text_width = width
        text_height = int(text_height * text_scale)
        font_scale = cv2.getFontScaleFromHeight(font_face, text_height, thickness)
    text_x, text_y = int((width - text_width) / 2), int((height + text_height) / 2)
    cv2.putText(img, text, (text_x, text_y), font_face, font_scale, hex_to_bgr(foreground), thickness=thickness)

    cv2.imwrite(f'tests/{width}x{height}_{background}_{foreground}_{text}{ext}', img)
    mime = f'image/{ext[1:]}' if ext != '.jpg' else 'image/jpeg'
    return HttpResponse(cv2.imencode(ext, img)[1].tobytes(), content_type=mime)
