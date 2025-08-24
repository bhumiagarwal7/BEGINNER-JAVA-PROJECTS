import re

class AIMoodDetector:
    def _init_(self):
        # Simple keyword-based emotion dictionary
        self.emotion_dict = {
            'happy':    ['happy', 'joy', 'glad', 'delighted', 'excited', 'pleased', 'content', 'smile', 'wonderful', 'great', 'awesome', 'love'],
            'sad':      ['sad', 'unhappy', 'depressed', 'down', 'miserable', 'cry', 'upset', 'disappointed', 'gloomy'],
            'angry':    ['angry', 'mad', 'furious', 'annoyed', 'irritated', 'hate', 'rage', 'upset'],
            'surprised':['surprised', 'shocked', 'amazed', 'astonished', 'wow', 'unexpected'],
            'fear':     ['afraid', 'scared', 'fear', 'terrified', 'nervous', 'worried', 'anxious'],
            'neutral':  ['ok', 'fine', 'neutral', 'meh', 'alright']
        }
        self._emotion_pattern = {emotion: re.compile('|'.join([re.escape(w) for w in words]), re.IGNORECASE)
                                 for emotion, words in self.emotion_dict.items()}

    def analyze_text(self, text):
        scores = {emotion: 0 for emotion in self.emotion_dict}
        for emotion, pattern in self._emotion_pattern.items():
            scores[emotion] += len(pattern.findall(text))
        # Pick the highest scoring mood
        max_emotion = max(scores, key=lambda k: scores[k])
        if scores[max_emotion] == 0:
            return {'mood': 'unknown', 'scores': scores, 'feedback': 'No clear emotion detected.'}
        feedback = f"The tone of your writing appears to be '{max_emotion}'."
        return {'mood': max_emotion, 'scores': scores, 'feedback': feedback}

if __name__ == "_main_":
    detector = AIMoodDetector()
    print("Type a short message (social media post, chat, etc.):")
    user_text = input("> ")
    result = detector.analyze_text(user_text)
