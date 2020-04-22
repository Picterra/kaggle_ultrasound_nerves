import logging
import sys
from picterra import APIClient

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)

raster = 'f9abc42b-73d4-429c-9e44-f095a1949df4'
detector = '21cd315d-5795-4559-afa0-5a4e9498f064'

pic = APIClient()
result_id = pic.run_detector(detector, raster)
pic.download_result_to_file(result_id, 'result.geojson')