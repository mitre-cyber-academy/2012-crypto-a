I've got a very simple challenge put together that requires the contestants to first guess a one byte XOR key to decrypt a file and then recognize that the contents are base64 encoded.  They can use base64 tools in Python, Perl, or the unix base64 command to decode it.  That will yield an executable that they run to get the key.  We would just hand the contestants the challenge file that python crypto1.py create produces.

gcc -o crypto1 crypto1.c
python crypto1.py create
python crypto1.py solved
./solved
The key is MCA-98DA37CC
