https://www.cnblogs.com/phinecos/archive/2010/05/22/1741667.html
<pre><code>
gcc -I /usr/local/include/lame lame_test.c -lmp3lame -o lame_test

yum install sox

# ./lame_test ./test.raw ./test.mp3
./lame_test: error while loading shared libraries: libmp3lame.so.0: cannot open shared object file: No such file or directory

发现libmp3lame.so.0 在/usr/local/lib下

export LD_LIBRARY_PATH=/usr/local/lib
---
gcc -shared -fPIC -I /usr/include/python2.7/ -I /usr/local/include/lame/ pylame.c lame_test.c -lmp3lame -o pylame.so

---
gcc -fPIC -I /usr/include/python2.7/ -I /usr/local/include/lame/ -c pylame.c -o pylame.o

gcc -fPIC -I /usr/include/python2.7/ -I /usr/local/include/lame/ -c lame_test.c -o lame_test.o

gcc -shared pylame.o lame_test.o -lmp3lame -o pylame.so

---
gcc -pthread -fno-strict-aliasing -O2 -g -pipe -Wall -Wp,-D_FORTIFY_SOURCE=2 -fexceptions -fstack-protector-strong --param=ssp-buffer-size=4 -grecord-gcc-switches -m64 -mtune=generic -D_GNU_SOURCE -fPIC -fwrapv -DNDEBUG -O2 -g -pipe -Wall -Wp,-D_FORTIFY_SOURCE=2 -fexceptions -fstack-protector-strong --param=ssp-buffer-size=4 -grecord-gcc-switches -m64 -mtune=generic -D_GNU_SOURCE -fPIC -fwrapv -fPIC -Iinclude -I/usr/include/python2.7/ -I/usr/local/include/lame/ -I/usr/include/python2.7 -c lame_test.c -o lame_test.o

gcc -pthread -fno-strict-aliasing -O2 -g -pipe -Wall -Wp,-D_FORTIFY_SOURCE=2 -fexceptions -fstack-protector-strong --param=ssp-buffer-size=4 -grecord-gcc-switches -m64 -mtune=generic -D_GNU_SOURCE -fPIC -fwrapv -DNDEBUG -O2 -g -pipe -Wall -Wp,-D_FORTIFY_SOURCE=2 -fexceptions -fstack-protector-strong --param=ssp-buffer-size=4 -grecord-gcc-switches -m64 -mtune=generic -D_GNU_SOURCE -fPIC -fwrapv -fPIC -Iinclude -I/usr/include/python2.7/ -I/usr/local/include/lame/ -I/usr/include/python2.7 -c pylame.c -o pylame.o

gcc -pthread -shared -Wl,-z,relro lame_test.o pylame.o -L/usr/local/lib -L/usr/lib64 -lpython2.7 -o pylame.so

gcc -pthread -shared -Wl,-z,relro lame_test.o pylame.o -L/usr/local/lib -lmp3lame -o pylame.so

“-L/usr/local/lib -lmp3lame”指定了 /usr/local/lib/libmp3lame.so

https://www.cnblogs.com/benio/archive/2010/10/25/1860394.html
</code></pre>