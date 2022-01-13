import ltapy.session
import ltapy.utils
import time
import numpy as np

def lens_shift():
    ses = ltapy.session.Session(pid=1336)
    lt = ses.lt
    lt.Message("Successfully connected to LightTools!")
    # 初始化
    data_array_x = [0]*10
    data_array_y = [0]*10
    modlue = "LENS_MANAGER[1].COMPONENTS[Components].GROUP[group_3]"
    lens = "LENS_MANAGER[1].COMPONENTS[Components].GROUP[group_3].GROUP[Lens]"
    img = "LENS_MANAGER[1].COMPONENTS[Components].GROUP[group_3].SOLID[Image]"
    for r in range(50):
        lt.DbSet(modlue, "Alpha", 0)
        lt.DbSet(modlue, "Beta", 0)
        lt.DbSet(modlue, "Gamma", 0)
        lt.DbSet(lens, "Alpha", 0)
        lt.DbSet(lens, "Beta", 0)
        lt.DbSet(lens, "Gamma", 0)
        lt.DbSet(img, "X", 0)
        lt.DbSet(img, "Y", 0)
        # 給予模組隨機旋轉角度(0~1)
        random_x = np.random.uniform(-0.5,0.5)
        random_y = np.random.uniform(-0.5,0.5)
        lt.DbSet(modlue, "Alpha", random_x)
        lt.DbSet(modlue, "Beta", random_y)
        # 將光線對準Sensor中心
        img_X = lt.DbGet(img, "X")
        img_Y = lt.DbGet(img, "Y")
        # print(f'{img_X},{img_Y}')
        key_x = "LENS_MANAGER[1].OPT_MANAGER[Optimization_Manager].OPT_MERITFUNCTIONS[Merit_Function].OPT_NSRAYMERITFUNCTION[Center_X].OPT_NSRAYMFITEM[FanItem]"
        key_y = "LENS_MANAGER[1].OPT_MANAGER[Optimization_Manager].OPT_MERITFUNCTIONS[Merit_Function].OPT_NSRAYMERITFUNCTION[Center_Y].OPT_NSRAYMFITEM[FanItem]"
        lt.SetOption('DbUpdate', 0)
        lt.DbSet(key_x, "TargetAt", img_X, 1, 1)
        lt.DbSet(key_x, "TargetAt", img_X, 2, 1)
        lt.DbSet(key_x, "TargetAt", img_X, 3, 1)
        lt.DbSet(key_y, "TargetAt", img_Y, 1, 1)
        lt.DbSet(key_y, "TargetAt", img_Y, 2, 1)
        lt.DbSet(key_y, "TargetAt", img_Y, 3, 1)
        lt.SetOption('DbUpdate', 1)

        lt.Cmd("Optimize")
        # Lens移動量
        lt.DbGet(lens, "X")
        lt.DbGet(lens, "Y")
        # 各光線位置
        for i in range(1, 10):
            Ray = f'LENS_MANAGER[1].NS_RAYS[Rays].NS_FAN[R{i}].NS_RAY[R{i}.r2].NS_SEGMENT[segment_13]'
            get_value_x = lt.DbGet(Ray, "Global_X")
            get_value_y = lt.DbGet(Ray, "Global_Y")
            data_array_x[i] = get_value_x
            data_array_y[i] = get_value_y
        print(f'{data_array_x[1]-data_array_x[5]},{data_array_y[1]-data_array_y[5]},'
              f'{data_array_x[2]-data_array_x[5]},{data_array_y[2]-data_array_y[5]},'
              f'{data_array_x[3]-data_array_x[5]},{data_array_y[3]-data_array_y[5]},'
              f'{data_array_x[4]-data_array_x[5]},{data_array_y[4]-data_array_y[5]},'
              f'{data_array_x[5]-data_array_x[5]},{data_array_y[5]-data_array_y[5]},'
              f'{data_array_x[6]-data_array_x[5]},{data_array_y[6]-data_array_y[5]},'
              f'{data_array_x[7]-data_array_x[5]},{data_array_y[7]-data_array_y[5]},'
              f'{data_array_x[8]-data_array_x[5]},{data_array_y[8]-data_array_y[5]},'
              f'{data_array_x[9]-data_array_x[5]},{data_array_y[9]-data_array_y[5]}')

