from .crystalcore_os import CrystalCore
from .emotional_intelligence import EmotionalIntelligence
from .active_learning import ActiveLearningQueue, ActiveLearner
from .training_pipeline import EmotionModelTrainer

try:
    from .huggingface_trainer import CrystalCoreEI, EMOTION_LABEL_MAP, EMOTION_LABEL_MAP_REV
except ImportError:
    CrystalCoreEI = None
    EMOTION_LABEL_MAP = None
    EMOTION_LABEL_MAP_REV = None

try:
    from .multimodal_emotion import (
        MultimodalEI,
        AudioEmotionDetector,
        VisualEmotionDetector,
        MultimodalEmotionFusion,
    )
except ImportError:
    MultimodalEI = None
    AudioEmotionDetector = None
    VisualEmotionDetector = None
    MultimodalEmotionFusion = None

__all__ = [
    "CrystalCore",
    "EmotionalIntelligence",
    "ActiveLearningQueue",
    "ActiveLearner",
    "EmotionModelTrainer",
    "CrystalCoreEI",
    "EMOTION_LABEL_MAP",
    "EMOTION_LABEL_MAP_REV",
    "MultimodalEI",
    "AudioEmotionDetector",
    "VisualEmotionDetector",
    "MultimodalEmotionFusion",
]
