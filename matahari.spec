%global specversion 19
%global upstream_version 0.6.0

Name:		matahari
Version:	0.6.0
Release:	%{specversion}%{?dist}
Summary:	QMF Agents for Linux guests

Group:		Applications/System
License:	GPLv2
URL:		http://matahariproject.org

Obsoletes:  %{name}-selinux < %{version}-%{release}
Obsoletes:  %{name}-broker < %{version}-%{release}
Obsoletes:  %{name}-core < %{version}-%{release}
Obsoletes:  %{name}-lib < %{version}-%{release}
Obsoletes:  %{name}-agent-lib < %{version}-%{release}
Obsoletes:  %{name}-devel < %{version}-%{release}
Obsoletes:  %{name}-python < %{version}-%{release}
Obsoletes:  %{name}-host < %{version}-%{release}
Obsoletes:  %{name}-network < %{version}-%{release}
Obsoletes:  %{name}-rpc < %{version}-%{release}
Obsoletes:  %{name}-service < %{version}-%{release}
Obsoletes:  %{name}-sysconfig < %{version}-%{release}
Obsoletes:  %{name}-consoles < %{version}-%{release}
Obsoletes:  %{name}-shell < %{version}-%{release}
Obsoletes:  %{name}-vios-proxy-guest < %{version}-%{release}
Obsoletes:  %{name}-vios-proxy-host < %{version}-%{release}
Obsoletes:  %{name}-debuginfo < %{version}-%{release}
Obsoletes:  mingw32-matahari < 0.4.4-14
Obsoletes:  libvirt-qmf < 0.3.0-9

%description

Matahari has been removed from Enterprise Linux. This package exists only to
ensure that all Matahari-related libraries and their dependencies are removed
from the system.

Matahari provides QMF Agents that can be used to control and manage
various pieces of functionality, using the AMQP protocol

The Advanced Message Queuing Protocol (AMQP) is an open standard application
layer protocol providing reliable transport of messages

QMF provides a modeling framework layer on top of Qpid (which implements
AMQP).  This interface allows you to manage a host and its various components
as a set of objects with properties and methods

%prep

%build

%install

%files
%defattr(-, root, root, -)

%changelog
* Tue Jan 15 2013 Zane Bitter <zbitter@redhat.com> 0.6.0-19
- Add dist tag back into release
  Resolves: rhbz#894155

* Mon Jan 14 2013 Jeff Peeler <jpeeler@redhat.com> 0.6.0-18
- Bump obsoletes version for libvirt-qmf and mingw32-matahari
  Resolves: rhbz#894155

* Mon Jan 14 2013 Jeff Peeler <jpeeler@redhat.com> 0.6.0-17
- Add obsolete for debuginfo package
  Resolves: rhbz#894155

* Fri Oct 12 2012 Zane Bitter <zbitter@redhat.com> 0.6.0-16
- Add a files stanza to spec, so that an RPM will be generated
  Resolves: rhbz#833109

* Fri Sep 28 2012 Zane Bitter <zbitter@redhat.com> 0.6.0-15
- Remove Matahari and replace with an empty package.
- Also obsolete libvirt-qmf and matahari-mingw32
  Resolves: rhbz#833109

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
