gcc -c -fPIC crypt.c -o crypt.o
gcc -shared -Wl,-soname,crypt.so -o libcrypt.so  crypt.o -lssl -lcrypto
