gcc -c -fPIC crypt.c -o crypt.o
gcc -shared -Wl,-soname,crypt.so -o libcrypt.so  crypt.o -lssl -lcrypto

gcc -c -fPIC compress.c -o compress.o
gcc -shared -Wl,-soname,libcompress.so -o libcompress.so  compress.o -lz