# This builds on some iRODS compatible items.
# Ultimately, we will be getting an environment variable for which collection
# to use.

FROM      ytproject/yt-devel:latest
MAINTAINER Matthew Turk "matthewturk@gmail.com"
#
# install package dependencies to prevent Docker build from erring out
RUN wget -P /home/user ftp://ftp.renci.org/pub/irods/releases/4.0.3/irods-icommands-4.0.3-64bit.deb
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y `dpkg -I /home/user/irods-icommands-4.0.3-64bit.deb | sed -n 's/^ Depends: //p' | sed 's/,//g'`
RUN dpkg -i /home/user/irods-icommands-4.0.3-64bit.deb
