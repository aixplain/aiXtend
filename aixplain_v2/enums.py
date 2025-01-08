# This is an auto generated module. PLEASE DO NOT EDIT


from enum import Enum
from .enums_include import *


class Function(str, Enum):
    OBJECT_DETECTION = "object-detection"
    TEXT_EMBEDDING = "text-embedding"
    SEMANTIC_SEGMENTATION = "semantic-segmentation"
    REFERENCELESS_AUDIO_GENERATION_METRIC = "referenceless-audio-generation-metric"
    SCRIPT_EXECUTION = "script-execution"
    IMAGE_IMPAINTING = "image-impainting"
    IMAGE_EMBEDDING = "image-embedding"
    METRIC_AGGREGATION = "metric-aggregation"
    SPEECH_TRANSLATION = "speech-translation"
    DEPTH_ESTIMATION = "depth-estimation"
    NOISE_REMOVAL = "noise-removal"
    DIACRITIZATION = "diacritization"
    AUDIO_TRANSCRIPT_ANALYSIS = "audio-transcript-analysis"
    EXTRACT_AUDIO_FROM_VIDEO = "extract-audio-from-video"
    AUDIO_RECONSTRUCTION = "audio-reconstruction"
    CLASSIFICATION_METRIC = "classification-metric"
    TEXT_GENERATION_METRIC = "text-generation-metric"
    TEXT_SPAM_DETECTION = "text-spam-detection"
    TEXT_TO_IMAGE_GENERATION = "text-to-image-generation"
    VOICE_CLONING = "voice-cloning"
    TEXT_SEGMENATION = "text-segmenation"
    BENCHMARK_SCORING_MT = "benchmark-scoring-mt"
    IMAGE_MANIPULATION = "image-manipulation"
    NAMED_ENTITY_RECOGNITION = "named-entity-recognition"
    OFFENSIVE_LANGUAGE_IDENTIFICATION = "offensive-language-identification"
    SEARCH = "search"
    SENTIMENT_ANALYSIS = "sentiment-analysis"
    IMAGE_COLORIZATION = "image-colorization"
    SPEECH_CLASSIFICATION = "speech-classification"
    DIALECT_DETECTION = "dialect-detection"
    VIDEO_LABEL_DETECTION = "video-label-detection"
    SPEECH_SYNTHESIS = "speech-synthesis"
    SPLIT_ON_SILENCE = "split-on-silence"
    EXPRESSION_DETECTION = "expression-detection"
    AUTO_MASK_GENERATION = "auto-mask-generation"
    DOCUMENT_IMAGE_PARSING = "document-image-parsing"
    ENTITY_LINKING = "entity-linking"
    REFERENCELESS_TEXT_GENERATION_METRIC_DEFAULT = "referenceless-text-generation-metric-default"
    FILL_TEXT_MASK = "fill-text-mask"
    SUBTITLING_TRANSLATION = "subtitling-translation"
    INSTANCE_SEGMENTATION = "instance-segmentation"
    UTILITIES = "utilities"
    VISEME_GENERATION = "viseme-generation"
    AUDIO_GENERATION_METRIC = "audio-generation-metric"
    VIDEO_UNDERSTANDING = "video-understanding"
    TEXT_NORMALIZATION = "text-normalization"
    ASR_QUALITY_ESTIMATION = "asr-quality-estimation"
    VOICE_ACTIVITY_DETECTION = "voice-activity-detection"
    SPEECH_NON_SPEECH_CLASSIFICATION = "speech-non-speech-classification"
    AUDIO_TRANSCRIPT_IMPROVEMENT = "audio-transcript-improvement"
    TEXT_CONTENT_MODERATION = "text-content-moderation"
    EMOTION_DETECTION = "emotion-detection"
    AUDIO_FORCED_ALIGNMENT = "audio-forced-alignment"
    VIDEO_CONTENT_MODERATION = "video-content-moderation"
    IMAGE_LABEL_DETECTION = "image-label-detection"
    VIDEO_FORCED_ALIGNMENT = "video-forced-alignment"
    TEXT_GENERATION = "text-generation"
    TEXT_CLASSIFICATION = "text-classification"
    SPEECH_EMBEDDING = "speech-embedding"
    TOPIC_CLASSIFICATION = "topic-classification"
    TRANSLATION = "translation"
    SPEECH_RECOGNITION = "speech-recognition"
    SUBTITLING = "subtitling"
    IMAGE_CAPTIONING = "image-captioning"
    AUDIO_LANGUAGE_IDENTIFICATION = "audio-language-identification"
    VIDEO_EMBEDDING = "video-embedding"
    ASR_AGE_CLASSIFICATION = "asr-age-classification"
    AUDIO_INTENT_DETECTION = "audio-intent-detection"
    LANGUAGE_IDENTIFICATION = "language-identification"
    OCR = "ocr"
    ASR_GENDER_CLASSIFICATION = "asr-gender-classification"
    LANGUAGE_IDENTIFICATION_AUDIO = "language-identification-audio"
    BASE_MODEL = "base-model"
    LOGLIKELIHOOD = "loglikelihood"
    IMAGE_TO_VIDEO_GENERATION = "image-to-video-generation"
    PART_OF_SPEECH_TAGGING = "part-of-speech-tagging"
    BENCHMARK_SCORING_ASR = "benchmark-scoring-asr"
    VISUAL_QUESTION_ANSWERING = "visual-question-answering"
    DOCUMENT_INFORMATION_EXTRACTION = "document-information-extraction"
    VIDEO_GENERATION = "video-generation"
    MULTI_CLASS_IMAGE_CLASSIFICATION = "multi-class-image-classification"
    STYLE_TRANSFER = "style-transfer"
    MULTI_CLASS_TEXT_CLASSIFICATION = "multi-class-text-classification"
    INTENT_CLASSIFICATION = "intent-classification"
    MULTI_LABEL_TEXT_CLASSIFICATION = "multi-label-text-classification"
    TEXT_RECONSTRUCTION = "text-reconstruction"
    FACT_CHECKING = "fact-checking"
    INVERSE_TEXT_NORMALIZATION = "inverse-text-normalization"
    TEXT_TO_AUDIO = "text-to-audio"
    IMAGE_COMPRESSION = "image-compression"
    MULTILINGUAL_SPEECH_RECOGNITION = "multilingual-speech-recognition"
    TEXT_GENERATION_METRIC_DEFAULT = "text-generation-metric-default"
    REFERENCELESS_TEXT_GENERATION_METRIC = "referenceless-text-generation-metric"
    AUDIO_EMOTION_DETECTION = "audio-emotion-detection"
    KEYWORD_SPOTTING = "keyword-spotting"
    TEXT_SUMMARIZATION = "text-summarization"
    SPLIT_ON_LINEBREAK = "split-on-linebreak"
    OTHER_MULTIPURPOSE = "other-(multipurpose)"
    SPEAKER_DIARIZATION_AUDIO = "speaker-diarization-audio"
    IMAGE_CONTENT_MODERATION = "image-content-moderation"
    TEXT_DENORMALIZATION = "text-denormalization"
    SPEAKER_DIARIZATION_VIDEO = "speaker-diarization-video"
    TEXT_TO_VIDEO_GENERATION = "text-to-video-generation"

