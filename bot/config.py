#    This file is part of the Compressor distribution.
#    Copyright (c) 2021 Danish_00
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, version 3.
#
#    This program is distributed in the hope that it will be useful, but
#    WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
#    General Public License for more details.
#
# License can be found in <
# https://github.com/1Danish-00/CompressorQueue/blob/main/License> .

from decouple import config

try:
    APP_ID = config("APP_ID", "14874438")
    API_HASH = config("API_HASH", "9d75f325568b6297204ef261040595f7")
    BOT_TOKEN = config("BOT_TOKEN", "5387861278:AAF3CtbOu298iG522AY615UqtvxrDMT_XsU")
    DEV = 1322549723
    OWNER = config("OWNER", "5178332815")
    FFMPEG = config("FFMPEG","ffmpeg -i '''{}''' -preset faster -c:v libx265 -vf 'drawtext=fontfile=Aclonica.ttf:fontsize=27:fontcolor=white:bordercolor=black@0.50:x=w-tw-10:y=10:box=1:boxcolor=black@0.5:boxborderw=6:text=Omnimo3' -s 854x480 -crf 28 -map 0:v -c:a aac  -b:a 35k -map 0:a -c:s copy -map 0:s? '''{}''' -y")
    THUMB = config("THUMBNAIL", "https://telegra.ph/file/75ee20ec8d8c8bba84f0)
except Exception as e:
    LOGS.info("Environment vars Missing")
    LOGS.info("something went wrong")
    LOGS.info(str(e))
    exit(1)
