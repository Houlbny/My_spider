import matroid
from matroid.client import Matroid

api = Matroid(client_id = 'abc', client_secret = '123')

# List available detectors
detectors_to_use = api.list_detectors()

# Classifying a picture from a URL
logo_classification_result = api.classify_image(detector_id = 'test', image_url = 'https://www.matroid.com/images/logo2.png')

# Classifying a picture from a file path
stadium_classification_result = api.classify_image(detector_id = 'test', image_file = '/Users/matroid/Desktop/stadium.jpg')

# Classifying pictures from multiple file paths
famous_people_results = api.classify_image(detector_id = 'test', image_file = ['/home/matroid/taylor.png', '/home/matroid/kanye.jpeg'])

# Begin video classification
classifying_video = api.classify_video(detector_id = 'test', video_file = '/home/matroid/video.mp4')

# Classify YouTube video
classifying_youtube_video = api.classify_video(detector_id = 'test', video_url = 'https://youtube.com/watch?v=abc')

# Get video results
video_results = api.get_video_results(video_id = classifying_video['video_id'], threshold = 0.3, format = 'json')

# Register stream on Matroid
registered_stream = api.create_stream(options = {})

# Monitor stream
options = {
  'start_time': '2017-06-20T20:56:19.096Z',
  'end_time': '2017-06-21T20:00:00.000Z',
  'thresholds': {'cat': 0.5,'dog': 0.7},
  'endpoint': 'http://mydomain.fake:9000/matroid_detections'
}
monitored_stream = api.monitor_stream(stream_id = registered_stream['stream_id'], detector_id = 'test', **options)
# Parameters sent to endpoint: name, detectedAt, detector, screenshotUrl, clipUrl, detections

# Create and train a detector
"""
  zip_file: a zip file containing the images to be used in the detector creation
            the root folder should contain only directories which will become the labels for detection
            each of these directories should contain only a images corresponding to that label
    structure example:
      cat/
        garfield.jpg
        nermal.png
      dog/
        odie.tiff
"""
detector_id = api.create_detector(zip_file = '/home/matroid/catdog.zip', detector_type = 'general')['detector_id']
api.train_detector(detector_id)

# Check on training progress
api.detector_info(detector_id)

# Check your Matroid Credits balance
api.account_info()