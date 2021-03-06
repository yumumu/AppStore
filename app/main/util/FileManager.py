#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by why001 on 20/05/2017

import os, glob, zipfile
from config import base_dir

app_dir = 'AppFiles'
temp_dir = 'TempFiles'
file_type = {
    'iOS': '*.ipa',
    'Android': '*.apk'
}

def save_user_file(user_id, platform_type, app_id, version_number, app_file):
    if user_id and platform_type and app_file:
        file_dir = app_dir
        file_dir += '/' + str(user_id)
        file_dir += '/' + platform_type
        file_dir += '/' + app_id
        file_dir += '/' + str(version_number)
        save_path = os.path.join(base_dir, file_dir)
        os.makedirs(save_path, exist_ok=True)
        file_name = app_file.filename
        app_file.save(os.path.join(save_path, file_name))
        return True
    else:
        return False


def file_path(user_id, platform_type, app_id, version_number):
    app_path = base_dir + '/' + app_dir
    app_path += '/' + str(user_id)
    app_path += '/' + platform_type
    app_path += '/' + app_id
    app_path += '/' + str(version_number)

    os.chdir(app_path)
    files = glob.glob(file_type[platform_type])
    if len(files) > 0:
        return os.path.join(app_path, files[0])
    else:
        return None


def save_temp_file(temp_file, session_id):
    file_dir = app_dir + '/' + temp_dir
    file_dir += '/' + session_id
    save_path = os.path.join(base_dir, file_dir)
    os.makedirs(save_path, exist_ok=True)
    dest_path = os.path.join(save_path, temp_file.filename)
    temp_file.save(dest_path)
    return dest_path

def save_temp_file_with_name(temp_file, file_name, session_id):
    file_dir = app_dir + '/' + temp_dir
    file_dir += '/' + session_id
    save_path = os.path.join(base_dir, file_dir)
    os.makedirs(save_path, exist_ok=True)
    dest_path = os.path.join(save_path, file_name)
    temp_file.save(dest_path)
    return dest_path

def save_blob_file(temp_file, file_name, session_id):
    file_dir = app_dir + '/' + temp_dir
    file_dir += '/' + session_id
    save_path = os.path.join(base_dir, file_dir)
    os.makedirs(save_path, exist_ok=True)
    blob_path = os.path.join(save_path, file_name)
    temp_file.save(blob_path)
    return blob_path


def get_plist_path(blob_path):
    head, tail = os.path.split(blob_path)
    zip_ref = zipfile.ZipFile(blob_path, 'r')
    zip_ref.extractall(head)
    zip_ref.close()

    return os.path.join(head, 'Info.plist')

def delete_file(file_path):
    pass