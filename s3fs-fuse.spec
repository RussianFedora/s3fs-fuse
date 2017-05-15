Summary:	FUSE file system backed by Amazon S3 bucket
Name:		s3fs-fuse
Version:	1.82
Release:	1%{?dist}

License:	GPLv2
URL:		https://github.com/s3fs-fuse/s3fs-fuse
Source0:	https://github.com/%{name}/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:	automake
BuildRequires:	pkgconfig(fuse)
BuildRequires:	pkgconfig(libcrypto)
BuildRequires:	pkgconfig(libcurl)
BuildRequires:	pkgconfig(libxml-2.0)

%description
s3fs allows Linux and Mac OS X to mount an S3 bucket via FUSE. s3fs preserves
the native object format for files, allowing use of other tools like s3cmd.

%prep
%autosetup

%build
aclocal
autoheader
automake --add-missing
autoconf

%configure
%make_build

%install
%make_install

%files
%license COPYING
%doc ChangeLog README.md
%{_bindir}/s3fs
%{_mandir}/man1/s3fs.1*

%changelog
* Mon May 15 2017 Arkady L. Shane <ashejn@russianfedora.pro> - 1.82-1
- update to 1.82

* Tue Mar 28 2017 Arkady L. Shane <ashejn@russianfedora.pro> - 1.80-1
- initial build
