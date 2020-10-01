FROM ubuntu

WORKDIR /FileZilla

ARG DEBIAN_FRONTEND=noninteractive

#La base del Docker
RUN sed -i~orig -e 's/# deb-src/deb-src/' /etc/apt/sources.list \
&& apt-get -yqq update \
&& apt-get -y upgrade 


#Las cosas esenciales y las de build-dep
RUN apt-get -y install apt-utils \
&& apt-get -y install build-essential \
&& apt-get -y build-dep filezilla \
&& apt-get -y install make \
&& apt-get -y install autoconf-archive \
&& apt-get -y install autoconf \
&& apt-get -y install automake \
&& apt-get -y install subversion \
&& apt-get -y install wget \
&& apt-get -y install curl \
&& apt-get -y install libgnutls30 \
&& apt-get -y install cmake


#GnuTLS
RUN wget ftp://ftp.gnutls.org/gcrypt/gnutls/v3.6/gnutls-3.6.15.tar.xz \
&& tar xf gnutls-3.6.15.tar.xz \
&& cd gnutls-3.6.15 \
&& autoreconf -vfi \
&& ./configure --with-included-unistring \
&& make -j8 \
&& make install 


#wxWidgets
RUN wget https://github.com/wxWidgets/wxWidgets/releases/download/v3.1.4/wxWidgets-3.1.4.tar.bz2 \
&& tar xvf wxWidgets-3.1.4.tar.bz2 \
&& rm -r wxWidgets-3.1.4.tar.bz2 \
&& cd wxWidgets-3.1.4 \
&& ./configure \
&& make -j8 \
&& make install 

#Libid
RUN apt-get install -y libidn11-dev

#libdbus
RUN apt-get install -y libdbus-cpp-dev


#perl
RUN apt-get install -y perl

#El FileZilla de por si
RUN wget https://dl1.cdn.filezilla-project.org/client/FileZilla_3.50.0_x86_64-linux-gnu.tar.bz2 \
&& cd filezilla-3.50.0 \
RUN autoreconf -i
RUN ./configure 
RUN make -j8
RUN make install


ENTRYPOINT [~/Documents/Tarea_2_Taller/fileZilla/ElFile]
