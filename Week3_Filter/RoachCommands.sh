#! /usr/bin/env bash
pkill adc_snaps_2014_
pkill dig_dwn_conv_2_

mkdir -p "adc_SampleSig"
chmod 777 *

for i in {1,2,4,8}
do
	mkdir -p "adc_lo_freq_$i"
	chmod 777 *
done

sleep .5

cd /boffiles/
./adc_snaps_2014_Feb_13_2111.bof &


sleep .5

PID=`pidof ./adc_snaps_2014_Feb_13_2111.bof` #`pgrep 'adc_snaps_2014_'`
cd /proc/
#echo $PID #$$
cd $PID
cd hw/ioreg/

echo -ne "\x00\x00\x00\x01" > trig
sleep .1
echo -ne "\x00\x00\x00\x00" > trig


cp "./adc_bram" > "~/adc_SampleSig"

# Frequency 1
echo -ne "\x00\x00\x00\x01" > lo_freq

echo -ne "\x00\x00\x00\x01" > trig
sleep .1
echo -ne "\x00\x00\x00\x00" > trig

echo adc_bram > ~/lo_freq_1
echo cos_bram > ~/lo_freq_1
echo sin_bram > ~/lo_freq_1

# Frequency 2

echo -ne "\x00\x00\x00\x02" > lo_freq

echo -ne "\x00\x00\x00\x01" > trig
sleep .1
echo -ne "\x00\x00\x00\x00" > trig

echo adc_bram > ~/lo_freq_2
echo cos_bram > ~/lo_freq_2
echo sin_bram > ~/lo_freq_2

# Frequency 4

echo -ne "\x00\x00\x00\x04" > lo_freq

echo -ne "\x00\x00\x00\x01" > trig
sleep .1
echo -ne "\x00\x00\x00\x00" > trig

echo adc_bram > ~/lo_freq_4
echo cos_bram > ~/lo_freq_4
echo sin_bram > ~/lo_freq_4

# Frequency 8

echo -ne "\x00\x00\x00\x08" > lo_freq

echo -ne "\x00\x00\x00\x01" > trig
sleep .1
echo -ne "\x00\x00\x00\x00" > trig

echo adc_bram > ~/lo_freq_8
echo cos_bram > ~/lo_freq_8
echo sin_bram > ~/lo_freq_8

cd ~/
cd Samp

kill $PID
cd /boffiles/

./dig_dwn_conv_2_2014_Feb_25_1332.bof &
PID=`pidof ./dig_dwn_conv_2_2014_Feb_25_1332.bof` #`pgrep 'adc_snaps_2014_'`
cd /proc/
cd $PID
cd hw/ioreg
ls
