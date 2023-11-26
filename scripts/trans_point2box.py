# Column 1 		        frame number
# Column 2		        time (txt: 30 Hz, mp4: 15 Hz)
# Column 3-3+n		    x coordinates
# Column 3+n+1-3+2*n 	y coordinates

def trans_point_box(txt_path, output_dir):
    width = 2456
    height = 2058
    box_length = 100

    with open(txt_path, 'r') as file:
        content = file.read()
        content = content.split('\n')
        for i, data in enumerate(content):
            data = data.split('\t')
            print(data)
            item_width = float(box_length / width)
            item_height = float(box_length / height)
            num = int(data[0]) - 1
            with open(f"{output_dir}/frame_{int(num):04d}.txt", 'w') as f:
                f.write("0" + ' ' + str(float(data[2]) / width) + ' ' + str(float(data[12]) / height) + ' ' + str(item_width) + ' ' + str(item_height) + '\n')
                f.write("0" + ' ' + str(float(data[3]) / width) + ' ' + str(float(data[13]) / height) + ' ' + str(item_width) + ' ' + str(item_height) + '\n')
                f.write("0" + ' ' + str(float(data[4]) / width) + ' ' + str(float(data[14]) / height) + ' ' + str(item_width) + ' ' + str(item_height) + '\n')
                f.write("0" + ' ' + str(float(data[5]) / width) + ' ' + str(float(data[15]) / height) + ' ' + str(item_width) + ' ' + str(item_height) + '\n')
                f.write("0" + ' ' + str(float(data[6]) / width) + ' ' + str(float(data[16]) / height) + ' ' + str(item_width) + ' ' + str(item_height) + '\n')
                f.write("0" + ' ' + str(float(data[7]) / width) + ' ' + str(float(data[17]) / height) + ' ' + str(item_width) + ' ' + str(item_height) + '\n')
                f.write("0" + ' ' + str(float(data[8]) / width) + ' ' + str(float(data[18]) / height) + ' ' + str(item_width) + ' ' + str(item_height) + '\n')
                f.write("0" + ' ' + str(float(data[9]) / width) + ' ' + str(float(data[19]) / height) + ' ' + str(item_width) + ' ' + str(item_height) + '\n')
                f.write("0" + ' ' + str(float(data[10]) / width) + ' ' + str(float(data[20]) / height) + ' ' + str(item_width) + ' ' + str(item_height) + '\n')
                f.write("0" + ' ' + str(float(data[11]) / width) + ' ' + str(float(data[21]) / height) + ' ' + str(item_width) + ' ' + str(item_height) + '\n')


if __name__ == '__main__':
    txt_path = "raw/txt/path/10-fish-part1-2016.txt"
    # txt_path = "raw/txt/path/10-fish-part2-2016.txt"
    output_dir = "output/dir/path"
    trans_point_box(txt_path, output_dir)
