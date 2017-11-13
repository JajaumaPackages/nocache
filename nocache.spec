Name:           nocache
Version:        1.0
Release:        1%{?dist}
Summary:        A wrapper tool minimizing cache effects

License:        BSD
URL:            https://github.com/Feh/nocache
Source0:        https://github.com/Feh/nocache/archive/v%{version}.tar.gz

%description
The nocache tool tries to minimize the effect an application has on the Linux
file system cache. This is done by intercepting the open and close system calls
and calling posix_fadvise with the POSIX_FADV_DONTNEED parameter.

%prep
%setup -q

%build
make CFLAGS="%{optflags}" LIBDIR="/%{_lib}" %{?_smp_mflags}

%install
rm -rf %{buildroot}
%make_install PREFIX=%{_prefix} LIBDIR="/%{_lib}"

%files
%license COPYING
%doc README
%{_bindir}/cachedel
%{_bindir}/cachestats
%{_bindir}/nocache
%{_libdir}/nocache.so
%{_mandir}/man1/cachedel.1*
%{_mandir}/man1/cachestats.1*
%{_mandir}/man1/nocache.1*

%changelog
* Mon Nov 13 2017 Jajauma's Packages <jajauma@yandex.ru> - 1.0-1
- Initial release
