# Compute checksums

## Goal

Some file formats (images, videos, ...) are organised in "chunks",
containing a header and the data.
To make sure the files are not corrupted, checksums are sometimes computed.


Given a list of integers ranging from 0 to 255 (parameter *file_bytes*), representing the bytes of a file. You have to return the checksums of all the chunks. 
The file is structured as follows: 

* The first byte is the header of the first chunk, which defines its size (header is not counted in the chunk size).
* The next bytes are the chunk data.
* The next byte is the header of the second chunk, and so on.

The data you get in input will always be consistent.
For example, if the last chunk header is 5, then you have exactly 5 bytes just after, no more, no less. 

You have to retrieve all the chunks.
For each of them, sum up all their bytes (header not included), and keep only the 8 lowest bits to produce its checksum. Then return a list containing all the checksums. 

**Warning:** some chunk may have a size of 0. In that case, there is no data bytes.
The next byte is the header of the next chunk.

A zero-sized chunk has a checksum of 0.

The input data always contains at least one chunk.

## Detailed example

With these bytes:

3, 44, 55, 66, 2, 110, 220

The first byte is 3, so the first chunk has a size of 3. Its data is 
44, 55, 66. The sum is 165. But we have to keep only the 8 lowest bits.
165 modulo 256 is 165. 

The byte just after is 2, so the second chunk has a size of 2. Its data is 110, 220.
The sum is 330. But we have to keep only the 8 lowest bits. 330 modulo 256 is 74. 

The result to return is a list containing the bytes 165, 74 