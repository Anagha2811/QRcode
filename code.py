# qrcode is module for making qr code eith functions make and save 
import qrcode as qr
# as is used for using short form of qrcode that is qr
img= qr.make("https://github.com/Anagha2811")
# any info inside quotes, any url or string, the qr image is generated for it
# its my github profile
img.save("github_profile.png")
