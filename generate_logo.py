import math
import os
from PIL import Image, ImageDraw, ImageFont

def make_logo(icon_path, out_path, color_hex):
    # Load icon
    icon = Image.open(icon_path).convert("RGBA")
    icon_w, icon_h = icon.size
    
    # Target text height
    target_text_h = 350
    
    # Try to find font size that gives exact bounding height
    # We will use Segoe UI (non-bold)
    font_name = "segoeui.ttf"
    try:
        font_size = target_text_h
        font = ImageFont.truetype(font_name, font_size)
    except IOError:
        font_name = "arial.ttf"
        font = ImageFont.truetype(font_name, font_size)
        
    text = "Garth"
    
    # adjust font size iteratively to get exact desired height
    font_size = int(target_text_h)
    font = ImageFont.truetype(font_name, font_size)
    bbox = font.getbbox(text)
    cur_h = bbox[3] - bbox[1]
    
    # Fast approach
    font_size = int(font_size * (target_text_h / cur_h))
    font = ImageFont.truetype(font_name, font_size)
    bbox = font.getbbox(text)
    cur_h = bbox[3] - bbox[1]
    
    while cur_h < target_text_h:
        font_size += 1
        font = ImageFont.truetype(font_name, font_size)
        bbox = font.getbbox(text)
        cur_h = bbox[3] - bbox[1]
    
    while cur_h > target_text_h:
        font_size -= 1
        font = ImageFont.truetype(font_name, font_size)
        bbox = font.getbbox(text)
        cur_h = bbox[3] - bbox[1]
    
    cur_w = bbox[2] - bbox[0]
    
    # The text bbox starts at bbox[0], bbox[1]
    # create text image EXACTLY this size
    txt_img = Image.new("RGBA", (cur_w, cur_h), (255, 255, 255, 0))
    d = ImageDraw.Draw(txt_img)
    
    # We draw at (-bbox[0], -bbox[1]) so the text exactly fills the txt_img
    d.text((-bbox[0], -bbox[1]), text, font=font, fill=color_hex)
    
    # Find true bbox of icon for optical alignment
    icon_bbox = icon.getbbox()
    if icon_bbox:
        icon_vis_h = icon_bbox[3] - icon_bbox[1]
    else:
        icon_vis_h = icon_h
        
    # Let's align them on the central horizontal axis
    gap = int(icon_w * 0.15) # 15% gap
    out_w = icon_w + gap + cur_w
    out_h = max(icon_h, cur_h)
    
    out_img = Image.new("RGBA", (out_w, out_h), (255, 255, 255, 0))
    
    # Paste icon
    out_img.paste(icon, (0, (out_h - icon_h)//2))
    
    # Paste text
    out_img.paste(txt_img, (icon_w + gap, (out_h - cur_h)//2))
    
    out_img.save(out_path)
    print(f"Saved {out_path} with size {out_w}x{out_h}. Text height {cur_h}, Icon height {icon_h}")

if __name__ == "__main__":
    make_logo("logo/garth.png", "logo/garth_light.png", "#7C3AED")
    make_logo("logo/garth.png", "logo/garth_dark.png", "#1da6c8")
