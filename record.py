import cv2
import os
import argparse

parser = argparse.ArgumentParser(description='Simple video capture script.')
parser.add_argument('--save', nargs = '?', help='Directory path to save image. If not save mode, it is ignored.')
parser.add_argument('--setting', action='store_true', help='Open camera setting pannel. Other flags are all ignored.')
parser.add_argument('--mode', choices=['a', 'm'], default='m', help='capture mode. "a" for automatic capturing, "m" for manual capturing')
parser.add_argument('--period', type = int, default=1, help='capture frame period')

args = parser.parse_args()
#print(parser)

cap = cv2.VideoCapture(0)
if args.setting:
    cap.set(cv2.CAP_PROP_SETTINGS, 0.0)

def get_file_name(args, id):
    return "{}/{}.png".format(args.save, id)

if args.save and not os.path.exists(args.save):
    os.makedirs(args.save)

if args.mode == 'a':
    is_auto = True
else:
    is_auto = False

frame_id = 0
while True:
    ret, frame = cap.read()
    cv2.imshow('frame', frame)

    img_file_name = get_file_name(args, frame_id)

    input_key = cv2.waitKey(1) & 0xFF
    if input_key == ord('q'):
        break

    if args.setting or args.save is None:
        continue

    if is_auto or (input_key == ord(' ')):
        if frame_id % args.period == 0:
            cv2.imwrite(img_file_name, frame)

    frame_id += 1
