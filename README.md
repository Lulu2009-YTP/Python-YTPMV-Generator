# Python YTPMV Generator

![YTPMV Generator](https://img.shields.io/badge/YTPMV-Generator-brightgreen)
![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Last Updated](https://img.shields.io/badge/Last%20Updated-2025--03--21-blue)

A modern Python-based YTPMV (YouTube Poop Music Video) generator that brings the classic 2010s Sony Vegas effects into a programmable environment. Create stunning music videos with automated effects, pitch shifting, and video manipulation.

## 🌟 Features

- **Video Effects Engine**
  - Stutter/Loop effects
  - Pitch shifting
  - Color manipulation
  - Mirror effects
  - Time stretching
  - Wave distortion

- **Audio Processing**
  - Beat detection
  - Audio pitch manipulation
  - Time stretching
  - Volume modulation
  - Stutter effects

- **Supported Libraries**
  - MoviePy
  - FFmpeg
  - Pydub
  - NumPy
  - Pillow
  - SciPy

## 📋 Requirements

```plaintext
Python 3.8 or higher
FFmpeg
```

## 🔧 Installation

1. Clone the repository:
```bash
git clone https://github.com/Lulu2009-YTP/python-ytpmv-generator.git
cd python-ytpmv-generator
```

2. Install required packages:
```bash
pip install -r requirements.txt
```

3. Install FFmpeg (if not already installed):
- **Windows**: Download from [FFmpeg Official Site](https://ffmpeg.org/download.html)
- **Linux**: `sudo apt-get install ffmpeg`
- **macOS**: `brew install ffmpeg`

## 🚀 Quick Start

```python
from ytpmv_generator import YTPMVGenerator

# Initialize generator
generator = YTPMVGenerator()

# Load source materials
generator.load_source("source_video.mp4")
generator.load_audio("music_track.mp3")

# Define effect sequence
effects = ['stutter', 'pitch_shift', 'color', 'stutter']

# Generate YTPMV
generator.create_ytpmv("output_ytpmv.mp4", effects)
```

## 🎨 Available Effects

| Effect Name | Description | Parameters |
|------------|-------------|------------|
| stutter | Creates repeating segments | interval: float |
| pitch_shift | Adjusts video/audio pitch | semitones: int |
| color | Applies color manipulation | intensity: float |
| mirror | Mirrors video horizontally/vertically | direction: str |
| wave | Applies wave distortion | amplitude: float |

## 📖 Documentation

Detailed documentation for all features and effects can be found in the `docs/` directory:
- [Basic Usage Guide](docs/basic_usage.md)
- [Effect Reference](docs/effects.md)
- [Advanced Techniques](docs/advanced.md)

## 🎬 Examples

Check the `examples/` directory for sample projects:
- Basic YTPMV creation
- Complex effect chains
- Audio synchronization
- Custom effect templates

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Inspired by classic Sony Vegas YTPMV techniques
- FFmpeg development team
- MoviePy contributors
- YTPMV community

## 📞 Contact

Lulu2009-YTP - [@YourTwitter](https://twitter.com/YourTwitter)

Project Link: [https://github.com/Lulu2009-YTP/python-ytpmv-generator](https://github.com/Lulu2009-YTP/python-ytpmv-generator)

## 🔄 Latest Updates

- 2025-03-21: Initial release
- Added core video manipulation features
- Implemented basic effect chain system
- Added documentation and examples

---
Created with ❤️ by [Lulu2009-YTP](https://github.com/Lulu2009-YTP)