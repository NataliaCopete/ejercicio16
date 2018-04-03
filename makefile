album.png:album.txt
	python grafica.py

album.txt:album.cpp
	c++ album.cpp
	./a.out>album.txt


