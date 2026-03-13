import unittest
from EmotionDetection import emotion_detector


class TestEmotionDetector(unittest.TestCase):

    def test_joy(self):
        response = emotion_detector("I am glad this happened")
        self.assertEqual(response["dominant_emotion"], "joy")

    def test_anger(self):
        response = emotion_detector("I am really mad about this")
        self.assertEqual(response["dominant_emotion"], "anger")

    def test_sadness(self):
        response = emotion_detector("I am very sad today")
        self.assertEqual(response["dominant_emotion"], "sadness")

    def test_fear(self):
        response = emotion_detector("I am scared")
        self.assertEqual(response["dominant_emotion"], "fear")

    def test_disgust(self):
        response = emotion_detector("This is disgusting")
        self.assertEqual(response["dominant_emotion"], "disgust")


if __name__ == "__main__":
    unittest.main()