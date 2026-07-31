from services.damage_analysis import DamageAnalysisService

detections = [
    {
        "part": "scratch",
        "confidence": 0.91
    },
    {
        "part": "smash",
        "confidence": 0.71
    }
]

result = DamageAnalysisService.analyze(detections)

print(result)