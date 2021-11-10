import argparse

def parse_args():
    parser = argparse.ArgumentParser(description='Submitting script')
    
    parser.add_argument('--url', default='https://www.wjx.cn/vj/YO6Htg1.aspx', type=str,
                        help='问卷地址')
    parser.add_argument('--hr', default=20, type=int,
                        help='时间(hr)')
    parser.add_argument('--min', default=0, type=int,
                        help='时间(min)')
    
    parser.add_argument('--name', default='柴文浩', type=str,
                        help='姓名')
    parser.add_argument('--id', default='3190110xxx', type=str,
                        help='学号')
    parser.add_argument('--phone', default='183xxxx0991', type=str,
                        help='电话')
    parser.add_argument('--loc', default='ZJUI', type=str,
                        help='单位')
    parser.add_argument('--grade', default='2019', type=str,
                        help='年级')

    args = parser.parse_args()
    return args