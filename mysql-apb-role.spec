%if 0%{?copr}
%define build_timestamp .%(date +"%Y%m%d%H%M%%S")
%else
%define build_timestamp %{nil}
%endif

Name:		mysql-apb-role
Version:	1.0.9
Release:	1%{build_timestamp}%{?dist}
Summary:	Ansible Playbook for MariaDB APB

License:	ASL 2.0
URL:		https://github.com/ansibleplaybookbundle/RHSCL-MySQL-APB
Source0:	https://github.com/ansibleplaybookbundle/RHSCL-MySQL-APB/archive/%{name}-%{version}.tar.gz
BuildArch:  	noarch


%description
%{summary}

%prep
%setup -q -n %{name}-%{version}

%install
mkdir -p %{buildroot}/opt/apb/ %{buildroot}/opt/ansible/
mv playbooks %{buildroot}/opt/apb/actions
mv roles %{buildroot}/opt/ansible/roles

%files
%doc
/opt/apb/actions
/opt/ansible/roles

%changelog
* Tue Nov 07 2017 Jason Montleon <jmontleo@redhat.com> 1.0.9-1
-  Bug 1508278 - Use include_tasks instead of include for updated Ansible
  version. (cchase@redhat.com)

* Fri Nov 03 2017 Jason Montleon <jmontleo@redhat.com> 1.0.8-1
- Bug 1508278 - Revert to using include for now for Ansible 2.3.2
  compatibility. (cchase@redhat.com)

* Fri Nov 03 2017 Jason Montleon <jmontleo@redhat.com> 1.0.7-1
- Bug 1508994 - Hide password with display_type: password (cchase@redhat.com)
- Bug 1508278 - Use include_tasks instead of include (cchase@redhat.com)

* Mon Oct 30 2017 Jason Montleon <jmontleo@redhat.com> 1.0.6-1
- Bug 1507321 - fixed binding parameters to work with mediawiki. Using the
  generic fields also allows applications to switch between different
  databases. (cchase@redhat.com)

* Thu Oct 19 2017 David Zager <david.j.zager@gmail.com> 1.0.5-1
- Bug 1503523 - Add asb module to deprovision yaml (david.j.zager@gmail.com)

* Tue Oct 10 2017 Jason Montleon <jmontleo@redhat.com> 1.0.4-1
- Update dockerfiles (david.j.zager@gmail.com)
- Bug 1500364 - Update apb.yml with all dependent images
  (david.j.zager@gmail.com)

* Mon Oct 09 2017 Jason Montleon <jmontleo@redhat.com> 1.0.3-1
- Updated mysql image to use rhscl instead of centos (dymurray@redhat.com)
- Bug 1498571 - Remove image from APB (david.j.zager@gmail.com)

* Wed Oct 04 2017 Jason Montleon <jmontleo@redhat.com> 1.0.2-1
- new package built with tito

* Wed Oct 04 2017 Jason Montleon <jmontleo@redhat.com>
- new package built with tito

* Thu Sep 28 2017 David Zager <dzager@redhat.com> 1.0.0-1
- new package built with tito

