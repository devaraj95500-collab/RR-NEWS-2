RR NEWS Telugu — Android APK Build Project

ఈ ZIP Android source project మాత్రమే; ఇప్పటికే తయారైన APK కాదు.
ప్రస్తుత యాప్‌లో RR NEWS స్క్రిప్ట్ ఎడిటర్, బులెటిన్ ప్రివ్యూ, మొబైల్ TTS,
TXT/PNG export మరియు AI Video Studio request UI ఉన్నాయి.

AI VIDEO STATUS:
- AI మహిళా యాంకర్, హై-క్వాలిటీ తెలుగు AI వాయిస్, lip-sync, MP4 తయారీకి
  నిజమైన backend మరియు provider credentials ఇంకా అవసరం.
- AI Video Studioలో HTTPS backend URL కాన్ఫిగర్ చేసినప్పుడే అభ్యర్థన పంపుతుంది.
- API secret keysని APKలో లేదా public GitHub repositoryలో పెట్టకండి.
- YouTube upload OAuth/API అనుసంధానం ఇంకా అమలు కాలేదు.
- పూర్తి వివరాలకు AI_VIDEO_INTEGRATION_TELUGU.txt చూడండి.

మొబైల్ ద్వారా APK బిల్డ్ (GitHub Actions):
1. ZIPను extract చేయండి.
2. ప్రాజెక్ట్‌లోని అన్ని ఫైళ్లు/ఫోల్డర్లను కొత్త GitHub repositoryకి upload చేయండి.
   .github/workflows/build-apk.yml ఫైల్ తప్పనిసరిగా ఉండాలి.
3. GitHubలో Actions తెరిచి “Build RR NEWS Telugu APK” workflowను run చేయండి
   (లేదా main branchకి push చేయండి).
4. Build విజయవంతమైతే RR-NEWS-Telugu-debug-apk artifactను download చేయండి.
5. ZIP artifactను extract చేసి app-debug.apkను Androidలో install చేయండి.

ఇది testing/debug APK. Public release కోసం signing, privacy/security review,
AI backend setup మరియు పూర్తి పరీక్షలు అవసరం.
