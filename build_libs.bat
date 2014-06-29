gcc -c -fPIC crypt.c -o crypt.o
gcc -shared -Wl,-soname,libcrypt.so -o libcrypt.so  crypt.o C:\OpenSSL-Win32\lib\MinGW\libeay32.a C:\OpenSSL-Win32\lib\MinGW\ssleay32.a