import qrcode as qr
img = qr.make("https://dipeshsubedi.info.np/")
img.save("dipesh.png")