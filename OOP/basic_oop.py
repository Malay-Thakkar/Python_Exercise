class MediaItem:
    def __init__(self, title, file_path):
        self.__title = title  # Private attribute
        self.__file_path = file_path  
    
    def play(self):  #abstraction
        pass
    
    def get_title(self):
        return self.__title
    
    def set_title(self, title):
        self.__title = title
    
    # Static method to check if a file exists
    @staticmethod
    def file_exists(file_path):
        return True  # For simplicity, assume file exists

    # Class method to create a MediaItem from a file
    @classmethod
    def from_file(cls, file_path):
        title = file_path.split('/')[-1].split('.')[0]  # Extract title from file path
        return cls(title, file_path)


class Image(MediaItem):
    def __init__(self, title, file_path, resolution):
        super().__init__(title, file_path)
        self.__resolution = resolution
    
    def play(self):
        print(f"Displaying image: {self.get_title()}")

    def get_resolution(self):
        return self.__resolution
    
    def set_resolution(self, resolution):
        self.__resolution = resolution


class Video(MediaItem):
    def __init__(self, title, file_path, duration):
        super().__init__(title, file_path)
        self.__duration = duration
    
    def play(self):
        print(f"Playing video: {self.get_title()}")

    def get_duration(self):
        return self.__duration
    
    def set_duration(self, duration):
        self.__duration = duration


class Audio(MediaItem):
    def __init__(self, title, file_path, duration):
        super().__init__(title, file_path)
        self.__duration = duration
    
    def play(self):
        print(f"Playing audio: {self.get_title()}")

    def get_duration(self):
        return self.__duration
    
    def set_duration(self, duration):
        self.__duration = duration

    # Additional method for audio-specific functionality
    def get_audio_info(self):
        return f"Title: {self.get_title()}, Duration: {self.get_duration()}"



# Example usage
image = Image("Nature", "nature.jpg", "1920x1080")
video = Video("Demo", "demo.mp4", "5:30")
audio = Audio("Song", "song.mp3", "4:20")
media_items = [image, video, audio]

for item in media_items:
    item.play()

print(audio.get_audio_info()) 
# Accessing static method
print(MediaItem.file_exists("example.txt"))

# Accessing class method
file_media_item = MediaItem.from_file("example.txt")
print(file_media_item.get_title())  # Output: example