class Supplier(Enum):
    APLICATA = {"id": "1409", "name": "Aplicata", "code": "aplicata"}
    AZURE = {"id": "1766", "name": "Microsoft", "code": "azure"}
    SDAIA = {"id": "210", "name": "SDAIA", "code": "sdaia"}
    BRITISHTELECOM = {"id": "1767", "name": "British Telecommunications", "code": "britishtelecom"}
    META = {"id": "1768", "name": "Meta", "code": "meta"}
    APPTEK_SPACETOON = {"id": "1796", "name": "AppTek-SpaceToon", "code": "apptek-spacetoon"}
    GOOGLE = {"id": "1769", "name": "Google", "code": "google"}
    APPTEK = {"id": "1797", "name": "AppTek2", "code": "apptek"}
    HOUNDIFY = {"id": "1770", "name": "Houndify", "code": "houndify"}
    TREATMENT = {"id": "1807", "name": "Treatment", "code": "treatment"}
    HUGGINGFACE = {"id": "1771", "name": "HuggingFace", "code": "huggingface"}
    UNBABEL = {"id": "1808", "name": "Unbabel", "code": "unbabel"}
    DEEPGRAM = {"id": "1799", "name": "Deepgram", "code": "deepgram"}
    EBAY = {"id": "1800", "name": "eBay", "code": "ebay"}
    IDENTV = {"id": "1801", "name": "IdenTV", "code": "identv"}
    PANGEANIC = {"id": "1802", "name": "Pangeanic", "code": "pangeanic"}
    RAMSA = {"id": "1804", "name": "Ramsa", "code": "ramsa"}
    RDI = {"id": "1805", "name": "RDI", "code": "rdi"}
    SUKOON = {"id": "1806", "name": "Sukoon", "code": "sukoon"}
    KATEB = {"id": "1772", "name": "Kateb", "code": "kateb"}
    KLANGOO = {"id": "1773", "name": "Klangoo", "code": "klangoo"}
    MODERMT = {"id": "1775", "name": "ModernMT", "code": "modermt"}
    NVIDIA = {"id": "1776", "name": "Nvidia", "code": "nvidia"}
    VECTARA = {"id": "2927", "name": "Vectara", "code": "vectara"}
    OPENAI = {"id": "1777", "name": "OpenAI", "code": "openai"}
    PICOVOICE = {"id": "1778", "name": "Picovoice", "code": "picovoice"}
    PURETALKAI = {"id": "1779", "name": "Puretalk.ai", "code": "puretalkai"}
    PYANNOTE = {"id": "1780", "name": "Pyannote", "code": "pyannote"}
    REVAI = {"id": "1781", "name": "RevAI", "code": "revai"}
    SACREBLEU = {"id": "1782", "name": "Sacrebleu", "code": "sacrebleu"}
    SAUTECH = {"id": "1783", "name": "SauTech", "code": "sautech"}
    STREAMN = {"id": "1785", "name": "StreamN", "code": "streamn"}
    UNIVERSITYOFHELSINKI = {"id": "1786", "name": "University of Helsinki", "code": "universityofhelsinki"}
    VUMICHIEN = {"id": "1787", "name": "Vumichien", "code": "vumichien"}
    YDSHIEH = {"id": "1788", "name": "Ydshieh", "code": "ydshieh"}
    YOURTTS = {"id": "1789", "name": "YourTTS", "code": "yourtts"}
    AWS = {"id": "1763", "name": "AWS", "code": "aws"}
    CORE42 = {"id": "12371", "name": "Core42", "code": "core42"}
    SCALESERP = {"id": "10473", "name": "Scale SERP", "code": "scaleserp"}
    SPEECHMATICS = {"id": "10930", "name": "Speechmatics", "code": "speechmatics"}
    IBM = {"id": "10931", "name": "IBM", "code": "ibm"}
    ELEVENLABS = {"id": "10482", "name": "ElevenLabs", "code": "elevenlabs"}
    73 = {"id": "73", "name": "Miqdad Dali", "code": "73"}
    TIMECHAT = {"id": "11688", "name": "TimeChat", "code": "timechat"}
    PLAYHT = {"id": "14573", "name": "PlayHT", "code": "playht"}
    WIKIPEDIA = {"id": "11150", "name": "Wikipedia", "code": "wikipedia"}
    CREWAI = {"id": "16094", "name": "Crewai", "code": "crewai"}
    OPENWEATHER = {"id": "16249", "name": "OpenWeather", "code": "openweather"}
    AIXPLAIN = {"id": "1", "name": "aiXplain", "code": "aixplain"}
    MARITACA_AI = {"id": "17296", "name": "Maritaca AI", "code": "maritaca-ai"}
    TOGETHER_AI = {"id": "17845", "name": "Together Ai", "code": "together-ai"}
    SAMBANOVA = {"id": "17861", "name": "SambaNova", "code": "sambanova"}
    FIREWORKS_AI = {"id": "17852", "name": "Fireworks AI", "code": "fireworks-ai"}
    HUME_AI = {"id": "17905", "name": "Hume Ai", "code": "hume-ai"}
    GROQ = {"id": "6839", "name": "Groq", "code": "groq"}
    TAVILY = {"id": "19379", "name": "Tavily", "code": "tavily"}
    CEREBRAS = {"id": "19790", "name": "Cerebras", "code": "cerebras"}
    FIRECRAWL = {"id": "20131", "name": "Firecrawl", "code": "firecrawl"}
    DEEPINFRA = {"id": "20164", "name": "Deepinfra", "code": "deepinfra"}
    STABILITYAI = {"id": "1784", "name": "Stability AI", "code": "stabilityai"}
    RESEMBLEAI = {"id": "14588", "name": "Resemble AI", "code": "resembleai"}
    MISTRALAI = {"id": "14770", "name": "Mistral AI", "code": "mistralai"}
    QCRI = {"id": "1803", "name": "QCRI", "code": "qcri"}
    MYSHELL = {"id": "11238", "name": "MyShell AI", "code": "myshell"}

