from aip import AipOcr, AipSpeech
import config

ocr_client = AipOcr(config.appid, config.apikey, config.secretkey)
speech_client = AipSpeech(config.appid, config.apikey, config.secretkey)
