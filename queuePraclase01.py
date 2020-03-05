








'''
    1,创建打印机任务的队列，每个任务都有个时间戳，队列启动的时候为空
    2，是否创建新的任务？如果是，创建时间戳添加到队列 090101
    3，打印机不忙并且有任务在等待
        从打印机队列删除一个任务并将其分配给  打印机  090301
        当前时间减去创建任务的时间戳，计算任务的等待时间  2
        将该任务的等待时间附件到列表中稍后处理
        根据打印任务的页数，确定需要多少时间
    4，打印机需要1s打印，所以得从2分钟内-1s = 等待时间
    5，任务完成，所需要的时间是0，打印机空闲
    6，模拟完成后从生成的等待时间列表中计算平均等待时间


    printer  打印机印象   两种状态，默认空闲
    printerqueue  打印队列对象   用来创建任务
    Task   任务对象

'''
class Printer:

    #初始化参数：设置打印机的速率（每分钟5页还是10页）
    def __init__(self,)
        self.pagerate = pom
        self.currentTask = None #空闲状态
        self.timeRemaining = 0

    def busy(self):
        if self.currentTask != None:
            return True
        else:
            return False

            