def sensor_shift():
    ses = ltapy.session.Session(pid=11556)
    lt = ses.lt
    lt.Message("Successfully connected to LightTools!")
    # 初始化
    data_array_x = [0] * 10
    data_array_y = [0] * 10
    modlue = "LENS_MANAGER[1].COMPONENTS[Components].GROUP[group_3]"
    lens = "LENS_MANAGER[1].COMPONENTS[Components].GROUP[group_3].GROUP[Lens]"
    img= "LENS_MANAGER[1].COMPONENTS[Components].GROUP[group_3].SOLID[Image]"
    for r in range(10):
        lt.DbSet(modlue, "Alpha", 0)
        lt.DbSet(modlue, "Beta", 0)
        lt.DbSet(modlue, "Gamma", 0)
        lt.DbSet(lens, "Alpha", 0)
        lt.DbSet(lens, "Beta", 0)
        lt.DbSet(lens, "Gamma", 0)
        lt.DbSet(img, "X", 0)
        lt.DbSet(img, "Y", 0)
        # 給予模組隨機旋轉角度(0~1)
        random_x = np.random.uniform(-0.5, 0.5)
        random_y = np.random.uniform(-0.5, 0.5)
        modlue_Alpha = lt.DbSet(modlue, "Alpha", random_x)
        modlue_Beta = lt.DbSet(modlue, "Beta", random_y)
        # 將光線對準Sensor中心
        ray_X = lt.DbGet("LENS_MANAGER[1].NS_RAYS[Rays].NS_FAN[R5].NS_RAY[R5.r2].NS_SEGMENT[segment_13]", "Global_X")
        ray_Y = lt.DbGet("LENS_MANAGER[1].NS_RAYS[Rays].NS_FAN[R5].NS_RAY[R5.r2].NS_SEGMENT[segment_13]", "Global_Y")
        # print(f'{img_X},{img_Y}')
        key_x = "LENS_MANAGER[1].OPT_MANAGER[Optimization_Manager].OPT_MERITFUNCTIONS[Merit_Function].OPT_NSRAYMERITFUNCTION[Ray_X].OPT_NSRAYMFITEM[FanItem]"
        key_y = "LENS_MANAGER[1].OPT_MANAGER[Optimization_Manager].OPT_MERITFUNCTIONS[Merit_Function].OPT_NSRAYMERITFUNCTION[Ray_Y].OPT_NSRAYMFITEM[FanItem]"
        lt.SetOption('DbUpdate', 0)
        lt.DbSet(key_x, "TargetAt", ray_X, 1, 1)
        lt.DbSet(key_x, "TargetAt", ray_X, 2, 1)
        lt.DbSet(key_x, "TargetAt", ray_X, 3, 1)
        lt.DbSet(key_y, "TargetAt", ray_Y, 1, 1)
        lt.DbSet(key_y, "TargetAt", ray_Y, 2, 1)
        lt.DbSet(key_y, "TargetAt", ray_Y, 3, 1)
        lt.SetOption('DbUpdate', 1)

        lt.Cmd("Optimize")
        # Lens旋轉量
        lens_Alpha = lt.DbGet(lens, "Alpha")
        lens_Beta = lt.DbGet(lens, "Beta")
        # 各光線位置
        for i in range(1, 10):
            Ray = f'LENS_MANAGER[1].NS_RAYS[Rays].NS_FAN[R{i}].NS_RAY[R{i}.r2].NS_SEGMENT[segment_13]'
            get_value_x = lt.DbGet(Ray, "Global_X")
            get_value_y = lt.DbGet(Ray, "Global_Y")
            data_array_x[i] = get_value_x
            data_array_y[i] = get_value_y
        print(f'{data_array_x[1] - data_array_x[5]},{data_array_y[1] - data_array_y[5]},'
              f'{data_array_x[2] - data_array_x[5]},{data_array_y[2] - data_array_y[5]},'
              f'{data_array_x[3] - data_array_x[5]},{data_array_y[3] - data_array_y[5]},'
              f'{data_array_x[4] - data_array_x[5]},{data_array_y[4] - data_array_y[5]},'
              f'{data_array_x[5] - data_array_x[5]},{data_array_y[5] - data_array_y[5]},'
              f'{data_array_x[6] - data_array_x[5]},{data_array_y[6] - data_array_y[5]},'
              f'{data_array_x[7] - data_array_x[5]},{data_array_y[7] - data_array_y[5]},'
              f'{data_array_x[8] - data_array_x[5]},{data_array_y[8] - data_array_y[5]},'
              f'{data_array_x[9] - data_array_x[5]},{data_array_y[9] - data_array_y[5]}')
