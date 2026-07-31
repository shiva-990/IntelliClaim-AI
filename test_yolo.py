from services.yolo_service import YOLOService

image_path = "data/raw/car3_test.jpg"

results = YOLOService.predict(image_path)

parsed = YOLOService.parse_results(results)

print(parsed)