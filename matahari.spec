%global specversion 14
%global upstream_version 0.6.0

%define _default_patch_fuzz 2

# Keep around for when/if required
#global alphatag {upstream_version}.git
%global mh_release %{?alphatag:0.}%{specversion}%{?alphatag:.%{alphatag}}%{?dist} 
# Messaging buses
%bcond_without dbus
%bcond_without qmf

Name:		matahari
Version:	0.6.0
Release:	%{mh_release}
Summary:	QMF Agents for Linux guests

Group:		Applications/System
License:	GPLv2
URL:		http://matahariproject.org

Source0:	https://github.com/matahari/matahari/downloads/matahari-0.6.0.tar.gz
Patch1:         cmake-2.6.diff
Patch2:		qpid-broker-only-load-ssl.diff
Patch3:		no-autogenerate-man-pages.diff
Patch4:		remove-unused-includes.diff
Patch5:		remove-qpidclient.diff
Patch6:		disable-by-default.diff

BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Obsoletes:  %{name}-selinux < %{version}-%{release}

# NOTE: The host API uses dbus for the machine uuid
Requires:	dbus
Requires:	qmf > 0.7
Requires:	pcre
Requires:	%{name}-broker
Requires:	%{name}-core
Requires:	%{name}-host
Requires:	%{name}-network
Requires:	%{name}-rpc
Requires:	%{name}-service
Requires:	%{name}-sysconfig
Requires:	%{name}-consoles

BuildRequires:	cmake
BuildRequires:	libuuid-devel
BuildRequires:	gcc-c++
BuildRequires:	pcre-devel
BuildRequires:	glib2-devel
BuildRequires:  sigar-devel > 1.6.5-0.2
BuildRequires:	libcurl-devel
BuildRequires:	nss-devel
BuildRequires:	help2man
BuildRequires:	augeas-devel
BuildRequires:	python2-devel

%if %{with qmf}
BuildRequires:	qpid-cpp-client-devel > 0.7
BuildRequires:	qpid-qmf-devel > 0.7
%endif

%if %{with dbus}
BuildRequires:	dbus-devel dbus-glib-devel polkit-devel libxslt
%endif

%description

Matahari provides QMF Agents that can be used to control and manage
various pieces of functionality, using the AMQP protocol

The Advanced Message Queuing Protocol (AMQP) is an open standard application
layer protocol providing reliable transport of messages

QMF provides a modeling framework layer on top of Qpid (which implements
AMQP).  This interface allows you to manage a host and its various components
as a set of objects with properties and methods

%package core
License:	GPLv2+
Summary:	Core files for Matahari
Group:		Applications/System
Requires(pre):	shadow-utils

%description core
Core files for Matahari

%if %{with qmf}
%package broker
License:	GPLv2+
Summary:	Optional AMQP Broker for Matahari
Group:		Applications/System
Requires:	%{name}-core = %{version}-%{release}
Requires:	%{name}-lib = %{version}-%{release}
Requires:	qpid-cpp-server > 0.7
Requires:	qpid-cpp-server-ssl > 0.7
Requires:	qmf > 0.7
Requires:       qpid-tools
Requires(post):     chkconfig
Requires(preun):    chkconfig
Requires(preun):    initscripts

%description broker
Optional AMQP Broker for Matahari
%endif

%package vios-proxy-host
License:	ASL 2.0
Summary:	Network proxy using virtioserial for QEMU host
Group:		Applications/System
Requires:       vios-proxy-host
Requires:	%{name}-broker = %{version}-%{release}
Requires(post):     chkconfig
Requires(preun):    chkconfig
Requires(preun):    initscripts

%description vios-proxy-host
%{name} specific host initialization scripts

%package vios-proxy-guest
License:	ASL 2.0
Summary:	Network proxy using virtioserial for QEMU host
Group:		Applications/System
Requires:       vios-proxy-guest
Requires:	%{name}-broker = %{version}-%{release}
Requires(post):     chkconfig
Requires(preun):    chkconfig
Requires(preun):    initscripts

%description vios-proxy-guest
%{name} specific guest initialization scripts

%package lib
License:	GPLv2+
Summary:	C libraries used by Matahari agents
Group:		Applications/System
Requires:	%{name}-core = %{version}-%{release}
Requires:	sigar > 1.6.5-0.2

%description lib
C libraries used by Matahari agents

%package agent-lib
License:		GPLv2+
Summary:		C++ library used by Matahari agents
Group:			Applications/System
Requires:		%{name}-lib = %{version}-%{release}
Requires:		qpid-cpp-client-ssl > 0.7

