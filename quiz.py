from cryptography.fernet import Fernet

key = 'TluxwB3fV_GWuLkR1_BzGs1Zk90TYAuhNMZP_0q4WyM='

# Oh no! The code is going over the edge! What are you going to do?
message = b'gAAAAABb9sIQ64Am7MbBopmSDx91B7kekigGppBkRjjKHFc7Bo-tkV_fIodZJLh02Am3Z34o-8RLmGMgKvbnZFTsVJ9EUKNSsCy8X0EqXLsoPq5XPE_Nc34wIGOtdYAIDTcTNyMnMjcggRyR0wLke4uVBV6-0US6HHFUvhQGyyt9ItEthw357_2AEasCA5h0124OOc9E2-2K'

def main():
    print('running main')
    f = Fernet(key)
    print(f.decrypt(message))


if __name__ == "__main__":
    main()
