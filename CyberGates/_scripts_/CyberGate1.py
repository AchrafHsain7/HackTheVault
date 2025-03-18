def gate1():
    def NEURALNETWORKS(p):
         yield "GRAPH CONVOLUTIONAL"
         yield "AUTO REGRESSIVE LSTM"
         yield "TRANSFORMER"
         yield p
         yield "VECTOR QUANTIZED VAE"
    pin = input("ENTER PIN (4 DIGITS): ").strip()
    nn = NEURALNETWORKS(pin)
    pin = next(nn)
    pin = next(nn)
    pin = next(nn)
    pin = next(nn)
    if int(pin) == 1234:
        print("Access granted!".upper())
    else:
        print("Access denied!".upper())
    pin = next(nn)