%description agent-lib
C++ library containing the base class for Matahari agents

%package python
License:	GPLv2+
Summary:	Matahari Python API
Group:		Applications/System
Requires:	python-qpid-qmf

%description python
Python libraries for Matahari

%package shell
License:	GPLv2+
Summary:	Matahari shell (mhsh)
Group:		Applications/System
Requires:	%{name}-python = %{version}-%{release}

%description shell
Interactive shell for accessing Matahari agents

%package host
License:	GPLv2+
Summary:	QMF agent for remote hosts
Group:		Applications/System
Requires:	%{name}-lib = %{version}-%{release}
Requires:	%{name}-agent-lib = %{version}-%{release}
Requires:	tuned
Requires(post):     chkconfig
Requires(preun):    chkconfig
Requires(preun):    initscripts

%description host
QMF agent for viewing and controlling remote hosts

%package network
License:	GPLv2+
Summary:	QMF agent for network devices
Group:		Applications/System
Requires:	%{name}-lib = %{version}-%{release}
Requires:	%{name}-agent-lib = %{version}-%{release}
Requires(post):     chkconfig
Requires(preun):    chkconfig
Requires(preun):    initscripts
Obsoletes:	matahari-net < %{version}-%{release}
Provides:	matahari-net = %{version}-%{release}

%description network
QMF agent for viewing and controlling network devices

%package rpc
License:	GPLv2+
Summary:	QMF agent for RPC plugins
Group:		Applications/System
Requires:	%{name}-lib = %{version}-%{release}
Requires:	%{name}-agent-lib = %{version}-%{release}
Requires:	%{name}-python = %{version}-%{release}
Requires(post):     chkconfig
Requires(preun):    chkconfig
Requires(preun):    initscripts

%description rpc
QMF agent for dispatching RPC calls to plugins

%package service
License:	GPLv2+
Summary:	QMF agent for system services
Group:		Applications/System
Requires:	%{name}-lib = %{version}-%{release}
Requires:	%{name}-agent-lib = %{version}-%{release}
Requires(post):     chkconfig
Requires(preun):    chkconfig
Requires(preun):    initscripts

%description service
QMF agent for viewing and controlling system services

%package sysconfig
License:	GPLv2+
Summary:	QMF agent for post boot configuration services
Group:		Applications/System
Requires:	%{name}-lib = %{version}-%{release}
Requires:	%{name}-agent-lib = %{version}-%{release}
Requires(post):     chkconfig
Requires(preun):    chkconfig
Requires(preun):    initscripts

%description sysconfig
QMF agent/console for providing post boot capabilities

%package devel
License:	GPLv2+
Summary:	Matahari development package
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-lib = %{version}-%{release}
Requires:	%{name}-agent-lib = %{version}-%{release}
Requires:	qpid-cpp-client-devel > 0.7
Requires:	qpid-qmf-devel > 0.7
Requires:	glib2-devel
Requires(post):     chkconfig
Requires(preun):    chkconfig
Requires(preun):    initscripts

%description devel
Headers and shared libraries for developing Matahari agents

%package consoles
License:       GPLv2+
Summary:       QMF console for monitoring various agents
Group:	       Applications/System
Requires:      %{name}-lib = %{version}-%{release}
Requires:      %{name}-agent-lib = %{version}-%{release}

%description consoles
QMF console for monitoring various agents

%prep
%setup -q -n matahari-%{upstream_version}
%patch1 -p1
%patch2 -p1
%patch3 -p1
find . -name *8.gz -exec rm -rf {} +
%patch4 -p1
%patch5 -p1
%patch6 -p1

%build
%{cmake} -DCMAKE_BUILD_TYPE=RelWithDebInfo %{!?with_qmf: -DWITH-QMF:BOOL=OFF} %{!?with_dbus: -DWITH-DBUS:BOOL=OFF} -Dinitdir=%{_initddir} -Dsysconfdir=%{_sysconfdir} .
make -f Makefile %{?_smp_mflags}

%install
rm -rf %{buildroot}
make DESTDIR=%{buildroot} -f Makefile install

