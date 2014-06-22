
Name: app-tomcat
Epoch: 1
Version: 1.0.0
Release: 1%{dist}
Summary: Apache Tomcat J2EE
License: MyLicense
Group: ClearOS/Apps
Packager: Packager
Vendor: Vendor
Source: %{name}-%{version}.tar.gz
Buildarch: noarch
Requires: %{name}-core = 1:%{version}-%{release}
Requires: app-base

%description
Apache Tomcat is an open source software implementation of the Java Servlet and JavaServer Pages technologies

%package core
Summary: Apache Tomcat J2EE - Core
License: MyLicense
Group: ClearOS/Libraries
Requires: app-base-core

%description core
Apache Tomcat is an open source software implementation of the Java Servlet and JavaServer Pages technologies

This package provides the core API and libraries.

%prep
%setup -q
%build

%install
mkdir -p -m 755 %{buildroot}/usr/clearos/apps/tomcat
cp -r * %{buildroot}/usr/clearos/apps/tomcat/


%post
logger -p local6.notice -t installer 'app-tomcat - installing'

%post core
logger -p local6.notice -t installer 'app-tomcat-core - installing'

if [ $1 -eq 1 ]; then
    [ -x /usr/clearos/apps/tomcat/deploy/install ] && /usr/clearos/apps/tomcat/deploy/install
fi

[ -x /usr/clearos/apps/tomcat/deploy/upgrade ] && /usr/clearos/apps/tomcat/deploy/upgrade

exit 0

%preun
if [ $1 -eq 0 ]; then
    logger -p local6.notice -t installer 'app-tomcat - uninstalling'
fi

%preun core
if [ $1 -eq 0 ]; then
    logger -p local6.notice -t installer 'app-tomcat-core - uninstalling'
    [ -x /usr/clearos/apps/tomcat/deploy/uninstall ] && /usr/clearos/apps/tomcat/deploy/uninstall
fi

exit 0

%files
%defattr(-,root,root)
/usr/clearos/apps/tomcat/controllers
/usr/clearos/apps/tomcat/htdocs
/usr/clearos/apps/tomcat/views

%files core
%defattr(-,root,root)
%exclude /usr/clearos/apps/tomcat/packaging
%dir /usr/clearos/apps/tomcat
/usr/clearos/apps/tomcat/deploy
/usr/clearos/apps/tomcat/language
/usr/clearos/apps/tomcat/libraries
