## Objectives

- Articulate the roles of the following directories
    - `/`, the root directory, which contains all other files
    - `/bin`, which contains executables required for the basic function of the system
    - `/usr`, which contains user-facing files and applications
    - `/var`, which contains files whose values change frequently
    - `/tmp`, where applications can write "throwaway" data not needed between reboots
    - `/home`, which contains users' personal data
- Give representative examples of the contents of each of the following directories
    - `/bin`, which contains executables such as `grep` and `bash`
    - `/usr`, whose contents include:
      - `/usr/share/man`, which contains manpages used by `man`
      - `/usr/bin`, which contains nonessential binaries such as `cowsay` and `apt-get`
    - `/var`, whose contents include:
      - System logs in `/var/logs`
      - Temporary files required through reboots in `/var/tmp`
    - `/home`, which contains individual users' personal directories and information in, e.g., `/home/<username>/Documents`; `/home/<username>/Downloads`; etc.
- Given a file or file type, identify likely locations on the file system in which it might be found
  - E.g.: `ls` is likely to be found in `/bin` or `/usr/bin`, because it is a binary; and probably the latter, because it's user-facing