// g++ -g3 -ggdb -O0 -DDEBUG -I/usr/include/cryptopp Driver.cpp -o Driver.exe -lcryptopp -lpthread
// g++ -g -O2 -DNDEBUG -I/usr/include/cryptopp Driver.cpp -o Driver.exe -lcryptopp -lpthread

#include <crypto++/osrng.h>
using CryptoPP::AutoSeededRandomPool;

#include <iostream>
using std::cout;
using std::cerr;
using std::endl;

#include <string>
using std::string;

#include <cstdlib>
using std::exit;

#include <crypto++/cryptlib.h>
using CryptoPP::Exception;

#include <crypto++/hmac.h>
using CryptoPP::HMAC;

#include <crypto++/sha.h>
using CryptoPP::SHA256;

#include <crypto++/hex.h>
using CryptoPP::HexEncoder;
using CryptoPP::HexDecoder;

#include <crypto++/filters.h>
using CryptoPP::StringSink;
using CryptoPP::StringSource;
using CryptoPP::HashFilter;
using CryptoPP::HashVerificationFilter;

#include <crypto++/secblock.h>
using CryptoPP::SecByteBlock;

int main(int argc, char* argv[])
{
	 int n_times = atoi(argv[1]);
	 // int wait_time = atoi(argv[2]);

	 // wait time for key exchange added in driver function

	// for(int iter2 = 0; iter2 < n_times ; iter2++) {
		AutoSeededRandomPool prng;

		SecByteBlock key(16);
		prng.GenerateBlock(key, key.size());

		string plain = "Yoda said, Do or do not. There is no try.";
		string mac, encoded;

		/*********************************\
		\*********************************/

		// Pretty print key
		encoded.clear();
		StringSource(key, key.size(), true,
			new HexEncoder(
				new StringSink(encoded)
			) // HexEncoder
		); // StringSource
		// cout << "key: " << encoded << endl;

		// cout << "plain text: " << plain << endl;

		/*********************************\
		\*********************************/

		try
		{
			HMAC< SHA256 > hmac(key, key.size());		

			StringSource(plain, true, 
				new HashFilter(hmac,
					new StringSink(mac)
				) // HashFilter      
			); // StringSource
		}
		catch(const CryptoPP::Exception& e)
		{
			cerr << e.what() << endl;
			exit(1);
		}

		/*********************************\
		\*********************************/

		// Pretty print MAC
		encoded.clear();
		StringSource(mac, true,
			new HexEncoder(
				new StringSink(encoded)
			) // HexEncoder
		); // StringSource
		// cout << "hmac: " << encoded << endl;

		/*********************************\
		\*********************************/

		try
		{
			HMAC< SHA256 > hmac(key, key.size());
			const int flags = HashVerificationFilter::THROW_EXCEPTION | HashVerificationFilter::HASH_AT_END;

			// Tamper with message
			// plain[0] ^= 0x01;

			// Tamper with MAC
			// mac[0] ^= 0x01;
			
			 for(int iter = 0; iter < n_times; iter++) {

			StringSource(plain + mac, true, 
				new HashVerificationFilter(hmac, NULL, flags)
			); // StringSource

			// cout << "Verified message" << endl;
		}
		}

		catch(const CryptoPP::Exception& e)
		{
			cerr << e.what() << endl;
			exit(1);
		}
	//}
	return 0;
}

