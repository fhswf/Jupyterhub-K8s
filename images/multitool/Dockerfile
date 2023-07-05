FROM wbitt/network-multitool:e21fa4b

USER root

RUN setcap cap_chown,cap_fowner,cap_dac_read_search,cap_dac_override,cap_fsetid,cap_setuid,cap_setgid+ep /bin/chown
RUN setcap cap_chown,cap_fowner,cap_dac_read_search,cap_dac_override,cap_fsetid,cap_setuid,cap_setgid+ep /bin/chmod

# docker run --user 1000:100 --cap-add=CHOWN --cap-add=FOWNER --cap-add=cap_dac_override --cap-add=cap_dac_read_search --rm -it mymultitool:latest sh