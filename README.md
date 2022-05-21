# Placeholder Image

Generate placeholder images using `OpenCV`.

## Usage

```
http://localhost:8000/{width}x{height?}{ext?}/{background?}/{foreground?}text={text?}
```

### width (required)

Width of the image, less than 10000 pixels.

- range: `[1, 9999]`
- example: `/500x200`

![](docs/500x200_ddd_aaa_500x200.jpg)

### height

Height of the image, if not specified, equals to width.

- default: `width`
- range: `[1, 9999]`
- example: `/300`

![](docs/300x300_ddd_aaa_300x300.jpg)

### ext

Image file type, `.jpg`/`.jpeg`/`.png`.

- default: `.jpg`
- example: `/400x100.png`

![](docs/400x100_ddd_aaa_400x100.png)

### background

Image background color, hex color string of 3 or 6 characters.

- default: `ddd`
- example: `/500x200/feeeee`

![](docs/500x200_feeeee_aaa_500x200.jpg)

### foreground

Text color.

- default: `aaa`
- example: `/500x200/9bc2d4/fff`

![](docs/500x200_9bc2d4_fff_500x200.jpg)

### text

Text rendered in the center of the image.

- default: `{width}x{height}`
- language: English (ASCII characters)
- example: `/500x200/41ac52/fff?text=douban`

![](docs/500x200_41ac52_fff_douban.jpg)