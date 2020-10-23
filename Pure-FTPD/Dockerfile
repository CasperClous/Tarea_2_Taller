FROM ubuntu

WORKDIR /pure_FTP

ARG DEBIAN_FRONTEND=noninteractive

RUN apt-get -yqq update \
&& apt-get -y upgrade \
&& apt-get -y install build-essential \
&& apt-get -y install libplib-dev \
&& apt-get -y install apt-utils \
&& apt-get -y install make \
&& apt-get -y install -y autoconf-archive \
&& apt-get -y install -y git \
&& apt-get -y install -y automake \
&& git clone https://github.com/jedisct1/pure-ftpd.git \
&& cd pure-ftpd \
&& aclocal \
&& autoreconf -vfi \
&& automake -a \
&& ./configure --with-everything \
&& make -j4 \
&& make install
RUN /usr/local/sbin/pure-ftpd &

RUN groupadd -g 1000 ftp && useradd -d /home/ftp -s /bin/bash -m ftp -u 1000 -g 1000
USER ftp
ENV HOME /home/ftp
