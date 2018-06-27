from aip import AipOcr, AipSpeech, AipImageClassify
import config

ocr_client = AipOcr(config.appid, config.apikey, config.secretkey)
speech_client = AipSpeech(config.appid, config.apikey, config.secretkey)
image_classify_client = AipImageClassify(config.appid, config.apikey, config.secretkey)
