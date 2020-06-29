with open('testing.txt', 'w') as f:
	f.write('trying this again')
	
with open('testing.txt') as f: # 'r' mode is default
	print(f.read()) # worked
	
with open('testing.txt', 'a+') as f:
	f.write('\nhopefully appending this')
	f.seek(0) # resetting pointer to beginning. 2nd parameter optional, assumes 0 if not given
	print(f.read()) # worked
	print(f.tell()) # gives current pointer position (now at end again, following read call - 42!)
	f.seek(0)
	print(f.tell()) # worked again
	
with open('testing.txt', 'r+') as f:
	f.write('trying smeg again') # overwrites first line
	f.seek(0)
	print(f.read())
	f.seek(7, 0)
	f.write('this') # correcting first line
	f.seek(0)
	print(f.read()) # worked
	f.seek(0, 2) # places cursor at end
	f.write('\nand some more rubbish for experimentation')
	f.seek(0)
	print(f.read(50)) # reads specified number of bytes. in general 1 byte = 1 ASCII character
	print(f.read(50)) # picks up from where previous read() left off, unless cursor is moved
	f.seek(0)
	print(f.readline(1))
	print(f.readline(2))
	print(f.readline(3)) # does the same as f.read(). Pythonista bug?
	f.seek(0)
	print(f.readline()) # but works if no parameter supplied
	print(f.readlines()) # works. moves \n characters to ends of lines (typed at starts)
	f.seek(0)
	for line in f:
		print(line) # works but adds blank newlines. poss bug

