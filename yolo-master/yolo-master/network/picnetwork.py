import oss2

def uploadResult(file_name,file_path):
    auth = oss2.Auth("LTAIVfJ0YwF4jusW","CSxD6ldDZ3jOFlVkJjkF6jISbthSbz")
    endpoint = "oss-cn-beijing.aliyuncs.com"
    bucket = oss2.Bucket(auth,endpoint,"vehicledetection")
    bucket.put_object_from_file(file_name[0],file_path[0])
    bucket.put_object_from_file(file_name[1],file_path[1])
    print("successful!")

def uploadVedio(file_name,file_path):
    auth = oss2.Auth("LTAIVfJ0YwF4jusW","CSxD6ldDZ3jOFlVkJjkF6jISbthSbz")
    endpoint = "oss-cn-beijing.aliyuncs.com"
    bucket = oss2.Bucket(auth,endpoint,"vehicledetection")
    bucket.put_object_from_file(file_name,file_path)
    print("successful!")