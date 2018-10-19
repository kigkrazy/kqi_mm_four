#!/usr/bin/python
# -*- coding: utf-8 -*-


class GlobalVar:

    db_handle = None
    mq_client = None

    def set_db_handle(db):
        GlobalVar.db_handle = db
    @classmethod
    def get_db_handle(cls):
        return GlobalVar.db_handle
    @classmethod
    def set_mq_client(cls,mq_cli):
        GlobalVar.mq_client = mq_cli
    @classmethod
    def get_mq_client(cls):
        return GlobalVar.mq_client