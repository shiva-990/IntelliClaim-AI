from services.yolo_service import YOLOService

# Change this to an image that exists in your project
image_path = "uploads/claims/car_test.jpg"

results = YOLOService.predict(image_path)

parsed = YOLOService.parse_results(results)

print("\n===== YOLO Detection Results =====")
print(parsed)