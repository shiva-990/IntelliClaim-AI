from cv.services.detection_service import DetectionService

service = DetectionService()

predictions = service.detect_claim("CLM000001")

print("=" * 60)

print(f"Images Processed : {len(predictions)}")

print("=" * 60)

for prediction in predictions:

    print(prediction.image_name)

    print(len(prediction.detections))

    print("-" * 40)