#!/usr/bin/python
# coding: utf8
"""
Author: Renato Machado
Objective: Creates a password, encrypt and validate the password
Change:
"""

import random
import bcrypt


def create_password(num_caract):

    char = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%&"
    if num_caract != num_caract:
        return {'erro': 'Falha na criação da senha.'}

    passwd = ""
    while len(passwd) != num_caract:
        passwd = passwd + random.choice(char)
    if len(passwd) == num_caract:
        return passwd


class TrataHash(object):

    @staticmethod
    def insere_hash(passwd):
        hash_senha = bcrypt.hashpw(passwd.encode('utf-8'), bcrypt.gensalt())
        return hash_senha

    @staticmethod
    def valida_senha(password, hash_senha):
        val_pass = bcrypt.hashpw(password.encode('utf-8'), hash_senha.encode('utf-8')) == hash_senha.encode('utf-8')
        return val_pass


if __name__ == '__main__':

    password = create_password(16)
    print(f'Senha criada: {password}')

    pass_hash = str(TrataHash.insere_hash(password)).split("'")[1]
    print(f'Senha criptografada: {pass_hash}')

    val_pass = TrataHash.valida_senha(password, pass_hash)
    print(f'Senha validada: {val_pass}')
