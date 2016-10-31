//adb操作命令
adb backup [-f ] [-apk|-noapk] [-shared|-noshared] [-all] [-system|-nosystem] [<packages...>]

 - write an archive of the device's data to <file>. If no -f option is supplied then the data 
 is written to "backup.ab" in the current directory.

 (-apk|-noapk enable/disable backup of the .apks themselves in the archive; 
 the default is noapk.)
 (-shared|-noshared enable/disable backup of the device's shared storage / SD card contents; 
 the default is noshared.)
 (-all means to back up all installed applications)
 (-system|-nosystem toggles whether -all automatically includes system applications; 
 the default is to include system apps)
 (<packages...> is the list of applications to be backed up.  If the -all or -shared flags 
 are passed, then the package list is optional.  Applications explicitly given on the command 
 line will be included even if -nosystem would ordinarily cause them to be omitted.)
