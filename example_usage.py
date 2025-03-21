from ytpmv_generator import YTPMVGenerator

def main():
    generator = YTPMVGenerator()
    
    # Load source materials
    generator.load_source("source_video.mp4")
    generator.load_audio("music_track.mp3")
    
    # Define effect sequence
    effects = ['stutter', 'pitch_shift', 'color', 'stutter']
    
    # Generate YTPMV
    generator.create_ytpmv("output_ytpmv.mp4", effects)

if __name__ == "__main__":
    main()