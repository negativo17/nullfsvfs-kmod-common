%global real_name nullfsvfs

Name:       %{real_name}-kmod-common
Version:    0.26
Release:    1%{?dist}
Summary:    A virtual file system that behaves like /dev/null
License:    GPLv3+
URL:        https://github.com/abbbi/%{real_name}
BuildArch:  noarch

Source0:    %{url}/archive/v%{version}.tar.gz#/%{real_name}-%{version}.tar.gz

Requires:   %{real_name}-kmod = %{?epoch:%{epoch}:}%{version}
Provides:   %{real_name}-kmod-common = %{?epoch:%{epoch}:}%{version}

# Renamed from nullfs to nullfsvfs in 0.23+
Obsoletes:  nullfs-kmod-common < %{?epoch:%{epoch}:}%{version}

%description
A virtual file system that behaves like /dev/null. It can handle regular file
operations but writing to files does not store any data. The file size is
however saved, so reading from the files behaves like reading from /dev/zero
with a fixed size.

Writing and reading is basically an NOOP, so it can be used for performance
testing with applications that require directory structures.

This package contains common files.
 
%prep
%autosetup -p1 -n %{real_name}-%{version}

%files
%license LICENSE
%doc README.md

%changelog
* Sun Mar 08 2026 Simone Caronni <negativo17@gmail.com> - 0.26-1
- Rename to nullfsvfs and update to 0.26.

* Mon Feb 09 2026 Simone Caronni <negativo17@gmail.com> - 0.22-1
- Update to 0.22.

* Mon Dec 01 2025 Simone Caronni <negativo17@gmail.com> - 0.21-1
- Update to 0.21.

* Wed Jun 18 2025 Simone Caronni <negativo17@gmail.com> - 0.19-1
- Update to 0.19.

* Wed Apr 16 2025 Simone Caronni <negativo17@gmail.com> - 0.18-1
- Update to 0.18.

* Wed Nov 29 2023 Simone Caronni <negativo17@gmail.com> - 0.17-1
- First build.

