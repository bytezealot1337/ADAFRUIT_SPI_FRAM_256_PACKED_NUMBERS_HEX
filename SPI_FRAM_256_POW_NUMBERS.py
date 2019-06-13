# SPI FRAM NUMBERS - 256 Hex
import board
import busio
import digitalio
import storage
import time
import adafruit_fram

# Create SPI Bus
spi_bus = busio.SPI(board.SCK, board.MOSI, board.MISO)

# Set Up Chip-Select
spi_cs = digitalio.DigitalInOut(board.D2)
spi_cs.direction = digitalio.Direction.OUTPUT
spi_cs.value = True

# Set Up SPI FRAM
fram = adafruit_fram.FRAM_SPI(spi_bus, spi_cs, write_protect=False, wp_pin=None, baudrate=12000000) # 12MHz

byteArrayRange = len(fram) # 8192 Bytes

input_number = 999999999
print("\n---> Input Number is {} <---".format(input_number), end="\n")
outputNumber = 0

if((input_number < 0) or (input_number > 999999999)):
    print("Input Number Must be Between 0 and 999999999...", end="\n")
else:
    write_position = 0
    while(input_number > 0):
        substractor = input_number % 256
        input_number = int((input_number - substractor) / 256)
        fram[write_position] = substractor
        write_position += 1

    print("---> SPI Write to fRAM Done <---", end="\n")

    read_position = 0
    while(read_position < write_position):
        adder = fram[read_position][0]
        outputNumber += adder * pow(256, read_position)
        read_position += 1

    print("\n\"SPI fRAM\" Data \"Result\" is:", end="\n")
    print("BIN: {}".format(bin(outputNumber)), end="\n")
    #print("OCT: {}".format(oct(outputNumber)), end="\n")
    print("DEC: {}".format(outputNumber), end="\n")
    print("HEX: {}".format(hex(outputNumber)), end="\n")
# END OF SCRIPT
