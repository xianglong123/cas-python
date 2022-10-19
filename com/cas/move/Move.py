import pymysql
from gmssl.sm4 import CryptSM4, SM4_ENCRYPT, SM4_DECRYPT
import base64

mobile = ''

class SM4Utils:

    def __init__(self, ):
        pass

    # 加密方法
    def encryptData_ECB(self, plain_text):
        # 创建 SM4对象
        crypt_sm4 = CryptSM4()
        # 定义key值
        secret_key = bytes().fromhex('0e00bca58b4b9243e0550dd9d22ff700')
        # print("key: ", secret_key)

        # 设置key
        crypt_sm4.set_key(secret_key, SM4_ENCRYPT)

        # 调用加密方法加密(十六进制的bytes类型)
        encrypt_value = crypt_sm4.crypt_ecb(plain_text)
        # print("encrypt_value: ", encrypt_value)

        # 用base64.b64encode转码（编码后的bytes）
        cipher_text = base64.b64encode(encrypt_value)

        # print("加密后：", cipher_text)
        # print(cipher_text.decode('utf-8', 'ignore'))
        # 返回加密后的字符串
        return cipher_text.decode('utf-8', 'ignore')

    def decryptData_ECB(self, cipher_text):
        crypt_sm4 = CryptSM4()
        secret_key = bytes().fromhex('0e00bca58b4b9243e0550dd9d22ff700')
        crypt_sm4.set_key(secret_key, SM4_DECRYPT)
        # 将转入参数base64.b64decode解码成十六进制的bytes类型
        byt_cipher_text = base64.b64decode(cipher_text)
        # 调用加密方法解密，解密后为bytes类型
        decrypt_value = crypt_sm4.crypt_ecb(byt_cipher_text)
        return decrypt_value.decode('utf-8', 'ignore')


class DbUtils:
    def __init__(self, ):
        pass

    # 获取连接
    def execute(self, sql):
        try:
            db = pymysql.connect(host='10.4.8.125',
                                 port=6446,
                                 user='dicpuat',
                                 password='Dicpuat#123',
                                 database='dicp_uat')
        except Exception as e:
            print('数据库连接不到，检查是否连接UAT网络，😠')
            return
        # 使用 cursor() 方法创建一个游标对象 cursor
        cursor = db.cursor()
        # 使用 execute()  方法执行 SQL 查询
        cursor.execute(sql)
        # 使用 fetchone() 方法获取单条数据.
        db.commit();
        print("操作成功！")
        # 关闭数据库连接
        cursor.close();
        db.close()

def moveOutSql():
    global mobile
    if mobile == '':
        date = input("请输入手机号明文：")
        mobile = date
    else:
        pass
    sm4 = SM4Utils()
    mobileEnc = sm4.encryptData_ECB(mobile.encode("utf-8"))
    print("select * from dicp_eic_info where mobile_no ='" + mobileEnc + "'")
    print("select * from dicp_user where mobile_no ='" + mobileEnc + "'")
    print("select * from  dim_net_manager_info where mobile_no='" + mobileEnc + "'")
    print("select * from  dicp_app_info where mobile ='" + mobileEnc + "'")


def moveInDicpEicInfo():
    date = input("请输入DicpEicInfo查询数据：")
    if date == 'end':
        print("子流程终止")
        return
    sql = "INSERT INTO dicp_uat.dicp_eic_info (eic_id, mobile_no, user_id, eic_info, pid, eic_source, personal_status, eic_counter, eic_effect_time, eic_expire_time, CREATE_DATE, create_time, eic_status, tm_smp, bussiness_name, update_time) VALUES (" + date + ")"
    print(sql)
    DbUtils().execute(sql)
    pass


def moveInDicpUser():
    date = input("请输入DicpUser查询数据：")
    if date == 'end':
        print("子流程终止")
        return
    sql = "INSERT INTO dicp_uat.dicp_user (user_id, mobile_no, id_no, name, age, attribution_area_no, sex, birthday, register_merchant_id, photo_url, register_date, register_time, register_source, super_card_flag, seid, identity_card_positive_url, identity_card_reverse_url, status, tm_smp, nation, user_prov_id, user_prov_name, user_city_id, user_city_name) VALUES (" + date + ")"
    print(sql)
    DbUtils().execute(sql)
    pass


def moveInManager():
    date = input("请输入查询数据：")
    if date == 'end':
        print("子流程终止")
        return
    sql = "INSERT INTO dicp_uat.dicp_eic_info (eic_id, mobile_no, user_id, eic_info, pid, eic_source, personal_status, eic_counter, eic_effect_time, eic_expire_time, CREATE_DATE, create_time, eic_status, tm_smp, bussiness_name, update_time) VALUES (" + date + ")"
    print(sql)
    DbUtils().execute(sql)
    pass

    # 'BIP2209290000000000000000148768', '/Zd49QQzINngvMgGHI9UIw==', '180****6392', null, null, '0', '04', '0', 'M', '0', '2022-09-29 14:07:47', '2022-09-29 14:07:48', '20220929140748'


def moveInDicpAppInfo():
    date = input("请输入查询数据：")
    if date == 'end':
        print("子流程终止")
        return
    sql = "INSERT INTO dicp_uat.dicp_app_info (id, mobile, mobile_mask, seid, card_version, status, app_status, counter, channel_type, delete_flag, create_time, update_time, tm_smp) VALUES (" + date + ")"
    print(sql)
    DbUtils().execute(sql)
    pass


if __name__ == '__main__':
    # print("规则：p1-生成迁出SQL")
    print("规则：u1-迁入dicp_eic_info")
    print("规则：u2-迁入dicp_user")
    print("规则：u3-迁入dim_net_manager_info ")
    print("规则：u4-迁入dicp_app_info")
    print("规则：u4-迁入dicp_app_info")
    print("规则：end-结束子流程/整个流程")
    date = 'p1'
    while date != 'end':
        date = input("请选择规则：")
        if date == 'end':
            print('脚本退出')
            break
        # if date == 'p1':
        moveOutSql()
        # continue
        if date == 'u1':
            moveInDicpEicInfo()
            continue
        elif date == 'u2':
            moveInDicpUser()
            continue
        elif date == 'u3':
            moveInManager()
            continue
        elif date == 'u4':
            moveInDicpAppInfo()
            continue
        else:
            print('脚本退出')
            break
