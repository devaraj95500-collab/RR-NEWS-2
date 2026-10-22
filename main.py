"""RR NEWS Telugu backend starter. Provider integration is intentionally guarded until configured."""
import os
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

app = FastAPI(title="RR NEWS Telugu AI Video Backend", version="0.1.0")

class VideoRequest(BaseModel):
    brand: str = "RR NEWS Telugu"
    headline: str = Field(default="", max_length=300)
    place: str = Field(default="", max_length=150)
    category: str = Field(default="స్థానిక వార్తలు", max_length=100)
    script: str = Field(default="", max_length=12000)
    ticker: str = Field(default="మరిన్ని స్థానిక వార్తల కోసం చూస్తూనే ఉండండి... RR NEWS", max_length=300)
    anchor_style: str = Field(default="saree", pattern="^(saree|modern)$")
    duration: str = Field(default="30-60", pattern="^(30-60|60-180)$")
    quality: str = Field(default="high", pattern="^(high|standard)$")
    voice: str = Field(default="female", pattern="^(female|male)$")
    output_format: str = "mp4"

@app.get("/health")
def health():
    return {"ok": True, "service": "RR NEWS Telugu AI backend", "provider_integration": "not_configured"}

@app.post("/api/video/generate")
def generate_video(req: VideoRequest):
    if not (req.headline.strip() or req.script.strip()):
        raise HTTPException(status_code=400, detail="headline or script is required")
    missing = []
    for name in ("SARVAM_API_KEY", "DID_API_KEY"):
        if not os.getenv(name):
            missing.append(name)
    image_var = "RRNEWS_ANCHOR_SAREE_IMAGE_URL" if req.anchor_style == "saree" else "RRNEWS_ANCHOR_MODERN_IMAGE_URL"
    if not os.getenv(image_var):
        missing.append(image_var)
    if missing:
        raise HTTPException(status_code=503, detail={
            "message": "AI వీడియో సేవలు ఇంకా కాన్ఫిగర్ కాలేదు. Server secrets, audio hosting, మరియు provider pipeline సెటప్ చేయాలి.",
            "missing_server_settings": missing,
            "next_step": "See ai-backend-starter/README_TELUGU.md. Never put API keys in the Android app."
        })
    # Deliberate safety stop: TTS audio upload + provider-specific D-ID request/status polling
    # must be implemented and tested for the user's selected account before enabling real generation.
    raise HTTPException(status_code=501, detail={
        "message": "Credentials detected, కానీ live TTS → secure audio hosting → avatar MP4 pipeline ఇంకా అమలు/పరీక్ష కాలేదు.",
        "next_step": "Complete and test the provider adapters before enabling generation. No fake video link was returned."
    })