def lens_tilt():
    ses = ltapy.session.Session(pid=10596)
    lt = ses.lt
    lt.Message("Successfully connected to LightTools!")
    # 初始化
    data_array_x = [0]*10
    data_array_y = [0]*10
    modlue = "LENS_MANAGER[1].COMPONENTS[Components].GROUP[group_3]"
    lens = "LENS_MANAGER[1].COMPONENTS[Components].GROUP[group_3].GROUP[Lens]"
    for r in range(10):
        lt.DbSet(modlue, "Alpha", 0)
        lt.DbSet(modlue, "Beta", 0)
        lt.DbSet(modlue, "Gamma", 0)
        lt.DbSet(lens, "Alpha", 0)
        lt.DbSet(lens, "Beta", 0)
        lt.DbSet(lens, "Gamma", 0)
        # 給予模組隨機旋轉角度(0~1)
        random_x = np.random.uniform(-0.5,0.5)
        random_y = np.random.uniform(-0.5,0.5)
        modlue_Alpha = lt.DbSet(modlue, "Alpha", random_x)
        modlue_Beta = lt.DbSet(modlue, "Beta", random_y)
        # 將光線對準Sensor中心
        img_X = lt.DbGet("LENS_MANAGER[1].COMPONENTS[Components].GROUP[group_3].SOLID[Image]", "X")
        img_Y = lt.DbGet("LENS_MANAGER[1].COMPONENTS[Components].GROUP[group_3].SOLID[Image]", "Y")
        # print(f'{img_X},{img_Y}')
        key_x = "LENS_MANAGER[1].OPT_MANAGER[Optimization_Manager].OPT_MERITFUNCTIONS[Merit_Function].OPT_NSRAYMERITFUNCTION[Center_X].OPT_NSRAYMFITEM[FanItem]"
        key_y = "LENS_MANAGER[1].OPT_MANAGER[Optimization_Manager].OPT_MERITFUNCTIONS[Merit_Function].OPT_NSRAYMERITFUNCTION[Center_Y].OPT_NSRAYMFITEM[FanItem]"
        lt.SetOption('DbUpdate', 0)
        lt.DbSet(key_x, "TargetAt", img_X, 1, 1)
        lt.DbSet(key_x, "TargetAt", img_X, 2, 1)
        lt.DbSet(key_x, "TargetAt", img_X, 3, 1)
        lt.DbSet(key_y, "TargetAt", img_Y, 1, 1)
        lt.DbSet(key_y, "TargetAt", img_Y, 2, 1)
        lt.DbSet(key_y, "TargetAt", img_Y, 3, 1)
        lt.SetOption('DbUpdate', 1)

        lt.Cmd("Optimize")
        # Lens旋轉量
        lens_Alpha = lt.DbGet(lens, "Alpha")
        lens_Beta = lt.DbGet(lens, "Beta")
        # 各光線位置
        for i in range(1, 10):
            Ray = f'LENS_MANAGER[1].NS_RAYS[Rays].NS_FAN[R{i}].NS_RAY[R{i}.r2].NS_SEGMENT[segment_13]'
            get_value_x = lt.DbGet(Ray, "Global_X")
            get_value_y = lt.DbGet(Ray, "Global_Y")
            data_array_x[i] = get_value_x
            data_array_y[i] = get_value_y
        print(f'{data_array_x[1]-data_array_x[5]},{data_array_y[1]-data_array_y[5]},'
              f'{data_array_x[2]-data_array_x[5]},{data_array_y[2]-data_array_y[5]},'
              f'{data_array_x[3]-data_array_x[5]},{data_array_y[3]-data_array_y[5]},'
              f'{data_array_x[4]-data_array_x[5]},{data_array_y[4]-data_array_y[5]},'
              f'{data_array_x[5]-data_array_x[5]},{data_array_y[5]-data_array_y[5]},'
              f'{data_array_x[6]-data_array_x[5]},{data_array_y[6]-data_array_y[5]},'
              f'{data_array_x[7]-data_array_x[5]},{data_array_y[7]-data_array_y[5]},'
              f'{data_array_x[8]-data_array_x[5]},{data_array_y[8]-data_array_y[5]},'
              f'{data_array_x[9]-data_array_x[5]},{data_array_y[9]-data_array_y[5]}')

lens_shift()
