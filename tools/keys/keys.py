from crypt import AES256_cert_create

def main():
    transfer = input("Create transfer key? y/n")
    if transfer == "y":
        AES256_cert_create("transf.crt")
        print("transf.crt generated")

    retr = input("Create retrieve key? y/n")
    if retr == "y":
        AES256_cert_create("retrieve.crt")
        print("retrieve.crt generated")

    print("Complete!")

if __name__ == '__main__':
    main()