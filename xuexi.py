#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
@project: AutoXue
@file: xuexi.py
@author: wei zhang
@Copyright © 2021. All rights reserved.
'''
import datetime
import re
from unit import caps, cfg, logger, rules
from configparser import NoOptionError, NoSectionError
from secureRandom import decrypt
import subprocess
import time
from autoxue import AutoApp

nox_port = ('62001', '62025', '62026', '62027', '62028', '62029')
path_run = f'start /b /D "{cfg.get("emu_args", "emu_path")}"'
if cfg.get('emu_args', 'true_machine') == '1' or cfg.get('emu_args', 'true_machine').lower() == 'true':
    is_true_machine = True
else:
    is_true_machine = False

try:
    if cfg.get('test', 'is_test') == '0' or cfg.get('test', 'is_test').upper() == 'FALSE':
        is_test = False
    else:
        is_test = True
except (NoOptionError, NoSectionError):
    print("请检查default.ini文件中[test]中is_test是否设置为True、1或者False、0（大小写都无所谓）。")
    is_test = False

def adb_connect(**args):
    """
    启动adb连接模块
    """
    cmd = f'{path_run} adb connect {args["udid"]}'
    logger.info(f'[{args["username"]}]\033[27;31;46m 正在连接模拟器 {args["udid"]}，请稍候...\033[0m')
    while True:
        try:
            subp = subprocess.Popen(cmd, shell=True, stdout=open('.\\logs\\' + 'adbconnect.log', 'a'),stderr=subprocess.STDOUT)
            subp.communicate()
            break
        except subprocess.CalledProcessError as msg:
            logger.info(f'{msg},adb连接失败，5秒后重试...')
            time.sleep(10)

def stop_adb_server():
    cmd = f'{path_run} adb.exe '
    if 0 == subprocess.check_call(cmd + 'kill-server', shell=True, stdout=open('.\\logs\\' + 'adbconnect.log', 'a'), stderr=subprocess.STDOUT):
        logger.debug(f'\033[7;41m adb kill-server成功\033[0m')
        time.sleep(3)
    else:
        logger.info(f'\033[7;41m adb kill-server失败\033[0m')

def restart_adb_server():
    stop_adb_server()
    cmd = f'{path_run} adb.exe '
    if 0 == subprocess.check_call(cmd + 'start-server', shell=True, stdout=open('.\\logs\\' + 'adbconnect.log', 'a'), stderr=subprocess.STDOUT):
        logger.debug(f'\033[27;31;46m adb start-server成功\033[0m')
        time.sleep(3)
    else:
        logger.info(f'\033[27;31;46m adb start-server失败\033[0m')

def emu_start(**args):
    """
    启动模拟器
    """
    cmd = ''
    logger.info(f"[{args['username']}]\033[27;32;41m启动模拟器\033[0m")
    port = str(args['port'])
    if cfg.get('emu_args', 'emu_name').lower() == 'microvirt':
        cmd = f'{path_run} MEmuConsole.exe "{args["emu_name"]}"'
    elif cfg.get('emu_args', 'emu_name').lower() == 'nox':
        cmd = f'{path_run} NoxConsole.exe launch -name:{args["emu_name"]}'
    elif cfg.get('emu_args', 'emu_name').lower() == 'leidian':
        cmd = f'{path_run} dnconsole.exe launch --name {args["emu_name"]}'
    try:
        subp = subprocess.Popen(cmd, shell=True, stdout=open('.\\logs\\' + port + '.log', 'a'), stderr=subprocess.PIPE)
        subp.communicate()
    except Exception as e:
        logger.dubeg(e)
        pass

def emu_close_all():
    cmd = ''
    if cfg.get('emu_args', 'emu_name').lower() == 'microvirt':
        cmd = f'{path_run} memuc stopall'
    elif cfg.get('emu_args', 'emu_name').lower() == 'nox':
        cmd = f'{path_run} NoxConsole.exe quitall'
    elif cfg.get('emu_args', 'emu_name').lower() == 'leidian':
        cmd = f'{path_run} dnconsole.exe quitall'
    if 0 == subprocess.check_call(cmd, shell=True, stdout=open('.\\logs\\' + 'emu.log', 'a'), stderr=subprocess.STDOUT):
        logger.info(f'\033[27;31;46m 成功关闭已经打开的模拟器。\033[0m')
    else:
        logger.info(f'\033[27;31;46m 关闭模拟器操作失败...\033[0m')

def begin_study(**args):
    """
    启动学习或者测试模块
    """
    logger.info(f'\033[7;41m {args["username"]}开始学习。\033[0m')
    xuexi_app = AutoApp(args)
    if args['testapp']:
        xuexi_app.test()
    else:
        xuexi_app.start()
    logger.info(f'\033[7;41m 今日学习完成！！！\033[0m')

if __name__ == '__main__':
    begin_time = datetime.datetime.now()
    
    app_args_list = []

    user_list = list(set(re.split(r'[,，;；、/.\s]', cfg.get('users', 'study_users'))))
    for i in user_list:
        #根据用户名长度判断是否是RSA 1024位加密解密
        if len(cfg.get('users', f'username{i}')) > 11:
            username = decrypt(cfg.get('users', f'username{i}'), cfg.get('users', 'prikey_path'))
            password = decrypt(cfg.get('users', f'password{i}'), cfg.get('users', 'prikey_path'))
        else:
            username = cfg.get('users', f'username{i}')
            password = cfg.get('users', f'password{i}')
        
        if is_true_machine:
            emu_name = cfg.get('capability', 'devicename')
            udid = cfg.get('capability', 'udid')
        elif cfg.get('emu_args', 'emu_name').lower() == 'microvirt':
            emu_name = cfg.get('users', f'emu_mv_{i}')
            udid = f'127.0.0.1:215{int(i) - 1}3'
        elif cfg.get('emu_args', 'emu_name').lower() == 'nox':
            emu_name = cfg.get('users', f'emu_nox_{i}')
            udid = f'127.0.0.1:{nox_port[int(i) - 1]}'
        elif cfg.get('emu_args', 'emu_name').lower() == 'leidian':
            emu_name = cfg.get('users', f'emu_nox_{i}')
            udid = f'127.0.0.1:{5555 + 2 * (int(i) - 1)}'
        
        app_args_list.append(
            {
                'id': i,
                'username': username,
                'password': password,
                'emu_name': emu_name,
                'udid': udid,
                'host': '127.0.0.1',
                'port': 4723 + (int(i) - 1) * 2,
                'systemPort': 8200 + (int(i) - 1),
                'testapp': is_test
            })

    if is_true_machine:
        for run_args in app_args_list:
            begin_study(**run_args)
    else:
        emu_close_all()
        restart_adb_server()
        for run_args in app_args_list:
            emu_start(**run_args)
            time.sleep(20)
            adb_connect(**run_args)
            begin_study(**run_args)
        emu_close_all()
        stop_adb_server()

    end_time = datetime.datetime.now()
    logger.info(f'\033[7;41m 开始：{begin_time}  结束：{end_time}，总计耗时：{end_time - begin_time}\033[0m')