%if %{defined _unitdir}
rm -f $RPM_BUILD_ROOT/%{_sysconfdir}/rc.d/init.d/matahari-service
rm -f $RPM_BUILD_ROOT/%{_sysconfdir}/rc.d/init.d/matahari-network
rm -f $RPM_BUILD_ROOT/%{_sysconfdir}/rc.d/init.d/matahari-host
rm -f $RPM_BUILD_ROOT/%{_sysconfdir}/rc.d/init.d/matahari-rpc
rm -f $RPM_BUILD_ROOT/%{_sysconfdir}/rc.d/init.d/matahari-sysconfig
rm -f $RPM_BUILD_ROOT/%{_sysconfdir}/rc.d/init.d/matahari-sysconfig-console
rm -f $RPM_BUILD_ROOT/%{_sysconfdir}/rc.d/init.d/matahari-broker
rm -f $RPM_BUILD_ROOT/%{_sysconfdir}/rc.d/init.d/matahari-vios-proxy-host
rm -f $RPM_BUILD_ROOT/%{_sysconfdir}/rc.d/init.d/matahari-vios-proxy-guest
%endif

%post -n matahari-lib -p /sbin/ldconfig
%postun -n matahari-lib -p /sbin/ldconfig

%post -n matahari-agent-lib -p /sbin/ldconfig
%postun -n matahari-agent-lib
# Can't use -p, gives: '/sbin/ldconfig: relative path `0' used to build cache' error
/sbin/ldconfig

%if %{with qmf}
#== Host

%post host
/sbin/chkconfig --add matahari-host

%preun host
if [ $1 = 0 ]; then
   /sbin/service matahari-host stop >/dev/null 2>&1 || :
   chkconfig --del matahari-host
fi

%postun host
if [ "$1" -ge "1" ]; then
    /sbin/service matahari-host condrestart >/dev/null 2>&1 || :
fi

#== Network

%post network
/sbin/chkconfig --add matahari-network

%preun network
if [ $1 = 0 ]; then
   /sbin/service matahari-network stop >/dev/null 2>&1 || :
   chkconfig --del matahari-network
fi

%postun network
if [ "$1" -ge "1" ]; then
    /sbin/service matahari-network condrestart >/dev/null 2>&1 || :
fi

#== RPC

%post rpc
/sbin/chkconfig --add matahari-rpc

%preun rpc
if [ $1 = 0 ]; then
   /sbin/service matahari-rpc stop >/dev/null 2>&1 || :
   chkconfig --del matahari-rpc
fi

%postun rpc
if [ "$1" -ge "1" ]; then
    /sbin/service matahari-rpc condrestart >/dev/null 2>&1 || :
fi

#== Services

%post service
/sbin/chkconfig --add matahari-service

%preun service
if [ $1 = 0 ]; then
   /sbin/service matahari-service stop >/dev/null 2>&1 || :
   chkconfig --del matahari-service
fi

%postun service
if [ "$1" -ge "1" ]; then
    /sbin/service matahari-service condrestart >/dev/null 2>&1 || :
fi

#== sysconfig

%post sysconfig
/sbin/chkconfig --add matahari-sysconfig

%preun sysconfig
if [ $1 = 0 ]; then
   /sbin/service matahari-sysconfig stop >/dev/null 2>&1 || :
   chkconfig --del matahari-sysconfig
fi

%postun sysconfig
if [ "$1" -ge "1" ]; then
    /sbin/service matahari-sysconfig condrestart >/dev/null 2>&1 || :
fi

#== Broker

%post broker
/sbin/chkconfig --add matahari-broker

%preun broker
if [ $1 = 0 ]; then
    /sbin/service matahari-broker stop >/dev/null 2>&1 || :
    chkconfig --del matahari-broker
fi

%postun broker
if [ "$1" -ge "1" ]; then
    /sbin/service matahari-broker condrestart >/dev/null 2>&1 || :
fi

#== Vios Proxy Host

%post vios-proxy-host
/sbin/chkconfig --add matahari-vios-proxy-host

%preun vios-proxy-host
if [ $1 = 0 ]; then
   /sbin/service matahari-vios-proxy-host stop >/dev/null 2>&1 || :
   chkconfig --del matahari-vios-proxy-host
fi

%postun vios-proxy-host
if [ "$1" -ge "1" ]; then
    /sbin/service matahari-vios-proxy-host condrestart >/dev/null 2>&1 || :
fi

#== Vios Proxy Guest

%post vios-proxy-guest
/sbin/chkconfig --add matahari-vios-proxy-guest

%preun vios-proxy-guest
if [ $1 = 0 ]; then
   /sbin/service matahari-vios-proxy-guest stop >/dev/null 2>&1 || :
   chkconfig --del matahari-vios-proxy-guest
fi

%postun vios-proxy-guest
if [ "$1" -ge "1" ]; then
    /sbin/service matahari-vios-proxy-guest condrestart >/dev/null 2>&1 || :
