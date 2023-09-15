API_ID = 14874438
API_HASH = '9d75f325568b6297204ef261040595f7'
THUMBNAIL = 'https://telegra.ph/file/9ac3e9ba4cd523f37a6b1.jpg'

FFMPEG = 'ffmpeg -i '''{}''' -preset faster -c:v libx265 -vf 'drawtext=fontfile=Aclonica.ttf:fontsize=27:fontcolor=white:bordercolor=black@0.50:x=w-tw-10:y=10:box=1:boxcolor=black@0.5:boxborderw=6:text=Omnimo3' -s 854x480 -crf 28 -map 0:v -c:a aac  -b:a 35k -map 0:a -c:s copy -map 0:s? '''{}''' -y'
BOT_TOKEN = '5387861278:AAF3CtbOu298iG522AY615UqtvxrDMT_XsU' 
OWNER = 5178332815
