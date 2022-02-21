import glob
import text_analysis.pattern_matching.matching as pattern_matching
import visual_analysis.histogram_analysis.histogram_analysis as histogram_analysis
import spatial_analysis.proximity_analysis.proximity_analysis as proximity_analysis
import utils.utils as utils

# get input image files
img_files = [file for file in glob.glob("UIED/data/input/" + "*.*")]
img_files.sort()
# print(len(img_files))

# get OCR files
ocr_files = [file for file in glob.glob("UIED/data/output/ocr/" + "*.json")]
ocr_files.sort()
# print(len(ocr_files))

# iterate over the OCR files
for i in range(len(ocr_files)):
    print('###################### processing: ', ocr_files[i], '######################')

    print("------------text_analysis_output-----------")
    analysis_result = pattern_matching.match_patterns(ocr_files[i])

    print("------------visual_analysis_output-----------")
    image_file = img_files[i]
    analysis_result = histogram_analysis.analyze_histogram(analysis_result, image_file)

    print("------------proximity_analysis_output-----------")
    analysis_result = proximity_analysis.analyze_proximity(analysis_result, image_file)
    utils.print_dictionary(analysis_result)

    print("------------size_analysis_output-----------")
