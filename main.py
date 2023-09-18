import subprocess
import wifi_qrcode_generator as qr

try:
    id = subprocess.check_output(['netsh', 'wlan', 'show', 'interfaces']).decode('utf-8').split('\n')
     
    id_results = str([b.split(":")[1][1:-1]
                      for b in id if "Profile" in b])[2:-3]
 
    password = subprocess.check_output(
        ['netsh', 'wlan', 'show', 'profiles',
         id_results, 'key=clear']).decode('utf-8').split('\n')
     
    pass_results = str([b.split(":")[1][1:-1]
                        for b in password if "Key Content" in b])[2:-2]
    print("Username :", id_results)
    print("Password :", pass_results)
     
except:
    print("Failed")
     
#generate qr code
qr.wifi_qrcode(id_results, False, 'WPA', pass_results)