fi

#== Core

%pre core
getent group qpidd >/dev/null || groupadd -r qpidd
exit 0

%endif

%clean
test "x%{buildroot}" != "x" && rm -rf %{buildroot}

%files
%defattr(644, root, root, 755)
%doc AUTHORS COPYING

%files agent-lib
%defattr(644, root, root)
%attr(755, -, -) %dir %{_datadir}/matahari/
%doc AUTHORS COPYING

%if %{with qmf}
%{_libdir}/libmcommon_qmf.so.*
%endif

%if %{with dbus}
%{_libdir}/libmcommon_dbus.so.*
%endif

%files core
%defattr(644, root, root)
%doc AUTHORS COPYING
%config(noreplace) %{_sysconfdir}/sysconfig/matahari
%if %{with qmf}
%dir %attr(0770, root, qpidd) %{_localstatedir}/lib/%{name}
%endif

%files python
%defattr(644, root, root, 755)
%doc AUTHORS COPYING
%{python_sitelib}/matahari/*.py
%{python_sitelib}/matahari/*.pyc
%{python_sitelib}/matahari/*.pyo

%files shell
%defattr(644, root, root, 755)
%doc AUTHORS COPYING
%attr(755, -, -) %{_bindir}/mhsh
%{python_sitelib}/matahari/shell/*.py
%{python_sitelib}/matahari/shell/*.pyc
%{python_sitelib}/matahari/shell/*.pyo
%{python_sitelib}/matahari/shell/interpreter/*.py
%{python_sitelib}/matahari/shell/interpreter/*.pyc
%{python_sitelib}/matahari/shell/interpreter/*.pyo

%files lib
%defattr(644, root, root, 755)
%{_libdir}/libmcommon.so.*
%{_libdir}/libmhost.so.*
%{_libdir}/libmnetwork.so.*
%{_libdir}/libmrpc.so.*
%{_libdir}/libmservice.so.*
%{_libdir}/libmsysconfig.so.*
%doc AUTHORS COPYING

%files network
%defattr(644, root, root, 755)
%doc AUTHORS COPYING
%if %{defined _unitdir}
%{_unitdir}/matahari-network.service
%endif

%if %{with qmf}
%if %{undefined _unitdir}
%attr(755, root, root) %{_initddir}/matahari-network
%endif
%attr(755, root, root) %{_sbindir}/matahari-qmf-networkd
%{_mandir}/man8/matahari-qmf-networkd.8*
%endif

%if %{with dbus}
%attr(755, root, root) %{_sbindir}/matahari-dbus-networkd

%{_datadir}/polkit-1/actions/org.matahariproject.Network.policy
%{_datadir}/dbus-1/interfaces/org.matahariproject.Network.xml
%{_datadir}/dbus-1/system-services/org.matahariproject.Network.service
%config %{_sysconfdir}/dbus-1/system.d/org.matahariproject.Network.conf
%endif

%files host
%defattr(644, root, root, 755)
%doc AUTHORS COPYING
%if %{defined _unitdir}
%{_unitdir}/matahari-host.service
%endif

%if %{with qmf}
%if %{undefined _unitdir}
%attr(755, root, root) %{_initddir}/matahari-host
%endif
%attr(755, root, root) %{_sbindir}/matahari-qmf-hostd
%{_mandir}/man8/matahari-qmf-hostd.8*
%endif

%if %{with dbus}
%attr(755, root, root) %{_sbindir}/matahari-dbus-hostd

%{_datadir}/polkit-1/actions/org.matahariproject.Host.policy
%{_datadir}/dbus-1/interfaces/org.matahariproject.Host.xml
%{_datadir}/dbus-1/system-services/org.matahariproject.Host.service
%config %{_sysconfdir}/dbus-1/system.d/org.matahariproject.Host.conf
%endif

%files rpc
%defattr(644, root, root, 755)
%doc AUTHORS COPYING
%attr(0755, -, -) %dir /usr/lib/matahari/plugins
%if %{defined _unitdir}
%{_unitdir}/matahari-rpc.service
%endif

%if %{with qmf}
%if %{undefined _unitdir}
%attr(755, root, root) %{_initddir}/matahari-rpc
%endif
%attr(755, root, root) %{_sbindir}/matahari-qmf-rpcd
%{_mandir}/man8/matahari-qmf-rpcd.8*
%endif

%files service
%defattr(644, root, root, 755)
%doc AUTHORS COPYING
%if %{defined _unitdir}
%{_unitdir}/matahari-service.service
%endif

%if %{with qmf}
%if %{undefined _unitdir}
%attr(755, root, root) %{_initddir}/matahari-service
%endif
%attr(755, root, root) %{_sbindir}/matahari-qmf-serviced
%{_mandir}/man8/matahari-qmf-serviced.8*
%endif

%if %{with dbus}
%attr(755, root, root) %{_sbindir}/matahari-dbus-serviced

%{_datadir}/polkit-1/actions/org.matahariproject.Resources.policy
%{_datadir}/polkit-1/actions/org.matahariproject.Services.policy
%{_datadir}/dbus-1/interfaces/org.matahariproject.Services.xml
%{_datadir}/dbus-1/system-services/org.matahariproject.Services.service
%config %{_sysconfdir}/dbus-1/system.d/org.matahariproject.Services.conf
%endif

%files sysconfig
%defattr(644, root, root, 755)
%doc AUTHORS COPYING

%if %{defined _unitdir}
%{_unitdir}/matahari-sysconfig.service
%endif

%if %{with qmf}
%if %{undefined _unitdir}
%attr(755, root, root) %{_initddir}/matahari-sysconfig
%endif
%attr(755, root, root) %{_sbindir}/matahari-qmf-sysconfigd
%{_mandir}/man8/matahari-qmf-sysconfigd.8*
%endif

%if %{with dbus}
%attr(755, root, root) %{_sbindir}/matahari-dbus-sysconfigd

%{_datadir}/polkit-1/actions/org.matahariproject.Sysconfig.policy
%{_datadir}/dbus-1/interfaces/org.matahariproject.Sysconfig.xml
%{_datadir}/dbus-1/system-services/org.matahariproject.Sysconfig.service
%config %{_sysconfdir}/dbus-1/system.d/org.matahariproject.Sysconfig.conf
%endif

%files consoles
%defattr(644, root, root, 755)
%doc AUTHORS COPYING

%if %{with qmf}
%if %{undefined _unitdir}
%attr(755, root, root) %{_initddir}/matahari-sysconfig-console
%endif
%attr(755, root, root) %{_sbindir}/matahari-qmf-sysconfig-consoled
%{_mandir}/man8/matahari-qmf-sysconfig-consoled.8*
%attr(755, root, root) %{_sbindir}/matahari-qmf-service-cli
%{_mandir}/man8/matahari-qmf-service-cli.8*

%if %{defined _unitdir}
%{_unitdir}/matahari-sysconfig-console.service
%endif
%endif

%if %{with qmf}
%files broker
%defattr(644, root, root, 755)
%if %{undefined _unitdir}
%attr(755, root, root) %{_initddir}/matahari-broker
%endif
%config(noreplace) %{_sysconfdir}/sysconfig/matahari-broker
%config(noreplace) %{_sysconfdir}/matahari-broker.conf
%attr(755, root, root) %{_sbindir}/matahari-brokerd
%{_mandir}/man8/matahari-brokerd.8*
%doc AUTHORS COPYING

%if %{defined _unitdir}
%{_unitdir}/matahari-broker.service
%endif

%else
%exclude %{_sysconfdir}/matahari-broker.conf
%endif

%files vios-proxy-host
%defattr(644, root, root, 755)
%config(noreplace) %{_sysconfdir}/sysconfig/matahari-vios-proxy

%if %{defined _unitdir}
%{_unitdir}/matahari-vios-proxy-host.service
%endif

%if %{with qmf}
%if %{undefined _unitdir}
%attr(755, root, root) %{_initddir}/matahari-vios-proxy-host
%endif
%endif

%files vios-proxy-guest
%defattr(644, root, root, 755)
%{_sysconfdir}/udev/rules.d/99-matahari-guest-agent.rules
%config(noreplace) %{_sysconfdir}/sysconfig/matahari-vios-proxy

%if %{defined _unitdir}
%{_unitdir}/matahari-vios-proxy-guest.service
%endif

%if %{with qmf}
%if %{undefined _unitdir}
%attr(755, root, root) %{_initddir}/matahari-vios-proxy-guest
%endif
%endif

%files devel
%defattr(644, root, root, 755)
%doc AUTHORS COPYING

%{_libdir}/libm*.so
%{_includedir}/matahari.h
%{_includedir}/matahari/config.h
%{_includedir}/matahari/logging.h
%{_includedir}/matahari/utilities.h
%{_includedir}/matahari/errors.h
%{_includedir}/matahari/dnssrv.h
%{_includedir}/matahari/host.h
%{_includedir}/matahari/network.h
%{_includedir}/matahari/rpc.h
%{_includedir}/matahari/sysconfig.h
%{_includedir}/matahari/services.h
%{_datadir}/cmake/Modules/FindMatahari.cmake

%if %{with qmf}
%{_includedir}/matahari/agent.h
%{_includedir}/matahari/object.h
%{_includedir}/matahari/mainloop.h
%{_datadir}/cmake/Modules/FindQPID.cmake
%endif

%if %{with dbus}
%{_includedir}/matahari/dbus_common.h
%{_includedir}/matahari/gobject_class.h
%{_datadir}/cmake/Modules/MatahariMacros.cmake
%{_datadir}/matahari/schema-to-dbus.xsl
%{_datadir}/matahari/dbus-to-c.xsl
%{_datadir}/matahari/check-policy.xsl
%endif

%changelog
* Tue Apr 24 2012 Zane Bitter <zbitter@redhat.com> 0.6.0-14
- Actually disable daemons by default
  Resolves: rhbz#806372

* Tue Mar 27 2012 Jeff Peeler <jpeeler@redhat.com> 0.6.0-13
- Re-enable non-x86 builds
  Resolves: rhbz#806923

* Tue Mar 27 2012 Jeff Peeler <jpeeler@redhat.com> 0.6.0-12
- Rebuild with updated qpid (0.14) package.

* Mon Mar 26 2012 Zane Bitter <zbitter@redhat.com> 0.6.0-11
- Disable non-x86 builds
  Resolves: rhbz#806923

* Fri Mar 23 2012 Jeff Peeler <jpeeler@redhat.com> 0.6.0-10
- Remove linking requirement for libqpidclient.
- Further Resolves: rhbz#805367

* Fri Mar 23 2012 Zane Bitter <zbitter@redhat.com> 0.6.0-9
- Disable daemons by default
  Resolves: rhbz#806372

* Wed Mar 21 2012 Jeff Peeler <jpeeler@redhat.com> 0.6.0-8
- Remove unused includes to avoid linking to qpid::sys symbols.
- Resolves: rhbz#805367

* Fri Mar 16 2012 Jeff Peeler <jpeeler@redhat.com> 0.6.0-7
- Rebuild to link with updated qpid package.

* Thu Mar 15 2012 Jeff Peeler <jpeeler@redhat.com> 0.6.0-6
- Fix man pages not being installed properly.
- Fix permission on lockfile preventing broker daemon startup.
- Resolves: rhbz#803718, rhbz#803590

* Fri Mar 9  2012 Zane Bitter <zbitter@redhat.com> 0.6.0-5
- Fix buffer overflow in broker wrapper
  Related: rhbz#795430
- Move shadow-utils dependency to correct subpackage

* Thu Mar 1 2012 Russell Bryant <rbryant@redhat.com> 0.6.0-4
- Remove unnecessary condrestart calls in %%post scripts.
- Make the broker wrapper tell qpidd to only load the ssl plugin.
- Resolves: rhbz#752325, rhbz#795430, rhbz#723078

* Thu Feb 16 2012 Zane Bitter <zbitter@redhat.com> 0.6.0-3
- Remove hard dependency on puppet

* Wed Feb 15 2012 Zane Bitter <zbitter@redhat.com> 0.6.0-2
- Add -broker dependency on -lib

* Tue Feb 14 2012 Zane Bitter <zbitter@redhat.com> 0.6.0-1
- Rebase to upstream release 0.6.0
  Resolves: rhbz#759243

* Mon Nov 07 2011 Matthew Garrett <mjg@redhat.com> 0.4.4-11
- Disable by default (rhbz#751790)751790

* Wed Oct 19 2011 Zane Bitter <zbitter@redhat.com> 0.4.4-9
- Read the CPU features on non-x86 architectures (rhbz#746288)
- Add daemons to chkconfig after installation (rhbz#746084)
- Resolves: rhbz#746084
- Related: rhbz#746288

* Tue Oct 11 2011 Russell Bryant <rbryant@redhat.com> 0.4.4-8
- Build for all arches
- Resolves: rhbz#663468

* Tue Oct 04 2011 Russell Bryant <rbryant@redhat.com> 0.4.4-7
- Validate sysconfig keys sooner (rhbz#741965)
- Add man pages in a patch instead of generating during build (rhbz#737088)
- Update sigar version dependency (rhbz#737541)
- Resolves: rhbz#741965, rhbz#737088, rhbz#737541

* Mon Sep 26 2011 Russell Bryant <rbryant@redhat.com> 0.4.4-6
- resolve coverity warnings in broker wrapper (rhbz#735426)
- add validation on sysconfig keys (rhbz#740090)
- store sysconfig keys in a subdir (rhbz#740091)
- Resolves: rhbz#740090, rhbz#740091
- Related: rhbz#735426

* Wed Sep 21 2011 Russell Bryant <rbryant@redhat.com> 0.4.4-5
- remove hard puppet dependency
- fix sysconfig agent no response (rhbz#740038)
- Resolves: rhbz#740038
- Related: rhbz#737137

* Mon Sep 19 2011 Russell Bryant <rbryant@redhat.com> 0.4.4-4
- Sync with upstream spec file fixes.
- add man pages (rhbz#737088)
- fix some sysconfig issues (rhbz#737137)
- ensure old processes get cleaned up after an upgrade (rhbz#737618)
- fix agent crash on NULL UUIDs (rhbz#739666)
- don't list "LSB" as a valid standard on windows (rhbz#739952)
- Resolves: rhbz#737088, rhbz#737137, rhbz#737618, rhbz#739666
- Resolves: rhbz#739952, rhbz#737541

* Fri Sep 09 2011 Russell Bryant <rbryant@redhat.com> 0.4.4-2
- Remove kstart integration.
- Related: rhbz#674578

* Thu Sep 08 2011 Russell Bryant <rbryant@redhat.com> 0.4.4-1
- Rebase to upstream release 0.4.4
- Resolves: rhbz#735419, rhbz#735429, rhbz#733483. rhbz#734981
- Resolves: rhbz#735426, rhbz#734536, rhbz#733468, rhbz#734522
- Resolves: rhbz#733393, rhbz#736468
- Related: rhbz#674578

* Wed Aug 31 2011 Russell Bryant <rbryant@redhat.com> 0.4.3-1
- Rebase to upstream release 0.4.3
- Resolves: rhbz#733384, rhbz#733393, rhbz#733451, rhbz#731858
- Resolves: rhbz#733150, rhbz#714249 

* Wed Aug 24 2011 Russell Bryant <rbryant@redhat.com> 0.4.2-9
- Update patch level to: 468fc0b
- Resolves: rhbz#733013

* Mon Aug 22 2011 Russell Bryant <rbryant@redhat.com> 0.4.2-8
- Update patch level to: a67ab9c
- Resolves: rhbz#732498, rhbz#730087, rhbz#731914. rhbz#731858, rhbz#731233
- Related: rhbz#728360

* Thu Aug 18 2011 Andrew Beekhof <abeekhof@fedoraproject.org> 0.4.2-7
- Update patch level to: d8d6ee9
- Resolves: rhbz#729332, rhbz#730044, rhbz#730066, rhbz#731534, rhbz#714249

* Tue Aug 16 2011 Andrew Beekhof <abeekhof@fedoraproject.org> 0.4.2-6
- Update patch level to: 6b5df25
- Resolves: rhbz#730066, rhbz#727194, rhbz#728360, rhbz#730087, rhbz#714249

* Thu Aug 11 2011 Andrew Beekhof <abeekhof@fedoraproject.org> 0.4.2-5
- Rebase on new upstream release: 325f740
- Resolves: rhbz#729516, rhbz#729331, rhbz#728977, #728988

* Wed Aug 09 2011 Andrew Beekhof <abeekhof@fedoraproject.org> 0.4.2-4
- Restore the pre-0.4.2-2 package layout 
- Related: rhbz#728631

* Tue Aug 09 2011 Andrew Beekhof <abeekhof@fedoraproject.org> 0.4.2-3
- Rebase on new upstream release: 0516313
- Resolves: rhbz#728631, rhbz#729063, rhbz#727192
- Resolves: rhbz#688191, rhbz#727961, rhbz#688193

* Thu Jul 26 2011 Adam Stokes <astokes@fedoraproject.org> 0.4.2-2
- Rebase on new upstream release: a242762
- Related:  rhbz#709649

* Thu Jul 21 2011 Andrew Beekhof <andrew@beekhof.net> 0.4.2-1
- Rebase on new upstream release
- Related:  rhbz#709649

* Wed Apr 20 2011 Andrew Beekhof <abeekhof@redhat.com> - 0.4.0-5
- Really do not start matahari services by default
- Resolves: rhbz#698370

* Wed Apr 20 2011 Andrew Beekhof <abeekhof@redhat.com> - 0.4.0-4
- Do not start matahari services by default
- Resolves: rhbz#698370

* Fri Apr 15 2011 Andrew Beekhof <abeekhof@redhat.com> - 0.4.0-3
- Add explicit dependancy on qpid-cpp-{client|server}-ssl
- Resolves: rhbz#696810

* Tue Apr  5 2011 Andrew Beekhof <abeekhof@redhat.com> - 0.4.0-2
- Add explicit versioned dependancies between relevant sub-packages
- Avoid the -libs package depending on QMF libraries
- Fix post and postun scripts for matahari-service
- Resolves: rhbz#688164 rhbz#692400 rhbz#688197 
- Resolves: rhbz#674185 rhbz#690587

* Thu Mar 24 2011 Andrew Beekhof <abeekhof@redhat.com> - 0.4.0-1
- Split the packaging up, one subpackage per agent 
- Remove dependancy on qpid-cpp-server-devel
- Convert agents to the QMFv2 API
- Rebuild for updated qpid-cpp
  Related: rhbz#658828

* Fri Feb  4 2011 Andrew Beekhof <andrew@beekhof.net> - 0.4.0-0.30.0b41287.git
- Rebuild for updated qpid-cpp
  Related: rhbz#658828

* Fri Feb  4 2011 Andrew Beekhof <andrew@beekhof.net> - 0.4.0-0.29.0b41287.git
- Update to upstream version 2798d52.git
  + Support password authentication to qpid
  + Prevent errors when matahari is started at boot
  Related: rhbz#658828

* Thu Jan 13 2011 Andrew Beekhof <andrew@beekhof.net> - 0.4.0-0.28.0b41287.git
- Refresh from upstream
- Local broker is now optional
- Functional Host, Network and Services (including support for OCF Resources) agents
  Related: rhbz#658828
 
* Tue Jan 11 2011 Andrew Beekhof <andrew@beekhof.net> - 0.4.0-0.27.ad8b81b.git
- Only build on Intel architectures for now due to qpid dependancy
  Related: rhbz#658828 

* Tue Jan 11 2011 Andrew Beekhof <andrew@beekhof.net> - 0.4.0-0.26.ad8b81b.git
- Import into RHEL

* Wed Oct 12 2010 Andrew Beekhof <andrew@beekhof.net> - 0.4.0-0.8.ad8b81b.git
- Added the Network agent
- Removed unnecessary OO-ness from existing Host agent/schema

* Fri Oct 01 2010 Adam Stokes <astokes@fedoraproject.org> - 0.4.0-0.1.5e26232.git
- Add schema-net for network api

* Tue Sep 21 2010 Andrew Beekhof <andrew@beekhof.net> - 0.4.0-0.1.9fc30e4.git
- Pre-release of the new cross platform version of Matahari
- Add matahari broker scripts

* Thu Oct 08 2009 Arjun Roy <arroy@redhat.com> - 0.0.4-7
- Refactored for new version of qpidc.

* Fri Oct 02 2009 Kevin Kofler <Kevin@tigcc.ticalc.org> - 0.0.4-6
- Rebuild for new qpidc.

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Jul 16 2009 Arjun Roy <arroy@redhat.com> - 0.0.4-4
- Changed buildroot value to meet fedora packaging guidelines
- Updated project website

* Mon Jul 13 2009 Arjun Roy <arroy@redhat.com> - 0.0.4-3
- Quietened rpmlint errors and warnings.
- Fixed most gcc warnings.
- Changed init script so it doesn't run by default
- Now rpm specfile makes it so service runs by default instead

* Thu Jul 9 2009 Arjun Roy <arroy@redhat.com> - 0.0.4-2
- Bumped qpidc and qmf version requirements to 0.5.790661.

* Thu Jul 9 2009 Arjun Roy <arroy@redhat.com> - 0.0.4-1
- Removed dependency on boost. Added dependency on pcre.

* Thu Jul 2 2009 Arjun Roy <arroy@redhat.com> - 0.0.3-2
- Fixed bug with not publishing host hypervisor and arch to broker
- Updated aclocal.m4 to match new version of automake

* Tue Jun 30 2009 Arjun Roy <arroy@redhat.com> - 0.0.3-1
- Added getopt and daemonize support
- Added sysV init script support

* Mon Jun 29 2009 Arjun Roy <arroy@redhat.com> - 0.0.2-1
- Now tracks hypervisor and arch using libvirt

* Tue Jun 23 2009 Arjun Roy <arroy@redhat.com> - 0.0.1-1
- Initial rpmspec packaging
