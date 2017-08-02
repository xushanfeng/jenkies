# # -*- coding:utf-8
# # import threadpool
# from threading import Thread
# import commands
# import sys
# import time
#
#
# def command(typ):
#     # typ 浏览器类型
#     # 根据不同的浏览器类型执行不同的命令
#     tmp = "pytest --browser=" + typ + " --html=./" + typ + ".html"
#     commands.getstatusoutput(tmp)
#
# if __name__ == "__main__":
#     print "执行开始"
#     types = sys.argv[1:]
#     # pool = threadpool.ThreadPool(len(types))
#     # # 根据参数数组长度产生不同的线程池
#     # requests = threadpool.makeRequests(command, types)
#     # [pool.putRequest(req) for req in requests]
#     # # 执行不同的线程
#     # pool.wait()
#     th = []
#     for i in types:
#         print i
#         tmp = Thread(target=command, args=(i,))
#         th.append(tmp)
#
#     for j in th:
#         j.setDaemon(True)
#         j.start()
#         print j.name
#     # 等待线程执行结束
#     j.join()
#     print "执行结束"
