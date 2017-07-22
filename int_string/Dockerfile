FROM ubuntu
MAINTAINER yuawn
RUN apt-get update
RUN apt-get install xinetd -y
RUN apt-get install libc6-dev-i386 -y
RUN useradd -m int_string
RUN chown -R root:root /home/int_string
CMD ["/usr/sbin/xinetd","-dontfork"]
