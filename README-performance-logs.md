# Performance logging on an Ubuntu host
1. You'll need to be able to `ssh` into the host console. You do not need to be `root` but you need to be logged into the _host_, not in a container.
2. The package `sysstat` should be installed already. I checked our geocoder instance and it's there.
3. Start a logger:
    ```
    iostat 10 2>&1 | tee iostat.log
    ```
4. Execute the stuff you want to analyze ... do a database query, or access the Django API.
5. To kill the logger, type `CTRL-C`.
6. You can download the log with `scp` if you can `ssh` into the host.
7. `iostat` logs CPU and disk access but not RAM usage. To do a RAM log:
    ```
    vmstat 10 2>&1 | tee vmstat.log
    ```
    
    and execute the stuff again. `CTRL-C` stops the log and `scp` downloads.
