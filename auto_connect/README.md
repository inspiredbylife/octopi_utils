# Auto Connect

Automatically connect to printer when connected via USB

## Enable API access

Enable API access for the admin user by following http://docs.octoprint.org/en/master/api/general.html#authorization. If the API key is active don't regenerate the key, instead just copy it.

## Copy the script

Copy the script from github to "/home/pi/printer_auto_connect.py" file and enable the file to be executable by executing

```chmod +x /home/pi/printer_auto_connect.py```

## Edit the file and replace API key

Edit the script with your favorite text editor and replace the text `YOUR_API_KEY' with your API key copied above.

## Install urllib3

Install urllib3 python library using

```pip install urllib3```

If the above command bails out with `Requirement already satisfied (use --upgrade to upgrade): urllib3 in /usr/local/lib/python2.7/dist-packages` or similar message make sure that you have the latest version of the library using

```pip show urllib3```

We need at least version 1.10 or above. If you have a older version you can upgrade via

```pip install --upgrade urllib3```

## Add udev rule

Add below udev rule to trigger the auto connect script as soon as the printer is connected to pi. Create a file under "/etc/udev/rules.d/" directory with below contents

```SUBSYSTEM=="tty", ATTRS{idVendor}=="2974", ATTRS{idProduct}=="0503", RUN+="/home/pi/printer_auto_connect.py"```

## Reboot pi

Reboot pi for the changes to take affect. Now turn off and on the printer for it to connect automatically.
