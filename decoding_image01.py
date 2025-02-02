# from pyzbar.pyzbar import decode
# import cv2
# import numpy as np
# import zxing

# def decode_pdf417(image_path):
#     # Read the image in RGB format (some libraries expect RGB)
#     image = cv2.imread(image_path)
#     image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)  # Convert to RGB
#     gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#     # Minimal preprocessing (adjust parameters as needed)
#     # 1. Resize to enhance small codes
#     resized = cv2.resize(gray, None, fx=1.5, fy=1.5, interpolation=cv2.INTER_CUBIC)
    
#     # 2. Gentle contrast enhancement
#     clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
#     contrast_enhanced = clahe.apply(resized)
    
#     # 3. Binarize using adaptive thresholding
#     thresh = cv2.adaptiveThreshold(
#         contrast_enhanced, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2
#     )

#     # Detect PDF417 with pyzbar
#     barcodes = decode((thresh).astype('uint8'))  # Ensure uint8 dtype

#     # Check for PDF417
#     pdf417_found = False
#     for barcode in barcodes:
#         if barcode.type == 'PDF417':
#             data = barcode.data.decode("utf-8")
#             print(f"[pyzbar] PDF417 Data: {data}")
#             pdf417_found = True
#             # Draw bounding box (adjust coordinates for resizing)
#             points = [(int(p.x / 1.5), int(p.y / 1.5)) for p in barcode.polygon]
#             pts = np.array(points, dtype=np.int32)
#             cv2.polylines(image, [pts], True, (0, 255, 0), 2)
#             x, y = pts[0][0], pts[0][1]
#             cv2.putText(image, data, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

#     # Fallback to ZXing if pyzbar fails
#     if not pdf417_found:
#         print("[pyzbar] No PDF417 detected. Trying ZXing...")
#         reader = zxing.BarCodeReader()
#         result = reader.decode(image_path)
#         if result and result.format == 'PDF_417':
#             print(f"[ZXing] PDF417 Data: {result.parsed}")
#             # Draw bounding box
#             if result.points:
#                 points = [(int(p.x), int(p.y)) for p in result.points]
#                 cv2.polylines(image, [np.array(points, dtype=np.int32)], True, (0, 255, 0), 2)
#                 x, y = points[0][0], points[0][1]
#                 cv2.putText(image, result.parsed, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
#         else:
#             print("[ZXing] No PDF417 detected.")

#     # Display the result
#     cv2.imshow("Result", image)
#     cv2.waitKey(0)
#     cv2.destroyAllWindows()

# # Run the decoder
# decode_pdf417("image01.png")


from aspose.barcode import barcoderecognition

reader = barcoderecognition.BarCodeReader("image01.png", barcoderecognition.DecodeType.AllSupportedTypes)
recognized_results = reader.read_bar_codes()
for barcode in recognized_results:
    print(barcode.code_text)