class Language(Enum):
    AFRIKAANS = {"language": "af", "dialect": ""}
    AFRIKAANS_SOUTH_AFRICA = {"language": "af", "dialect": "South Africa"}
    ALBANIAN = {"language": "sq", "dialect": ""}
    ALBANIAN_ALBANIA = {"language": "sq", "dialect": "Albania"}
    ARMENIAN = {"language": "hy", "dialect": ""}
    ARMENIAN_ARMENIA = {"language": "hy", "dialect": "Armenia"}
    ASSAMESE = {"language": "asm", "dialect": ""}
    BANGLA = {"language": "bn", "dialect": ""}
    BANGLA_BANGLADESH = {"language": "bn", "dialect": "Bangladesh"}
    BANGLA_INDIA = {"language": "bn", "dialect": "India"}
    BASQUE = {"language": "eu", "dialect": ""}
    BASQUE_SPAIN = {"language": "eu", "dialect": "Spain"}
    BULGARIAN = {"language": "bg", "dialect": ""}
    BULGARIAN_BULGARY = {"language": "bg", "dialect": "Bulgary"}
    BULGARIAN_BULGARIA = {"language": "bg", "dialect": "Bulgaria"}
    CATALAN = {"language": "ca", "dialect": ""}
    CATALAN_SPAIN = {"language": "ca", "dialect": "Spain"}
    CEBUANO = {"language": "ceb", "dialect": ""}
    CORSICAN = {"language": "co", "dialect": ""}
    CZECH = {"language": "cs", "dialect": ""}
    CZECH_CZECH_REPUBLIC = {"language": "cs", "dialect": "Czech Republic"}
    CZECH_CZECH = {"language": "cs", "dialect": "Czech"}
    DIVEHI = {"language": "dv", "dialect": ""}
    ESPERANTO = {"language": "eo", "dialect": ""}
    ESTONIAN = {"language": "et", "dialect": ""}
    ESTONIAN_ESTONIA = {"language": "et", "dialect": "Estonia"}
    FIJIAN = {"language": "fj", "dialect": ""}
    FINNISH = {"language": "fi", "dialect": ""}
    FINNISH_FINLAND = {"language": "fi", "dialect": "Finland"}
    GERMAN = {"language": "de", "dialect": ""}
    GERMAN_GERMANY = {"language": "de", "dialect": "Germany"}
    GERMAN_AUSTRIA = {"language": "de", "dialect": "Austria"}
    GERMAN_SWITZERLAND = {"language": "de", "dialect": "Switzerland"}
    GREEK = {"language": "el", "dialect": ""}
    GREEK_GREECE = {"language": "el", "dialect": "Greece"}
    HAITIAN = {"language": "ht", "dialect": ""}
    HAUSA = {"language": "ha", "dialect": ""}
    HAWAIIAN = {"language": "haw", "dialect": ""}
    ICELANDIC = {"language": "isl", "dialect": ""}
    IGBO = {"language": "ig", "dialect": ""}
    INDONESIAN = {"language": "id", "dialect": ""}
    INDONESIAN_INDONESIA = {"language": "id", "dialect": "Indonesia"}
    INUKTITUT = {"language": "iu", "dialect": ""}
    IRISH = {"language": "ga", "dialect": ""}
    IRISH_IRELAND = {"language": "ga", "dialect": "Ireland"}
    JAPANESE = {"language": "ja", "dialect": ""}
    JAPANESE_JAPAN = {"language": "ja", "dialect": "Japan"}
    KAZAKH = {"language": "kk", "dialect": ""}
    KAZAKH_KAZAKHSTAN = {"language": "kk", "dialect": "Kazakhstan"}
    KINYARWANDA = {"language": "rw", "dialect": ""}
    KLINGON = {"language": "tlh", "dialect": ""}
    KOREAN = {"language": "ko", "dialect": ""}
    KOREAN_KOREA = {"language": "ko", "dialect": "Korea"}
    KURDISH = {"language": "ku", "dialect": ""}
    KYRGYZ = {"language": "ky", "dialect": ""}
    LUXEMBOURGISH = {"language": "lb", "dialect": ""}
    LUXEMBOURGISH_SOUTH_AFRICA = {"language": "lb", "dialect": "South Africa"}
    MACEDONIAN = {"language": "mk", "dialect": ""}
    MACEDONIAN_NORTH_MACEDONIA = {"language": "mk", "dialect": "North Macedonia"}
    MALTESE = {"language": "mt", "dialect": ""}
    MALTESE_MALTA = {"language": "mt", "dialect": "Malta"}
    MAORI = {"language": "mi", "dialect": ""}
    MONGOLIAN = {"language": "mn", "dialect": ""}
    MONGOLIAN_MONGOLIA = {"language": "mn", "dialect": "Mongolia"}
    AMHARIC = {"language": "am", "dialect": ""}
    AMHARIC_ETHIOPIA = {"language": "am", "dialect": "Ethiopia"}
    ODIA = {"language": "or", "dialect": ""}
    ROMANIAN = {"language": "ro", "dialect": ""}
    ROMANIAN_ROMANIA = {"language": "ro", "dialect": "Romania"}
    ARABIC = {"language": "ar", "dialect": ""}
    ARABIC_CLASSICAL_ARABIC = {"language": "ar", "dialect": "Classical Arabic"}
    ARABIC_UNITED_ARAB_EMIRATES = {"language": "ar", "dialect": "United Arab Emirates"}
    ARABIC_EGYPT = {"language": "ar", "dialect": "Egypt"}
    ARABIC_MOROCCO = {"language": "ar", "dialect": "Morocco"}
    ARABIC_SAUDI_ARABIA = {"language": "ar", "dialect": "Saudi Arabia"}
    ARABIC_MODERN_STANDARD_ARABIC = {"language": "ar", "dialect": "Modern Standard Arabic"}
    ARABIC_QATAR = {"language": "ar", "dialect": "Qatar"}
    ARABIC_IRAQ = {"language": "ar", "dialect": "Iraq"}
    ARABIC_OMAN = {"language": "ar", "dialect": "Oman"}
    ARABIC_TUNISIA = {"language": "ar", "dialect": "Tunisia"}
    ARABIC_YEMEN = {"language": "ar", "dialect": "Yemen"}
    ARABIC_KUWAIT = {"language": "ar", "dialect": "Kuwait"}
    ARABIC_PALESTINE = {"language": "ar", "dialect": "Palestine"}
    ARABIC_ALGERIA = {"language": "ar", "dialect": "Algeria"}
    ARABIC_GULF = {"language": "ar", "dialect": "Gulf"}
    ARABIC_BAHRAIN = {"language": "ar", "dialect": "Bahrain"}
    ARABIC_JORDAN = {"language": "ar", "dialect": "Jordan"}
    ARABIC_LIBYA = {"language": "ar", "dialect": "Libya"}
    ARABIC_ISRAEL = {"language": "ar", "dialect": "Israel"}
    ARABIC_AUTO_DETECT = {"language": "ar", "dialect": "Auto-Detect"}
    ARABIC_LEBANON = {"language": "ar", "dialect": "Lebanon"}
    ARABIC_SYRIA = {"language": "ar", "dialect": "Syria"}
    AZERBAIJANI = {"language": "az", "dialect": ""}
    AZERBAIJANI_AZERBAIJAN = {"language": "az", "dialect": "Azerbaijan"}
    BASHKIR = {"language": "ba", "dialect": ""}
    BOSNIAN = {"language": "bs", "dialect": ""}
    BOSNIAN_BOSNIA = {"language": "bs", "dialect": "Bosnia"}
    BELARUSIAN = {"language": "be", "dialect": ""}
    BURMESE = {"language": "my", "dialect": ""}
    BURMESE_MYANMAR = {"language": "my", "dialect": "Myanmar"}
    DANISH = {"language": "da", "dialect": ""}
    DANISH_DENMARK = {"language": "da", "dialect": "Denmark"}
    NYANJA = {"language": "ny", "dialect": ""}
    PASHTO = {"language": "ps", "dialect": ""}
    POLISH = {"language": "pl", "dialect": ""}
    POLISH_POLAND = {"language": "pl", "dialect": "Poland"}
    PUNJABI = {"language": "pa", "dialect": ""}
    PUNJABI_INDIA = {"language": "pa", "dialect": "India"}
    PUNJABI_GURMUKHI_INDIA = {"language": "pa", "dialect": "Gurmukhi India"}
    QUERETARO = {"language": "oto", "dialect": ""}
    RUSSIAN = {"language": "ru", "dialect": ""}
    RUSSIAN_RUSSIA = {"language": "ru", "dialect": "Russia"}
    SERBIAN = {"language": "sr", "dialect": ""}
    SERBIAN_SERBIA = {"language": "sr", "dialect": "Serbia"}
    SHONA = {"language": "sn", "dialect": ""}
    SINDHI = {"language": "sd", "dialect": ""}
    SLOVAK = {"language": "sk", "dialect": ""}
    SLOVAK_SLOVAKIA = {"language": "sk", "dialect": "Slovakia"}
    SOMALI = {"language": "so", "dialect": ""}
    SOMALI_SOMALIA = {"language": "so", "dialect": "Somalia"}
    SWAHILI = {"language": "sw", "dialect": ""}
    SWAHILI_KENYA = {"language": "sw", "dialect": "Kenya"}
    SWAHILI_TANZANIA = {"language": "sw", "dialect": "Tanzania"}
    TAGALOG = {"language": "tl", "dialect": ""}
    TAHITIAN = {"language": "ty", "dialect": ""}
    TAJIK = {"language": "tg", "dialect": ""}
    TATAR = {"language": "tt", "dialect": ""}
    TELUGU = {"language": "te", "dialect": ""}
    TELUGU_INDIA = {"language": "te", "dialect": "India"}
    TIBETAN = {"language": "bo", "dialect": ""}
    TONGAN = {"language": "to", "dialect": ""}
    TURKISH = {"language": "tr", "dialect": ""}
    TURKISH_TURKEY = {"language": "tr", "dialect": "Turkey"}
    UZBEK = {"language": "uz", "dialect": ""}
    UZBEK_UZBEKISTAN = {"language": "uz", "dialect": "Uzbekistan"}
    VIETNAMESE = {"language": "vi", "dialect": ""}
    VIETNAMESE_VIETNAM = {"language": "vi", "dialect": "Vietnam"}
    WELSH = {"language": "cy", "dialect": ""}
    XHOSA = {"language": "xh", "dialect": ""}
    YUCATEC = {"language": "yua", "dialect": ""}
    ZULU = {"language": "zu", "dialect": ""}
    PERSIAN = {"language": "fa", "dialect": ""}
    PERSIAN_IRAN = {"language": "fa", "dialect": "Iran"}
    PERSIAN_PERSIAN = {"language": "fa", "dialect": "Persian"}
    PORTUGUESE = {"language": "pt", "dialect": ""}
    PORTUGUESE_PORTUGAL = {"language": "pt", "dialect": "Portugal"}
    PORTUGUESE_BRAZIL = {"language": "pt", "dialect": "Brazil"}
    PORTUGUESE_EUROPEAN = {"language": "pt", "dialect": "European"}
    PORTUGUESE_BRAZILIAN = {"language": "pt", "dialect": "Brazilian"}
    CHINESE = {"language": "zh", "dialect": ""}
    CHINESE_MANDARIN = {"language": "zh", "dialect": "Mandarin"}
    CHINESE_HONG_KONG = {"language": "zh", "dialect": "Hong Kong"}
    CHINESE_TAIWANESE_MANDARIN = {"language": "zh", "dialect": "Taiwanese, Mandarin"}
    CHINESE_TRADITIONAL = {"language": "zh", "dialect": "Traditional"}
    CROATIAN = {"language": "hr", "dialect": ""}
    CROATIAN_CROATIA = {"language": "hr", "dialect": "Croatia"}
    FILIPINO = {"language": "fil", "dialect": ""}
    FILIPINO_PHILIPPINES = {"language": "fil", "dialect": "Philippines"}
    FILIPINO_TAGALOG = {"language": "fil", "dialect": "Tagalog"}
    GUJARATI = {"language": "gu", "dialect": ""}
    GUJARATI_INDIAN = {"language": "gu", "dialect": "Indian"}
    GUJARATI_INDIA = {"language": "gu", "dialect": "India"}
    HMONG = {"language": "hmn", "dialect": ""}
    LATVIAN = {"language": "lv", "dialect": ""}
    LATVIAN_LATVIA = {"language": "lv", "dialect": "Latvia"}
    LITHUANIAN = {"language": "lt", "dialect": ""}
    LITHUANIAN_LITHUANIA = {"language": "lt", "dialect": "Lithuania"}
    UYGHUR = {"language": "ug", "dialect": ""}
    DARI = {"language": "prs", "dialect": ""}
    DUTCH = {"language": "nl", "dialect": ""}
    DUTCH_BELGIUM = {"language": "nl", "dialect": "Belgium"}
    DUTCH_NETHERLANDS = {"language": "nl", "dialect": "Netherlands"}
    ENGLISH = {"language": "en", "dialect": ""}
    ENGLISH_UNITED_STATES = {"language": "en", "dialect": "United States"}
    ENGLISH_UNITED_KINGDOM = {"language": "en", "dialect": "United Kingdom"}
    ENGLISH_INDIA = {"language": "en", "dialect": "India"}
    ENGLISH_WELSH = {"language": "en", "dialect": "Welsh"}
    ENGLISH_AUSTRALIA = {"language": "en", "dialect": "Australia"}
    ENGLISH_NIGERIA = {"language": "en", "dialect": "Nigeria"}
    ENGLISH_NEW_ZEALAND = {"language": "en", "dialect": "New Zealand"}
    ENGLISH_KENYA = {"language": "en", "dialect": "Kenya"}
    ENGLISH_PHILIPPINES = {"language": "en", "dialect": "Philippines"}
    ENGLISH_INDIAN = {"language": "en", "dialect": "Indian"}
    ENGLISH_AUSTRALIAN = {"language": "en", "dialect": "Australian"}
    ENGLISH_HONG_KONG = {"language": "en", "dialect": "Hong Kong"}
    ENGLISH_SOUTH_AFRICA = {"language": "en", "dialect": "South Africa"}
    ENGLISH_GHANA = {"language": "en", "dialect": "Ghana"}
    ENGLISH_SINGAPORE = {"language": "en", "dialect": "Singapore"}
    ENGLISH_IRELAND = {"language": "en", "dialect": "Ireland"}
    ENGLISH_CANADA = {"language": "en", "dialect": "Canada"}
    ENGLISH_TANZANIA = {"language": "en", "dialect": "Tanzania"}
    ENGLISH_SCOTTISH = {"language": "en", "dialect": "Scottish"}
    ENGLISH_PAKISTAN = {"language": "en", "dialect": "Pakistan"}
    FRENCH = {"language": "fr", "dialect": ""}
    FRENCH_CANADA = {"language": "fr", "dialect": "Canada"}
    FRENCH_FRANCE = {"language": "fr", "dialect": "France"}
    FRENCH_SWITZERLAND = {"language": "fr", "dialect": "Switzerland"}
    FRENCH_BELGIUM = {"language": "fr", "dialect": "Belgium"}
    FRENCH_CANADIAN = {"language": "fr", "dialect": "Canadian"}
    GEORGIAN = {"language": "ka", "dialect": ""}
    GEORGIAN_GEORGIA = {"language": "ka", "dialect": "Georgia"}
    GALICIAN = {"language": "gl", "dialect": ""}
    GALICIAN_SPAIN = {"language": "gl", "dialect": "Spain"}
    FRISIAN = {"language": "fy", "dialect": ""}
    HEBREW = {"language": "he", "dialect": ""}
    HEBREW_ISRAEL = {"language": "he", "dialect": "Israel"}
    HUNGARIAN = {"language": "hu", "dialect": ""}
    HUNGARIAN_HUNGARY = {"language": "hu", "dialect": "Hungary"}
    HINDI = {"language": "hi", "dialect": ""}
    HINDI_INDIA = {"language": "hi", "dialect": "India"}
    ITALIAN = {"language": "it", "dialect": ""}
    ITALIAN_ITALY = {"language": "it", "dialect": "Italy"}
    ITALIAN_SWITZERLAND = {"language": "it", "dialect": "Switzerland"}
    KANNADA = {"language": "kn", "dialect": ""}
    KANNADA_INDIA = {"language": "kn", "dialect": "India"}
    JAVANESE = {"language": "jv", "dialect": ""}
    JAVANESE_INDONESIA = {"language": "jv", "dialect": "Indonesia"}
    KHMER = {"language": "km", "dialect": ""}
    KHMER_CAMBODIA = {"language": "km", "dialect": "Cambodia"}
    LAO = {"language": "lo", "dialect": ""}
    LAO_LAOS = {"language": "lo", "dialect": "Laos"}
    MALAGASY = {"language": "mg", "dialect": ""}
    MALAY = {"language": "ms", "dialect": ""}
    MALAY_MALAYSIA = {"language": "ms", "dialect": "Malaysia"}
    MALAYALAM = {"language": "ml", "dialect": ""}
    MALAYALAM_INDIA = {"language": "ml", "dialect": "India"}
    MARATHI = {"language": "mr", "dialect": ""}
    MARATHI_INDIA = {"language": "mr", "dialect": "India"}
    NEPALI = {"language": "ne", "dialect": ""}
    NEPALI_NEPAL = {"language": "ne", "dialect": "Nepal"}
    NORWEGIAN = {"language": "no", "dialect": ""}
    NORWEGIAN_NORWAY = {"language": "no", "dialect": "Norway"}
    SAMOAN = {"language": "sm", "dialect": ""}
    SESOTHO = {"language": "st", "dialect": ""}
    SCOTS_GAELIC = {"language": "gd", "dialect": ""}
    SINHALA = {"language": "si", "dialect": ""}
    SINHALA_SRI_LANKA = {"language": "si", "dialect": "Sri Lanka"}
    SLOVENIAN = {"language": "sl", "dialect": ""}
    SLOVENIAN_SLOVENIA = {"language": "sl", "dialect": "Slovenia"}
    SWEDISH = {"language": "sv", "dialect": ""}
    SWEDISH_SWEDEN = {"language": "sv", "dialect": "Sweden"}
    YORUBA = {"language": "yo", "dialect": ""}
    SPANISH = {"language": "es", "dialect": ""}
    SPANISH_DOMINICAN_REPUBLIC = {"language": "es", "dialect": "Dominican Republic"}
    SPANISH_MEXICO = {"language": "es", "dialect": "Mexico"}
    SPANISH_PUERTO_RICO = {"language": "es", "dialect": "Puerto Rico"}
    SPANISH_EQUATORIAL_GUINEA = {"language": "es", "dialect": "Equatorial Guinea"}
    SPANISH_MEXICAN = {"language": "es", "dialect": "Mexican"}
    SPANISH_VENEZUELA = {"language": "es", "dialect": "Venezuela"}
    SPANISH_GUATEMALA = {"language": "es", "dialect": "Guatemala"}
    SPANISH_NICARAGUA = {"language": "es", "dialect": "Nicaragua"}
    SPANISH_PARAGUAY = {"language": "es", "dialect": "Paraguay"}
    SPANISH_URUGUAY = {"language": "es", "dialect": "Uruguay"}
    SPANISH_COLOMBIA = {"language": "es", "dialect": "Colombia"}
    SPANISH_PANAMA = {"language": "es", "dialect": "Panama"}
    SPANISH_UNITED_STATES = {"language": "es", "dialect": "United States"}
    SPANISH_ECUADOR = {"language": "es", "dialect": "Ecuador"}
    SPANISH_ARGENTINA = {"language": "es", "dialect": "Argentina"}
    SPANISH_SPAIN = {"language": "es", "dialect": "Spain"}
    SPANISH_HONDURAS = {"language": "es", "dialect": "Honduras"}
    SPANISH_CHILE = {"language": "es", "dialect": "Chile"}
    SPANISH_CUBA = {"language": "es", "dialect": "Cuba"}
    SPANISH_COSTA_RICA = {"language": "es", "dialect": "Costa Rica"}
    SPANISH_PERU = {"language": "es", "dialect": "Peru"}
    SPANISH_EL_SALVADOR = {"language": "es", "dialect": "El Salvador"}
    SPANISH_BOLIVIA = {"language": "es", "dialect": "Bolivia"}
    SPANISH_EUROPEAN = {"language": "es", "dialect": "European"}
    SUNDANESE = {"language": "su", "dialect": ""}
    SUNDANESE_INDONESIA = {"language": "su", "dialect": "Indonesia"}
    TURKMEN = {"language": "tk", "dialect": ""}
    TAMIL = {"language": "ta", "dialect": ""}
    TAMIL_SRI_LANKA = {"language": "ta", "dialect": "Sri Lanka"}
    TAMIL_INDIA = {"language": "ta", "dialect": "India"}
    TAMIL_SINGAPORE = {"language": "ta", "dialect": "Singapore"}
    TAMIL_MALAYSIA = {"language": "ta", "dialect": "Malaysia"}
    THAI = {"language": "th", "dialect": ""}
    THAI_THAILAND = {"language": "th", "dialect": "Thailand"}
    TIGRINYA = {"language": "tir", "dialect": ""}
    UKRAINIAN = {"language": "ukr", "dialect": ""}
    UKRAINIAN_UKRAINE = {"language": "ukr", "dialect": "Ukraine"}
    YIDDISH = {"language": "yi", "dialect": ""}
    URDU = {"language": "ur", "dialect": ""}
    URDU_PAKISTAN = {"language": "ur", "dialect": "Pakistan"}
    URDU_INDIA = {"language": "ur", "dialect": "India"}

class License(str, Enum):
    CC_BY = "620ba3983e2fa95c500b4297"
    CC_BY_SA = "620ba39b3e2fa95c500b4298"
    CC_BY_NC = "620ba39e3e2fa95c500b4299"
    CC_BY_NC_SA = "620ba3a03e2fa95c500b429a"
    MIT = "620ba3a83e2fa95c500b429d"
    CC_BY_ND = "620ba3a33e2fa95c500b429b"
    CC_BY_NC_ND = "620ba3a63e2fa95c500b429c"
    GPL = "620ba3ab3e2fa95c500b429e"
    APACHE_LICENSE_VERSION_2_0 = "620ba3ae3e2fa95c500b429f"
    BSD_3_CLAUSE = "620ba3b13e2fa95c500b42a0"
    UNKNOWN = "620ba3b73e2fa95c500b42a2"
    PUBLIC_DOMAIN_CC0 = "620ba3943e2fa95c500b4296"
    CUSTOM = "620ba3b43e2fa95c500b42a1"
