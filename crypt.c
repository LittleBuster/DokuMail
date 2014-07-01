 #include <openssl/evp.h>

#define BUFSIZE 1024
 

int do_crypt(char *infile, char *outfile, unsigned char key[32], unsigned char iv[8])
{
	int outlen, inlen;
	FILE *in, *out;
	unsigned char inbuf[BUFSIZE], outbuf[BUFSIZE];
	
	in = fopen(infile, "rb");
	out = fopen(outfile, "wb");	
	
	EVP_CIPHER_CTX ctx;
	const EVP_CIPHER * cipher;
	EVP_CIPHER_CTX_init(&ctx);
	cipher = EVP_aes_256_cfb();
	EVP_EncryptInit(&ctx, cipher, key, iv);

	for(;;) {
		inlen = fread(inbuf, 1, BUFSIZE, in);
		if(inlen <= 0) 
			break;

		if(!EVP_EncryptUpdate(&ctx, outbuf, &outlen, inbuf, inlen))
			return 0;

		fwrite(outbuf, 1, outlen, out);
	}
	if(!EVP_EncryptFinal(&ctx, outbuf, &outlen)) 
		return 0;

	fwrite(outbuf, 1, outlen, out);
	EVP_CIPHER_CTX_cleanup(&ctx);
	
	fclose(in);
	fclose(out);
	return 1;
} 

int do_decrypt(char *infile, char *outfile, unsigned char key[32], unsigned char iv[8])
{
	int outlen, inlen;
	FILE *in, *out;
	unsigned char inbuf[BUFSIZE], outbuf[BUFSIZE];
	
	in = fopen(infile, "rb");
	out = fopen(outfile, "wb");	
	
	EVP_CIPHER_CTX ctx;
	const EVP_CIPHER * cipher;
	EVP_CIPHER_CTX_init(&ctx);
	cipher = EVP_aes_256_cfb();
	EVP_DecryptInit(&ctx, cipher, key, iv);

	for(;;) {
		inlen = fread(inbuf, 1, BUFSIZE, in);
		if(inlen <= 0) break;

		if(!EVP_DecryptUpdate(&ctx, outbuf, &outlen, inbuf, inlen)) return 0;

		fwrite(outbuf, 1, outlen, out);

	}
	if(!EVP_DecryptFinal(&ctx, outbuf, &outlen)) return 0;

	fwrite(outbuf, 1, outlen, out);
	EVP_CIPHER_CTX_cleanup(&ctx);
	
	fclose(in);
	fclose(out);
	return 1;
}

extern int do_crypt(char *infile, char *outfile, unsigned char key[32], unsigned char iv[8]);
extern int do_decrypt(char *infile, char *outfile, unsigned char key[32], unsigned char iv[8]);