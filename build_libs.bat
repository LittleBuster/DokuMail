gcc -c -fPIC crypt.c -o crypt.ow
gcc -shared -Wl,-soname,libcrypt.dll -o libcrypt.dll  crypt.ow C:\OpenSSL-Win32\lib\MinGW\libeay32.a C:\OpenSSL-Win32\lib\MinGW\ssleay32.a

gcc -c -fPIC compress.c -o compress.o
gcc -shared -Wl,-soname,libcompress.dll -o libcompress.dll  compress.o C:\MinGW\zlib1.dll