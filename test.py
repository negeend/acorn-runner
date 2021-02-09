# import sys
# import os
# from os import listdir
# from os.path import isfile, join
# request = "GET /cgibin/posts.py HTTP/1.1\nHost: localhost:8070\nUser-Agent: curl/7.64.1\nAccept: */*"
# CGIVariables = {"Accept": "HTTP_ACCEPT", "Host": "HTTP_HOST", "User-Agent": "HTTP_USER_AGENT", "Accept-Encoding": "HTTP_ACCEPT_ENCODING"}
# parts = request.split("\n")

# parts[0] = parts[0].split(" ")
# headers = {}
# i = 1
# while i < len(parts):
#     parts[i] = parts[i].split(": ")
#     headers[parts[i][0]] = parts[i][1]
#     i += 1

# for var in CGIVariables:
#     if var in headers:
#         os.environ[CGIVariables.get(var)] = headers.get(var)



# print(parts)
# print(headers)
# # print(os.environ)




# def getFilePaths(dirname):
#     listOfFile = os.listdir(dirname)
#     completeFileList = list()
#     for file in listOfFile:
#         completePath = os.path.join(dirname, file)
#         if os.path.isdir(completePath):
#             completeFileList = completeFileList + getFilePaths(completePath)
#         else:
#             completeFileList.append(completePath)
#     return completeFileList

# def getFileNames(filePaths):
#     fileNames = []
#     for filePath in filePaths:
#         filePath = filePath.split("/")
#         fileNames.append(filePath[len(filePath) - 1])
#     return fileNames

# def getContents(filename):
# 	reply = "".encode()
# 	f = open(filename, "rb")
# 	for line in f:
# 		reply += line
# 	return reply

# def parseConfigFile(filename):
#     properties = {}
#     file = open(filename)
#     lines = file.readlines()
#     file.close()
#     i = 0
#     while i < len(lines):
#         lines[i] = lines[i].strip("\n")
#         lines[i] = lines[i].split("=")
#         i += 1
#     for line in lines:
#         properties[line[0]] = line[1]
#     return properties


# filename = "config.cfg"
# try:
#     file = open(filename)
#     lines = file.readlines()
#     file.close()
# except FileNotFoundError:
#     print("Unable To Load Configuration File")
#     sys.exit()

# if len(lines) != 4:
#     print("Missing Field From Configuration File")
#     sys.exit()

# i = 0
# while i < len(lines):
#     lines[i] = lines[i].strip("\n")
#     lines[i] = lines[i].split("=")
#     i += 1

# properties = []
# for line in lines:
#     properties.append(line[0])

# if (not 'staticfiles' in properties) or (not 'cgibin' in properties) or (not 'port' in properties) or (not 'exec' in properties):
#     print("Missing Field From Configuration File.")
#     sys.exit()

# # print(lines)
# # print(properties)




# filePaths = getFilePaths("./files")
# # print(filePaths)
# fileNames = getFileNames(filePaths)
# # print(getFileNames(filePaths))

# # print(parts[0][1])

# # if "?" in parts[0][1]:
# #     print("HI")
# # if parts[0][1] == "/":
# #     filename = "index.html"
# #     filepath = "./files/" + filename
# # else:
# #     filename = parts[0][1].replace("/", "")

# # response = parts[0][2]
# # file1 = filename.split("?")
# # if len(file1) > 1:
# #     file2 = file1[0]
# #     queries = file1[1]
# # else:
# #     file2 = filename.split(".")

# # suffix = file2[1]

# # print(file1)
# # print(file2)

# if "?" in parts[0][1]:
#     querieString = parts[0][1].split("?")
#     filepath = querieString[0]
#     filename = filepath.split("/")[len(filepath.split("/"))- 1]
#     queries = querieString[1]
# else:
#     if parts[0][1] == "/":
#         filename = "index.html"
#         filepath = staticfiles + "/" + filename
#     elif parts[0][1].split("/")[1] == "cgibin":
#         filename = parts[0][1].split("/")[2]
#     else:
#         filename = parts[0][1].replace("/", "")

# print(filename)
# print(queries)


# def getContentType(suffix):
#     if suffix == "txt":
#         return "text/plain"
#     if suffix == "html":
#         return "text/html"
#     if suffix == "js":
#         return "application/javascript"
#     if suffix == "css":
#         return "text/css"
#     if suffix == "png":
#         return "image/png"
#     if suffix == "jpg" or suffix == "jpeg":
#         return "image/jpeg"
#     if suffix == "xml":
#         return "text/xml"
# response = ""
# if filename in fileNames:
#     index = fileNames.index(filename)
#     response += "200 OK\n"
#     response += "Content-Type: {}\n\n".format(getContentType(suffix))
#     content = getContents(filePaths[index])
# else:
#     response += "404 File Not Found\n"
#     response += "Content-Type: {}\n\n".format(getContentType(suffix))
#     content = '<html>\n<head>\n\t<title>404 Not Found</title>\n</head>\n<body bgcolor="white">\n<center>\n\t<h1>404 Not Found</h1>\n</center>\n</body>\n</html>\n'

# # print(response)
# # print(content)






# def getContents(filename):
# 	reply = "".encode()
# 	f = open(filename, "rb")
# 	for line in f:
# 		reply += line
# 	f.close()
# 	return reply

# print(getContents('image.jpg'))

ls = []
ls.append("hi")
print(ls)