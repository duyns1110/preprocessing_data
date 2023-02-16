from glob import glob
import xml.etree.ElementTree as ET
import os
from PIL import Image
path = r"/home/lenovo/Desktop/labelImg/NH_Agribank"
save_path = r"/home/lenovo/Desktop/labelImg/NH_Agribank_res"
filenames = []

#merge xml
all_xml_ps = glob(os.path.join(path, '*xml'))
for xml_p in all_xml_ps:
    if filenames != []:
        filenames.remove(filenames[-1])
        continue
    file_name = xml_p.split('/')[-1].split('.')[0].split('_')
    print(file_name)
    name_file = file_name[0] + '_' + file_name[1] + '_'
    print(name_file)
    for check in all_xml_ps:
        if name_file in check:
            filenames.append(check)
        else:
            continue
    print(filenames)
    # parse the XML file
    tree1 = ET.parse(filenames[0])
    root1 = tree1.getroot()
    root1[1].text = name_file
    root1[2].text = save_path + "/" + name_file + '.xml'

    # find the first element named "object"
    for i, element in enumerate(root1):
        if element.tag == "object":
            first_object = i
            break

    # remove all elements behind the first "object" element
    for element in root1[first_object + 1:]:
        root1.remove(element)

    # write the above elements to a new XML file

    for filename_idx in range(1, len(filenames)):
        filename = filenames[filename_idx]
        tree = ET.parse(filename)
        root = tree.getroot()

        # find the first 'object' element in the second file
        object_elem = None
        for elem in root:
            if elem.tag == 'object':
                object_elem = elem
                break

        # append the first 'object' element from the second file to the modified tree from the first file
        root1.append(object_elem)

    print(name_file)

    # write the combined XML tree to a new file
    ET.ElementTree(root1).write(save_path + "/" + name_file + '.xml')

#merge images
img_name = None
all_xml_ps = glob(os.path.join(path, '*jpg'))
for jpg_p in all_xml_ps:
    if img_name == jpg_p:
        continue
    else:
        img_name = jpg_p
        img = Image.open(jpg_p)
        img_name = img_name.split("/")[-1].split(".")[0].split("_")
        img = img.save(save_path + "/" + img_name[0] + "_" + img_name[1] + "." + "jpg")