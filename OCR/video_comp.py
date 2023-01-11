from videohash import VideoHash
path1 =""
path2 =""
videohash1 = VideoHash(path=path1)
videohash2 = VideoHash(path=path2)
diff = videohash1 - videohash2
if(diff< 0.25):
    print("similar content detected")