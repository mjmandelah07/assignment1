# Given a list slice it into 3 equal chunks and reverse each chunk
sampleList = [11, 45, 8, 23, 14, 12, 78, 45, 89]
chunk_1 = sampleList[:3]
chunk_2 = sampleList[3:6]
chunk_3 = sampleList[6:9]

print("Original list:", sampleList)
print("Chunk  1:", chunk_1)
print("After reversing chunk 1:", chunk_1[::-1])
print("chunk 2:", chunk_2)
print('After reversing chunk 2:', chunk_2[::-1])
print("chunk 3:", chunk_3)
print("After reversing chunk 3:", chunk_3[::-1])