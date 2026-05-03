h=open('myfile.txt','r')
i=0
while True:
    line=h.readline()

    if not line: #this is for when the line are over otherwise it will keep running
        break
    i+=1
    m1=line.split(",")[0]
    m2=line.split(",")[1]
    m3=line.split(",")[2]
    print(f"The marks of the student {i} is {m1}")
    print(f"The marks of the student {i} is {m2}")
    print(f"The marks of the student {i} is {m3}")

# press and hold alt button and select multiple cursors

# Focus on these 4 things only:
#
# 1. Opening files (proper way)
# with open("file.txt", "r") as f:
#     data = f.read()
#
# 👉 with is important (auto closes file)
# 👉 This is the standard pattern everywhere
#
# 2. Reading methods (only 3 matter)
# f.read()        # whole file as string
# f.readline()    # one line at a time
# f.readlines()   # list of all lines
#
# You don’t need anything beyond this right now.
#
# 3. Writing to file
# with open("file.txt", "w") as f:
#     f.write("Hello")
#
# Modes:
#
# "w" → overwrite
# "a" → append
# "r" → read
# 4. Looping through file (VERY important)
#
# Instead of your current approach:
#
# while True:
#     line = f.readline()
#
# 👉 Use this:
#
# with open("file.txt") as f:
#     for line in f:
#         print(line)
#
# This is:
#
# cleaner
# safer
# more Pythonic
# what real code uses
# 🧠 About your concern:
#
# “I understood logic but can’t write it myself”
#
# That’s normal. You're in Stage 2 learning:
#
# See code → understand
# Modify code → semi-comfortable
# Write from scratch → struggle ❗ (you are here)
# Write naturally → mastery
#
# You’re exactly where you should be.
#
# 🚫 What you should NOT do now
# Don’t try to memorize all file methods
# Don’t dive into advanced stuff (binary files, buffering, etc.)
# ✅ What you SHOULD do instead
#
# Practice small patterns repeatedly
#
# Example:
#
# with open("file.txt") as f:
#     for line in f:
#         nums = line.strip().split(",")
#         print(nums)


# with open("myfile.txt") as f:
#     m1=f.split(',')[0]
#     m2=f.split(',')[1]
#     m3=f.split(',')[2]
#     print(m1,m2,m3)
#     print((m1+m2+m3)/3)



# SEEK,TELL AND TRUNCATE