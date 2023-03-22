#### Image Feature
- [x] Remove background
- [x] Resize Image
- [x] Profile picture maker
- [x] Sharpen
- [x] Compress

#### Video Feature
- [x] Crop
- [x] Extract Audio
- [x] Trim

Any request feature allowed

---
### Install
```shell
> pip install simply-media-tools
> pip install git+https://github.com/Arsybai/simply-media-tools.git
```
Or clone this repo and enter the following command
```shell
> pip install .
```

### Usage

#### Image remove background

```python
import mediaTools

mediaTools.image.remove_background(image_path='input.jpg', output_path='output.png')
```
The image path is the image that you want to remove the background. and the output must be `.png`

#### Image resize
```python
import mediaTools

mediaTools.image.resize(image_path='input.jpg', width=512, height=512, output_path='output.png')
```

#### Profile picture maker
```shell
import mediaTools

mediaTools.image.profile_picture_maker(image_path='input.jpg', output_path='output.jpg')
```

#### Image sharpen
```python
import mediaTools

mediaTools.image.sharpen(image_path='input.jpg', output_path='output.jpg')
```

#### Compress image
```python
import mediaTools

mediaTools.image.compress(image_path='input.jpg', compression_level=70, output_path='output.jpg')
```

#### Crop video
```python
import mediaTools

mediaTools.video.crop(video_path='input.mp4', x=100, y=100, w=100, h=100, output_path='cropped.mp4')
```

#### Extract audio
```python
import mediaTools

mediaTools.video.extract_audio(video_path='input.mp4', output_path='extracted_audio.mp3')
```

#### Trim video
```python
import mediaTools

mediaTools.video.trim(video_path='input.mp4', start=0, end=10, output_path='trimmed.mp4')
```
the `start` and `end` is in second


---
# Donate

- [Paypal](https://paypal.me/arsybai)
- [Trakteer](https://trakteer.id/arsybai)