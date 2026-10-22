# RR NEWS Telugu — AI backend starter

ఈ ఫోల్డర్ AI సేవలను అనుసంధానించడానికి ప్రారంభ టెంప్లేట్ మాత్రమే. ఇది ఒంటరిగా నిజమైన MP4 తయారు చేయదు.

## సిఫారసు చేసిన pipeline
1. Sarvam AI Bulbul ద్వారా Telugu `te-IN` audio తయారు చేయడం.
2. తయారైన audio ను మీ private object storageలో తాత్కాలికంగా ఉంచి HTTPS audio URL పొందడం.
3. D-ID video APIకి మీ అనుమతితో రూపొందించిన/ఉపయోగించడానికి హక్కు ఉన్న anchor image + audio URL పంపడం.
4. D-ID video status complete అయిన తర్వాత MP4 URLను appకి ఇవ్వడం.

## అవసరమైనవి
- Sarvam API key: https://docs.sarvam.ai/api/api-guides-tutorials/text-to-speech/rest-api
- D-ID API key/account: https://docs.d-id.com/docs/quickstart
- audio files కోసం private storage/HTTPS URL provider
- Python 3.11+

API keysను APK, index.html, GitHub source, లేదా ఈ చాట్‌లో పెట్టకండి. Host/server secretsలో మాత్రమే ఉంచండి.

## Run locally
`pip install -r requirements.txt`
`.env.example` ను `.env` గా కాపీ చేసి values ని మీ server environmentలో పెట్టండి.
`uvicorn main:app --host 0.0.0.0 --port 8000`

ఈ starterలో provider calls పూర్తి చేయడానికి audio hosting మరియు D-ID request details మీ account/documentationకు అనుగుణంగా సెటప్ చేయాలి. Live provider integrationగా భావించకండి.
