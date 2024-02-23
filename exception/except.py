filename1 = input('원본 파일 이름을 입력하시오: ')
filename2 = input('복사 파일 이름을 입력하시오: ')

infile = open(filename1, 'rb')
outfile = open(filename2, 'wb')

while True:
    copy_buffer = infile.read(1024)
    print(len(copy_buffer))
    if not copy_buffer:
        break
    outfile.write(copy_buffer)

infile.close()
outfile.close()
print(filename1+'를 '+filename2+'로 복사하였습니다. ')