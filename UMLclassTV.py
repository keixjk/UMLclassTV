# TV class definition
class TV:
# initialize TV objects
    def __init__(self):
        self.channel = 1
        self.volumeLevel = 1
        self.on = False
   
# set on to True
    def turnOn(self):
        self.on = True

# set on to False
    def turnOff(self):
        self.on = False

# return the current channel
    def getChannel(self):
        return self.channel
    
# if on is True and channel is between 1 and 120 (inclusive):
    def setChannel(self, channel):
        if self.on and 1 <= channel <= 120:
    # set the channel to the given value
            self.channel = channel

# return the current volume level
    def getVolume(self):
        return self.volumeLevel
    
# if on is True and channel is between 1 and 7 (inclusive):
    def setVolume(self, volumeLevel):
        if self.on and 1 <= volumeLevel <= 7:
    # set the volume level to the given value
            self.volumeLevel = volumeLevel

# if on is True and channel is less than 120:
    def channelUp(self):
        if set.on and self.channel < 120:
    # increment the channel by 1
            self.channel += 1

# if on is True and channel is greater than 1:
    def channelDown(self):
        if self.on and self.channel > 1:
    # decrement the channel by 1
            self.channel -= 1

# if on is True and volumeLevel is less than 7:
    def volumeUp(self):
        if self.on and self.volumeLevel < 7:
    # increment the volume level by 1
            self.volumeLevel += 1

# if on is True and volumeLevel is greater than 1:
    def volumeDown(self):
        if self.on and self.volume > 1:
    # decrement the volume level by 1
            self.volumeLevel -= 1

# TestTV Program
def main():
# Create two TV objects
    tv1 = TV()
    tv2 = TV()

# Turn on TV1 and set the channel and volume level
    tv1.turnOn()
    tv1.setChannel(30)
    tv1.setVolume(3)
# print
    print("TV1's channel is", tv1.getChannel(), "and volume level is", tv1.getVolume())

# Turn on TV2 and set the channel and volume level
    tv2.turnOn()
    tv2.setChannel(3)
    tv2.setVolume(2)
# print
    print("TV2's channel is", tv2.getChannel(), "and volume level is", tv2.getVolume())

# Run the TestTV program
if __name__ == "__main__":
    main()